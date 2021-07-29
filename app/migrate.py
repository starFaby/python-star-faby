from .database import *

def createDb():
    """Metodo de cracion de la base de datos"""
    db.drop_all()
    db.create_all()

def initDb():
    """Metodo de inicializacion de uestra base de datos"""
    createDb()
    admin = User(
        name="faby",
        lastname="star",
        username="faby",
        email="star._faby@hotmail.com",
        isAdmin=True,
        cellphone="0983856136",
    )
    admin.onSetPassord("faby123")
    db.session.add(admin)
    db.session.commit()