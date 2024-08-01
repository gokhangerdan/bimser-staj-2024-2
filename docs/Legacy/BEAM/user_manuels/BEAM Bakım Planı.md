## Varlıklara Varsıyalan Bakım Planı Tanımlama
## Bakım Planı ve İş Adımı Oluşturma:

BEAM uygulamasında Ana Menü’ye girilerek sırasıyla;

-   Bakım Yönetimi
    -   Periyodik Bakım
        -   İş Adımları
            -   Ekle

Adımları izlenmelidir.

![Resim1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload519068b6-0bd0-4053-ac18-bb52a32c64d9)

Açılan iş adımı tanımlama ekranından, bakım yapılırken uygulanması istenilen bir iş adımı tanımlanacak.

Benim bu örnekte kullandığım bilgiler şu şekilde;

Kod: ELK-BKM-01

Tanım: Varlığın elektrik bağlantısı kesilmelidir.

Iş Adımı için gerekli içerik doldurulduktan sonra kaydet butonu ile ilgili tanımlama sisteme eklenmiş olacaktır.


![Resim2](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload44b68c5e-ff1d-467c-94ff-66deb014df4a)

İş Adımı tanımlandıktan sonra bu iş adımının uygulanacağı bakım planı tanımlaması yapılmalıdır.;

-   Bakım Yönetimi
    -   Periyodik Bakım
        -   Bakım Planı
            -   Ekle

Adımları izlenerek Bakım planı tanımlama sayfasına girilmelidir.


![Resim3](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7388a9b2-1cdd-4c3a-9a63-10f25f2389a1)

Burada da Kod ve Tanım bilgileri doldurulur,


![Resim4](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c80d6df-a5f5-44a4-be55-d0d2c11861f4)

Sonrasında sol tarafta yer alan sekmelerden “İŞ ADIMLARI” sekmesine girilir ve bu bakım planında uygulanması istenen iş adımları bu sekme yardımıyla seçilir. Daha sonra Kaydet butonuna basılarak bu işlem tamamlanmış olur.

![Resim5](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42636366-ac6b-462f-a9db-d34b0c2a11ee)

## Varlık İçin Varsayılan Bakım Planı Tanımlama

Öncelikle aşağıdaki adımlar izlenerek varlık detaylarını içeren sayfaya girilmelidir:

-   Varlık Yönetimi
    -   Varlıklar
        -   Ekle / Değiştir

Varlık sayfasında yer alan sekmelerden “BAKIM PLANI” sekmesi tıklanmaldıır.


![Resim6](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload656c6594-b09e-41b5-b6d1-077fd521e8ba)

![Resim7](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload798c46c6-bd3e-4a78-83ed-162e136d5603)

*Eğer sizin ekranınızda “BAKIM PLANLARI” sekmesi yer almıyor ise:*

*Varlık Yönetimi -\> Tanımlar -\>* Varlık Türleri

Varlık içerisinde seçili olan “VARLIK TÜRÜ” için “DEÜİŞTİR”

*Sol tarafta yer alan “SEKME GÖRÜNÜRLÜĞÜ” sekmesi.*

*“Bakım Planları” check’I işaretli duruma getirilir.*

*KAYDET butonu ile işlem kaydedilir ve tekrar ilgili varlık içerisine tekrar girilmelidir.*

*Bu işlem sonrası ilgili sekme sizin ekranınızda da yer alacaktır.*

Bakım Planları sekmesi içerisinde yer alan tablonun üzerindeki “+” butonuna basılarak, varlık ile varsayılan bakım planı eşleştirmesi için şartları belirleyeceğimiz ve ilişkilendirmeyi yapacağımız ekran karşımıza gelecektir:


![Resim8](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload675f73d3-2895-497a-872e-31b0ffd7c0c6)

Bu açılan ekranda bulunan alanlar:

-   PLAN KODU - Tanımladığımız bakım planını seçeceğimiz alan.
-   PLAN TANIMI – Tanımladığımız planın tanım bilgisi. (plan kodu seçimi sonrası otomatik dolacak)
-   İŞ EMRİ TÜRÜ – Bu varlığa açılan iş emrinin türü ; bu alana girilen iş emri türü ise bu plan ve içerisindeki iş adımları ilgili iş ermine otomatik aktarılacaktır.
-   BAKIM KODU – Bu varlığa açılan iş emrinin bakım arıza kodu ; bu alana girilen bakım arıza kodu ise seçilen bu plan ve içerisindeki iş adımları, ilgili iş ermine otomatik aktarılacaktır.

Görsellerde örneğini yaptığım “JNR-01” varlığı için İş Emri Türü: “A” ve Bakım Kodu: “B” seçilerek açılan iş emrinin varsayılan bakım planı olarak “ELK-BKM” ve bu plan içerisinde yer alan İş Adımı “ELK-BKM-01” tanımlarını tamamladım.

Şimdi Sonucu görmek için belirttiğim şartlarda bir iş emri oluşturuyorum:


![Resim9](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05bbc3eb-2c8e-49cb-8ac1-f514f4d63017)

![Resim10](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbfd9a6fa-921e-45c6-ba47-d9d7bf177ba7)

![Resim11](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadadd36ffb-84db-4db2-b577-2986883ea7be)

![Resim12](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94b71026-8d6d-4e96-a92c-0ae0e054fb42)

**Eğer Farklı koşullarda, farklı bakım planları eklemek isterseniz aynı işlemi tekrar tekrar yapabilirsiniz.**

**Eklediğiniz bakımplanı ayarlarından hangisinin koşulu sağlanıyor ise iligli bakım planı ve iş adımları iş ermine aktarılacaktır.**
