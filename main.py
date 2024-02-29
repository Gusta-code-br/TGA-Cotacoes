#import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter
import fdb
import hashlib
import pyperclip
from configparser import ConfigParser


class MyApp:

    def __init__(self, root):
        self.root = root
        self.root.title("TGA - Cotação")

        config = ConfigParser()
        config.read('desktop.ini')
        self.hostname = config['DataBase']['host']
        self.database = config['DataBase']['path']
        self.username = config['DataBase']['user']
        self.password = config['DataBase']['password']
        self.inicialnomeuser = config['Login']['usuario']

        self.UserName = customtkinter.CTkLabel(root, text="Usuário: ")
        self.UserName.grid(padx=(20), pady=(0), row=0, column=1, sticky="nsew")
        self.PassWord = customtkinter.CTkLabel(root, text="Senha: ")
        self.PassWord.grid(padx=(20), pady=(0), row=1, column=1, sticky="nsew")
        self.EntryUser = customtkinter.CTkEntry(root)
        self.EntryUser.insert(0, self.inicialnomeuser)
        self.EntryUser.grid(padx=(20), pady=(0), row=0, column=2, sticky="nsew")
        self.EntryPass = customtkinter.CTkEntry(root, show="*")
        self.EntryPass.grid(padx=(20), pady=(20), row=1, column=2, sticky="nsew")

        self.ButtonBD = customtkinter.CTkButton(root, text="DB", command=self.DataBase)
        self.ButtonBD.grid(padx=(10), pady=(10), row=3, column=1, sticky="nsew")
        self.GetIn = customtkinter.CTkButton(root, text="Login", command=self.tela_inicial)
        self.GetIn.grid(padx=(10), pady=(10), row=3, column=2, sticky="nsew")

    def DataBase(self):
        self.UserName.grid_forget()
        self.PassWord.grid_forget()
        self.EntryUser.grid_forget()
        self.EntryPass.grid_forget()
        self.ButtonBD.grid_forget()
        self.GetIn.grid_forget()
        ConfigDB(root)

    def tela_inicial(self):
        self.UserName.grid_forget()
        self.PassWord.grid_forget()
        self.EntryUser.grid_forget()
        self.EntryPass.grid_forget()
        self.ButtonBD.grid_forget()
        self.GetIn.grid_forget()
        nome = self.EntryUser.get()
        senha = self.EntryPass.get()
        senha_hash = hashlib.md5(senha.encode()).hexdigest().upper()

        self.connection = fdb.connect(host=self.hostname, database=self.database, user=self.username,
                                      password=self.password)
        self.cursor = self.connection.cursor()
        query = f"SELECT * FROM gusuarios WHERE nome = '{nome}' AND senha = '{senha_hash}'"
        self.cursor.execute(query)
        if(self.cursor.fetchall()):
            TelaInicial(root)
        else:
            messagebox.showinfo("Erro de login", "Usuário e senha não compátiveis")
            MyApp(root)


