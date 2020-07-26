from admin import app
from admin import db
import os
import os.path as op
import argparse


# Build a sample db on the fly, if one does not exist yet.
app_dir = op.join(op.realpath(os.path.dirname(__file__)), 'admin')

parser = argparse.ArgumentParser()
parser.add_argument('--create-schema', dest='create_schema', type=str, help='Create db schema')
args = parser.parse_args()

if args.create_schema == 'y':
    db.drop_all()
    db.create_all()
    db.session.commit()

# Start app
app.run(debug=True)
