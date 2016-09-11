from flask import render_template
from app import app

from app.modules import models

import collections
@app.route('/')
def hello_world():
    return render_template('/index.html')

@app.route('/teal/<gfy_url>/')
def get_specific_teal(gfy_url):
    try:
        post = models.check_for_post(gfy_url)
    except Exception as e:
        return (render_template('/404.html'), 404)
    
    return render_template('/post.html',
        post=post
    )

@app.route('/random/')
def random_teal():
    return(
        render_template('/post.html',
            post=models.get_random_post()
        )
    )
