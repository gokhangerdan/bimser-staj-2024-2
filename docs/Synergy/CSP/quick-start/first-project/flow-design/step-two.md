---
sidebar_label: İkinci Adım
sidebar_position: 2
custom_edit_url: ""
---

# İkinci Adım

Akışı başlatan kullanıcı formu doldurup gönderdiğinde akışın, form üzerinde seçilen **“Vekalet Eden Kullanıcı”** alanındaki kişiye düşmesi isteniyor.

Form üzerindeki bir alanın değerini, akış tarafında kullanabilmek için öncelikle formdaki bu alana akış ekranında erişmemiz gerekir. Bu gibi durumlarda akış nesnelerinden **Değişken (Variable)** nesnesi kullanılır. Değişken nesnesi, akış ekranına eklenerek, özelliklerindeki;

- **Kaynak Doküman** alanından, hangi form üzerindeki veriye akış tarafında erişilmek isteniyorsa o formun bağlandığı Doküman nesnesi,

- **Kaynak Nesne** alanından ise seçilen form üzerindeki nesnelerden hangisinin verisi bu değişkende tutulmak isteniyorsa o form nesnesinin seçimi yapılmalıdır.

![İkinci Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bf6c151-dfab-4303-9b7c-569ba627d7eb)

Form üzerindeki Combobox nesnesinde seçilen kişiye, akış tarafında onay düşürebilmek için kişi bilgisini akıştaki değişken nesnesinde tuttuk. Şimdi bu kişi bilgisini akıştaki bir onay pozisyonuna atamamız gerekiyor. Bu işlem için, akışı başlatan nesnesinin “Gönder” aksiyon kolundan sonra bir **Atama (Assignment)** nesnesi, Atama nesnesinden sonra da bir **Pozisyon (Position)** nesnesi akışa yerleştirilir.

![İkinci Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3269ea62-b944-4a15-921e-56506b7c6763)

Atama nesnesi ile, Değişken nesnesinde tutulan kişi bilgisi, Pozisyon nesnesine atanacaktır. Bu doğrultuda Atama nesnesinin özelliklerinde;

- **Hedef Nesne** alanında, akıştaki hangi nesneye değer atanacağı seçilir. Bizim örneğimiz için seçilecek nesne atamadan sonra gelen Pozisyon nesnesidir

- **Kaynak Tipi** alanında, atama tipi seçilecektir. Örneğe göre, akıştaki Değişken nesnesinde tutulan değer, Pozisyon nesnesine atanacağı için bu alanda, **“Değişken Değerden Kullanıcı”** seçeneği seçilir

:::info

Form üzerindeki ComboBox nesnesinin değer alanında, Kullanıcı Id bilgisi tutulduğu için **“Değişken Değerden Kullanıcı”** seçiliyor. Bu alanda kullanıcının Pozisyon Id bilgisi tutulsa idi, **“Değişken Değerden Pozisyon”** seçeneği seçilecekti.

:::

- **Öğeyi Seçin** alanında ise, akıştaki hangi değişken nesnesindeki değer atamada kullanılacaksa o Değişken nesnesi seçilir.

![İkinci Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada46bcf17-cce1-4a41-986a-41d17b0fc0c1)

Akış, atama nesnesinden geçtiğinde, Pozisyon nesnesinde artık form üzerinden vekalet için seçilen kullanıcı olacaktır. Bu vekalet kullanıcısı, akışı başlatanın doldurduğu formu görüntüleyip, izin tarihleri süresince uygunsa işlemi onaylayacak, değilse reddederek akışı, akışı başlatana geri gönderecektir.

Öncelikle vekalet kullanıcısının doldurulan formu görebilmesi için, nesne özelliklerindeki **Belge** alanından, ilgili formun bağlı olduğu Doküman nesnesinin seçimi yapılmalıdır. Vekalet kullanıcısı, akışı başlatanın doldurduğu form üzerinde herhangi bir düzenleme yapamamalıdır. Bu yüzden doküman eklerken düzenleme yetkisini bu pozisyon için vermiyoruz.

![İkinci Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c819a73-e105-43ec-b2d2-221ed81cfede)

Senaryoya göre, vekalet eden kullanıcının **“Onayla”** ve **“Reddet”** aksiyon butonlarına sahip olması gerekiyor. Araç Kutusundan sürükle/bırak ile akış ekranına konumlandırılan bir Pozisyon nesnesinin olayları, varsayılan olarak “Onayla” ve “Reddet” dir. Eğer senaryoya göre farklı bir aksiyona sahip olması gerekse idi, bu değişiklik, pozisyon nesnesinin özelliklerindeki **“Olaylar”** alanından yapılacaktı. Şuan varsayılan olarak gelen olaylar, senaryomuza uygun olduğu için bu alanda bir değişiklik yapmıyoruz.

![İkinci Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09192de2-863c-455c-9557-b82c376f8366)

Pozisyon nesnesine ekli tüm aksiyon tanımları için, nesneden ilgili aksiyona ait ok çıkarılarak, ilgili aksiyonun gerçekleşmesi durumunda akışın nereye yönleneceğinin belirtilmesi gerekir.

Senaryoya göre; vekalet eden kullanıcı, süreci “Onayla” aksiyon butonuna basarak onaylarsa akış, bir sonraki adım olarak akışı başlatanın yöneticisine gönderilmelidir. Akışı başlatan kullanıcı, sistemde tanımlı herhangi bir kullanıcı olabileceği için, kullanıcı yöneticisi pozisyonuna sabit değer ataması yapılamaz. Akışı kim başlattıysa onun yöneticisini bulup, Yönetici pozisyonuna atamak için bu adımda da **Atama** nesnesi kullanılacaktır.

Yani, “Vekalet Kullanıcısı” pozisyon nesnesinden sonra, yönetici ataması yapan bir Atama nesnesi bulunmalıdır. “Vekalet Kullanıcısı” pozisyonunun **“Onayla”** aksiyon oku da bu Atama nesnesine bağlanır.

![İkinci Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload28f50303-c07c-4166-b4e7-e382c2667fc7)

Yine senaryoya göre bu kez “Vekalet Kullanıcısı” nesnesi süreci, “Reddet” aksiyon butonuna basarak reddederse akış, akışı başlatan kullanıcıya geri gönderilecektir. Bu yüzden “Vekalet Kullanıcısı” nesnesinden çıkarılan **“Reddet”** aksiyon oku, Akışı Başlatan nesnesine bağlanır.

![İkinci Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfcb62a8-fd21-40db-af06-b2b8e29fc38f)