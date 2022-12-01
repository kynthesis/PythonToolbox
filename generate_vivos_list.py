# format: filename.wav|speaker_number
import random

mode = 'train'

input_file = open(f'{mode}_prompts.txt')
readlines = input_file.readlines()

writelines = []
writelines2 = []

d = {'1': 0, '2': 0, '27': 0, '29': 0}

for line in readlines:
    filename = line.split(' ')[0]
    speaker_num = int(filename[8:10])

    if (speaker_num not in [1, 2, 27, 29]):
        continue
    if (d[str(speaker_num)] >= 200):
        continue

    text = f'./vivos/waves/' + filename[:10] + '/' + filename + '.wav|' + str(int(filename[8:10])) + '\n'
    
    if (d[str(speaker_num)] >= 180):
        writelines2.append(text)
    else:
        writelines.append(text)

    d[str(speaker_num)] += 1

random.shuffle(writelines)

output_file = open(f'train_list.txt', 'w')
output_file.writelines(writelines)
output_file.close()

random.shuffle(writelines2)

output_file = open(f'val_list.txt', 'w')
output_file.writelines(writelines2)
output_file.close()

print(d)