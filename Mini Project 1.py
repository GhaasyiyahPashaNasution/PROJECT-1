alumni_pr2 = []

def input_data():
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")
    universitas = input("Masukkan Universitas yang Sedang Dijalani: ")
    jalur_masuk = input("Masukkan Jalur Masuk: ")
    no_telepon = input("Masukkan No Telepon: ")
    
    
    alumni = {
        "nama" : nama,
        "kelas" : kelas,
        "universitas" : universitas,
        "jalur masuk" : jalur_masuk,
        "telepon" : no_telepon
    }
    alumni_pr2.append(alumni)
    print("Data Berhasil Ditambahkan! ")
    print()
    
    
    
def tampil_data():
    if not alumni_pr2:
        print("Data Belum Terdaftar")
    else:
        for alumni in alumni_pr2:
            (f"Nama: {alumni['nama']}, Kelas: {alumni['kelas']}, Universitas: {alumni['universitas']}, "
                  f"{alumni['jalur masuk']}, {alumni['telepon']}")
    print()
            
            
            
def mencari_data ():
    keyword = input("Masukkan Nama/No Telepon/Universitas: ").lower()
    found = False
    for alumni in alumni_pr2:
        if (keyword in alumni['nama'].lower() or
            keyword in alumni['telepon'].lower() or
            keyword in alumni['universitas']):
                print(f"Nama: {alumni['nama']}, Kelas: {alumni['kelas']}, Universitas: {alumni['universitas']}, "
                  f"{alumni['jalur masuk']}, {alumni['telepon']}")
                found = True
    if not found:
        print("Data Tidak Ditemukan!")
    print()
    
    
def mengubah_data():
    nama = input("Masukkan Nama yang Ingin Diubah: ")
    for alumni in alumni_pr2:
        if alumni ['nama'] == nama:
            print("Masukkan data baru (kosongkan jika tidak ingin mengubah):")
            alumni['nama'] = input(f"Nama ({alumni['nama']}): ") or alumni['nama']
            alumni['kelas'] = input(f"Kelas ({alumni['kelas']}): ") or alumni['kelas']
            alumni['universitas'] = input(f"Universitas ({alumni['universitas']}): ") or alumni['univeritas']
            alumni['jalur_masuk'] = input(f"Jalur Masuk ({alumni['jalur masuk']}): ") or alumni['jalur masuk']
            alumni['telepon'] = input(f"No Telepon ({alumni['telepin']}): ") or alumni['Telepon']
            print("✅ Data berhasil diubah!\n")
            return
    print(" Data dengan Nama tersebut tidak ditemukan.\n")
    print()
    
    
def menghapus_data():
    nama = input("Masukkan Nama yang Ingin Diapus: ")
    for alumni in alumni_pr2:
        if alumni ['nama'] == nama:
            alumni_pr2.remove(alumni)
            print("Data Berhasil Dihapus!\n ")
            return
    print("Data Tidak Ditemukkan! \n")
    
    
    
def main():
    while True:
        print("====PDDKTI VERSI ANAK ALUMNI SMAS PR 2====")
        print("1. Input Data Alumni")
        print("2. Menampilkan Data Alumni")
        print("3. Mencari Data")
        print("4. Mengubah Data")
        print("5. Menghapus Data")
        print("6. Keluar Dari APP")
        pilihan = input("Menu yang Ingin Dipilih: ")
        
        if pilihan == "1":
            input_data()
        elif pilihan == "2":
            tampil_data()
        elif pilihan == "3":
            mencari_data()
        elif pilihan == "4":
            mengubah_data()
        elif pilihan == "5":
            mengubah_data()
        elif pilihan == "6":
            print("Keluar Dari APP")
            break
        else:
            print("Pilihan Tidak Ada di Opsi! \n")
            
           
            
    
            
if " __ main__":
    main()
        
            
            
        
            
    
    
    
    

            
            
            
            
            
    
            
            
                  














    
    

    
























    
    






    

    
    
    
    
    

    






    











        
    
    