from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.app_context().push()
Bootstrap(app=app)


@app.route('/')
def home_page():
    return  render_template('index.html')

# TODO Change debug to False
if __name__ == "__main__":
    app.run(debug=True)