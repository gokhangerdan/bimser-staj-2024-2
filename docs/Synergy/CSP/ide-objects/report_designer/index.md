# REPORT DESIGNER
"Report Designer", kullanıcılara platformdan bağımsız bir şekilde rapor oluşturma ve önizleme imkanı sunan profesyonel bir araçtır. Bu özellik, kullanıcıların raporları istedikleri şekilde tasarlamalarına ve ihtiyaçlarına uygun olarak düzenlemelerine olanak sağlar.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/0-b8be0a94-7dcf-43d4-9f8c-3317b89326b7.png)
 "Report Designer" oluşturmak için IDE üzerinde aşağıdaki adımları takip edin:

1.  "IDE" açılır.
2.  "PROJE YÖNETİCİSİ" açılır.
3.  İlgili proje seçilir ve "ÇÖZÜM GEZGİNİ" sekmesi açılır.
4.  "REPORTS" klasörüne sağ tıklanır. Ekle butonuna basılarak rapor oluşturulur.

## İlk Raporumuzu Oluşturalım.
"Raporun ilk bandı olan "Report Header", sayfa dışı bölgelerdeki kenar boşluklarında yer alır. Burada raporun adını, şirket logosunu, oluşturulma tarihini, kullanıcı adını ve diğer önemli bilgiler yer alır. Bu sayede, raporun başlangıcında gerekli tanıtım ve bilgilendirmeleri sağlanır.

"Report Footer" ise raporun son sayfasında Sayfa Altbilgisi ve Alt Kenar Boşluğu'ndan önce yer alır. Raporun özetini veya sonuçlarını göstermek için Rapor Altbilgisi bandı kullanılır. Bu bölümde, toplam değerler, ortalama değerler veya diğer önemli sonuçlar sunulur.

"Details" bandı ise raporda verilerin detaylı şekilde görüntülendiği bölümdür. Bu bandı kullanarak, veri kaynağındaki her kayıt için ayrı bir satır oluşturabilir. Detay bandı, veriler filtrelenmediği sürece tüm kayıtlar yazdırılır. Genellikle raporun en büyük bölümüdür ve raporun ana içeriğini temsil eder.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/1-5693de38-2346-4b32-bb66-1dc4e21802c3.png)
Araç kutusundan tablo nesnesini sürükle bırak yöntemi ile "Rapor Designer" üzerine eklenir. Tablo nesnesi eklenirken 3 sütun ile oluşur. Tablo nesnesini özelleştirmek için aşağıdaki adımlar takip edilir.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/2-673c328d-b541-4dc7-8358-f13fa040e87e.png)
Sütun hücresine çift tıklanır. Sağ tarafta özellikleri görüntülenir. Özellikler penceresinden "Text" alanına sütuna verilecek isim girilir. Bu işlem diğer hücreler için de uygulanır.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/3-91b4849b-4a31-4275-b6fb-a592d67046e7.png)
Özellikler penceresinde bulunan depo simgesine tıklanır, Datasource (Veri Kaynağı) listesi içerisinden raporda kullanılması istenilen kaynak sorgusu seçilir. Bu seçenek, projeniz içinde tanımlı olan veri kaynaklarını içerir.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/4-81115d6a-fad1-4104-a1b8-c9404238c31f.png)
Data kaynağı sürükle bırak yöntemi ile Report Designer'in Details alanına eklenir.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/5-ce3490ec-f802-4541-97f6-3508a2c25764.png)
Hücreye tıklanır ve yandaki 'f' simgesi seçilerek hücrenin hangi değeri getireceği, alt görseldeki gibi işaretlenir.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/6-c2277bc4-aa27-4c1a-b34f-95ca682a9aa2.png)
Report items > Alanlar altında DataSource'dan gelen alanlar listelenir. İşaretlenen hücrenin hangi veriyi getireceği burada belirlenir.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/7-ae52bdbd-d088-4ee6-ae3b-c6ca163f38f3.png)
Rapor tasarımınızı tamamladıktan sonra, Report Header alanına bir etiket ekleyerek metin formatı belirlenir. Bu etiket, raporunuzun başlığı veya başka bir metin öğesi olabilir ve istediğiniz görüntüyü yansıtacak şekilde özelleştirilebilir. 'f' simgesine tıklayarak, tarih yapısını belirlemek için farklı seçenekler arasından tercih yapılır. 
Değişiklikleri kaydetmek için sol üst köşede bulunan menü çizgilerine tıklanır ve ardından "Kaydet" butonuna basılır. Bu işlem, raporunuzun güncel tasarımını korumanızı sağlar ve ileride tekrar erişmek veya paylaşmak istediğinizde kullanmanız için kaydedilen bir versiyon oluşturur. 
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/8-c158c9e7-b598-401a-a15e-34609e0eddfe.png)
Raporun görüntüleneceği form açılır. Araç kutusu içerisinden "ReportViewer" nesenesi eklenir.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/9-c997518b-1370-48d0-98af-1b8ca98275c7.png)
Nesnenin özelliklerine ulaşmak için nesneye çift tıklanır. Özellikler penceresi > Appearence içerisinde bulunan Report alanına tıklanarak görüntülenecek olan Rapor seçilir. Proje yayınlanarak ilgili kırılımlara eklenerek kullanıcılara sunulmaya hazır hale gelir.
## Form Görünümü
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/10-77a02aee-0583-41cf-bb26-f4bdce20060a.png)
Birden fazla indirme seçeneği nesne üzerinde listelenir. 
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/11-6bb34839-a39f-40f2-b676-a89fc0fafbcf.png)

![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/12-6140db38-fc37-4411-a9f2-b0156f3bda9e.png)
Rapor içerisinde bir arama gerçekleştirilebilir. Büyüteç simgesine tıklandıktan sonra aranacak kelime kutucuğa yazılır. Rapor ve arama altında eşleşmeler mevcutsa "Search Result" alanında listelenir.
