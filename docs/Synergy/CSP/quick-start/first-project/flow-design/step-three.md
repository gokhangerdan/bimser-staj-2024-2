---
sidebar_label: Üçüncü Adım
sidebar_position: 3
custom_edit_url: ""
---

# Üçüncü Adım

Bu adımda akışın, “Vekalet Eden Kullanıcı” onay verdikten sonra, akışı başlatan kişinin yöneticisine düşmesi gerekiyor. Akışı başlatan kullanıcıya göre bu kullanıcının yöneticisi dinamik atanacağı için bir önceki adımda, “Vekalet Eden Kullanıcı” adımından sonra yönetici ataması yapacak bir **Atama** nesnesi koymuştuk. Yönetici ataması yapacak olan Atama nesnesinden sonra da, yöneticinin atanacağı bir **Pozisyon** nesnesi akışa yerleştirilir.

![Üçüncü Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload27246fcb-db34-463a-a7ea-11ce3977e590)

Atama nesnesinde, ikinci eklediğimiz Pozisyon nesnesine, akışı başlatanın yöneticisini atayacağız. Bu yüzden Atama nesnesinin özelliklerindeki;

- **Hedef Nesne** alanında, akıştaki hangi nesneye değer atanacağı seçilir. Bizim örneğimiz için seçilecek nesne atamadan sonra gelen Pozisyon nesnesidir
- **Kaynak Tipi** alanında, atama tipi seçilecektir. Biz yönetici ataması yapacağımız için bu alanda “Kullanıcı Yöneticisi” seçeneği seçilir
- Kaynak tipi olarak yönetici ataması seçtiğimiz için bu seçeneğe özgü Profil isimli bir alan açılacaktır. Profil alanında kişinin hangi yönetici profiline ait yöneticisinin atamada kullanılacağı seçilir.
- **Seçilen Nesne** alanında ise, akıştaki hangi nesnenin yöneticisinin atanacağı seçimi yapılır. Senaryoya göre akışı başlatan kullanıcının yöneticisi atanacaktır. Araç kutusundan sürükle-bırak ile akışa yerleştirilen pozisyon nesnelerinde, varsayılan kullanıcı Akışı Başlatan kullanıcısıdır. Yönetici ataması yapılacak pozisyon nesnesi de forma ilk eklendiğinde, herhangi bir değişiklik yapılmamışsa akışı başlatan kişiyi değer olarak tutar. Bu yüzden “Seçili Nesne” alanında, yönetici atanacak aynı pozisyon nesnesinin seçimini yapabiliriz.

![Üçüncü Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68d4643a-a9ac-4ca1-9c81-5bbaad3c23f5)

Akış “Yönetici Ata” atama nesnesinden geçtiğinde, akışı başlatanın yöneticisi bir sonraki pozisyon nesnesine atanmış olacaktır.

Yönetici, izin talep eden kişinin doldurduğu formu görüp, uygunsa izni onaylayarak bir sonraki adıma akışı ilerletecek, uygun değilse reddederek akışı, akışı başlatana geri gönderecektir.

Öncelikle yöneticinin, doldurulan formu görebilmesi için, nesne özelliklerindeki **Belge** alanından, ilgili formun bağlı olduğu Doküman nesnesinin seçimi yapılmalıdır. Yönetici, akışı başlatanın doldurduğu form üzerinde herhangi bir düzenleme yapamamalıdır. Bu yüzden doküman eklerken düzenleme yetkisini bu pozisyon için vermiyoruz.

![Üçüncü Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9412a2e-dfb1-4e50-8454-02eebd0c1c38)

Senaryoya göre, yönetici kullanıcının **“Onayla”** ve **“Reddet”** aksiyon butonlarına sahip olması gerekiyor. Araç Kutusundan sürükle/bırak ile akış ekranına konumlandırılan bir Pozisyon nesnesinin olayları, varsayılan olarak “Onayla” ve “Reddet” dir. Eğer senaryoya göre farklı bir aksiyona sahip olması gerekse idi, bu değişiklik, pozisyon nesnesinin özelliklerindeki **“Olaylar”** alanından yapılacaktı. Şuan varsayılan olarak gelen olaylar, senaryomuza uygun olduğu için bu alanda bir değişiklik yapmıyoruz.

![Üçüncü Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload374b10ea-1b70-4852-a988-d99ebc5b5d3c)

Pozisyon nesnesine ekli tüm aksiyon tanımları için, nesneden ilgili aksiyona ait ok çıkarılarak, ilgili aksiyonun gerçekleşmesi durumunda akışın nereye yönleneceğinin belirtilmesi gerekir.

Senaryoya göre; Yönetici, süreci “Onayla” aksiyon butonuna basarak onaylarsa akış, bir sonraki adım olarak İnsan Kaynakları Departmanı’na gönderilmelidir. İnsan Kaynakları Departmanı’nda bulunan tüm kullanıcılara (birden fazla kullanıcı) aynı anda süreci yönlendirmek için, bu adımda kullanılması gereken nesne, **Pozisyon Grubu (Position Group)** nesnesidir. Pozisyon grubuna IK departmanı tanımlandığında, o departmanda kaç tane kullanıcı varsa otomatik olarak gruba dolmuş olacaktır.

Yani, “Yönetici” pozisyon nesnesinden sonra akışa, IK departmanı kullanıcılarını dolduracağımız bir Pozisyon Grubu nesnesi koyuyoruz. “Yönetici” pozisyonunun **“Onayla** aksiyon okunu da bu Pozisyon Grubu nesnesine bağlıyoruz.

![Üçüncü Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8cc6afc-4dee-42a0-9de7-1f885e0d92eb)

Yine senaryoya göre bu kez “Yönetici” nesnesi süreci, “Reddet” aksiyon butonuna basarak reddederse akış, akışı başlatan kullanıcıya geri gönderilecektir. Bu yüzden “Yönetici” nesnesinden çıkarılan **“Reddet”** aksiyon oku, Akışı Başlatan nesnesine bağlanır.

![Üçüncü Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7c18239-2bbb-4105-a7af-b55046b53645)