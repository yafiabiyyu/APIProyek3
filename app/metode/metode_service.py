from ..models.alternatif_model import AlternatifDoc
from ..models.kriteria_model import KriteriaDoc, SubkriteriaDoc
import scipy.stats as ss


class DataMetode:
    def ambil_data(self):
        nama_alternatif = []
        nim_alternatif = []
        data_nilai = []
        # ambil data alternatif
        get_alternatif_data = AlternatifDoc.objects().all()
        for data in range(0, len(get_alternatif_data)):
            data_nilai.append([])
            nim_alternatif.append(get_alternatif_data[data]._id)
            nama_alternatif.append(
                get_alternatif_data[data].nama_mahasiswa
            )
            for id in range(
                len(get_alternatif_data[data].subkriteria_id)
            ):
                nilai = SubkriteriaDoc.objects(
                    _id=get_alternatif_data[data].subkriteria_id[id]
                ).first()
                data_nilai[data].append(nilai.nilai)
        return nim_alternatif, nama_alternatif, data_nilai

    def perbaikan_data_bobot(self):
        data_bobot = KriteriaDoc.objects().only("bobot").all()
        perbaikan_bobot = []
        bobot = []
        for t in data_bobot:
            bobot.append(t.bobot)
        total_bobot = sum(bobot)
        for i in range(len(bobot)):
            perbaikan_bobot.append(bobot[i] / total_bobot)
        return perbaikan_bobot

    def konversi(self):
        data_konversi = []
        nim_alternatif, nama_alternatif, data_nilai = self.ambil_data()
        for data in range(0, len(nim_alternatif)):
            dict_konversi = {
                "_id": nim_alternatif[data],
                "nama_mahasiswa": nama_alternatif[data],
                "k1": data_nilai[data][0],
                "k2": data_nilai[data][1],
                "k3": data_nilai[data][2],
                "k4": data_nilai[data][3],
                "k5": data_nilai[data][4],
            }
            data_konversi.append(dict_konversi)
        return data_konversi

    def normalisasi_data(self):
        nim_data, nama_data, nilai_data = self.ambil_data()
        max_number = []
        data_normalisasi = []
        for i in range(5):
            get_max = max([item[i] for item in nilai_data])
            max_number.append(get_max)
        for data in range(0, len(nilai_data)):
            data_normalisasi.append([])
            for id in range(len(nilai_data[data])):
                hasil = nilai_data[data][id] / max_number[id]
                data_normalisasi[data].append(round(hasil, 10))
        return data_normalisasi


class MSaw:
    def __init__(self):
        self.data_metode = DataMetode()

    def vector_data(self):
        bobot = self.data_metode.perbaikan_data_bobot()
        normalisasi_data = self.data_metode.normalisasi_data()
        vector_data_list = []
        for data in range(0, len(normalisasi_data)):
            vector_data_list.append([])
            for id in range(len(normalisasi_data[data])):
                hasil_vector = normalisasi_data[data][id] ** bobot[id]
                vector_data_list[data].append(round(hasil_vector, 10))
        return vector_data_list

    def jumlah_and_rank(self):
        data_vector = self.vector_data()
        jumlah = []
        hasil = []
        result = 1
        for data in range(0, len(data_vector)):
            for id in range(len(data_vector[data])):
                result = result * data_vector[data][id]
            jumlah.append(round(result, 10))
            result = 1
        for i in range(0, len(jumlah)):
            hasil_itung = jumlah[i] / sum(jumlah)
            hasil.append(round(hasil_itung, 10))
        rank = ss.rankdata([-1 * i for i in hasil]).astype(int).tolist()
        print(type(rank))
        return rank, hasil


class Saw:
    def __init__(self):
        self.data_metode = DataMetode()

    def jumlah_and_rank_saw(self):
        bobot = self.data_metode.perbaikan_data_bobot()
        data_normalisasi = self.data_metode.normalisasi_data()
        hasil_saw_list = []
        result = 0
        for data in range(0, len(data_normalisasi)):
            for id in range(0, len(data_normalisasi[data])):
                result = (
                    data_normalisasi[data][id] * bobot[id]
                ) + result
            hasil_saw_list.append(round(result, 10))
            result = 0
        rank = (
            ss.rankdata([-1 * i for i in hasil_saw_list])
            .astype(int)
            .tolist()
        )
        return rank, hasil_saw_list
