from collections import Counter

gen = None
genes = {}
with open('dna.fasta', 'r') as dna:
    for data in dna:
        data = data.strip()

        if '>' in data:
            gen = data[1:] #name
            genes[gen] = Counter()
        else:
            for simvol in data:
                genes[gen][simvol] +=1


print(genes)