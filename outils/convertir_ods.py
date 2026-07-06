#!/usr/bin/env python3
"""Convertit un tableur ODS de coordination SAMSAH en fichier JSON
importable dans l'application Coordination-SAMSAH.html.

Usage :
    python3 convertir_ods.py mon_tableau.ods [sortie.json]

Le tableur attendu suit le format du « Tableau global des projets » :
ligne d'en-têtes (Nom, Prénom, Date de naissance, Âge, Référent,
Date de signature du PP, Fin de notification SAMSAH, Objectifs,
Avancement, Prochain écrit), puis une ligne par usager avec
d'éventuelles lignes supplémentaires portant les objectifs.
"""
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {
    'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
    'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
}

DOMAINES = {
    'educatif': 'Educatif', 'social': 'Social', 'sociale': 'Social',
    'soin': 'Soin', 'psychologie': 'Psychologie',
    'psychomotricité': 'Psychomotricité', 'psychomotricite': 'Psychomotricité',
    'ergothérapie': 'Ergothérapie', 'ergotherapie': 'Ergothérapie',
}


def norm(s):
    return (s or '').replace('\xa0', ' ').strip()


def lire_feuille(chemin):
    """Retourne les lignes (listes de chaînes) de la première feuille."""
    racine = ET.fromstring(zipfile.ZipFile(chemin).read('content.xml'))
    table = next(racine.iter('{%s}table' % NS['table']))
    lignes = []
    for row in table.findall('table:table-row', NS):
        cellules = []
        for cell in row:
            if cell.tag.split('}')[1] not in ('table-cell', 'covered-table-cell'):
                continue
            repet = int(cell.get('{%s}number-columns-repeated' % NS['table'], '1'))
            texte = '\n'.join(''.join(p.itertext()) for p in cell.findall('text:p', NS))
            if repet > 500:  # remplissage de fin de ligne
                repet, texte = 1, ''
            cellules.extend([texte] * repet)
        while cellules and not norm(cellules[-1]):
            cellules.pop()
        lignes.append(cellules)
    while lignes and not lignes[-1]:
        lignes.pop()
    return lignes


def parse_objectif(txt):
    """Sépare « Educatif : 1. … » en (domaine, texte)."""
    m = re.match(r'^\s*([A-Za-zÀ-ÿ]+)\s*:\s*(.*)$', txt, re.S)
    if m and m.group(1).lower() in DOMAINES:
        return DOMAINES[m.group(1).lower()], m.group(2).strip()
    return None, txt


def convertir(lignes):
    # repérer la ligne d'en-têtes (celle qui contient « Nom »)
    debut = next(i for i, l in enumerate(lignes)
                 if l and norm(l[0]).lower() == 'nom') + 1
    usagers, courant = [], None
    for l in lignes[debut:]:
        l = [norm(c) for c in l] + [''] * (10 - len(l))
        if l[0]:
            courant = {
                'id': len(usagers) + 1,
                'nom': l[0], 'prenom': l[1], 'naissance': l[2],
                'referent': l[4], 'signaturePP': l[5],
                'finNotification': l[6], 'prochainEcrit': l[9],
                'note': '', 'objectifs': [],
            }
            usagers.append(courant)
        if courant is None:
            continue
        if l[7]:
            domaine, texte = parse_objectif(l[7])
            if domaine is None and not courant['objectifs']:
                courant['note'] = texte  # « Période d'observation en cours »…
            else:
                courant['objectifs'].append({
                    'domaine': domaine or 'Autre',
                    'texte': re.sub(r'\s*\n\s*', '\n', texte),
                    'statut': l[8] or 'En cours',
                })
        elif l[8] and courant['objectifs']:
            courant['objectifs'][-1]['statut'] = l[8]
    return usagers


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    entree = sys.argv[1]
    sortie = sys.argv[2] if len(sys.argv) > 2 else 'donnees-samsah.json'
    usagers = convertir(lire_feuille(entree))
    donnees = {'titre': 'Tableau global des projets — SAMSAH', 'usagers': usagers}
    with open(sortie, 'w', encoding='utf-8') as f:
        json.dump(donnees, f, ensure_ascii=False, indent=1)
    print(f'{len(usagers)} usagers convertis → {sortie}')
    print("Dans l'application : bouton « Importer » puis choisir ce fichier.")


if __name__ == '__main__':
    main()
