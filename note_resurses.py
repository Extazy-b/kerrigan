from flask import jsonify, render_template, make_response, url_for
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.users import User


parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('content', required=True)
parser.add_argument('is_private', required=True, type=bool)
parser.add_argument('is_published', required=True, type=bool)
parser.add_argument('user_id', required=True, type=int)



class NoteResourse(Resource):
    def get(self, note_id):
        session = db_session.create_session()
        user = session.query(Note).get(note_id)
        data = user.to_dict(only=('name', 'surname', 'nickname', 'email', 'created_date'))
        img = f'http://127.0.0.1:5000/static/photo/{user_id}.jpg'
        print(img)
        return make_response(render_template('user.html', id=user_id, nick=data['nickname'], img=img, name=f"{data['name']} {data['surname']}"))
    
    def post(self):
        pass


class ListNoteResourse(Resource):
    
    def get(self):
        pass
    
    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_published=args['is_published'],
            is_private=args['is_private']
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})