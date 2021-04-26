from flask import Flask, render_template, redirect, url_for
from flask_restful import reqparse, abort, Api, Resource
from os import path
from data import db_session
from data.users import User
from forms.user import RegisterForm, LoginForm
from forms.note import NewNoteForm
import user_resurses
import note_resurses

PEOPLE_FOLDER = path.join('static', 'photo')

app = Flask(__name__)
api = Api(app)
CSRF_ENABLED = True

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

api.add_resource(user_resurses.UserResourse, '/user/<int:user_id>')
api.add_resource(user_resurses.ListUserResourse, '/users')

""" api.add_resource(note_resurses.NoteResourse, 'note/<int:note_id>')
api.add_resource(note_resurses.NoteListResourse, '/notes')  """


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    print(form.photo.raw_data)
    """ ph = open() """
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            nickname=form.nickname.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect(f"/user/{user.id}")
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if not db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('login.html', title='Авторизация', form=form, 
                                    message="Неверный адрес электронной почты")
        else:
            user = db_sess.query(User).filter(User.email == form.email.data).first()
            if user.check_password(form.password.data):
                print(user.id)
                db_sess.commit()
                return redirect(f"/user/{user.id}")
            else:
                return render_template('login.html', title='Авторизация', form=form, 
                                    message="Неверный пароль")
        db_sess.commit()
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/new_note_<int:user_id>', methods=['GET', 'POST'])
def new_note(user_id):
    form = NewNoteForm()
    if form.validate_on_submit():
        parser = reqparse.RequestParser()
        parser.add_argument("text", default="")
        parser.add_argument("photos", default=[])
        parser.add_argument("videos", default=[])
        parser.add_argument("audios", default=[])
        args = parser.parse_args()
        print(args)
    return render_template('new_note.html', title='Новая запись', form=form)

def main():
    db_session.global_init("db/blogs.sqlite")
    app.run()

if __name__ == '__main__':
    main()
