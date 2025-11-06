import mysql.connector
import django.contrib.auth.hashers as hashers
from django.contrib.auth.hashers import make_password
from collections import Counter

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="461315",
        database="TallerMecanico"
    )

class Persona:
    def __init__(self, dni, nombre, apellido, tel, dir):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.tel = tel
        self.dir = dir

    def insertar(self):
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Persona (dni, nombre, apellido, tel, dir) VALUES (%s, %s, %s, %s, %s)",
                (self.dni, self.nombre, self.apellido, self.tel, self.dir)
            )
            conn.commit()
        except Exception as e:
            print("Error al insertar Persona:", e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def eliminar_Personas(dni):
        print(dni)
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Persona WHERE dni = %s", (dni,))
            conn.commit()
        except Exception as e:
            print("Error al eliminar Persona:", e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def actualizar_Personas(dni, nombre, apellido, tel, dir):
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE Persona 
                SET nombre=%s, apellido=%s, tel=%s, dir=%s 
                WHERE dni=%s
            """, (nombre, apellido, tel, dir, dni))
            conn.commit()
        except Exception as e:
            print("Error al actualizar Persona:", e)
        finally:
            cursor.close()
            conn.close()

class cliente(Persona):   
    def __init__(self, dni, nombre, apellido, tel, dir):
        super().__init__(dni, nombre, apellido, tel, dir)
        self.insertar()

    def insertar(self):
        super().insertar()
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Cliente (dni_Cliente) VALUES (%s)", (self.dni,))
            conn.commit()
        except Exception as e:
            print("Error al insertar Cliente:", e)
        finally:
            cursor.close()
            conn.close()
                             
    def obtener_Cliente_filtrada(nombre):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                SELECT c.cod_Cliente, p.dni, p.nombre, p.apellido, p.tel, p.dir
                FROM Cliente c
                JOIN Persona p ON c.dni_Cliente = p.dni
                WHERE c.cod_Cliente LIKE %s
                """, (nombre,))
                return cursor.fetchall()

    def obtener_Cliente():
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT c.cod_Cliente, p.dni, p.nombre, p.apellido, p.tel, p.dir
        FROM Cliente c
        JOIN Persona p ON c.dni_Cliente = p.dni
        """)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados

class Empleados(Persona):
    def __init__(self, dni, nombre, apellido, tel, dir):
        super().__init__(dni, nombre, apellido, tel, dir)
        self.insertar()

    def insertar(self):
        super().insertar()
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Empleado (dni_empleado) VALUES (%s)", (self.dni,))
            conn.commit()
            #Insertar un nuevo usuario con los datos de el empleado
            contraseña_encriptada = make_password(self.dni)
            cursor.execute("SELECT legajo FROM Empleado WHERE dni_empleado=%s", (self.dni,))
            legajo = cursor.fetchone()[0]
            cursor.execute("""
                INSERT INTO `auth_user` 
                (`password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`)
                VALUES
                (%s, NULL, 0, %s, %s, %s, %s, 0, 1, NOW())
            """, (contraseña_encriptada, f"Empleado#{legajo}", self.nombre, self.apellido, f"{self.nombre.lower().replace(" ", "_")}@example.com"))
            conn.commit()
        except Exception as e:
            print("Error al insertar Empleado:", e)
        finally:
            cursor.close()
            conn.close()
        
    def obtener_Empleado_filtrada(nombre):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                SELECT c.legajo, p.dni, p.nombre, p.apellido, p.tel, p.dir
                FROM Empleado c
                JOIN Persona p ON c.dni_empleado = p.dni
                WHERE c.legajo LIKE %s
                """, (nombre,))
            return cursor.fetchall()

    def obtener_Empleado():
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT c.legajo, p.dni, p.nombre, p.apellido, p.tel, p.dir
        FROM Empleado c
        JOIN Persona p ON c.dni_empleado = p.dni
        """)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados

class Provedores(Persona):
    def __init__(self, dni, nombre, apellido, tel, dir):
        super().__init__(dni, nombre, apellido, tel, dir)
        self.insertar()

    def insertar(self):
        super().insertar()
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Provedor (dni_Provedor) VALUES (%s)", (self.dni,))
            conn.commit()
        except Exception as e:
            print("Error al insertar Proveedor:", e)
        finally:
            cursor.close()
            conn.close()

    def obtener_Provedor_filtrada(nombre):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT c.cod_Provedor, p.dni, p.nombre, p.apellido, p.tel, p.dir
                    FROM Provedor c
                    JOIN Persona p ON c.dni_Provedor = p.dni
                    WHERE c.cod_Provedor LIKE %s
                """, (nombre,))
                return cursor.fetchall()

    def obtener_Provedor():
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.cod_Provedor, p.dni, p.nombre, p.apellido, p.tel, p.dir
            FROM Provedor c
            JOIN Persona p ON c.dni_Provedor = p.dni
        """)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados

class Repuestos:

    def obtener_Repuesto_filtrada(nombre):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT nombre, precio_x_unidad, cantidad
                    FROM Repuesto
                    WHERE nombre LIKE %s
                """, (f"%{nombre}%",))
                return cursor.fetchall()

    def obtener_Repuesto():
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT nombre, precio_x_unidad, cantidad FROM Repuesto")
                return cursor.fetchall()

    def insertar_repuesto(nombre, precio_x_unidad, cantidad):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Repuesto (nombre, precio_x_unidad, cantidad)
                    VALUES (%s, %s, %s)
                """, (nombre, precio_x_unidad, cantidad))
                conn.commit()

    def eliminar_repuesto(nombre):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Repuesto WHERE nombre = %s", (nombre,))
                conn.commit()

    def actualizar_repuesto(nombre, precio_x_unidad, cantidad):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    UPDATE Repuesto
                    SET precio_x_unidad=%s, cantidad=%s
                    WHERE nombre=%s
                """, (precio_x_unidad, cantidad, nombre))
                conn.commit()

