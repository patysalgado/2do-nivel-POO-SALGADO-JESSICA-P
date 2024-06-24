class Cliente:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre  # Nombre del cliente
        self.identificacion = identificacion  # Identificación del cliente

    def __str__(self):
        # Método para devolver una representación en cadena del objeto
        return f"Cliente: {self.nombre}, ID: {self.identificacion}"

# Ejemplo de uso
cliente1 = Cliente("Juan Pérez", "12345678")
print(cliente1)  # Mostrar información del cliente
