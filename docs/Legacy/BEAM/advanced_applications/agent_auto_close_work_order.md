# Agent Servis ile Otomatik İş Emri Kapama

AutoCloseWorkOrder servisi Kapanmaya hazır olan İş emirlerini kontrol ederek, İş Emrini durumunu “Açık” durumdan “Kapalı” duruma getirmektedir.  Servis çalıştıktan sonra işe alınan İş Emirleri için belirlenen kişilere mail atmaktadır.

• Örmek  “40- KAPATMA ONAYINDA” olan statüsündeki,  480 dk ve fazla açık kalmış iş emirlerini otomatik kapatacaktır.
	•  “KAPATMA ONAYINDA” statüsünde ““İş Emri Kapama Validasyonlarını Aktif Et” seçeneği işaretlendiğinde, bu statüye alınıp kaydedilen İş Emrinde sanki kapatılıyormuş gibi doldurulması gereken alanların kontrolü yapılacaktır. (Resim -2 )
	• Servis ayarları , filtreler aşağıda listelenmektedir.  (Resim -1)
	• Şirket, Fabrika, Sarfyeri, Kısım, Bakım/Arıza Kodu, Bakım Önceliği, Statü Kodu, İş Emri Türü ve İş Tipine göre  filtreleme yapılabilmektedir
	• Wait Minute : Statü değişikliğinden sonra , İş Emri minimum kaç dk beklenmesi isteniyorsa burays giriliyor.


Aşağıda yapılan ayar şu şekildedir, 200 Şirketinde “43” statüsündeki  ve “ARB” İş Emri Türündeki İş Emirleri , 43 statüsüne alındıktan 1 dk sonra hala açıksa kapansın anlamına gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/AutoClose1-d2850fa2-839a-4b31-9d84-dbe6c51c538b.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/AutoClose2-53f32606-77bc-4f19-aa9f-32312bb9fc2d.png)

