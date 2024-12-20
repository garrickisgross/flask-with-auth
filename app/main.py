import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from . import auth

bp = Blueprint('main', __name__, url_prefix='/main')


@bp.route('/')
@auth.login_required
def home():
    return render_template('main/home.html')