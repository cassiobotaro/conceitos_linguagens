# Escopo(resolução de escopos e namespaces)
# a resolução de nomes é sempre do interior para o exterior
# das funções a menos que explicitamente modificado
variavela = 5


def função_qualquer(variavela):
    """
    Calcula o dobro de um número, mas antes incrementa o valor em 1.
    """
    print(id(variavela))
    variavela += 1
    print(id(variavela))
    return variavela ** 2

print(função_qualquer(3))
print(variavela)

# É importante notar que mesmo depois de alterar o valor da variavela
# dento da função, externamente seu valor permanece intacto.
# o que acontece é que dentro daquele escopo(o da função) um novo rótulo
# variavela é criado e atribuido a operação, sem afetar o rotulo externo.
# Um outro detalhe é que se repararmos o endereço de memória de variavela
# é o mesmo dentro e fora da função
# isto é porque a passagem de parâmetro é por referência.
# não há copia do valor passado como parãmetro, e isto é bom
# Copias podem ser lentas

# Poderia ser feito uma modificação no valor externo, mas isto teria
# de ser explícito
variavela = 3


def global_qualquer():
    """Modificando a variável global."""
    global variavela
    print(id(variavela))
    variavela += 1
    print(id(variavela))
    return variavela ** 2

print(global_qualquer())
print(variavela)

# Efeito colateral
# Ocorre quando o parametro da função é uma lista, um dicionário ou algum
# outro tipo mutável.
# Como as operações são feitas 'in place', o que ocorre dentro da
# função é refletido fora.
lista = [1, 3, 2]


def ordena_lista_e_insere_número(lista):
    lista.sort()
    lista.append(4)

ordena_lista_e_insere_número(lista)
print(lista)


# Uma curiosidade sobre escopos
x = 10
s = [x**2 for x in range(5)]
print(x)
# Irá imprimir o valor 10, pois list comprehensions têm o seu próprio
# escopo

# Namespaces
# Eventualmente há uma colisão na vinculação de nomes, e a resolução disto
# pelo interpretador é considerar a ultima atribuição ou importação daquele
# nome
from math import sin


def sin(y):
    return 42

# O seno de qulquer número é 42
# uma maneira simples de resolver este problema é com utilização de namespaces,
# ou seja, você invocará uma função utilizando um espaço de nomes
# exemplo:
import math
# e invoque a função utilizando
math.sin(30)
# Agora não há mais a colisão

# Métodos anônimos
# Pode ser definida basicamente como: "Dado uma entrada, me retorne uma saída."
# São funções que não possuem nome.
# Sua representação é através da palavra reservada lambda
lambda x, y: x + y  # soma dois números
# A função deixa de existir quando não há mais referências a ela
# Uma  utilidade:
sorted([(1, 'Cássio'), (2, 'Rapha'), (3, 'Igor')], key=lambda x: x[1])

# Embora eu ainda prefire explicitar as funções
from operator import itemgetter
sorted([(1, 'Cássio'), (2, 'Rapha'), (3, 'Igor')], key=itemgetter(0))

# Closure
# closure é o registro de uma função associado a variáveis livre dentro
# de um contexto léxico em funções de primeira classe


def makeInk(x):
    def inc(y):
        return x + y
    return inc

closure1 = makeInk(1)
closure2 = makeInk(5)
closure1(3)
closure2(3)

# Ser uma função de primeira classe significa posso fazer atribuição desta
# a uma variavel ou passa-la como parâmetro a outra função.
# E quando é dito que estamos registrando uma função associando variáveis
# livres dentro de um contexto, e é o que vemos com a variável x no exemplo
# acima.
# A função inc tem associado a ela a variável x, e a função é  o retorno
# quando invocamos a função makeInc.
# Com isso ao invocarmos closure1, o valor 1 estará atribuido a x
# da função inc retornada em makeInc(1), o mesmo vale para a closure 2 e
# seu respectivo valor de x

# Se o conceito ainda soar estranho, não se apavore, este conceito de alterar
# uma função em tempo de execução é dado como metaprogramação e não é
# considerado um assunto simples.
