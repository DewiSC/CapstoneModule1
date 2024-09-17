from tabulate import tabulate

def MenuUtama():
    while True:
        try:
            print("===========REGISTRASI RUMAH SAKIT===========")
            print("1. Emergency")
            print("2. Inpatient")
            print("3. Outpatient")
            print("4. Keluar")
            print("="*45)

            pilih = int(input("Masukkan pilihan (1-4) : "))
            if pilih == 1:
                Emergency()
                break
            elif pilih == 2:
                Inpatient()
                break
            elif pilih == 3:
                Outpatient()
                break
            elif pilih == 4:
                print("Keluar dari program. Terima kasih!")
                exit()
            else:
                print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
        except ValueError:
            print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
def Emergency():
    global dataPasien_EM
    global dataPasienUtama
    while True:
        try:
            print("===========EMERGENCY===========")
            print("1. Data Pasien")
            print("2. Input Data Pasien")
            print("3. Edit Data Pasien")
            print("4. Hapus Data Pasien")
            print("5. Kembali ke Menu Utama")
            print("="*31)

            pilihEM = int(input("Masukkan pilihan (1-5) : "))
            if pilihEM == 1:
                MenuDataPasien("EM")
                break
            elif pilihEM == 2:
                menuInputData("EM")
                break
            elif pilihEM == 3:
                MenuEditDataPasien("EM")
                break
            elif pilihEM == 4:
                MenuHapusDataPasien("EM")
                break
            elif pilihEM == 5:
                MenuUtama()
                break
            else:
                print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
        except ValueError:
            print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
def Inpatient():
    global dataPasien_IP
    global dataPasienUtama
    while True:
        try:
            print("===========INPATIENT===========")
            print("1. Data Pasien")
            print("2. Input Data Pasien")
            print("3. Edit Data Pasien")
            print("4. Hapus Data Pasien")
            print("5. Kembali ke Menu Utama")
            print("="*31)

            pilihIP = int(input("Masukkan pilihan (1-5) : "))
            if pilihIP == 1:
                MenuDataPasien("IP")
                break
            elif pilihIP == 2:                
                menuInputData("IP")
                break
            elif pilihIP == 3:
                MenuEditDataPasien("IP")
                break
            elif pilihIP == 4:
                MenuHapusDataPasien("IP")
                break
            elif pilihIP == 5:
                MenuUtama()
                break
            else:
                print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
        except ValueError:
            print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
def Outpatient():
    global dataPasien_OP
    global dataPasienUtama
    while True:
        try:
            print("===========OUTPATIENT===========")
            print("1. Data Pasien")
            print("2. Input Data Pasien")
            print("3. Edit Data Pasien")
            print("4. Hapus Data Pasien")
            print("5. Kembali ke Menu Utama")
            print("="*32)

            pilihOP = int(input("Masukkan pilihan (1-5) : "))
            if pilihOP == 1:
                MenuDataPasien("OP")
                break
            elif pilihOP == 2:                
                menuInputData("OP")
                break
            elif pilihOP == 3:
                MenuEditDataPasien("OP")
                break
            elif pilihOP == 4:
                MenuHapusDataPasien("OP")
                break
            elif pilihOP == 5:
                MenuUtama()
                break
            else:
                print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
        except ValueError:
            print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
def noMedisAkhir(data_pasien):
    if data_pasien:
        angkaAkhir = max(data_pasien.keys(), key=lambda k: int(k[1:]))
        return int(angkaAkhir[1:])
    return 0
def noMedisOtomatis(data_pasien):
    final_nomedis = noMedisAkhir(data_pasien)
    return f"P{final_nomedis + 1:04}"
def noRegAkhir(data_pasien):
    if data_pasien:
        angkaAkhir = [int(v['Noreg'].split('-')[1]) for v in data_pasien.values() if v['Noreg'].startswith('EM-') or v['Noreg'].startswith('IP-') or v['Noreg'].startswith('OP-')]
        if angkaAkhir:
            return max(angkaAkhir)
    return 0
def noRegOtomatis(tipe):    
    if tipe == "EM":
        final_nomedis = noRegAkhir(dataPasien_EM)
        return f"EM-{final_nomedis + 1:04}"
    elif tipe == "IP":
        final_nomedis = noRegAkhir(dataPasien_IP)
        return f"IP-{final_nomedis + 1:04}"
    elif tipe == "OP":
        final_nomedis = noRegAkhir(dataPasien_OP)
        return f"OP-{final_nomedis + 1:04}"
    else:
        return 0
def validasitglLahir(tgl):
    if tgl.count("/") != 2:
        return "Format salah!! Formatnya harus DD/MM/YYYY"
    jumlah_angka = ''
    for char in tgl:
        if not (char.isdigit() or char == "/"):
            return "Format salah!! Formatnya harus DD/MM/YYYY dan harus Angka."
        elif char.isdigit():
            jumlah_angka += char
    if len(jumlah_angka) > 8:
        return "Format salah!! Angka tidak boleh lebih dari 8."
    
    D, M, Y = tgl.split("/")
    if len(D) != 2:
        return "Format salah!! Formatnya harus DD/MM/YYYY"
    elif len(M) != 2:
        return "Format salah!! Formatnya harus DD/MM/YYYY"
    elif len(Y) != 4:
        return "Format salah!! Formatnya harus DD/MM/YYYY"
    elif int(D) > 31:
        return "Format salah!! Hari tidak bisa lebih dari 31 Hari."
    elif int(M) > 12:
        return "Format salah!! Bulan tidak bisa lebih dari 12 Bulan."
    elif int(M) == 2:
        if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
            if int(D) > 29:
                return "Format salah!! Bulan Februari pada tahun kabisat tidak bisa lebih dari 29."
        else:
            if int(D) > 28:
                return "Format salah!! Bulan Februari tidak bisa lebih dari 28."
    else:
        return
