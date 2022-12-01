# format: filename.wav|speaker_number
import random

input_file = open('prompts.txt')
readlines = input_file.readlines()

writelines = []

for line in readlines:
    filename = line.split(' ')[0]
    text = './vivos/train/waves/' + filename[:10] + '/' + filename + '.wav|' + str(int(filename[8:10])) + '\n'
    writelines.append(text)

random.shuffle(writelines)

output_file = open('train_list.txt', 'w')
output_file.writelines(writelines)
output_file.close()