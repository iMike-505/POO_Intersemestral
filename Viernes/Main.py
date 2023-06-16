from Cosas import *

def main():
    per1= Persona("Pedro", 19)
    print(per1)
    print(Persona.descripcion)

    print("----- H E R E N C I A - A L U M N 0-----")
    al1 = Alumno("Carlos", 23, "319284556", "Economía")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Ismael"
    print(al2)
    al2.dormir()

    print("----- H E R E N C I A - P R O F E -----")
    profe1 = Profesor("Jesús", 30 + 16, 655482913, "Software")
    print(profe1)
    profe1.dormir()

    print("----- H E R E N C I A - A Y U D A N T E -----")
    ayudante = AyudanteProfesor("Pancho", 21, "12942913", "Agropecuario", 57613, "Software", 4)
    print(ayudante)
    ayudante.dormir()


main()