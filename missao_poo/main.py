from produto import Produto, ProdutoNacional, ProdutoImportado
from funcionario import FuncionarioCLT, FuncionarioPJ

produtos = [
ProdutoNacional("Teclado", 100.0, 20),
ProdutoImportado("Celular", 2000.0, 5, 0.15),
Produto("Mouse", 50.0, 30)
]

funcionarios = [
FuncionarioCLT("João Silva", 3000.0),
FuncionarioPJ("Maria Souza", 160, 50.0)
]

print("=== Detalhes dos Produtos ===")
for produto in produtos:
    produto.exibir_detalhes()
print(f"Preço final: R${produto.preco_final():.2f}")
produto.emitir_nota()
print()

print("=== Operações de Estoque ===")
produtos[0].vender(5)
produtos[1].repor(3)
print()

print("=== Pagamento de Funcionários ===")
for funcionario in funcionarios:
    print(f"{funcionario.nome}: R${funcionario.calcular_pagamento():.2f}")