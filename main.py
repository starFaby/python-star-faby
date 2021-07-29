from flask import render_template as render, flash
from app import createApp
from app.migrate import initDb

app = createApp()

@app.errorhandler(404)
def notFound(error):
    return render('errors/error404.html')

@app.errorhandler(500)
def notFound(error):
    return render('errors/error500.html')

@app.route("/")
def index():
    return render('index.html')

@app.route("/database")
def database():
    initDb()
    return "Creacion de la base de datos exitosamente"