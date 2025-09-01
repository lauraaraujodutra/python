import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro Botão"
    page.padding = 20
    
    # criando um texto que será modificado pelo botão
    mensagem = ft.Text(
        value="Clique no botão abaixo",
        size=20,
        text_align=ft.TextAlign.CENTER
    )
    
    # função que será executada quando o botão for clicado
    def botao_clicado(evento):
        mensagem.value = "Parabéns! Você clicou no botão! 🎉"
        mensagem.color = "green"  # usando string para cor, compatível com qualquer versão
        page.update()

    # criando nosso botão
    meu_botao = ft.ElevatedButton(
        text="Clique em mim!",
        on_click=botao_clicado,  # associando a função ao evento de clique
        width=200,
        height=50,
    )

    # adicionando os elementos à página
    page.add(mensagem)
    page.add(meu_botao)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
