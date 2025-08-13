import json

class Libro():
    def __init__(self,nombre,autor,isbn,editorial,año,estado):
        self._nombre = nombre
        self._autor = autor
        self._isbn = isbn
        self._editorial = editorial
        self._año = año
        self._estado = estado
        
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, new_nombre):
        self._nombre = new_nombre
    
    def getAutor(self):
        return self._autor
    
    def setAutor(self, new_autor):
        self._autor = new_autor
    
    def getIsbn(self):
        return self._isbn
    
    def setIsbn(self, new_isbn):
        self._isbn = new_isbn
        
    def getEditorial(self):
        return self._editorial
    
    def setEditorial(self, new_editorial):
        self._editorial = new_editorial
        
    def getAño(self):
        return self._año
    
    def setAño(self,new_año):
        self._año = new_año
        
    def getEstado(self):
        return self._estado
    
    def setEstado(self,new_estado):
        self._estado = new_estado
    
    def to_dict(self):
        return {
            "nombre": self._nombre,
            "autor": self._autor,
            "isbn": self._isbn,
            "editorial": self._editorial,
            "año": self._año,
            "estado": self._estado
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["nombre"],
            data["autor"],
            data["isbn"],
            data["editorial"],
            data["año"],
            data["estado"]
        )
        
    def guardarLibro(libro, ARCHIVO_LIBROS):
        with open(ARCHIVO_LIBROS,"w", encoding="utf-8") as file:
            json.dump([lib.to_dict() for lib in libro], file, ensure_ascii=False, indent=4)
        print(f"Lista de Libros guardada en {ARCHIVO_LIBROS}")
    
    def cargarLibro(ARCHIVO_LIBROS):
        try:
            with open(ARCHIVO_LIBROS,"r",encoding="utf-8") as file:
                data = json.load(file)
                return[Libro.from_dict(item) for item in data]
        except FileNotFoundError:
            return []
        