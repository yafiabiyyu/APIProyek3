from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import NotFound

from ..service.alternatif_service import AlternatifService
from ..service.seleksi_service import Seleksi

api = Namespace("alternatif", "Endpoint untuk alternatif")
data_alternatif = api.model(
    "alternatif",
    {
        "_id": fields.String(
            required=True,
            description="NIM mahasiswa yang ditambahkan kedalam alternatif",
        ),
        "nama_mahasiswa": fields.String(
            required=True,
            description="Nama yang akan ditambahkan ke alternatif",
        ),
        "alamat": fields.String(
            required=True,
            description="Alamat dari altrnatif yang akan ditambahkan",
        ),
        "jenis_kelamin": fields.String(
            required=True,
            description="Jenis kelamin yang akan ditambahkan ke alternatif",
        ),
        "subkriteria_id": fields.List(
            fields.String(
                required=True, description="ID dari subkriteria"
            )
        ),
    },
)
data_seleksi = api.model(
    "data_seleksi",
    {
        "_id": fields.String(
            required=True,
            description="NIM mahasiswa yang ditambahkan kedalam alternatif",
        ),
        "nama_mahasiswa": fields.String(
            required=True,
            description="Nama yang akan ditambahkan ke alternatif",
        ),
        "pendapatan_ortu": fields.String(
            required=True,
            description="Data pendapatan ortu alternatif"
        ),
        "tanggungan_ortu": fields.String(
            required=True,
            description="Data tanggungan ortu alternatif"
        ),
        "status_ortu": fields.String(
            required=True,
            description="Data status ortu alternatif"
        ),
        "semester": fields.String(
            required=True,
            description="Data semester alternatif"
        ),
        "ipk": fields.String(
            required=True,
            description="Data ipk alternatif"
        ),
    }
)

alternatif = AlternatifService()
seleksi = Seleksi()

@api.route('/data/seleksi')
class SeleksiResource(Resource):
    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk mengambil data seleksi",
    )
    @api.marshal_list_with(data_seleksi, envelope="data")
    def get(self):
        try:
            return seleksi.seleksi()
        except Exception as e:
            api.abort(404, e)

@api.route("/data")
class AlternatifResourceAll(Resource):
    # @jwt_required
    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk menyimpan data alternatif",
    )
    # @api.expect(data_alternatif)
    def post(self):
        try:
            GetAlternatifData = request.json
            AlternatifSatus = alternatif.add_alternatif(
                GetAlternatifData
            )
            return jsonify(AlternatifSatus)
        except Exception as e:
            print(e)
            api.abort(400, e)

    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk mengambil seluruh data alternatif",
    )
    @api.marshal_list_with(data_alternatif, envelope="data")
    def get(self):
        try:
            return alternatif.get_all_data()
        except Exception as e:
            api.abort(404, e)


@api.route("/data/<nim>")
class AlternatifByNim(Resource):
    @api.doc(responses={200: "OK", 404: "Not Found"})
    @api.marshal_with(data_alternatif)
    def get(self, nim):
        DataAlternatifByNim = alternatif.get_alternatif_by_nim(nim)
        return DataAlternatifByNim
        # if not DataAlternatifByNim:
        #     raise NotFound("Data alternatif tidak ditemukan")
        # else:
        #     return DataAlternatifByNim

    @api.doc(responses={200: "OK", 404: "Not Found"})
    @api.expect(data_alternatif)
    def put(self, nim):
        try:
            status, message = alternatif.update_alternatif(
                nim, api.payload
            )
        except Exception as e:
            api.abort(404, e)
        else:
            if status:
                return message
            else:
                return message

    @api.doc(responses={200: "OK", 404: "Not Found"})
    def delete(self, nim):
        try:
            data = alternatif.delete_alternatif(nim)
            return jsonify(data)
        except Exception as e:
            api.abort(404, e)
