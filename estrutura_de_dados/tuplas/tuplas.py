# A principal diferença entre Tuplas e Lista é que as tuplas são imutáveis, enquanto as listas são mutaveisl.

carros = ('celta', 'fox',) #Boa pratica inserir essa virgula no final para dizer para o python que o objeto em questão é uma tupla e não para aplicar uma regra de precedencia.

#metodos

carros.count('celta') #1
len(carros) #2
carros.index('fox') #1
carros[0] = 'fusca' #erro, pois não é possivel modificar elementos em tuplas

#Esses são basicamente todos os metodos de tupla