# Coordination SAMSAH — application locale

Application locale de suivi des projets personnalisés (usagers, référents,
échéances de notification, objectifs par domaine), pensée pour remplacer le
tableur Excel/LibreOffice de coordination par un outil plus fluide.

**Aucune installation, aucun serveur, aucun internet** : tout tient dans un
seul fichier, `Coordination-SAMSAH.html`.

## Démarrage

1. Copier `Coordination-SAMSAH.html` n'importe où sur l'ordinateur
   (Bureau, Documents, clé USB…).
2. Double-cliquer dessus : il s'ouvre dans le navigateur (Edge, Chrome,
   Firefox…), même sans connexion internet.
3. Les modifications sont **enregistrées automatiquement** dans le
   navigateur de ce poste.

> ⚠️ Le fichier du dépôt contient uniquement des données d'exemple.
> Les données réelles ne sont jamais publiées sur GitHub : elles restent
> sur le poste de travail (voir « Vos données » ci-dessous).

## Fonctionnalités

- **Recherche instantanée** sur les noms, référents, objectifs, notes.
- **Tri** par clic sur les en-têtes de colonnes ; **filtre par référent**.
- **Alertes automatiques** : notifications échues (rouge) et échéances à
  moins de 6 mois (orange), avec compteurs cliquables en haut de page.
- **Fiche usager dépliable** : objectifs groupés par domaine
  (Éducatif, Social, Soin, Psychologie, Psychomotricité, Ergothérapie)
  avec leur avancement.
- **Édition complète** : ajout/modification/suppression d'usagers et
  d'objectifs, calcul automatique de l'âge.
- **Sauvegarde JSON** (copie de secours), **import JSON**,
  **export CSV** compatible Excel, **impression**.
- Thèmes clair et sombre (suit le réglage de Windows).

## Vos données

- Les données vivent dans le navigateur du poste (localStorage) et dans
  les fichiers JSON que vous exportez. Rien ne part sur internet.
- Pensez à faire régulièrement **💾 Sauvegarder (JSON)** pour garder une
  copie de secours (le fichier se télécharge ; rangez-le dans un dossier
  sécurisé conforme aux règles RGPD de votre service).
- Pour travailler sur un autre poste : exportez le JSON, puis
  **📂 Importer** sur l'autre poste.

## Reprendre les données d'un tableur ODS existant

```
python3 outils/convertir_ods.py "Tableau_coordo.ods" donnees.json
```

puis, dans l'application, bouton **📂 Importer** et choisir `donnees.json`.

## Et si on veut un « vrai » .exe Windows ?

Le fichier HTML couvre déjà l'usage quotidien. Si un exécutable installable
devient nécessaire (icône dédiée, fenêtre sans navigateur), le même code
peut être empaqueté tel quel avec [Tauri](https://tauri.app) ou
[Electron](https://www.electronjs.org) — à demander comme évolution.
