"""
Gestor de Metas Personales
Aplicacion de consola para registrar y hacer seguimiento a tus metas.
"""

metas = []


def agregar_meta(descripcion):
    if descripcion.strip() == "":
        print("La meta no puede estar vacia")
        return
    nueva_meta = {"descripcion": descripcion, "cumplida": False}
    metas.append(nueva_meta)


def ver_metas():
    if len(metas) == 0:
        print("Aun no tienes metas registradas.")
        return
    for i, meta in enumerate(metas):
        estado = "Cumplida" if meta["cumplida"] else "Pendiente"
        print(f"{i}. {meta['descripcion']} - {estado}")

def eliminar_meta(indice):
    if 0 <= indice < len(metas):
        eliminada = metas.pop(indice)
        print(f"Meta eliminada: {eliminada['descripcion']}")
    else:
        print("Índice no válido")

def contar_cumplidas():
    total = sum(1 for m in metas if m["cumplida"])
    print(f"Metas cumplidas: {total} de {len(metas)}")


def mostrar_menu():
    print("\n=== Gestor de Metas Personales ===")
    print("Organiza tus objetivos y sigue tu progreso")
    print("1. Agregar meta")
    print("2. Ver metas")
    print("3. Salir")


continuar = True

while continuar:
    mostrar_menu()
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        descripcion = input("Describe tu meta: ")
        agregar_meta(descripcion)
    elif opcion == "2":
        ver_metas()
    elif opcion == "3":
        print("Hasta luego!")
        continuar = False
    else:
        print("Opcion no valida, intenta de nuevo.")
