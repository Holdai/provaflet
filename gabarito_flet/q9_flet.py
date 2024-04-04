import flet as ft

def main(page: ft.Page):

    elementos = ("Eu", "Tu", "Ele")

    for elementos in elementos:
        page.add(ft.Text(elementos))

ft.app(target=main)
#Essa tupla pode ser modificada? #NOTE - Não
