---
sidebar_label: Pozisyonlar
sidebar_position: 2
custom_edit_url: ""
---

# Pozisyonlar

Pozisyon kavramını, kullanıcıların şirket içerisindeki koltukları olarak düşünebiliriz. Kullanıcılar, bu pozisyon koltuklarına oturan kişilerdir. Bir kullanıcı işten ayrıldığında ya da kullanıcının pozisyonu değiştiğinde, mevcut pozisyon koltuğu sabit kalır. O pozisyondan giden kullanıcı yerine, pozisyon koltuğuna başka bir kullanıcı oturur. Yani pozisyon, organizasyonun belirlediği görev tanımını yerine getiren personelin konumudur.

Sistem içerisindeki iş akışları, kullanıcılar üzerinden yürütülebildiği gibi, pozisyonlar üzerinden de yürütülebilir. Bir onay adımında, o onay adımına bir pozisyon tanımlanmışsa işlemler, ilgili pozisyondaki kullanıcı üzerinden, pozisyon bazlı yürütülmüş olur. Bu durumda iş akışları, sabit kullanıcı bağımlılığından kurtulur, pozisyonda hangi kullanıcı tanımlı ise işlemler o kullanıcı üzerinden ilerler. Burada asıl önemli olan işi yapan pozisyondur.

Bir kullanıcının birden fazla pozisyon tanımı olabilir. Böyle bir durumda akış adımlarında, kullanıcı bazlı değil, pozisyon bazlı atamalar yapılması, aynı kişinin farklı pozisyonlarına ait, farklı görevlerini yürütebilmesine ve süreçlerde alınan aksiyonların, aksiyon alınan pozisyon bazlı değerlendirilebilmesine imkan sağlar.

Mevcut pozisyonların listesine ve bu pozisyon tanımlarına ait detay bilgilere, “Pozisyonlar” başlığı altından erişilebilir.

