import tkinter as tk
from tkinter import messagebox

# Dicionário para armazenar os usuários cadastrados (substitua isso por um banco de dados real)
usuarios = {"usuario": "senha"}

def fazer_login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()

    # Verifica se o usuário e a senha estão corretos
    if usuarios.get(usuario) == senha:
        messagebox.showinfo("Login", "Login bem-sucedido!")
        # Após o login bem-sucedido, habilitamos as opções
        cadastrar_button.config(state=tk.NORMAL)
        remover_button.config(state=tk.NORMAL)
        listar_button.config(state=tk.NORMAL)
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos")

def cadastrar_usuario():
    novo_usuario = novo_usuario_entry.get()
    nova_senha = nova_senha_entry.get()

    # Adiciona o novo usuário ao dicionário (substitua isso por um banco de dados real)
    usuarios[novo_usuario] = nova_senha
    messagebox.showinfo("Cadastro de Usuário", "Usuário cadastrado com sucesso!")

def remover_usuario():
    usuario_a_remover = remover_usuario_entry.get()

    # Remove o usuário do dicionário (substitua isso por um banco de dados real)
    if usuario_a_remover in usuarios:
        del usuarios[usuario_a_remover]
        messagebox.showinfo("Remoção de Usuário", "Usuário removido com sucesso!")
    else:
        messagebox.showerror("Remoção de Usuário", "Usuário não encontrado")

def listar_usuarios():
    lista_usuarios = "\n".join(usuarios.keys())
    messagebox.showinfo("Lista de Usuários", f"Usuários cadastrados:\n{lista_usuarios}")

# Criando a janela
janela = tk.Tk()
janela.title("Programa")

# Rótulo de novo usuário
novo_usuario_label = tk.Label(janela, text="Novo Usuário:")
novo_usuario_label.pack()

# Campo de entrada de novo usuário
novo_usuario_entry = tk.Entry(janela)
novo_usuario_entry.pack()

# Rótulo de nova senha
nova_senha_label = tk.Label(janela, text="Nova Senha:")
nova_senha_label.pack()

# Campo de entrada de nova senha
nova_senha_entry = tk.Entry(janela, show="*")
nova_senha_entry.pack()

# Botão de cadastrar usuário
cadastrar_button = tk.Button(janela, text="Cadastrar Usuário", command=cadastrar_usuario)
cadastrar_button.pack()
cadastrar_button.config(state=tk.DISABLED)  # Desabilita até o login

# Rótulo de usuário a ser removido
remover_usuario_label = tk.Label(janela, text="Usuário a Remover:")
remover_usuario_label.pack()

# Campo de entrada de usuário a ser removido
remover_usuario_entry = tk.Entry(janela)
remover_usuario_entry.pack()

# Botão de remover usuário
remover_button = tk.Button(janela, text="Remover Usuário", command=remover_usuario)
remover_button.pack()
remover_button.config(state=tk.DISABLED)  # Desabilita até o login

# Botão de listar usuários
listar_button = tk.Button(janela, text="Listar Usuários", command=listar_usuarios)
listar_button.pack()
listar_button.config(state=tk.DISABLED)  # Desabilita até o login

# Rótulo de usuário
usuario_label = tk.Label(janela, text="Usuário:")
usuario_label.pack()

# Campo de entrada de usuário
usuario_entry = tk.Entry(janela)
usuario_entry.pack()

# Rótulo de senha
senha_label = tk.Label(janela, text="Senha:")
senha_label.pack()

# Campo de entrada de senha
senha_entry = tk.Entry(janela, show="*")
senha_entry.pack()

# Botão de login
login_button = tk.Button(janela, text="Login", command=fazer_login)
login_button.pack()

# Iniciando a interface gráfica
janela.mainloop()