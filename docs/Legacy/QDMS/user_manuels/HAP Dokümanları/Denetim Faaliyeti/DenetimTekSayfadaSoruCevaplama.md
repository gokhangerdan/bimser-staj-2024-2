---
title: Sorular Tek sayfada Cevaplasın Özelliği
description: “Sorular Tek sayfada Cevaplasın” ( Puanlı ) özelliği Kullanımı Kullanıcı Yardım Dokümanı
sidebar_position: 3
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::

**Denetim Faaliyetleri Modülünde “Sorular Tek sayfada Cevaplasın” ( Puanlı ) özelliği Kullanımı Kullanıcı Yardım Dokümanı**


## **1.Denetim Faaliyeti Modülü**

Bulgulara Döf/Aksiyon açılarak çözüm süreci başlatma, eski denetimlere ait aksiyonların sonuçlarını izleme, denetçilerin iş yükü dağılımını planlama, denetim planları tanımlama ve zaman çizelgesi olarak görüntüleme, dinamik soru listeleri oluşturma denetçiler ve denetlenen birim sorumlularını denetim öncesi ve sonrası bilgilendirme, otomatik denetim raporları oluşturmayı sağlayan modüldür.

## **1.1.Sistem Altyapı Tanımları/Denetim Faaliyeti**

Denetim Faaliyetleri Modülünün altyapısını oluşturacak tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre giriş ekranında veriler karşımıza çıkmaktadır.

### **1.1.1.Soru Grupları Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Denetim Faaliyeti/ Soru Grupları Tanımlama

Soru gruplarının oluşturulup tanımlanma işleminin yapıldığı menüdür. Denetimde sorulacak soruların farklı tiplerde gruplandırılıp, bu gruplar baz alınarak filtreleme veya raporlarda kullanılma durumları belirlenir. Soru havuzuna eklenen sorular bu gruplarla ilişkilendirilir. Genellikle şube, mağaza vb. denetimler için soruların gruplandırılmasında fayda sağlar. Bunun dışında, soru havuzuna soruları eklerken, filtreden daha kolay bulabilmek için gruplandırma kullanılabilir. Örnek olarak, yönetim sistemi, süreç, departman bazlı gruplandırılabilir. Denetimde puanlı sorularımı ağırlıklı olarak ayırıyorsam soru grupları tanımlama işlemini gerçekleştiriyorum Her bir soru grubu farklı bir ağırlıkla çarpılma işlemi yapılıyorsa örneğin Yönetim sistemine bazlı bir soru grubu tanımladığında ağırlığını 1 ile, Süreç bazlı bir soru grubu tamamlandığında ağırlığını 2 ile çarpılıyorsa bu soru gruplarının ağırlıkları farklı demektir. Bunun dışında eğer Puanlı Denetim yapmıyorsanız veya ağırlık puan vermiyorsanız Soru Grupları sadece soru listesi oluştururken Filtre amaçlı olarak yol gösterir. Zorunlu değildir. Puanlı bir denetim yapmak için ilk olarak Soru grubu tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66c190db-d5d2-4105-931b-bcc51d419ee0)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04557fa6-fc14-4d26-80a5-8861feaf32b3):Yeni bir soru grubu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload035c102f-84fc-4e27-a7a2-8a74fd8b2c64):Listede seçili soru grubu bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5ce95fd-2486-4e23-9f45-b1f0a40f9f37):Listede seçili soru grubu bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41f9f1d2-9ea8-489c-bc5a-7289573c60a9):Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8aabf1c-4e76-44e9-9439-da1b03499362):Veriler Excel’e aktarılabilir.

Soru grubu tanımlama ekranına yeni bir soru grubu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload649fcbc0-84e3-4f1b-a654-91434876ec24) (yeni) butonu tıklanarak Soru Grubu Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6735f77e-3e21-4355-b316-3c02837d8e6c)

**Açılan ekranda ilgili alanlar tanımlanır:**

**No:** Sistem tarafından otomatik verilir.

**Soru Grubu Kodu:** Soru grup kodu girilir.

**Soru Grubu Tanımı:** Soru grubu için tanım yazılır.

**Ağırlık:** Buradaki alan puanlı denetimler için soru grubu bazında, soruların ağırlıklandırılıp formüle dayalı puanlarının hesaplanması gerektiği durumlarda kullanılır. Diğer durumlarda boş bırakılmasında bir sakınca yoktur.

Soru grupları tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20c69077-cf35-4451-bcd3-af34d7184312)

### **1.1.2.Soru Havuzu**

**Menü Adı:** Sistem Altyapı Tanımları/Denetim Faaliyeti/ Soru Havuzu

Denetimde sorulacak soruların tanımlama işleminin gerçekleştiği menüdür. Tanımlanan her sorunun sorulacağı departman, yönetim sistemleri, madde numaraları, ilgili dokümanları, ilgili süreçleri, bağlı olacağı soru grubu gibi alanlar belirlenebilir. Aynı zamanda sorunun aktif/ pasif özelliği bulunmakta, sorunun bir daha sorulmayacağı durumlarda soru pasife çekilebilmektedir. Böylece geçmişte sorunun sorulduğu denetim kayıtlarında soru kaybolmayacak, yeni denetimlerde ise aktif soru havuzunda yer almayacaktır. Denetim Faaliyetleri Modülünde "Sorular Tek sayfada Cevaplasın" ( puanlı ) özelliği kullanılırken soru havuzunda soru tanımlarken seçeneğin yazılmasında büyük harf ve küçük ayrımında dikkate alınması için doğru bir şekilde seçenekleri tanımlanması gerekir. Bu özellik kullanırken soru tanımlarken aynı seçeneklerin tanımlanarak Soru Havuzunda tanımlanan soruların tiplerini aynı olması gerekmektedir. Puanlı Denetim yapılırken eklenen soruların seçeneklerin doğru bir şekilde tanımlanması tamamen aynı olması gerekir. Soru havuzu zorunlu değildir. Soruyla ilişkilendirilmemiş denetimlerde gerçekleştirilebilir. Örneğin Bazı firmalar soru dışında bulguları tespit ederler. Özellikle Saha denetimlerinde herhangi bir soru sormadan bu uygunsuzluk var diyerek o bulgu üzerine gidilip, o bulguya Döf ve Aksiyon açılabilir. Böylece soruyla ilişkilendirilmemiş denetimlerinde gerçekleştirilmesi işlemi yapılır. Denetim esnasında soru ekleme işlemi yapma gibi bir durumuz söz konusu olmaz. Sadece soru havuzunda soru çekme gibi bir durumuz söz konusu olabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload513fe7be-cb6d-45ce-9a0c-29d1248318b4)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04557fa6-fc14-4d26-80a5-8861feaf32b3):Yeni bir soru tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload035c102f-84fc-4e27-a7a2-8a74fd8b2c64):Listede seçili soru bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c41a8c9-29aa-4bdf-a742-89ea006d5a7e):Sorular revize edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload21256548-fd9b-4306-a94d-c40957e991fa):Revize edilen soruların eski revizyonları izlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5ce95fd-2486-4e23-9f45-b1f0a40f9f37):Listede seçili soru bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4904e758-e0df-4172-a616-d4ecec391272): Listede seçili soru bilgisi kopyalanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41f9f1d2-9ea8-489c-bc5a-7289573c60a9):Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8aabf1c-4e76-44e9-9439-da1b03499362):Veriler Exce’le aktarılabilir.

