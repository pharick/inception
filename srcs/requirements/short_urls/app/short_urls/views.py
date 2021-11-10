from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_wtf import FlaskForm
from wtforms.fields.html5 import URLField
from wtforms.validators import url
from hashlib import blake2b

from .models import Url
from . import db

bp = Blueprint('short_urls', __name__)


class UrlForm(FlaskForm):
    url = URLField(validators=(url(),))


@bp.route('/', methods=('GET', 'POST'))
def index():
    form = UrlForm(request.form)
    return render_template('short_urls/index.html', form=form)


@bp.route('/short', methods=('GET', 'POST'))
def short():
    form = UrlForm(request.form)

    if request.method == 'GET' or not form.validate_on_submit():
        return redirect(url_for('short_urls.index'))

    url = form.url.data
    url_obj = Url.query.filter_by(url=url).first()

    if url_obj is None:
        hash = blake2b(url.encode(), digest_size=5).hexdigest()
        url_obj = Url(url=url, hash=hash)
        db.session.add(url_obj)
        db.session.commit()

    short_url = f'https://cbelva.42.fr/short_urls/{url_obj.hash}'

    return render_template('short_urls/short.html', short_url=short_url)


@bp.route('/<hash>')
def go(hash):
    url_obj = Url.query.filter_by(hash=hash).first()

    if url_obj is None:
        abort(404)

    return redirect(url_obj.url)
