const { app, BrowserWindow, Menu, shell, dialog, session } = require('electron');
const path = require('path');

// Une seule fenêtre à la fois (les données vivent dans le profil Electron du poste)
const verrou = app.requestSingleInstanceLock();
if (!verrou) {
  app.quit();
} else {
  let fenetre;

  app.on('second-instance', () => {
    if (fenetre) {
      if (fenetre.isMinimized()) fenetre.restore();
      fenetre.focus();
    }
  });

  function creerFenetre() {
    fenetre = new BrowserWindow({
      width: 1400,
      height: 900,
      minWidth: 900,
      minHeight: 600,
      title: 'Coordination',
      icon: path.join(__dirname, 'build', 'icone.png'),
      autoHideMenuBar: true,
      backgroundColor: '#12161d',
      webPreferences: {
        contextIsolation: true,
        nodeIntegration: false,
        spellcheck: false,
      },
    });

    fenetre.loadFile(path.join(__dirname, 'app', 'index.html'));

    // les liens externes (aucun normalement) s'ouvrent dans le navigateur, pas dans l'appli
    fenetre.webContents.setWindowOpenHandler(({ url }) => {
      shell.openExternal(url);
      return { action: 'deny' };
    });
  }

  // Ctrl+P (impression) et Ctrl+Z (annulation) déjà gérés par la page elle-même ;
  // on garde un menu minimal pour Windows (barre masquée par défaut, accessible via Alt).
  const modele = [
    {
      label: 'Fichier',
      submenu: [{ role: 'quit', label: 'Quitter' }],
    },
    {
      label: 'Affichage',
      submenu: [
        { role: 'reload', label: 'Recharger' },
        { role: 'resetZoom', label: 'Taille normale' },
        { role: 'zoomIn', label: 'Agrandir le texte' },
        { role: 'zoomOut', label: 'Réduire le texte' },
        { type: 'separator' },
        { role: 'togglefullscreen', label: 'Plein écran' },
      ],
    },
  ];
  Menu.setApplicationMenu(Menu.buildFromTemplate(modele));

  // Les exports de l'application (JSON, CSV, trames Word) déclenchent un
  // vrai « Enregistrer sous » Windows, comme dans Excel ou Word.
  function activerEnregistrerSous() {
    session.defaultSession.on('will-download', (evenement, item) => {
      const chemin = dialog.showSaveDialogSync(fenetre, {
        title: 'Enregistrer sous',
        defaultPath: item.getFilename(),
      });
      if (chemin) item.setSavePath(chemin);
      else item.cancel();
    });
  }

  app.whenReady().then(() => {
    activerEnregistrerSous();
    creerFenetre();
  });

  app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
  });

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) creerFenetre();
  });
}