Soru havuzu ekranına yeni bir Soru eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload649fcbc0-84e3-4f1b-a654-91434876ec24) (yeni) butonu tıklanarak Soru Havuzu/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd7c9416-aaef-4413-9591-803d68dc38ce) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f0b2f55-9d2b-4209-ade9-786d7ae3b71f)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Soru No:** Sistem tarafından otomatik verilir.

**Revizyon No:** Revizyon no sistem tarafından otomatik olarak verilir.

**Soru:** Sorunun tanımı yazılır.

**Beklenen Cevap:** Beklenen cevap girildiğinde, denetçinin denetim yaparken soruya verilmesi gereken cevaba göre değerlendirmesi sağlanabilir.

**Durum:** Sorunun aktif ve pasif durumu belirlenir. Durumu pasife yapılan soru kullanım dışıdır.

**Puan Seçimi:** Denetim puanlı bir denetim ise; puanın hesaplanması soru üzerinden mi yoksa seçenekler üzerinden mi ya da seçeneklerle ilişkili kontrol noktaları üzerinden mi olacağının belirlendiği alandır.

**Puan:** Puanlı denetimde, denetim puanı soru üzerinden hesaplanıyorsa; sorunun max ve min puanı belirlenir. Burada yazılan puanlar denetim gerçekleştirme sayfasındaki cevaplar sekmesinde ilgili soruya cevap verilirken görülecektir. Denetçi max ve min puanı görüp sorunun cevabına istinaden sorudan aldığı puanı girer.

**Seçenek:** Seçenekler veya kontrol noktalarının seçenek değerlerinin ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8770aedf-1a99-4fc6-9026-52078c694cc3) ekle butonu tıklanarak girildiği alandır.

Seçenek ve kontrol noktası alanlarında soruya verilen cevabın seçeneğine göre kontrol noktası, DF veya aksiyon zorunlu olacak ise ilgili check-box’ ların işaretlenmesi gerekir. Varsayılan işaretlenirse o soru için tanımlanan seçeneğin, denetim gerçekleştirme aşamasında varsayılan olarak seçili gelmesi sağlanır. Seçenek tanımlanırken sağdaki kutucuktan seçeneğe puan verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73b1f544-d493-4802-bdbf-ce3be75d939a)

Eğer bir sorunun doğruluğu, kontrollere göre yapılıyorsa kontrol noktası zorunlu olsun check-box’ ı işaretlenmelidir. Daha sonra kontrol noktaları alanına gidilip, ilgili tanımlamalar seçenek tanımlamada olduğu gibi yapılır. Seçim tipi belirtildikten sonra, eğer puanlı denetim yapılacaksa, kullanılacak hesaplama yöntemi de seçilir. Bu hesaplama yöntemleri Toplama, Ortalama Alma, En Yüksek Değer, En Düşük Değer, Seçilmeyenlerin Toplamı gibi hesaplama yöntemleridir. Puan hesaplamasının; soru, seçenek ya da kontrol noktasına göre baz alınıp hesaplanacağının belirlenmesi gerekmektedir.

**Yalnızca Bir Tanesi Seçilebilir:** seçeneği aktif edilirse soru için tanımlanan seçenek ve kontrol noktalarından bir tanesi seçilebir.

**Birden Fazla Seçilebilir:** seçeneği aktif edilirse soru için tanımlanan seçenek ve kontrol noktalarından birden fazla seçilebilir.

**Hesaplama Yöntemi:** Soruda tanımlanan seçeneklerin denetim puanı hesaplanırken hangi yöntem ile hesaplanacağının belirlendiği alandır.

Burada bir diğer husus, denetimde kullanılacak olan soruların sisteme aktarılmasıdır. Aktarım, Sistem Altyapı/Konfigürasyon/Aktarımlar/Denetim Sorusu Aktarımı kısmından ilgili şablonu indirilerek yapılmaktadır.

**Diğer Alanlar sekmesi** ise, soru ile ilgili yönetim sistemleri, ilgili madde numaraları, ilgili departmanlar, ilgili süreçler, ilgili dokümanlar![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37b2f468-73c3-4c9d-a1ef-c26f6b3844e2) (ekle) butonu ile seçilerek ilişkilendirilebilir. Aynı zamanda daha önce tanımlanan soru grupları da soru grubu alanından seçilerek ilişkilendirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload752ad8cd-c5b4-4914-9626-ec443060e6e8)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İlgili Yönetim Sistemleri:** Soru ile ilgili yönetim sistemi ile ilişkilendirilir.

**İlgili Departmanlar:** Soru ile ilgili departmanlar seçilir.

**İlgili Madde Numaraları:** Soru ile ilgili yönetim sistemi seçildiğinde o yönetim sistemine bağlı madde numaraları ilişkisi verilir.

**İlgili Dokümanlar:** Soru ile ilgili tanımlı dokümanlardan ilişki verilir.

**İlgili Süreçler:** Soru ile ilgili tanımlı süreçlerden ilişki verilir.

**Soru Grubu:** Diğer alanlar sekmesinde soru grubu bilgisinin seçilebildiği alandır.

Soru Havuzu/Yeni Kayıt ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload823460bd-42b8-420c-93c2-68edb1f8c39a)

“Sorular Tek sayfada Cevaplasın" ( puanlı ) özelliğinin kullanıp Puanlı bir Denetim gerçekleştirmek için Soru Grubu alanında Sistemde tanımlı Soru grubu ile sorularımızı tek tek ilişkilendirme işlemini gerçekleştiriyoruz.

### **1.1.3.Soru Listesi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Denetim Faaliyeti/ Soru Listesi Tanımlama

