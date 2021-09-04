import os
import csv


file_to_save = os.path.join('Resources','election_analysis.txt')

#outfile = open(file_to_save, 'w')
#outfile.write('Hello world')
#outfile.close()

with open(file_to_save,'w') as txt_file:
    #txt_file.write('Hello people')
    txt_file.write("Arapahoe")
    txt_file.write("Denver")
    txt_file.write("Jefferson")
