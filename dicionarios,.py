# declaraçoes de dicionario
pessoa = {"nome": "Jander", "idade": "33"}

pessoa = dict(nome = "Jander", idade = 33)

# adicionando dados ao dicionario
pessoa["telefone"] = "666-66666"

# acessando valores
print(pessoa["nome"])

# dicionarios aninhados

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3344-4442"},
    "Melaine@gmail.com": {"nome": "Melaine", "telefone": "3344-8888", "extra" : {"a": "1"}}

}

print(contatos["giovanna@gmail.com"]["telefone"])
teste = contatos["Melaine@gmail.com"]["extra"]["a"]

print(teste)

for chave in contatos:
     print(chave, contatos[chave])
     
# .itens() retorna uma lista de tuplas
for chave, valor in contatos.items():
    print(chave, valor)

