nomes = ["Ana", "carlos", "Beatriz", "Daniel", "Elisa"]
if nomes.count("carlos") != 0:
    print("Carlos está na lista")
nomes[3] = "Bruna"
print(nomes)
print(f"O nome ana aparece {nomes.count('Ana')} vezes")