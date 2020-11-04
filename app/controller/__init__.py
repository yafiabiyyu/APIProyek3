from flask import Blueprint
from flask_restplus import Api

# import namespace
from .auth_controller import api as auth_ns
from .kriteria_controller import api as kriteria_ns

controller = Blueprint("api", __name__)
api = Api(controller, version="1.0", title="RESTAPI untuk proyek 3")
api.add_namespace(auth_ns, path="/proyek/user")
api.add_namespace(kriteria_ns, path="/proyek/kriteria")
