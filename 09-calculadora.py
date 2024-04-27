print("Bienvenido a la Calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi, div")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no valida XD")
        break

    print(f"El resultado es {resultado}")
