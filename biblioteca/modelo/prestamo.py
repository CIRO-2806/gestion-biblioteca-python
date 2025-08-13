import json
class Prestamo:
    def __init__(self,indice,libroPrestado,fechaPrestamo,fechaDevolucion,prestador,prestado):
        self._indice = indice
        self._libroPrestado = libroPrestado
        self._fechaPrestamo = fechaPrestamo
        self._fechaDevolucion = fechaDevolucion
        self._prestador = prestador
        self._prestado = prestado
    
    def getIndice(self):
        return self._indice
    
    def setIndice(self,new_indice):
        self._indice = new_indice
        
    def getLibroPrestado(self):
        return self._libroPrestado
    
    def setLibroPrestado(self, new_libroPrestado):
        self._libroPrestado = new_libroPrestado
    
    def getFechaPrestamo(self):
        return self._fechaPrestamo
    
    def setFechaPrestamo(self,new_fechaPrestamo):
        self._fechaPrestamo = new_fechaPrestamo
        
    def getFechaDevolucion(self):
        return self._fechaDevolucion
    
    def setFechaDevolucion(self,new_fechaDevolucion):
        self._fechaDevolucion = new_fechaDevolucion
        
    def getPrestador(self):
        return self._prestador
    
    def setPrestador(self,new_prestador):
        self._prestador = new_prestador

    def getPrestado(self):
        return self._prestado
    
    def setPrestado(self,new_prestado):
        self._prestado = new_prestado
        
    def to_dict(self):
        return {
            "indice": self._indice,
            "libroPrestado": self._libroPrestado,
            "fechaPrestamo": self._fechaPrestamo,
            "fechaDevolucion": self._fechaDevolucion,
            "prestador": self._prestador,
            "prestado": self._prestado
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["indice"],
            data["libroPrestado"],
            data["fechaPrestamo"],
            data["fechaDevolucion"],
            data["prestador"],
            data["prestado"]
        )
        
    def guardarPrestamo(prestamo, ARCHIVO_PRESTAMOS):
        with open(ARCHIVO_PRESTAMOS,"w", encoding="utf-8") as file:
            json.dump([pre.to_dict() for pre in prestamo], file, ensure_ascii=False, indent=4)
        print(f"Lista de prestamos guardada en {ARCHIVO_PRESTAMOS}")
    
    def cargarPrestamo(ARCHIVO_PRESTAMOS):
        try:
            with open(ARCHIVO_PRESTAMOS,"r",encoding="utf-8") as file:
                data = json.load(file)
                return[Prestamo.from_dict(item) for item in data]
        except FileNotFoundError:
            return []  
    