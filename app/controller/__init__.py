from flask import Blueprint
from flask_restplus import Api

# import namespace
from .auth_controller import api as auth_ns
from .kriteria_controller import api as kriteria_ns
from .subkriteria_controller import api as subkriteria_ns
from .alternatif_controller import api as alternatif_ns
from .hasil_controller import api as hasil_ns

controller = Blueprint("api", __name__)
api = Api(controller, version="1.0", title="RESTAPI untuk proyek 3")
api.add_namespace(auth_ns, path="/proyek/user")
api.add_namespace(kriteria_ns, path="/proyek/kriteria")
api.add_namespace(subkriteria_ns, path="/proyek/subkriteria")
api.add_namespace(alternatif_ns, path="/proyek/alternatif")
api.add_namespace(hasil_ns, path="/proyek/hasil")
