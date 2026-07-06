# Plan de la version complète — « Coordination SAMSAH »

Outil de travail quotidien du coordinateur d'un SAMSAH (toutes déficiences et
TSA). Objectif : remplacer définitivement le tableur par une application
locale plus fluide, plus fiable et pensée pour le métier.

**Principes non négociables**
- 100 % local : aucune donnée ne part sur internet, aucun compte, aucun abonnement.
- Zéro installation : un fichier à double-cliquer (empaquetable en .exe plus tard).
- Chaque écran doit être plus rapide que l'équivalent Excel : recherche
  instantanée, saisie en 2 clics maximum, alertes calculées automatiquement.

---

## Module 1 — Tableau de bord (écran d'accueil)

- Compteurs : file active, capacité de l'agrément et taux d'occupation,
  entrées/sorties du mois, personnes en période d'observation.
- **« À faire » de la semaine** : écrits à rendre, synthèses prévues,
  échéances proches — triés par urgence, cochables.
- Alertes automatiques, cliquables pour voir les personnes concernées :
  - notification MDPH échue / à moins de 6 mois / à moins de 3 mois
    (rappel pour le dépôt de renouvellement) ;
  - bilan intermédiaire dû (6 mois après signature du PP) ;
  - renouvellement du PP dû (1 an après signature) ;
  - période d'observation dépassant la durée prévue ;
  - PP non signé plus de X jours après l'admission.
- Charge par référent : nombre d'usagers suivis par chaque professionnel.

## Module 2 — Dossier usager complet

- **Identité** : nom, prénom, date de naissance (âge automatique), sexe,
  adresse, téléphones, email.
- **Entourage** : aidants et contacts d'urgence ; mesure de protection
  (tutelle/curatelle, mandataire et ses coordonnées).
- **Administratif MDPH** : numéro de dossier, notification en cours
  (début/fin), type de déficience (TSA / autre), renouvellement déposé
  (oui/non, date de dépôt).
- **Parcours** : date d'admission, période d'observation, statut
  (liste d'attente → observation → actif → fin d'accompagnement → sorti),
  motif de sortie.
- **Équipe autour de la personne** : référent principal + intervenants par
  domaine (éducatif, social, soin, psychologie, psychomotricité, ergothérapie).
- **Partenaires** : médecin traitant, CMP, ESAT/employeur, autres services.
- **Notes horodatées** au fil de l'accompagnement.

## Module 3 — Projet personnalisé (PP)

- Dates de signature, avenants, prochain bilan et renouvellement
  **calculés automatiquement**.
- Attentes exprimées par la personne (ses mots à elle).
- Objectifs par domaine ; chaque objectif porte : intitulé, moyens/actions,
  statut (à démarrer / en cours / atteint / partiellement atteint /
  abandonné), échéance, professionnel responsable.
- **Historique** : chaque renouvellement archive la version précédente du PP,
  consultable à tout moment.

## Module 4 — Échéancier et calendrier

