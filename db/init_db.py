from db.database import sql_engine, Base
from db.models import Theme, Song, Submission

def init_db():
    Base.metadata.create_all(bind=sql_engine)

if __name__ == "__main__":
    init_db()