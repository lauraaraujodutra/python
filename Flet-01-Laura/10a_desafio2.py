import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Completa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.bgcolor = ft.Colors.BLACK

    # Display da calculadora
    display = ft.Text(
        value="0",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.RIGHT,
        expand=True
    )

    historico = ft.Text(
        value="",
        size=20,
        color=ft.Colors.GREY_400,
        text_align=ft.TextAlign.RIGHT,
        expand=True
    )

    valor_atual = "0"
    valor_anterior = ""
    operador = ""

    def atualizar_display():
        display.value = valor_atual
        historico.value = f"{valor_anterior} {operador}"
        page.update()

    def limpar(e):
        nonlocal valor_atual, valor_anterior, operador
        valor_atual = "0"
        valor_anterior = ""
        operador = ""
        atualizar_display()

    def adicionar_numero(e):
        nonlocal valor_atual
        numero = e.control.text
        if valor_atual == "0":
            valor_atual = numero
        else:
            valor_atual += numero
        atualizar_display()

    def adicionar_ponto(e):
        nonlocal valor_atual
        if "." not in valor_atual:
            valor_atual += "."
        atualizar_display()

    def selecionar_operador(e):
        nonlocal valor_atual, valor_anterior, operador
        if valor_atual != "":
            valor_anterior = valor_atual
            operador = e.control.text
            valor_atual = "0"
        atualizar_display()

    def calcular(e):
        nonlocal valor_atual, valor_anterior, operador
        try:
            if operador == "+":
                resultado = float(valor_anterior) + float(valor_atual)
            elif operador == "-":
                resultado = float(valor_anterior) - float(valor_atual)
            elif operador == "×":
                resultado = float(valor_anterior) * float(valor_atual)
            elif operador == "÷":
                if float(valor_atual) != 0:
                    resultado = float(valor_anterior) / float(valor_atual)
                else:
                    resultado = "Erro"
            else:
                resultado = valor_atual

            valor_atual = str(resultado)
            valor_anterior = ""
            operador = ""
            atualizar_display()
        except:
            valor_atual = "Erro"
            atualizar_display()

    def apagar(e):
        nonlocal valor_atual
        valor_atual = valor_atual[:-1] if len(valor_atual) > 1 else "0"
        atualizar_display()

    # Função para criar botões
    def criar_botao(texto, cor=ft.Colors.BLUE_GREY_800, expand=1, func=None):
        return ft.ElevatedButton(
            texto,
            on_click=func,
            bgcolor=cor,
            color=ft.Colors.WHITE,
            width=70,
            height=70,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10)
            ),
            expand=expand
        )

    # Layout dos botões
    botoes = [
        [("C", ft.Colors.RED_400, limpar), ("⌫", ft.Colors.BLUE_GREY_600, apagar), ("%", ft.Colors.BLUE_GREY_600, selecionar_operador), ("÷", ft.Colors.ORANGE, selecionar_operador)],
        [("7", ft.Colors.BLUE_GREY_800, adicionar_numero), ("8", ft.Colors.BLUE_GREY_800, adicionar_numero), ("9", ft.Colors.BLUE_GREY_800, adicionar_numero), ("×", ft.Colors.ORANGE, selecionar_operador)],
        [("4", ft.Colors.BLUE_GREY_800, adicionar_numero), ("5", ft.Colors.BLUE_GREY_800, adicionar_numero), ("6", ft.Colors.BLUE_GREY_800, adicionar_numero), ("-", ft.Colors.ORANGE, selecionar_operador)],
        [("1", ft.Colors.BLUE_GREY_800, adicionar_numero), ("2", ft.Colors.BLUE_GREY_800, adicionar_numero), ("3", ft.Colors.BLUE_GREY_800, adicionar_numero), ("+", ft.Colors.ORANGE, selecionar_operador)],
        [("0", ft.Colors.BLUE_GREY_800, adicionar_numero), (".", ft.Colors.BLUE_GREY_800, adicionar_ponto), ("=", ft.Colors.GREEN_400, calcular)]
    ]

    # Adiciona display e botões na tela
    page.add(
        ft.Column(
            [
                historico,
                display,
                ft.Divider(height=1, color=ft.Colors.GREY),
                *[
                    ft.Row(
                        [criar_botao(txt, cor, func=func) for txt, cor, func in linha],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        spacing=10
                    )
                    for linha in botoes
                ]
            ],
            spacing=10,
            expand=True
        )
    )

    atualizar_display()

ft.app(target=main)
