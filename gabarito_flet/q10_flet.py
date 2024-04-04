import flet as ft

def main(page: ft.Page):

    lista = ["Java", "Python", "C#"]

    for lista in lista:
        page.add(ft.Text(lista))

ft.app(target=main)

#Executou? #NOTE - Sim 
#Elas se parecem né verdade? #NOTE - Sim
#Qual diferença técnica entre ela (tupla e lista)? #NOTE - A utilização de colchetes
