# While loop
resposta = input('Vamos sair? [s/n] ')
while resposta != 's':
    resposta = input('Vamos sair? [s/n] ')
    # Vetifica ocorrencia da palavra na resposta
    if 'chato' in resposta:
        break
    
condition  = 1
while condition < 10:
    print(condition)
    condition +=1
    
# For loop
exempleList = [1, 4, 6, 7, 8]

for x in exempleList:
    print(x)
    
for x in range(1,11):
    print(x)
    print(x*2)