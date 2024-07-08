# Clase base Empleado
class Empleado:
    def __init__(self, nombre, edad, salario):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad  # Atributo encapsulado
        self._salario = salario  # Atributo encapsulado

    def obtener_nombre(self):
        return self._nombre

    def obtener_edad(self):
        return self._edad

    def obtener_salario(self):
        return self._salario

    def descripcion(self):
        return f"{self._nombre}, {self._edad} años, salario: {self._salario}"

    def calcular_bono(self):
        return self._salario * 0.10  # Bono del 10%


# Clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self._departamento = departamento  # Atributo adicional

    def obtener_departamento(self):
        return self._departamento

    # Sobrescribimos el método descripcion
    def descripcion(self):
        return f"Gerente: {self._nombre}, {self._edad} años, departamento: {self._departamento},salario:{self._salario}"

    # Sobrescribimos el método calcular_bono
    def calcular_bono(self):
        return self._salario * 0.20  # Bono del 20%


# Clase derivada Desarrollador
class Desarrollador(Empleado):
    def __init__(self, nombre, edad, salario, lenguaje):
        super().__init__(nombre, edad, salario)
        self._lenguaje = lenguaje  # Atributo adicional

    def obtener_lenguaje(self):
        return self._lenguaje

    # Sobrescribimos el método descripcion
    def descripcion(self):
        return f"Desarrollador: {self._nombre}, {self._edad} años, lenguaje: {self._lenguaje}, salario: {self._salario}"

    # Sobrescribimos el método calcular_bono
    def calcular_bono(self):
        return self._salario * 0.15  # Bono del 15%


# Función principal
def main():
    # Crear instancia de Empleado
    empleado = Empleado("Juan Pérez", 30, 50000)
    print(empleado.descripcion())
    print(f"Bono: {empleado.calcular_bono()}")

    # Crear instancia de Gerente
    gerente = Gerente("Ana Gómez", 40, 70000, "Ventas")
    print(gerente.descripcion())
    print(f"Bono: {gerente.calcular_bono()}")

    # Crear instancia de Desarrollador
    desarrollador = Desarrollador("Luis Díaz", 25, 60000, "Python")
    print(desarrollador.descripcion())
    print(f"Bono: {desarrollador.calcular_bono()}")

    # Polimorfismo: lista de empleados
    empleados = [empleado, gerente, desarrollador]
    for emp in empleados:
        print(emp.descripcion())
        print(f"Bono: {emp.calcular_bono()}")


# Ejecutar la función principal
if __name__ == "__main__":
    main()