class ConfigDB:
    def __init__(self, root):
        self.root = root

        config = ConfigParser()
        config.read('desktop.ini')
        self.hostname = config['DataBase']['host']
        self.database = config['DataBase']['path']
        self.username = config['DataBase']['user']
        self.password = config['DataBase']['password']

        self.UserName = customtkinter.CTkLabel(root, text="Usuário: ")
        self.UserName.grid(padx=(20), pady=(0), row=0, column=1, sticky="nsew")
        self.PassWord = customtkinter.CTkLabel(root, text="Senha: ")
        self.PassWord.grid(padx=(20), pady=(0), row=1, column=1, sticky="nsew")
        self.EntryUser = customtkinter.CTkEntry(master=root)
        self.EntryUser.insert(0, self.username)
        self.EntryUser.grid(padx=(20), pady=(0), row=0, column=2, sticky="nsew")
        self.EntryPass = customtkinter.CTkEntry(root, show="*")
        self.EntryPass.insert(0, self.password)
        self.EntryPass.grid(padx=(20), pady=(20), row=1, column=2, sticky="nsew")

        self.CaminhoLabel = customtkinter.CTkLabel(master=root, text="Caminho: ")
        self.CaminhoLabel.grid(padx=(10), pady=(10), row=3, column=1, sticky="nsew")
        self.CaminhoDB = customtkinter.CTkEntry(master=root)
        self.CaminhoDB.insert(0, self.database)
        self.CaminhoDB.grid(padx=(10), pady=(10), row=3, column=2, sticky="nsew")

        self.conection = customtkinter.CTkButton(master=root, text="Conectar", command=self.connect)
        self.conection.grid(padx=(10), pady=(10), row=4, column=1, sticky="nsew")

        self.GetBack = customtkinter.CTkButton(master=root, text="Voltar", command=self.voltar)
        self.GetBack.grid(padx=(10), pady=(10), row=4, column=2, sticky="nsew")

    def voltar(self):
        self.UserName.grid_forget()
        self.EntryUser.grid_forget()
        self.EntryPass.grid_forget()
        self.PassWord.grid_forget()
        self.CaminhoDB.grid_forget()
        self.conection.grid_forget()
        self.GetBack.grid_forget()
        self.CaminhoLabel.grid_forget()
        MyApp(root)

    def connect(self):
        try:
            self.user = self.EntryUser.get()
            self.password = self.EntryPass.get()
            self.path = self.CaminhoDB.get()

            parametros_conexao = {
                'host': 'localhost',  # Você pode especificar o IP ou o nome do servidor Firebird
                'database': self.database,  # Caminho para seu banco de dados Firebird
                'user': self.username,
                'password': self.password,
            }
            con = fdb.connect(**parametros_conexao)

            messagebox.showinfo("Conexão bem-sucedida", "Conexão ao Firebird realizada com sucesso!")

            # Fechar a conexão
            con.close()
        except Exception as e:
            messagebox.showerror("Erro de conexão", f"Ocorreu um erro ao conectar ao Firebird:\n{str(e)}")


