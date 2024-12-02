import flet as ft

def main(page: ft.Page):
    page.title = "Flet App con Dos Columnas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    

    # Primera columna con una imagen
    columna_imagen = ft.Column([
        ft.Image(src=f"/icons/icon-512.png", width=200, height=200),
    ], expand=False)
    

    # Segunda columna con dos campos de texto y un botón
    def boton_click(e):
        # Aquí puedes definir lo que sucede cuando se hace clic en el botón
        pass

    columna_formulario = ft.Column([
        ft.TextField(label="Campo 1", width=200),
        ft.TextField(label="Campo 2", width=200),
        ft.ElevatedButton("Enviar", on_click=boton_click)
    ], expand=True)


    # Añade las columnas a una fila y luego a la página
    page.add(ft.Row([columna_imagen, columna_formulario]))

ft.app(main)