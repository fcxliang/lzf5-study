from paste.util.template import url
from routes import Mapper

# from test import app
#
#
# @app.route('/')
# @app.route('/index')
# def index():
#     return "hello world!"

m = Mapper()
m.resource('location', 'locations',parent_resource=dict(member_name='region',collection_name='regions'))
print m.match("/regions/14/location")

