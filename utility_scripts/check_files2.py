# performs basic checks on the DB, and builds a CSV file ...

import os
import logging
import csv
import glob
from util_functions import *




logging.basicConfig(format='%(levelname)s:\t%(asctime)s:\t%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


folder = r"C:\Users\u7151703\Desktop\research\datasets\processing\nex\datasets" # prettier    
logging.info("Checking %s" %folder)
    
# 1. Check that the two files exist, at least in principle (maybe they're empty)
files = os.listdir(folder)
if files.count("README.yaml") != 1: 
    logging.error("couldn't find a YAML file for %s" %folder)
    raise ValueError
logging.info("    found YAML file")

if files.count("alignment.nex") != 1:
    logging.error("couldn't find alignment.nex file for %s" %folder)
    raise ValueError

logging.info("    found alignment.nex file")

# clean up the folder: remove all files except the two we want
extras = set(files) - set(['alignment.nex', 'README.yaml', 'alignment.nex-seq-summary.txt', 'alignment.nex-summary.txt'])
if extras:
    logging.info("    removing %d additional file(s)", len(extras))
    for f in extras:
        logging.info("        %s" %(f))
        os.remove(os.path.join(folder, f))
                
# 2. parse the yaml file
logging.info("    checking YAML file")
yaml_file = os.path.join(folder, "README.yaml")
check_yaml(yaml_file)

# 3. check the alignment file
logging.info("    checking alignment.nex file")

alignment_file = os.path.join(folder, "alignment.nex")
aln = check_alignment(alignment_file)

logging.info("    done, no errors found")

#logging.info("Database contains %d datasets" % ( len(dataset_folders)))
#logging.info("All datasets checked and no errors detected")