Soru Listesi tanımlama işleminin gerçekleştiği menüdür. Soru havuzunda tanımlanan sorular departman, yönetim sistemi, süreç ismi gibi “Soru Listesi” oluşturularak kategorize edilebilir. Bu ekranda soru listesinin puanlı olup olmayacağı da belirlenir. “Sorular Tek sayfada Cevaplasın" ( puanlı ) özelliğinin kullanıldığı menüdür. Eğer soru sorularak denetim yapılacaksa, Denetimde soru sorulacaksa Soru listesi mutlaka kullanılması gerekmektedir. Soru grubu zorunlu değildir ama Soru listesi zorunlu olmak zorundadır. Çünkü soru sorularak denetim yapılabilmesi için Denetim Tanımlama menüsünde Denetim tanımlanırken Denetim Soru listesi ile ilişkilendirilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c808130-a22a-4bf8-b9d0-0db0318ebab0)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8e4328a-9e67-4032-a0d3-cb1563f11895):Yeni soru listesi oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec48601c-9d05-4228-9402-082a7b274c26):Listede seçili soru liste bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload226e5457-2452-43b2-9ec6-8d80f7a901b0): Listede seçili soru listesi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69c1b226-ffb6-401d-8736-dc8a95c1d174): Soru listesine bağlı sorular seçilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8aabf1c-4e76-44e9-9439-da1b03499362): Soru listesi verileri Excel’e aktarılabilir.

Soru Listesi tanımlama ekranına yeni bir Soru Listesi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload649fcbc0-84e3-4f1b-a654-91434876ec24) (yeni) butonu tıklanarak Soru Listesi Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc2141eb-7635-4ed9-922f-fc8bad210301)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcdbab5bb-2b69-401a-bf83-22d92edd8b4c)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Liste No:** Sistem tarafından otomatik verilir.

**Soru Listesi Tanımı:** Soru listesinin tanımı girilir.

**Puanlı Mı? :** Soru listesi puanlı olacaksa seçilir.

**Sorular Tek Sayfada Cevaplansın:** Denetim puanlı yapılacaksa soruların tek sayfada cevaplanıp cevaplanmayacağı işaretlenir. Sorular tek sayfadan cevaplansın özelliği puanlı soru listelerinde, seçeneklerin daha kolay işaretlenebilmesi için optik cevap anahtarı benzeri görünüm ile sağlanmaktadır. Sorular tek sayfada cevaplansın seçeneği; tüm soruların seçenek değerleri aynı olduğu durumda kullanılmaktadır. Denetim Modülünde "Sorular Tek sayfada Cevaplasın" ( puanlı ) özelliği kullanıp Puanlı denetim gerçekleştirmek için Puanlı alanı ilgili check box işaretlenir. Puanlı alanı işaretlendikten sonran Sorular Tek sayfada cevaplansın alanı görüntülenir ve bu alanla ilgili check box’ta işaretlendiğinde bu özellik Denetim Faaliyetleri Modülünde kullanılır.

Soru listesi tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234bd8d3-78ae-4fca-b2fb-f708b3806c47)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload299859fd-fdc8-4604-af22-d38f02093c22)Sorular butonuna tıkladıktan sonra ilgili soru listesi için soru tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3082adbd-1f83-4b46-a024-edbc19030106)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8e4328a-9e67-4032-a0d3-cb1563f11895) Yeni butonu tıklanır. Soru seç ekranında eklenecek sorular eklenir. Eklenmiş sorular için düzenle butonuna tıklanarak sorunun zorunlu sorulma durumu, ağırlığı ve soru listesi puanlı seçilmişse, puanı belirlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload39232c20-600a-4320-a565-bdd6eb61eb9d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadefddac5a-fdff-40f6-bbaa-3a6e1155022b)

Sorular tek sayfadan cevaplansın seçeneği işaretlendiğinde denetim gerçekleştirme aşağıdaki görünüm şeklinde olacaktır:

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e32b7bc-5daa-4afb-b958-cf76bcf641dd)

HDD seçeneği sorunun denetim puanının hesaplanmasına dahil edilmeyeceği durumda seçilir.

İlgili soru için, cevap verildikten sonra, detaylar alanından düzeltici faaliyet veya aksiyon planlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade33a9755-ad3e-435f-ba97-72f85360834f)

Sorular tek sayfada cevaplansın seçeneği; tüm soruların seçenek değerleri aynı olmadığı durumda sistem uyarı verir. Soru listesi tanımlama-Sorular ekranında seçenek değeri aynı olmayan bir soru ekleme işleminde yapıldığında sistem listedeki eklenen sorunun numarası belirterek ekran görüntüsündeki örnekte olduğu gibi “Listedeki 11 nolu soru/sorular cevapları tek sayfada yanıtlama uygun değildir” şeklinde uyarı mesajını verir. Bu yüzden Sorular Tek sayfada Cevaplasın" ( puanlı ) özelliği kullanılırken Soru tiplerinin aynı olması için seçenekleri tanımlarken seçeneklerin aynı şekilde tanımlanması gerekmektedir. Ayrıca soru seçenekleri tanımlarken Büyük Küçük Harf yazım kuralına da dikkat etmek gerekir. Bu özelliğin uygulanması için seçenekleri mutlaka aynı olması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2dca9d0-836e-4775-8e3a-dd558500cb92)

### **1.1.4.Denetçi Yeterlilik Seviyesi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Denetim Faaliyeti/ Denetçi Yeterlilik Seviyesi Tanımlama

Denetçilerin yetkinliklerinin tanımlandığı menüdür. Baş denetçi, denetçi, gözlemci gibi yetkinlikler tanımlanabilir. Bu menüde tanımlanan yetkinlik seviyeleri denetçi tanımlama menüsünde, denetçilerin ilgili yönetim sistemleri için seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb5cad06-fffd-42b4-b132-f9fd813084d5)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8e4328a-9e67-4032-a0d3-cb1563f11895): Yeni bir yeterlilik seviyesi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec48601c-9d05-4228-9402-082a7b274c26): Listede seçili yeterlilik seviyesi bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload226e5457-2452-43b2-9ec6-8d80f7a901b0): Listede seçili yeterlilik seviyesi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8aabf1c-4e76-44e9-9439-da1b03499362): Veriler Excel’e aktarılabilir.

Yeterlilik Seviyesi tanımlama ekranına yeni bir yeterlilik seviyesi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload649fcbc0-84e3-4f1b-a654-91434876ec24) (yeni) butonu tıklanarak Yeterlilik Seviyesi Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload599517d4-d079-4ff0-b574-427708c79625)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Yeterlilik Seviyesi:** Sistem tarafından otomatik verilir.

**Yeterlilik Seviyesi Tanımı:** Yeterlilik seviyesi tanımı girilir.

**Denetim Yapabilir:** Denetime denetçi atarken burada seçilen kriter filtrelemede kullanılır.

Yeterlilik Seviyesi Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc6e5193-86a9-499c-afa0-8164ab8efcfb)

### **1.1.5.Denetçi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Denetim Faaliyeti/ Denetçi Tanımlama

