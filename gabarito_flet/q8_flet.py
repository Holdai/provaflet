import flet as ft
from questao_07_flet import Carro

def main(page: ft.Page):
    # Cria um campo de texto para o nome do carro
    nome_tf = ft.TextField(label="Nome do carro:", max_lines=1)

    # Cria um campo de texto para a marca do carro
    marca_tf = ft.TextField(label="Marca do carro:", max_lines=1)

    # Cria um Text para exibir o carro criado
    carro_text = ft.Text()

    def criar_carro(e):
        # Cria um novo objeto Carro
        carro = (nome_tf.value, marca_tf.value)

        # Exibe o carro criado
        carro_text.value = f"Carro criado: {carro}"

        # Atualiza a página
        page.update()

    # Cria um botão para criar um novo carro
    criar_btn = ft.ElevatedButton("Criar carro", on_click=criar_carro)

    # Adiciona os widgets à página
    page.add(nome_tf, marca_tf, criar_btn, carro_text)

ft.app(target=main)
