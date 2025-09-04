# Pruebas de ejemplo en un solo print
print(
    "Pruebas de ejemplo:\n"
    "abc12     → Acepta\n"
    "123abc    → No Acepta\n"
    "A1B2C3    → Acepta\n"
    ".a         →No Acepta\n"
    "Z9        → Acepta\n"
    "9Z        → No Acepta\n"
    "a_b       → No Acepta\n"
    "Hola123   → Acepta\n"
    "Hola@123  → No Acepta\n"
    "12.3A.Z -> No Acpeta" 
)

# Bucle interactivo
while True:
    prueba = input("Ingrese cadena (ENTER para salir): ")
    if not prueba:
        break

    estado = True

    # Validar primer carácter (debe ser letra)
    if not (('a' <= prueba[0] <= 'z') or ('A' <= prueba[0] <= 'Z')):
        estado = False
    else:
        # Validar el resto (letras o dígitos)
        for c in prueba[1:]:
            if not (('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')):
                estado = False
                break

    if estado:
        print("Acepta")
    else:
        print("No Acepta")


while True:
    prueba = input("Ingrese cadena (ENTER para salir): ")
    if not prueba:
        break

    estado = True

    if not (('a' <= prueba[0] <= 'z') or ('A' <= prueba[0] <= 'Z')):
        estado = False
    else:

        for i in prueba[1:]:
            if not (('a' <= i <= 'z') or ('A' <= i <= 'Z') or ('0' <= i <= '9')):
                estado = False
                break

    if estado:
        print("Acepta")
    else:
        print("No Acepta")

