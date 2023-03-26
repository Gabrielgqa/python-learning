# Mostra texto na tela
print("Hello World")
# Pede para o usuário inserir algum valor
name = input("Informe seu nome")
# 'F' de format. Habilita a inserção de variável
print(f"Bem vindo, {name}!")
# Variáveis fracamente tipadas
nome = 'Gabriel'
new_name = nome
# Desaloca valor da memória
del new_name
# Pegar tipo de variável
print(type(nome))
# Valores do boolean com maiúsculo
booll = False
print(type(booll))
# Tipo str/int/float/bool
# Python -i (abre arquivo no modo interativo usando a função abaixo trás todas as formas de interação disponíveis)
dir(nome)
# Conectivos lógicos and, or, not