#Codigo Servidor
import sys
class Servidor():
   
    def __init__(self):
        self.direccion = '0.0.0.0'
        self.puerto = 16621

    def clasificar_peticiones(self, figura):
        if figura.lower() == 'triangulo':
            return 3
        elif figura.lower() == 'rectangulo':
            return 2
        elif figura.lower() == 'circulo':
            return 1
        else:
            return 0
    
    def calcular_area(self, figura, base, altura, radio):
        if figura == 3:
            return (base*altura)/2
        if figura == 1:
            pi = 3.14
            return round(pi*radio*radio)
    
    def calcular_perimetro(self, altura, base):
        return 2*(base+altura)


    def main(self):
        sys.stdout.write('\nAlo bro?\n')

if __name__ == '__main__':
    serv = Servidor()
    serv.main()
