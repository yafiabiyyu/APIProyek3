from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import NotFound, HTTPException

from ..service.metode_service import MSaw

api = Namespace("hasil", "Endpoint untuk hasil")
msaw = MSaw()

@api.route("/data/konversi")
class KriteriaResource(Resource):
    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk ambil data konversi",
    )
    # @api.marshal_list_with(DataKriteria, envelope="data")
    def get(self):
        try:
            return msaw.normalisasi_data()
        except Exception as e:
            api.abort(400, e)

@api.route("/data/normalisasi")
class KriteriaResource(Resource):
    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk ambil data normalisasi",
    )
    # @api.marshal_list_with(DataKriteria, envelope="data")
    def get(self):
        try:
            normalisasi = msaw.normalisasi_api()
            # print(normalisasi)
            return normalisasi
        except Exception as e:
            api.abort(400, e)

@api.route("/data/vector")
class KriteriaResource(Resource):
    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk ambil data vector",
    )
    # @api.marshal_list_with(DataKriteria, envelope="data")
    def get(self):
        try:
            vector = msaw.vector_data()
            # print(normalisasi)
            return vector
        except Exception as e:
            api.abort(400, e)

@api.route("/data/hasil/msaw")
class KriteriaResource(Resource):
    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk ambil data msaw",
    )
    # @api.marshal_list_with(DataKriteria, envelope="data")
    def get(self):
        try:
            vector = msaw.jumlah_and_rank()
            # print(normalisasi)
            return vector
        except Exception as e:
            api.abort(400, e)