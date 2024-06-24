class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo      # Tipo de la habitación (e.g., Sencilla, Doble, Suite)
        self.disponible = True  # Estado de disponibilidad de la habitación

    def __str__(self):

        # Método para devolver una representación en cadena del objeto
        return f"Habitación {self.numero} ({self.tipo}), Disponible: {self.disponible}"

    def ocupar(self):
        # Método para marcar la habitación como ocupada
        self.disponible = False

    def liberar(self):
        # Método para marcar la habitación como disponible
        self.disponible = True

# Ejemplo de uso
habitacion1 = Habitacion(101, "Sencilla")
print(habitacion1)  # Mostrar información de la habitación
habitacion1.ocupar()  # Ocupar la habitación
print(habitacion1)  # Mostrar información actualizada de la habitación