QDMS’de denetim yapacak kişilerin tanımlanma işleminin gerçekleştiği menüdür. Denetçiler tanımlanırken, hangi yönetim sistemi ile ilgili denetim yapabilecekleri belirlenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f86f470-7c78-4c52-b927-0da27947b32b)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8e4328a-9e67-4032-a0d3-cb1563f11895):Yeni bir denetçi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec48601c-9d05-4228-9402-082a7b274c26): Listede seçili denetçi bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload226e5457-2452-43b2-9ec6-8d80f7a901b0): Listede seçili denetçi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8aabf1c-4e76-44e9-9439-da1b03499362) : Veriler excele aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41f9f1d2-9ea8-489c-bc5a-7289573c60a9) : Kayıtlar filtrelenerek arama yapılabilir.

Denetçi tanımlama ekranına yeni bir denetçi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload649fcbc0-84e3-4f1b-a654-91434876ec24) (yeni) butonu tıklanarak Denetçi Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload088ea52e-8823-4841-b847-4f7e7dfd65c7)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Denetçi:** Denetçiler sistemde tanımlı olan personel listesinden seçilebilir.

**Yetkin olduğu Yönetim Sistemleri:** Denetçinin yetkin olduğu yönetim sistemi sistemde tanımlı yönetim sistemlerinde seçilebilir. Hangi yönetim sistemlerinde hangi seviyede denetim yapabileceği bu alanda belirlenir.

**İş Yeri:** Denetçi ilgili iş yeri ile ilişkilendirilir. Denetçiler iş yerleri ile ilişkilendirildiğinde çoklu lokasyonlu firmalar için denetime denetçi atarken filtrelemede kolaylık sağlar.

Denetçi tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9a06a5f-eada-4440-9b1a-c5f91537761b)

### **1.1.6.Bulgu Tipleri Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Denetim Faaliyeti/ Bulgu Tipleri Tanımlama

Denetimde tespit edilen bulgu tiplerinin tanımlandığı menüdür. Majör, minör, gözlem vb. tanımlamalar yapılabilir. Belirlenen bulgu tiplerine göre Döf veya aksiyon açılabilir ya da kullanıcı seçimli yapılabilir. Tanımlanan bir bulgu tipinde, işlem tipi kullanıcı seçimli seçilirse ilgili bulgu için Döf veya Aksiyon açılması zorunlu tutulmamaktadır. Ancak bir bulgu tipi Döf veya aksiyon ile ilişkilendirilirse denetim gerçekleştirme aşamasında denetçinin Döf veya aksiyon açması zorunlu tutulur. Bu amaçlar doğrultusunda ilgili bulgu tipleri tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66327d7a-4e46-4f7b-8c45-a7e8aa6488a5)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8e4328a-9e67-4032-a0d3-cb1563f11895):Yeni bir bulgu tipi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec48601c-9d05-4228-9402-082a7b274c26):Listede seçili bulgu tipi bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload226e5457-2452-43b2-9ec6-8d80f7a901b0): Listede seçili bulgu tipi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8aabf1c-4e76-44e9-9439-da1b03499362) :Veriler Excel’e aktarılabilir.

Bulgu Tipi tanımlama ekranına yeni bir bulgu tipi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload649fcbc0-84e3-4f1b-a654-91434876ec24) (yeni) butonu tıklanarak Bulgu Tipi Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04df57fb-a13a-4801-b4d4-1082ea784c05)

**Açılan ekranda ilgili alanlar tanımlanır:**

**No:** Sistem tarafından otomatik verilir.

**Bulgu Tipi:** Tipi tanım bilgisinin girilir.

**İşlem Tipi:** Tanımlanan bulgu tipi Aksiyon/Döf Açılmasın, Kullanıcı Seçimli, Döf Açılsın ve Aksiyon Açılsın işlem tipi seçeneklerinden birisi ile ilişkilendirilir.

**Aksiyon Termin Süresi:** İşlem tipi aksiyon ile ilişkilendirildiğinde, açılacak aksiyonların termin süresi bu aşamada belirlenebiliyorsa değer girilir.

**Döf Termin Süresi:** İşlem tipi Döf ile ilişkilendirildiğinde, açılacak Döf’lerin termin süresi bu aşamada belirlenebiliyorsa değer girilir.

Bulgu Tipi Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb945293-b71e-4fd8-a3f0-552d0b776fa8)

### **1.1.7.Denetim Tipi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Denetim Faaliyeti/ Denetim Tipi Tanımlama

Kurumda gerçekleştirilen denetimlerin, türlerinin tanımlandığı menüdür. İç Denetim, Dış Denetim, Ürün Denetimi gibi.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f9cb00c-3940-4262-91b9-dcb17c1e6481)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8e4328a-9e67-4032-a0d3-cb1563f11895):Yeni bir denetim tipi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec48601c-9d05-4228-9402-082a7b274c26): Listede seçili denetim tipi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload226e5457-2452-43b2-9ec6-8d80f7a901b0): Listede seçili denetim tipi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8aabf1c-4e76-44e9-9439-da1b03499362): Veriler Excel’e aktarılabilir.

Denetim Tipi tanımlama ekranına yeni bir denetim tipi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload649fcbc0-84e3-4f1b-a654-91434876ec24) (yeni) butonu tıklanarak Denetim Tipi Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6fc8b21-70a6-4807-aabc-df45f8ead836)

**Açılan ekranda ilgili alanlar tanımlanır:**

**No:** Sistem tarafından otomatik verilir.

**Denetim Tipi:** Denetim tipi tanım bilgisinin girilir.

**İşlem Tipi:** Tanımlanan denetim için Kullanıcı Seçimli, Aksiyon ve Döf Açılmasın, Döf Açılsın, Aksiyon Açılsın seçeneklerinin seçilebildiği alandır.

Denetim tipi bazında, gerçekleştirilecek denetimlerin her bulgusu için Döf veya Aksiyon açılmasının zorunlu olduğu durumlarda, işlem tipi Döf veya Aksiyon seçilir, bunun dışında kullanıcı seçimli olarak varsayılan tanımlanmıştır. Kullanıcı seçimli olan durumlar için bulgu tipi bazında, seçilen Döf-Aksiyon açılma durumları geçerli olacaktır.

**Denetçi Soruları Değiştirimesin:** Tanımlanan denetim tipleri için denetçi denetim gerçekleştirme sayfasında soru ekleme ve çıkarma işlemi yapamaz.

Denetim Tipi Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e941e27-737b-4827-9f3f-b8914d83a7b2)

### **1.1.8.Denetim Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Denetim Faaliyeti/ Denetim Tanımlama

Denetim tanımlama işleminin gerçekleştiği menüdür. Bu menüde denetimler soru listeleri ve diğer seçenekler ile ilişkilendirilir. Denetim Havuzu oluşturulduğumuz kısımdır. Bu menüde tanımlanan denetim direk görev olarak düşüp gerçekleştirilecek denetim olarak düşmemektedir. Bu menüde tanımlanan denetim firmada bu denetim düzenli veya düzensiz olarak yapılır anlamına gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload27eb8de6-cf27-4fba-a530-48d15b7d88dc)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8e4328a-9e67-4032-a0d3-cb1563f11895):Yeni bir denetim tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec48601c-9d05-4228-9402-082a7b274c26):Listede seçili denetim bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload226e5457-2452-43b2-9ec6-8d80f7a901b0): Listede seçili denetim bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41f9f1d2-9ea8-489c-bc5a-7289573c60a9) :Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8aabf1c-4e76-44e9-9439-da1b03499362) :Veriler Excel’e aktarılabilir.

