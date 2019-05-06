from functools import wraps
from flask import redirect, url_for, session
import os
import secrets
from PIL import Image


def logged_in(f):
    @wraps(f)
    def decorated_funcion(*args, **kwargs):
        if not session.get('id'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_funcion


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/user_images', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn