from ..models.alternatif_model import AlternatifDoc
from ..models.kriteria_model import KriteriaDoc, SubkriteriaDoc


class msaw:
    def __init__(self):
        self.bobot = []
        self.perbaikan_bobot = []
        self.nilai_konversi = []
        self.max_number_list = []
        self.normalisasi_data = []
        self.vector = []
        self.jumlah = []
        self.preverensi = []

    def extract_nilai(self):
        data_alternatif = AlternatifDoc.objects().all()
        for data in range(0, len(data_alternatif)):
            self.nilai_konversi.append([])
            for id in range(len(data_alternatif[data].subkriteria_id)):
                nilai = SubkriteriaDoc.objects(
                    _id=data_alternatif[data].subkriteria_id[id]
                ).first()
                self.nilai_konversi[data].append(nilai.nilai)

    def extract_bobot(self):
        data_bobot = KriteriaDoc.objects().only("bobot").all()
        bobot = []
        for t in data_bobot:
            bobot.append(t.bobot)
        total_bobot = sum(bobot)
        for i in range(len(bobot)):
            self.perbaikan_bobot.append(bobot[i] / total_bobot)

    def normalisasi(self):
        for i in range(5):
            max_number = max([item[i] for item in self.nilai_konversi])
            self.max_number_list.append(max_number)
        for data in range(0, len(self.nilai_konversi)):
            self.normalisasi_data.append([])
            for id in range(len(self.nilai_konversi[data])):
                hasil_normalisasi = (
                    self.nilai_konversi[data][id]
                    / self.max_number_list[id]
                )
                self.normalisasi_data[data].append(
                    round(hasil_normalisasi, 10)
                )

    def calculate_vector(self):
        for data in range(0, len(self.normalisasi_data)):
            self.vector.append([])
            for id in range(len(self.normalisasi_data[data])):
                hasil_vector = (
                    self.normalisasi_data[data][id]
                    ** self.perbaikan_bobot[id]
                )
                self.vector[data].append(round(hasil_vector, 10))

    def main(self):
        self.extract_nilai()
        self.extract_bobot()
        self.normalisasi()
        self.calculate_vector()
        print(self.normalisasi_data)
