#To translate DNA into protein you need:
#1) Transfer DNA to RNA - by changing the nucleotides (G for C, C for G, T for A and A for T)
#
#2) Then the nucleotide thymine (T) become Uracil (U).
#
#3) then view each triplet (codon) in the genetic code table.
# AGU becomes Serine, which we can write as S. AUU becomes Isoleucine (Ile), which we write I
# Also you need Need a codon table (Use Google)

from collections import Counter

with open('dna.fasta', 'r') as data:
    dna_data = data.read().splitlines()


def count_nucleotides(data):
    gen = None
    genes = {}
    for dna in data:
        if '>' in dna:
            gen = dna[1:]
            genes[gen] = Counter()
        else:
            for simvol in dna:
                genes[gen][simvol] +=1
    return genes


def translate_from_dna_to_rna(data):
    rnk = []
    for counter, str in enumerate(data):
        if '>' in str:
            rnk.append(str)
            continue
        len_str = len(str)
        for symbol in str:
            if symbol == 'A':
                rnk_symbol = 'T'
            elif symbol == 'T':
                rnk_symbol = 'A'
            elif symbol == 'G':
                rnk_symbol = 'C'
            elif symbol == 'C':
                rnk_symbol = 'G'
            rnk.append(rnk_symbol)

        all_str = "".join(rnk[counter:len_str + counter])
        rnk[counter:len_str + counter] = [all_str]
    return rnk


def timin_in_uracil(data):
    timin_rnk = []
    for counter, str in enumerate(data):
        if '>' in str:
            timin_rnk.append(str)
            continue
        len_str = len(str)
        for symbol in str:
            timin_rnk_symbol = symbol
            if symbol == 'T':
                timin_rnk_symbol = 'U'
            timin_rnk.append(timin_rnk_symbol)

        all_str = "".join(timin_rnk[counter:len_str + counter])
        timin_rnk[counter:len_str + counter] = [all_str]
    return timin_rnk


def translate_rna_to_protein(data):
    protein = []
    codontable = {
        'GUU':'V', 'GCU':'A', 'GAU':'A', 'GGU':'G',
        'GUC':'V', 'GCC':'A', 'GAC':'A', 'GGC':'G',
        'GUA':'V', 'GCA':'A', 'GAA':'G', 'GGA':'G',
        'GUG':'V', 'GCG':'A', 'GAG':'G', 'GGG':'G',
        'AUU':'I', 'ACU':'T', 'AAU':'A', 'AGU':'S',
        'AUC':'I', 'ACC':'T', 'AAC':'A', 'AGC':'S',
        'AUA':'I', 'ACA':'T', 'AAA':'L', 'AGA':'A',
        'AUG':'M', 'ACG':'T', 'AAG':'L', 'AGG':'A',
        'CUU':'L', 'CCU':'P', 'CAU':'H', 'CGU':'A',
        'CUC':'L', 'CCC':'P', 'CAC':'H', 'CGC':'A',
        'CUA':'L', 'CCA':'P', 'CAA':'G', 'CGA':'A',
        'CUG':'L', 'CCG':'P', 'CAG':'G', 'CGG':'A',
        'UUU':'F', 'UCU':'S', 'UAU':'T', 'UGU':'C',
        'UUC':'F', 'UCC':'S', 'UAC':'T', 'UGC':'C',
        'UUA':'L', 'UCA':'S', 'UAA':'S', 'UGA':'S',
        'UUG':'L', 'UCG':'S', 'UAG':'S', 'UGG':'T',
    }


    for counter, str in enumerate(data):
        if '>' in str:
            protein.append(str)
            continue
        len_str = len(str)
        for i in range(0, len(str), 3):
            for key in codontable:
                if str[i:i+3] == key:
                    protein.append(codontable[key])

        all_str = "".join(protein[counter:len_str + counter])
        protein[counter:len_str + counter] = [all_str]
    return protein


def genetic_code(data):
    timin_rnk = []
    for counter, str in enumerate(timin):
        if '>' in str:
            timin_rnk.append(str)
            continue
        len_str = len(str) + len(str) // 3
        for index, symbol in enumerate(str):
            index += 1
            timin_rnk_symbol = symbol
            timin_rnk.append(timin_rnk_symbol)
            if index % 3 == 0:
                timin_rnk.append(' ')

        all_str = "".join(timin_rnk[counter:len_str + counter])
        all_str = all_str.rstrip()
        timin_rnk[counter:len_str + counter] = [all_str]
    return timin_rnk

count_nucleotides = count_nucleotides(dna_data)
rnk = translate_from_dna_to_rna(dna_data)
timin = timin_in_uracil(rnk)
gen = genetic_code(timin)
protein = translate_rna_to_protein(timin)



with open('01_count_nucleotides.fasta', 'w') as outfile:
   for key in count_nucleotides:
       count_nucleotides_string = str(key)
       outfile.write(count_nucleotides_string + '\n')
       count_nucleotides_string = str(count_nucleotides[key])
       outfile.write(count_nucleotides_string + '\n')


with open('02_translate_from_dna_to_rna.fasta', 'w') as outfile:
    for str in rnk:
        rnk_str = str
        outfile.write(rnk_str + '\n')


with open("03_translate_rna_to_protein", 'w') as outfile:
    for str in protein:
        protein_str = str
        outfile.write(protein_str + '\n')





