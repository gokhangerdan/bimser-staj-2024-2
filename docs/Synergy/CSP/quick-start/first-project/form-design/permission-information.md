---
sidebar_label: İzin Bilgileri Bölümü
sidebar_position: 3
custom_edit_url: ""
---

# İzin Bilgileri Bölümü

İzin bilgileri bölümü için forma [Label](ide-objects/form/standart-form-controls/Label.md) nesnesi ile yeni bir bölüm başlığı yazalım.

![İzin Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f53c4ac-1ca9-40c6-9b36-f23cfe9e12dc)

**İzin Başlangıç Tarihi** alanı için forma [DateTimePicker](ide-objects/form/standart-form-controls/DateTimePicker.md) nesnesi eklenir. Varsayılan olarak bugünün tarihi nesnede görünür olsun seçeneğini bu alan için **SetTodayAsDefault** özelliğini aktif ederek gerçekleştirebiliriz.

![İzin Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f2b3cf3-d874-4541-ac32-deb8d3ac4650)

**İşe Dönüş Tarihi** alanı için forma bir başka [DateTimePicker](ide-objects/form/standart-form-controls/DateTimePicker.md) nesnesi ekliyoruz.

![İzin Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8cc19801-57f6-419d-91e9-00d6eeac7348)

**Vekalet Eden Kullanıcı** alanında, izin süresince izne çıkan kullanıcının yerine bakacak kullanıcı, sistemde tanımlı mevcut kullanıcılar arasından seçilecektir. Bu durumda sistemde tanımlı tüm kullanıcıları getiren bir sorguya ihtiyaç duyulur.

Geliştirme arayüzünde Menü Yapısında bulunan **Araçlar** başlığı altında **Bağlantılar** bölümü bulunur. Bağlantılar bölümünde, dış kaynaklardan veri çekip proje içerisinde kullanmak üzere farklı tipte bağlantı bilgileri tanımlanır. Örnek uygulamada, mevcut veritabanına bağlanmak için gerekili olan bilgiler, “PREDEVDB” isimli bağlantı kaydında tanımlanmıştır. Süreçte bu bağlantı tanımı üzerinden veritabanına bağlantı sağlanacaktır.

:::info

Siz, veri çekmek için kullanacağınız bağlantı tipine ve kendi kaynak bilgilerinize göre bağlantı oluşturup projenizde, sisteminize ait oluşturduğunuz bağlantı tanımlarını kullanmalısınız.

:::

![İzin Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf0d457bf-b557-45e8-bb59-92b100068ec8)

Projeye yeni bir veri kaynağı eklemek için, proje yapısının altındaki **Veri Kaynağı (DataSource)** kısmına sağ tıklanır ve **“Yeni Öğe”** seçeneği seçilir. Yeni Öğe seçeneğine tıklandığında verinin çekileceği kaynak yapı tipi seçilir ve oluşturulacak sorguya bir isim verilir.

![İzin Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5120cc2-5106-498b-bb0f-30313e3ee63b)

Sorgu tipi ve adı girilip, “Tamam” butonuna tıklandığında, ilgili sorgu oluşturulup, ekrana sorgu penceresi açılır. Özellik Görüntüleyici panelinde ise sorgunun,  açıklamasının girilebileceği **Açıklama** alanı, sorgunun hangi bağlantı kaynağından çekileceğinin seçiminin yapıldığı **Bağlantı** alanı, **Çalışma Tipi** ve **Komut Tipi** alanları yer almaktadır. Bu alanlar, hazırlanacak sorguya göre doldurulur.

![İzin Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04a94fe5-8e59-4499-90bf-852b27237cc2)

Açılan sorgu ekranına, kullanıcıların sistemde tutulduğu veritabanı tablosundan kullanıcı bilgilerini çeken bir sorgu yazılır ve ekranın üzerindeki **Çalıştır** butonuna basılır. Bağlantı bilgilerinde ya da sorguda bir hata yoksa, yazılan sorgu çalıştırılarak sonuçlar, ekranın altındaki **Sütunlar** ve **Sonuç** sekmelerine dolacaktır.

![İzin Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada6529ac6-7cb0-4d06-add4-d16dcc8d3f7f)

Şimdi yapılması gereken, sorguyla çektiğimiz kullanıcıları formdaki **“Vekalet Eden Kullanıcı”** alanında göstermek ve uç kullanıcının bu liste içerisinden bir kullanıcı seçmesini sağlamaktır. Böyle bir yapı için [ComboBox](ide-objects/form/standart-form-controls/ComboBox.md) nesnesi kullanılır. Combobox nesnesinin özelliklerindeki **Veri Kaynağı (DataSource)** alanında, Tip olarak **Dinamik** seçilir. Vari kaynağı kısmında, projeye eklediğimiz sorgu seçilir ve nesnenin görünüm ve değer kısımlarında tutulması istenen kolonlar seçilir. Tüm kullanıcılar arasından aranan kullanıcının hızlı bulunabilmesi için nesne özelliklerindeki **ShowSearch** seçeneği aktif edilebilir.

![İzin Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload279d69ff-e6d3-4ddd-888b-07a5700b0563)

**İletişim Numarası** alanına, uç kullanıcının bir telefon numarası girmesi istenmektedir. Telefon numarası bilgisinin tüm kullanıcılar tarafından, belirlenen bir formatta girilmesi istendiği için, (örn; 0xxx xxx xx xx şeklinde) sabit format yapısı belirleyebileceğimiz **MaskInput** nesnesinin bu alan için kullanımı uygundur.

MaskInput nesnesinin özelliklerindeki **Maske (Mask)** alanına, 0999 999 99 99 formatı tanımlanır. Böylece uç kullanıcıdan 0xxx xxx xx xx yapısıyla bir telefon bilgisi girmesi beklenir.

![İzin Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload725f4a19-7162-4000-a763-ea383469d223)

**Açıklama** alanı, formu dolduran kullanıcının belirtmek istediği bir durum varsa açıklama metni gireceği kısımdır. Girilecek metin uzun olabileceğinden dolayı birden çok satırda gösterimi için bu alanda TextArea nesnesi kullanımı tercih edilmiştir. Tek satırlık bir açıklama girilmesi istenirse TextArea nesnesi yerine TextBox nesnesi de bu alan için kullanılabilir.

![İzin Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb5e6cbf-f5ed-4853-b099-8cc38c53a25e)