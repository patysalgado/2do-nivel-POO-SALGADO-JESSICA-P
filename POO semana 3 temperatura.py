class ClimaDiario:
    def _init_(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        # Lista de temperaturas de ejemplo
        self.temperaturas = [30.4, 29.2, 31.6, 28.7, 27.4, 29.3, 27.7]
        print(f"Temperaturas ingresadas: {self.temperaturas}")

    def calcular_promedio(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio

# Clase principal que utiliza ClimaDiario
class ClimaSemanal:
    def _init_(self):
        self.clima_diario = ClimaDiario()

    def ejecutar(self):
        print("Bienvenido al programa de cálculo del promedio semanal de temperatura.")
        self.clima_diario.ingresar_temperaturas()
        promedio = self.clima_diario.calcular_promedio()
        print(f"El promedio semanal de la temperatura es: {promedio:.2f} grados.")

# Crear una instancia de ClimaSemanal y ejecutar el programa
if _name_ == "_main_":
    programa = ClimaSemanal()
    programa.ejecutar()