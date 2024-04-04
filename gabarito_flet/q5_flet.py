import flet as ft

def main(page: ft.Page): 
    #definição do objeto página
    #Text - Títilo
    #TextField - caixinha de texto
    #button - (entrar no site flet.dev, ir na parte de configuração lá tem os tipos de botões)
    texto=ft.TextField(
        label="Informe um de 1 a 12: ",
        width=222,
        height=55,
    )
    def clique_btn(e): # e = evento 
        
        dia_escolhido = texto.value
        match dia_escolhido:
            case "1":
                print("Janeiro")
                page.update()
            case "2":
                print("Fevereiro")
                page.update()
            case "3":
                print("Março")
                page.update()
            case "4":
                print("Abril")
                page.update()
            case "5":
                print("Maio")
                page.update()
            case "6":
                print("Junho")
                page.update()
            case "7":
                print("Julho")
                page.update()
            case "8":
                print("Agosto")
                page.update()
            case "9":
                print("Setembro")
                page.update()
            case "10":
                print("Outubro")
                page.update()
            case "11":
                print("Novembro")
                page.update()
            case "12":
                print("Dezembro")
                page.update()
            case _:
                print("Dia inválido. Digite um número de 1 a 12.")
                page.update()
    btn = ft.ElevatedButton("Qual é o mês?",on_click=clique_btn)
    page.add(texto,btn)

    pass

ft.app(target=main)