class Usuarios:
    def get_options():
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT email FROM Usuarios ORDER BY email")
                resultados = cursor.fetchall()
                return [(email[0]) for email in resultados]

    def obtener_Usuario_filtrada(email):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM Usuarios
                    WHERE email LIKE %s
                """, (f"%{email}%",))
                return cursor.fetchall()

    def obtener_Usuario():
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Usuarios")
                return cursor.fetchall()

    def insertar_Usuario(email, contraseña,legajo):

        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT dni_empleado 
                    FROM Empleado
                    WHERE legajo=%s
                """, (legajo,))
                dni=cursor.fetchone()
                cursor.execute("""
                    SELECT nombre 
                    FROM Persona
                    WHERE dni=%s
                """, (dni[0],))
                
                nombre=cursor.fetchone()
                cursor.execute("""
                    INSERT INTO Usuarios 
                    VALUES (%s, %s, %s,%s)
                """, (email, nombre[0], contraseña,legajo))
                conn.commit()

    def eliminar_Usuario(email):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Usuarios WHERE email = %s", (email,))
                conn.commit()

    def actualizar_Usuario(email, contraseña,legajo):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    UPDATE Usuarios
                    SET contraseña=%s, legajo=%s
                    WHERE email=%s
                """, (contraseña,legajo, email))
                conn.commit()

    def Login(Email,Password):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT nombre
                    FROM Usuarios
                    WHERE email=%s AND contraseña=%s
                """, (Email, Password))
                resultado = cursor.fetchone()
                cursor.close()
                conn.close()
                return resultado

