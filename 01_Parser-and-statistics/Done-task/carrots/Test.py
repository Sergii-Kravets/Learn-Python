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

def dnk_into_rnk (data):
    rnk = []
    for counter, str in enumerate(dna_data):
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






print(dna_data)
print()
print(dnk_into_rnk(dna_data))



