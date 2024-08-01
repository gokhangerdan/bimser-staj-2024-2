---
sidebar_label: E-posta Bildirimlerinin Özelleştirilmesi
sidebar_position: 8
custom_edit_url: ""
---


# E-posta Bildirimlerinin Özelleştirilmesi

Şifremi Unuttum Bildirimi
Şifremi Unuttum seçeneği kullanılarak şifre yenileme işlemi aşamasında gönderilen e-postadır. E-posta içeriği DM’de aşağıdaki path’te yer alan şablon dosyası düzenlenerek özelleştirilebilir. İçerikte aşağıdaki değişkenler kullanılmaktadır.
Path
•	Türkçe: system/settings/templates/RememberMeMailTemplate-tr-TR.html
•	İngilizce: system/settings/templates/RememberMeMailTemplate-en-US.html

Değişkenler
•	{{UrlLink}}: Şifre yenileme linki

Aktivite Bildirimi
Aktivite işlemlerinde gönderilen e-postadır. E-posta içeriği DM’de aşağıdaki path’te yer alan şablon dosyası düzenlenerek özelleştirilebilir. İçerikte aşağıdaki değişkenler kullanılmaktadır.
Path
•	system/settings/templates/ActivityMailTemplate.html
Değişkenler
•	{{Message}}: E-posta gövdesi
•	{{Link}}: Aktivite sayfasına erişim linki
•	{{LinkName}}: Linkin görünür adı
•	{{FirstName}}: E-posta gönderilen kişi adı
•	{{LastName}}: E-posta gönderilen kişi soyadı
•	{{Hi}}: Selamlama ifadesi

Dosya Paylaşım Bildirimi
DM’de bir dosya paylaşıldığında paylaşılan kişilere iletilen e-postadır. E-posta içeriği DM’de aşağıdaki path’te yer alan şablon dosyası düzenlenerek özelleştirilebilir. İçerikte aşağıdaki değişkenler kullanılmaktadır.
Path
•	system/settings/templates/ShareMailTemplate_tr-TR.html
•	system/settings/templates/ShareMailTemplate_en-US.html
Değişkenler
•	{{Message}}: E-posta gövdesi

DM Abonelik Bildirimi
DM’de bir dosya için abonelik sürecinde üretilen e-postadır. E-posta içeriği DM’de aşağıdaki path’te yer alan şablon dosyası düzenlenerek özelleştirilebilir. İçerikte aşağıdaki değişkenler kullanılmaktadır.
Path
•	system/settings/templates/SubscriptionMailTemplate.html
Değişkenler
•	{{Message}}: E-posta gövdesi
•	{{Link}}: Dosya erişim linki
•	{{LinkName}}: Link görünür adı
•	{{FirstName}}: E-posta gönderilen kişi adı
•	{{LastName}}: E-posta gönderilen kişi soyadı
•	{{Hi}}: Selamlama ifadesi

Akış Bildirimleri
Süreç akış aşamalarında gönderilen e-postadır. Varsayılan e-posta içeriği DM’de aşağıdaki path’te yer alan şablon dosyası düzenlenerek özelleştirilebilir. 
Path
•	System\settings\templates\FlowMailTemplate.html
Değişkenler
•	{{Message}}: E-posta gövdesi
•	{{Link}}: Dosya erişim linki
•	{{LinkName}}: Link görünür adı
•	{{FirstName}}: E-posta gönderilen kişi adı
•	{{LastName}}: E-posta gönderilen kişi soyadı
•	{{Hi}}: Selamlama ifadesi
•	{{FlowInitiatorFirstName}}: Akışı başlatan kişi adı
•	{{FlowInitiatorLastName}}: Akışı başlatan kişi soyadı
•	{{ProcessCaption}}: Süreç adı
•	{{ProcessId}}: Süreç belge no
Ayrıca akış özelinde Bilgilendirme, Pozisyon, Pozisyon Grubu gibi e-posta gönderiminin yapıldığı nesnelerde e-posta içeriği özelleştirilebilmektedir. 
Bunun için, akışta nesnelerde Özellik Görüntüleyici penceresinde Edit Message Source seçeneği aktif edilmelidir. Özellik aktif edildiğinde e-posta içeriğinin düzenlenmesi için Source Message alanı açılmaktadır. Bu alana tıklandığında sistemde akış e-posta şablon dosyasının düzenlenebileceği pencere açılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/mail1-a1cd218e-83b3-4de9-8465-49bdb722616e.png)

Bu ekranda e-posta şablonu düzenlenerek akışta gönderilecek e-posta özelleştirilebilir. Gönderilecek e-posta yapısı Önizleme sekmesinden görüntülenebilir. Ayrıca dil seçimi alanından farklı dillerde gönderilecek e-posta içerikleri de özelleştirilebilmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/mail2-f05b313a-e33a-4db8-bae7-41ab3155b71c.png)
