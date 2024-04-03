import tkinter as tk
from tkinter import messagebox
from dbjuegoclic import PostgreSQLDatabase

class JuegoClicker:
    def __init__(self, ventana, saldos_jugadores, mostrar_menu):
        self.ventana = ventana
        self.ventana.title("Clicker Game")
        self.ventana.geometry("800x900")
        self.ventana.configure(bg="gray")  

        self.saldos_jugadores = saldos_jugadores  
        self.mostrar_menu = mostrar_menu  

        self.nickname = None  
        self.puntaje_maximo = 0
        self.tiempo_restante = 20
        self.temporizador = None  

        self.frame_superior = tk.Frame(ventana)
        self.frame_superior.pack(side=tk.TOP, fill=tk.X)

        self.etiqueta_nombre = tk.Label(self.frame_superior, text="Ingresa tu nombre:", font=("Arial", 12))
        self.etiqueta_nombre.pack(side=tk.LEFT, padx=10)

        self.entry_nombre = tk.Entry(self.frame_superior)
        self.entry_nombre.pack(side=tk.LEFT, padx=10)

        self.boton_iniciar = tk.Button(self.frame_superior, text="Iniciar juego", command=self.iniciar_juego)
        self.boton_iniciar.pack(side=tk.LEFT, padx=10)

        self.etiqueta_saldo = tk.Label(ventana, text="Saldo: 0$", font=("Arial", 16), fg="green")
        self.etiqueta_saldo.pack(side=tk.TOP, padx=10, pady=20)

        self.etiqueta_puntuacion_actual = tk.Label(ventana, text="Puntuación actual: 0", font=("Arial", 12))
        self.etiqueta_puntuacion_actual.pack(side=tk.TOP, padx=10)

        self.etiqueta_maximo = tk.Label(ventana, text="Puntaje máximo: 0", font=("Arial", 12))
        self.etiqueta_maximo.pack(side=tk.TOP, padx=10)

        self.boton_click = tk.Button(ventana, text="Haz click aquí", command=self.incrementar_saldo, width=20, height=5, font=("Arial", 12, "bold"))
        self.boton_click.pack(pady=20)

        self.boton_reiniciar = tk.Button(ventana, text="Volver a jugar", command=self.reiniciar_juego, width=20, height=2, font=("Arial", 12))
        self.boton_reiniciar.pack(side=tk.LEFT, padx=10, pady=10)
        self.boton_reiniciar.config(state=tk.DISABLED)
        self.boton_menu = tk.Button(ventana, text="Volver al Menú", command=self.volver_al_menu)
        self.boton_menu.pack(side=tk.LEFT, padx=10, pady=10)

        self.etiqueta_tiempo = tk.Label(ventana, text="Tiempo restante: 20", font=("Arial", 16))
        self.etiqueta_tiempo.pack(side=tk.TOP, padx=10)

        self.canvas = tk.Canvas(ventana, width=400, height=300)
        self.canvas.pack()

        self.jugador = self.canvas.create_oval(190, 140, 210, 160, fill="black")

        self.jugador_nombre = self.canvas.create_text(200, 120, text="", font=("Arial", 12), fill="blue")

        self.entry_nombre.focus_set()  

    def iniciar_juego(self):
        self.nickname = self.entry_nombre.get()
        if self.nickname:
            self.saldo = self.saldos_jugadores.get(self.nickname, 0)  # Obtener saldo del jugador actual
            self.ventana.title("Clicker Game - Jugador: " + self.nickname)
            self.entry_nombre.config(state=tk.DISABLED)
            self.boton_iniciar.config(state=tk.DISABLED)
            self.canvas.itemconfig(self.jugador_nombre, text=self.nickname)  

            self.ventana.bind("<w>", lambda event: self.mover_jugador(event, 0, -10))
            self.ventana.bind("<a>", lambda event: self.mover_jugador(event, -10, 0))
            self.ventana.bind("<s>", lambda event: self.mover_jugador(event, 0, 10))
            self.ventana.bind("<d>", lambda event: self.mover_jugador(event, 10, 0))

            self.actualizar_tiempo()

    def mover_jugador(self, evento, dx, dy):
        self.canvas.move(self.jugador, dx, dy)
        x1, y1, x2, y2 = self.canvas.coords(self.jugador)
        x_media = (x1 + x2) / 2
        self.canvas.coords(self.jugador_nombre, x_media, y1 - 20)

    def incrementar_saldo(self):
        self.saldo += 1
        self.etiqueta_saldo.config(text="Saldo: " + str(self.saldo) + "$")  
        self.etiqueta_puntuacion_actual.config(text="Puntuación actual de " + self.nickname + ": " + str(self.saldo))
        if self.saldo > self.puntaje_maximo:
            self.puntaje_maximo = self.saldo
            self.etiqueta_maximo.config(text="Puntaje máximo de " + self.nickname + ": " + str(self.puntaje_maximo))
        self.saldos_jugadores[self.nickname] = self.saldo  # Actualizar saldo en el diccionario

    def reiniciar_juego(self):
        self.saldo = self.saldos_jugadores.get(self.nickname, 0)  # Obtener saldo del jugador actual
        self.etiqueta_saldo.config(text="Saldo: " + str(self.saldo) + "$")  
        self.etiqueta_puntuacion_actual.config(text="Puntuación actual: 0")
        self.tiempo_restante = 20
        self.etiqueta_tiempo.config(text="Tiempo restante: 20")
        self.boton_click.config(state=tk.NORMAL)
        self.boton_reiniciar.config(state=tk.DISABLED)
        self.entry_nombre.config(state=tk.NORMAL)
        self.boton_iniciar.config(state=tk.NORMAL)
        self.entry_nombre.delete(0, tk.END)
        self.entry_nombre.focus_set()  

        self.ventana.unbind("<w>")
        self.ventana.unbind("<a>")
        self.ventana.unbind("<s>")
        self.ventana.unbind("<d>")
        self.boton_volver_menu = tk.Button(self.ventana, text="Volver al menú", command=self.volver_al_menu, width=20, height=2, font=("Arial", 12))
        self.boton_volver_menu.pack(side=tk.BOTTOM, pady=10)

    def actualizar_tiempo(self):
        if self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.etiqueta_tiempo.config(text="Tiempo restante: " + str(self.tiempo_restante))
            self.temporizador = self.ventana.after(1000, self.actualizar_tiempo)
        else:
            self.boton_click.config(state=tk.DISABLED)
            self.boton_reiniciar.config(state=tk.NORMAL)

    def volver_al_menu(self):
        self.ventana.destroy()
        ventana_menu = tk.Tk() 
        from registroylogin import MenuJuego,RegistroVentana, InicioSesionVentana

        menu = MenuJuego(ventana_menu)  
        ventana_menu.mainloop()  

