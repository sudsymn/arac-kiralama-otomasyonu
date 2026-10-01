import os 

while True:
    print("********** Ana Menü **********")
    print("(M) - Müşteri")
    print("(B) - Bakım")
    print("(K) - Kiralama")
    print("(C-Ç) - Çıkış")
    secim = input("Seçmek istediğiniz işlemin baş harfini giriniz: ").upper()
    
    if secim == "M":
        if not os.path.exists("musteriler.ss"):
            dosya = open("musteriler.ss", "w", encoding="utf-8")
            dosya.close() 
            print("Müşteriler dosyası bulunamadı...Yeni dosya oluşturuldu...")   
        
        Musteriler = []
        dosya = open("musteriler.ss", "r", encoding="utf-8")
        for satir in dosya:
            Musteriler.append(satir.strip())
        dosya.close()
                    
        while True:
            print("********** Müşteri İşlemleri **********")
            print("1-) Ekleme")
            print("2-) Silme")
            print("3-) Güncelleme")
            print("4-) Tümünü silme")
            print("5-) Araya Ekleme")
            print("6-) Bul")
            print("7-) Sırala")
            print("8-) Listele")
            print("9-) Ana Menüye Dön")
            print("0-) Çıkış")
            altSecim = input("Seçmek istediğiniz işlemin rakamını tuşlayınız: ")
            
            if altSecim == "1":
                print("*** Ekleme İşlemleri ***")
                while True:
                    ad = input("Müşteri Adı: ")  
                    if len(ad) < 2 or (ad.replace(' ','').isalpha() == False):
                        print("\t Ad sadece metinsel karakterden oluşmalıdır. En az iki harf giriniz.")
                    else:
                        break    
                while True:
                    soyad = input("Müşteri Soyadı: ")  
                    if len(soyad) < 2 or (soyad.replace(' ','').isalpha() == False):
                        print("\t Soyad sadece metinsel karakterden oluşmalıdır. En az iki harf giriniz.")
                    else:
                        break
                while True:
                    telefon = input("Müşteri Telefon Numarası: ")
                    if len(telefon) != 11 or (telefon.isdigit() == False):
                        print("\tTelefon numaranızın başında sıfır olmalı...Sadece rakamlardan oluşmalı...")
                    else:
                        break                
                while True:
                    ehliyetNo = input("Ehliyet Numarası: ")
                    if len(ehliyetNo) != 6 or (ehliyetNo.isdigit() == False):
                        print("\tEhliyet numaranız 6 rakamdan oluşmalıdır...")
                    else:
                        break    
                while True:
                    adres = input("Adres: ")
                    if len(adres) < 2:
                        print("\tAdres boş bırakılamaz!")  
                    else:
                        break      
                while True:
                    musteriTur = input("Müşteri Tür (Bireysel-Kurumsal): ")
                    if musteriTur.lower() != "bireysel" and musteriTur.lower() != "kurumsal":
                        print("\tMüşteri türü geçersiz...")
                    else:
                        break
                        
                kayit = ad + "-" + soyad + "-" + telefon + "-" + ehliyetNo + "-" + adres + "-" + musteriTur
                Musteriler.append(kayit)
                dosya = open("musteriler.ss", "a", encoding="utf-8")
                dosya.write(kayit + "\n")
                dosya.close()
                input("Ekleme işlemi tamamlandı...\nMenüye dönmek için entera basınız.")                  
            
            elif altSecim == "2":
                print("*** Silme İşlemleri ***\n*** Dosyada Kayıtlı Müşteriler ***")
                print("Ad-Soyad-Telefon-Ehliyet No-Adres-Müşteri Türü")
                satirNo = 1
                for satir in Musteriler:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                
                if len(Musteriler) > 0:
                    silinecekSatirNo = int(input("Silinecek satır numarasını giriniz: "))
                    if silinecekSatirNo >= 1 and silinecekSatirNo <= len(Musteriler):
                        Musteriler.pop(silinecekSatirNo - 1)
                        dosya = open("musteriler.ss", "w", encoding="utf-8")
                        for satir in Musteriler:
                            dosya.write(satir + "\n")
                        dosya.close()
                        print("Kayıt silindi...")
                    else:
                        print("Geçersiz satır numarası!")
                else:
                    print("Silinecek kayıt bulunamadı...")
                input("Menüye dönmek için entera basınız.")    
            
            elif altSecim == "3":
                print("*** Güncelleme İşlemleri ***\n*** Dosyada Kayıtlı Müşteriler ***")
                print("Ad-Soyad-Telefon-Ehliyet No-Adres-Müşteri Türü")
                satirNo = 1
                for satir in Musteriler:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                
                if len(Musteriler) > 0:
                    guncellenecekSatirNo = int(input("Güncellenecek satır numarasını giriniz: "))
                    if guncellenecekSatirNo >= 1 and guncellenecekSatirNo <= len(Musteriler):
                        parcalar = Musteriler[guncellenecekSatirNo - 1].split('-')
                        
                        while True:
                            ad = input("Müşteri Adı (" + parcalar[0] + "): ")
                            if ad == "":
                                ad = parcalar[0]
                                break
                            elif len(ad) < 2 or (ad.replace(' ','').isalpha() == False):
                                print("\t Ad sadece metinsel karakterden oluşmalıdır. En az iki harf giriniz.")
                            else:
                                break

                        while True:
                            soyad = input("Müşteri Soyadı (" + parcalar[1] + "): ")
                            if soyad == "":
                                soyad = parcalar[1]
                                break
                            elif len(soyad) < 2 or (soyad.replace(' ','').isalpha() == False):
                                print("\t Soyad sadece metinsel karakterden oluşmalıdır. En az iki harf giriniz.")
                            else:
                                break

                        while True:
                            telefon = input("Telefon (" + parcalar[2] + "): ")
                            if telefon == "":
                                telefon = parcalar[2]
                                break
                            elif len(telefon) != 11 or (telefon.isdigit() == False):
                                print("\tTelefon numaranızın başında sıfır olmalı...Sadece rakamlardan oluşmalı...")
                            else:
                                break

                        while True:
                            ehliyetNo = input("Ehliyet No (" + parcalar[3] + "): ")
                            if ehliyetNo == "":
                                ehliyetNo = parcalar[3]
                                break
                            elif len(ehliyetNo) != 6 or (ehliyetNo.isdigit() == False):
                                print("\tEhliyet numaranız 6 rakamdan oluşmalıdır...")
                            else:
                                break

                        while True:
                            adres = input("Adres (" + parcalar[4] + "): ")
                            if adres == "":
                                adres = parcalar[4]
                                break
                            elif len(adres) < 2:
                                print("\tAdres boş bırakılamaz!")
                            else:
                                break

                        while True:
                            musteriTur = input("Müşteri Türü (" + parcalar[5] + "): ")
                            if musteriTur == "":
                                musteriTur = parcalar[5]
                                break
                            elif musteriTur.lower() != "bireysel" and musteriTur.lower() != "kurumsal":
                                print("\tMüşteri türü geçersiz...")
                            else:
                                break
                        
                        yeniKayit = ad + "-" + soyad + "-" + telefon + "-" + ehliyetNo + "-" + adres + "-" + musteriTur
                        Musteriler[guncellenecekSatirNo - 1] = yeniKayit
                        
                        dosya = open("musteriler.ss", "w", encoding="utf-8")
                        for satir in Musteriler:
                            dosya.write(satir + "\n")
                        dosya.close()
                        print("Kayıt güncellendi...")
                    else:
                        print("Geçersiz satır numarası!")
                else:
                    print("Güncellenecek kayıt bulunamadı...")
                input("Menüye dönmek için entera basınız.")    
            
            elif altSecim == "4":
                print("*** Tüm Kayıtları Silme İşlemleri ***")
                onay = input("Dosyadaki tüm kayıtlar silinecektir. Devam etmek istiyor musunuz? (E-H): ").upper()
                if onay == "E":
                    Musteriler.clear()
                    dosya = open("musteriler.ss", "w", encoding="utf-8")
                    dosya.close()
                    print("Dosyadaki tüm kayıtlar silindi...")
                else:
                    print("Silme işlemi iptal edildi...")
                input("Menüye dönmek için entera basınız.")        
            
            elif altSecim == "5":
                print("*** Araya Ekleme İşlemleri ***\nDosyada Kayıtlı Müşteriler **********")
                satirNo = 1
                for satir in Musteriler:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                
                arayaEklenecekSatirNo = int(input("Araya eklenecek satır numarasını giriniz: "))
                if arayaEklenecekSatirNo >= 1 and arayaEklenecekSatirNo <= len(Musteriler) + 1:
                    while True:
                        ad = input("Müşteri Adı: ")  
                        if len(ad) < 2 or (ad.replace(' ','').isalpha() == False):
                            print("\t Ad sadece metinsel karakterden oluşmalıdır. En az iki harf giriniz.")
                        else:
                            break    
                    while True:
                        soyad = input("Müşteri Soyadı: ")  
                        if len(soyad) < 2 or (soyad.replace(' ','').isalpha() == False):
                            print("\t Soyad sadece metinsel karakterden oluşmalıdır. En az iki harf giriniz.")
                        else:
                            break
                    while True:
                        telefon = input("Müşteri Telefon Numarası: ")
                        if len(telefon) != 11 or (telefon.isdigit() == False):
                            print("\tTelefon numaranızın başında sıfır olmalı...Sadece rakamlardan oluşmalı...")
                        else:
                            break                
                    while True:
                        ehliyetNo = input("Ehliyet Numarası: ")
                        if len(ehliyetNo) != 6 or (ehliyetNo.isdigit() == False):
                            print("\tEhliyet numaranız 6 rakamdan oluşmalıdır...")
                        else:
                            break    
                    while True:
                        adres = input("Adres: ")
                        if len(adres) < 2:
                            print("\tAdres boş bırakılamaz!")  
                        else:
                            break      
                    while True:
                        musteriTur = input("Müşteri Tür (Bireysel-Kurumsal): ")
                        if musteriTur.lower() != "bireysel" and musteriTur.lower() != "kurumsal":
                            print("\tMüşteri türü geçersiz...")
                        else:
                            break
                    
                    kayit = ad + "-" + soyad + "-" + telefon + "-" + ehliyetNo + "-" + adres + "-" + musteriTur
                    Musteriler.insert(arayaEklenecekSatirNo - 1, kayit)
                    dosya = open("musteriler.ss", "w", encoding="utf-8")
                    for satir in Musteriler:
                        dosya.write(satir + "\n")
                    dosya.close()
                    print("Kayıt eklendi...")
                else:
                    print("Geçersiz satır numarası!")
                input("Menüye dönmek için entera basınız.")    
            
            elif altSecim == "6":
                print("*** Arama İşlemleri (Bul) ***") 
                aranan = input("Aranacak değeri giriniz: ")
                bulunan = 0
                for satir in Musteriler:
                    if aranan.lower() in satir.lower():
                        bulunan = bulunan + 1
                        print(str(bulunan) + ") " + satir)
                if bulunan == 0:
                    print("Aranan bilgi bulunamadı...")
                input("Menüye dönmek için entera basınız.")                    
            
            elif altSecim == "7":
                print("*** Sıralama İşlemleri ***")
                Musteriler.sort()
                satirNo = 1
                for satir in Musteriler:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                
                dosya = open("musteriler.ss", "w", encoding="utf-8")
                for satir in Musteriler:
                    dosya.write(satir + "\n")
                dosya.close()
                print("Kayıtlar sıralandı...")
                input("Menüye dönmek için entera basınız...")      
            
            elif altSecim == "8":
                print("*** Listeleme İşlemleri ***")
                print("Ad-Soyad-Telefon-Ehliyet No-Adres-Müşteri Türü")
                satirNo = 1
                for satir in Musteriler:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                input("Menüye dönmek için entera basınız.")     
            
            elif altSecim == "9":
                break
            elif altSecim == "0":
                exit()

    elif secim == "B":
        if not os.path.exists("bakim.ss"):
            dosya = open("bakim.ss", "w", encoding="utf-8")
            dosya.close() 
            print("Bakım dosyası bulunamadı...Yeni dosya oluşturuldu...")   
        
        Bakim = []
        dosya = open("bakim.ss", "r", encoding="utf-8")
        for satir in dosya:
            Bakim.append(satir.strip())
        dosya.close()
                    
        while True:
            print("********** Bakım İşlemleri **********") 
            print("1-) Ekleme")
            print("2-) Silme")
            print("3-) Güncelleme")
            print("4-) Tümünü silme")
            print("5-) Araya Ekleme")
            print("6-) Bul")
            print("7-) Sırala")
            print("8-) Listele")
            print("9-) Ana Menüye Dön")
            print("0-) Çıkış")
            altSecim1 = input("Seçmek istediğiniz işlemin rakamını tuşlayınız: ")
            
            if altSecim1 == "1":
                print("*** Ekleme İşlemleri ***")
                while True:
                    aracPlaka = input("Araç plakası: ")
                    if len(aracPlaka) < 5:
                        print("\tGeçersiz plaka girdiniz!")
                    else:
                        break
                while True:
                    tarih = input("Bakım tarihi (gg.aa.yyyy): ")
                    if len(tarih) < 8:
                        print("\tTarih formatı geçersiz!")
                    else:
                        break
                while True:
                    ucret = input("Bakım ücreti: ")
                    if ucret.isdigit() == False:
                        print("\tBakım ücreti sayısal olmalıdır!")
                    else:
                        break
                while True:
                    aciklama = input("Açıklama: ")
                    if len(aciklama) < 2:
                        print("\tAçıklama boş bırakılamaz!")
                    else:
                        break

                kayit = aracPlaka + "-" + tarih + "-" + ucret + "-" + aciklama
                Bakim.append(kayit)
                dosya = open("bakim.ss", "a", encoding="utf-8")
                dosya.write(kayit + "\n")
                dosya.close()
                input("Ekleme işlemi tamamlandı...\nMenüye dönmek için entera basınız.")    
            
            elif altSecim1 == "2":
                print("*** Silme İşlemleri ***")
                satirNo = 1
                for satir in Bakim:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                if len(Bakim) > 0:
                    silinecekSatirNo = int(input("Silinecek satır numarasını giriniz: "))
                    if silinecekSatirNo >= 1 and silinecekSatirNo <= len(Bakim):
                        Bakim.pop(silinecekSatirNo - 1)
                        dosya = open("bakim.ss", "w", encoding="utf-8")
                        for satir in Bakim:
                            dosya.write(satir + "\n")
                        dosya.close()
                        print("Kayıt silindi...")
                    else:
                        print("Geçersiz satır numarası!")
                else:
                    print("Silinecek kayıt bulunamadı...")
                input("Menüye dönmek için entera basınız.")    
            
            elif altSecim1 == "3":
                print("*** Güncelleme İşlemleri ***")
                satirNo = 1
                for satir in Bakim:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                if len(Bakim) > 0:
                    guncellenecekSatirNo = int(input("Güncellenecek satır numarasını giriniz: "))
                    if guncellenecekSatirNo >= 1 and guncellenecekSatirNo <= len(Bakim):
                        parcalar = Bakim[guncellenecekSatirNo - 1].split('-')
                        
                        while True:
                            aracPlaka = input("Plaka (" + parcalar[0] + "): ")
                            if aracPlaka == "":
                                aracPlaka = parcalar[0]
                                break
                            elif len(aracPlaka) < 5:
                                print("\tGeçersiz plaka girdiniz!")
                            else:
                                break

                        while True:
                            tarih = input("Tarih (" + parcalar[1] + "): ")
                            if tarih == "":
                                tarih = parcalar[1]
                                break
                            elif len(tarih) < 8:
                                print("\tTarih formatı geçersiz!")
                            else:
                                break

                        while True:
                            ucret = input("Ücret (" + parcalar[2] + "): ")
                            if ucret == "":
                                ucret = parcalar[2]
                                break
                            elif ucret.isdigit() == False:
                                print("\tBakım ücreti sayısal olmalıdır!")
                            else:
                                break

                        while True:
                            aciklama = input("Açıklama (" + parcalar[3] + "): ")
                            if aciklama == "":
                                aciklama = parcalar[3]
                                break
                            elif len(aciklama) < 2:
                                print("\tAçıklama boş bırakılamaz!")
                            else:
                                break
                        
                        Bakim[guncellenecekSatirNo - 1] = aracPlaka + "-" + tarih + "-" + ucret + "-" + aciklama
                        dosya = open("bakim.ss", "w", encoding="utf-8")
                        for satir in Bakim:
                            dosya.write(satir + "\n")
                        dosya.close()
                        print("Kayıt güncellendi...")
                    else:
                        print("Geçersiz satır numarası!")
                else:
                    print("Güncellenecek kayıt bulunamadı...")
                input("Menüye dönmek için entera basınız.")    
            
            elif altSecim1 == "4":
                onay1 = input("Tüm kayıtlar silinecek. Devam edilsin mi? (E-H): ").upper()
                if onay1 == "E":
                    Bakim.clear()
                    dosya = open("bakim.ss", "w", encoding="utf-8")
                    dosya.close()
                    print("Tüm kayıtlar silindi...")
                input("Menüye dönmek için entera basınız.")
            
            elif altSecim1 == "5":
                satirNo = 1
                for satir in Bakim:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                arayaEklenecekSatirNo = int(input("Araya eklenecek satır numarasını giriniz: "))
                if arayaEklenecekSatirNo >= 1 and arayaEklenecekSatirNo <= len(Bakim) + 1:
                    while True:
                        aracPlaka = input("Araç plakası: ")
                        if len(aracPlaka) < 5:
                            print("\tGeçersiz plaka girdiniz!")
                        else:
                            break
                    while True:
                        tarih = input("Bakım tarihi: ")
                        if len(tarih) < 8:
                            print("\tTarih formatı geçersiz!")
                        else:
                            break
                    while True:
                        ucret = input("Bakım ücreti: ")
                        if ucret.isdigit() == False:
                            print("\tBakım ücreti sayısal olmalıdır!")
                        else:
                            break
                    while True:
                        aciklama = input("Açıklama: ")
                        if len(aciklama) < 2:
                            print("\tAçıklama boş bırakılamaz!")
                        else:
                            break

                    kayit = aracPlaka + "-" + tarih + "-" + ucret + "-" + aciklama
                    Bakim.insert(arayaEklenecekSatirNo - 1, kayit)
                    dosya = open("bakim.ss", "w", encoding="utf-8")
                    for satir in Bakim:
                        dosya.write(satir + "\n")
                    dosya.close()
                    print("Kayıt araya eklendi...")
                else:
                    print("Geçersiz satır numarası!")
                input("Menüye dönmek için entera basınız.")   
            
            elif altSecim1 == "6":
                aranan = input("Aranacak değeri giriniz: ")
                bulunan = 0
                for satir in Bakim:
                    if aranan.lower() in satir.lower():
                        bulunan = bulunan + 1
                        print(str(bulunan) + ") " + satir)
                if bulunan == 0:
                    print("Kayıt bulunamadı.")
                input("Menüye dönmek için entera basınız.")
            
            elif altSecim1 == "7":
                Bakim.sort()
                satirNo = 1
                for satir in Bakim:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                dosya = open("bakim.ss", "w", encoding="utf-8")
                for satir in Bakim:
                    dosya.write(satir + "\n")
                dosya.close()
                input("Menüye dönmek için entera basınız.")   
            
            elif altSecim1 == "8":
                satirNo = 1
                for satir in Bakim:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                input("Menüye dönmek için entera basınız.")     
            
            elif altSecim1 == "9":
                break
            elif altSecim1 == "0":
                exit()

    elif secim == "K":
        if not os.path.exists("kiralama.ss"):
            dosya = open("kiralama.ss", "w", encoding="utf-8")
            dosya.close() 
            print("Kiralama dosyası bulunamadı...Yeni dosya oluşturuldu...")   
        
        Kiralama = []
        dosya = open("kiralama.ss", "r", encoding="utf-8")
        for satir in dosya:
            Kiralama.append(satir.strip())
        dosya.close()
                    
        while True:
            print("********** Kiralama İşlemleri **********")
            print("1-) Ekleme")
            print("2-) Silme")
            print("3-) Güncelleme")
            print("4-) Tümünü silme")
            print("5-) Araya Ekleme")
            print("6-) Bul")
            print("7-) Sırala")
            print("8-) Listele")
            print("9-) Ana Menüye Dön")
            print("0-) Çıkış") 
            altSecim2 = input("Seçmek istediğiniz işlemin rakamını tuşlayınız: ")
            
            if altSecim2 == "1":
                while True:
                    subeAd = input("Şube adı: ")
                    if len(subeAd) < 2:
                        print("\tŞube adı en az iki harf olmalıdır!")
                    else:
                        break
                while True:
                    musteriAdSoyad = input("Müşteri adı-soyadı: ")
                    if len(musteriAdSoyad) < 3:
                        print("\tMüşteri adı soyadı geçersiz!")
                    else:
                        break
                while True:
                    kiraBaslamaTarihi = input("Kira başlama tarihi (gg.aa.yyyy): ")
                    if len(kiraBaslamaTarihi) < 8:
                        print("\tTarih geçersiz!")
                    else:
                        break
                while True:
                    kiraBitistarihi = input("Kira bitiş tarihi (gg.aa.yyyy): ")
                    if len(kiraBitistarihi) < 8:
                        print("\tTarih geçersiz!")
                    else:
                        break
                while True:
                    teslimTarihi = input("Teslim tarihi (gg.aa.yyyy): ")
                    if len(teslimTarihi) < 8:
                        print("\tTarih geçersiz!")
                    else:
                        break
                while True:
                    plakaNo = input("Plaka numarası: ")
                    if len(plakaNo) < 5:
                        print("\tPlaka geçersiz!")
                    else:
                        break
                
                kayit = subeAd + "-" + musteriAdSoyad + "-" + kiraBaslamaTarihi + "-" + kiraBitistarihi + "-" + teslimTarihi + "-" + plakaNo
                Kiralama.append(kayit)
                dosya = open("kiralama.ss", "a", encoding="utf-8")
                dosya.write(kayit + "\n")
                dosya.close()
                input("Ekleme işlemleri tamamlandı. Menüye dönmek için entera basınız.")    
            
            elif altSecim2 == "2":
                satirNo = 1
                for satir in Kiralama:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                if len(Kiralama) > 0:
                    silinecekSatirNo = int(input("Silinecek satır numarasını giriniz: "))
                    if silinecekSatirNo >= 1 and silinecekSatirNo <= len(Kiralama):
                        Kiralama.pop(silinecekSatirNo - 1)
                        dosya = open("kiralama.ss", "w", encoding="utf-8")
                        for satir in Kiralama:
                            dosya.write(satir + "\n")
                        dosya.close()
                        print("Kayıt silindi...")
                    else:
                        print("Geçersiz satır numarası!")
                else:
                    print("Silinecek kayıt bulunamadı...")
                input("Menüye dönmek için entera basınız.")    
            
            elif altSecim2 == "3":
                satirNo = 1
                for satir in Kiralama:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                if len(Kiralama) > 0:
                    guncellenecekSatirNo = int(input("Güncellenecek satır numarasını giriniz: "))
                    if guncellenecekSatirNo >= 1 and guncellenecekSatirNo <= len(Kiralama):
                        parcalar = Kiralama[guncellenecekSatirNo - 1].split('-')
                        
                        while True:
                            subeAd = input("Şube Ad (" + parcalar[0] + "): ")
                            if subeAd == "":
                                subeAd = parcalar[0]
                                break
                            elif len(subeAd) < 2:
                                print("\tŞube adı en az iki harf olmalıdır!")
                            else:
                                break

                        while True:
                            musteriAdSoyad = input("Müşteri (" + parcalar[1] + "): ")
                            if musteriAdSoyad == "":
                                musteriAdSoyad = parcalar[1]
                                break
                            elif len(musteriAdSoyad) < 3:
                                print("\tMüşteri adı soyadı geçersiz!")
                            else:
                                break

                        while True:
                            kiraBaslamaTarihi = input("Başlama Tarihi (" + parcalar[2] + "): ")
                            if kiraBaslamaTarihi == "":
                                kiraBaslamaTarihi = parcalar[2]
                                break
                            elif len(kiraBaslamaTarihi) < 8:
                                print("\tTarih geçersiz!")
                            else:
                                break

                        while True:
                            kiraBitistarihi = input("Bitiş Tarihi (" + parcalar[3] + "): ")
                            if kiraBitistarihi == "":
                                kiraBitistarihi = parcalar[3]
                                break
                            elif len(kiraBitistarihi) < 8:
                                print("\tTarih geçersiz!")
                            else:
                                break

                        while True:
                            teslimTarihi = input("Teslim Tarihi (" + parcalar[4] + "): ")
                            if teslimTarihi == "":
                                teslimTarihi = parcalar[4]
                                break
                            elif len(teslimTarihi) < 8:
                                print("\tTarih geçersiz!")
                            else:
                                break

                        while True:
                            plakaNo = input("Plaka (" + parcalar[5] + "): ")
                            if plakaNo == "":
                                plakaNo = parcalar[5]
                                break
                            elif len(plakaNo) < 5:
                                print("\tPlaka geçersiz!")
                            else:
                                break
                        
                        Kiralama[guncellenecekSatirNo - 1] = subeAd + "-" + musteriAdSoyad + "-" + kiraBaslamaTarihi + "-" + kiraBitistarihi + "-" + teslimTarihi + "-" + plakaNo
                        dosya = open("kiralama.ss", "w", encoding="utf-8")
                        for satir in Kiralama:
                            dosya.write(satir + "\n")
                        dosya.close()
                        print("Kayıt güncellendi...")
                    else:
                        print("Geçersiz satır numarası!")
                else:
                    print("Güncellenecek kayıt bulunamadı...")
                input("Menüye dönmek için entera basınız.")    
            
            elif altSecim2 == "4":
                onay2 = input("Tüm kayıtlar silinecektir. Devam edilsin mi? (E-H): ").upper()
                if onay2 == "E":
                    Kiralama.clear()
                    dosya = open("kiralama.ss", "w", encoding="utf-8")
                    dosya.close()
                    print("Tüm kayıtlar silindi...")
                input("Menüye dönmek için entera basınız.") 
            
            elif altSecim2 == "5":
                satirNo = 1
                for satir in Kiralama:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                arayaEklenecekSatirNo = int(input("Araya eklenecek satır numarasını giriniz: ")) 
                if arayaEklenecekSatirNo >= 1 and arayaEklenecekSatirNo <= len(Kiralama) + 1:
                    while True:
                        subeAd = input("Şube adı: ")
                        if len(subeAd) < 2:
                            print("\tŞube adı en az iki harf olmalıdır!")
                        else:
                            break
                    while True:
                        musteriAdSoyad = input("Müşteri adı-soyadı: ")
                        if len(musteriAdSoyad) < 3:
                            print("\tMüşteri adı soyadı geçersiz!")
                        else:
                            break
                    while True:
                        kiraBaslamaTarihi = input("Kira başlama tarihi: ")
                        if len(kiraBaslamaTarihi) < 8:
                            print("\tTarih geçersiz!")
                        else:
                            break
                    while True:
                        kiraBitistarihi = input("Kira bitiş tarihi: ")
                        if len(kiraBitistarihi) < 8:
                            print("\tTarih geçersiz!")
                        else:
                            break
                    while True:
                        teslimTarihi = input("Teslim tarihi: ")
                        if len(teslimTarihi) < 8:
                            print("\tTarih geçersiz!")
                        else:
                            break
                    while True:
                        plakaNo = input("Plaka numarası: ")
                        if len(plakaNo) < 5:
                            print("\tPlaka geçersiz!")
                        else:
                            break

                    kayit = subeAd + "-" + musteriAdSoyad + "-" + kiraBaslamaTarihi + "-" + kiraBitistarihi + "-" + teslimTarihi + "-" + plakaNo
                    Kiralama.insert(arayaEklenecekSatirNo - 1, kayit)
                    dosya = open("kiralama.ss", "w", encoding="utf-8")
                    for satir in Kiralama:
                        dosya.write(satir + "\n")
                    dosya.close()
                    print("Kayıt araya eklendi...")
                else:
                    print("Geçersiz satır numarası!")
                input("Menüye dönmek için entera basınız.")    
            
            elif altSecim2 == "6":
                aranan = input("Aranacak değeri giriniz: ")
                bulunan = 0
                for satir in Kiralama:
                    if aranan.lower() in satir.lower():
                        bulunan = bulunan + 1
                        print(str(bulunan) + ") " + satir)
                if bulunan == 0:
                    print("Kayıt bulunamadı...")
                input("Menüye dönmek için entera basınız.")  
            
            elif altSecim2 == "7":
                Kiralama.sort()
                satirNo = 1
                for satir in Kiralama:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                dosya = open("kiralama.ss", "w", encoding="utf-8")
                for satir in Kiralama:
                    dosya.write(satir + "\n")
                dosya.close()
                input("Menüye dönmek için entera basınız.")    
            
            elif altSecim2 == "8":
                satirNo = 1
                for satir in Kiralama:
                    print(str(satirNo) + ") " + satir)
                    satirNo = satirNo + 1
                input("Menüye dönmek için entera basınız.")     
            
            elif altSecim2 == "9":
                break
            elif altSecim2 == "0":
                exit()

    elif secim == "C" or secim == "Ç":
        print("Çıkış yapıldı.")
        break
    else:
        print("Yanlış seçim yaptınız.")