def validasiNoRegis(tipe,noreg):
    if noreg.count("-") != 1:
        return "Format salah!! Formatnya harus XX-XXXX"
    tipe1, angka = noreg.split("-")
    if len(tipe) != 2:
        return "Format salah!! Formatnya harus XX-XXXX"
    elif len(angka) != 4:
        return "Format salah!! Formatnya harus XX-XXXX"
    elif tipe1 not in ["EM","IP","OP"]:
        return "Format salah!! XX sebelum tanda(-) hanya bisa EM, IP atau OP"
    elif not angka.isdigit():
        return "Format salah!! XXXX setelah tanda(-) hanya bisa Angka"
    elif tipe != tipe1:
        return f"{noreg} bukan data pasien {tipe}"
    else:
        return
def cariNoreg(noreg):   
    for key, pasien in dataPasien_EM.items():
        if pasien["Noreg"] == noreg:
            return "EM", pasien, key
  
    for key, pasien in dataPasien_IP.items():
        if pasien["Noreg"] == noreg:
            return "IP", pasien, key
   
    for key, pasien in dataPasien_OP.items():
        if pasien["Noreg"] == noreg:
            return "OP", pasien, key
    
    return None, None
def RuanganIP(): 
    try:   
        print("===========PILIH RUANGAN===========")
        print("1. Ruang Anggrek")
        print("2. Ruang Edelweis")
        print("3. Ruang Kamboja")
        print("4. Ruang Matahari")
        print("5. Kembali Ke Menu Sebelumnya")
        print("="*35)    
        pilihRuang = int(input("Pilih Ruangan (1-4) / Kembali (5) : "))
        if pilihRuang == 1:
            return "Ruang Anggrek"
        elif pilihRuang == 2:
            return "Ruang Edelweis"
        elif pilihRuang == 3:
            return "Ruang Kamboja"
        elif pilihRuang == 4:
            return "Ruang Matahari"
        elif pilihRuang == 5:
            Inpatient()
        else:
            print("Pilihan tidak ada!! silahkan pilih lagi.")
            return RuanganIP()
    except ValueError:
        print("Pilihan tidak valid!")
def PoliOP():
    try:
        print("===========PILIH POLI===========")
        print("1. Poli Gigi")
        print("2. Poli Jantung")
        print("3. Poli Mata")
        print("4. Poli Umum")
        print("5. Kembali Ke Menu Sebelumnya")    
        print("="*32)
        pilihPoli = int(input("Pilih Poli (1-4) / Kembali (5) : "))
        if pilihPoli == 1:
            return "Poli Gigi"
        elif pilihPoli == 2:
            return "Poli Jantung"
        elif pilihPoli == 3:
            return "Poli Mata"
        elif pilihPoli == 4:
            return "Poli Umum"
        elif pilihPoli == 5:
            Outpatient()
        else:
            print("Pilihan tidak ada!! silahkan pilih lagi.")
            return PoliOP()
    except ValueError:
        print("Pilihan tidak valid!")
def MenuDataPasien(tipe):
    while True:
        try:           
            if tipe == "EM":
                print("===========DATA PASIEN EMERGENCY===========")
            elif tipe == "IP":
                print("===========DATA PASIEN INPATIENT===========")
            elif tipe == "OP":
                print("===========DATA PASIEN OUTPATIENT===========")
            print("1. Seluruh Data Pasien")
            print("2. Data Pasien Berdasarkan Nomor Rekam Medis")
            print("3. Kembali ke menu sebelumnya")
            print("="*44)

            pilihDp = int(input("Masukkan pilihan (1-3) : "))
            if pilihDp == 1:
                DataPasien(tipe,pilihDp)
                break
            elif pilihDp == 2:
                DataPasien(tipe,pilihDp)
                break
            elif pilihDp == 3:
                if tipe == "EM":
                    Emergency()
                    break
                elif tipe == "IP":
                    Inpatient()
                    break
                elif tipe == "OP":
                    Outpatient()
                    break
                else:
                    print("Tipe tidak sesuai")
            else:
                print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
        except ValueError:
            print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")  
