import flet as ft

#Se importa la librería random
import random

def main(page: ft.Page):
    #Se crean las variables globales
    global numero_secreto,estrada_numero,text_resultado,boton_adivina
    
    page.title = "Adivina el número"
    
    numero_secreto = random.randint(1,100)
    
    titulo=ft.Text("Adivina el número",size=25,color="white")
    estrada_numero=ft.TextField(label="Tu adivinanza entre 1 y 100",width=300)
    boton_adivina=ft.ElevatedButton("Adivinar")
    text_resultado=ft.Text("",color="white")
    
    #Se crea el contenedor de la interfaz grafíca
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                estrada_numero,
                boton_adivina,
                text_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=300
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="black",
        width=page.window.width,
        height=page.window.height,
        padding=20
    )
    
    page.add(contenedor_principal)


ft.app(main)
