from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Desenvolvedor(Resource):
    def get(self):
        return 'Olá Dev'


api.add_resource(Desenvolvedor, '/dev')

if __name__ == '__main__':
    app.run(debug=True)
