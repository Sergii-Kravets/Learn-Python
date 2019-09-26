from collections import Counter

with open('dna.fasta', 'r') as data:
    dna_data = data.read().splitlines()



def number_of_nucleotides(data):
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


def dnk_into_rnk(data):
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


def genetic_code_in_protein(data):
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



rnk = dnk_into_rnk(dna_data)
timin = timin_in_uracil(rnk)
gen = genetic_code(timin)
protein = genetic_code_in_protein(timin)

print(dna_data)
print()
print(number_of_nucleotides((dna_data)))
print()
print(rnk)
print()
print(timin)
print()
print(gen)
print()
print(protein)




