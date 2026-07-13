# Site vitrine — LOMONGIELLO Frédéric

Site web professionnel de l'organisation, destiné notamment à :

- renseigner le champ **« Site Web de l'organisation »** de la Google Play Console ;
- fournir l'URL de **politique de confidentialité** exigée pour publier une application ;
- présenter l'activité et les logiciels de l'éditeur.

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | Page d'accueil (présentation, solution, contact) |
| `confidentialite.html` | Politique de confidentialité (obligatoire Google Play) |
| `mentions-legales.html` | Mentions légales (obligatoire en France) |
| `assets/style.css` | Feuille de style commune |
| `.nojekyll` | Empêche GitHub Pages de filtrer les fichiers |

Le site est **statique** (HTML/CSS uniquement), sans dépendance externe, responsive et compatible thème clair/sombre.

## Mettre le site en ligne (gratuit, GitHub Pages)

1. Fusionnez ce dossier `docs/` sur la branche **`main`**.
2. Sur GitHub : **Settings → Pages**.
3. Dans **Build and deployment → Source**, choisissez **GitHub Actions**
   (le workflow `.github/workflows/deploy-site.yml` publie automatiquement le dossier `docs/`).
4. L'URL publique sera de la forme :
   `https://<votre-compte>.github.io/ia-m-dico-social-/`

Cette URL peut être collée dès maintenant dans la Google Play Console, puis
validée via la Google Search Console.

## Brancher votre nom de domaine (plus tard)

Quand vous aurez acheté un domaine (ex. `exemple.fr`) :

1. Ajoutez un fichier `docs/CNAME` contenant uniquement votre domaine, ex. :
   ```
   www.exemple.fr
   ```
2. Chez votre registrar, créez les enregistrements DNS pointant vers GitHub Pages :
   - un `CNAME` de `www` vers `<votre-compte>.github.io`
   - (pour le domaine racine) des enregistrements `A` vers les IP de GitHub Pages.
3. Dans **Settings → Pages → Custom domain**, saisissez votre domaine et activez
   **Enforce HTTPS**.

## À personnaliser

- Adresse e-mail de contact (`lom@dgh974.fr`) dans les 3 pages si besoin.
- Numéros d'immatriculation (SIREN/SIRET, TVA) dans `mentions-legales.html`.
- Numéro de téléphone, si vous souhaitez l'afficher.
