---
title: "Adım 6 Projenin Adım Adım Çalıştırılması"
sidebar_position: 6
---

# Projenin Adım Adım Çalıştırılması

Masraf Beyanında bulunacak kullanıcı, web arayüzüne kendi kullanıcı bilgileri ile giriş yaptıktan sonra, Uygulamalar menüsünden, “Masraf Beyan Süreci” başlığına tıklayacaktır.

“Masraf Beyan Süreci” başlığına tıklandığında, geliştirme arayüzünde tasarlanan form ekranı açılır.

Form Bilgileri kısmındaki **“Belge Numarası”** alanına, form gönderildikten sonra sistem tarafından verilen form numarası otomatik atanacaktır. **“Belge Tarihi”** alanında ise formun oluşturulduğu tarih ve saat bilgisi otomatik gösterilir.

Talep Eden Kullanıcı Bilgileri alanında, formu açan kullanıcının **Adı Soyadı** ve **Departman** bilgisi otomatik olarak dolu gelir.

Masraf Beyan bildirecek kullanıcı, “Masraf Detay Bilgileri” kısmındaki Masraf Detayları Tablosundaki **“Ekle”** butonuna tıklar ve sağ tarafta Masraf Detayları Formu açılır. Kullanıcı alanları doldurduktan sonra **“Kaydet”** butonuna tıklar ve girdiği alanlar tabloya kaydedilir.
![uygulama baslatildi](https://docsbimser.blob.core.windows.net/imagecontainer/uygulama%20ilk%20ba%C5%9Flat%C4%B1%C5%9F-9d2ae5c3-dd37-4486-a9e3-a1e78fb204cc.png)

Detay Formundaki Masraf Tipi alanında “Diğer” seçeneği işaretlendiğinde ve açıklama girilmediğinde kullanıcıyı uyarı mesajı gösterilir.
![diger masraf uyari](https://docsbimser.blob.core.windows.net/imagecontainer/diger%20harcama%20uyari-434bc63d-1a9a-483c-a320-acb367a053f5.png)

Kullanıcı ilgili alanları doldurduktan sonra “Gönder” Butonuna tıklar ve form, formu dolduran kullanıcının Amirinin onayına düşer.
![amir onayinda](https://docsbimser.blob.core.windows.net/imagecontainer/amire%20dustu-a6ae8bdb-226f-4ec8-b644-0ff8a553aa78.png)

Formdaki Form Bilgileri ve Talep Eden Bilgileri sistem tarafından atandığı için düzenlenememekte ancak akışı başlatan tarafından doldurulmuş tüm alanlar(Masraf Detay Bilgileri) ise Akışı Başlatanın Amiri tarafından düzenlenebilmektedir.
 Ayrıca Akışı Başlatanın Amiri pozisyonundaki kullanıcı, formu reddedebilir, revizyon talebinde bulunabilir veya onaylayabilir.
 ![amir asamasi](https://docsbimser.blob.core.windows.net/imagecontainer/amir%20asamasi-0d52b44c-86a5-4899-988b-8c9204e5744a.png)

Masraf Tutarı 2000 tl’nin altında olduğu için Form, Amir onayından sonra Akış üzerindeki İK Grubundaki kullanıcılara yönlendirilir.

Senaryo gereği İK Grubunun Form üzerindeki herhangi bir alanda değişiklik yapma yetkisi bulunmamakta ve Form üzerinde sadece Onaylama işlemi gerçekleştirebilmektedir.

İK Grubunda bulunan 2 kullanıcıdan yalnızca birinin onayı gerçekleştiğinde Akış, Muhasebe Departmanında bulunan kullanıcılara ilerler.
![ik grubu](https://docsbimser.blob.core.windows.net/imagecontainer/IKGrubu-f07fff5d-7b23-4111-8b22-d3f99e964c16.png)

Muhasebe Departmanında bulunan kullanıcılar da form üzerinde bir düzenleme yetkisini sahip değildir yalnızca formu onaylayabilmektedirler.
![muhasebe](https://docsbimser.blob.core.windows.net/imagecontainer/muhasebedep-ac7d81c9-bb03-4e90-866c-9d16a0ae7013.png)

Muhasebe Departmanında bulunan kullanıcılardan yalnızca bir kişinin formu onaylaması akışın ilerlemesi için yeterlidir. Onay verildikten sonra ise Akışı Başlatan kişiye, sürecin tamamlandığına dair bir bilgilendirme maili iletilir ve Süreç tamamlanır.
![ilk senaryo akis tarihcesi](https://docsbimser.blob.core.windows.net/imagecontainer/ilk%20senaryo%20akis%20tarihcesi-f806a6b0-7604-4149-acc5-d7565d1d832c.png)

Diğer bir senaryoda ise Akışı Başlatan Masraf tutarı 2000 tl’den büyük olacak şekilde formu doldurur ve gönderir.
![masraf tutari 2000 den buyuk](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20tutari%202000den%20buyuk-53962fec-a81b-4c30-a3ae-681c49fbd55e.png)

Akışı Başlatanın Amiri, Revizyon talebinde bulunabilir ve akış tekrar Akışı Başlatan kullanıcıya geri döner.
![amir revizyon talebi](https://docsbimser.blob.core.windows.net/imagecontainer/amir%20revizyon%20talebi-cce42e61-cadb-4ae5-9bca-9d9df9b77203.png)

Akışı başlatan kullanıcı revizyon sebebinde girilen açıklamaya göre formu düzenler ve tekrar Amir onayına gönderir.Form, Amir onayından da geçtikten sonra Departman Yöneticisinin onayına düşer.

Departman Yöneticisi, Form üzerinde düzenleme yapabilir. Formu, onaylayabilir veya reddedebilir.
![dep yonetici](https://docsbimser.blob.core.windows.net/imagecontainer/departman%20yoneticisi-a5ee4604-078d-492f-87d3-b19f98324c3d.png)

Red sonucunda kullanıcıya bir bilgilendirme mesajı gönderilir ve Akış biter. Onaylama sonrasında ise form tekrar İK Grubunun onayına düşer.
![dep yonetici onayi sonrasi](https://docsbimser.blob.core.windows.net/imagecontainer/dep%20yonetici%20onayi%20sonrasi-7c8320a1-4a81-4e4d-a9f9-be4f2a7bb76e.png)

İk Grubu ve Muhasebe departmanının da formu onaylamasının ardından Akışı Başlatan Kullanıcıya bilgilendirme maili gönderilir ve Süreç Tamamlanır.
![2.surec tamamlandi akis tarihcesi](https://docsbimser.blob.core.windows.net/imagecontainer/son%20adim-557def7f-25ad-4094-a13c-00ad4c90ed9b.png)

