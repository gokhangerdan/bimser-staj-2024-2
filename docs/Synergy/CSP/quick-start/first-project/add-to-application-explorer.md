---
sidebar_label: Adım 5 Projeyi Uygulamalar Menüsüne Ekleme
sidebar_position: 5
custom_edit_url: ""
---

# Projeyi Uygulamalar Menüsüne Ekleme

Projenin, uç kullanıcılar tarafından kullanılabilmesi için, web arayüzünde Uygulamalar listesine eklenmesi gerekir. Yeni uygulama ekleyebilmek için web arayüzüne yetkili bir kullanıcı ile giriş yapılarak, Ayarlar kısmından [Uygulama Gezgini](web/application-explorer.md) başlığına tıklanır.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0116c37-3c58-4da7-90fe-da282b76c73a)

Uygulama Gezgini ekranında bulunan **“Ekle”** seçeneğine tıklanarak uygulamalar menüsüne yeni kayıt eklenir.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71cbc127-b4fb-4bf2-a97c-d10dcd8ac5db)

Ekle seçeneğine tıklandığında ekrana, uygulama detaylarının girileceği pencere açılacaktır. Tüm İnsan Kaynakları süreçlerini, menü de tek bir başlık altında eklemek için öncelikle **“IK Süreçleri”** isimli ana menü başlığını oluşturalım. Bu düğüme tıklandığında herhangi bir form ya da süreç açılmayacak, yalnızca bu düğümün altına eklenen uygulamalar listelenecektir. O yüzden **“Düğüm İşlem Türü”** alanında **“Yok”** seçeneği seçilir. Ve **“Kök Düğüm Ata”** alanı pasif yapılır.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload726e49d0-e929-4a40-bd12-613a1ed8b898)

**“Profiller”** sekmesi açılır. Henüz yeni profil eklenmediği için, varsayılan olarak gelen “admin” isimli profil bu alanda seçilerek **Ekle** butonuna tıklanır.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a1f8f7c-6210-4d03-b7ca-8c77bc73b94b)

“admin” isimli profilde aktif edilen uygulama düğümü, Uygulama Gezgini ekranındaki **“Kaydet”** butonuna basılarak kaydedilir.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e0de797-1852-45e0-9838-1e31b07b66a5)

Oluşturulan “IK Süreçleri” başlığının altına “Yıllık İzin Süreci” projesine ait menü kaydını oluşturmak için, Uygulama Gezgininden tekrar **“Ekle”** butonuna tıklanır. Açılan ekranda;

- **Başlık** kısmına “Yıllık İzin Süreci” yazılır.

- Menüden bu uygulamaya tıklandığında açılacak formun tam ekran açılması için, **Panel Boyutu** alanından **“3”** seçeneği seçilir.

- Menüden bu uygulamaya tıklandığında, geliştirme arayüzünde tasarlanan projenin yeni bir akışı başlatılacağı için **Düğüm İşlem Türü** alanından **“Bir Akış Başlat”** seçeneği seçilir.

- **Projeler** alanından, geliştirme arayüzünde oluşturulan “Yıllık İzin Talep” projesi seçilir.

- **Akışlar** kısmından ise, “Yıllık İzin Talep” sürecinin akışı seçilir.

- **Kök Düğüm Ata** alanı aktif edilerek listeden, az önce oluşturulan “IK Süreçleri” ana düğümü seçilir.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddac474d8-317d-46ba-8775-753819149d2f)

Profiller sekmesinden yine “admin” profili seçilerek, bu uygulama düğümü de admin profilinde aktif edilir. Bu işlem sonrasında, Uygulamalar menüsünde, “IK Süreçleri” başlığı altına “Yıllık İzin Süreci” uygulaması eklenmiş olur. Düzenleme, Uygulama Gezgini ekranından kaydedilmelidir.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0af56d1e-fee1-4ab7-b1de-4ca714966d6e)

Artık, “Yıllık İzin Süreci” isimli uygulama başlığı, “admin” profil yetkisine sahip kullanıcılar tarafından, Uygulamalar menüsünde görüntülenebilir ve tıklandığında süreç başlatılabilir. Bu sürece, yalnızca “admin” profiline sahip kullanıcılar tarafından değil, sistemdeki tüm kullanıcılar tarafından erişilebilmesi için, tüm kullanıcıların yetkilendirileceği **“Tüm Kullanıcılar Profili”** isimli yeni bir menü profili tanımlanmalıdır.

Uygulama Gezgini ekranındaki **Profil** alanından **“Ekle”** butonu ile yeni profil ekleme sayfası açılarak profile isim verilir.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36f02240-999f-4806-99ad-ed029129a2f6)

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload858fdfd5-0046-470e-833d-66da9f048e76)

Yeni profil tanımı eklendikten sonra, **Profil** listesinden bu profil seçildiğinde, uygulama menüsündeki tüm uygulama kayıtları pasif olarak görünür. “IK Süreçleri” ve altındaki “Yıllık İzin Süreci” uygulama başlıkları, bu profilde aktif edileceği için, ikisinin de detaylar kısmından, “Düzenle” butonuna basılır. Profil sekmesi açılarak yeni eklenen, “Tüm Kullanıcılar Profili” de uygulama profillerine eklenir.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81ef0b1a-43b6-4518-a461-726f40cedac6)

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7db6905-cef7-4f34-9bd9-d5bef1c825bd)

İki uygulama başlığı da “Tüm Kullanıcılar Profili” profilinde aktif edildikten sonra, Uygulama Gezgini ekranının detaylarından Kaydet butonu ile profil değişiklikleri kaydedilir. Artık, “Tüm Kullanıcılar Profili” için yetkilendirilen kullanıcılar, bu iki menü başlığını görebilir ve kullanabilir olurlar.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1d6ef9e-bcc6-4737-8f43-9fbc2047edd7)

Menü profili de oluşturulduktan sonra sıra, menü profilini sistemdeki tüm kullanıcılara yetkilendirmeye gelmiştir. Bunun için, web arayüzüne yetkili bir kullanıcı ile giriş yapılır. Ayarlar kısmından **Güvenlik** menüsüne tıklanır.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5bcba32a-4195-4c5e-ac9e-67dd13c7ca24)

Güvenlik ekranınaki **“Grup Ekle”** butonuna tıklanarak, oluşturulacak gruba bir isim ve açıklama girilir.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cb56223-d49d-4380-bfcf-8adf8492afb9)

Yeni grup tanımı, grup listesine eklenmiş olarak görünür. Bu grup tanımına tıklandığında sağ taraftaki **“Üyeler”** sekmesine gelinir. **“Ekle”** butonu ile gruba, **“everyone”** kullanıcı grup tanımı eklenir.

![Projeyi Uygulamalar Menüsüne Ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76d50dd2-3151-4346-b98b-2d18534b2664)

Daha sonra **“İzinler”** sekmesine gelinir ve **“Menü”** başlığı genişletilir. Menü yetkisinin altında, sistemde tanımlı tüm menü profilleri listelenecektir. Bu listeden, az önce oluşturulan “Tüm Kullanıcılar Profili” tanımına **“İzin Ver”** seçeneği ile yetki verilir ve ardından “Değişiklikleri Kaydet” butonu ile düzenlemeler kaydedilir. Böylece, sistemdeki tüm kullanıcılar, Tüm Kullanıcılar Profilinde tanımlı, IK Süreçleri ve Yıllık İzin Süreci başlıklarını görebilir ve Yıllık İzin Süreci başlığına tıkladığında yeni süreç başlatabilirler.