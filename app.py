import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from flaskapp import create_app
from flaskapp.config import DevelopmentConfig


from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Models
class Profile(db.Model):
	# Id : Field which stores unique id for every row in
	# database table.
	# first_name: Used to store the first name if the user
	# last_name: Used to store last name of the user
	# Age: Used to store the age of the user
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20), unique=False, nullable=False)
	last_name = db.Column(db.String(20), unique=False, nullable=False)
	age = db.Column(db.Integer, nullable=False)

	# repr method represents how one object of this datatable
	# will look like
	def __repr__(self):
		return f"Name : {self.first_name}, Age: {self.age}"

if __name__ == '__main__':
	app.run()


sentry_sdk.init(
    dsn=
    "https://1fdf413ccfcc4a249f79519bfc269965@o374456.ingest.sentry.io/5192531",
    integrations=[FlaskIntegration()],
)

app = create_app(config_class=DevelopmentConfig)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "must-revalidate, max-age=0"
    return response


if __name__ == "__main__":
    app.run()