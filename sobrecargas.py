# Sobrecargas
# Sobrecarga de Operadores
# Como tudo é objeto até mesmo a chamada a operadores pode ser transcrita
# como uma invocação ao método correspondente
a = 1
b = 2
print(a + b)
# Posso transcrever isto em:
print(a.__add__(b))
# Quando tento somar a(int) e uma string o que ocorre?
try:
    print(a + '1')
except TypeError as e:
    print("Como a tipagem é forte essa operação não ocorre.")
# Mas então se não há coerção de tipo, porque o vezes funciona?
print(3 * 'lol')
# O operador vezes, nada mais é que a invocação da função __mul__
# e ele é sobrecarregado, quando o tipo recebido é string
# ele replica a cadeia de caracteres e em seguida concatena
# retornando o resultado.
print(3.__mul__('lol'))
# Posso utilizar esta sobrecarga em classes próprias para aproveitar da
# utilização de operadores.
class MinhaClasse:

    def __add__(self, other):
        return 42

instância = MinhaClasse()
print(instância + 10)

# Funny
# No python 2 é possível por um descuido  um objeto ser igual e
# diferente a algo
class Teste(object):
    def __eq__(self, value):
        return 3 == value

t = Teste()
print(3 == t != 3)
# Isto só ocorre porque o operador != é representado na função
# __ne__ e como só sobreescrevi o __eq__ o retorno continua como True
# afinal t e 3 são diferentes
# No python 3, quando não presente __ne__, o retorno do operador !=
# é o contrario do __eq__

# Sobrecarga de métodos
# Um unico nome, respondendo por várias assinaturas de funções.
from functools import singledispatch
# Vamos supor uma função que captura tweets e pode receber como parâmetro
# uma string ou uma lista com diversos valores
# Para simular a sobrecarga de métodos o python utiliza um mecanismo de dispatch
# em que uma função é um despaixante para outras
# meu despachante simplesmente lança exceção dizendo que tipo do args
# deve ser string ou uma lista
@singledispatch
def search(arg, **options):
    raise TypeError('Args should be a string, list or a tuple.')

# Para cada tipo que deve ser despachado para uma determinada função
# um novo registro deve ser feito
# O python somente  olha o tipo do primeiro parâmetro para decidir para onde
# deve redirecionar a execução

@search.register(list)
@search.register(tuple)
def _(arg, **options):
    print("A função foi invocada utilizando uma lista ou tupla.")
    ... # aqui viria o código da função

# Até mesmo uma função pre-existente pode ser utiliada como dispatch

@search.register(str)
def outra_função(arg, **options):
    print("A função foi invocada com uma string.")
    ... # aqui viria o código da função

# Algo como em java de receber somente alguns parâmetros não é feito
# utilizando este mecanismo, mas sim com parâmetros nomeados
# Assim se um função pode receber 2, 3 ou 4 parâmetros, é só dar um valor
# default aos parâmetros opcionais.
