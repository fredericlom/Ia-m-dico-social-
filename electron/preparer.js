// Copie le fichier HTML source (racine du dépôt) dans electron/app/index.html
// avant chaque lancement ou compilation, pour n'avoir qu'une seule source de vérité.
const fs = require('fs');
const path = require('path');

const source = path.join(__dirname, '..', 'Coordination-SAMSAH.html');
const dossier = path.join(__dirname, 'app');
const destination = path.join(dossier, 'index.html');

fs.mkdirSync(dossier, { recursive: true });
fs.copyFileSync(source, destination);
console.log('Copié :', source, '→', destination);
