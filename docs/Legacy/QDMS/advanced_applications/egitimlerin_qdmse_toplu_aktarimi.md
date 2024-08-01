# Eğitimlerin Toplu Bir Şekilde Sisteme Aktarılması

Eğitim planlama modülünde geçmiş tarihli eğitimler QDMS sistemine toplu bir şekilde aktarılabilir. Bu aktarımın sağlanabilmesi için Sistem Altyapı Tanımları  > BSAT > Konfigürasyon Ayarları > Aktarımlar > Eğitim Aktarma menüsü açılır. Açılan sayfada "Şablon İndir" butonuna tıklanarak aktarım şablonu indirilir.

İndirilen excelde bulunan sütunlar için;

ANA PLAN --> Sistemde Tanımlı olan bir ana plan kodu yazılmalıdır. Entegre Yönetim Sistemi > Eğitim Planlama > Eğitim Planı sayfası açıldığında Eğitim plan kodu değerlerinden biri bu sütun için yazılı olmalıdır.

DETAY PLAN --> Detay Plan kodu sistemde tanımlı olmayan, her bir satır için kendine özgü bir detay plan kodu yazılmalıdır. 

Eğitim Tanım Kodu --> Entegre Yönetim Sistemi  > Eğitim Planlama > Eğitim Tanımlama sayfasında bulunan eğitim tanımının kodu yazılmalıdır.

Başlangıç Tarihi --> Eğitimin başlangıç tarihi yazılır.

Bitiş Tarihi --> Eğitimin bitiş tarihi yazılır.

Statu Bitiş Tarihi --> Eğitimin bitti statüsüne getirildiği tarih girilir. Bitiş tarihi ve statü bitiş tarihi aynı tarihler olarak yazılmalıdır.

Eğitim Veren --> Aktarım sağlanan eğitimlerin eğitim veren kullanıcısı qdms sisteminizde tanımlı değil ise adı soyadı; qdms sisteminde tanımlı ise sicil numarası yazılması gerekmektedir.

Eğitim Veren TCKN --> Eğitim veren kullanıcının TCKN bilgisi yazılmalıdır. IBYS kapsamında eğitimler aktarılıyor ve bakanlığa gönderimi yapılacak ise bu alanın kesinlikle dolu olması gerekmektedir.

Eğitim Sorumlusu --> Eğitim sorumlusu kişinin QDMS sicil numarası yazılır.

Eğitim Yeri --> Eğitimin verildiği yer bilgisi yazılır.

Süre --> Eğitim süresi yazılır. Dakika cinsinden belirtilmelidir.

Eğitim Veren Tip --> Eğitim veren iç kullanıcı ise "I"; eğitim veren dış kullanıcı ise "D" yazılmalıdır.

Eğitim Yeri Tipi --> Eğitim yeri iç eğitim yeri ise "I"; dış eğitim yeri ise "D" yazılmalıdır.

Eğitim Türü --> Uzaktan eğitim verilmiş ise "0"; Yüzyüze eğitim verilmiş ise "1" yazılmalıdır.

Belge Türü --> Eğitim veren kişinin belge türünün girildiği alandır. 1- İş Yeri Hekimi; 2- ISG Uzmanı; 3-Diğer Sağlık Personeli

İşyeri Kodu --> Eğitimin hangi iş yeri için gerçekleştirildiği bilgisi yazılır. QDMS içerisinde iş yeri tanımlama sayfasında bulunan işyeri kodu yazılmalıdır.

Başlangıç Saat --> Eğitimin başladığı saat bilgisi yazılır. 

Bitiş Saat --> Eğitimin bittiği saat bilgisi yazılır. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/Egitim1-d9e6bb0c-761d-443b-898a-3af8373e4155.png)

Geçme Notu --> Eğitim için geçme notu verilecek ise geşçme notu bilgilsi yazılır. 

Durumu --> Eğitimlerin durumu yazılır. 1- Planlanıyor; 2- Devam Ediyor; 3- Bitti; 4- Ertelenmiş; 5-İptal.

