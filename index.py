class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

def incluircontato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    agenda.append(Contato(nome, telefone))
    print(f"Contato {nome} adicionado com sucesso!")

def exibircontatos(agenda):
    if not agenda:
        print("A agenda está vazia.")
    else:
        print("Lista de Contatos:")
        for contato in agenda:
            print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")

def buscarcontato(agenda, nome):
    for contato in agenda:
        if contato.nome.lower() == nome.lower():
            return contato
    return None

def atualizarcontato(agenda, nome, novo_telefone):
    contato = buscarcontato(agenda, nome)
    if contato:
        contato.telefone = novo_telefone
        print(f"Telefone do contato {nome} atualizado com sucesso.")
    else:
        print(f"Contato {nome} não encontrado na agenda.")

def excluircontato(agenda, nome):
    contato = buscarcontato(agenda, nome)
    if contato:
        agenda.remove(contato)
        print(f"Contato {nome} removido da agenda.")
    else:
        print(f"Contato {nome} não encontrado na agenda.")

def ordenarcontatos(agenda):
    agenda.sort(key=lambda contato: contato.nome.lower())
    print("Contatos em ordem alfabética.")

def main():
    agenda = []

    while True:
        print("\nAgenda de Contatos ")
        print("1. Adicionar Contato")
        print("2. Exibir Contatos")
        print("3. Buscar Contato")
        print("4. Atualizar Contato")
        print("5. Excluir Contato")
        print("6. Ordenar Contatos por Nome")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            incluircontato(agenda)
        elif escolha == "2":
            exibircontatos(agenda)
        elif escolha == "3":
            nome = input("Digite o nome do contato que deseja buscar: ")
            contato = buscarcontato(agenda, nome)
            if contato:
                print(f"Contato encontrado - Nome: {contato.nome}, Telefone: {contato.telefone}")
            else:
                print(f"Contato {nome} não encontrado na agenda.")
        elif escolha == "4":
            nome = input("Digite o nome do contato que deseja atualizar: ")
            novo_telefone = input("Digite o novo telefone: ")
            atualizarcontato(agenda, nome, novo_telefone)
        elif escolha == "5":
            nome = input("Digite o nome do contato que deseja excluir: ")
            excluircontato(agenda, nome)
        elif escolha == "6":
            ordenarcontatos(agenda)
        elif escolha == "7":
            print("Encerrando a agenda.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

    


