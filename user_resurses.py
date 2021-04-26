from flask import jsonify, render_template, make_response, url_for
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.users import User


class UserResourse(Resource):
    def get(self, user_id):
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        data = user.to_dict(only=('name', 'surname', 'nickname', 'email', 'created_date'))
        img = f'http://127.0.0.1:5000/static/photo/{user_id}.jpg'
        print(img)
        return make_response(render_template('user.html', id=user_id, nick=data['nickname'], img=img, name=f"{data['name']} {data['surname']}"))

class ListUserResourse(Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('name', 'surname', 'nickname', 'email', 'created_date')) for item in user]})