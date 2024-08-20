class anl:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        print("un  animal hace un sonido.")

    def describir(self):
        print(f"Soy un {self.__class__.__name__}, me llamo {self.nombre} y tengo {self.edad} años.")
class Perro(anl):
    def hacer_sonido(self):
        print("GUAU, GUAU!")
class Gato(anl):
    def hacer_sonido(self):
        print("MIAU, MIAU!")
pollo = Perro("chequen", 7)
loro = Gato("mish", 9)


pollo.describir() 
pollo.hacer_sonido()  

loro.describir()  
loro.hacer_sonido() 

#Juan Pablo Zacarias Paiz
#201805637