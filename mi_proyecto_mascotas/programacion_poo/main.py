from mascota import Mascota

if __name__ == "__main__":
    print("---Gestion de mascota con POO ---\n")

    mascota1 = Mascota("Jachi", "Perro", 5)
    mascota2 = Mascota("Luna", "Gato", 2)

    print("[Datos de Mascota 1]")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()

    print("-" * 40)

    print("[Datos de mascota 2]")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()