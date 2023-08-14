# a little script to concatenate lots of nexus files in a folder
# and write a new one.
# cd to the infile before running

from Bio.Nexus import Nexus
#from Bio import AlignIO
import os

infile = r"C:\Users\u7151703\Desktop\research\datasets\Sanchez-Baracaldo_2017\nex"

file_list = [x for x in os.walk(infile)][0][2]
print(file_list)
full_file_list = [[x, os.path.join(infile, x)] for x in file_list]

#try:
#	file_list.remove(".DS_Store") # thanks Mac
#except:
#	pass

print("loading files")
nexi =  [(fname[0], Nexus.Nexus(fname[1])) for fname in full_file_list]

print("combining alignments")
combined = Nexus.combine(nexi)

print("writing output")
outfile = os.path.join(infile, "alignment.nex")
outfile = open(outfile, 'w')
combined.write_nexus_data(outfile)
outfile.close()