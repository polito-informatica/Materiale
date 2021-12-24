FILENAME = '14BHDLZ_2022_shuffled.csv'
# nota: i nomi non corrispondono a studenti reali, in quanto matricole, nomi
# e cognomi sono stati rimescolati in ordine casuale

file = open(FILENAME, 'r')

studenti = []
prima = True

for line in file:
    if not prima:
        record = line.rstrip().split(',')
        studenti.append({
            'matricola': int(record[0]),
            'cognome': record[1],
            'nome': record[2]
        })
    else:
        prima = False # la prima linea contiene i nomi dei campi
file.close()


# Lettura come dizionario
import csv

file = open(FILENAME, 'r')
reader = csv.DictReader(file)

studenti = []
for record in reader:
    studenti.append(record)
file.close()
