from flask import Flask
from controllers import create
from controllers.create import create_index, create_recall

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


app.add_url_rule('/create', methods=['GET'], view_func=create_index)
app.add_url_rule('/create/recall', methods=['POST'], view_func=create_recall)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3134)
