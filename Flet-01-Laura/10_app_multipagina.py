import flet as ft

def main(page: ft.Page):
    # Configurações iniciais
    page.title = "🛍️ Loja Virtual Mini"
    page.bgcolor = ft.Colors.GREY_100
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.padding = 25

    carrinho, total_carrinho = [], 0.0

    # Área de produtos
    area_produtos = ft.GridView(expand=1, runs_count=2, max_extent=200,
                                spacing=15, run_spacing=15, child_aspect_ratio=0.9)

    # Elementos do carrinho
    contador_carrinho = ft.Text("Carrinho (0)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)
    total_texto = ft.Text("Total: R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_700)
    lista_carrinho = ft.ListView(height=180, spacing=8)
    notificacao = ft.Text("", size=14, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLUE_700)

    def mostrar_notificacao(msg, cor=ft.Colors.BLUE_700):
        notificacao.value, notificacao.color = msg, cor
        page.update()

    def atualizar_carrinho():
        nonlocal total_carrinho
        contador_carrinho.value = f"Carrinho ({len(carrinho)})"
        total_texto.value = f"Total: R$ {total_carrinho:.2f}"
        lista_carrinho.controls.clear()

        for i, item in enumerate(carrinho):
            lista_carrinho.controls.append(
                ft.Row([
                    ft.Text(item["nome"], expand=True, size=14),
                    ft.Text(f"R$ {item['preco']:.2f}", color=ft.Colors.GREEN_600, size=14),
                    ft.IconButton(ft.icons.DELETE, icon_color=ft.Colors.RED, tooltip="Remover",
                                  on_click=lambda e, idx=i: remover_do_carrinho(idx))
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
        page.update()

    def adicionar_ao_carrinho(nome, preco):
        nonlocal total_carrinho
        carrinho.append({"nome": nome, "preco": preco})
        total_carrinho += preco
        atualizar_carrinho()
        mostrar_notificacao(f"✅ {nome} adicionado ao carrinho!", ft.Colors.GREEN_700)

    def remover_do_carrinho(idx):
        nonlocal total_carrinho
        if 0 <= idx < len(carrinho):
            produto = carrinho.pop(idx)
            total_carrinho -= produto["preco"]
            atualizar_carrinho()
            mostrar_notificacao(f"❌ {produto['nome']} removido!", ft.Colors.RED_700)

    def finalizar_compra(e):
        nonlocal total_carrinho
        if carrinho:
            carrinho.clear()
            total_carrinho = 0.0
            atualizar_carrinho()
            mostrar_notificacao("🎉 Compra finalizada com sucesso!", ft.Colors.BLUE_800)
        else:
            mostrar_notificacao("⚠️ Carrinho vazio!", ft.Colors.ORANGE)

    def criar_card(nome, preco, emoji, cor):
        return ft.Container(
            content=ft.Column([
                ft.Text(emoji, size=40, text_align=ft.TextAlign.CENTER),
                ft.Text(nome, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                ft.Text(f"R$ {preco:.2f}", size=14, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
            bgcolor=cor,
            padding=15,
            border_radius=15,
            shadow=ft.BoxShadow(blur_radius=10, spread_radius=1, color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK)),
            on_click=lambda e: adicionar_ao_carrinho(nome, preco),
            ink=True,
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            width=180,
            height=190
        )

    produtos = [
        {"nome": "Smartphone", "preco": 899.99, "emoji": "📱", "cor": ft.Colors.BLUE_600},
        {"nome": "Notebook", "preco": 2499.90, "emoji": "💻", "cor": ft.Colors.RED_600},
        {"nome": "Tênis", "preco": 299.99, "emoji": "👟", "cor": ft.Colors.BLUE_700},
        {"nome": "Camiseta", "preco": 89.90, "emoji": "👕", "cor": ft.Colors.RED_700},
        {"nome": "Livro", "preco": 45.00, "emoji": "📚", "cor": ft.Colors.BLUE_500},
        {"nome": "Fone", "preco": 199.99, "emoji": "🎧", "cor": ft.Colors.RED_500},
    ]

    for p in produtos:
        area_produtos.controls.append(criar_card(p["nome"], p["preco"], p["emoji"], p["cor"]))

    # Layout da página
    page.add(
        ft.Column([
            ft.Text("🛍️ Loja Virtual Mini", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
            ft.Text("Escolha seus produtos favoritos!", size=16, color=ft.Colors.GREY_700),
            ft.Container(content=area_produtos, padding=10, border_radius=12, bgcolor=ft.Colors.WHITE),
            ft.Divider(height=20, color=ft.Colors.GREY_300),
            ft.Container(
                content=ft.Column([
                    ft.Row([contador_carrinho, total_texto], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    lista_carrinho,
                    ft.Row([
                        ft.ElevatedButton("🛒 Finalizar Compra", on_click=finalizar_compra,
                                          bgcolor=ft.Colors.RED_600, color=ft.Colors.WHITE, width=220)
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    notificacao
                ], spacing=15),
                padding=20,
                border_radius=12,
                bgcolor=ft.Colors.WHITE,
                shadow=ft.BoxShadow(blur_radius=8, spread_radius=1, color=ft.Colors.with_opacity(0.15, ft.Colors.BLACK))
            )
        ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
