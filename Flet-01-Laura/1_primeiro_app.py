import flet as ft

def main(page: ft.Page):
    page.title = "Meu primeiro App Flet"
    page.padding = 20
    
    meu_texto = ft.Text(
        value="🎉 Oi, eu sou a Laurinha (Primeiro app com Flet!)",
        size=24,
        color=ft.Colors.BLUE,   # <<-- corrigido aqui
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    page.add(
        meu_texto,
        ft.Text("Bem-vindos ao mundo da Laurinha!", size=16),
        ft.Text("Estou aprendendo a criar apps com Flet!", size=16, color=ft.Colors.BLUE), # corrigido aqui também
    )

ft.app(target=main)
