from app import db


# =============================================================
# Define a base model for other database tables to inherit
# =============================================================
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,
                                server_default=db.func.now())


class Game(Base):

    __tablename__ = 'games'

    away_team = db.Column(db.String(80))
    away_score = db.Column(db.Integer)
    home_team = db.Column(db.String(80))
    home_score = db.Column(db.Integer)
    winning_goal = db.Column(db.String(80))
    video_url = winning_goal = db.Column(db.Text)

    def __init__(self, away_team, away_score, home_team, home_score,
                    winning_goal, video_url):
        self.away_team = away_team
        self.away_score = away_score
        self.home_team = home_team
        self.home_score = home_score
        self.winning_goal = winning_goal
        self.video_url = video_url

    @property
    def serialize(self):
        # =============================================================
        # Return object data in easily serializeable format
        # =============================================================
        return {
            'id': self.id,
            'date': self.date_created
            'away_team': self.away_team,
            'away_score': self.away_score,
            'home_team': self.home_team,
            'home_score': self.home_score,
            'winning_goal': self.winning_goal,
            'video_url': self.video_url
        }

    def __repr__(self):
        return '<Game %r>' % self.id