def DataPasien(tipe, pilihanDp):
    while True:
        try:
            while True:
                print("="*50)
                if pilihanDp == 1:
                    if tipe == "EM":
                        print(tabulate([[key] + list(value.values()) for key, value in dataPasien_EM.items()], 
                            headers=["NoMedis", "NoReg", "Nama", "Jenis Kelamin", "Tanggal Lahir", "Alamat"], 
                            tablefmt="pipe"))
                        break
                    elif tipe == "IP":
                        print(tabulate([[key] + list(value.values()) for key, value in dataPasien_IP.items()], 
                            headers=["NoMedis", "NoReg", "Nama", "Jenis Kelamin", "Tanggal Lahir", "Alamat","Ruangan"], 
                            tablefmt="pipe"))
                        break
                    elif tipe == "OP":
                        print(tabulate([[key] + list(value.values()) for key, value in dataPasien_OP.items()], 
                            headers=["NoMedis", "NoReg", "Nama", "Jenis Kelamin", "Tanggal Lahir", "Alamat","Poli"], 
                            tablefmt="pipe"))
                        break
                    else:
                        print("tipe tidak ada")
                        break
                elif pilihanDp ==2:
                    inputNoMedis = input("Masukkan Nomor Rekam Medis : ").upper()
                    if len(inputNoMedis) == 5 and inputNoMedis[0] == 'P' and inputNoMedis[1:].isdigit():
                        if tipe == "EM" and (inputNoMedis in dataPasien_EM):
                            pasien = dataPasien_EM[inputNoMedis]
                            tampilData = [[inputNoMedis, pasien["Noreg"], pasien["Nama"], pasien["Jenis Kelamin"], pasien["Tanggal Lahir"], pasien["Alamat"]]]
                            print(tabulate(tampilData, headers=["NoMedis", "NoReg", "Nama", "Jenis Kelamin", "Tanggal Lahir", "Alamat"], tablefmt="pipe"))
                            break
                        elif tipe == "IP" and (inputNoMedis in dataPasien_IP):
                            pasien = dataPasien_IP[inputNoMedis]
                            tampilData = [[inputNoMedis, pasien["Noreg"], pasien["Nama"], pasien["Jenis Kelamin"], pasien["Tanggal Lahir"], pasien["Alamat"], pasien["Ruangan"]]]
                            print(tabulate(tampilData, headers=["NoMedis", "NoReg", "Nama", "Jenis Kelamin", "Tanggal Lahir", "Alamat", "Ruangan"], tablefmt="pipe"))
                            break
                        elif tipe == "OP" and (inputNoMedis in dataPasien_OP):
                            pasien = dataPasien_OP[inputNoMedis]
                            tampilData = [[inputNoMedis, pasien["Noreg"], pasien["Nama"], pasien["Jenis Kelamin"], pasien["Tanggal Lahir"], pasien["Alamat"], pasien["Poli"]]]
                            print(tabulate(tampilData, headers=["NoMedis", "NoReg", "Nama", "Jenis Kelamin", "Tanggal Lahir", "Alamat", "Poli"], tablefmt="pipe"))
                            break
                        else:
                            print("No Rekam Medis belum ada, silahkan registrasi.")
                            break
                    else:
                        print("Format Nomor Rekam Medis Salah! Silahkan masukkan kembali Nomor Rekam Medis.")
                        break

                else:
                    print("Tidak ada pilihan")
                    break
            
            while True:
                print("="*50)
                pilDp = input("Apakah ingin kembali ke menu sebelumnya?(y/n) : ").upper()
                if pilDp == "Y":
                    MenuDataPasien(tipe)
                    break
                elif pilDp == "N":
                    print("Keluar dari program. Terima kasih!")
                    exit()
                else:
                    print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
                    continue                    

        except ValueError:
            print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
def menuInputData(tipe):
    while True:
        try:
            print("===========REGISTRASI===========")
            print("1. Pasien Lama")
            print("2. Pasien Baru")
            print("3. Kembali Ke Menu Sebelumnya")
            print("="*32)
            reg = int(input("Masukkan pilihan (1-3) : "))
            if reg == 1:
                nomedis = input("Masukkan Nomor Rekam Medis : ").upper()
                if nomedis in dataPasienUtama:
                    if tipe == "EM":
                        inputDataPasien(tipe,None,nomedis)
                        break
                    elif tipe == "IP":
                        ruanganIP = RuanganIP()
                        inputDataPasien(tipe,ruanganIP,nomedis)
                        break
                    elif tipe == "OP":
                        poliOP = PoliOP()
                        inputDataPasien(tipe,poliOP,nomedis)
                        break
                else:
                    print("Nomor Rekam Medis tidak terdaftar. Silahkan registrasi pasien baru.")
            elif reg == 2:
                if tipe == "EM":
                    InputDataPasienBaru(tipe,None)
                    break
                elif tipe == "IP":
                    ruanganIP = RuanganIP()
                    InputDataPasienBaru(tipe,ruanganIP)
                    break
                elif tipe == "OP":
                    poliOP = PoliOP()
                    InputDataPasienBaru(tipe,poliOP)
                    break
            elif reg == 3:
                if tipe == "EM":
                    Emergency()
                    break
                elif tipe == "IP":
                    Inpatient()
                    break
                elif tipe == "OP":
                    Outpatient()
                    break
            else:
                print("Pilihan tidak ada! Silahkan input lagi!")
        except ValueError:
            print("Pilihan tidak ada! Silahkan input lagi!")
