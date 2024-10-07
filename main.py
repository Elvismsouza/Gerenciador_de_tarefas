from database import add_task, view_tasks, mark_task_completed, remove_task, create_table

# Função para exibir o menu e interagir com o usuário
def menu():
    create_table()  # Criar a tabela no início do programa
    while True:
        print("\n----- Gerenciador de Tarefas -----")
        print("1. Adicionar nova tarefa")
        print("2. Visualizar todas as tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        choice = input("\nEscolha uma opção: ")

        if choice == '1':
            description = input("Descrição da tarefa: ")
            add_task(description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("ID da tarefa a ser marcada como concluída: "))
            mark_task_completed(task_id)
        elif choice == '4':
            task_id = int(input("ID da tarefa a ser removida: "))
            remove_task(task_id)
        elif choice == '5':
            print("Saindo do Gerenciador de Tarefas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciando o programa
if __name__ == "__main__":
    menu()

