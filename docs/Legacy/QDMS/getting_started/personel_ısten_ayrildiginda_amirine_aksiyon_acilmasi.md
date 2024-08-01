# PERSONEL İŞTEN AYRILDIĞINDA AMİRİNE AKSİYON AÇILMASI

Bir çalışan işten ayrıldığında QDMS’te üzerinde bekleyen işlerini tamamlamamış olabilir. QDMS işten ayrılan kişinin bir üst amirine görseldeki gibi aksiyon açabilir ve mail ile bilgilendirme yapabilir. Ancak açılan bu aksiyon işten ayrılan kişinin üzerinde bekleyen görevler için değil, görevlerin devredilmesi içindir. Açılan bu aksiyonun içeriği ise “İşten ayrılan kişinin üzerinde bekleyen işler bulunmaktadır, bu işlerin tamamlanması ya da bir başka kullanıcıya devredilmesi gerekmektedir.” şeklindedir. 

Bilgilendirme amaçlı üst amire açılan aksiyonlar, işten ayrılan kişinin üzerinde bekleyen görevlerden bağımsız, onları etkilemeden açılan bir aksiyondur. Diğer bir deyişle üst amirin bu görevlere müdahale etmesi için açılan bir aksiyondur.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Aksiyon-117e2545-104b-4a86-892b-4429973936d8.png)

Bunu sağlamak için; 




### 1-	HR entegrasyonu olması gerekmektedir.

### 2-	Sistem Altyapı parametrelerinden 195 nolu parametre “Evet” olmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/1-1c3a9a58-343e-4e73-a800-ba6098242076.png)

### 3-	196,197,198,199,200 nolu parametreler doğru şekilde doldurulmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/2-dc812e96-04e1-4d09-8232-3776a589aa85.png)

İşten ayrılan kişinin üst amirine açılan aksiyonlar başlığı altında bir aksiyon planı oluşturulmalıdır. Oluşturulan ana aksiyonun numarası 196 nolu parametreye yazılmalıdır.
Kişi işten ayrıldığında amirine QDMS tarafından açılacak olan aksiyon için bir tanım ve kalem tipinin olması gerekmektedir. Oluşacak aksiyon kaleminin tanımı 197 nolu parametreye, kalem tipi kodu (Sistem Altyapı Tanımları>Aksiyon>Aksiyon kalem tipi tanımlama) 198 nolu parametreye yazılmalıdır.


###  4-	Sistem Altyapı parametrelerinden 130 nolu parametre “Evet” olduğunda sistem, kişinin kendisine bağlı olduğu bir kullanıcının işten ayrıldığına dair bilgilendirme maili gönderir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/4-f95af39b-fd43-408c-9ff5-074c51067d4a.png)

Oluşacak aksiyon sayesinde işten ayrılan kişinin amiri, işten ayrılan kişinin üzerinde bekleyen işleri görev transfer ya da aksiyon gerçekleştirecek değiştirici menüsü üzerinden başka bir kullanıcıya/kullanıcılara devredebilir. Onay Transfer ile ileride o kişiye gelecek onayları başka bir kullanıcıya devredebilir. Pozisyon kodu değiştirici ile işten ayrılan kişinin pozisyon koltuğuna bir başkasını oturtabilir. Görevler pozisyonlara verildiğinden dolayı bu sayede bekleyen işler başka bir kullanıcıya devredilmiş olur. 
Amir, bu işlemi tamamladıktan sonra kendi üzerinde bekleyen aksiyonu da (İşten ayrılan kişinin amirine açılan aksiyon) gerçekleştirerek kapatabilir.


