
"""

defina três variáveis
nome_maquina,tempo_uso,ligado
crie um programa que leia esses valores
e mostre os valores e seus tipos.

passo 1: definir três variáveis
nome_maquina,
tempo_uso,
ligado
passo 2: ler os os valores
criar caixas de texto
nome_text = ft.TextField()

passo 3: mostrar os valores
def btn_click()
btn = ft....
msg =  ft.Text()
 
"""
import flet as ft
def main(page:ft.Page):
   #passo 1 - ok
   nome_maquina=""
   tempo_uso=0
   ligado = False
   #passo 2 - ?
   nome_text = ft.TextField(color="black")
   tempo_text = ft.TextField(color="black")
   ligado_text = ft.TextField(color="black")
   page.window_width =  250
   page.window_height= 400
   page.bgcolor = "White"

   #passo 3 - mostrar os valores
   #FIXME:definir um click
   #FIXME: definir um botão com click
   #FIXME: mostrar a mensagem
   msg_1 = ft.Text(color="black") 
   msg_2 = ft.Text(color="black") 
   msg_3 = ft.Text(color="black") 
   def btn_click(e):
      nome = nome_text.value
      tempo = int(tempo_text.value)
      ligado = bool(ligado_text.value)
      msg_1.value = f"nome: {nome} o tipo é:{type(nome)}"
      msg_2.value = f"tempo: {tempo} o tipo é:{type(tempo)}"
      msg_3.value = f"ligado: {ligado} o tipo é:{type(ligado)}"
      page.update()     
      
   
   btn = ft.ElevatedButton("clique aqui",on_click=btn_click)
   page.add(nome_text,tempo_text,ligado_text,btn,msg_1,msg_2,msg_3)
   page.update()
ft.app(target=main)

