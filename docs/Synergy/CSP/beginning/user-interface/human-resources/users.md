---
sidebar_label: Kullanıcılar
sidebar_position: 1
custom_edit_url: ""
---

# Kullanıcılar

Organizasyonun sahip olduğu personeller ve bu personellerin bilgileri genel olarak, organizasyonun insan varlıklarını oluşturur. Organizasyonun barındırdığı tüm insan varlığı, bu başlık altında tutulur ve yönetilir.

Her kullanıcının, şirket içerisindeki tanımı, görevi, yetkisi, organizasyon yapısı içerisindeki konumu ve yürüttüğü işlem adımları mevcuttur. Sistem içerisinde tüm bu bilgilerin yönetilebilmesi, değerlendirilebilmesi ve takip edilebilmesi için kullanıcı bilgilerine ihtiyaç vardır.

Kullanıcıların sisteme giriş yapabilmeleri, iş süreçlerini yürütebilmeleri, kullanıcı bazlı performans değerlendirme verilerinin alınabilmesi, kullanıcılar arası vekalet verilebilmesi ve iş atama işlemlerinin yapılabilmesi, kullanıcı bazlı rol ve yetki tanımlarının belirlenebilmesi gibi birçok aksiyon adımı sistemdeki kullanıcı tanımları üzerinden gerçekleştirilir.

Mevcut kullanıcıların listesine ve bu kullanıcılara ait detay bilgilere, “Kullanıcılar” başlığı altından erişilir.

