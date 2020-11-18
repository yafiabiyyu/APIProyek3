from ..models.alternatif_model import AlternatifDoc
from ..models.kriteria_model import KriteriaDoc, SubkriteriaDoc


class Seleksi:
    def extract_data_alternatif(self):
        nama_alternatif = []
        nim_alternatif = []
        subkriteria_list = []
        data_alternatif = AlternatifDoc.objects().all()
        for data in range(0, len(data_alternatif)):
            subkriteria_list.append([])
            nim_alternatif.append(data_alternatif[data]._id)
            nama_alternatif.append(data_alternatif[data].nama_mahasiswa)
            for id in range(len(data_alternatif[data].subkriteria_id)):
                nama_subkriteria = SubkriteriaDoc.objects(
                    _id=data_alternatif[data].subkriteria_id[id]
                ).first()
                subkriteria_list[data].append(
                    nama_subkriteria.nama_subkriteria
                )
        return nama_alternatif, nim_alternatif, subkriteria_list

    def seleksi(self):
        data_seleksi = []
        (
            list_nama,
            list_nim,
            list_subkriteria,
        ) = self.extract_data_alternatif()
        for data in range(0, len(list_nama)):
            dict_data = {
                "_id": list_nim[data],
                "nama_mahasiswa": list_nama[data],
                "pendapatan_ortu": list_subkriteria[data][0],
                "tanggungan_ortu": list_subkriteria[data][1],
                "status_ortu": list_subkriteria[data][2],
                "semester": list_subkriteria[data][3],
                "ipk": list_subkriteria[data][4],
            }
            data_seleksi.append(dict_data)
        return data_seleksi
