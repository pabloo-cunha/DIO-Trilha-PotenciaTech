'''
lista em python aceita qualquer tipo de objeto
'''

lista = [1, True, "Banana", 25.7]

#metodo de add

lista.append(64) #Irá adicionar no final [1, True, "Banana", 25.7, 64]

#metodo extend
lista2 = ["Maçã", "carne"]
lista.extend(lista2) #irá adicionar no final tudo que tiver dentro da lista2 [1, True, "Banana", 25.7, 64, "Maçã", "carne"]

#metodo copy - Cria uma nova lista a partida original
list_copy = lista.copy()
list_copy.append("lista copia")
print(f'lista original: {lista}')
print(f'nova lista com adição de elemento: {list_copy}')

#remoção do ultimo objeto, retornando-o.

elemento_retirado = list_copy.pop()
print(f'ultimo elemento da lista copia retirado: {elemento_retirado}')
print(f'nova lista: {list_copy}')

#remover elemento baseado no elemento passado como parametro
list_copy.remove("Maçã")
print(list_copy)

#ordenar lista. A ordenação só funciona para listas que possuem o mesmo tipo de elemento
palavras = ["c", "pablo", "Pablo", "abacate", "java"] #Letra maiusculas vem primeiro
numeros = [2 ,545 ,64, 84, 97, 26 ,27]
palavras.sort()
print(palavras)
palavras.sort(reverse=True) #invertendo os elementos
print(palavras)
palavras.sort(key=lambda x: len(x)) #organizando pela quantidade de caracteres iteraveis
print(palavras)

print(sorted(numeros)) #mesmo resultado de numeros.sort()