Sisteme yeni bir **[kullanıcı ekleme](#yeni-kullanıcı-eklenmesi)**, mevcut **[kullanıcı bilgilerini görüntüleme](#kullanıcı-bilgilerinin-görüntülenmesi)** veya **[kullanıcı bilgilerinde değişiklik](#kullanıcı-bilgilerinin-düzenlenmesi)** yapma işlemleri de yine bu başlık altından yürütülmektedir.

Kullanıcılar başlığına tıklandığında açılan panelde, sistemde tanımlı tüm kullanıcılar listelenir.

Bu kullanıcı listesi yapısının kolonları sıralanabilir, kayıtlar içerisinde filtreleme yapılabilir, mevcut kaydın detaylarına girilebilir, yeni kullanıcı eklenebilir veya mevcut bir kayıt değiştirilebilir.

<div style={{textAlign: 'center'}}>

![Kullanıcılar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7030bda1-7a07-4e8c-8754-44365e9abb33)

</div>

## Yeni Kullanıcı Eklenmesi
Kullanıcıların listelendiği ekranda, sol üst köşede **“Yeni”** isimli bir buton bulunmaktadır. Bu buton kullanılarak sisteme yeni bir kullanıcı tanımlanabilir.

![Kullanıcılar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f25bfd7-924d-4ce0-b967-fbe9ab6cb13e)

“Yeni” butonuna tıklandığında ekrana, yeni tanımlanacak kullanıcıların bilgilerinin girilmesi için boş bir kullanıcı bilgileri ekranı açılacaktır.

![Kullanıcılar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe1cf901-d232-41af-999c-eee1195f4d84)

Kullanıcı bilgileri ekranında yer alan alanlar ve bu alanların açıklamaları aşağıdaki gibidir;

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Kullanıcı Adı 	| Kullanıcının sistemdeki id bilgisi 	|
| Adı 	| Kullanıcının adı 	|
| Soyadı 	| Kullanıcının soyadı 	|
| Şifre 	| Kullanıcının sistemdeki şifre bilgisi 	|
| E-posta 	| Kullanıcının elektronik posta adresi 	|
| Departman 	| Kullanıcının dahil olduğu departman bilgisi 	|
| Meslek 	| Kullanıcının ünvanı 	|
| Durum 	| Kullanıcının sistemdeki durumunu belirtir. Aldığı değerler;<br/>**Aktif :** Kullanıcı aktiftir. Sistemde aktif olarak işlem yapabilmekte olan güncel bir kullanıcıdır<br/>**Pasif :** Kullanıcı pasiftir. Sistemde aktif olarak işlem yapamaz<br/>**Geçici Pasif :** Sisteme giriş yaparken 3 kez yanlış şifre girildiğinde, kullanıcının kilitlendiği durumdur 	|
| Aktarım Durumu 	| Kullanıcının sisteme harici HR uygulamalarından aktarılma durumunu belirtir. Aldığı değerler;<br/>**Aktif :** Kullanıcı sisteme HR uygulaması ile aktarılıyor demektir<br/>**Pasif :** Kullanıcı sisteme HR uygulaması ile aktarılmıyor, manuel yönetiliyor demektir 	|
| Doğum Tarihi 	| Kullanıcının doğum tarihi bilgisi 	|
| İşe Başlama Tarihi 	| Kullanıcının işe başlama tarihi bilgisi 	|
| İşten Ayrılış Tarihi 	| Kullanıcının işten ayrılma tarihi bilgisi 	|
| Kategori 	| Kullanıcının kategori bilgisidir. Aldığı değerler;<br/>**Mavi Yaka**<br/>**Beyaz Yaka** 	|
| Cinsiyet 	| Kullanıcının cinsiyet bilgisidir. Aldığı değerler;<br/>**Bay**<br/>**Bayan** 	|
| Tip 	| Kullanıcının sistemdeki tip bilgisidir. Aldığı değerler;<br/>**Normal :** Normal tipte (Sistem ve Özel olmayan) kullanıcıların tipidir<br/>**Özel :** Sistem içerisinde özel ayrıcalıkları olan kullanıcı tipidir. Admin kullanıcısı özel tipli kullanıcıya örnektir 	|
|  	| Eğer organizasyonda çoklu şirket yapısı mevcutsa, sistemde tanımlı tüm şirketler bu alanda listelenir, kullanıcının dahil olduğu şirket bilgisi buradan seçilir 	|
|  	| Eğer, kullanıcılar için tanımlı [“Kullanıcı Özellikleri”](./property-definitions/user-properties.md) mevcutsa, kullanıcı özellikleri burada listelenir ve eklenecek kullanıcının özellik verileri bu alanda girilir 	|
| Amirler 	| Kullanıcının, sistemdeki amir bilgisinin girildiği alandır. Bir kullanıcının, farklı amir profillerinde birden çok yöneticisi tanımlanabilir. Amirler alanında sistemde tanımlı tüm amir profilleri listelenir, ilgili kullanıcının o profildeki amiri kimse bu alanda listelenen kullanıcı tanımlarından seçimi yapılır. 	|

Yeni kullanıcının, kullanıcı bilgileri ekranında bulunan değerleri girilir ve ardından ekranın üstünde bulunan “Kaydet” butonuna basılır. Böylece sisteme yeni bir kullanıcı eklenmiş olur.

<div style={{textAlign: 'center'}}>

![Kullanıcılar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8af9b91-5be4-4cbf-9982-139aac30a735)

</div>

Yeni kullanıcı bilgileri girilip, “Kaydet” butonuna basıldıktan sonra, yeni eklenen kullanıcı, mevcut kullanıcı listesine eklenmiş olur.

## Kullanıcı Bilgilerinin Görüntülenmesi

Kullanıcı listesinde bulunan bir kayda tıklandığında, ilgili kaydın, kullanıcı bilgilerinin bulunduğu bir ekran açılacaktır.

<div style={{textAlign: 'center'}}>

![Kullanıcılar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde1ee8fe-3bcd-4275-9cb2-0dfceb4caf6e)

</div>

Sistemde tanımlı bir kullanıcının detay bilgilerine bu şekilde erişilebilir.

## Kullanıcı Bilgilerinin Düzenlenmesi

Kullanıcı listesinden, bilgileri düzenlenmek istenen kullanıcının satırına tıklandığında, ilgili kullanıcının bilgilerinin bulunduğu ekran açılacaktır.

Kullanıcı bilgileri ekranında herhangi bir değişiklik yapıldıktan sonra, ekranın üst tarafında bulunan “Kaydet” butonuna basılarak, bilgilerin güncellenmesi sağlanır.

Mevcut kayıt;

![Kullanıcılar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31254b74-b36b-4c0f-b218-83f622e1e23b)

Kullanıcının mesleği değiştiriliyor;

![Kullanıcılar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload480a716b-2382-4dbb-9c43-3421b16fcb0c)

Değişiklik kaydediliyor;

<div style={{textAlign: 'center'}}>

![Kullanıcılar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51f06fb7-fd07-42c0-a6de-c58bf41695e7)

</div>

## En İyi Uygulama

:::tip DOĞRU KULLANIM

Her kullanıcıyı temsil eden kullanıcı id bilgisi benzersiz olmalıdır.

:::

:::danger YANLIŞ KULLANIM

Sistemde bulunan aktif bir kullanıcı işten ayrıldığında, ilgili kullanıcı kaydı sistemden silinmemelidir. Kullanıcının durumu aktiften pasife alınmalıdır

:::