Denetim tanımlama ekranına yeni bir denetim eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload649fcbc0-84e3-4f1b-a654-91434876ec24) (yeni) butonu tıklanarak Denetim Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcb75acb2-b2a5-4268-81e3-115aa2575751)

Puanlı mı alanında ilgili check box işaretlendiğinde, ilgili soru listesi alanına puanlı soru listelerini getirecektir. Tersi durumda seçilmediğinde puansız soru listeleri seçilebilecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1df537f-1412-495d-8e62-1abee10dc5e5)

Soru Listesi Tanımlama menüsünde Puanlı olarak tanımladığımız Bayii Hijyen Denetim Soru Listesi seçildikten sonra Denetimiz Puanlı bir Denetim olarak tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload990cadb4-bcdb-4ee6-ba7f-c384e0ab87ec)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Denetim No:** Sistem tarafından otomatik verilir.

**Denetim Tanımı:** Denetim tanım bilgisinin girildiği alandır.

**Durum:** Denetimin aktif veya pasif bilgisi belirlenir.

**Denetim Tipi:** Denetim tipi bilgisinin seçilebildiği alandır. Örneğin Dış Denetim, İç Denetim, Proses Denetim vb.

**Plandaki Tekrar Sayısı:** Denetimlerin plana eklenirken kaç kez ekleneceği bilgisinin girildiği alandır.

**Puanlı Mı?:** Puanlı mı seçeneği işaretlendiğinde, ilgili soru listesi alanına puanlı soru listelerini getirecektir. Tersi durumda seçilmediğinde puansız soru listeleri seçilebilecektir.

**Plansız mı?:** Plansız seçeneği işaretlendiğinde ilgili denetim plansız denetimler menüsünde gözükecektir.

**İlgili Soru Listeleri:** Denetim Tanımlama ekranında puanlı ve puansız soru seçenekleri için ilgili soru listesi seçilir.

**İlgili Yönetim Sistemi:** Denetim, tanımlı yönetim sistemleri ile ilişkilendirilir.

**İlgili Departman:** Denetim, tanımlı departmanlar ile ilişkilendirilir.

**İlgili Süreçler:** Denetim, tanımlı süreçler ile ilişkilendirilir.

**İlgili Doküman:** Denetim tanımlama ekranında ilgili doküman bilgisinin sistemde tanımlı olan doküman listesinden seçilebildiği alandır.

**Denetim Detay Planı Şablonu:** QDMS denetim detay planı şablonlarını, standart formatında vermektedir. Rapor formatları tanımlama menüsüne denetim bazlı farklı formatlarda detay plan şablonları tanımlanabilir. İlgili denetim için kullanılacak detay şablonun, rapor formatları tanımlama menüsünden dosya adı yazıldığında o denetim için tanımlanan formatta detay plan çıktısı alınabilmesi sağlanır.

**Denetim Raporu Şablonu:** QDMS denetim raporu şablonlarını, standart formatında vermektedir. Rapor formatları tanımlama menüsüne denetim bazlı farklı formatlarda rapor şablonları tanımlanabilir. İlgili denetim için kullanılacak denetim rapor şablonunun, rapor formatları tanımlama menüsünden dosya adı yazıldığında o denetim için tanımlanan formatta denetim raporu çıktısı alınabilmesi sağlanır.

**Denetçi Soruları Değiştiremesin**: Bu seçenek işaretlendiğinde, denetçi denetim gerçekleştirme aşamasında soru ekleyip çıkaramaz.

Denetim Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86c35373-8ef5-42b9-81e7-70a7404548f4)

## **1.2.Entegre Yönetim Sistemi/Denetim Faaliyeti**

Denetim planlarının oluşturulduğu, planlı denetim ve plansız denetimin gerçekleştiği, raporların ve grafiklerin görüntülendiği kısımdır.

### **1.2.1.Denetim Planları**

**Menü Adı:** Entegre Yönetim Sistemi/Denetim Faaliyeti/Denetim Planları

Yıllık denetim planının oluşturulduğu menüdür. Denetim planı oluşturulduktan sonra planın içerisine denetimler eklenir. Denetim planları tarih veya denetim tipi bazınla oluşturulabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86f03565-165a-4fe4-b9a9-6ea629ce6eeb)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12dfc610-2de2-4a89-86a5-d881ed01e760):Yeni bir plan tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9049c960-de59-478b-b992-8c55b9c87a2c):Listede seçili plan bilgileri güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd63ec94e-d578-4dcf-bd86-3f7441095695):Listede seçili plan kaydı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf2ddf55-2d0b-4a35-a571-d3d3e603d88b): Listede seçili plan kopyalanarak yeni plan oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26630772-5af5-4756-a31e-3a1d06ac59ed):Denetim planındaki denetimler belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload519b7a3c-34b7-4205-97cc-a9c801981ed5):Plan-Ortak denetim planı görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7427fbc-21a9-4bfa-96d7-68736b6951be):Denetim planının denetim çizelgesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadebc5293a-d41c-4326-8def-14e040783f3e):Denetim bilgileri Excel ortamına aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload586ff707-d8f8-4f47-8956-31c975c25ddb) :Denetim plan ekranının tabloya aktarılmasını sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3227ddf-d693-4ecf-8499-a287be724060):Denetim planının yayınlanarak e-posta ile bildirimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41f9f1d2-9ea8-489c-bc5a-7289573c60a9):Kayıtlar filtrelenerek arama yapılabilir.

Denetim Planları ekranına yeni bir denetim planı eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload649fcbc0-84e3-4f1b-a654-91434876ec24) (yeni) butonu tıklanarak Denetim Planları/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42caef48-f472-43b7-8d46-9dfbdf1bc6a2)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Plan No**: Sistem tarafından otomatik verilir.

**Plan Tanımı:** Plan tanım bilgisinin girildiği alandır.

**Planın Başlangıç Tarihi:** Planın başlangıç tarihi girilir.

**Planın Bitiş Tarihi:** Planın bitiş tarihi girilir. Seçilen başlangıç ve bitiş tarihleri dışında plana denetim eklenemez.

**Denetçilere kaç gün önce haber verilsin? :** Denetçilere denetim tarihinden kaç gün önce mail ile bilgilendirme yapılması gerektiği tanımlanır.

**Denetlenenlere kaç gün önce haber verilsin? :** Denetlenen kişilere denetim tarihinden kaç gün önce mail ile bilgilendirme yapılması gerektiği tanımlanır.

