
import sqlite3 as sql
import createdb as db
import utils 
from flask import Flask, render_template, request
import os

"""
    AppWeb -> Bookshop.
    Contiene varias funciones.
    * Conecta a la base de datos.
    * Convierte los datos a un tipo apto para devolverlos.
    * Una función Index que mediante el metodo:
    'GET'  pide un html.
    'POST' envía los datos del formulario.
"""

# Flask initialization
#------------------------------------------------------------------------------
app:         Flask = Flask(__name__)

# Conexión con la base de datos
#--------------------------------------------------------------------
#@app.route('/')
def get_db_connection():
    """Connection with database."""

    conn = sql.connect('libreria.db')
    conn.row_factory = sql.Row
    return conn

# Imagenes de las portadas de los libros
#--------------------------------------------------------------------
@app.route("/")
def gallery():
    """
        Función 'Gallery' devuelve una lista con la ruta de las imagenes
        para poner usar en la platilla y crear una galeria de imagenes.
    """
    path_img = os.path.join('static', 'imgs')

    app.config["UPLOAD_FOLDER"] = path_img

    image_lists = os.listdir('static/imgs')
    imagelist = ['imgs/' + image for image in image_lists]
    return render_template("index.html", imagelist=imagelist)
    

#--------------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    """
        Recibe una peticion de busqueda mediante el metodo ''.
        Devuelve Los datos medinte el metodo ''.
    """
    conn = get_db_connection()

    if request.method == 'GET':
       return render_template('index.html')

    if request.method == 'POST':
        search_book:  str = request.form['searchBook']

    books: list[tuple] = db.query_book("titulo", search_book)  
    books_out = utils.convert_result(books)

    return render_template('index.html', libros=books_out)
    
# #------------------------------------------------------------------------------
# # Main
# #------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
