#   Oriented object programming course by Bradesco Foundation

# Classes vão armazenar trechos de códigos relacionados entre si

#   DEFINIÇÕES:

    # Classes: Vão armazenar trechos de códigos relacionados entre si.
    # Objetos: Variável que possui todas as características comuns à classe, porém, com valores diferentes em seus atributos
    # Abstração: Ação de utilizar mensagens para acessar os recursos de uma classe.
    # Atributos: Características das classes
    # Funções: Função nativa do Python que retorna um valor declarado dentro da classe
    # Métodos: Função nativa do Python que não possui retorno declarado dentro de uma classe.
    # Exceção: Controla o fluxo de execução durante um erro.
    # Mensagem: Chamada a um atributo, método ou função.
    # Herança: Uma classe pode herdar atributos, métodos e/ou funções de outra.
    # Encapsulamento: O encapsulamento permite que os atributos sejam vistos somente nas classes onde foram declarados, definindo o nível de acesso de atributos, métodos ou funções.
    # Polimorfismo: Escolher entre os atributos, métodos e/ou funções que sobrescreveram ou que foram sobrescritos.

# Vamos criar um pequeno projeto de uma loja virtual

# MinhaClasse()
# A partir das classes é possível criar objetos, ou seja, uma classe é um “molde” para a criação de objetos.

class Main:
    pass

from Cliente import Cliente

c1 = Cliente("João","1197958424")
c2 = Cliente("Luan César Carvalho","98154-1343")

print("\nCadastrando cliente...\n",c1)
print("Nome: ", c1._nome, "\nTelefone: " , c1._telefone)

from Conta import Conta

conta1 = Conta(c1._nome,6565,0)
conta2 = Conta(c2._nome,2732,9.47)


print("\nTitular: ", conta1._titular, "\nNúmero: ", conta1._numero, "\nSaldo: R$", conta1._saldo)
print("\nTitular: ", conta2._titular, "\nNúmero: ", conta2._numero, "\nSaldo: R$", conta2._saldo)

print("")
conta=Conta(c1.get_nome(),conta1._numero,0)


conta.extrato()
conta.deposita(100)
conta.extrato()
conta.saque(50)
conta.extrato()