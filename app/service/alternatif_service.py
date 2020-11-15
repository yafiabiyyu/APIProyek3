from ..models.alternatif_model import AlternatifDoc

class AlternatifService:
    def add_alternatif(self, data):
        check_alternatif = AlternatifDoc.objects(_id=data['_id']).first()
        if check_alternatif is not None:
            message_object={
                "status":"gagal",
                "message":"Data alternatif telah terdaftar"
            }
            return message_object
        else:
            try:
                save_alternatif = AlternatifDoc(
                    _id = data['_id'],
                    nama_mahasiswa = data['nama_mahasiswa'],
                    alamat = data['alamat'],
                    jenis_kelamin = data['jenis_kelamin'],
                    subkriteria_id = data['subkriteria_id']
                ).save()
                message_object={
                    "status":"berhasil",
                    "message":"Data alternatif telah tersimpan"
                }
                return message_object
            except Exception as e:
                message_object={
                    "status":"gagal",
                    "message":e
                }
                return message_object
    def get_all_data(self):
        try:
            data = list(AlternatifDoc.objects().all())
            print(data)
            return data
        except Exception as e:
            message_object = {"status": "gagal", "message": e}
            return message_object
    def get_alternatif_by_nim(self, nim):
        data = AlternatifDoc.objects(_id=nim).first()
        if data is None:
            message_object = {
                'status':'gagal',
                'message':'Alternatif dengan nim {} tidak ditemukan'.format(nim)
            }
            return message_object
        else:
            return data