**Denetim Kapatma Süresi:** Denetimin kapatılma süresi girilir.

**Bilgilendirilecekler:** Denetim planı yayınlandığında bilgilenecek kişilere mail ile duyurulur.

**Bilgilendirilecekleri plandaki tüm denetimleri yansıt:** Eklenen bilgileneceklerin tümünü plandaki tüm denetimlerin bilgilenecek kısmına yansıtır.

**Denetim Kodu Şablonu:** Denetim kodlarının otomatik verilmesi istenirse, kod yapısının formatı tanımlanır. Örn: 2020.\#\#\#

**Denetim Kodu Sayacı:** Denetim kodunun hangi sayıdan başlayacağı bilgisi girilir.

**Denetimleri Plana Otomatik Ekle:** Denetim planına, tanımlanmış tüm denetimleri otomatik olarak ekler, sonrasında denetimler güncellenerek tarihleri ve denetçi alanları güncellenir.

**Denetim Raporu Otomatik Oluşsun:** İlgili check box işaretlenirse denetim kapatma menüsünde denetim raporunun oluşması için butona tıklamaya gerek duyulmaz.

**Denetim Tipi:** Tanımlanan planın denetim tipi seçilir.

**İşyeri:** Denetim gerçekleşecek işyeri bilgisi seçilir.

Denetim Planları ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95577324-201d-42c4-b853-24d0ed3b053a)

### **1.2.1.1.Planda Yer Alan Denetimlerin Belirlenmesi**

Denetim planını yaptıktan sonra, planın içine denetim ekleme aşamasına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3d0d7c4-014d-4d3d-9f6a-886d945ed3b4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload733557a5-8e69-4b73-b5de-8e1d5470b503) Denetimler butonuna basılarak denetim ekleme sayfasına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload577f2313-925a-4914-966c-d6ed9cbe474c)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12dfc610-2de2-4a89-86a5-d881ed01e760): Yeni bir denetim kaydı tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload895774fb-8929-4daa-b72c-f23a8214d144): Denetim eklenerek denetim havuzundan çoklu seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9049c960-de59-478b-b992-8c55b9c87a2c): Listede seçili denetim kaydı bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf2ddf55-2d0b-4a35-a571-d3d3e603d88b): Listede seçili denetim kaydı kopyalanarak yeni kayıt oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3754d933-bdb6-4936-bf36-699e33d30015): Sorular butonu ile denetimde sorulacak sorular soru listesinden seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11bbb72b-ccb0-48a3-a158-c60bb1028e76): Denetim sonucunu göster butonu yardımıyla Denetim sonucu görüntülenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc809b06e-92dd-4dea-b72a-45b1afcdbd40): İptal-Öteleme butonu yardımıyla denetim ötelenebilir/ iptal edilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd63ec94e-d578-4dcf-bd86-3f7441095695):Sil butonu ile seçili kayıt silinir, ancak kaydın bir planda kullanılmamış olması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadebc5293a-d41c-4326-8def-14e040783f3e): Kayıtlar Excel ortamına aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3227ddf-d693-4ecf-8499-a287be724060):Denetim Planındaki seçili denetimler yayınlanarak e-posta ile bildirimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41f9f1d2-9ea8-489c-bc5a-7289573c60a9): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12dfc610-2de2-4a89-86a5-d881ed01e760): Yeni butonu tıklanarak denetim kaydı tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5fe605a-2001-463e-91cc-aa2fa91ae2ee) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload393a5555-4ca9-4ef7-9bcc-0b3d07a36b5a)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Denetim Kodu:** Denetim kod bilgisinin girildiği alandır. Otomatik kod şablonu belirlendiğinde kod girilmesi gerekmez.

**Denetim:** Altyapılardan tanımlanmış olan denetimler seçilir.

**Denetim Başlangıç Tarihi:** Denetim başlangıç tarihi girilir.

**Denetim Bitiş Tarihi:** Denetim bitiş tarihi girilir.

**Denetim Saati:** Denetim saati girilir.

**Denetim Konusu:** Denetim konusu girilir.

**Durum:** Yeni tanımlanan denetimler plan statüsü ile kayıt edilir. Denetimlerin durumu değiştikçe buradaki alan otomatik güncellenir.

**Baş Denetçi:** Denetçi listesinden baş denetçi seçilir.

**Denetim Ekibi:** Denetçi listesinden denetim ekibi belirlenir.

**Denetlenen birimin görüşü alınacak mı?:** Denetlenen birimin görüşleri alınacaksa ilgili check box işaretlenir.

**Denetlenen Birim Sorumluları:** Sistemde tanımlı olan personel listesinden sorumlular seçilir.

**Bilgiledirilecekler:** Denetimin aşamalarından mail ile bilgi sahibi olacak kişilerin seçildiği alandır.

**Ek Dosyalar**: Denetimde varsa ek dosya yüklenecek kısımdır.

**Kontrol Et:** Denetimlerde kişilerin verilen tarihlerde denetimlerinin olup olmadığı kontrol edilecekse ilgili check box işaretlenir.

**Denetimler Değerlendirilecek mi?:** Denetimlerin denetim sonunda anket ile değerlendirilmesi istenirse ilgili check box işaretlenir.

**Denetçiler Değerlendirilecek mi?:** Denetçilerin denetim sonunda anket ile değerlendirilmesi istenirse ilgili check box işaretlenir.

**Baş Denetçi İçin de Anket Oluşturulsun mu? :** Anketin baş denetçi içinde gönderilmesi istenirse ilgili check box işaretlenir.

Planda yer alacak her bir denetim kaydı oluşturulurken; denetimin adı, denetimin başlangıç ve bitiş tarihleri, saati, denetimin konusu, işyeri, baş denetçisi, denetim ekibi, denetlenen birim ve sorumluları, bilgilendirilecekler alanları belirlenir. Varsa ek dosya eklenir. QDMS bir kontrol yöntemi uygular; denetçi kendi birimini denetleyemez, aynı zamanda denetçi aynı gün içinde başka denetimde denetçi olarak seçilemez, eğer bu kontrolün yapılması isteniyorsa, sayfanın altındaki “Kontrol et” butonu işaretlenmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) Kaydet butonu ile denetim planın içerisine denetim kayıt işlemi gerçekleştirilir. Baş denetçinin ve denetim ekibinin “**Bekleyen İşlerim”** sayfasında **“Gerçekleştirilecek Denetim Listesi”** görüntülenecektir. Denetimin gerçekleşeceği tarihte sistem ilgili denetim kaydına ait bilgilendirmeleri, mail yolu ile iletecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d2da723-cc59-44b4-937b-f2d9b0fe86e7)

### **1.2.2.Bekleyen Denetimlerim**

