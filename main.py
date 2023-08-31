import os
import xml.etree.ElementTree as ET

programa = True
xml_content = None

class Nodo_Fila:

    def __init__(self, fila, dato):
        self.Dato = Fila(fila, dato)
        self.Siguiente = None

    def AsignarSiguiente(self, nodo_random):
        self.Siguiente = nodo_random
    
    def DevolverSiguiente(self):
        return self.Siguiente
    
    def DevolverFila(self):
        return self.Dato.DevolverFila()
    
    def DevolverData(self):
        return self.Dato.DevolverData()
    
    def InsertarEnColunma(self, Dato):
        self.Dato.InsertarEnColumna(Dato)
    
    def ImprimirListaColumna(self):
        self.Dato.ImprimirColumnas()

    def ModificarDatoColumna(self, Columna, dato):
        self.Dato.ModificarDatoColumna(Columna, dato)

class Fila:

    def __init__(self, noFila, dato):
        self.NoFila = noFila
        self.ListaColumnas = Cola_Columna()
        self.Dato = dato

    def InsertarEnColumna(self, dato):
        self.ListaColumnas.Insertar(dato)
    
    def ImprimirColumnas(self):
        self.ListaColumnas.ImprimirLista()

    def DevolverFila(self):
        return self.NoFila
    
    def DevolverData(self):
        return "Esta es la fila: " + str(self.NoFila) + " El conteido es: " + self.Dato
    
    def ModificarDatoColumna(self, Columna, Dato):
        self.ListaColumnas.ModificarDato(Columna, Dato)

class Columna:
    
    def __init__(self, columna, dato):
        self.Columna = columna
        self.Dato = dato
    
    def DevolverColumna(self):
        return self.Columna
    
    def DevolverData(self):
        return self.Dato
    
    def ModificarDato(self, dato):
        self.Dato = dato

class Cola_Columna:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0

    def Insertar(self, Dato):
        self.Contador += 1
        NuevoNodo =  Nodo_Columna(self.Contador, Dato)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
    
    def ImprimirLista(self):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            print(Auxiliar.DevolverData())
            Auxiliar = Auxiliar.Siguiente
        print("Terminó de imprimir lista")

    def ModificarDato(self, columna, dato):
        Contador = 0
        Auxiliar = self.Inicio
        if columna == 0 or columna > self.Contador:
            print("No existe la columna")
            return
        else:
            while Auxiliar != None:
                Contador += 1
                if Contador == columna:
                    print("Encontramos columna")
                    #Modificamos dato
                    Auxiliar.ModificarDato(dato)
                else:
                    Auxiliar = Auxiliar.Siguiente

class Nodo_Columna:

    def __init__(self, columna, dato):
        self.Dato = Columna(columna, dato)
        self.Siguiente = None

    def AsignarSiguiente(self, nodo_random):
        self.Siguiente = nodo_random
    
    def DevolverSiguiente(self):
        return self.Siguiente
    
    def DevolverColumna(self):
        return self.Dato.DevolverColumna()
    
    def DevolverData(self):
        return self.Dato.DevolverData()
    
    def ModificarDato(self, dato):
        self.Dato.ModificarDato(dato)

def procesar_archivo_xml(xml_content):
    senales = []
    for senal_element in xml_content.findall('senal'):
        nombre = senal_element.get('nombre')
        t = int(senal_element.get('t'))
        A = int(senal_element.get('A'))

        matriz_frecuencias = Nodo_Fila(0, None)  # Inicializar la matriz de frecuencias
        matriz_patrones = Nodo_Fila(0, None)     # Inicializar la matriz de patrones

        for dato_element in senal_element.findall('dato'):
            fila = int(dato_element.get('t'))
            columna = int(dato_element.get('A'))
            valor = int(dato_element.text)

            # Insertar el dato en la matriz de frecuencias
            # ...

            # Insertar el dato en la matriz de patrones
            # ...

        senales.append({
            'nombre': nombre,
            't': t,
            'A': A,
            'matriz_frecuencias': matriz_frecuencias,
            'matriz_patrones': matriz_patrones
        })

    matriz_reducida = Nodo_Fila(0, None)  # Inicializar la matriz reducida de frecuencias
    
    # Analizar las matrices de patrones para reducir la matriz de frecuencias
    for senal in senales:
        nodo_patron = senal['matriz_patrones']
        nodo_frecuencia = senal['matriz_frecuencias']
        
        while nodo_patron.DevolverSiguiente() is not None:
            grupo_actual = nodo_patron.DevolverData()
            frecuencias_grupo = Nodo_Fila(0, None)
            
            # Recorrer las columnas y sumar las frecuencias de los grupos
            columna_patron = grupo_actual.DevolverSiguiente()
            columna_frecuencia = nodo_frecuencia.DevolverSiguiente()
            
            while columna_patron is not None and columna_frecuencia is not None:
                if columna_patron.DevolverData() == 1:
                    frecuencias_grupo.InsertarEnColunma(columna_frecuencia.DevolverData())
                columna_patron = columna_patron.DevolverSiguiente()
                columna_frecuencia = columna_frecuencia.DevolverSiguiente()
            
            # Insertar el grupo de frecuencias en la matriz reducida
            if frecuencias_grupo.DevolverSiguiente() is not None:
                matriz_reducida.InsertarEnColunma(frecuencias_grupo)
            
            nodo_patron = nodo_patron.DevolverSiguiente()
            nodo_frecuencia = nodo_frecuencia.DevolverSiguiente()

    # Aquí puedes imprimir la matriz reducida o realizar otras operaciones con ella
    print("Matriz reducida de frecuencias:")
    matriz_reducida.ImprimirListaColumna()

while programa:
    print("Menú Principal:")
    print(" 1. Cargar Archivo")
    print(" 2. Procesar Archivo")
    print(" 3. Escribir Archivo de Salida")
    print(" 4. Mostrar Datos del Estudiante")
    print(" 5. Generar Gráfica")
    print(" 6. Inicializar Sistema")
    print(" 7. Salida")
    print("="*20)
    
    opcion = int(input("Escriba la opción a elegir: "))
    
    if opcion == 1:
        print("Opcion Cargar Archivo:")
        path = input("Ingrese la ruta del archivo: ")
        
        if os.path.exists(path) and path.endswith(".xml"):
            print("Archivo cargado con éxito :)")
            try:
                tree = ET.parse(path)
                root = tree.getroot()
                xml_content = root  # Guardar el contenido XML en la variable
            except ET.ParseError:
                print("El archivo no es un XML válido.")
        else:
            print("El archivo no existe en la ubicación proporcionada o no es un archivo XML.")
    elif opcion == 2:

        if xml_content:
            print(procesar_archivo_xml(xml_content))
        else:
            print("No hay ningun archivo XML cargado en la memoria")
        
    elif opcion == 7:
        programa = False