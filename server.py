from flask import Flask, render_template, request, redirect #redirect permite redireccionar

app=Flask(__name__)

#ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')

#ruta para la ruta /proceso
@app.route('/proceso', methods=['POST']) #acción del formulario
def proceso():
    print(request.form)
    return redirect('/exito') #la redireccion nos lleva a la nueva url


@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__=="__main__":
    app.run(debug=True)