def inputDataPasien(tipe,Ruang_atau_Poli,nomedis):
    while True:
        try:    
            if nomedis in dataPasienUtama:
                data = dataPasienUtama[nomedis]
                print("===========DATA PASIEN===========")
                print(f"Nomor Rekam Medis : {nomedis}")
                print(f"Nama : {data["Nama"]}")
                print(f"Jenis Kelamin : {data["Jenis Kelamin"]}")
                print(f"Tanggal Lahir : {data["Tanggal Lahir"]}")
                print(f"Alamat : {data["Alamat"]}")
                print("="*33)
                                        
                noReg = noRegOtomatis(tipe)                    
                if tipe == "IP" or tipe == "OP":
                    ruangAtauPoli = Ruang_atau_Poli
                while True:
                    lanjut = input("Apakah akan melanjutkan registrasi dengan data di atas? (y/n) : ").upper()
                    if lanjut == "Y":                    
                        print("="*44)
                        if tipe == "EM":
                            print(f"Nomor Rekam Medis : {nomedis}\nNomor Registrasi : {noReg}\nNama : {data['Nama']}\nJenis Kelamin : {data['Jenis Kelamin']}\nTanggal Lahir : {data['Tanggal Lahir']}\nAlamat : {data['Alamat']}")
                        elif tipe == "IP":
                            print(f"Nomor Rekam Medis : {nomedis}\nNomor Registrasi : {noReg}\nNama : {data['Nama']}\nJenis Kelamin : {data['Jenis Kelamin']}\nTanggal Lahir : {data['Tanggal Lahir']}\nAlamat : {data['Alamat']}\nRuangan : {ruangAtauPoli}")
                        elif tipe == "OP":
                            print(f"Nomor Rekam Medis : {nomedis}\nNomor Registrasi : {noReg}\nNama : {data['Nama']}\nJenis Kelamin : {data['Jenis Kelamin']}\nTanggal Lahir : {data['Tanggal Lahir']}\nAlamat : {data['Alamat']}\nPoli : {ruangAtauPoli}")                            
                        simpan = input("Apakah data tersebut akan disimpan? (y/n) : ").upper()
                        if simpan == "Y":                    
                            if tipe == "EM":                        
                                data_baru = {
                                            "Noreg": noReg,
                                            "Nama": data["Nama"],
                                            "Jenis Kelamin": data["Jenis Kelamin"],
                                            "Tanggal Lahir": data["Tanggal Lahir"],
                                            "Alamat": data["Alamat"]
                                            }                                
                                dataPasien_EM[nomedis] = data_baru                        
                            elif tipe == "IP":
                                data_baru = {
                                            "Noreg": noReg,
                                            "Nama": data["Nama"],
                                            "Jenis Kelamin": data["Jenis Kelamin"],
                                            "Tanggal Lahir": data["Tanggal Lahir"],
                                            "Alamat": data['Alamat'],
                                            "Ruangan": ruangAtauPoli
                                            }
                                dataPasien_IP[nomedis] = data_baru      
                            elif tipe == "OP":
                                data_baru = {
                                            "Noreg": noReg,
                                            "Nama": data["Nama"],
                                            "Jenis Kelamin": data["Jenis Kelamin"],
                                            "Tanggal Lahir": data["Tanggal Lahir"],
                                            "Alamat": data["Alamat"],
                                            "Poli": ruangAtauPoli
                                            }
                                dataPasien_OP[nomedis] = data_baru
                            
                            print("Data Tersimpan.")                    
                            break
                        elif simpan == "N":
                            print("Data tidak jadi di simpan. Silahkan kembali ke menu sebelumnya.")
                            menuInputData(tipe)
                            break
                        else:
                            print("Pilihan tidak ada!! Silahkan masukkan lagi.")
                    elif lanjut == "N":
                        print("Pasien tidak jadi Registrasi. Silahkan kembali ke menu sebelumnya.")
                        menuInputData(tipe)
                        break
                    else:
                        print("Pilihan tidak ada! Silahkan input lagi!")
                        continue
                while True:
                    print("="*44)
                    pilDp = input("Apakah ingin kembali ke menu sebelumnya?(y/n) : ").upper()
                    if pilDp == "Y":
                        if tipe == "EM":
                            Emergency()
                            break
                        elif tipe == "IP":
                            Inpatient()
                            break
                        elif tipe == "OP":
                            Outpatient()
                            break                    
                    elif pilDp == "N":
                        print("Keluar dari program. Terima kasih!")
                        exit()
                    else:
                        print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
                        continue           
        except ValueError:
            print("Format salah! Silahkan input lagi!")