**Menü Adı:** Entegre Yönetim Sistemi/Denetim Faaliyetleri/Bekleyen Denetimlerim

Baş denetçinin ve denetim ekibinin **“Bekleyen İşlerim”** sayfasında süresi yaklaşan denetim kayıtları listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8275ccfb-910f-4fec-8b8f-38765ab67382)

### **1.2.2.1.Denetimi Gerçekleştirme**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf2597b2-a5d0-4695-ab6f-f401d354c0ef)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2778747-f096-47b7-b8ae-25a66ad02ef9):Listede seçili denetimin denetim tarihi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload39c989a5-06e7-4c3e-a2c1-be266ffb3e8f):Listede seçili denetime yeni soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7afbbb56-8be1-440f-9ef1-a2b1bfc0c82c):Listede seçili denetimin detay planı oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76fd53ef-27a7-4a59-8839-42b506c9ac11):Listede seçili denetime ek dosya eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8161fd7e-5abd-4202-81d2-f397f81aab0e):Listede seçili denetim gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadebc5293a-d41c-4326-8def-14e040783f3e): Kayıtlar Excel ortamına aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41f9f1d2-9ea8-489c-bc5a-7289573c60a9): Kayıtlar filtrelenerek arama yapılabilir.

Denetimi gerçekleştirmek için, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec136f4a-e142-4a90-a105-938f1fdf5787) (denetimi gerçekleştir) butonu tıklanarak sırası ile cevaplar, bulgular, diğer bilgiler, varsa ek dosyalar girilir, son olarak denetim raporu hazırlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e32b7bc-5daa-4afb-b958-cf76bcf641dd)

Denetim puanlı yapıldığı için soruların tek sayfada cevaplansın (puanlı) özelliği işaretlenmişti. Sorular tek sayfadan cevaplansın özelliği puanlı soru listelerinde, seçeneklerin daha kolay işaretlenebilmesi için optik cevap anahtarı benzeri görünümünde Cevaplar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1fe5960a-0113-4bab-8b6f-e46b42c10013)

Cevaplar sekmesinde Puanlı Denetim olduğu için eklenen sorular ve sorulara verilecek seçenekler optik okuyucu şeklinde görüntülendiğinde soruya verilecek seçenek işaretlenir ve soru ile ilgili detaylar kısmına giriş yapılmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload72f995b1-de62-441e-9083-e7ae60f5b3ca) (detaylar) butonuna basılır. Çıkan sayfada, verilen cevap girilir. Döf veya Aksiyon açılacak ise ilgili check-box’ lar işaretlenir. Bulgu Tipi Tanımlama menüsünde tanımlanan İşlem tiplerine göre Majör bulgu tipi seçildiğinde Döf açılması zorunluluğu, Minör bulgu tipi seçildiğinde Aksiyon açılması zorunluğu, Olumlu bulgu tipinde kullanıcı seçimli olarak Döf ve Aksiyon açılması zorunluluk gerekmediği ya da Aksiyon ve Döf açılmaması seçilebilir. Sorunun Uygunluk durumu seçeneklerinde Uygun veya Uygun değil seçeneklerinden soruya uygun olup olmaması belirlenir. Sorunun seçilen seçeneğine bağlı bir ek dosya varsa ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0855db30-38d3-4bce-ad66-b3099b426f65)butonu ile ek dosya eklenir. Seçenekle ilişki kurulacak bir yönetim sistemi ve madde numarası varsa sistemde tanımlı yönetim sistemi ve madde numarası listesinden seçilerek ilişkilendirilir. Gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) (Kaydet ) butonu tıklanarak detaylar ilgili kayıt işlemi gerçekleştirilir.

1\. sorunun seçeneği için Bulgu tipi Minor seçildiğinde işlem tipi Aksiyon oluştur seçeneği işaretli olarak gelir ve seçeneğe bağlı olarak Aksiyon oluşturulur. Aksiyon oluştururken açılan Aksiyonun’ un Bitiş Tarihi, Aksiyon Sorumlusu ve Aksiyonu Yapacak kişi bilgilerin girildiği gibi alanlarla ilgili bilgiler değiştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3bace32d-1292-4601-b436-eda0c0916c10)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe65631f-5009-4b47-937d-0b984ffa29c3)

Sorunun seçeneğinde bağlı olarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc82efdc4-f211-445d-8b35-478c48a848d5) (Aksiyon oluştur) ikonu ile sorunun seçeneğine bir Aksiyon açıldığı kayıt işleminde sonra görüntülenir.

2\. sorunun seçeneği işaretlenerek Detaylar kısmında verilecek cevap bilgisi girilir. Uygunluk durumu seçeneklerinde uygun veya uygun değil seçeneklerinden seçim yapılır. Bulgu tipi Majör seçildiğinde işlem tipi Döf oluştur seçeneği işaretli olarak gelir ve Döf oluşturulur. Döf oluştururken açılan Döf’ün Termin Tarihi, Ekip Lideri ve Gelişme Tarihi gibi alanları ilgili bilgiler değiştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8a4a0ce-725f-465d-828f-117cb1d3172a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade9d3d648-2823-42ee-8834-5ee7a0964126)

Sorunun seçeneğinde bağlı olarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload499223ed-d021-4b6d-a754-cb87d4f465a1) (Döf oluştur) ikonu ile sorunun seçeneğine bir Döf açıldığını kayıt işleminde sonra görüntülenir.

3\. Sorunun seçeneği işaretlendikten sonra Bulgu Tipi Minor seçilerek Aksiyon oluşturur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc1f36f9-471a-4f07-a651-1434717d062c)

Cevaplar sayfasında, Düzeltici faaliyet açılan sorular ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload499223ed-d021-4b6d-a754-cb87d4f465a1) (Döf oluştur) ikonu ile aksiyon açılanlarda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc82efdc4-f211-445d-8b35-478c48a848d5)(Aksiyon oluştur) ikonu ile gösterilmektedir.

Bulgular sekmesi tıklanarak cevaplar ile ilgili uygunsuzluk var ise bulgu açılabilir.

**Bulgular**

Denetimde tespit edilen bulgular girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f881160-5a58-4a1e-a681-a0e6f75924b1)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12dfc610-2de2-4a89-86a5-d881ed01e760):Yeni bir bulgu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9049c960-de59-478b-b992-8c55b9c87a2c): Listede seçili bulgu bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload687fadb6-4bc0-47e4-b0d7-0fab549a8ae5): Listede seçili bulgu bilgisi kopyalanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd63ec94e-d578-4dcf-bd86-3f7441095695): Listede seçili bulgu bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf3967c30-73fa-489e-a3e4-7c5493deec36) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9f3e905-6e99-403e-a8ad-1db7761e40f2)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Bulgu No:** Sistem tarafından otomatik olarak verilir.

**Bulgu Özeti:** Bulgu Özeti girilir.

