import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from lista_de_tareas import ListaDeTareas

class Interfaz:
    def __init__(self, root):
        self.lista_de_tareas = ListaDeTareas()
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")

        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        # Configurar el protocolo de cierre de la ventana para guardar cambios
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

        # Crear una barra de menú
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Salir", command=self.cerrar_aplicacion)

        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack(pady=10)

        # Agregar los logos
        self.logo_frame = tk.Frame(self.frame, bg="#f0f0f0")
        self.logo_frame.pack(pady=5)

        self.logo1 = Image.open("logo1.png")
        self.logo1 = self.logo1.resize((100, 100), Image.LANCZOS)
        self.logo1_img = ImageTk.PhotoImage(self.logo1)
        self.logo1_label = tk.Label(self.logo_frame, image=self.logo1_img, bg="#f0f0f0")
        self.logo1_label.pack(side=tk.LEFT, padx=10)

        self.logo2 = Image.open("logo2.png")
        self.logo2 = self.logo2.resize((100, 100), Image.LANCZOS)
        self.logo2_img = ImageTk.PhotoImage(self.logo2)
        self.logo2_label = tk.Label(self.logo_frame, image=self.logo2_img, bg="#f0f0f0")
        self.logo2_label.pack(side=tk.LEFT, padx=10)

        self.titulo = tk.Label(self.frame, text="Gestor de Tareas", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.titulo.pack(pady=5)

        self.entry_frame = tk.Frame(self.frame, bg="#f0f0f0")
        self.entry_frame.pack(pady=5)
        
        self.entry_label = tk.Label(self.entry_frame, text="Nueva Tarea:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
        self.entry_label.pack(side=tk.LEFT, padx=5)

        self.entry = tk.Entry(self.entry_frame, width=30, font=("Helvetica", 12), bd=2, relief="groove")
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind("<Return>", self.agregar_tarea)

        self.button_frame = tk.Frame(self.frame, bg="#f0f0f0")
        self.button_frame.pack(pady=5)

        self.boton_agregar = tk.Button(self.button_frame, text="Agregar Tarea", command=self.agregar_tarea, font=("Helvetica", 12), bg="#4caf50", fg="white", activebackground="#45a049", bd=0, padx=10, pady=5, relief="groove")
        self.boton_agregar.pack(side=tk.LEFT, padx=5)

        self.boton_completar = tk.Button(self.button_frame, text="Completar Tarea", command=self.completar_tarea, font=("Helvetica", 12), bg="#2196f3", fg="white", activebackground="#1976d2", bd=0, padx=10, pady=5, relief="groove")
        self.boton_completar.pack(side=tk.LEFT, padx=5)

        self.boton_eliminar = tk.Button(self.button_frame, text="Eliminar Tarea", command=self.eliminar_tarea, font=("Helvetica", 12), bg="#f44336", fg="white", activebackground="#d32f2f", bd=0, padx=10, pady=5, relief="groove")
        self.boton_eliminar.pack(side=tk.LEFT, padx=5)

        self.boton_exportar = tk.Button(self.button_frame, text="Exportar Tareas", command=self.exportar_tareas, font=("Helvetica", 12), bg="#ff9800", fg="white", activebackground="#fb8c00", bd=0, padx=10, pady=5, relief="groove")
        self.boton_exportar.pack(side=tk.LEFT, padx=5)

        self.lista_frame = tk.Frame(self.frame, bg="#f0f0f0")
        self.lista_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.lista_scroll = tk.Scrollbar(self.lista_frame)
        self.lista_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_tareas = tk.Listbox(self.lista_frame, width=50, height=15, font=("Helvetica", 12), yscrollcommand=self.lista_scroll.set, selectbackground="#d3d3d3", bd=2, relief="groove")
        self.lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.lista_scroll.config(command=self.lista_tareas.yview)
        
        self.actualizar_lista()

    def cerrar_aplicacion(self):
        self.lista_de_tareas.guardar_tareas()
        self.root.quit()

    def agregar_tarea(self, event=None):
        descripcion = self.entry.get()
        if descripcion:
            self.lista_de_tareas.agregar_tarea(descripcion)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
            messagebox.showinfo("Información", "Tarea agregada exitosamente")

    def completar_tarea(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            self.lista_de_tareas.completar_tarea(indice)
            self.actualizar_lista()
            messagebox.showinfo("Información", "Tarea completada exitosamente")
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para completar")

    def eliminar_tarea(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            self.lista_de_tareas.eliminar_tarea(indice)
            self.actualizar_lista()
            messagebox.showinfo("Información", "Tarea eliminada exitosamente")
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar")

    def exportar_tareas(self):
        with open("lista_de_tareas.txt", "w") as file:
            tareas = self.lista_de_tareas.mostrar_tareas()
            for tarea in tareas:
                file.write(f"{tarea}\n")
        messagebox.showinfo("Información", "Lista de tareas exportada exitosamente")

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        tareas = self.lista_de_tareas.mostrar_tareas()
        for tarea in tareas:
            if "Completada" in tarea:
                self.lista_tareas.insert(tk.END, tarea)
                self.lista_tareas.itemconfig(tk.END, {'bg':'#d3ffd3'})
            else:
                self.lista_tareas.insert(tk.END, tarea)
                self.lista_tareas.itemconfig(tk.END, {'bg':'#ffd3d3'})
