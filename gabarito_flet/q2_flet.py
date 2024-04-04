import flet as ft

def main(page:ft.Page):
     #confiurar pagina
     page.window_width = 500
     page.window_height = 500
     
     #criar um componente Text() - titulo de texto
     titulo = ft.Text("cadastro aluno")
     nome_txt = ft.TextField(width=150)
     #botão
     def btn_click(e):
          titulo.value = nome_txt.value
          page.update()
     btn = ft.ElevatedButton("Clique aqui",on_click=btn_click)
     #adiciona o titulo na pagina
     page.add(titulo,nome_txt,btn)
     
     page.update()

ft.app(target=main)