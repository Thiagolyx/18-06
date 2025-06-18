class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def eh_antigo(self):
        return self.ano < 2000


livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
print(f"{livro1.titulo} é antigo?", livro1.eh_antigo())