Eğitim Sonucu --> Eğitimler tamamlandıktan sonra katılımcılara verilecek olan belge türü yazılır. S- Sertifika; B- Başarı Belgesi. 

Periyodik Mi --> Eğitimlerin periyodik eğitim olup olmadığı yazılır. Periyodik ise 1; değil ise 0 yazılmalıdır.

Tekrar Periyodu --> Periyodik girilmiş olan eğitimler için tekrar periyodu yazılır. Yazılacak değer Ay cinsinden yazılmalıdır.

Süreç --> Eğitim bir süreç ile ilişkili ise süreç kodu yazılmalıdır. Sistem Altyapı Tanımları > BSAT > Tanımlar > Süreç Tanımlama sayfasında bulunan süreç kodu girilmelidir. Eğer birden fazla süreç ile ilişkili ise süreç kodları birbirinden noktalı virgül ile ayrılmalıdır.

Doküman --> Eğitim bir doküman ile ilişkili ise doküman kodu yazılmalıdır. Eğer birden fazla doküman ile ilişkili ise doküman kodları birbirinden noktalı virgül ile ayrılmalıdır.

Değerlendirilecek --> Eğitim etkinlik değerlendirme işlemi yapılacak ise 1, yapılmayacak ise 0 değeri girilmelidir.

Değerlendirecek Kişi Tipi --> Değerlendirme sağlayacak kişi pozisyon koduna göre belirlenecek ise 1; rol'e göre gidecek ise 2 yazılmalıdır.

Değerlendirecek Kişi --> Kişi tipi 1 girilmiş ise sicil numarası, kişi tipi 2 girilmiş ise rol kodu yazılmalıdır.

Eğitim Açıklaması --> Aktarılan eğitimlerin açıklaması yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/2-78328ec0-cf01-4e6e-9e14-3ed1e2aa92ac.png)

ANA PLAN --> Eğitim planı sheet'inde verilmiş olan plan kodu yazılmalıdır.

DETAY PLAN --> Eğitim Planı sheet'inde verilmiş olan detay kodu yazılmalıdır.

Katılımcının Sicil No --> Eğitime katılan katılımcıların sicil numaraları girilir. Birden fazla katılımcı için ana plan kodu ve detay plan kodu satır olarak çoklamalıdır.

Katıldı/Katılmadı --> İlgili katılımcı eğitime katıldı ise 1; katılmadı ise 0 yazılır.

Katılım Tarihi --> Katılımcının eğitime katıldığı tarih bilgisi yazılır.

Katılmama Nedeni --> Eğer katılım sağlamayan bir katılımcı bulunuyor ise bu katılımcının katılmama nedeni yazılır.

Değerlendirildi Mi? --> Katılımcı eğitim veren tarafından değerlendirildi ise 1; değerlendirilmedi ise 0 yazılır.

Deperlendirme Puanı --> Katılımcının değerlendirme puanı yazılır.

Katılımcı Eğitime Puan Verdi Mi ? --> Katılımcı eğitim etkinliğini değerlendirdi ise 1; değerlendirmedi ise 0 yazılır.

Katılımcının Eğitime Verdiği Puan --> Katılımcının eğitim etkinliğine verdiği puan yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3-964e3849-f8a0-4517-b9fb-861ece663788.png)

Şablon doldurularak kaydediltikten sonra Eğitim Aktarma sayfasında bulunan "Şablon Yükle" butonuna tıklanır. Ardından doldurulmuş olan excel seçilir ve "Kontrol Et" butonuna tıklanır. 

Sistem verilerin aktarım işlemi için uygun olup olmadığını kontrol edecektir. Veriler aktarım işlemi için uygun ise verileri aktar butonuna tıklayarak eğitimlerinizi toplu bir şekilde sisteme aktarabilirsiniz. Hata alınması halinde sistem hangi satırda hata bulunduğunu yazacaktır. Hatalı satırlar excel şablonu içerisinden düzeltilmeli ve tekrar şablon yükle butonuna tıklayarak yeniden yüklenmelidir.

