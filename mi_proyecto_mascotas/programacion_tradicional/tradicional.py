def registrar_mascota():
    print("-- Registro de Mascota (Tradicional) --")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (Ej: perro, gato): ")
    edad = int(input("Ingrese la edad de la mascota: "))

    return nombre, especie, edad
def mostrar_mascota(nombre, especie, edad):
    print("INFORMACION DE LA MASCOTA")
    print(f"Nombre: {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad: {edad} años")

if __name__ == "__main__":

    nom, esp, ed = registrar_mascota()

    mostrar_mascota(nom, esp, ed)