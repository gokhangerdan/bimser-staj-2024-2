---
sidebar_label: Kullanıcı Grupları
sidebar_position: 6
custom_edit_url: ""
---

# Kullanıcı Grupları

Yetki tanımlamalarında veya akış tasarımı esnasında kullanılmak üzere, belirli bir özellik baz alınarak kullanıcı grupları oluşturulabilir.

Örneğin; bir projenin akışının belirli bir adımında kontrol grubu olarak sistemde tanımlı 3 kullanıcının aksiyonuna ihtiyaç duyuluyor. Bu durumda akışa sabit Pozisyon nesneleri ekleyip bu 3 kullanıcıyı ilgili pozisyon nesnelerinde tanımlamaktansa, “Kullanıcı Grupları” kısmından bu 3 kişinin içinde olduğu bir kullanıcı grubu kaydı oluşturulur ve akışın ilgili adımında aksiyon bu kullanıcı grubuna düşürülür. Böylece kontrol grubu yapısına yeni bir kullanıcı ekleneceği zaman veya var olan bir kullanıcı bu gruptan çıkarılacağı zaman, akış dizaynına müdahale etmektense direk ilgili Kullanıcı Grubu kaydında düzenleme yapılarak yönetilebilirlik artırılmış olur.

Başka bir örnek olarak; uygulama menüsüne eklenmiş bir projeyi veya raporu sadece belirli kişilerin görebilmesi istendiğinde, yine bu kişileri barındıran bir kullanıcı grubu oluşturulup, ilgili menü düğümlerinin yetkisi tek tek kullanıcılara verilmektense direkt olarak gruba verilir. Böylece gruba dahil olan kullanıcılar, gruba verilen yetkilerden otomatik olarak yararlanmış olacaktır.

Mevcut kullanıcı gruplarının listesine ve bu kullanıcı gruplarına ait detay bilgilere, “Kullanıcı Grupları” başlığı altından erişilir.

