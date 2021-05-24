class Vehiculo():
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas
    def __str__(self):
        return "color {},{} ruedas".format(self.color,self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad,cilindrado):
            super().__init__(color,ruedas)
            self.velocidad=velocidad
            self.cilindrado=cilindrado
            
    def __str__(self):
        return super().__str__()+",{} km/h,{} cc".format(self.velocidad,self.cilindrado)

y=Coche("rojo",4,100,1500)
print(y)