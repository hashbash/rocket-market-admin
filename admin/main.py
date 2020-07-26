from admin import app, db
from flask import send_file
from flask_admin.contrib.sqla import ModelView
import flask_admin as admin
from admin import models


@app.route('/favicon.ico')
def favicon():
    return send_file('static/favicon.ico')


# Create admin
admin = admin.Admin(app, name='Rocket: admin', template_mode='bootstrap3')
admin.add_view(ModelView(models.Tickers, db.session))
