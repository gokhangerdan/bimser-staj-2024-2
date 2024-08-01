---
sidebar_label: Departmanlar
sidebar_position: 3
custom_edit_url: ""
---

# Departmanlar

Departmanlar, organizasyon içerisinde belirli bir işi yapmak üzere ayrıştırılan bölümlerdir. Organizasyon içerisindeki her kullanıcının ait olduğu bir departman mevcuttur. Departmanlar, sistem içerisinde aynı ya da benzer işleri yapan kullanıcıların bulunduğu gruplar olarak düşünülebilir.

İş süreçleri, belirli bir departmanın değerine göre farklı dallara ayrılabilir. Akış içerisindeki kullanıcının departman bilgisine göre farklı akış senaryoları tasarlanabilir veya farklı form görselleri dizayn edilebilir. Aynı departmandaki kişilere iş süreci düşürülmek istendiğinde, ilgili iş adımında tek tek aynı departmanlı kullanıcıları seçmek yerine direkt departman seçilerek, seçilen departmandaki tüm kullanıcılara onay düşürülmesi sağlanabilir.

Departman bazında yetkilendirme işlemi yapılabilir. Belirli bir departmanın, sistemde bir yetkiye sahip olması istendiğinde, o departmanda bulunan kullanıcılara tek tek yetki vermek yerine direkt departmana yetkinin verilmesi gerekir. Böylece departmana yeni bir kullanıcı eklendiğinde, yeni kişi departmanından gelen yetkilere otomatik sahip olmuş olur.

Departman tanımları, sistemde yapılan işlerin, departman bazlı performans değerlendirme analizlerinin yapılabilmesi için de kullanılmaktadır.

Mevcut departmanların listesine ve bu departman tanımlarına ait detay bilgilere, “Departmanlar” başlığı altından erişilebilir.

Sisteme yeni bir **[departman ekleme](#yeni-departman-eklenmesi)**, mevcut **[departman bilgilerini görüntüleme](#departman-bilgilerinin-görüntülenmesi)** veya **[departman bilgilerinde değişiklik yapma](#departman-bilgilerinin-düzenlenmesi)** işlemleri de yine bu başlık altından yürütülmektedir.

Departmanlar başlığına tıklandığında yan panelde, sistemde tanımlı tüm departmanlar listelenir.

Bu departman listesi yapısının kolonları sıralanabilir, kayıtlar içerisinde filtreleme yapılabilir, mevcut kaydın detaylarına girilebilir, yeni departman eklenebilir veya mevcut bir kayıt değiştirilebilir.

<div style={{textAlign: 'center'}}>

![Departmanlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4139ae5-c221-422e-93c0-2998103548f9)

</div>

## Yeni Departman Eklenmesi

Departmanların listelendiği ekranda, sol üst köşede “Yeni” isimli bir buton bulunmaktadır. Bu buton kullanılarak sisteme yeni bir departman tanımlanabilir.

![Departmanlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload570e776a-bfcf-479a-9eea-96f7cb198911)

“Yeni” butonuna tıklandığında ekrana, yeni tanımlanacak departmanın bilgilerinin girilmesi için boş bir departman bilgileri ekranı açılacaktır.

![Departmanlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e5b230d-da41-4642-9502-235116fed3aa)

Departman bilgileri ekranında yer alan alanlar ve bu alanların açıklamaları aşağıdaki gibidir;

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Kod 	| Departmanın id bilgisi 	|
| Açıklama 	| Departmanın tanımı, açıklaması 	|
| Yönetici 	| Departmanın yönetici kullanıcısı 	|
| Yönetici Departmanı 	| Üst departman bilgisi 	|
| Durum 	| Departmanın aktif olma durumunu belirtir. Aldığı değerler;<br/>**Aktif :** Departman aktiftir<br/>**Pasif :** Departman pasiftir 	|
| Aktarım Durumu 	| Departmanın sisteme harici HR uygulamalarından aktarılma durumunu belirtir. Aldığı değerler;<br/>**Aktif :** Departman sisteme HR uygulaması ile aktarılıyor demektir<br/>**Pasif :** Departman sisteme HR uygulaması ile aktarılmıyor, manuel yönetiliyor demektir 	|
| Tip 	| Departmanın sistemdeki tip bilgisidir. Aldığı değerler;<br/>**Normal :** Normal tipte (Özel olmayan) departmanlar için kullanılır<br/>**Özel :** Özel tipte kullanıcıların olduğu departmanlar için olup bazı özel işlemleri gerçekleştirmek (daha çok otomatik gerçekleşen işler) için kullanılan departman tipidir 	|
|  	| Eğer organizasyonda çoklu şirket yapısı mevcutsa, sistemde tanımlı tüm şirketler bu alanda listelenir, departmanın dahil olduğu şirket bilgisi buradan seçilir 	|
|  	| Eğer, departmanlar için tanımlı [“Departman Özellikleri”](./property-definitions/department-properties.md) mevcutsa, departman özellikleri burada listelenir ve eklenecek departmanın özellik verileri bu alanda girilir 	|

Yeni departmanın, departman bilgileri ekranında bulunan değerleri girilir ve ardından ekranın üstünde bulunan “Kaydet” butonuna basılır. Böylece sisteme yeni bir departman eklenmiş olur.

<div style={{textAlign: 'center'}}>

![Departmanlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40027de3-afb1-4663-bcd9-27994d400d31)

</div>

Yeni departman bilgileri girilip, “Kaydet” butonuna basıldıktan sonra, yeni eklenen departman, mevcut departman listesine eklenmiş olur.

## Departman Bilgilerinin Görüntülenmesi

Departman listesinde bulunan bir kayda tıklandığında, ilgili kaydın, departman bilgilerinin bulunduğu bir ekran açılacaktır.

![Departmanlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88dbea72-989c-43e2-87a4-c25c44d11248)

Sistemde tanımlı bir departmanın detay bilgilerine bu şekilde erişilebilir.

## Departman Bilgilerinin Düzenlenmesi

Departman listesinden, bilgileri düzenlenmek istenen departmanın satırına tıklandığında, ilgili departmanın bilgilerinin bulunduğu ekran açılacaktır.

Departman bilgileri ekranında herhangi bir değişiklik yapıldıktan sonra, ekranın üst tarafında bulunan “Kaydet” butonuna basılarak, bilgilerin güncellenmesi sağlanır.

Mevcut kayıt;

![Departmanlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab2cb7c4-2b6f-46b4-8a1c-d77803b29ab8)

Departmanın yöneticisi değiştiriliyor;

![Departmanlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7271782-fc3a-4128-8c38-042eafb755fe)

Değişiklik kaydediliyor;

![Departmanlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb14e1a5c-f8ce-4394-9992-c66dee1a2035)

Böylece departmanın yöneticisi değiştirilmiş olur.

## En İyi Uygulama

:::tip DOĞRU KULLANIM

- Sistemde tanımlı her departman kaydının departman id bilgisi benzersiz olmalıdır

:::

:::danger YANLIŞ KULLANIM

- Mevcut bir departman kapatıldığında sistemde tanımlı kaydı silinmemelidir. Departman kaydının durumu aktiften pasife alınmalıdır

:::