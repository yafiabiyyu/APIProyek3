from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import NotFound, HTTPException

from ..service.hasil_service import HasilService

api = Namespace("hasil", "Endpoint untuk hasil")
hasil = HasilService()

@api.route("/data/konversi")
class KonversiResource(Resource):
    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk ambil data konversi",
    )
    # @api.marshal_list_with(DataKriteria, envelope="data")
    def get(self):
        try:
            return hasil.get_konversi()
        except Exception as e:
            api.abort(400, e)

@api.route("/data/normalisasi")
class NormalisasiResource(Resource):
    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk ambil data normalisasi",
    )
    # @api.marshal_list_with(DataKriteria, envelope="data")
    def get(self):
        try:
            normalisasi = hasil.get_normalisasi()
            # print(normalisasi)
            return normalisasi
        except Exception as e:
            api.abort(400, e)

@api.route("/data/hasil/msaw")
class MsawResource(Resource):
    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk ambil data msaw",
    )
    # @api.marshal_list_with(DataKriteria, envelope="data")
    def get(self):
        try:
            msaw = hasil.get_hasil_msaw()
            # print(normalisasi)
            return msaw
        except Exception as e:
            api.abort(400, e)

@api.route("/data/hasil/saw")
class sawResource(Resource):
    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk ambil data saw",
    )
    # @api.marshal_list_with(DataKriteria, envelope="data")
    def get(self):
        try:
            saw = hasil.get_hasil_saw()
            # print(normalisasi)
            return saw
        except Exception as e:
            api.abort(400, e)