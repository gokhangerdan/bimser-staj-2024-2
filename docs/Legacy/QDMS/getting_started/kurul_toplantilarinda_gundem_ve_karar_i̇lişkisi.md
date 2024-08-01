# Kurul Toplantılarında Gündem ve Karar İlişkisi

Kurul toplantı modülünde işleyiş şu şekildedir:

1. Toplantı kaynağı tanımlama (Toplantı için şablon oluşturma)
2. Toplantı kalemi ekleme (Toplantı planlama)
3. Taslak Onayı
4. Katılım Onayı
5. Toplantı yapılması kararının alındığı Karar Onayı
6. Toplantı Başlat-Toplantı Bitir

Bu akış içerisinde Sistem Altyapı Tanımları altındaki toplantı kaynağına eklenen gündemler  Entegre Yönetim Sistemi tarafından Toplantı planlandığında toplantı gündemlerine otomatik olarak eklenmektedir. Planlama yaparken ve sonrasında toplantıya yetkisi olanlar ekstra gündem eklemeleri de yapabilmektedir.

6. Adımda toplantıyı tamamlarken çeşitli önlemler açılabilir (DÖF Aksiyon vb.). Ardından toplantı kapatılır. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/Gündem-be03481b-7c02-42e4-b4b2-affa34569af6.png)

Toplantı yapılıp karar aşamasında önlem açıldığında ve bu önlem bir sonraki toplantıya kadar kapanmadıysa, aynı kaynaktan yeni bir toplantı planlanmak istendiğinde Yeni planlanacak Toplantı gündemine altyapıdaki toplantı kaynağından gelen otomatik gündemler haricinde bir önceki toplantıda önlemle ilişkilendirilmiş olup önlemi açık statüde bulunan gündemlerde otomatik olarak  eklenmektedir. (1. özellik) 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Karar-cc257237-e820-49ec-81af-39211511dfc1.png)

Buna ek olarak, bir toplantı planlanıp 6. adımdaki karar aşamasına gelindiğinde ise seçilen toplantı kaynağından oluşan son toplantıdan açık önlemleri olan kararlarda yeni toplantının kararlarına otomatik olarak gelmektedir. (2.özellik)

