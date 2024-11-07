from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/') # Se establece la ruta para página de inicio
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST']) # Se establece la ruta 'ejercicio1' y permite los métodos GET y POST
def calculonotas():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        nota_final = (nota1 + nota2 + nota3) / 3
        # Se establece el resultado de aprobación a partir de la nota final y la asitencia
        if nota_final >= 40 and asistencia >= 75:
            resultado = "APROBADO"
        else:
            resultado = "REPROBADO"
        return render_template('ejercicio1.html', nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia, nota_final=nota_final, resultado=resultado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST']) # Se establece la ruta 'ejercicio2' y permite los métodos GET y POST
def nombremayor():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        largo1 = len(nombre1)
        largo2 = len(nombre2)
        largo3 = len(nombre3)
        # Se establece cuál es el nombre que tiene mayor cantidad de caracteres
        if largo1 > largo2 and largo1 > largo3:
            resultado1 = f'El nombre con mayor cantidad de caracteres es : {nombre1}'
            resultado2 = f'El nombre tiene : {largo1} caracteres'
        elif largo2 > largo1 and largo2 > largo3:
            resultado1 = f'El nombre con mayor cantidad de caracteres es : {nombre2}'
            resultado2 = f'El nombre tiene : {largo2} caracteres'
        elif largo3 > largo1 and largo3 > largo2:
            resultado1 = f'El nombre con mayor cantidad de caracteres es : {nombre3}'
            resultado2 = f'El nombre tiene : {largo3} caracteres'
        else:
            resultado1 = "Hay nombres con la misma cantidad de caracteres."
            resultado2 = ""
        return render_template('ejercicio2.html', nombre1=nombre1, nombre2=nombre2, nombre3=nombre3, largo1=largo1, largo2=largo2, largo3=largo3, resultado1=resultado1, resultado2=resultado2)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run() # Inicia el servidor web de Flask