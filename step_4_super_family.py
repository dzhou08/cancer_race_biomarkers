from enum import unique
from operator import itemgetter
import pandas as pd
import re
import numpy as np
import itertools as it
import csv

root_drive_path = './Cancers/'

for cancer in ['UCS','THCA','PRAD','LIHC','KIRP','KIRC','ESCA','BRCA','BLCA']:
    # iterate for different races
    for race in ['Asian','Black']:
        geneSuperfamilyDict = {}
        # initialization: for each the superfamily, set gene count equal to 0
        with open(root_drive_path + 'step4_cdsearch_files/' + cancer + '_' + race + '.txt') as superfamily_file:
            for line in superfamily_file:
                if line[:2] == "Q#":
                    superfamily = line.split()[9]
                    geneSuperfamilyDict[superfamily] = 0
        # read the file again and calculate the superfamily gene count numbers
        with open(root_drive_path + 'step4_cdsearch_files/' + cancer + "_" + race + ".txt") as superfamily_file:
            for line in superfamily_file:
                if line[:2] == "Q#":
                    superFamily = line.split()[9]
                    geneSuperfamilyDict[superFamily] += 1

        # sort the superfamily dictionary with descending order of gene count numbers
        sorted_dict = sorted(geneSuperfamilyDict.items(), key=lambda x:x[1], reverse = True)

        # output the superfamily and count of genes
        fields = ['Superfamily', 'Count of Genes']
        rows = sorted_dict
        with open(root_drive_path + '/step4_superfamily_results/' + cancer + '_' + race+ '_count_of_genes_in_superfamily.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(fields)
            write.writerows(rows)