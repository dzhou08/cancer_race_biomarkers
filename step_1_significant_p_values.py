def read_race_gene_file(cancer,race):
    try:
        file_name = root_drive_path + 'Judy_MutationRate_Files/' + cancer + '_' + race + '_Vs_White.csv'
        data = pd.read_csv(file_name, index_col = 0)

        # only keep the significant (p_value < 0.05) genes
        data = data[data['p value'] < 0.05].rename(columns = {"p value": "p value " + race})

        mutationData = pd.read_csv(root_drive_path + 'TCGA_mutprop_cancer_race_info.csv', index_col = 0)
        # prefix of column name with cancer and race
        colName = 'TCGA-' + cancer + "(" + race

        data_header = mutationData.columns
        for col in data_header:
            try:

                if col.startswith(colName):
                    # keep only gene_name and the cancer+ race col
                    mutationDataSubset = mutationData[['gene_name', col]]
                    # merge two dataframes based on gene name, keeping only significant genes
                    inner_merged = pd.merge(data, mutationDataSubset, left_on = ["Gene"], right_on = ["gene_name"])
                    inner_merged = inner_merged[['Gene', 'p value ' + race, col]]
                    # sort the dataframe with descending order of p values
                    inner_merged = inner_merged.sort_values([col,"Gene"], ascending = [False,True])
                    inner_merged = inner_merged.rename(columns = {col: "mutation rates"})
                    inner_merged.to_csv(root_drive_path + '/2023_summer/Daniel_step1_SignificantP_results_colab/' + cancer + '_' + race + '_genes.csv', index = False)
                    return

            except KeyError:
                pass

    except FileNotFoundError:
        pass


if __name__ == "__main__":
  cancers = input("What are the cancers? ALL for all Cancer types or Cancer names separated by comma. ")
  
  if cancers == "ALL":
      data = pd.read_csv(root_drive_path + 'TCGA_mutprop_cancer_race_info.csv')
      data_header = data.columns
      cancers = set()
      for col_header in data_header:
          try:
              cancer_name = re.search("TCGA-(.+?)\(", col_header).group(1)
              cancers.add(cancer_name)
          except AttributeError:
              pass
  else:
      cancers = cancers.split(',')
  
  for cancer in cancers:
      # read Asian gene file
      read_race_gene_file(cancer, "Asian")

    # read Black gene file
    read_race_gene_file(cancer, "Black")
