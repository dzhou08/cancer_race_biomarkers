# MutDispar
This software examines survival disparities in mutation frequencies of
oncogenes and reveal the biological and clinical significance
of driver mutations, which contribute to mortality disparity.

## Pipeline
![image](https://github.com/dzhou08/cancer_race_biomarkers/assets/65268595/ea0d82b3-e45d-414f-9948-282ed0d987bf)

## Requirements
- python 3
- numpy
- pandas

## Installation
In order to get started with *MutDispar*, you can just clone this repo as follows;
```bash
git clone https://github.com/dzhou08/cancer_race_biomarkers.git
cd ./cancer_race_biomarkers
```
## Usage
### Step 0: Mount The shared Folder on Google Drive

### Step 1: Calculate Significant P Values
1. Calculate the frequency of mutated genes in each race for TCGA cancers
2. Perform proportion test for the frequency of mutation
3. Select genes with significant p-values from proportion test

```
python3 step_1_significant_p_values.py
```
Below is an example of the first six rows of an output file
| Gene | p value Asian | mutation rates |
|:-----------:|:------------|:------------|
|*TTN*|0.0252253881867595|0.318181818181818|
|*STAG2*|0.0379037259675974|0.25|
|*TP53*|0.0007432979061513|0.227272727272727|
|*HRAS*|0.0033335101263974|0.159090909090909|
|*ARID1A*|0.0104834979681634|0.159090909090909|

### Step 2A: Find the longest common sequence
Calculate the longest common list of genes in sorted order based on their p-value for both Asian and Black files
We are looking for the following Cancer types: UCS,THCA,PRAD,LIHC,KIRP,KIRC,ESCA,BRCA,BLCA

```
python3 step_2a_longest_common_sequence.py
```

Below is an example of the first six rows of an output file
| gene | p_value_asian | mutation_asian | p_value_black | mutation_black |
|:-----------:|:------------|:------------|:------------|:------------|
|*TP53*|0.0020686768505332|0.517241379310345|0.0003245032792273|0.462962962962963
|*CLIC5*|0.0065693216385066|0.0344827586206897|0.0005063394448323|0.0308641975308642
|*CSF3*|0.0004104195653529|0.0344827586206897|0.0047829398494226|0.0185185185185185
|*GS1-309P15.2*|0.0004104195653529|0.0344827586206897|0.0047829398494226|0.0185185185185185
|*RP11-356C4.3*|0.0004104195653529|0.0344827586206897|0.0451901189627159|0.0123456790123457

### Step 2B: Find the common genes
Calculate common genes between the Asian and Black race files
We are looking for the following Cancers: UCS,THCA,PRAD,LIHC,KIRP,KIRC,ESCA,BRCA,BLCA

```
python3 step_2b_common_genes.py
```

### Step 3: Find longest protein sequence
1. Extract protein sequences from Ensembl of genes found in Step 2.1.
2. Take longest protein sequence for each gene within file from Step 3.1.

```
python3 step_3_longest_protein_sequence.py
```

### Step 4: Super family analysis
1. Perform CDSearch to identify superfamilies for each gene
2. Identify common superfamilies for each race in selected cancers

```
python3 step_4_super_family.py
```
