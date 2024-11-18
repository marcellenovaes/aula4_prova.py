# Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email.
# Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, 
# o número de telefone e o endereço de email. Após coletar todas as informações necessárias, 
# exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.

colunas = "-" * 60

dicionario = {}

def dados_usuario():
    print("insira seus dados abaixo")
    
    nome= input("Nome: ").strip().upper()
    
    telefone = int(input("Telefone: "))
    
    email = input("Email : ").strip().upper()
    
    dicionario[nome] = {'telefone': telefone, 'email':email}   
    
def ver_dicionario():

    if dicionario:
        print(colunas)
        print("DADOS CADASTRADOS:")
        print(colunas)
        
        for nome, dados in dicionario.items():
            print(f"Nome: {nome}")
            print(f"  Telefone: {dados['telefone']}")
            print(f"  Email: {dados['email']}")
            print(colunas)  # Separador entre os cadastros
    else:
        print("Nenhum dado cadastrado ainda.")

    
    
while True:
    print(colunas)
    print("CADASTRO")
    print(colunas)
    dados_usuario()
    ver_dicionario()
    opcao = input("Deseja sair? (s/n)")

    match opcao:
        case "s":
            print("Saindo do sistema.")
            break
        case "n":
            print("Continuando o cadastro...")
        case _:
            print("Opção inválida. Digite 's' para sair ou 'n' para continuar.")
            