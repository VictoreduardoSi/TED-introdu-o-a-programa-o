# Atividade Do aluno Victor eduardo.
macas = int(input("Quantidade de maçãs:"))
if macas < 12:
    preco = (float(1.3))
    total = preco * macas
    print(f"{total:.1f}")
else:
    preco = float(int(1.3))
    total = preco * macas
    print(f"{total:.1f}")
