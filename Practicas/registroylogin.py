import tkinter as tk
from tkinter import ttk, messagebox
from dbjuegoclic import PostgreSQLDatabase

class RegistroVentana:
    def __init__(self, ventana, db,mostrar_menu_func):
        self.ventana = ventana
        self.db = db
        self.mostrar_menu_func = mostrar_menu_func  # Guardamos la función mostrar_menu en un atributo
        self.ventana.title("Registro de Usuario")
        self.ventana.geometry("400x200")  # Tamaño de la ventana

        style = ttk.Style()
        style.theme_use("clam")  # Usar el tema "clam"

        style.configure("TLabel", background="white", foreground="black", font=("Arial", 10))  # Estilo para las etiquetas
        style.configure("TEntry", fieldbackground="lightgray", font=("Arial", 10))  # Estilo para las entradas de texto
        style.configure("TButton", background="lightblue", font=("Arial", 10))  # Estilo para los botones

        self.frame = ttk.Frame(ventana)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.etiqueta_usuario = ttk.Label(self.frame, text="Nombre de Usuario:")
        self.etiqueta_usuario.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_usuario = ttk.Entry(self.frame)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.etiqueta_contraseña = ttk.Label(self.frame, text="Contraseña:")
        self.etiqueta_contraseña.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_contraseña = ttk.Entry(self.frame, show="*")
        self.entry_contraseña.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        
        self.mostrar_contraseña_var = tk.BooleanVar()
        self.mostrar_contraseña_var.set(False)
        self.checkbox_mostrar_contraseña = ttk.Checkbutton(self.frame, text="Mostrar contraseña", variable=self.mostrar_contraseña_var, command=self.mostrar_contraseña)
        self.checkbox_mostrar_contraseña.grid(row=2, columnspan=2, pady=(20, 0), sticky=tk.W)

        self.boton_registrar = ttk.Button(self.frame, text="Registrar", command=self.registrar_usuario)
        self.boton_registrar.grid(row=3, columnspan=2, pady=(20, 0), sticky=tk.W+tk.E)

    def registrar_usuario(self):
        nombre_usuario = self.entry_usuario.get().strip()
        contraseña = self.entry_contraseña.get()


        # Verificar si se ingresó un nombre de usuario
        if not nombre_usuario:
            messagebox.showerror("Error", "Por favor ingrese un nombre de usuario.")
            return

        # Verificar si el nombre de usuario ya existe
        if self.db.get_usuario_by_nombre(nombre_usuario):
            messagebox.showerror("Error", "El usuario ya existe.")
            return

        # Verificar si se ingresó una contraseña
        if not contraseña:
            messagebox.showerror("Error", "Por favor ingrese una contraseña.")
            return

        # Registrar el nuevo usuario en la base de datos
        self.db.insert_usuario(nombre_usuario, contraseña)
        messagebox.showinfo("Registro Exitoso", "¡Usuario registrado correctamente!")
        # Cerrar la ventana de registro después de registrar el usuario
        self.ventana.destroy()
        # Mostrar la ventana de inicio de sesión
        iniciar_sesion_ventana = InicioSesionVentana(tk.Toplevel(), self.db, self.mostrar_menu_func)  # Pasamos la función como argumento

    def mostrar_contraseña(self):
        if self.mostrar_contraseña_var.get():
            self.entry_contraseña.config(show="")
        else:
            self.entry_contraseña.config(show="*")

class InicioSesionVentana:
    def __init__(self, ventana, db, mostrar_menu_func):  
        self.ventana = ventana
        self.db = db
        self.ventana.title("Inicio de Sesión")
        self.ventana.geometry("400x200")  # Tamaño de la ventana

        style = ttk.Style()
        style.theme_use("clam")  # Usar el tema "clam"

        style.configure("TLabel", background="white", foreground="black", font=("Arial", 10))  # Estilo para las etiquetas
        style.configure("TEntry", fieldbackground="lightgray", font=("Arial", 10))  # Estilo para las entradas de texto
        style.configure("TButton", background="lightblue", font=("Arial", 10))  # Estilo para los botones

        self.frame = ttk.Frame(ventana)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.etiqueta_usuario = ttk.Label(self.frame, text="Nombre de Usuario:")
        self.etiqueta_usuario.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_usuario = ttk.Entry(self.frame)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.etiqueta_contraseña = ttk.Label(self.frame, text="Contraseña:")
        self.etiqueta_contraseña.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_contraseña = ttk.Entry(self.frame, show="*")
        self.entry_contraseña.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.mostrar_contraseña_var = tk.BooleanVar()
        self.mostrar_contraseña_var.set(False)
        self.checkbox_mostrar_contraseña = ttk.Checkbutton(self.frame, text="Mostrar contraseña", variable=self.mostrar_contraseña_var, command=self.mostrar_contraseña)
        self.checkbox_mostrar_contraseña.grid(row=2, columnspan=2, pady=(20, 0), sticky=tk.W)

        self.boton_iniciar_sesion = ttk.Button(self.frame, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_iniciar_sesion.grid(row=3, columnspan=2, pady=(20, 0), sticky=tk.W+tk.E)

    def iniciar_sesion(self):
        nombre_usuario = self.entry_usuario.get().strip()
        contraseña = self.entry_contraseña.get()

        # Verificar si se ingresó un nombre de usuario
        if not nombre_usuario:
            messagebox.showerror("Error", "Por favor ingrese un nombre de usuario.")
            return

        # Verificar si se ingresó una contraseña
        if not contraseña:
            messagebox.showerror("Error", "Por favor ingrese una contraseña.")
            return

        # Obtener el usuario de la base de datos por su nombre
        usuario = self.db.get_usuario_by_nombre(nombre_usuario)

        # Verificar si el usuario existe
        if not usuario:
            messagebox.showerror("Error", "El usuario no existe.")
            return

        # Verificar si la contraseña es correcta
        if usuario[2] == contraseña:
            messagebox.showinfo("Inicio de Sesión Exitoso", "¡Inicio de sesión exitoso!")
            # Cerrar la ventana de inicio de sesión después de iniciar sesión
            self.ventana.destroy()
            from common import MenuJuego  # Importamos la clase MenuJuego desde common.py

            # Llamar a la función mostrar_menu en la ventana principal del juego
            menu_juego = MenuJuego(self.ventana, self.db)  # Creamos una instancia de MenuJuego
            menu_juego.mostrar_menu()  # Llamamos a mostrar_menu en la instancia de MenuJuego
        else:
            messagebox.showerror("Error", "Contraseña incorrecta.")
    
    def mostrar_contraseña(self):
        if self.mostrar_contraseña_var.get():
            self.entry_contraseña.config(show="")
        else:
            self.entry_contraseña.config(show="*")

if __name__ == "__main__":
    db = PostgreSQLDatabase(dbname="juegoclick", user="postgres", password="123456789")

    # Crear la tabla de usuarios si no existe
    db.create_table()

    # Mostrar la ventana de registro
    ventana_registro = tk.Tk()
    from common import MenuJuego  # Importamos la clase MenuJuego desde common.py

    registro_ventana = RegistroVentana(ventana_registro, db, MenuJuego)  # Pasamos la clase MenuJuego en lugar de la función mostrar_menu
    ventana_registro.mainloop()

    # Después de salir del bucle principal, creamos una instancia de MenuJuego y llamamos a mostrar_menu
    menu_juego = MenuJuego(tk.Tk(), db)
    menu_juego.mostrar_menu()

