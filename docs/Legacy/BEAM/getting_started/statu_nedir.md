# STATÜ NEDİR?

# BEAM ÜZERİNDE STATÜ EKLEME VE STATÜLER ÜZERİNDEN BİLGİLENDİRME ALINMASI NASIL GERÇEKLEŞİR?

Statüler iş emirlerinin anlık durumu hakkında bilgi edinmemizi sağlar. Benim ilgili iş emrimde bakım başlamış mı, bakım tamamlanmış mı, devreye alındı mı, sorumlu atandı mı tarzında verileri "statü" alanından öğrenebilirim. Bu tarz veriler sistemde otomatik olarak eklidir ve varsayılanları bulunmaktadır. Statülerin varsayılanlarının bulunması ilgili iş içerisinde manuel olarak herhangi bir veri girişi gerçekleştirmeden işin statüsünün otomatik değişmesi anlamını taşımaktadır. Örnek veriyorum bir çalışan personel işin üzerine gelip "ben bu işe başladım" der ise iş statüsünü otomatik olarak "işe başlandı" olarak günceller. Çalışan personelin işin içerisine girip statüyü "işe başlandı" statüsüne çekmesine gerek yoktur

Bu dokümanımızda varsayılanı olmayan bir statünün sisteme eklenmesi üzerinde duracağız. 

Bakım Yönetimi```>``` Tanımlar```>``` Statüler alanında ekle butonu ile süreç başlatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/statü.1-121d5e0b-5c85-41a0-8b15-be01fc877ecf.png)

Statü tipi sekmesinde hangi sayfalarda bu statü kullanılacak ise seçim yapılır. Genelde yaygın olarak kullanılan Emir / Talep Statüsü sekmesidir. Statü kodu yazılır. Önemli olan "statü tanımı" alanıdır. İş emirlerinde veya iş taleplerinde işin hangi durumu belirtilmek isteniyorsa "statü tanımı" alanına yazılır.

Örnek veriyorum iş emirlerinde malzeme beklenmeye başlandı. Çalışan personelin iş emri içerisinde bu statüyü seçmesi talep ediliyor, öncelikle sisteme tanıtıp seçimini yaptıracağız. Bu sebep ile statü tanımı alanına "malzeme bekleniyor" yazdık.

![](https://docsbimser.blob.core.windows.net/imagecontainer/statü.2-36a8c9ca-3b1c-4938-a3e2-22d8fdf765af.png)

Bu statü çalışan kişinin ilgili iş emrinde manuel seçim yaparak işin durumunu belirteceği bir statüdür. Bu sebep ile "varsayılanlar" sekmesinden herhangi bir seçim yapmaması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/statü.1.a-124e8f1b-b699-41a6-91c5-9109db37bfda.png)

### VARSAYILANI OLAN BİR STATÜ SİSTEME EKLEMEK İSTERSEK NE YAPACAĞIZ?

### VARSAYILAN MEVCUT İSE MUHAKKAK İŞARETLENİR

Varsayılanın statülerde işlevi şudur: Biz iş emrinde herhangi bir işlem gerçekleştirdiğimizde işin kendi durumunu (statüsünü) otomatik olarak değiştirmesini sağlar.

Bu varsayılanlar belirli durumlarda gerçekleşir. Örnek veriyorum iş içerisinde "üretimi durdurdum" seçeneği işaretlenerek kaydedildi. Statü alanında değişim gerçekleştirilmesine gerek kalmadan iş statüsünü "üretim durdu" olarak güncelleyecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/statü.2.a.-ba8b2439-3052-4ba1-b212-bb7d94cd39b9.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/statü%202.b.-a4167df4-81d1-4ca6-94aa-332960ba0f34.png)

### STATÜLER ÜZERİNDEN BİLDİRİ ALINMAK İSTENİYORSA NE YAPILMALI?

Sistem üzerinden bildiri alınmak isteniyorsa varsayılanlar sekmesinden "mesaj gönder" ifadesinin işaretli olması gerekmektedir

İlgili statü hakkında bilgilendirilecek kişileri "e posta/sms tablosu" üzerinden sisteme tanıtırım

