from flask import Blueprint, current_app, request
from .model import Data
from .serealizer import DataSchema

bp_data = Blueprint('date', __name__)


@bp_data.route('/events', methods=['GET'])
def mostrar():
    ds = DataSchema(many=True)
    result = Data.query.with_entities(Data.event, Data.timestamp)
    return ds.jsonify(result), 200

@bp_data.route('/events/cadastrar', methods=['POST'])
def cadastrar():
    ds = DataSchema()
    
    data = ds.load(request.json)
    print(data)
    current_app.db.session.add(data)
    current_app.db.session.commit()
    return ds.jsonify(data), 201


@bp_data.route('/autocomplete/<string>', methods=['GET'])
def autocomplete(string):
    ds = DataSchema(many=True)
    if (len(string) < 2):
        result = {}
        return ds.jsonify(result), 200
    else:
        search = "{}%".format(string)
        result = Data.query.filter(Data.event.like(search)).with_entities(Data.event, Data.timestamp)
        result = sorted(result)
        return ds.jsonify(result), 200