def InputDataPasienBaru(tipe, Ruang_atau_Poli):
    while True:
        try:    
            while True:       
                if tipe == "EM":
                    print("===========DATA PASIEN EMERGENCY===========")
                elif tipe == "IP":
                    print("===========DATA PASIEN INPATIENT===========")
                elif tipe == "OP":
                    print("===========DATA PASIEN OUTPATIENT===========")
                
                nomedis = noMedisOtomatis(dataPasienUtama)
                noReg = noRegOtomatis(tipe)
                Nama = input("Nama : ").capitalize()
                while True:
                    JK = input("Jenis Kelamin (L/P) : ").upper()
                    if JK == "L":
                        Jenis_Kelamin = "Laki-Laki"
                        break
                    elif JK == "P":
                        Jenis_Kelamin = "Perempuan"
                        break
                    else:
                        print("pilihan salah! masukkan lagi!")
                while True:               
                    Tgl = input("Tanggal Lahir (DD/MM/YYYY) : ")
                    validTgl = validasitglLahir(Tgl)
                    if validTgl is None:
                        Tanggal_Lahir = Tgl
                        break
                    else:
                        print(validTgl)
                Alamat = input("Alamat : ")
                if tipe == "IP" or tipe == "OP":
                    ruangAtauPoli = Ruang_atau_Poli
                
                print("="*44)
                if tipe == "EM":
                    print(f"Nomor Rekam Medis : {nomedis}\nNomor Registrasi : {noReg}\nNama : {Nama}\nJenis Kelamin : {Jenis_Kelamin}\nTanggal Lahir : {Tanggal_Lahir}\nAlamat : {Alamat}")
                elif tipe == "IP":
                    print(f"Nomor Rekam Medis : {nomedis}\nNomor Registrasi : {noReg}\nNama : {Nama}\nJenis Kelamin : {Jenis_Kelamin}\nTanggal Lahir : {Tanggal_Lahir}\nAlamat : {Alamat}\nRuangan : {ruangAtauPoli}")
                elif tipe == "OP":
                    print(f"Nomor Rekam Medis : {nomedis}\nNomor Registrasi : {noReg}\nNama : {Nama}\nJenis Kelamin : {Jenis_Kelamin}\nTanggal Lahir : {Tanggal_Lahir}\nAlamat : {Alamat}\nPoli : {ruangAtauPoli}")
                
                simpan = input("Apakah data tersebut akan disimpan? (y/n) : ").upper()
                if simpan == "Y":                    
                    if tipe == "EM":                        
                        data_baru = {
                                        "Noreg": noReg,
                                        "Nama": Nama,
                                        "Jenis Kelamin": Jenis_Kelamin,
                                        "Tanggal Lahir": Tanggal_Lahir,
                                        "Alamat": Alamat
                                    }
                        dataPasien_EM[nomedis] = data_baru                        
                    elif tipe == "IP":
                        data_baru = {
                                        "Noreg": noReg,
                                        "Nama": Nama,
                                        "Jenis Kelamin": Jenis_Kelamin,
                                        "Tanggal Lahir": Tanggal_Lahir,
                                        "Alamat": Alamat,
                                        "Ruangan": ruangAtauPoli
                                    }
                        dataPasien_IP[nomedis] = data_baru      
                    elif tipe == "OP":
                        data_baru = {
                                        "Noreg": noReg,
                                        "Nama": Nama,
                                        "Jenis Kelamin": Jenis_Kelamin,
                                        "Tanggal Lahir": Tanggal_Lahir,
                                        "Alamat": Alamat,
                                        "Poli": ruangAtauPoli
                                    }
                        dataPasien_OP[nomedis] = data_baru
                    data_baru = {
                                    "Nama": Nama,
                                    "Jenis Kelamin": Jenis_Kelamin,
                                    "Tanggal Lahir": Tanggal_Lahir,
                                    "Alamat": Alamat,
                                }
                    dataPasienUtama[nomedis] = data_baru
                    print("Data Tersimpan.")                    
                    break
                elif simpan == "N":
                    print("Data tidak jadi di simpan.")
                    if tipe == "EM":
                        Emergency()
                        break
                    elif tipe == "IP":
                        Inpatient()
                        break
                    elif tipe == "OP":
                        Outpatient()
                        break
                else:
                    print("Pilihan tidak ada!! Silahkan masukkan lagi.")

            while True:
                print("="*50)
                pilDp = input("Apakah ingin kembali ke menu sebelumnya?(y/n) : ").upper()
                if pilDp == "Y":
                    if tipe == "EM":
                        Emergency()
                        break
                    elif tipe == "IP":
                        Inpatient()
                        break
                    elif tipe == "OP":
                        Outpatient()
                        break                    
                elif pilDp == "N":
                    print("Keluar dari program. Terima kasih!")
                    exit()
                else:
                    print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
                    continue
        except ValueError:
            print("Format salah! Silahkan input lagi!")
def MenuEditDataPasien(tipe):
    while True:
        try:
            while True:
                print("===========EDIT DATA PASIEN===========")
                print("1. Edit Data Pasien Berdasarkan Nomor Rekam Medis")
                print("2. Edit Data Pasien Berdasarkan Nomor Registrasi")
                print("3. Kembali Ke Menu Sebelumnya")
                print("="*38)
                pilEdit = int(input("Masukkan pilihan (1-3) : "))
                if pilEdit == 1:
                    while True:
                        nomedis = input("Masukkan Nomor Rekam Medis : ").upper()
                        if nomedis in dataPasienUtama:
                            EditDataPasien(tipe,nomedis,None)
                            break
                        else:
                            print("Nomor Rekam Medis tidak terdaftar.")
                elif pilEdit == 2:
                    while True:
                        noreg = input("Masukkan Nomor Registrasi : ").upper()
                        validnoreg = validasiNoRegis(tipe,noreg)
                        if validnoreg == None:    
                            tipe, dataValid, nomedis = cariNoreg(noreg)                            
                            if dataValid:
                                EditDataPasien(tipe,None,noreg)
                                break
                            elif not dataValid:
                                print("Nomor Registrasi tidak ditemukan.")                        
                        else:
                            print(validasiNoRegis(tipe,noreg))
                elif pilEdit == 3:
                    print("Kembali Ke Menu Sebelumnya.")
                    if tipe == "EM":
                        Emergency()
                        break
                    elif tipe == "IP":
                        Inpatient()
                        break
                    elif tipe == "OP":
                        Outpatient()
                        break
                else:
                    print("Pilihan yang dimasukkan salah!! Silakan coba lagi111.") 
        except ValueError:
            print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")   