class Tienda:
    def __init__(self, ventana, saldo):
        self.ventana = ventana
        self.ventana.title("Tienda")
        self.ventana.geometry("300x400")
        self.ventana.configure(bg="gray")

        self.saldo = saldo  

        self.etiqueta_saldo = tk.Label(ventana, text="Saldo actual: " + str(self.saldo) + "$", font=("Arial", 14), bg="gray")
        self.etiqueta_saldo.pack(pady=10)

        self.potenciador_clic = tk.Button(ventana, text="Potenciador de Clic - $10", command=self.comprar_potenciador_clic)
        self.potenciador_clic.pack(pady=10)

        self.generador_automatico = tk.Button(ventana, text="Generador Automático - $20", command=self.comprar_generador_automatico)
        self.generador_automatico.pack(pady=10)

        self.mejora_velocidad = tk.Button(ventana, text="Mejora de Velocidad - $15", command=self.comprar_mejora_velocidad)
        self.mejora_velocidad.pack(pady=10)

        self.boton_volver_menu = tk.Button(ventana, text="Volver al menú", command=self.volver_al_menu, width=20, height=2, font=("Arial", 12))
        self.boton_volver_menu.pack(pady=10)

    def comprar_potenciador_clic(self):
        print("Potenciador de clic comprado")

    def comprar_generador_automatico(self):
        print("Generador automático comprado")

    def comprar_mejora_velocidad(self):
        print("Mejora de velocidad comprada")

    def volver_al_menu(self):
        self.ventana.destroy()
        self.mostrar_menu()

if __name__ == "__main__":
    db = PostgreSQLDatabase(dbname="juegoclick", user="postgres", password="123456789")

    # Crear la tabla de usuarios si no existe
    db.create_table()
    ventana_principal = tk.Tk()
    from registroylogin import MenuJuego

    menu_juego = MenuJuego(ventana_principal, db)
    ventana_principal.mainloop()
