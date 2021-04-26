import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Note(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'note'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    test_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    photo_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    video_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    music_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
                
    user = orm.relation('User')