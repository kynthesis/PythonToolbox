# format: filename.wav|speaker_number
import random

input_file = open(f'transcriptAll.txt')
readlines = input_file.readlines()

writelines = []

speakers = dict()

for line in readlines:
    elemements = line.split('|')
    filename = elemements[0]
    speaker = elemements[2]
    print(filename + '|' + speaker)

    if speaker in speakers:
        speakers[speaker] += 1
    else:
        speakers[speaker] = 0

print(speakers)

# random.shuffle(writelines)

# output_file = open(f'train_list.txt', 'w')
# output_file.writelines(writelines)
# output_file.close()
