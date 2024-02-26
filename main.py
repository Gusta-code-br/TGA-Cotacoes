import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import fdb
import hashlib
import pyperclip


class MyApp:

    def __init__(self, root):
        self.root = root
        self.root.title("TGA - Cotação")

        self.UserName = tk.Label(root, text="Usuário: ")
        self.UserName.grid(padx=(20), pady=(0), row=0, column=1, sticky="nsew")
        self.PassWord = tk.Label(root, text="Senha: ")
        self.PassWord.grid(padx=(20), pady=(0), row=1, column=1, sticky="nsew")
        self.EntryUser = tk.Entry(root)
        self.EntryUser.grid(padx=(20), pady=(0), row=0, column=2, sticky="nsew")
        self.EntryPass = tk.Entry(root, show="*")
        self.EntryPass.grid(padx=(20), pady=(20), row=1, column=2, sticky="nsew")

        self.ButtonBD = tk.Button(root, text="DB", command=self.database)
        self.ButtonBD.grid(padx=(10), pady=(10), row=3, column=1, sticky="nsew")
        self.GetIn = tk.Button(root, text="Login", command=self.tela_inicial)
        self.GetIn.grid(padx=(10), pady=(10), row=3, column=2, sticky="nsew")

    def database(self):
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

        self.connection = fdb.connect(host='localhost', database='C:\TGA\Dados\TGA.FDB', user='SYSDBA',
                                      password='masterkey')
        self.cursor = self.connection.cursor()
        query = f"SELECT * FROM gusuarios WHERE nome = '{nome}' AND senha = '{senha_hash}'"
        self.cursor.execute(query)
        #self.cursor.execute(, (f"%{nome}%", f"%{senha_hash}%",))
        if(self.cursor.fetchall()):
            TelaInicial(root)
        else:
            messagebox.showinfo("Erro de login", "Usuário e senha não compátiveis")
            MyApp(root)


class ConfigDB:
    def __init__(self, root):
        self.root = root

        self.UserName = tk.Label(text="Usuário: ")
        self.UserName.grid(padx=(20), pady=(0), row=0, column=1, sticky="nsew")
        self.PassWord = tk.Label(text="Senha: ")
        self.PassWord.grid(padx=(20), pady=(0), row=1, column=1, sticky="nsew")
        self.EntryUser = tk.Entry()
        self.EntryUser.insert(0, "SYSDBA")
        self.EntryUser.grid(padx=(20), pady=(0), row=0, column=2, sticky="nsew")
        self.EntryPass = tk.Entry(show="*")
        self.EntryPass.insert(0, "masterkey")
        self.EntryPass.grid(padx=(20), pady=(20), row=1, column=2, sticky="nsew")

        self.CaminhoLabel = tk.Label(text="Caminho: ")
        self.CaminhoLabel.grid(padx=(10), pady=(10), row=3, column=1, sticky="nsew")
        self.CaminhoDB = tk.Entry()
        self.CaminhoDB.insert(0, "D:\TGA\TGA.FDB")
        self.CaminhoDB.grid(padx=(10), pady=(10), row=3, column=2, sticky="nsew")

        self.conection = tk.Button(text="Conectar", command=self.connect)
        self.conection.grid(padx=(10), pady=(10), row=4, column=1, sticky="nsew")

        self.GetBack = tk.Button(text="Voltar", command=self.voltar)
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
                'database': self.path,  # Caminho para seu banco de dados Firebird
                'user': self.user,
                'password': self.password,
            }
            con = fdb.connect(**parametros_conexao)

            messagebox.showinfo("Conexão bem-sucedida", "Conexão ao Firebird realizada com sucesso!")

            # Fechar a conexão
            con.close()
        except Exception as e:
            messagebox.showerror("Erro de conexão", f"Ocorreu um erro ao conectar ao Firebird:\n{str(e)}")


