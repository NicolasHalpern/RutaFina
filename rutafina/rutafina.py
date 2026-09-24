class Pedido:
    def __init__(self, id_pedido, cliente, direccion, producto):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.direccion = direccion
        self.producto = producto
        self.estado = "Registrado"  # Registrado, En Preparación, En Camino, Entregado
        self.repartidor_asignado = "Sin asignar"
        self.eta = "A calcular por el comercio"

    def __str__(self):
        return (f"Pedido #{self.id_pedido} | Cliente: {self.cliente} | "
                f"Producto: {self.producto} | Dirección: {self.direccion} | "
                f"Estado: [{self.estado}] | Repartidor: {self.repartidor_asignado} | ETA: {self.eta}")


class SistemaSmartGastro:
    def __init__(self):
        self.pedidos = []
        # Repartidores propios 
        self.repartidores = [
            {"id": 1, "nombre": "Carlos (Moto 1)"},
            {"id": 2, "nombre": "Lucía (Moto 2)"},
            {"id": 3, "nombre": "Marcos (Bici 1)"}
        ]
        self.contador_id = 101  # ID inicial de ejemplo

    def menu_usuario(self):
        while True:
            print("\n=== PORTAL DE CLIENTE (USUARIO) ===")
            print("1. Hacer un nuevo pedido")
            print("2. Consultar el estado de mi pedido (Evita llamadas al local)")
            print("3. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print("\n--- NUEVO PEDIDO ---")
                cliente = input("Su nombre y apellido: ")
                direccion = input("Dirección de entrega: ")
                producto = input("¿Qué desea pedir?: ")
                
                id_generado = self.contador_id
                self.contador_id += 1
                
                nuevo_pedido = Pedido(id_generado, cliente, direccion, producto)
                self.pedidos.append(nuevo_pedido)
                print(f"\n[¡ÉXITO!] Pedido registrado con el ID: #{id_generado}. ¡Ya fue enviado al comercio!")
                
            elif opcion == "2":
                try:
                    id_p = int(input("Ingrese su número de ID de pedido: "))
                    encontrado = False
                    for p in self.pedidos:
                        if p.id_pedido == id_p:
                            print("\n--- INFORMACIÓN EN TIEMPO REAL ---")
                            print(f"Estado actual: {p.estado}")
                            print(f"Repartidor en camino: {p.repartidor_asignado}")
                            print(f"Tiempo Estimado de Llegada (ETA): {p.eta}")
                            encontrado = True
                            break
                    if not encontrado:
                        print("\n[ERROR] No se encontró ningún pedido con ese ID.")
                except ValueError:
                    print("Por favor, ingrese un ID válido numérico.")
                    
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")

    def menu_restaurante(self):
        while True:
            print("\n=== PANEL DE CONTROL (RESTAURANT) ===")
            print("1. Ver todos los pedidos (Panel general)")
            print("2. Asignar repartidor (Adiós al 'a ojo')")
            print("3. Actualizar estado y ETA del pedido")
            print("4. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print("\n--- LISTADO DE PEDIDOS EN CURSO ---")
                if not self.pedidos:
                    print("No hay pedidos activos en este momento.")
                for p in self.pedidos:
                    print(p)
                    
            elif opcion == "2":
                print("\n--- ASIGNACIÓN DE REPARTIDORES PROPIOS ---")
                if not self.pedidos:
                    print("No hay pedidos para asignar.")
                    continue
                
                try:
                    id_p = int(input("ID del pedido a asignar: "))
                    p = self._buscar_pedido_objeto(id_p)
                    if not p:
                        print("[ERROR] Pedido no encontrado.")
                        continue
                        
                    print("\nRepartidores disponibles:")
                    for r in self.repartidores:
                        print(f"[{r['id']}] {r['nombre']}")
                        
                    id_rep = int(input("Seleccione el ID del repartidor: "))
                    rep_obj = next((r for r in self.repartidores if r["id"] == id_rep), None)
                    
                    if rep_obj:
                        p.repartidor_asignado = rep_obj["nombre"]
                        p.estado = "En Preparación"
                        p.eta = "25-35 mins"
                        print(f"\n[LOGÍSTICA] Pedido #{id_p} asignado correctamente a {rep_obj['nombre']}.")
                    else:
                        print("[ERROR] Repartidor no válido.")
                except ValueError:
                    print("Entrada numérica inválida.")
                    
            elif opcion == "3":
                print("\n--- ACTUALIZAR ESTADO / TIEMPOS ---")
                try:
                    id_p = int(input("ID del pedido a actualizar: "))
                    p = self._buscar_pedido_objeto(id_p)
                    if not p:
                        print("[ERROR] Pedido no encontrado.")
                        continue
                        
                    print(f"Estado actual: {p.estado} | ETA actual: {p.eta}")
                    print("Nuevos estados sugeridos: En Preparación, En Camino, Entregado")
                    nuevo_estado = input("Ingrese el nuevo estado: ")
                    nuevo_eta = input("Actualizar ETA (ej: 15 mins, Llegando, etc.): ")
                    
                    p.estado = nuevo_estado
                    if nuevo_eta.strip():
                        p.eta = nuevo_eta
                        
                    print(f"\n[ACTUALIZADO] Pedido #{id_p} actualizado con éxito.")
                except ValueError:
                    print("Datos inválidos.")
                    
            elif opcion == "4":
                break
            else:
                print("Opción inválida.")

    def _buscar_pedido_objeto(self, id_pedido):
        for p in self.pedidos:
            if p.id_pedido == id_pedido:
                return p
        return None


def main():
    sistema = SistemaSmartGastro()
    
    while True:
        print("\n========================================")
        print("    SISTEMA DE GESTIÓN - RUTAFINA    ")
        print("========================================")
        print("¿Cómo desea ingresar?")
        print("1. Soy Usuario (Cliente)")
        print("2. Soy Administrador / Restaurant (Comercio)")
        print("3. Salir del programa")
        
        rol = input("\nSeleccione su perfil: ")
        
        if rol == "1":
            sistema.menu_usuario()
        elif rol == "2":
            sistema.menu_restaurante()
        elif rol == "3":
            print("\n¡Gracias por utilizar RUTAFINA!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