Sisteme yeni bir **[pozisyon ekleme](#yeni-pozisyon-eklenmesi)**, mevcut **[pozisyon bilgilerini görüntüleme](#pozisyon-bilgilerinin-görüntülenmesi)** veya **[pozisyon bilgilerinde değişiklik](#pozisyon-bilgilerinin-düzenlenmesi)** yapma işlemleri de yine bu başlık altından yürütülmektedir.

Pozisyonlar başlığına tıklandığında açılan panelde, sistemde tanımlı tüm pozisyonlar listelenir.

Bu pozisyon listesi yapısının kolonları sıralanabilir, kayıtlar içerisinde filtreleme yapılabilir, mevcut kaydın detaylarına girilebilir, yeni pozisyon eklenebilir veya mevcut bir kayıt değiştirilebilir.

<div style={{textAlign: 'center'}}>

![Pozisyonlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13d95e1e-d4dc-4347-9979-53cec5103a94)

</div>

## Yeni Pozisyon Eklenmesi

Pozisyonların listelendiği ekranda, sol üst köşede “Yeni” isimli bir buton bulunmaktadır. Bu buton kullanılarak sisteme yeni bir pozisyon tanımlanabilir.

![Pozisyonlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload218344d5-5f0d-4a5e-acb3-80a406d87579)

“Yeni” butonuna tıklandığında ekrana, yeni tanımlanacak pozisyonun bilgilerinin girilmesi için boş bir pozisyon bilgileri ekranı açılacaktır.

![Pozisyonlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade53d9f46-60d3-4c57-8c6f-1ddbe4cd8b1e)

Pozisyon bilgileri ekranında yer alan alanlar ve bu alanların açıklamaları aşağıdaki gibidir;

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Kod 	| Pozisyonun id bilgisi 	|
| Açıklama 	| Pozisyonun tanımı, açıklaması 	|
| Kullanıcı 	| Pozisyonun kullanıcısı 	|
| Durum 	| Pozisyonun aktif olma durumunu belirtir. Aldığı değerler;<br/>**Aktif :** Pozisyon aktiftir. Sistemde aktif olarak işlem yapabilmekte olan güncel bir pozisyondur<br/>**Pasif :** Pozisyon pasiftir. Sistemde aktif olarak işlem yapamaz 	|
| Aktarım Durumu 	| Pozisyonun sisteme harici HR uygulamalarından aktarılma durumunu belirtir. Aldığı değerler;<br/>**Aktif :** Pozisyon sisteme HR uygulaması ile aktarılıyor demektir<br/>**Pasif :** Pozisyon sisteme HR uygulaması ile aktarılmıyor, manuel yönetiliyor demektir 	|
| Aktarılmış Pozisyon Kodu 	| Eğer pozisyon, harici HR uygulamasından aktarılıyor ise ve HR kaynağında farklı bir id bilgisine sahip ise kaynaktaki id bilgisi bu alanda belirtilir 	|
| Tip 	| Pozisyonun sistemdeki tip bilgisidir. Aldığı değerler;<br/>**Normal :** Normal tipte (Sistem ve Özel olmayan) pozisyonların tipidir<br/>**Özel :** Bir insan pozisyonu olmayıp bazı özel işlemleri gerçekleştirmek (daha çok otomatik gerçekleşen işler) için kullanılan pozisyon tipidir 	|
|  	| Eğer organizasyonda çoklu şirket yapısı mevcutsa, sistemde tanımlı tüm şirketler bu alanda listelenir, pozisyonun dahil olduğu şirket bilgisi buradan seçilir 	|
|  	| Eğer, pozisyonlar için tanımlı [“Pozisyon Özellikleri”](./property-definitions/position-properties.md) mevcutsa, pozisyon özellikleri burada listelenir ve eklenecek pozisyonun özellik verileri bu alanda girilir 	|

Yeni pozisyonun, pozisyon bilgileri ekranında bulunan değerleri girilir ve ardından ekranın üstünde bulunan “Kaydet” butonuna basılır. Böylece sisteme yeni bir pozisyon eklenmiş olur.

<div style={{textAlign: 'center'}}>

![Pozisyonlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7f76073-b5c5-4b34-99e7-7c120b2c271c)

</div>

Yeni pozisyon bilgileri girilip, “Kaydet” butonuna basıldıktan sonra, yeni eklenen pozisyon, mevcut pozisyon listesine eklenmiş olur.

## Pozisyon Bilgilerinin Görüntülenmesi

Pozisyon listesinde bulunan bir kayda tıklandığında, ilgili kaydın, pozisyon bilgilerinin bulunduğu bir ekran açılacaktır.

![Pozisyonlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d4e8831-692e-4134-8fc2-4312ff92cd0c)

Sistemde tanımlı bir pozisyonun detay bilgilerine bu şekilde erişilebilir.

## Pozisyon Bilgilerinin Düzenlenmesi

Pozisyon listesinden, bilgileri düzenlenmek istenen pozisyonun satırına tıklandığında, ilgili pozisyonun bilgilerinin bulunduğu ekran açılacaktır.

Pozisyon bilgileri ekranında herhangi bir değişiklik yapıldıktan sonra, ekranın üst tarafında bulunan “Kaydet” butonuna basılarak, bilgilerin güncellenmesi sağlanır.

Mevcut kayıt;

![Pozisyonlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53fb2379-2beb-48e2-87e0-8acccb7f2ac6)

Pozisyona tanımlı kullanıcı değiştiriliyor;

![Pozisyonlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload298aa7d3-7259-4e75-961b-a889fd865449)

Değişiklik kaydediliyor;

<div style={{textAlign: 'center'}}>

![Pozisyonlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3536fb0e-02b7-4728-a870-9c2a22395275)

</div>

Böylece pozisyona bağlı kullanıcı bilgisi değiştirilmiş olur.

## En İyi Uygulama

:::tip DOĞRU KULLANIM

- Her kullanıcıyı temsil eden Kod (pozisyon id) bilgisi benzersiz olmalıdır

- Sistemde, her kullanıcının en az bir pozisyon tanımına sahip olması idealdir

- Aynı kullanıcıya ait farklı pozisyon tanımlarında, kullanıcı kodu alanı aynı iken, pozisyon id bilgisi benzersiz olmalıdır

- Aynı pozisyon açıklamasına sahip, birden fazla pozisyon kaydı olabilir. Bu durumda pozisyon kayıtlarının açıklama alanı aynı iken, pozisyon id alanları benzersiz olmalıdır. Yani sistemde, aynı pozisyon açıklamasına sahip farklı pozisyon id li kayıtlar bulunabilir

:::

:::danger YANLIŞ KULLANIM

- Kullanıcıya, sahip olduğu pozisyondan kaynaklı bir yetki verileceği zaman bu yetki, kullanıcı yetkisi olarak verilmemelidir. Kullanıcının pozisyonuna yetki verilmelidir. Böylece pozisyon içindeki kullanıcı tanımı değişse dahi, yetki pozisyona verildiği için, o pozisyona gelen her kullanıcı bu yetkiden otomatikman yararlanmış olur. Pozisyona bağlı kullanıcı değiştiğinde tekrar yetki vermek gerekmez

- Sistemde bulunan aktif bir pozisyon artık kullanılmayacaksa, ilgili pozisyon kaydı sistemden silinmemelidir. Pozisyonun durumu aktiften pasife alınmalıdır

:::