class Menu(object):
    def hello(self):
        print(
        '''
                        CTIMER
            SEU CONVERSOR DE TEMPERATURA!
        '''
        )
    def menu(self):
        print(
        '''
            1 - Celcius para Kelvin
            2 - Celcius para Fahrenheit
            3 - Fahrenheit para Celcius
            4 - Fahrenheit para Kelvin
            5 - Kelvin pra Fahrenheit
            6 - Kelvin para Celcius
            7 - Sair
        '''
        )

class Converter(object):
    def __init__(self,option,timer):
        self.option = option
        self.temp = timer

    def conve_temp(self):
        if(self.option == 1):
            res = self.temp + 273
            print(f'{self.temp} Celcius para {res:.1f} Kelvin')
        elif(self.option == 2):
            res = (160 + 9 * self.temp)/5
            print(f'{self.temp} Celcius para {res} Fahrenheit')
        elif(self.option == 3):
            res = 5 * (self.temp - 32)/9
            print(f'{self.temp} Fahrenheit para {res:.1f} Celcius')
        elif(self.option == 4):
            res = ((self.temp - 32 * 5) / 9) + 273
            print(f'{self.temp} Fahrenheit para {res} Kelvin')
        elif(self.option == 5):
            res = (((self.temp - 273) * 9) / 5) + 32
            print(f'{self.temp} Kelvin para {res} Fahrenheit')
        else:
            res = self.temp - 273
            print(f'{self.temp} Kelvin para {res} Celcius')


def main():
    m = Menu()
    m.hello()
    m.menu()
    while True:
        op = int(input("Selecione uma opção: "))
        if(op != 7 and op < 8 and op > 0):
            timer = int(input("Converter: "))
            c = Converter(op,timer)
            c.conve_temp()
        elif(op == 7):
            print("Saindo")
            exit()
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    main()
