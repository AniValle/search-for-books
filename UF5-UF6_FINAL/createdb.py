import sqlite3 as sql
import utils
from   pathlib  import Path

"""Crear base de datos"""


# Crear base de datos.
# -----------------------------------------------------------------------------
def createdb():
    """Se crea la base de datos.
       Conectarse a la base de datos
       Y cerrar la conexión."""

    conn = sql.connect("libreria.db")
    conn.commit()
    conn.close()

#--------------------------------------------------------------------
def createtable():
    """Creación de tabla. """

    conn = sql.connect("libreria.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Libros (
            id INTEGER,
            titulo TEXT NOT NULL,
            precio REAL ,
            descripcion text
        )"""
    )

    conn.commit()
    conn.close()

#--------------------------------------------------------------------
def inserrows(librosjson: list[dict]):
    conn = sql.connect("libreria.db")
    cursor = conn.cursor()
    instruction: str = '''INSERT INTO Libros
                          VALUES (  
                              :id,
                              :titulo,
                              :precio,
                              :descripcion
                                );
                     '''
    cursor.executemany(instruction, librosjson)
    conn.commit()
    conn.close()

#--------------------------------------------------------------------
def query_book(column: str, search_book: str) -> list[tuple]:

    conn = sql.connect("libreria.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM libros WHERE upper(titulo) LIKE ?", (f"%{search_book.upper()}%", ))
    datos: list[tuple] = cursor.fetchall()
    conn.commit()
    conn.close()

    return datos


#--------------------------------------------------------------------
if __name__ == "__main__":

    # Read file json
    libros_json: list[dict] = utils.read_json_file('libros.json')

    # * Funciones crear daba base
    # createdb()

    # * Crear tabla
    # createtable()

    # * Insertar datos
    # inserrows(libros_json)

    # Query
    # print(query_book('titulo', 'El Duque'))
