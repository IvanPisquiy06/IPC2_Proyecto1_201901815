import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("Agencia Espacial de Guatemala")

        # Botones en la interfaz
        self.btn_cargar = tk.Button(master, text="Cargar archivo", command=self.cargar_archivo)
        self.btn_organismos = tk.Button(master, text="Identificar organismos", command=self.identify_organisms)
        self.btn_colocar_organismo = tk.Button(master, text="Colocar organismo", command=self.colocar_organismo)
        self.btn_verificar_muestra = tk.Button(master, text="Verificar muestra", command=self.verificar_muestra)
        self.btn_guardar = tk.Button(master, text="Guardar cambios", command=self.guardar_cambios)

        # Etiquetas y campos de entrada
        self.lbl_m = tk.Label(master, text="M:")
        self.lbl_n = tk.Label(master, text="N:")
        self.lbl_muestra = tk.Label(master, text="Muestra:")
        self.lbl_organismo = tk.Label(master, text="Organismo:")
        self.entry_m = tk.Entry(master)
        self.entry_n = tk.Entry(master)
        self.entry_muestra = tk.Entry(master)
        self.entry_organismo = tk.Entry(master)

        # Acomodar elementos en la ventana
        self.btn_cargar.grid(row=0, column=0, padx=10, pady=10)
        self.lbl_m.grid(row=1, column=0, padx=10, pady=10)
        self.entry_m.grid(row=1, column=1, padx=10, pady=10)
        self.lbl_n.grid(row=2, column=0, padx=10, pady=10)
        self.entry_n.grid(row=2, column=1, padx=10, pady=10)
        self.lbl_muestra.grid(row=3, column=0, padx=10, pady=10)
        self.entry_muestra.grid(row=3, column=1, padx=10, pady=10)
        self.lbl_organismo.grid(row=4, column=0, padx=10, pady=10)
        self.entry_organismo.grid(row=4, column=1, padx=10, pady=10)
        self.btn_organismos.grid(row=5, column=0, padx=10, pady=10)
        self.btn_colocar_organismo.grid(row=5, column=1, padx=10, pady=10)
        self.btn_verificar_muestra.grid(row=6, column=0, padx=10, pady=10)
        self.btn_guardar.grid(row=6, column=1, padx=10, pady=10)

    def cargar_archivo(self):
        # Abrir cuadro de diálogo para seleccionar archivo
        filename = filedialog.askopenfilename(initialdir=".", title="Seleccionar archivo", filetypes=(("XML files", "*.xml"),))
        # Cargar archivo y procesar datos
        # ...
    
    def identify_organisms(self):
        hola = 1

    def colocar_organismo(self):
        Hola = 3

    def verificar_muestra(self):
        Hola = 4

    def guardar_cambios(self):
        Hola = 5

root = tk.Tk()
app = App(root)
root.mainloop()