class Vehiculos:
    def obtener_Vehiculo_filtrada(matricula,dni_cliente):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT *
                    FROM Vehiculo
                    WHERE matricula LIKE %s,dni_cliente LIKE %s
                """, (f"%{matricula}%",dni_cliente))
                return cursor.fetchall()

    def obtener_Vehiculo(dni_cliente):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Vehiculo WHERE dni_cliente LIKE %s",(dni_cliente,))
                return cursor.fetchall()

    def obtener_Vehiculos():
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Vehiculo")
                return cursor.fetchall()

    def insertar_Vehiculo(matricula, color, modelo,dni_cliente):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Vehiculo
                    VALUES (%s, %s, %s, %s)
                """, (matricula, color, modelo, dni_cliente))
                conn.commit()

    def eliminar_Vehiculo(matricula):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Vehiculo WHERE matricula = %s", (matricula,))
                conn.commit()

    def actualizar_Vehiculo(matricula, color, modelo):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    UPDATE Vehiculo
                    SET color=%s, modelo=%s
                    WHERE matricula=%s
                """, (color, modelo, matricula))
                conn.commit()

class Presupuestos:

    def insertar_Presupuestos(matricula, repuesto, cantidad, legajo, precio):
        conn = conectar_bd()
        cursor = conn.cursor(buffered=True)
        id = None

        try:

            cursor.execute("SELECT id FROM Reparaciones WHERE matricula_vehiculo=%s", (matricula,))
            value = cursor.fetchall()

            if not value:
                cursor.execute(
                    "INSERT INTO Reparaciones (matricula_vehiculo) VALUES (%s)",
                    (matricula,)
                )
                conn.commit()
                cursor.execute("SELECT MAX(id) FROM Reparaciones")
                id = cursor.fetchone()[0]
            else:

                id = value[0][0]

            cursor.execute(
                """
                INSERT INTO detalle_Reparacion
                (reparacion_id, legajo, repuesto, cantidad, precio)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (id, legajo, repuesto, cantidad, precio)
            )

            conn.commit()

        except Exception as e:
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

        return id


    def obtener_Presupuesto(matricula):
        resultado = []
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Reparaciones WHERE matricula_vehiculo=%s", (matricula,))
                reparacion = cursor.fetchone() 
            
                if reparacion:  
                    resultado.append(reparacion)
                    id = reparacion[0]
                    cursor.execute("SELECT * FROM detalle_Reparacion WHERE reparacion_id=%s", (id,))
                    resultado.append(list(cursor.fetchall()))
                else:
                    resultado = []
        return resultado

    def eliminar_Presupuesto(id):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM detalle_Reparacion WHERE id=%s", (id,))
                conn.commit()
                
    def eliminar_Todo_Presupuesto(matricula):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute("SELECT id FROM Reparaciones WHERE matricula_vehiculo = %s", (matricula,))
                    resultado = cursor.fetchone()

                    if not resultado:
                        print("No se encontró reparación asociada a esa matrícula.")
                        return False

                    id_reparacion = resultado[0]

                    cursor.execute("DELETE FROM detalle_Reparacion WHERE reparacion_id = %s", (id_reparacion,))
                    conn.commit()

                    cursor.execute("DELETE FROM Reparaciones WHERE id = %s", (id_reparacion,))
                    conn.commit()
                    return True

                except Exception as e:
                    conn.rollback()
                    return False


    def actualizar_Presupuesto(repuesto, cantidad, legajo, precio, id):
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    UPDATE detalle_Reparacion
                    SET repuesto=%s, cantidad=%s, legajo=%s, precio=%s
                    WHERE id=%s
                """, (repuesto, cantidad, legajo, precio,id))
                conn.commit()

class FichaTecnica:
    def insertar_FichaTecnica(Vehiculo_Matricula):
        conn = conectar_bd()
        cursor = conn.cursor()

        try:
            presupuestos = Presupuestos.obtener_Presupuesto(Vehiculo_Matricula)

            if not presupuestos or len(presupuestos) < 2:
                return None

            detalles = presupuestos[1] 

            empleados = [fila[2] for fila in detalles]
            nroEmpleados = len(set(empleados))
            #arreglar esto
            subtotal = 0
            for fila in detalles:
                print("\nadas",fila)
                repuesto_nombre = fila[2]
                cantidad = fila[4]
                subtotal+=fila[5]
                cursor.execute("SELECT precio_x_unidad FROM Repuesto WHERE nombre = %s", (repuesto_nombre,))
                precio_repuesto = cursor.fetchone()

                if precio_repuesto:
                    subtotal += cantidad * precio_repuesto[0]

            #--------
            mano_de_obra = nroEmpleados * 1000
            total = subtotal + mano_de_obra

            cursor.execute("""
                INSERT INTO Ficha_Tecnica (Vehiculo_Matricula, nroEmpleados, subtotal, mano_de_obra, total)
                VALUES (%s, %s, %s, %s, %s)
            """, (Vehiculo_Matricula, nroEmpleados, subtotal, mano_de_obra, total))
            Presupuestos.eliminar_Todo_Presupuesto(Vehiculo_Matricula)
            conn.commit()
            return True

        except Exception as e:
            conn.rollback()
            return False

        finally:
            cursor.close()
            conn.close()

    def obtener_FichaTecnica():
        with conectar_bd() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Ficha_Tecnica")
                return cursor.fetchall()

