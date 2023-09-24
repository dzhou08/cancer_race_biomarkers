import pandas as pd

root_drive_path = './Cancers/'

for cancer in ['UCS','THCA','PRAD','LIHC','KIRP','KIRC','ESCA','BRCA','BLCA']:
    for race in ['Asian','Black']:
        geneDict = {}
        tempSequence = ""
        geneList = []
        with open(root_drive_path + 'step3_ensembl_protein_sequences_files/' + cancer + '_unique' + race + '.txt') as protein_file:
            for line in protein_file:
                if line[0] == ">":
                    gene = line.split("|")[4].replace("\n","")
                    geneDict[gene] = "";
        with open(root_drive_path + 'step3_ensembl_protein_sequences_files/' + cancer + '_unique' + race + '.txt') as protein_file:
            for line in protein_file:
                if line[0] == ">":
                    gene = line.split("|")[4].replace("\n","")
                    if len(geneList) > 0:
                        lastGene = geneList[len(geneList)-1]
                        if len(tempSequence.replace("\n","").replace("*","").replace("\n","")) > len(geneDict[lastGene]):
                            geneDict[lastGene] = tempSequence.replace("\n","").replace("*","")

                            #print(lastGene)

                        else:
                            pass
                    else:
                        pass
                    geneList.append(gene)
                    tempSequence = ""
                else:
                    tempSequence += line;
        with open(root_drive_path + '/step3_longest_protein_sequence/' + cancer + '_longest_protein_sequences_' + race + '.txt', 'w') as f:
            for gene in geneDict:
                f.write('>' + gene + '\n')
                for string in [geneDict[gene][i:i+64] for i in range(0, len(geneDict[gene]), 64)]:
                    f.write(string + '\n')
