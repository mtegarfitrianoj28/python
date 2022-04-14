class queue:
    def __init__(self):
        n = int (input("Masukkan size queue yang diinginkan:"))
        print("Sebuah queue Berkapasitas",n,"telah di buat")
        self.size = n
        self.current_size = 0
        self.data = [None] *n
        self.front = None
        self.back = None

    def isempty(self):
        if self.current_size == 0:
            return True
        else:
            return False
    
    def isfull(self):
        if self.current_size == self.size:
            return True
        else:
            return False

    def enqueue(self,newdata):
        if self.isfull():
            print("Maaf queue sudah penuh ",newdata,"tidak dapat dimasukan")
        else:
            if self.back is not None:
                self.back = (self.back + 1) % self.size
            else:
                self.front = 0
                self.back = 0

            self.data[self.back] = newdata
            self.current_size = self.current_size + 1
            print(newdata,"telah dimasukan kedalam queue")

    def dequeue(self):
        if self.isempty():
            print("Maaf Queue kosong, tidak ada data yang dapat di-dequeue")
            return None
        else:
            datakeluar = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front + 1) % self.size
            self.current_size = self.current_size - 1
            print(datakeluar,"telah dikeluarkan dari Queue")
            return datakeluar

    def printinfo(self):
        print("\n===============================================")
        print("INFO TENTANG QUEUE")
        print("Kapasitas queue:",self.size)
        print("Banyak isi queue saat ini:",self.current_size)
        #jika queue sedang kosong
        if self.isempty():
            print("Data posisi terdepan:-")
            print("Data pada posisi paling belakang= -")
        else:
            print("Data pada posisi terdepan:",self.data[self.front])
            print("Data posisi paling belakang:",self.data[self.back])
        print("isi list data:",self.data)
        print("================================================")

    def visualisasiqueue(self):
        print("\nVisualisasi Queue\n")
        for i in range(self.size):
            print("    [%2d]     "%(self.size-1),end="")
        print()

        for i in range(self.size):
            print("===============",end="")
        property()

        jumlahposisikosong = self.size = self.current_size
        for i in range(self.size):
            if i < jumlahposisikosong:
                print("  %10s  "%(""),end="")
            else:
                print("   %10s   "%(self.data[self.front-1-i]),end="")

        print(">> [Depan]",end="")
        print()
        for i in range(self.size):
            print("===================",end="")
        print("")

    def menu(self):
        import os
        os.system("CLS")
        print("Menu Atrian Rumah Sakit")
        print("====================================================================")
        print("1. Menambah Daftar Antrean")
        print("2. Cek Data Antrean")
        print("3. Hapus Data Antrean")
        print("4. Keluar Dari Program")
        print("=====================================================================")
        menu = int(input("Masukkan No Menu Yang Dipilih = "))
        if menu == 1:
            inputan = int(input("Masukkan Jumlah pasien = "))
            for i in range(inputan):
                nama = input("Masukan nama pasien ke % i =" % (i+1))
                self.enqueue(nama)
            self.visualisasiqueue()
            input("Tekan Enter untuk Kembali ke menu...")
            self.menu()

        elif menu == 2:
            self.printinfo()
            self.visualisasiqueue()
            input("Tekan Enter Untuk kembali ke menu ...")
            self.menu()
        
        elif menu ==3:
            self.dequeue()
            self.visualisasiqueue()
            input("Tekan Enter Untuk kembali ke menu...")
            self.menu()
        
        elif menu == 4:
            print("Anda akan keluar dari program")
            input("Tekan Enter untuk keluar dari program...")

        else:
            print("Keyboard anda salah, Mohon ulangi kembali")

#.............................................................
Q = queue()
Q.menu()

