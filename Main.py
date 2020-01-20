import csv
from IHM import *


def main():
    listColumns = []
    with open('panorama-des-festivals.csv', encoding="utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            listColumns.append(Manifestation(row['Nom de la manifestation'],
                                             row['Code postal'],
                                             row['Site web'],
                                             row['Commune principale'],
                                             [
                                                 row['Date de début'],
                                                 row['Date de fin']
                                             ],
                                             Domaines(row['Domaine'],
                                                      row['Complément domaine'])))
        csv_file.close()
    root = Tk()
    window = IHM(listColumns, root)
    window.init_window()


main()
