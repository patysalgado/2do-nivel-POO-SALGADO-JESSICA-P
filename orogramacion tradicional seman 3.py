# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = [30.4,29.2,31.6,28.7,27.4,29.3,27.7]
    for dia in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas

# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio
# Función principal para ejecutar el programa
def main():
    print("Bienvenido al programa de cálculo del promedio semanal de temperatura.")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de la temperatura es: {promedio:.2f} grados.")

# Ejecutar el programa principal
if _name_==_main_:
    main()