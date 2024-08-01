# GETLİNK METODU KULLANIMI HK.

Talebe istinaden ..BSAT/BSATWebAPI.asmx web servisimize GetLink metodu eklenmiştir.
Metot üzerinden aşağıda bulunan modüllerimizde bulunan kayıtların görüntüleme linkleri alınabilmektedir.
DÖF,
MS,
Öneri,
Aksiyon (Fonk1= Ana Aksiyon, Fonk2=Aksiyon Kalemi),
Doküman (Fonk1= Yetkili Link, Fonk2=Yetkisiz Link),
Risk 
Metot moduleID, fonksiyonID ve kayitKodu parametreleri almaktadır. fonksiyonID parametresi yalnızca Aksiyon ve Doküman modülü üzerinden link alınacağı durumlarda gönderilebilir diğer modüller için ilgili parametre boş gönderilebilir gönderilse dahi metot üzerinde herhangi bir etkisi olmaz. Aksiyon ve Doküman modülleri için gönderilebilecek fonksiyon ID bilgileri yukarıda yer aldığı gibidir yani integer olarak 1 ve 2 değeri gönderilebilir.
Örneğin yetkisiz doküman linki alınmak istenilen durumda fonksiyonID 2 değeri, yetkili doküman içinse 1 değeri gönderilmelidir. Yine aynı şekilde yalnızca ana aksiyon görüntüleme linki alınmak istendiği durumda fonksiyonID 1 değeri, kalem içinse 2 değeri gönderilmelidir.
	• Aksiyon kalemi için 10.2 numaralı aksiyon kaleminin görüntüleme linki alınacak ise kayitKodu 'na 10.2 gönderilebilir.
	• Eğer bir risk kaydının görüntüleme linkinin alınması bekleniyor ise RDF_NO.RDFD_NO.REV_NO formasında kayitKodu değeri gönderilmelidir. Örneğin RDF_NO 87920, RDFD_NO 6204 ve REV_NO 0 olan bir kayıt için kayitKodu alanından 87920.6204.0 değeri gönderilmelidir.
	• MS modülleri ise web sayfasında görülen kayıt kodu bilgisi gönderilebilir.

	• DÖF, Öneri, Doküman modülleri için direkt olarak kod bilgisi kayitKodu parametresine gönderilebilir.
Task - 62427 -
Talebe istinaden ..BSAT/BSATWebAPI.asmx web servisimize GetLink metodu eklenmiştir.
Metot üzerinden aşağıda bulunan modüllerimizde bulunan kayıtların görüntüleme linkleri alınabilmektedir.
DÖF,
MS,
Öneri,
Aksiyon (Fonk1= Ana Aksiyon, Fonk2=Aksiyon Kalemi),
Doküman (Fonk1= Yetkili Link, Fonk2=Yetkisiz Link),
Risk 
Metot moduleID, fonksiyonID ve kayitKodu parametreleri almaktadır. fonksiyonID parametresi yalnızca Aksiyon ve Doküman modülü üzerinden link alınacağı durumlarda gönderilebilir diğer modüller için ilgili parametre boş gönderilebilir gönderilse dahi metot üzerinde herhangi bir etkisi olmaz. Aksiyon ve Doküman modülleri için gönderilebilecek fonksiyon ID bilgileri yukarıda yer aldığı gibidir yani integer olarak 1 ve 2 değeri gönderilebilir.
Örneğin yetkisiz doküman linki alınmak istenilen durumda fonksiyonID 2 değeri, yetkili doküman içinse 1 değeri gönderilmelidir. Yine aynı şekilde yalnızca ana aksiyon görüntüleme linki alınmak istendiği durumda fonksiyonID 1 değeri, kalem içinse 2 değeri gönderilmelidir.
	• Aksiyon kalemi için 10.2 numaralı aksiyon kaleminin görüntüleme linki alınacak ise kayitKodu 'na 10.2 gönderilebilir.
	• Eğer bir risk kaydının görüntüleme linkinin alınması bekleniyor ise RDF_NO.RDFD_NO.REV_NO formasında kayitKodu değeri gönderilmelidir. Örneğin RDF_NO 87920, RDFD_NO 6204 ve REV_NO 0 olan bir kayıt için kayitKodu alanından 87920.6204.0 değeri gönderilmelidir.
	• MS modülleri ise web sayfasında görülen kayıt kodu bilgisi gönderilebilir.

	• DÖF, Öneri, Doküman modülleri için direkt olarak kod bilgisi kayitKodu parametresine gönderilebilir.


