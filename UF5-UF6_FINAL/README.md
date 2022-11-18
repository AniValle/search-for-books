## App Web Libreria

### Ani Valle

Contenido:

- Carpeta templates
    1. Index.html

- Carpeta Static
    1. css 
    2. carpeta img
        * contiene 8 imagenes

- fichero app.py
El contenido de la app
contiene 3 funciones
    * conexión con la base de datos.
    * Obetener la ruta de las imagenes.
    * la función index.

- createdb.py
    * Creación de la base de datos.
    * Creación de la tabla.
    * Insertar filas mediante un fichero .json
    * Buscador en la base de datos cogiendo usando 'like'.

- libredia.db
    * Tabla Libros.

- libros.json
    * datos de los libros.

- utils.py
    * Función para obtener la ruta padre.
    * Función para importar el .json
    * Función para convertis tipo.


- Carpeta **version-beta**
    *app fallida -> fichero .py con una app que no me funcionó.
    *database -> dos ficheros para crear bases de datos de forma diferente.
    
        1. crear_database.py
            Contiene funciones para
                * crear base de datos
                * crear la tabla
                * insertar filas.
                * buscar datos.
                * actualizar datos.
                * eliminar datos.

        2. crear_database_limpia.py
            * Funciones para crear bases de datos, tabla, insertar filas con exepciones.
