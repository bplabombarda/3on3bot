from app import app, db


# =============================================================
# Define a base model for other database tables to inherit
# =============================================================
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,
                                default=db.func.now())
    date_modified = db.Column(db.DateTime,
                                default=db.func.now(),
                                onupdate=db.func.now())


# TODO: Fill in Game scehma
class Game(Base):

    __tablename__ = 'games'

    game_date =
    home_team =
    away_team =
    winner =

    def __init__(self, ):
        self.

    @property
    def serialize(self):
        # =============================================================
        # Return object data in easily serializeable format
        # =============================================================
        return {
            'id': self.id,
        }

    def __repr__(self):
        return '<Game %r>' % (self.mgage_id)