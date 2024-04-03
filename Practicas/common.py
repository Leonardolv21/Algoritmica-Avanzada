import tkinter as tk

class MenuJuego:
    def __init__(self, ventana, db):
        self.ventana = ventana
        self.db = db  
        self.saldos_jugadores = {}  # Diccionario para almacenar los saldos de los jugadores
        self.menu_inicial()

    def menu_inicial(self):
        self.ventana.title("Clicker Game")  # Establece el título de la ventana después de que esté completamente construida
        self.ventana.geometry("800x900")
        self.ventana.configure(bg="gray")
        self.menu_frame = tk.Frame(self.ventana, bg="black")
        self.menu_frame.pack(expand=True)

        self.etiqueta_titulo = tk.Label(self.menu_frame, text="Menú Inicial", font=("Arial", 20), fg="white", bg="black")
        self.etiqueta_titulo.pack(pady=20)

        self.boton_registrar = tk.Button(self.menu_frame, text="Registrarse", font=("Arial", 14), bg="black", fg="white", command=self.abrir_registro)
        self.boton_registrar.pack(pady=10)

        self.boton_iniciar_sesion = tk.Button(self.menu_frame, text="Iniciar Sesión", font=("Arial", 14), bg="black", fg="white", command=self.abrir_inicio_sesion)
        self.boton_iniciar_sesion.pack(pady=10)

        self.boton_salir = tk.Button(self.menu_frame, text="Salir", font=("Arial", 14), bg="black", fg="white", command=self.salir)
        self.boton_salir.pack(pady=10)

    def abrir_registro(self):
        from registroylogin import RegistroVentana  # Importar aquí para evitar la circularidad
        ventana_registro = tk.Toplevel(self.ventana)
        registro_ventana = RegistroVentana(ventana_registro, self.db)

    def abrir_inicio_sesion(self):
        from registroylogin import InicioSesionVentana  # Importar aquí para evitar la circularidad
        ventana_inicio_sesion = tk.Toplevel(self.ventana)
        inicio_sesion_ventana = InicioSesionVentana(ventana_inicio_sesion, self.db, self.mostrar_menu)

    def mostrar_menu(self):
     self.ventana.destroy()  # Cierra la ventana de inicio de sesión
     juego_ventana = tk.Tk()  # Crea una nueva ventana para el juego
     from gameClicker import gameClicker
     
     juego = gameClicker(juego_ventana, self.db, self.mostrar_menu)  # Inicializa el juego en la nueva ventana
     juego_ventana.mainloop()  # Inicia el bucle principal del juego


    def salir(self):
        self.ventana.quit()
        self.ventana.destroy()
        
    def establecer_titulo_ventana(self, titulo):
        self.ventana.title(titulo)