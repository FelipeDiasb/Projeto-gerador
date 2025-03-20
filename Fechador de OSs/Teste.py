import flet as ft
import time



def main(page: ft.Page):
    # O código principal da nossa aplicação será inserido aqui
    pass

ft.app(target=main)


def main(page: ft.Page):

    # Função para fechar o banner de notificação
    def close_banner(e):
        page.banner.open = False
        page.update()

    # Configurações da página
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text("Calculadora IMC"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT
    )

    page.window_width = 400
    page.window_height = 550

    # Configuração do banner de notificação
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text("Ops, preencha todos os campos?"),
        actions=[
            ft.TextButton("Ok", on_click=close_banner),
        ],
    )

    # Layout da página
    layout = ft.ResponsiveRow(
        [  
            ft.Container(
                padding=5,
                col={"sm":4, "md": 4, "xl": 4},
                alignment=ft.alignment.center,
            ),
            ft.Container(
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            ft.Container(
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            ft.Container(
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            ft.Container(
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
        ],
    )

    # Adicionar o layout à página
    page.add(layout)

     # Entrada de altura, peso e gênero
    altura = ft.TextField(label="Altura", hint_text="Por favor insira sua altura")
    peso = ft.TextField(label="Peso", hint_text="Por favor insira seu peso")
    genero = ft.Dropdown(
        label="Gênero",
        hint_text="Escolha seu gênero?",
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
        ],
        #autofocus=True,
    )

    # Botão para calcular o IMC
    b_calcular = ft.ElevatedButton(text="Calcular IMC")

    # Exibição do IMC e resultados
    IMC = ft.Text("Seu IMC é ...", size=30)
    detalhes = ft.Text("Insira seus dados", size=20)

    img_capa = ft.Image(
        src=f"logo.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    info_app_resultado = ft.Column(
        controls=[
            IMC,
            detalhes,
        ])

    img_resultado = ft.Image(
        src=f"logo.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    info = ft.Row(
        controls=[
            info_app_resultado,
            img_resultado,
        ])
    

    # Layout da página
    layout = ft.ResponsiveRow(
        [  
            ft.Container(
                info,
                padding=5,
                col={"sm":4, "md": 4, "xl": 4},
                alignment=ft.alignment.center,
            ),

            ft.Container(
                altura,
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            ft.Container(
                peso,
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            ft.Container(
                genero,
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            ft.Container(
                b_calcular,
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
        ],
    )

    def calcular(e):
    # Verificar se os campos de peso, altura e gênero estão preenchidos
    if peso.value == "" or altura.value == "" or genero.value == "":
        # Mostrar notificação de erro
        page.banner.open = True
        page.update()
    else:
        valor_peso = float(peso.value)
        valor_altura = float(altura.value)

        # Calcular o IMC
        imc = valor_peso / (valor_altura * valor_altura)
        imc = float(f"{imc:.2f}")

        # Exibir o valor do IMC
        IMC.value = f"Seu IMC é {imc}"

        # Determinar a imagem correspondente ao resultado do IMC e fornecer detalhes
        if genero.value == "Feminino":
            if imc < 18.5:
                img_resultado.src = f"10.png"
                detalhes.value = 'Abaixo do peso'
            elif 18.5 <= imc < 24.9:
                img_resultado.src = f"8.png"
                detalhes.value = 'Peso Saudável'
            elif 25 <= imc < 29.9:
                img_resultado.src = f"6.png"
                detalhes.value = 'Sobrepeso ou Pré-Obeso'
            elif 30 <= imc < 34.9:
                img_resultado.src = f"4.png"
                detalhes.value = 'Obeso'
            else:
                img_resultado.src = f"2.png"
                detalhes.value = 'Severamente obeso'
        else:
            if imc < 18.5:
                img_resultado.src = f"9.png"
                detalhes.value = 'Abaixo do peso'
            elif 18.5 <= imc < 24.9:
                img_resultado.src = f"7.png"
                detalhes.value = 'Peso Saudável'
            elif 25 <= imc < 29.9:
                img_resultado.src = f"5.png"
                detalhes.value = 'Sobrepeso ou Pré-Obeso'
            elif 30 <= imc < 34.9:
                img_resultado.src = f"3.png"
                detalhes.value = 'Obeso'
            else:
                img_resultado.src = f"1.png"
                detalhes.value = 'Severamente obeso'

        # Limpar os campos de entrada
        peso.value = ""
        altura.value = ""
        genero.value = ""

        # Atualizar a página
        page.update()

    # Adicionar o layout à página
    page.add(layout)
