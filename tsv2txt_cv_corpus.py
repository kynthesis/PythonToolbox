import csv

tsv_file = open('validated.tsv')

read_tsv = csv.reader(tsv_file, delimiter='\t')

count = 0

speakers = dict()

for row in read_tsv:
    speaker = row[0]
    if speaker in speakers:
        speakers[speaker] += 1
    else:
        speakers[speaker] = 0

print(speakers.values)
print(len(speakers))