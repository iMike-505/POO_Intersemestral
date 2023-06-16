from Cosas import Alumno, Perro

def main():
    al1 = Alumno("Joss", 22, "ICO")
    print(vars(al1))
    al1.__nombre = "Reyes"
    print(vars(al1))
    al1.set_nombre("Esmeralda")
    print(vars(al1))
    print("------S T R I N G--------")
    print(al1)

    al1.set_edad(999)
    print(al1)

    al1.estudiar(4)

    print("---- P E R R O ------")
    perro1 = Perro("Poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "De la calle" # Set en notación Pythonic
    print(vars(perro1))
    perro1.__raza = "otra"
    print(vars(perro1))
    perro1.edad= 12
    perro1.estatura = 0.43
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)

main()