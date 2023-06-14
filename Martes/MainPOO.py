from cosas import Alumno

def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    # Para cambiar el nombre de una variable, se hace desde la clase
    print("------------")
    Alumno.facultad = "TEC de Monterrey"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("--- Objetos: ")
    print(vars(al1))
    print(vars(al2))
    print("---- Modificar atributos publicos ----")
    al1.edad = 99
    print(vars(al1))
    print(vars(al2))
"""
    al1 = Alumno("Diego", 19, "ICO")
    al2 = Alumno("Montse", 20, "Arquitectura")
    print(vars(al1))
    al1.__edad = 69
    print(al1.__edad)
    print(vars(al1))

main()