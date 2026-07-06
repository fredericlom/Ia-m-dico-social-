# Coordination — application Windows portable

Emballe `Coordination-SAMSAH.html` (le dossier racine du dépôt) dans une
vraie application Windows : sa propre fenêtre, sa propre icône, sans barre
d'adresse ni navigateur visible. C'est un `.exe` **portable** : aucune
installation, aucun droit administrateur nécessaire — on le copie où l'on
veut (Bureau, clé USB) et on double-clique dessus.

## Récupérer le .exe déjà compilé

Le fichier `Coordination-portable.exe` est produit automatiquement par
GitHub Actions à chaque modification de l'application (voir l'onglet
**Actions** du dépôt → dernier passage de *« Compiler l'application
Windows »* → section *Artifacts* en bas de la page → télécharger
`Coordination-portable-windows.zip`, qui contient le `.exe`).

## Compiler soi-même (nécessite Windows, ou macOS/Linux + Wine)

```
cd electron
npm install
npm run build:win-portable
```

Le fichier compilé apparaît dans `electron/dist/Coordination-portable.exe`.

## Ce que fait chaque fichier

- `main.js` — ouvre la fenêtre et affiche une vraie boîte « Enregistrer
  sous » Windows quand l'application exporte un fichier (JSON, CSV, trame
  Word), pour un comportement identique à Excel/Word.
- `preparer.js` — copie `../Coordination-SAMSAH.html` dans `app/index.html`
  avant chaque lancement/compilation : le code de l'application ne vit
  qu'à un seul endroit dans le dépôt.
- `build/icone.ico` — icône de l'application.
- `package.json` — configuration d'Electron Builder (cible `portable` par
  défaut ; la cible `nsis`, un installateur classique avec raccourcis
  Bureau/menu Démarrer, est aussi configurée si besoin un jour :
  `npm run build:win-installateur`).

Vos données restent inchangées : l'application portable utilise le même
stockage local (IndexedDB) que la version ouverte dans un navigateur.
