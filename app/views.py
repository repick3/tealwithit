from flask import render_template
from app import app

from app.modules import models

import collections
@app.route('/')
def hello_world():
    return render_template('/index.html')

@app.route('/random/')
def random_teal():
    return(
        render_template('/post.html',
            post=models.get_random_post()
        )
    )