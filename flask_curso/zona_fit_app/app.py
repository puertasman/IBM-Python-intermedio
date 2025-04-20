""" Aplicación usuarios gimnasio """

from flask import Flask, render_template, redirect, url_for
from cliente_dao import ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma

app = Flask(__name__)


app.config['SECRET_KEY'] = 'llave_secreta_123'

# Variables
TITULO_APP = 'Zona Fit'

@app.route('/')
@app.route('/index.html')
def inicio():
    """ Renderiza index.html con datos que recibe """
    # Recuperamos los datos de la base de datos
    clientes_db = ClienteDAO.seleccionar()
    # Formulario cliente form vacío
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html',
                           titulo = TITULO_APP,
                           clientes = clientes_db,
                           forma = cliente_forma
                           )

@app.route('/guardar', methods = ['POST'])
def guardar():
    """ Guarda los datos del formulario como nuevo usuario """
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    if cliente_forma.validate_on_submit():
        # llenamos el cliente con los valores del formulario
        cliente_forma.populate_obj(cliente)
        if not cliente.id:
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actulizar(cliente)
    # redireccionamos a inicio
    return redirect(url_for('inicio'))

@app.route('/limpiar')
def limpiar():
    """ Vacía la información del formulario """
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>') # si es cadena no hay que indicarlo
def editar(id):
    """ Para poder cargar los datos de una persona en el formulario """
    cliente = ClienteDAO.seleccionar_id(id)
    cliente_forma = ClienteForma(obj=cliente)
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html',titulo = TITULO_APP,
                           clientes = clientes_db,
                           forma = cliente_forma)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    """ Para poder cargar los datos de una persona en el formulario """
    cliente = Cliente(id=id)
    cliente = ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)
