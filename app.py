from __future__ import with_statement

from flask import Flask, request, g, redirect, url_for, \
     abort, render_template, flash
from flask_bootstrap import Bootstrap

import webbrowser

DEBUG=True

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)

@app.route("/")
def root():
     return render_template("childExample.html")

if __name__ == '__main__':
     
     url = 'http://localhost'
     webbrowser.open(url)
     
     app.run(host='0.0.0.0', port=80)