Sisteme yeni bir **[kullanıcı grubu ekleme](#yeni-kullanıcı-grubu-ekleme)**, mevcut **[kullanıcı grubu bilgilerini görüntüleme](#kullanıcı-grubu-bilgilerinin-görüntülenmesi)** veya **[kullanıcı grubu bilgilerinde değişiklik](#kullanıcı-grubu-bilgilerinin-düzenlenmesi)** yapma işlemleri de yine bu başlık altından yürütülmektedir.

Kullanıcı Grupları başlığına tıklandığında açılan panelde, sistemde tanımlı tüm kullanıcı grupları listelenir.

Bu kullanıcı grubu listesi yapısının kolonları sıralanabilir, kayıtlar içerisinde filtreleme yapılabilir, mevcut kaydın detaylarına girilebilir, yeni kullanıcı grubu eklenebilir veya mevcut bir kayıt değiştirilebilir.

<div style={{textAlign: 'center'}}>

![Kullanıcı Grupları](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4c57cf8-6e94-43b7-b1ab-5464ee92808c)

</div>

## Yeni Kullanıcı Grubu Ekleme

Kullanıcı Gruplarının listelendiği ekranda, sol üst köşede **“Yeni”** isimli bir buton bulunmaktadır. Bu buton kullanılarak sisteme yeni bir kullanıcı grubu tanımlanabilir.

![Kullanıcı Grupları](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34c21752-862d-4afb-9427-240df454e8b8)

“Yeni” butonuna tıklandığında ekrana, yeni tanımlanacak kullanıcı grubu bilgilerinin girilmesi için boş bir kullanıcı grubu bilgileri ekranı açılacaktır.

![Kullanıcı Grupları](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e14286d-fa26-4f76-b081-15d5e1e50a92)

Kullanıcı grubu bilgileri ekranında yer alan alanlar ve bu alanların açıklamaları aşağıdaki gibidir;

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| Grup Kodu 	| Oluşturulacak grubun id bilgisi 	|
| Açıklama 	| Grup açıklamasının girileceği alan 	|
| Durum 	| Grubun sistemdeki durumunun belirtildiği alandır. Aldığı değerler;<br/>**Aktif :** Kullanıcı grubu aktiftir. Sistemde aktif olarak işlem yapabilmekte olan güncel bir kullanıcı grubudur<br/>**Pasif :** Kullanıcı grubu pasiftir. Artık kullanılmayan bir grup olarak değerlendirilip sistemde aktif rol oynayamaz 	|
| Aktarım Durumu 	| Kullanıcı grubunun sisteme harici HR uygulamalarından aktarılma durumunu belirtir. Aldığı değerler;<br/>**Aktif :** Kullanıcı grubu sisteme HR uygulaması ile aktarılıyor demektir<br/>**Pasif :** Kullanıcı grubu sisteme HR uygulaması ile aktarılmıyor, manuel yönetiliyor demektir 	|
|  	| Eğer organizasyonda çoklu şirket yapısı mevcutsa, sistemde tanımlı tüm şirketler bu alanda listelenir, grubun dahil olduğu şirket bilgisi buradan seçilir 	|
|  	| Eğer, kullanıcı grubu için tanımlı [“Grup Özellikleri”](./property-definitions/user-group-properties.md) mevcutsa, kullanıcı grubu özellikleri burada listelenir ve eklenecek kullanıcı grubunun özellik verileri bu alanda girilir 	|
| Gruptaki Kullanıcılar 	| Gruba eklenecek kullanıcıların seçiminin yapıldığı kısımdır. Burada sistemde tanımlı tüm kullanıcılar listelenir, gruba dahil edilmek istenen kullanıcılar bu listeden seçilir. 	|

Yeni kullanıcı grubunun, grup bilgileri ekranında bulunan değerleri girilir ve ardından ekranın üstünde bulunan “Kaydet” butonuna basılır. Böylece sisteme yeni bir kullanıcı grubu eklenmiş olur.

![Kullanıcı Grupları](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2a8cbd8-783c-4c33-bbac-6a72c39e9507)

<div style={{textAlign: 'center'}}>

![Kullanıcı Grupları](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeca0ee0f-270d-4b6d-80a6-e5aad2602ca3)

</div>

Yeni kullanıcı grubu bilgileri girilip, “Kaydet” butonuna basıldıktan sonra, yeni eklenen kullanıcı grubu, mevcut kullanıcı grubu listesine eklenmiş olur. 

## Kullanıcı Grubu Bilgilerinin Görüntülenmesi

Kullanıcı grubu listesinde bulunan bir kayda tıklandığında, ilgili kaydın, grup bilgilerinin bulunduğu bir ekran açılacaktır.

![Kullanıcı Grupları](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload086a50ea-27c4-42aa-b8c8-ca8b0541d386)

Sistemde tanımlı bir kullanıcı grubunun detay bilgilerine bu şekilde erişilebilir.

## Kullanıcı Grubu Bilgilerinin Düzenlenmesi

Kullanıcı grubu listesinden, bilgileri düzenlenmek istenen grubun satırına tıklandığında, ilgili grup bilgilerinin bulunduğu ekran açılacaktır.

Kullanıcı grubu bilgileri ekranında herhangi bir değişiklik yapıldıktan sonra, ekranın üst tarafında bulunan “Kaydet” butonuna basılarak, bilgilerin güncellenmesi sağlanır.

Mevcut kayıt;

<div style={{textAlign: 'center'}}>

![Kullanıcı Grupları](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd414c90-ffbe-485b-8c7b-891911f378e2)

</div>

Gruptan “duyar” kullanıcı adına sahip kayıt çıkarılıp yerine “ademir” kullanıcı adına sahip başka bir kullanıcı ekleniyor;

![Kullanıcı Grupları](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload993e6c98-f9d4-4c83-a136-ac111b2ce07a)

Değişiklik kaydediliyor;

<div style={{textAlign: 'center'}}>

![Kullanıcı Grupları](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf20e4da3-8b55-4ad5-a0b6-e8a77841090b)

</div>

## En İyi Uygulama

:::tip DOĞRU KULLANIM

- Her kullanıcı grubunu temsil eden kullanıcı id bilgisi benzersiz olmalıdır

::: 