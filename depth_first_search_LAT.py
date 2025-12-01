#awal = A
#tujuan = F
#jalur
#lihat contoh graf1 di catatan 1 okt

peta1 =  {'A':set(['B','C','D']),
         'B':set(['A']),
         'C':set(['A','E']),
         'D':set(['A','F']),
         'E':set(['C','F']),
         'F':set(['E','D']),
         'G':set(['F','H']),
         'H':set(['G','D'])}

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:     
        # masukkan antrian paling depan ke variabel jalur
        jalur = queue.pop(-1)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                queue.append(jalur_baru) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)

        #cek isi antrian
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")

print(bfs(peta1,'A','F'))
