# convert a file full of alignments to nexus format
# just change the input format in the loop as appropriate
# and the alphabet

import os
import shutil

infile  = r"C:\Users\u7151703\Desktop\research\datasets\Sanchez-Baracaldo_2017"
outdir = r"C:\Users\u7151703\Desktop\research\datasets\Sanchez-Baracaldo_2017\nex\\"
rootdir = "C:\\Users\\u7151703\\"

nex_dir = os.path.join(infile, "nex")
if not os.path.isdir(nex_dir):
    os.makedirs(nex_dir)

file_list = [x for x in os.walk(infile)][0][2]



for f in file_list:
    cmd = r'python C:\Users\u7151703\Desktop\research\code\BenchmarkAlignments\utility_scripts\AMAS.py convert -d aa -f phylip -i '+ infile + '\\' + f +' -u nexus'
    os.system(cmd)
    fnex = f + '-out.nex'
    
    shutil.move(rootdir + fnex, outdir +fnex)
    
    lowercase_lines = []

    with open(outdir+fnex, 'r') as file:
        for line in file:
            if line == '':
                continue
            elif 'BEGIN DATA;' in line:
                lowercase_lines.append('begin DATA;')
            elif 'DIMENSIONS ' in line:
                lowercase_lines.append(line.lower())
            elif 'FORMAT DATATYPE' in line:
                lowercase_lines.append(line.lower())
            elif 'MATRIX' in line:
                lowercase_lines.append(line.lower())
            elif 'END;' in line:
                lowercase_lines.append(line.lower())
            else:
                lowercase_lines.append(line)
    
    
    with open(outdir+fnex, 'w') as file:
        file.writelines(lowercase_lines)
