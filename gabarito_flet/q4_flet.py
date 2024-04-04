import flet as ft

def main(page: ft.Page): 
    #definição do objeto página
    #Text - Títilo
    #TextField - caixinha de texto
    #button - (entrar no site flet.dev, ir na parte de configuração lá tem os tipos de botões)
    texto=ft.TextField(
        label="Informe um de 1 a 7: ",
        width=222,
        height=55,
    )
    def clique_btn(e): # e = evento 
        
        dia_escolhido = texto.value
        match dia_escolhido:
            case "1":
                print("Hoje é Domingo")
                page.update()
            case "2":
                print("Hoje é Segunda-feira")
                page.update()
            case "3":
                print("Hoje é Terça-feira")
                page.update()
            case "4":
                print("Hoje é Quarta-feira")
                page.update()
            case "5":
                print("Hoje é Quinta-feira")
                page.update()
            case "6":
                print("Hoje é Sexta-feira")
                page.update()
            case "7":
                print("Hoje é Sábado")
                page.update()
            case _:
                print("Dia inválido. Digite um número de 1 a 7.")
                page.update()
    btn = ft.ElevatedButton("Qual dia da semana é hoje?",on_click=clique_btn)
    page.add(texto,btn)

    pass

ft.app(target=main)                                                                 