class TelaInicial:
    def __init__(self, root, **kwargs):
        super().__init__(**kwargs)
        self.TipoDado = None
        self.root = root

        config = ConfigParser()
        config.read('desktop.ini')
        self.hostname = config['DataBase']['host']
        self.database = config['DataBase']['path']
        self.username = config['DataBase']['user']
        self.password = config['DataBase']['password']

        self.root.state('zoomed')
        self.root.title("TGA - Cotação")

        self.GerarLink = customtkinter.CTkButton(master=root, text="Gerar \n Link", command=self.geraLink)
        self.GerarLink.grid(padx=(20), pady=(20), row=1, column=1, sticky="nsew")

        self.RespostaFornecedor = customtkinter.CTkButton(root, text="Resposta do \n Fornecedor")
        self.RespostaFornecedor.grid(padx=(20), pady=(20), row=2, column=1, sticky="nsew")

        self.VisualizarStatus = customtkinter.CTkButton(root, text="Visualizar\n Status")
        self.VisualizarStatus.grid(padx=(20), pady=(20), row=3, column=1, sticky="nsew")

        # self.config_db = ConfigDB()

    def geraLink(self):

        self.TipoDado = customtkinter.CTkComboBox(master=root, values=['Automático', 'Data da Cotação', 'Fornecedor', 'ID Cotação'])
        # self.TipoDado.index(0)
        self.TipoDado.grid(padx=(100, 10), pady=(30), row=1, column=2, sticky="nsew")

        self.InputDado = customtkinter.CTkEntry(root)
        self.InputDado.grid(padx=(10), pady=(30), row=1, column=3, columnspan=3, sticky="nsew")

        self.Buscar = customtkinter.CTkButton(master=root, text="Buscar", command=self.tratamento)
        self.Buscar.grid(padx=(10), pady=(30), row=1, column=6, sticky="nsew")

        self.result_tree = ttk.Treeview(self.root, columns=('Número da Cotação', 'Data da Cotação', 'Comprador', 'Fornecedor'))  # Adicione quantas colunas forem necessárias
        self.result_tree.grid(row=2, column=2, columnspan=6, rowspan=10, padx=100, pady=10, sticky="nsew")

        self.configure_treeview(self.result_tree)
        style = ttk.Style()
        style.configure("Treeview", rowheight=30)
        # Configuração das colunas da Treeview
        self.result_tree.column('#0', width=1, anchor='center')
        self.result_tree.column('#1', width=200, anchor='center')
        self.result_tree.column('#2', width=200, anchor='center')
        self.result_tree.column('#3', width=250, anchor='center')
        self.result_tree.column('#4', width=300, anchor='center')
        # Adicione os cabeçalhos das colunas
        self.result_tree.heading('#1', text='Número da Cotação')
        self.result_tree.heading('#2', text='Data da Cotação')
        self.result_tree.heading('#3', text='Comprador')
        self.result_tree.heading('#4', text='Fornecedor')
        self.result_tree.bind("<Double-1>", self.on_checkbosclick)

        self.connection = fdb.connect(host=self.hostname, database=self.database, user=self.username, password=self.password)
        self.cursor = self.connection.cursor()

    def configure_treeview(self, tree):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 14, ), background=[('active', '#d9d9d9')])  # Tamanho da fonte para os cabeçalhos das colunas
        style.configure("Treeview", font=("Arial", 12))

    def tratamento(self):
        dados = self.TipoDado.get()
        print(dados)
        if dados == 'Automático':
            self.limpar_resultados()
            valor = self.InputDado.get()
            self.cursor.execute("SELECT codcotacao, datacotacao, codcomprador FROM tcotacao WHERE codcotacao LIKE ? ",
                                (f"%{valor}%", f"%{valor}%", f"%{valor}%"))
            result = self.cursor.fetchall()
            for row in result:
                self.result_tree.insert('', customtkinter.END, values=row)

        elif dados == "Data da Cotação":
            self.limpar_resultados()
            valor = self.InputDado.get()
            self.cursor.execute("SELECT codcotacao, datacotacao, codcomprador FROM tcotacao WHERE datacotacao LIKE ?",
                                (f"%{valor}%",))
            result = self.cursor.fetchall()
            for row in result:
                self.result_tree.insert('', customtkinter.END, values=row)

        elif dados == "Fornecedor":
            self.limpar_resultados()
            valor = self.InputDado.get()
            self.cursor.execute("SELECT tc.codcotacao, tc.datacotacao, tc.codcomprador, tco.codcfo "
                                "FROM tcotacao tc JOIN tcotacaoorc tco ON tc.codcotacao = tco.codcotacao "
                                "JOIN fcfo ON tco.codcfo = fcfo.codcfo "
                                "WHERE tco.codcfo LIKE ? OR fcfo.nomefantasia LIKE ?", (f"%{valor}%", f"%{valor}%",))
            result = self.cursor.fetchall()
            for row in result:
                self.result_tree.insert('', customtkinter.END, values=row)

        else:
            self.limpar_resultados()
            valor = self.InputDado.get()
            self.cursor.execute("SELECT codcotacao, datacotacao, codcomprador FROM tcotacao WHERE codcotacao LIKE ?",
                                (f"%{valor}%",))
            result = self.cursor.fetchall()
            for row in result:
                self.result_tree.insert('', customtkinter.END, values=row)

    def limpar_resultados(self):
        for child in self.result_tree.get_children():
            self.result_tree.delete(child)

    def on_checkbosclick(self, event):
        item_id = self.result_tree.focus()
        checked = self.result_tree.item(item_id)["values"][0]
        self.aviso_area_de_trasnferencia()

    def aviso_area_de_trasnferencia(self):
        texto = "https://tga_cotacao//id_2024-02-23"
        pyperclip.copy(texto)
        item_id = self.result_tree.focus()
        values = self.result_tree.item(item_id, "values")
        messagebox.showwarning("Aviso!", f'"https://tga_cotacao//{values[0]}"\nCopiado para a area de tranferencia!')

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = MyApp(root)
    root.mainloop()
