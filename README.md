# Coordination SAMSAH — application locale complète

Application de travail du coordinateur d'un SAMSAH : usagers, projets
personnalisés, échéancier automatique, journal d'accompagnement, liste
d'attente, écrits et statistiques. Pensée pour remplacer définitivement le
tableur Excel/LibreOffice.

**Aucune installation, aucun serveur, aucun internet** : tout tient dans un
seul fichier, `Coordination-SAMSAH.html` — à copier n'importe où (Bureau,
clé USB, lecteur réseau) et à ouvrir d'un double-clic.

> ⚠️ Le fichier du dépôt contient uniquement des données d'exemple fictives.
> Les données réelles ne sont jamais publiées sur GitHub.

## Les 7 onglets

| Onglet | Ce qu'il fait |
|---|---|
| 🏠 **Tableau de bord** | Compteurs (file active, taux d'occupation, entrées/sorties), « À faire cette semaine » cochable, alertes cliquables, charge par référent |
| 👥 **Usagers** | Dossier complet : identité, MDPH (notification, renouvellement), protection, entourage, équipe par domaine, partenaires, projet personnalisé avec objectifs par domaine et archives, notes horodatées |
| 📅 **Échéancier** | Échéances **générées automatiquement** (rappels MDPH à 6 et 3 mois, bilans intermédiaires à +6 mois, renouvellements de PP à +1 an, fins d'observation) + échéances manuelles ; vue liste et vue calendrier |
| 📓 **Journal** | Saisie d'une intervention en quelques secondes (VAD, entretien, appel…), historique filtrable, totaux d'heures |
| ⏳ **Liste d'attente** | Candidatures et priorités, admission en un clic vers la file active |
| 📝 **Écrits** | Suivi demandé → en cours → transmis → validé, **génération de trames Word pré-remplies** (bilan, renouvellement, note de situation) |
| 📈 **Statistiques** | Âges, déficiences, référents, mouvements sur 5 ans, motifs de sortie, durée moyenne d'accompagnement — chaque tableau exportable en CSV |

## Transversal

- **Recherche globale instantanée** depuis n'importe quel onglet.
- **Ctrl+Z** : annule la dernière action (30 niveaux).
- **Code d'accès optionnel** : données chiffrées sur le poste (AES-256,
  clé dérivée du code) et code demandé à chaque ouverture.
  ⚠️ code perdu = données irrécupérables — gardez un export JSON en lieu sûr.
- **Copies de secours automatiques** : une par jour, 10 conservées,
  restaurables depuis le menu ⚙️ Données.
- Export JSON complet, export CSV Excel de chaque vue, impression,
  thèmes clair/sombre.

## Vos données

- Enregistrement automatique sur le poste (IndexedDB du navigateur).
  Rien ne part sur internet.
- L'application **récupère automatiquement** les données saisies dans la V1
  au premier lancement, et le menu Importer accepte les fichiers JSON V1 et V2.
- Pour changer de poste : ⚙️ Données → Exporter, puis Importer sur l'autre poste.

## Reprendre un tableur ODS existant

```
python3 outils/convertir_ods.py "Tableau_coordo.ods" donnees.json
```
puis ⚙️ Données → **Importer un fichier JSON**.

## Développement

Le fichier livré est assemblé à partir de fragments (CSS, HTML, noyau,
vues, actions) et testé de bout en bout avec Playwright (30 scénarios :
CRUD usagers, échéances automatiques, chiffrement, migration V1,
imports/exports, Ctrl+Z…). Un empaquetage `.exe` (Tauri/Electron) reste
possible sans modifier le code.