def EditDataPasien(tipe,nomedis,noreg):
    while True:
        try:
            while True:
                if noreg == None:
                    data = dataPasienUtama[nomedis]
                    print("===========DATA PASIEN===========")
                    print(f"Nomor Rekam Medis : {nomedis}")
                    print(f"Nama : {data["Nama"]}")
                    print(f"Jenis Kelamin : {data["Jenis Kelamin"]}")
                    print(f"Tanggal Lahir : {data["Tanggal Lahir"]}")
                    print(f"Alamat : {data["Alamat"]}")
                    print("="*33)
                    while True:
                        verif = input("Apakah benar data di atas akan di ubah? (y/n) : ").upper()
                        if verif == "Y":
                            while True:
                                ubahData = input("Masukkan nama kolom yang ingin di edit : ").capitalize()
                                dataBaru = dataPasienUtama[nomedis]
                                kolomValid = ["Nama", "Alamat", "Jenis kelamin", "Tanggal lahir"]
                                if (ubahData == "Nomedis") or (ubahData == "Nomor Rekam Medis"):
                                    print("Nomor Rekam Medis tidak dapat di edit. Silahkan masukkan lagi nama kolom.")
                                elif ubahData in kolomValid:
                                    ubahKolom = input(f"Masukkan {ubahData} baru : ")
                                    dataBaru[ubahData] = ubahKolom                            
                                    if tipe == "EM":
                                        dataBaruEM = dataPasien_EM[nomedis]
                                        dataBaruEM[ubahData] = ubahKolom
                                    elif tipe == "IP":
                                        dataBaruIP = dataPasien_IP[nomedis]
                                        dataBaruIP[ubahData] = ubahKolom
                                    elif tipe == "OP":
                                        dataBaruOP = dataPasien_OP[nomedis]
                                        dataBaruOP[ubahData] = ubahKolom
                                    print("Data berhasil di Edit.")
                                    break
                                else:
                                    print("Kolom yang dimaksud tidak ada. Silahkan masukkan kolom yang benar")
                            break
                        elif verif == "N":
                            print("Data tidak jadi di edit.")                        
                            break
                        else:
                            print("Pilihan yang dimasukkan salah!! Silahkan coba lagi.")
                    break
                elif nomedis == None:
                    tipe, dataValid, nomedis = cariNoreg(noreg)                    
                    print("===========DATA PASIEN===========")
                    print(f"Nomor Rekam Medis : {nomedis}")
                    print(f"Nomor Registrasi : {noreg}")
                    print(f"Nama : {dataValid["Nama"]}")
                    print(f"Jenis Kelamin : {dataValid["Jenis Kelamin"]}")
                    print(f"Tanggal Lahir : {dataValid["Tanggal Lahir"]}")
                    print(f"Alamat : {dataValid["Alamat"]}")
                    if tipe == "IP":
                        print(f"Ruangan : {dataValid["Ruangan"]}")
                    elif tipe == "OP":
                        print(f"Poli : {dataValid["Poli"]}")
                    print("="*33)
                    while True:
                        verif = input("Apakah benar data di atas akan di ubah? (y/n) : ").upper()
                        if verif == "Y":
                            while True:
                                ubahData = input("Masukkan nama kolom yang ingin di edit : ").capitalize()                                                   
                                kolomValid = ["Nama", "Alamat", "Jenis kelamin", "Tanggal lahir","Ruangan","Poli"]
                                validRuang = ["Ruang Anggrek","Ruang Edelweis","Ruang Kamboja","Ruang Matahari"]
                                validPoli = ["Poli Gigi","Poli Jantung","Poli Mata","Poli Umum"]
                                if (ubahData == "Nomedis") or (ubahData == "Nomor Rekam Medis"):
                                    print("Nomor Rekam Medis tidak dapat di edit. Silahkan masukkan lagi nama kolom.")
                                elif ubahData == "Noreg":
                                    print("Nomor Registrasi tidak dapat di edit. Silahkan masukkan lagi nama kolom.")
                                elif (tipe == "EM" or tipe == "OP") and ubahData == "Ruangan":
                                    print("Kolom Ruangan tidak ada. Silahkan masukkan lagi nama kolom.")
                                elif (tipe == "EM" or tipe == "IP") and ubahData == "Poli":
                                    print("Kolom Poli tidak ada. Silahkan masukkan lagi nama kolom.")
                                elif ubahData in kolomValid:
                                    while True:
                                        ubahKolom = input(f"Masukkan {ubahData} baru : ")       
                                        if (tipe == "IP") and (ubahData == "Ruangan") and (ubahKolom not in validRuang):
                                            print("Ruangan tidak ada! Silahkan masukkan ruangan yang benar.")
                                        elif (tipe == "OP") and (ubahData == "Poli") and (ubahKolom not in validPoli):
                                            print("Poli tidak ada! Silahkan masukkan Poli yang benar.")
                                        else:
                                            break                                
                                    dataValid[ubahData] = ubahKolom
                                    dataPasienUtama[nomedis][ubahData] = ubahKolom                               
                                    print("Data berhasil di Edit.")
                                    break
                                else:
                                    print("Kolom yang dimaksud tidak ada. Silahkan masukkan kolom yang benar")
                            break
                        elif verif == "N":
                            print("Data tidak jadi di edit.")                        
                            break
                        else:
                            print("Pilihan yang dimasukkan salah!! Silahkan coba lagi.")
                    break
            while True:
                    print("="*44)
                    pilDp = input("Apakah ingin kembali ke menu sebelumnya?(y/n) : ").upper()
                    if pilDp == "Y":
                        MenuEditDataPasien(tipe)
                        break
                    elif pilDp == "N":
                        print("Keluar dari program. Terima kasih!")
                        exit()
                    else:
                        print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
                        continue 
        except ValueError:
            print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
