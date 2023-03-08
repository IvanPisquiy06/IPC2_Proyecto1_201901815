import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from graphviz import Digraph
from graphviz import Graph


class App:
    def Organismo(self, nombre, porcentaje):
        self.nombre = nombre
        self.porcentaje = porcentaje
        self.muestras = []

    def agregar_muestra(self, muestra):
        self.muestras.append(muestra)

    def porcentaje_total(self):
        return sum([muestra.porcentaje for muestra in self.muestras])

    def Muestra(self, nombre, datos):
        self.nombre = nombre
        self.datos = datos

    def __init__(self, master):
        self.master = master
        master.title("Agencia Espacial de Guatemala")

        # Botones en la interfaz
        self.btn_cargar = tk.Button(master, text="Cargar archivo", command=self.cargar_archivo)
        self.btn_organismos = tk.Button(master, text="Identificar organismos", command=self.create_matrix)

        # Acomodar elementos en la ventana
        self.btn_cargar.grid(row=0, column=0, padx=10, pady=10)
        self.btn_organismos.grid(row=5, column=0, padx=10, pady=10)

    def cargar_archivo(self):
        file_path = filedialog.askopenfilename(initialdir="./", title="Seleccionar archivo", filetypes=(("XML files", "*.xml"),))

        tree = ET.parse(file_path)
        root = tree.getroot()

        # Acceder a los datos
        self.organismos = {}
        for organismo in root.find('listaOrganismos'):
            codigo = organismo.find('codigo').text
            nombre = organismo.find('nombre').text
            self.organismos[codigo] = nombre

        self.muestras = []
        for muestra in root.find('listadoMuestras'):
            codigo = muestra.find('codigo').text
            descripcion = muestra.find('descripcion').text
            self.filas = int(muestra.find('filas').text)
            self.columnas = int(muestra.find('columnas').text)
            celdas_vivas = []
            for celda in muestra.find('listadoCeldasVivas'):
                fila = int(celda.find('fila').text)
                columna = int(celda.find('columna').text)
                codigo_organismo = celda.find('codigoOrganismo').text
                celdas_vivas.append((fila, columna, codigo_organismo))
            self.muestras.append((codigo, descripcion, self.filas, self.columnas, celdas_vivas))
        
        
    def create_matrix(self):

        # Comprobar y actualizar la composición de vida según la regla básica
        for i in range(self.filas):
            for j in range(self.columnas):
                celda = (i, j)
                if not self.muestras[i][j]: 
                    # si la celda está vacía
                    organismos_vecinos = []
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == dy == 0: # no comprobar la propia celda
                                continue
                            x = i + dx
                            y = j + dy
                            if x < 0 or x >= self.filas or y < 0 or y >= self.columnas: 
                            # no salir de los límites de la matriz
                                continue
                            if muestra[x][y]: # si la celda vecina está viva
                                if muestra[x][y] not in organismos_vecinos: # agregar organismo a la lista de organismos vecinos
                                    organismos_vecinos.append(muestra[x][y])
                    for organismo in organismos_vecinos: # comprobar cada organismo vecino
                        organismo_vecino_sobrevive = False
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                if dx == dy == 0: # no comprobar la propia celda
                                    continue
                                x = i + dx
                                y = j + dy
                                if x < 0 or x >= self.filas or y < 0 or y >= self.columnas: 
                                # no salir de los límites de la matriz
                                    continue
                                if muestra[x][y] == organismo: # si la celda vecina tiene el mismo organismo
                                    organismo_vecino_sobrevive = True
                        if organismo_vecino_sobrevive:
                            self.celdas_vivas.append({'x': i, 'y': j, 'codigo_organismo': list(self.organismos.keys())[list(self.organismos.values()).index(organismo)]})
    
        # Actualizar el estado de la matriz
        muestra = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                celda = (i, j)
                if any((celda == (x[0], x[1])) for x in self.celdas_vivas):
                    organismo = self.organismos[self.celdas_vivas[(celda in self.celdas_vivas)]['codigo_organismo']]
                    fila.append(organismo)
                else:
                    fila.append(None)
            muestra.append(fila)
        self.matriz = muestra

        # Ajustar la lista de celdas vivas para las próximas iteraciones
        celdas_vivas_nueva = []
        for celda_viva in self.celdas_vivas:
            i, j = celda_viva['x'], celda_viva['y']
            organismo = self.organismos[celda_viva['codigo_organismo']]
            organismos_vecinos = []
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0: # no comprobar la propia celda
                        continue
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= self.filas or y < 0 or y >= self.columnas: 
                    # no salir de los límites de la matriz
                        continue
                    if muestra[x][y]: # si la celda vecina está viva
                        if muestra[x][y] not in organismos_vecinos: # agregar organismo a la lista de organismos vecinos
                            organismos_vecinos.append(muestra[x][y])
            organismo_sobrevive = False
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0: # no comprobar la propia celda
                        continue
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= self.filas or y < 0 or y >= self.columnas: 
                    # no salir de los límites de la matriz
                        continue
                    if muestra[x][y] == organismo: # si la celda vecina tiene el mismo organismo
                        organismo_sobrevive = True
            if organismo_sobrevive:
                celdas_vivas_nueva.append(celda_viva)
        self.celdas_vivas = celdas_vivas_nueva

root = tk.Tk()
app = App(root)
root.mainloop()
