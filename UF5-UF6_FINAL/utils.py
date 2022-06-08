import json
import createdb as db
from   pathlib  import Path

""" Utils.py contiene funciones que voy a usar más adelante.
    * Funciones <Obtener Datos>
        -Get_base_dir: Obtener el directorio base.
        - Read_json_file: Leer los datos desde un archivo .json

    * Funciones <Filtrar Datos>
        -Convertir el tipo de los datos.
"""

###############################################################################
# Funciones <Obtener Datos>
###############################################################################

# Obtenga el directorio base de este script de python usando __file__.
# -----------------------------------------------------------------------------
def get_base_dir() -> Path:

    this_file_path: Path = Path(__file__)
    base_dir:       Path = this_file_path.resolve().parent

    return base_dir


# Obtener Datos .json
# -----------------------------------------------------------------------------
def read_json_file(json_filename: str) -> list[dict]:

    base_dir:  Path       = get_base_dir()
    json_path: Path       = base_dir/json_filename
    json_text: str        = json_path.read_text()
    data:      list[dict] = json.loads(json_text)

    return data


###############################################################################
# Funciones <Filtrar Datos>
###############################################################################

#--------------------------------------------------------------------
# Convertir el tipo de los datos
#--------------------------------------------------------------------
def convert_result(source: list[tuple]) -> list[str]:
    """Convert the data to be returned to the template.
        Input: list of tuples, are the data returned in response to the query on the web.
        Output: a list of strings that I can work with better.
    """

    collecter = []
    for elem in source:
        for data in elem:
            collecter.append(str(data))
    #result: str = source[0][-1]
    
    return collecter #type: ignore



