from flask import Flask
from flask_graphal import GraphQLView
from schema import schema

app = Flask(__name__)

@app.route('/')
def default_route():
    return "Hello, Default Route!"

@app.route('/index')
def index():
    return "Hello,World!"
@app.route('/get_name')
def get_name():
    return "My name flask!"

app.add_url_rule(
        '/gql',
        view_func=GraphQLView.ad_view('graphql', schema=schema, graphiql=True)
        )
app.run()
