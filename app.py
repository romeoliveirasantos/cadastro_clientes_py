import tkinter as tk
from tkinter import messagebox
import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

#função para conectar ao banco de dados
def conectar_banco():
    try:
        conn = psycopg2.connect(
            dbname= DB_NAME,
            user= DB_USER,
            password= DB_PASSWORD,
            host= DB_HOST
        )
        return conn
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None

#função para adicionar cliente
def adicionar_cliente(nome, email, wapp):
    conn = conectar_banco()
    if conn is None:
        return  #não prosseguir se a conexão falhar
    
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO clientes (nome, email, wapp) VALUES (%s, %s, %s)", (nome, email, wapp))
        conn.commit()
        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao adicionar cliente: {e}")
    finally:
        cursor.close()
        conn.close()

#função para listar clientes
def listar_clientes():
    conn = conectar_banco()
    if conn is None:
        return []  #retorna lista vazia se a conexão falhar
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        return clientes
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao listar clientes: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

# HUD app
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Clientes")

        #tamanho da janela
        self.root.geometry("800x800")

        #campos de entrada
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.pack(padx=10, pady=5)
        self.entry_nome = tk.Entry(root, width=40)
        self.entry_nome.pack(padx=10, pady=5)

        self.label_email = tk.Label(root, text="Email:")
        self.label_email.pack(padx=10, pady=5)
        self.entry_email = tk.Entry(root, width=40)
        self.entry_email.pack(padx=10, pady=5)

        self.label_wapp = tk.Label(root, text="WhatsApp:")
        self.label_wapp.pack(padx=10, pady=5)
        self.entry_wapp = tk.Entry(root, width=40)
        self.entry_wapp.pack(padx=10, pady=5)

        # Botão para adicionar cliente
        self.botao_adicionar = tk.Button(root, text="Adicionar Cliente", command=self.adicionar)
        self.botao_adicionar.pack(pady=10)

        # Botão para listar clientes
        self.botao_listar = tk.Button(root, text="Listar Clientes", command=self.listar)
        self.botao_listar.pack(pady=10)

        # Lista de clientes
        self.lista_clientes = tk.Listbox(root, width=50)
        self.lista_clientes.pack(padx=10, pady=5)

    def adicionar(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        wapp = self.entry_wapp.get()
        if nome and email and wapp:
            adicionar_cliente(nome, email, wapp)
            self.entry_nome.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_wapp.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "preencha todos os campos.")

    def listar(self):
        self.lista_clientes.delete(0, tk.END)  #limpa lista atual
        clientes = listar_clientes()
        for cliente in clientes:
            self.lista_clientes.insert(tk.END, f"{cliente[1]} - {cliente[2]} - {cliente[3]}")  #exibe Nome - Email - WhatsApp

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
