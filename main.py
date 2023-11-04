# Importa a classe Interface
from interface import Interface
from bd import BD

# Classe principal do programa
interface = Interface()

opcao = ""
while opcao != 0:
    interface.logotipo()
    interface.mostraMenuPrincipal()
    opcao = interface.selecionaOpcao([1, 2, 0])
    interface.LimpaTela()

    # Tela de cadastro de filmes
    if opcao == 1:
        interface.mostraCadastroFilmes()
    opcao == ""
    interface.LimpaTela()

    # Tela de lista de filmes
    if opcao == 2:
        # Mostrar tela par lista de filmes
        interface.mostraListaFilmes()
        opcao = ""
        interface.LimpaTela()
        
