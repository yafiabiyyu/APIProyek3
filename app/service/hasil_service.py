from ..metode.metode_service import MSaw, DataMetode, Saw


class HasilService:
    def __init__(self):
        self.msaw = MSaw()
        self.data_metode = DataMetode()
        self.saw = Saw()

    def get_konversi(self):
        data_konversi = []
        (
            nim_alternatif,
            nama_alternatif,
            data_nilai,
        ) = self.data_metode.ambil_data()
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

    def get_normalisasi(self):
        data_all_normalisasi = []
        nim_data, nama_data, _ = self.data_metode.ambil_data()
        data_normalisasi = self.data_metode.normalisasi_data()
        for datas in range(0, len(nim_data)):
            dict_normalisasi = {
                "_id": nim_data[datas],
                "nama_mahasiswa": nama_data[datas],
                "k1": data_normalisasi[datas][0],
                "k2": data_normalisasi[datas][1],
                "k3": data_normalisasi[datas][2],
                "k4": data_normalisasi[datas][3],
                "k5": data_normalisasi[datas][4],
            }
            data_all_normalisasi.append(dict_normalisasi)
        return data_all_normalisasi

    def get_hasil_msaw(self):
        hasil_msaw_list = []
        rank, hasil = self.msaw.jumlah_and_rank()
        nim_data, nama_data, _ = self.data_metode.ambil_data()
        for data in range(0, len(nim_data)):
            dict_hasil = {
                "_id": nim_data[data],
                "nama_mahasiswa": nama_data[data],
                "nilai": hasil[data],
                "rank": rank[data],
            }
            hasil_msaw_list.append(dict_hasil)
        return hasil_msaw_list

    def get_hasil_saw(self):
        hasil_saw_list = []
        rank, hasil = self.saw.jumlah_and_rank_saw()
        nim_data, nama_data, _ = self.data_metode.ambil_data()
        for data in range(0, len(nim_data)):
            dict_hasil = {
                "_id": nim_data[data],
                "nama_mahasiswa": nama_data[data],
                "nilai": hasil[data],
                "rank": rank[data],
            }
            hasil_saw_list.append(dict_hasil)
        return hasil_saw_list
