class Produto:
    def init(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

def exibir_detalhes(self):
    print(f"Produto: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque} unidades")

def preco_final(self):
    return self.preco

def emitir_nota(self):
    print(f"Nota gerada para {self.nome}.")

def repor(self, quantidade):
    self.estoque += quantidade
    print(f"Estoque de {self.nome} reposto. Novo estoque: {self.estoque} unidades")

def vender(self, quantidade):
    if quantidade > self.estoque:
        print(f"Estoque insuficiente de {self.nome}. Estoque atual: {self.estoque} unidades")
    else:
        self.estoque -= quantidade
        print(f"Venda de {quantidade} unidades de {self.nome} realizada. Estoque restante: {self.estoque} unidades")
class ProdutoNacional(Produto):
    def init(self, nome, preco, estoque):
        super().init(nome, preco, estoque)

def emitir_nota(self):
    print(f"Nota fiscal nacional para {self.nome}.")

class ProdutoImportado(Produto):
    def init(self, nome, preco, estoque, taxa_importacao):
        super().init(nome, preco, estoque)
        self.taxa_importacao = taxa_importacao

def preco_final(self):
    return self.preco + (self.preco * self.taxa_importacao)

def emitir_nota(self):
    print(f"Nota de importação para {self.nome} com taxa aplicada.")