**Bulgu Detay:** Bulgu detayı girilir.

**Bulgu Tipi:** Bulgu tipi seçilir. Seçilen tipe göre düzeltici faaliyet veya aksiyon tanımlanabilir.

**İlgili Soru:** Bulgunun ilgili olduğu soru seçilir.

**İlgili Madde Numaraları:** İlgili madde no bulgu ile ilişkilendirilir.

**İlgili Dokümanlar:** İlgili doküman bulgu ile ilişkilendirilir.

**Ek Dosyalar:** Bulgular sekmesinde ilgili ek dosya varsa ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload297a2e08-0db9-4c23-bf44-7556e0b314ba)Dosya Seç/Yeni Kayıt ekranında sisteme yüklenilir.

Açılan ekranda bulgu özeti ve detayı girilir. Bulgu tipi seçilir. Belirlenen bulgu tiplerine göre bulgular için Döf oluştur check box’ı işaretlenerek düzeltici faaliyet başlatılır, aksiyon oluştur check box işaretlenerek ile de aksiyon başlatılabilmektedir. Örneğin bulgu tipi olarak minör seçildiğinde, Sistem Altyapı Tanımları/Denetim Faaliyeti/Bulgu Tipleri Tanımlama menüsünde minör tanımlı bulgu tipi için işlem tipi aksiyon açılsın, seçili ise bulgular sayfasında aksiyon oluştur alanı ile ilgili check box gelmesi sağlanır. Bulgu tipi majör olarak seçildiğinde, Sistem Altyapı Tanımları/Denetim Faaliyeti/Bulgu Tipleri Tanımlama menüsünde majör tanımlı bulgu tipi için işlem tipi Döf açılsın seçili ise bulgular sayfasında Döf oluştur alanı ile ilgili check box’ın gelmesi sağlanır. İlgili soru kısmı eğer cevaplar sayfasından açıldıysa otomatik gelir, direkt bulgular kulakçığından açılıyorsa kendimiz seçeriz. Bulguların, ilgili madde numaraları, ilgili dokümanlar, ek dosyalar alanlarıyla ilişkilendirilmesi isteniyorsa bu alanlara ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda83de9e-1db3-4c2e-b476-095587e82364)(ekle) butonuyla madde numarası, doküman ve ek dosya ekleyebiliriz. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a610bf7-33fb-45a6-9a1e-8172045a9f71) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77f95398-e038-4ebf-a3cb-15f06988ead6)

**Diğer Bilgiler,**

Diğer bilgiler sekmesinde ilave bilgiler ve notlar eklenebilir. Bu sekmeye alan eklenilmesi isteniyorsa SAT/ Bsat/ Konfigürasyon Ayarları/ Dil Ayarları menüsünden düzenleme yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload433791e4-ff67-4e33-afba-35993c14ef65)

**Ek Dosyalar**

Ek dosyalar sekmesinde denetimle ilgili ek dosya eklenmek isteniyorsa eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1c31561-c998-4662-aabf-56d685a8c01e)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5d9d441-75bc-4406-8e91-f0533eb88c5d):Yeni bir ek dosya eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc69e3be9-98c9-4581-bc7f-09f9e788fd91):Listede seçili ek dosya görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd63ec94e-d578-4dcf-bd86-3f7441095695):Listede seçili ek dosya silenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5d9d441-75bc-4406-8e91-f0533eb88c5d)Yeni butonu tıklanarak denetimle ilgili ek dosya eklenilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e9e652c-15e4-4a44-a486-ac40fcbd7a08)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f0b411a-ebe5-4094-bdae-93e636b62700)

**Denetim Raporu,**

Denetime ait bilgiler girildikten sonra denetim raporu oluşturulup denetim kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f241ecc-370b-4f6e-b281-2c2920820f77)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc9be39d-6099-429f-acf5-95a8d15b4c61):Denetim raporu oluşturur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94ce81c3-cd88-4159-b77b-501e9550dd7a):Denetim raporu ek dosyalarla indirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f877a1a-a7e0-4872-abda-2c77aebab60f): Denetim raporu yayınla butonu ile rapor e-posta olarak paylaşılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2723313c-57c5-4bca-b512-70b4520c4ddd): Denetim işlemleri kapatılarak, denetim sonuçlandırılmış olur.

Denetim raporu sekmesine gelindikten sonra, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc9be39d-6099-429f-acf5-95a8d15b4c61)(denetim raporu oluştur) butonuna tıklanır. Denetim raporunu oluşturmak istediğinizden emin misiniz? Mesajına tamam denildikten sonra denetim raporu başarıyla oluşturulmuştur

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload266e2cdf-2296-4018-8011-6a3997f7d997)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8dbd08b0-c577-43ee-a46b-a1f7cbde7019)

İlgili linke tıklayarak denetim raporuna ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e391413-34dd-4bc2-b743-2365bce40bf7)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49635a6d-389d-4e63-9ac8-35c53156490b) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1185de1-bfac-46db-8f2b-b87374aa6574)

**Denetimi Kapatma**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbaa9e46b-7580-44fd-a1db-71313f4c78ae) Denetim kapat botunu tıklanır. Denetim kapatma onayı kurgulanmış ise, denetim onay için bekleyen işlerime “Onay bekleyen Denetimler Listesi” olarak düşer. Aksi durumda onaya düşmeden denetim kapatılır ve kapatılma bilgisi ilgili kişilere mail ile duyurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload012c4e51-6438-4036-a7a2-f4509d91e300)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ec28f68-b2ed-4d29-bf28-34e58ce1e46b)

Onay bekleyen denetimler listesinde denetim kodu üzerindeki link tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc2e1beb-2801-423e-a532-92cce33906e3)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19a176dd-135c-4493-aa9b-eb7d22374a24)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcb2bf86f-1d56-463e-a7d6-f9f0fb53ae87)**:**Denetimi gerçekleştirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9ea36e0-f48c-4f0f-88f8-b359ec61f3ab): Seçili denetim onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63e51b49-5a31-4c55-86da-fdb021d2f31b): Seçili denetim reddedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41f9f1d2-9ea8-489c-bc5a-7289573c60a9): Kayıtlar filtrelenerek arama yapılabilir.

Onay bekleyen listede seçili denetimi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63e51b49-5a31-4c55-86da-fdb021d2f31b) (ret et) butonu tıklanarak reddedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbeb44043-079d-4226-b66d-c1c27af63d7d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f805feb-1284-4326-ae6d-156ecf165b36)

Onay bekleyen listede seçili denetimi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9ea36e0-f48c-4f0f-88f8-b359ec61f3ab)(onay) butonu tıklanarak denetim kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31689b10-b311-47b8-94ce-c79ca3b29e10)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9f3d368-bf97-453f-aef9-d96ab9ab12b2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f31ff90-8dce-4d1b-ba1d-180528ec656a)
