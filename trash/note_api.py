import flask

from . import db_session
from .notes import Note


blueprint = flask.Blueprint(
    'note_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/note')
def get_note():
    db_sess = db_session.create_session()
    note = db_sess.query(note).all()
    return jsonify(
        {
            'note':
                [item.to_dict(only=('title', 'content', 'user.name')) 
                 for item in note]
        }
    )