def MenuHapusDataPasien(tipe):
    while True:
        try:
            while True:
                print("===========HAPUS DATA PASIEN===========")
                print("1. Hapus Data Pasien Berdasarkan Nomor Rekam Medis")
                print("2. Hapus Data Pasien Berdasarkan Nomor Registrasi")
                print("3. Kembali Ke Menu Sebelumnya")
                print("="*38)
                pilEdit = int(input("Masukkan pilihan (1-3) : "))
                if pilEdit == 1:
                    while True:
                        nomedis = input("Masukkan Nomor Rekam Medis : ").upper()
                        if nomedis in dataPasienUtama:
                            HapusDataPasien(tipe,nomedis,None)
                            break
                        else:
                            print("Nomor Rekam Medis tidak terdaftar.")
                elif pilEdit == 2:
                    while True:
                        noreg = input("Masukkan Nomor Registrasi : ").upper()
                        validnoreg = validasiNoRegis(tipe,noreg)
                        if validnoreg == None:    
                            tipe, dataValid, nomedis = cariNoreg(noreg)                            
                            if dataValid:
                                HapusDataPasien(tipe,None,noreg)
                                break
                            elif not dataValid:
                                print("Nomor Registrasi tidak ditemukan.")                        
                        else:
                            print(validasiNoRegis(tipe,noreg))
                elif pilEdit == 3:
                    print("Kembali Ke Menu Sebelumnya.")
                    if tipe == "EM":
                        Emergency()
                        break
                    elif tipe == "IP":
                        Inpatient()
                        break
                    elif tipe == "OP":
                        Outpatient()
                        break
                else:
                    print("Pilihan yang dimasukkan salah!! Silakan coba lagi111.") 
        except ValueError:
            print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")  
def HapusDataPasien(tipe,nomedis,noreg):
    while True:
        try:
            while True:
                if noreg == None:
                    if tipe == "EM":
                        data = dataPasien_EM[nomedis]
                    elif tipe == "IP":
                        data = dataPasien_IP[nomedis]
                    elif tipe == "OP":
                        data = dataPasien_OP[nomedis]
                    print("===========DATA PASIEN===========")
                    print(f"Nomor Rekam Medis : {nomedis}")
                    print(f"Nama : {data["Nama"]}")
                    print(f"Jenis Kelamin : {data["Jenis Kelamin"]}")
                    print(f"Tanggal Lahir : {data["Tanggal Lahir"]}")
                    print(f"Alamat : {data["Alamat"]}")
                    print("="*33)
                    verif = input("Apakah benar data di atas akan di hapus? (y/n) : ").upper()
                    if verif == "Y":
                        if tipe == "EM":
                            del dataPasien_EM[nomedis]
                        elif tipe == "IP":
                            del dataPasien_IP[nomedis]
                        elif tipe == "OP":
                            del dataPasien_OP[nomedis]
                        print("Data berhasil di hapus.")
                        break
                    elif verif == "N":
                        print("Data tidak jadi di hapus.")                        
                        break
                    else:
                        print("Pilihan yang dimasukkan salah!! Silahkan coba lagi.")
                elif nomedis == None:
                    tipe, dataValid, nomedis = cariNoreg(noreg)                    
                    print("===========DATA PASIEN===========")
                    print(f"Nomor Rekam Medis : {nomedis}")
                    print(f"Nomor Registrasi : {noreg}")
                    print(f"Nama : {dataValid["Nama"]}")
                    print(f"Jenis Kelamin : {dataValid["Jenis Kelamin"]}")
                    print(f"Tanggal Lahir : {dataValid["Tanggal Lahir"]}")
                    print(f"Alamat : {dataValid["Alamat"]}")
                    if tipe == "IP":
                        print(f"Ruangan : {dataValid["Ruangan"]}")
                    elif tipe == "OP":
                        print(f"Poli : {dataValid["Poli"]}")
                    print("="*33)
                    verif = input("Apakah benar data di atas akan di hapus? (y/n) : ").upper()
                    if verif == "Y":
                        if tipe == "EM":
                            del dataPasien_EM[nomedis]
                        elif tipe == "IP":
                            del dataPasien_IP[nomedis]
                        elif tipe == "OP":
                            del dataPasien_OP[nomedis]
                        print("Data berhasil di hapus.")
                        break
                    elif verif == "N":
                        print("Data tidak jadi di hapus.")                        
                        break
                    else:
                        print("Pilihan yang dimasukkan salah!! Silahkan coba lagi.")
            while True:
                    print("="*44)
                    pilDp = input("Apakah ingin kembali ke menu sebelumnya?(y/n) : ").upper()
                    if pilDp == "Y":
                        MenuEditDataPasien(tipe)
                        break
                    elif pilDp == "N":
                        print("Keluar dari program. Terima kasih!")
                        exit()
                    else:
                        print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")
                        continue 
        except ValueError:
            print("Pilihan yang dimasukkan salah!! Silakan coba lagi.")

