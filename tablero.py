# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:43:06 2021

@author: JOSE ANGEL
"""

class tablero():
    def __init__(self,fil,col,f,c):
        self.filas=fil
        self.columnas=col
        self.filsel=f
        self.colsel=c
        self.L=[]
        
    def dibujar_tablero(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                self.L[i].append(" X ")
                print(self.L[i][j], end=" ")
            print("")
        
    def dibujar_diagonal1(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if i==j:
                    self.L[i].append(" X ")
                else:
                    self.L[i].append(" . ")
                print(self.L[i][j], end=" ")
            print("")
            
    def dibujar_diagonal2(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if i+j==self.filas-1:
                    self.L[i].append(" X ")
                else:
                    self.L[i].append(" . ")
                print(self.L[i][j], end=" ")
            print("")
      
    def dibujar_diagonales(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if i+j==self.filas-1 or i==j :
                    self.L[i].append(" X ")
                else:
                    self.L[i].append(" . ")
                print(self.L[i][j], end=" ")
            print("")
            
    def dibujar_punto_seleccionado(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if i==self.filsel and j==self.colsel:
                    self.L[i].append(" X ")
                else:
                    self.L[i].append(" . ")
                print(self.L[i][j], end=" ")
            print("")
            
    def dibujar_alfil(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if i-j==self.filsel-self.colsel or i+j==self.filsel + self.colsel :
                    self.L[i].append(" X ")
                else:
                    self.L[i].append(" . ")
                print(self.L[i][j], end=" ")
            print("")
            
    def dibujar_torre(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if i==self.filsel or j==self.colsel:
                    self.L[i].append(" X ")
                else:
                    self.L[i].append(" . ")
                print(self.L[i][j], end=" ")
            print("")
    
    def dibujar_reina(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if i==self.filsel or j==self.colsel or i-j==self.filsel-self.colsel or i+j==self.filsel + self.colsel:
                    self.L[i].append(" X ")
                else:
                    self.L[i].append("   ")
                print(self.L[i][j], end=" ")
            print("")
            
    
                
    def dibujar_peon(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if i==self.filsel and j==self.colsel or i==self.filsel+1 and j==self.colsel:
                    self.L[i].append(" X ")
                else:
                    self.L[i].append(" . ")
                print(self.L[i][j], end=" ")
            print("")
    
    def dibujar_rey(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if i==self.filsel or j==self.colsel or i-j==(self.filsel-self.colsel) or i+j==self.filsel + self.colsel :
                    
                    self.L[i].append(" X ")
                else:
                    self.L[i].append("   ")
                print(self.L[i][j], end=" ")
            print("")
    
    def dibujar_caballo(self):
        pass
    
    
    def dibujar_A(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if j==0 or j==self.columnas-1 or i==0 or i==self.filas /2:
                    self.L[i].append(" X ")
                else:
                    self.L[i].append("   ")
                print(self.L[i][j], end=" ")
            print("")
            
    
    def dibujar_B(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if j==0 or j==7 or i==0 or i==3 or  i==4 or i==7 :
                    if((j==7 and i==0) or (j==7 and i==7) or (j==7 and i==3) or (j==7 and i==4 )):
                        continue
                    self.L[i].append(" X ")
                else:
                    self.L[i].append("   ")
                print(self.L[i][j], end=" ")
            print("")
    def dibujar_C(self):
        for i in range(self.filas):
            self.L.append([])
            for j in range(self.columnas):
                if j==0  or j==7 or i==7:
                    if((j==7 and i==0) or (j==7 and i==7)):
                        continue
                    self.L[i].append(" X ")
                else:
                    self.L[i].append("   ")
                print(self.L[i][j], end=" ")
            print("")   
    
"---------------------------------------------------------"

filaseleccionada=int(input("seleccione fila [0 - 7]:"))
columnaseleccionada=int(input("seleccione columna[0 - 7]:"))


t1=tablero(8,8,filaseleccionada,columnaseleccionada)
#t1.dibujar_tablero()
#t1.dibujar_diagonal1()
#t1.dibujar_diagonal2()
#t1.dibujar_diagonales()
#t1.dibujar_punto_seleccionado()
#t1.dibujar_alfil()
#t1.dibujar_torre()
# t1.dibujar_reina()
# t1.dibujar_A()
# t1.dibujar_peon()
# t1.dibujar_rey()
t1.dibujar_B()
# t1.dibujar_C()


