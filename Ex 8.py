#somando números do intervalo informado limitando o mailor número
inicio= int (input("informe o primeiro:"))
fim= int (input("informe o número final:"))
salto=-int(input("informe:"))
texto= "Cálculo:"
soma=0
for numero in range (inicio, fim, salto):
    soma=soma+numero
    texto=texto+ str (numero)
    if numero> 50:
        texto=texto+ "\n|passou de 50"
        break
    if numero != fim-1:
        texto= texto + "+"
        print(f"{texto}")
        print (f"soma: {soma}")
        