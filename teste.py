import tkinter as tk

 

class Node:

    def __init__(self, key):

        self.key = key

        self.left = None

        self.right = None

        self.height = 1

 

class AVLTree:

    def insert(self, root, key):

        if not root:

            return Node(key)

        elif key < root.key:

            root.left = self.insert(root.left, key)

        else:

            root.right = self.insert(root.right, key)

 

        root.height = 1 + max(self.get_height(root.left),

                              self.get_height(root.right))

 

        balance = self.get_balance(root)

 

        # Casos de rotação

        # Left Left

        if balance > 1 and key < root.left.key:

            return self.right_rotate(root)

        # Right Right

        if balance < -1 and key > root.right.key:

            return self.left_rotate(root)

        # Left Right

        if balance > 1 and key > root.left.key:

            root.left = self.left_rotate(root.left)

            return self.right_rotate(root)

        # Right Left

        if balance < -1 and key < root.right.key:

            root.right = self.right_rotate(root.right)

            return self.left_rotate(root)

 

        return root

 

    def left_rotate(self, z):

        y = z.right

        T2 = y.left

 

        y.left = z

        z.right = T2

 

        z.height = 1 + max(self.get_height(z.left),

                           self.get_height(z.right))

        y.height = 1 + max(self.get_height(y.left),

                           self.get_height(y.right))

 

        return y

 

    def right_rotate(self, z):

        y = z.left

        T3 = y.right

 

        y.right = z

        z.left = T3

 

        z.height = 1 + max(self.get_height(z.left),

                           self.get_height(z.right))

        y.height = 1 + max(self.get_height(y.left),

                           self.get_height(y.right))

 

        return y

 

    def get_height(self, node):

        if not node:

            return 0

        return node.height

 

    def get_balance(self, node):

        if not node:

            return 0

        return self.get_height(node.left) - self.get_height(node.right)

 

class AVLTreeGUI:

    def __init__(self, master):

        self.master = master

        self.avl = AVLTree()

        self.root = None

 

        master.title("Visualizador de Árvore AVL")

 

        # Configuração da interface

        self.frame = tk.Frame(master)

        self.frame.pack(pady=10)

 

        self.label = tk.Label(self.frame, text="Insira elementos separados por espaço:")

        self.label.pack(side=tk.LEFT)

 

        self.entry = tk.Entry(self.frame, width=30)

        self.entry.pack(side=tk.LEFT, padx=5)

 

        self.btn_inserir = tk.Button(self.frame, text="Inserir", command=self.inserir)

        self.btn_inserir.pack(side=tk.LEFT)

 

        self.canvas = tk.Canvas(master, width=800, height=600, bg='white')

        self.canvas.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

 

    def inserir(self):

        elementos = self.entry.get().split()

        for elem in elementos:

            if elem.isdigit():

                self.root = self.avl.insert(self.root, int(elem))

        self.desenhar_arvore()

 

    def desenhar_arvore(self):

        self.canvas.delete("all")

        if not self.root:

            return

 

        # Obter níveis da árvore

        niveis = []

        fila = [(self.root, 0)]

        while fila:

            no, nivel = fila.pop(0)

            if len(niveis) <= nivel:

                niveis.append([])

            niveis[nivel].append(no)

            if no.left:

                fila.append((no.left, nivel + 1))

            if no.right:

                fila.append((no.right, nivel + 1))

 

        # Calcular posições

        posicoes = {}

        largura = self.canvas.winfo_width()

        altura = self.canvas.winfo_height()

        raio = 20

        espaco_vertical = 80

 

        for i, nivel in enumerate(niveis):

            y = 30 + i * espaco_vertical

            num_nos = len(nivel)

            espaco_horizontal = largura / (num_nos + 1)

            for j, no in enumerate(nivel):

                x = espaco_horizontal * (j + 1)

                posicoes[no] = (x, y)

 

        # Desenhar conexões

        for no in posicoes:

            x, y = posicoes[no]

            if no.left and no.left in posicoes:

                x_esq, y_esq = posicoes[no.left]

                self.canvas.create_line(x, y + raio, x_esq, y_esq - raio, width=2)

            if no.right and no.right in posicoes:

                x_dir, y_dir = posicoes[no.right]

                self.canvas.create_line(x, y + raio, x_dir, y_dir - raio, width=2)

 

        # Desenhar nós

        for no in posicoes:

            x, y = posicoes[no]

            self.canvas.create_oval(

                x - raio, y - raio,

                x + raio, y + raio,

                fill="lightblue", outline="black"

            )

            self.canvas.create_text(x, y, text=str(no.key), font=('Arial', 10, 'bold'))

 

if __name__ == "__main__":

    root = tk.Tk()

    app = AVLTreeGUI(root)

    root.mainloop()

 