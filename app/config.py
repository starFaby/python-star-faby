class Config:
    """clase de configuracion de flask """
    SECRET_KEY="starfaby"
    SQLALCHEMY_DATABASE_URI="sqlite:///../ideas.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
