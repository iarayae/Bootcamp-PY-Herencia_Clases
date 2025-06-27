from membresia import Gratis

# Función para mostrar la información completa de una membresía
def mostrar_info_membresia(membresia):
    print("\nResumen de la membresía actual:")
    print(f"Tipo de membresía: {membresia.__class__.__name__}")
    print(f"Costo: ${membresia.costo}")
    print(f"Dispositivos permitidos: {membresia.dispositivos}")
    print(f"Correo del suscriptor: {membresia.correo_suscriptor}")

    if hasattr(membresia, 'dias_regalo'):
        print(f"Días de regalo: {membresia.dias_regalo}")
    else:
        print("Días de regalo: No aplica")

    if hasattr(membresia, 'modificar_control_parental'):
        print("Control parental: Disponible")

    if hasattr(membresia, 'incrementar_contenido_offline'):
        print("Contenido sin conexión: Disponible")

    print("-" * 40)

# Bienvenida y entrada de datos del usuario
print("Bienvenido al sistema de membresías de streaming.\n")
correo = input("Ingrese su correo electrónico: ")
tarjeta = input("Ingrese su número de tarjeta: ")

# Crear membresía inicial (Gratis)
membresia = Gratis(correo, tarjeta)

# Mostrar estado inicial
mostrar_info_membresia(membresia)

# Solicitar cambio de membresía
print("Tipos de membresía disponibles:")
print("1: Básica")
print("2: Familiar")
print("3: Sin Conexión")
print("4: Pro")

try:
    opcion = int(input("Seleccione una opción de cambio (1 al 4): "))
    nueva_membresia = membresia.cambiar_suscripcion(opcion)
    mostrar_info_membresia(nueva_membresia)
except ValueError:
    print("Opción no válida. Fin del programa.")
