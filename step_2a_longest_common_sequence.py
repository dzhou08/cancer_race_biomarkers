from enum import unique
import pandas as pd
import re
import numpy as np
# lcs section of code from https://www.programiz.com/dsa/longest-common-subsequence

root_drive_path = './Cancers/'

# dynamic programming function to find longest common sequence
def lcs(L1, L2, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    # Building the matrix in bottom-up way
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif L1[i-1] == L2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]

    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if L1[i-1] == L2[j-1]:
            lcs_algo[index-1] = L1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1

    # Printing the sub sequences
    return lcs_algo

if __name__ == "__main__":
    cancers = input("What are the cancers? You can use 'UCS,THCA,PRAD,LIHC,KIRP,KIRC,ESCA,BRCA,BLCA': ")
    for cancer in cancers.split(','):
        try:
            asian_data = pd.read_csv(root_drive_path + 'step1_significant_p_results/' + cancer + '_Asian_genes.csv')
            black_data = pd.read_csv(root_drive_path + 'step1_significant_p_results/' + cancer + '_Black_genes.csv')
            asian_data_gene = asian_data['Gene'].values.tolist()
            black_data_gene = black_data['Gene'].values.tolist()
            lcs_genes = lcs(asian_data_gene, black_data_gene, len(asian_data_gene), len(black_data_gene))

            lcs_column_names = ['gene',
                                    'p_value_asian',
                                    'mutation_asian',
                                    'p_value_black',
                                    'mutation_black']

            lcs_df = pd.DataFrame(columns = lcs_column_names)

            for gene in lcs_genes:
                if gene != '':
                    asian_gene_data = asian_data.loc[asian_data['Gene'] == gene]
                    black_gene_data = black_data.loc[black_data['Gene'] == gene]

                    new_df = pd.DataFrame({'gene' : gene,
                    'p_value_asian' : asian_gene_data.iloc[0]['p value Asian'],
                    'mutation_asian' : asian_gene_data.iloc[0]['mutation rates'],
                    'p_value_black' : black_gene_data.iloc[0]['p value Black'],
                    'mutation_black' : black_gene_data.iloc[0]['mutation rates']}, index = [0])

                    lcs_df = pd.concat([lcs_df,new_df], ignore_index = True, axis = 0)

            lcs_df.to_csv(root_drive_path + '/step2a_lcs_results/' + cancer + '_lcs.csv', index = False)
        except FileNotFoundError:
            print("File not found")