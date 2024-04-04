import flet as ft

def main(page:ft.Page):
     #confiurar pagina
     page.window_widitch = 500
     page.window_height = 500
     #criar um componente Text() - titulo de texto
     titulo = ft.Text("alô Mundo")
     #adiciona o titulo na pagina
     page.add(titulo)
     page.horizontal_alignment 
     page.update()

ft.app(target=main)
