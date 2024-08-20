class Empleado:
    def __init__(self, Sueldo, ventas, bonificacion=250):
        self.Sueldo = Sueldo
        self.ventas = ventas
        self.bonificacion = bonificacion
    
    def calComision(self):
        return self.ventas * 0.10
    
    def caligss(self):
        return self.Sueldo * 0.0483
    
    def calahorro(self, total_ganado):
        return total_ganado * 0.07
    
    def totalganado(self):
        return self.Sueldo + self.calComision() + self.bonificacion
    
    def calcular_total_descuentos(self, totalganado):
        return self.calahorro(totalganado) + self.caligss()
    
    def calcular_sueldo_liquido(self):
        totalganado = self.totalganado()
        total_descuentos = self.calcular_total_descuentos(totalganado)
        return totalganado - total_descuentos
    
    def mostrar_resultados(self):
        print(f"Sueldo Base: Q.{self.Sueldo}")
        print(f"Comisión por Ventas: Q.{self.calComision()}")
        print(f"IGSS: Q.{self.caligss()}")
        totalganado = self.totalganado()
        print(f"Total Ganado: Q.{totalganado}")
        total_descuentos = self.calcular_total_descuentos(totalganado)
        print(f"Total Descuentos: Q.{total_descuentos}")
        print(f"Sueldo Líquido: Q.{self.calcular_sueldo_liquido()}")


Sueldo = float(input(" sueldo base: Q."))
ventas = float(input("valor de ventas realizadas: Q."))

empleado = Empleado(Sueldo, ventas)
empleado.mostrar_resultados()

#Juan Pablo Zacarias Paiz
#201805637