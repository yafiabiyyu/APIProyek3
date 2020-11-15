from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import NotFound, HTTPException

from ..service.subkriteria_service import SubkriteriaService

api = Namespace("SubKriteria", "Endpint untuk subkriteria")
DataSub = api.model(
    "subkriteria",
    {
        "_id": fields.String(readonly=True),
        # "jenis_kriteria": fields.String(
        #     required=True, description="Kode dari kriteria"
        # ),
        "nama_subkriteria": fields.String(
            required=True, description="Nama dari subkriteria"
        ),
        "nilai": fields.Float(
            required=True, description="Nilai dari subkriteria"
        ),
    },
)

subkriteria = SubkriteriaService()


@api.route("/data")
class SubkriteriaResource(Resource):
    @api.doc(
        response={200: "OK", 500: "Internal Server Error"},
        description="Endpoint untuk menyimpan data kriteria",
    )
    @api.expect(DataSub)
    def post(self):
        try:
            GetDataFromJson = request.json
            subkriteriaData = subkriteria.add_subkriteria(
                GetDataFromJson
            )
            return jsonify(subkriteriaData)
        except HTTPException as e:
            api.abort(500, e)


@api.route("/data/<kode_kriteria>")
class SubkriteriaResourceSpesific(Resource):
    @api.doc(
        responses={200: "OK", 404: "Not Found"},
        description="Endpoint untuk ambil data kriteria spesifik",
    )
    @api.marshal_list_with(DataSub, envelope="data")
    def get(self, kode_kriteria):
        getSubkrit = subkriteria.get_list_subkriteria_data(
            kode_kriteria
        )
        if not getSubkrit:
            api.abort(
                404,
                "Data subkriteria dengan kode {} tidak ditemukan".format(
                    kode_kriteria
                ),
            )
        else:
            return getSubkrit


@api.route("/data/<kode_subkriteria>")
class SubkriteriaUpdate(Resource):
    @api.doc(responses={200: "OK", 404: "Not Found"})
    @api.expect(DataSub)
    def put(self, kode_subkriteria):
        print(api.payload)
        try:
            status, message = subkriteria.update_subkriteria(
                kode_subkriteria, api.payload
            )
        except Exception as e:
            api.abort(400, e)
        else:
            if status:
                return message
            else:
                return message

    @api.doc(responses={200: "OK", 404: "Not Found"})
    def delete(self, kode_subkriteria):
        try:
            data = subkriteria.delete_subkriteria(kode_subkriteria)
            return jsonify(data)
        except Exception as e:
            api.abort(404, e)
