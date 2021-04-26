from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, FileField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class NewNoteForm(FlaskForm):
    text = TextAreaField('Напишите что-нибудь', validators=[DataRequired()])
    photos = FileField('Фото')
    videos = FileField('Видео')
    audios = FileField('Аудио')
    submit = SubmitField("Создать")
    