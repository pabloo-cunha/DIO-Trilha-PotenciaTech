curso = 'PyThOn'


print(curso.upper())
print(curso.lower())
print(curso.capitalize())
print(curso.title())


texto = "  Hello world   "

print(texto)
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"
print("###" + menu + "###")
print(menu.center(14))
print(menu.center(20, "#"))
print("-".join(menu))

nome = 'Pablo Vinicius de Lima da Cunha'
print(nome[0]) #captura letra do indice 0
print(nome[::-1]) #inversão de string
print(nome[:-1]) # elimina a ultima letra
print(nome[0:len(nome)-1:3]) #imprime da letra na posição 0 até a ultima, contando de 3 em 3 a partir da primeira.