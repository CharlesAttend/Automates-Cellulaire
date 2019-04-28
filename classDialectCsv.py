# -*- coding: utf-8 -*-

################################################################################

import csv

################################################################################

        #CLASS dialect, pour épurer le CSV
class Dialect(csv.Dialect):
    # Séparateur de champ
    delimiter = ","
    # Séparateur de ''chaîne''
    quotechar = None
    # Gestion du séparateur dans les ''chaînes''
    escapechar = None
    doublequote = None
    # Fin de ligne
    lineterminator = "\r\n"
    # Ajout automatique du séparateur de chaîne (pour ''writer'')
    quoting = csv.QUOTE_NONE
    # Ne pas ignorer les espaces entre le délimiteur de chaîne
    # et le texte
    skipinitialspace = False