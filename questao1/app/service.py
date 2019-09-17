from flask import Blueprint, current_app, request
from .model import Data
from .serealizer import DataSchema

bp_data = Blueprint('date', __name__)


@bp_data.route('/events', methods=['GET'])
def mostrar():
    ds = DataSchema(many=True)
    result = Data.query.all()
    return ds.jsonify(result), 200

@bp_data.route('/events/cadastrar', methods=['POST'])
def cadastrar():
    ds = DataSchema()
    
    data, error = ds.load(request.json)
    print(data)
    current_app.db.session.add(data)
    current_app.db.session.commit()
    return ds.jsonify(data), 201

    # return {},200

