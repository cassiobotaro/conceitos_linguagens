# Programação Imperativa
# Paradigma principal do Python, tem por característica
# mudança de estado do programa.
# O nome imperativo e por causa que ordens são dadas no imperativo.
# Basicamente um programa é escrito como:
# faça isto, faça aquilo, depois aquilo outro.
# Exemplo de um programa imprativo
somente_menores_que_1 = []
for x in (0.1, 0.3, 2.5, 0.8, 1.1, 0.1):
    if x < 1:
        somente_menores_que_1.append(x)
quadrado_valores = []
for y in somente_menores_que_1:
    quadrado_valores.append(y)
print(quadrado_valores)
# Repare que a mudança do programa são refletidas e
# armazenadas em células de memória(variáveis).

# Programação Funcional
# Características funcionais
# Provê map  e filter
# funções lambdas
# funções de primeira ordem(veja as lambdas sendo passados
# como parâmetros de outras funções)
map(lambda x: x ** 2, filter(lambda x: x < 1, (0.1, 0.3, 2.5, 0.8, 1.1, 0.1)))
# Restrições
# - não existe recursão em cauda
# - não é puramente funcional, logo não apresenta todas as suas características

# Orientação a objeto
# Não considerado por Sebesta como um paradigma de programação,
# O argumento é que toda programação orientada a objeto é imperativa,
# com única diferença que a estruturação dos arquivos é
# orientada a objetos.
# Exemplo da utilização.
# Características
# Elegância em getters e setters com utilização de properties
# Herança Múltipla
# Utilização do self explícito em métodos de instância


class Filho(Pai, Mae):

    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, valor):
        if valor > 0:
            self.__peso = valor
        else:
            raise ValueError('valor deve ser > 0')

# Python possui suporte a orientação a objetos, inclusive até mesmo
#  os tipos básicos em python são objetos.

# A conclusão é que Python é imperativo, mas também possui caratéristicas
# de outros paradigmas
# e suporte a orientação a objeto.