dataPasienUtama = {
        "P0001":{"Nama":"Anisa Rahayu","Jenis Kelamin":"Perempuan","Tanggal Lahir":"11/10/1996","Alamat":"Bekasi Barat"},
        "P0002":{"Nama":"Arya Saca","Jenis Kelamin":"Laki-Laki","Tanggal Lahir":"21/12/1975","Alamat":"Bekasi Timur"},
        "P0003":{"Nama":"Diana Larasati","Jenis Kelamin":"Perempuan","Tanggal Lahir":"08/08/1987","Alamat":"Jakarta Timur"},
        "P0004":{"Nama":"Evan Arne","Jenis Kelamin":"Laki-Laki","Tanggal Lahir":"01/03/1990","Alamat":"Bekasi Selatan"},
        "P0005":{"Nama":"Keenan Randika","Jenis Kelamin":"Laki-Laki","Tanggal Lahir":"12/03/1993","Alamat":"Jakarta Selatan"},        
        "P0006":{"Nama":"Alvin Ammar Dewanto","Jenis Kelamin":"Laki-Laki","Tanggal Lahir":"19/10/1992","Alamat":"Bekasi Utara"},
        "P0007":{"Nama":"Erwin Sena Saputra","Jenis Kelamin":"Laki-Laki","Tanggal Lahir":"21/07/1989","Alamat":"Bekasi Selatan"},
        "P0008":{"Nama":"Sugi Lestari","Jenis Kelamin":"Perempuan","Tanggal Lahir":"18/09/1979","Alamat":"Jakarta Timur"},
        "P0009":{"Nama":"Aamar Fardeh","Jenis Kelamin":"Laki-Laki","Tanggal Lahir":"11/04/1998","Alamat":"Bekasi Timur"},
        "P0010":{"Nama":"Febry Cahyaning","Jenis Kelamin":"Perempuan","Tanggal Lahir":"12/12/1992","Alamat":"Jakarta Barat"},
        "P0011":{"Nama":"Hilda Kurnia","Jenis Kelamin":"Perempuan","Tanggal Lahir":"16/10/1995","Alamat":"Jakarta Barat"},
        "P0012":{"Nama":"Irsyad Yudha Saputra","Jenis Kelamin":"Laki-Laki","Tanggal Lahir":"24/05/1988","Alamat":"Bekasi Barat"},
        "P0013":{"Nama":"Bunga Nabila","Jenis Kelamin":"Perempuan","Tanggal Lahir":"10/08/1997","Alamat":"Jakarta Timur"},
        "P0014":{"Nama":"Fauzi Winata","Jenis Kelamin":"Laki-Laki","Tanggal Lahir":"12/02/1990","Alamat":"Bekasi Utara"},
        "P0015":{"Nama":"Harry Setiawan","Jenis Kelamin":"Laki-Laki","Tanggal Lahir":"12/11/1999","Alamat":"Bekasi Selatan"}    
    }
dataPasien_EM = {
        "P0001":{"Noreg":"EM-0001", **dataPasienUtama["P0001"]},
        "P0002":{"Noreg":"EM-0002", **dataPasienUtama["P0002"]},
        "P0003":{"Noreg":"EM-0003", **dataPasienUtama["P0003"]},
        "P0004":{"Noreg":"EM-0004", **dataPasienUtama["P0004"]},
        "P0005":{"Noreg":"EM-0005", **dataPasienUtama["P0005"]}
    }
dataPasien_IP = {
        "P0006":{"Noreg":"IP-0001", **dataPasienUtama["P0006"],"Ruangan":"Ruang Edelweis"},
        "P0007":{"Noreg":"IP-0002", **dataPasienUtama["P0007"],"Ruangan":"Ruang Matahari"},
        "P0008":{"Noreg":"IP-0003", **dataPasienUtama["P0008"],"Ruangan":"Ruang Kamboja"},
        "P0009":{"Noreg":"IP-0004", **dataPasienUtama["P0009"],"Ruangan":"Ruang Anggrek"},
        "P0010":{"Noreg":"IP-0005", **dataPasienUtama["P0010"],"Ruangan":"Ruang Kamboja"}
    }
dataPasien_OP = {
        "P0011":{"Noreg":"OP-0001", **dataPasienUtama["P0011"],"Poli":"Poli Mata"},
        "P0012":{"Noreg":"OP-0002", **dataPasienUtama["P0012"],"Poli":"Poli Gigi"},
        "P0013":{"Noreg":"OP-0003", **dataPasienUtama["P0013"],"Poli":"Poli Umum"},
        "P0014":{"Noreg":"OP-0004", **dataPasienUtama["P0014"],"Poli":"Poli Mata"},
        "P0015":{"Noreg":"OP-0005", **dataPasienUtama["P0015"],"Poli":"Poli Jantung"}
    }
MenuUtama()