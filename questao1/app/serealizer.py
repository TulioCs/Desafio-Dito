from flask_marshmallow import Marshmallow
from .model import Data


ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class DataSchema(ma.ModelSchema):
    class Meta:
        model = Data
