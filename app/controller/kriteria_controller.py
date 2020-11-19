from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import NotFound, HTTPException

from ..service.kriteria_service import KriteriaService

api = Namespace("kriteria", "Endpoint untuk Kriteria")
DataKriteria = api.model(
    "kriteria",
    {
        "_id": fields.String(readonly=True),
        "nama_kriteria": fields.String(
            required=True, description="Nama dari kriteria"
        ),
        "atribut": fields.String(
            required=True, description="Jenis atribut dari kriteria"
        ),
        "bobot": fields.Float(
            required=True,
            description="Bobot nilai dari setiap kriteria",
        ),
    },
)

DataBobot = api.model(
    "data_bobot",
    {
        "_id": fields.String(readonly=True),
        "nama_kriteria": fields.String(
            required=True, description="Nama dari kriteria"
        ),
        "bobot": fields.Float(
            required=True,
            description="Bobot nilai dari setiap kriteria",
        ),
    },
)

kriteria = KriteriaService()


@api.route("/data")
class KriteriaResource(Resource):
    @api.doc(
        response={200: "OK", 500: "Internal Server Error"},
        description="Endpoint untuk menyimpan data kriteria",
    )
    @api.expect(DataKriteria)
    def post(self):
        try:
            GetDataFromJson = request.json
            KriteriaData = kriteria.add_kriteria(GetDataFromJson)
            return jsonify(KriteriaData)
        except HTTPException as e:
            api.abort(500, e)

    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk ambil data alternatif",
    )
    @api.marshal_list_with(DataKriteria, envelope="data")
    def get(self):
        try:
            return kriteria.get_all_data()
        except Exception as e:
            api.abort(400, e)


@api.route("/data/<kode>")
class KriteriaSpesificData(Resource):
    @api.doc(
        responses={200: "OK", 404: "Not Found"},
        description="Endpoint untuk ambil data kriteria spesifik",
    )
    @api.marshal_with(DataKriteria)
    def get(self, kode):
        KriteriaByKode = kriteria.get_spesifik_kriteria(kode)
        if not KriteriaByKode:
            api.abort(
                404,
                "Data Kriteria dengan kode {} tidak ditemukan".format(
                    kode
                ),
            )
        else:
            return KriteriaByKode

    @api.doc(responses={200: "OK", 404: "Not Found"})
    @api.expect(DataKriteria)
    def put(self, kode):
        print(api.payload)
        try:
            status, message = kriteria.update_kriteria(
                kode, api.payload
            )
        except Exception as e:
            api.abort(400, e.__doc__)
        else:
            if status:
                return message
            else:
                return message

@api.route("/data/bobot")
class BobotResource(Resource):
    @api.marshal_list_with(DataBobot, envelope="data")
    def get(self):
        try:
            return kriteria.ambil_bobot()
        except Exception as e:
            api.abort(400, e)