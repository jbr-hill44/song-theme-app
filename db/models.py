from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from db.database import Base

class Theme(Base):
    __tablename__ = "themes"

    theme_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

class Song(Base):
    __tablename__ = "songs"

    song_id = Column(Integer, primary_key=True, index=True)
    spotify_track_id = Column(String, unique=True, index=True)
    title = Column(String, index=True, nullable=False)
    artist = Column(String, index=True)
    album = Column(String, index=True)
    release_date = Column(DateTime)
    genre = Column(String)

class Submission(Base):
    __tablename__ = "submissions"

    submission_id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("songs.song_id"))
    theme_id = Column(Integer, ForeignKey("themes.theme_id"))
    submitter_name = Column(String, nullable=False)
    submission_date = Column(DateTime, default=datetime.now)
    status = Column(String, default="pending")  # pending, approved, rejected
