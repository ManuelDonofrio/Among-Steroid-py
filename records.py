import sqlite3

def crear_tabla():
    try:
        conexion = sqlite3.connect('records.db')
        conexion.execute('''CREATE TABLE IF NOT EXISTS records (
                            nombre TEXT,
                            puntaje INTEGER
                        )''')
        conexion.execute('''CREATE INDEX IF NOT EXISTS idx_puntaje ON records (puntaje DESC)''')  # Agregar índice de ordenamiento
        conexion.close()
    except sqlite3.Error as error:
        print("Error al crear la tabla:", error)

def guardar_puntaje(nombre, puntaje):
    try:
        conexion = sqlite3.connect("records.db")
        c = conexion.cursor()
        c.execute("INSERT INTO records (nombre, puntaje) VALUES (?, ?)", (nombre, puntaje))
        conexion.commit()
        conexion.close()
        print("Puntaje guardado")
    except sqlite3.Error as error:
        print("Error al guardar el puntaje:", error)

def obtener_mejores_puntajes(limit=3):
    try:
        conexion = sqlite3.connect("records.db")
        c = conexion.cursor()
        c.execute("SELECT nombre, puntaje FROM records ORDER BY puntaje DESC LIMIT ?", (limit,))
        puntajes = c.fetchall()
        conexion.close()
        print("Puntajes obtenidos exitosamente")
        return puntajes
    except sqlite3.Error as error:
        print("Error al obtener los puntajes:", error)