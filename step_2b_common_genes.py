from enum import unique
import pandas as pd
import re
import numpy as np

root_drive_path = './Cancers/'

cancers = input("What are the cancers? (All uppercase) You can use 'UCS,THCA,PRAD,LIHC,KIRP,KIRC,ESCA,BRCA,BLCA': ")
cancers = cancers.split(",")

column_names = ['cancer',
                'unique_asian_genes',
                'common_genes',
                'unique_black_genes']
                
gene_df = pd.DataFrame(columns = column_names)

for cancer in cancers:
    print(cancer)
    asian_data = pd.read_csv(root_drive_path + 'step1_significant_p_results/' + cancer + '_Asian_genes.csv')
    black_data = pd.read_csv(root_drive_path + 'step1_significant_p_results/' + cancer + '_Black_genes.csv')
    common_data = asian_data.merge(black_data, on = ['Gene'])
    common_genes = common_data['Gene'].tolist()
    unique_asian_genes = list(set(asian_data['Gene'].tolist()) - set(common_genes))
    unique_black_genes = list(set(black_data['Gene'].tolist()) - set(common_genes))

    gene_new_df = pd.DataFrame({'cancer': cancer, 
                                'unique_asian_genes' : ', '.join(unique_asian_genes),
                                'common_genes' : ', '.join(common_genes), 
                                'unique_black_genes' : ', '.join(unique_black_genes)}, 
                                index = [0])

    gene_df = pd.concat([gene_df,gene_new_df], ignore_index = True, axis = 0)

output_file_name = root_drive_path + 'step2b_common_genes_results/gene_list.csv'
gene_df.to_csv(output_file_name, index = False)
print(f'Write into {output_file_name}')