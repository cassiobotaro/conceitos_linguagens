# tipagem forte
# não há conversão ou coerção de tipos implícitas
variavela = 1
variavelb = 'a'

try:
    variavela + variavelb
except TypeError:
    print("Não posso fazer soma de tipos diferentes a menos que isto seja"
          "realmente necessário")

# Com tipos numéricos essa conversão acontece pois derivam de uma mesma
# origem na árvore de herança
variavela = 1  # int
variavelb = 2.0  # float

print(type(variavela + variavelb))

# A multiplicação de string não é uma conversão ou coerção,
# e sim sobrecarga de método e será explicado no arquivo sobrecarga.py.
print("Nan" * 8 + ' Batman!')

# A tipagem é dinâmica
# Embora o python compile trechos de código em bytecodes para otimizar
# sua execução, esta etapa de compilação não realiza verificação de
# tipos.
# Além disso os tipos podem ser modificados em tempo de execução
variavela = "string"
print(type(variavela))
variavela = [1, 2, 3]
print(type(variavela))

# Tipos primitivos
# Python não possui tipos primitivos, tudo em python é objeto.
# Exemplo:
variavela = 5
print(variavela.real)
print(variavela.imag)
# Números completos são builtin.
variavelb = 6 + 3j
print(variavelb.real)
print(variavelb.imag)

# A conversão de tipos é realizada através de "funções" correspondentes
lista_imutavel_sem_repetição = frozenset([1, 1, 2, 3, 4, 4])
# Estas funções na verdade são chamadas a classe correspondente
variavela, variavelb = "1", str("1")

# comparação e outros operadores
# A comparação entre elementos não é permitida(tipagem forte)
# a menos que dois elementos se permitam comparação
try:
    '2' > 1
except TypeError:
    print("Os elementos não são comparáveis.")

# Uma curiosidade é o operador de comparação é
# que não lança exceção
variavela = '1'
variavelb = 1
variavela == variavelb
# Tipicamente quando não consegue fazer a igualdade entre elementos
# NotImplemented é retornado pela variavel a
# e o python verifica se variavelb sabe como resolver a igualdade
# se ambos não sabem, o retorno é False
# E o != retorna o oposto de ==

# Ponteiros
# Não existe o tipo ponteiro, mas tudo tem  a ver com ponteiros
# a e b rotulam o mesmo endereço de memória
# com o valor 1
variavela = 1
variavelb = variavela
variavela is variavelb

# para economia de memória
# numeros e strings compartilham o mesmo espaço de memória
variavelb = 1
variavela is variavelb
id(variavela) == id(variavelb)

variavela = 'casa'
variavelb = 'casa'
id(variavela) == id(variavelb)
# mas nem sempre é possivel essa economia
id(2**32) == id(2**32)
