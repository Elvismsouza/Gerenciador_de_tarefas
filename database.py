#gerenciador_tarefas/
#├── main.py                # Arquivo principal
#├── database.py            # Arquivo para manipular o banco de dados
#├── animations.py          # Arquivo para animações de carregamento
#├── tasks.db               # Banco de dados SQLite gerado automaticamente
#└── __pycache__/           # Gerado automaticamente após execução

import sqlite3
from animations import loading_animation

# Função para conectar ao banco de dados
def connect_db():
    return sqlite3.connect('tasks.db')

# Função para criar a tabela de tarefas
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        completed INTEGER NOT NULL DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar uma tarefa ao banco de dados
def add_task(description):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (description, completed) VALUES (?, 0)', (description,))
    conn.commit()
    conn.close()
    loading_animation("Salvando tarefa no banco de dados")
    print("Tarefa adicionada com sucesso!")

# Função para visualizar todas as tarefas
def view_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    loading_animation("Carregando tarefas do banco de dados")
    if tasks:
        print("\nLista de Tarefas:")
        for task in tasks:
            status = 'Concluída' if task[2] else 'Pendente'
            print(f"{task[0]}. {task[1]} - {status}")
    else:
        print("\nNenhuma tarefa adicionada.")

# Função para marcar uma tarefa como concluída
def mark_task_completed(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    loading_animation("Marcando tarefa como concluída")
    print("Tarefa marcada como concluída!")

# Função para remover uma tarefa
def remove_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    loading_animation("Removendo tarefa do banco de dados")
    print("Tarefa removida com sucesso!")