class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("TGA - Cotação")

        self.GerarLink = tk.Button(text="Gerar \n Link", command=self.geraLink)
        self.GerarLink.grid(padx=(20), pady=(20), row=1, column=1, sticky="nsew")

        self.RespostaFornecedor = tk.Button(text="Resposta do \n Fornecedor")
        self.RespostaFornecedor.grid(padx=(20), pady=(20), row=2, column=1, sticky="nsew")

        self.VisualizarStatus = tk.Button(text="Visualizar\n Status")
        self.VisualizarStatus.grid(padx=(20), pady=(20), row=3, column=1, sticky="nsew")

        # self.config_db = ConfigDB()

    def geraLink(self):

        self.TipoDado = ttk.Combobox(root, values=['Automático', 'Data da Cotação', 'Fornecedor', 'ID Cotação'])
        # self.TipoDado.index(0)
        self.TipoDado.grid(padx=(100, 10), pady=(30), row=1, column=2, sticky="nsew")

        self.InputDado = tk.Entry()
        self.InputDado.grid(padx=(10), pady=(30), row=1, column=3, columnspan=3, sticky="nsew")

        self.Buscar = tk.Button(text="Buscar", command=self.tratamento)
        self.Buscar.grid(padx=(10), pady=(30), row=1, column=6, sticky="nsew")

        self.result_tree = ttk.Treeview(self.root, columns=('Número da Cotação', 'Data da Cotação', 'Comprador', 'Fornecedor'))  # Adicione quantas colunas forem necessárias
        self.result_tree.grid(row=2, column=2, columnspan=6, rowspan=6, padx=100, pady=10, sticky="nsew")

        # Configuração das colunas da Treeview
        self.result_tree.column('#0', width=1, anchor='center')
        self.result_tree.column('#1', width=180, anchor='center')
        self.result_tree.column('#2', width=100, anchor='center')
        self.result_tree.column('#3', width=200, anchor='center')
        self.result_tree.column('#4', width=250, anchor='center')
        # Adicione os cabeçalhos das colunas
        self.result_tree.heading('#1', text='Número da Cotação')
        self.result_tree.heading('#2', text='Data da Cotação')
        self.result_tree.heading('#3', text='Comprador')
        self.result_tree.heading('#4', text='Fornecedor')
        self.result_tree.bind("<Double-1>", self.on_checkbosclick)

        self.connection = fdb.connect(host='localhost', database='C:\TGA\Dados\TGA.FDB', user='SYSDBA', password='masterkey')
        self.cursor = self.connection.cursor()

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
                self.result_tree.insert('', tk.END, values=row)

        elif dados == "Data da Cotação":
            self.limpar_resultados()
            valor = self.InputDado.get()
            self.cursor.execute("SELECT codcotacao, datacotacao, codcomprador FROM tcotacao WHERE datacotacao LIKE ?",
                                (f"%{valor}%",))
            result = self.cursor.fetchall()
            for row in result:
                self.result_tree.insert('', tk.END, values=row)

        elif dados == "Fornecedor":
            self.limpar_resultados()
            valor = self.InputDado.get()
            self.cursor.execute("SELECT tc.codcotacao, tc.datacotacao, tc.codcomprador, tco.codcfo "
                                "FROM tcotacao tc JOIN tcotacaoorc tco ON tc.codcotacao = tco.codcotacao "
                                "WHERE tco.codcfo LIKE ? OR tco.nomefantasia LIKE ?", (f"%{valor}%",))
            result = self.cursor.fetchall()
            for row in result:
                self.result_tree.insert('', tk.END, values=row)

        else:
            self.limpar_resultados()
            valor = self.InputDado.get()
            self.cursor.execute("SELECT codcotacao, datacotacao, codcomprador FROM tcotacao WHERE codcotacao LIKE ?",
                                (f"%{valor}%",))
            result = self.cursor.fetchall()
            for row in result:
                self.result_tree.insert('', tk.END, values=row)

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
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