- Vue calendrier mensuelle + liste chronologique « tout ce qui arrive ».
- Échéances générées automatiquement depuis les dossiers (notifications,
  bilans, renouvellements, fins d'observation) + échéances manuelles
  (rendez-vous, écrits demandés, synthèses).
- Chaque échéance : responsable, statut fait/à faire, report possible.

## Module 5 — Journal d'accompagnement

- Saisie d'une intervention en quelques secondes : date, usager,
  professionnel, type (VAD, entretien, accompagnement extérieur, appel,
  synthèse, coordination partenaire), durée, note libre.
- Historique filtrable par personne, professionnel, type, période.
- Totaux automatiques (nombre d'actes, heures) réutilisés par le module 8.

## Module 6 — Liste d'attente

- Candidatures : date de réception, notification MDPH, contacts effectués,
  priorité, décision de la commission d'admission.
- Admission en un clic : la candidature devient un dossier actif sans resaisie.

## Module 7 — Écrits et documents

- Trames pré-remplies avec les données du dossier : bilan intermédiaire,
  renouvellement de PP, note de situation — export Word et impression PDF.
- Suivi de chaque écrit : demandé → en cours → transmis → validé,
  relié à l'échéancier.

## Module 8 — Statistiques et rapport d'activité

- Indicateurs annuels prêts pour le rapport d'activité : pyramide des âges,
  répartition par déficience et par référent, durée moyenne
  d'accompagnement, entrées/sorties et motifs, taux d'occupation.
- Export CSV/Excel de chaque indicateur.

## Module 9 — Recherche et confort d'utilisation

- Recherche globale instantanée depuis n'importe quel écran.
- Filtres croisés (référent + statut + alerte…), tri sur toutes les colonnes.
- Annulation de la dernière action (Ctrl+Z), raccourcis clavier.
- Impression propre de chaque vue ; thème clair/sombre ; taille de texte
  réglable (accessibilité).

## Module 10 — Données, sécurité, RGPD

- Sauvegarde dans un **vrai fichier de données** choisi par l'utilisateur
  (clé USB ou lecteur réseau du service possible) + copies de secours
  automatiques horodatées.
- Code d'accès demandé à l'ouverture, données chiffrées dans le fichier.
- Import : ancien tableur ODS (outil fourni), CSV, JSON.
  Export : JSON complet, CSV par vue.
- Journal des modifications (quoi, quand) pour retrouver une erreur de saisie.
- Aucune donnée nominative dans le dépôt GitHub : le code est public-able,
  les données restent au service.

---

## Ordre de construction proposé

| Étape | Contenu | Statut |
|---|---|---|
| V1 | Tableau des usagers, objectifs par domaine, alertes de notification, import ODS, export JSON/CSV | ✅ livrée |
| V2 | Dossier usager complet, PP enrichi avec historique, échéancier automatique, sauvegarde fichier + code d'accès | ✅ livrée |
| V3 | Tableau de bord « À faire », journal d'accompagnement, liste d'attente | ✅ livrée |
| V4 | Trames d'écrits Word/PDF, calendrier, statistiques et rapport d'activité | ✅ livrée |

Technique : fichier HTML autonome (IndexedDB + accès fichier), sans
dépendance réseau ; empaquetage Tauri en `.exe` possible en fin de parcours.

---

## Prompt de construction

> Voir la fin du fichier : prompt prêt à copier pour lancer la fabrication
> de la version complète, étape par étape.

```
Construis « Coordination SAMSAH », une application 100 % locale pour le
coordinateur d'un SAMSAH (toutes déficiences et TSA), en repartant du
fichier Coordination-SAMSAH.html existant (V1) du dépôt.

CONTRAINTES TECHNIQUES
- Un seul fichier HTML autonome (HTML/CSS/JS vanilla, aucune dépendance
  réseau, aucun serveur) ; interface entièrement en français ; thèmes
  clair/sombre ; impression propre de chaque vue.
- Données : IndexedDB avec sauvegarde/chargement dans un fichier choisi
  par l'utilisateur (File System Access API, avec repli téléchargement),
  copies de secours automatiques horodatées, code d'accès à l'ouverture
  avec chiffrement (WebCrypto, AES-GCM dérivé du code par PBKDF2).
- Compatibilité : import du JSON de la V1 sans perte, import CSV,
  export JSON complet et CSV par vue.

MODULES À CONSTRUIRE (dans cet ordre)
1. Dossier usager complet : identité, entourage et mesure de protection,
   administratif MDPH (numéro, notification début/fin, renouvellement
   déposé), parcours (admission, observation, statut, motif de sortie),
   équipe par domaine, partenaires, notes horodatées.
2. Projet personnalisé : attentes de la personne, objectifs par domaine
   (intitulé, moyens, statut, échéance, responsable), dates de signature
   et avenants, bilan intermédiaire (+6 mois) et renouvellement (+1 an)
   calculés automatiquement, archivage des versions précédentes.
3. Échéancier : échéances générées automatiquement (notifications MDPH
   avec rappels à 6 et 3 mois, bilans, renouvellements, fins
   d'observation) + échéances manuelles ; vue liste et vue calendrier
   mensuel ; statut fait/à faire, responsable, report.
4. Tableau de bord : compteurs (file active, taux d'occupation,
   entrées/sorties, observations), « À faire cette semaine » cochable,
   alertes cliquables, charge par référent.
5. Journal d'accompagnement : saisie rapide (date, usager, professionnel,
   type VAD/entretien/accompagnement/appel/synthèse/coordination, durée,
   note), historique filtrable, totaux par usager et par professionnel.
6. Liste d'attente : candidatures (réception, notification, priorité,
   contacts, décision), admission en un clic vers la file active.
7. Écrits : trames pré-remplies (bilan intermédiaire, renouvellement PP,
   note de situation) exportables en Word (.doc HTML) et imprimables ;
   suivi demandé/en cours/transmis/validé relié à l'échéancier.
8. Statistiques : pyramide des âges, répartitions par déficience et
   référent, durées d'accompagnement, entrées/sorties et motifs, taux
   d'occupation ; export CSV de chaque tableau.

EXIGENCES D'ERGONOMIE
- Recherche globale instantanée accessible de partout ; filtres croisés ;
  tri sur toutes les colonnes ; Ctrl+Z sur la dernière action ;
  navigation par onglets (Tableau de bord / Usagers / Échéancier /
  Journal / Liste d'attente / Écrits / Statistiques).
- Toute saisie courante en 2 clics maximum depuis le tableau de bord.
- Aucune donnée réelle dans le code : données d'exemple fictives
  uniquement ; conserver l'outil d'import ODS existant.

MÉTHODE
- Livrer module par module, chaque étape testée (navigateur headless)
  avant de passer à la suivante ; à chaque livraison, mettre à jour la
  démo avec données fictives et fournir le fichier prêt à l'emploi.
```
