# eBA Doküman Yönetimi: Yayınlama İş Akışı Oluşturma Dokümanı

## GİRİŞ

eBA Doküman Yönetimi: Yayınlama İş Akışı Oluşturma dokümanında; doküman yönetimine
kazandırılan doküman için yayınlama iş akışını oluşturma ve dokümanı yayınlama işlemlerinin nasıl yapıldığı anlatılmaktadır.


## 1. eBA Yayınlama İş Akışı Oluşturma

### 1.1	Doküman Yönetiminde Yayınlama İş Akışını Seçme

Doküman Yönetimine kazandırılan doküman istenilen kullanıcı/kullanıcılar onaylarına gönderilerek onaylardan sonra belli bir kullanıcı grubuna bilgilendirme olarak gönderilebilir. Bu işlem için doküman eklendikten sonra tanımlanan yayınlama iş akışı Yayınla butonun tıklanmasıyla başlatılır.
Doküman yönetiminde kütüphane ve dizinlere eklenen doküman için yayınlama iş akışı sürecini seçmek için Şekil 1’de, ilgili nesne seçildikten sonra Özellikler tıklanır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%201:%20Özellikler%20Ekranı-cf1a0fc0-ce7f-427b-b7cb-c6cc3b974c6e.png)

Şekil 1: Özellikler Ekranı

Şekil 2’de, Doküman sekmesi altında Yayınlama İş Akışı başlığı altında yayınlama işleminin başlatacağı süreç seçildikten sonra Kaydet butonuna tıklanır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%202:%20Yayınlama%20İş%20Akışını%20Seçme%20Ekranı-1cc0f999-71e5-4311-886e-de868cd91877.png)

### 1.2	Yayınlama İş Akışı Sürecini Oluşturma

Workflow Studio’da yayınlama iş akışı için yeni bir süreç tanımlanır. Yapılacak örnek süreçte, doküman yayınlanmlak istendiğinde önce Kalite Uzmanı onayına doküman sunulacak ve süreci onaylaması ile seçilen kullanıcılara doküman bilgilendirme olarak gönderilecektir. Yeni bir süreç oluşturduğumuzda varsayılan olarak gelen Doküman Oluştur ve Doküman nesneleri akıştan silinir. Çünkü var olan doküman sürece
eklenecek, yeni bir doküman oluşmayacaktır. Akış, Şekil 3’teki gibi tasarlanacaktır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%203:%20İş%20Akışı%20Tasarım%20Ekranı-c9d70e7f-e415-4fa3-99c3-51671994bd03.png)

Şekil 3: İş Akışı Tasarım Ekranı

Akışa yeni bir değişken eklenir. Bu değişken adı filename olması zorunludur. Akış tetiklendiğinde bu


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%204:%20Dosya%20Değişkeni%20Ekleme%20Ekranı-2c48fa74-c002-4323-ba33-0022c62f9ef2.png)

Şekil 4: Dosya Değişkeni Ekleme Ekranı

Değişkene dışarıdan ulaşılabilir olması için, Şekil 5’te, Bağlantı sekmesinde Genel seçeneği işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%205:%20Dosya%20Değişkeni%20Genel%20Ekranı-c2ef86e7-9e3c-4c6f-96a4-c5cc439b022a.png)

Şekil 5: Dosya Değişkeni Genel Ekranı

Şekil 6’da, yeni bir doküman nesnesi eklenir. Doküman adı istenildiği gibi verilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%206:%20Yeni%20Doküman%20Nesnesi%20Ekleme%20Ekranı-60d89508-76a6-49d9-9db7-9b9f0996a540.png)

Şekil 6: Yeni Doküman Nesnesi Ekleme Ekranı

İş akışına eklenen fonksiyon içerisine Şekil 7’deki 2 numaralı alandaki kod yazılır. 1 numaralı alanda yer 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%207:%20İş%20Akışı%20Kod%20Ekranı-46d53fe2-811a-465a-b054-50477b7a8e8e.png)

Şekil 7: İş Akışı Kod Ekranı

eBAPI.dll dosyası sürece eklenir. Şekil 8’de, ilgili süreç üzerinde sağ tuş tıklanarak Proje Özellikleri tıklanır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%208:%20Proje%20Özellikleri%20Ekranı-47f7032f-b5ab-4c0a-8687-d6f750035fe1.png)

Şekil 8: Proje Özellikleri Ekranı



![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%209:%20Yeni%20DLL%20Ekleme%20Ekranı-af1793db-e065-4e87-a6b3-fc4229ce6c05.png)

Şekil 9: Yeni DLL Ekleme Ekranı

Süreç onaya gönderildiğinde Kalite Uzmanının dokümanı görüntüleyebilmesi için eklenen doküman nesnesi pozisyona tanımlanır. Şekil 10’da, pozisyon nesnesine çift tıklanarak Özellikler penceresi açılır. Dokümanlar
sekmesinde 3 numaralı ikon tıklanarak eklenen doküman nesnesi seçilir. Aynı işlem Bilgilendirme nesnesinde
de yapılarak bilgilendirme kullanıcılarının dokümanı görüntülemesi sağlanır.



![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2010:%20Pozisyon%20Nesnesi%20Doküman%20Ekleme%20Ekranı%20-a1f16b8a-7b90-4ddd-961d-56a5803e11af.png)

Şekil 10: Pozisyon Nesnesi Doküman Ekleme Ekranı

Yapılan işlemlerden sonra proje derlenir ve kaydedilir. Doküman yönetiminde yayınlama iş akışı başlatacak doküman açılır. Yayınla butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2011:%20Dokümanı%20Yayınlama%20Ekranı-7b3a8062-e2d5-4a1d-9d1b-a97a32762325.png)

Şekil 11: Dokümanı Yayınlama Ekranı

Şekil 12’de, akışta seçilen kullanıcının Onaylar kutusunda seçilen yayınlama akışı tetiklendi. Kullanıcı süreci görüntülediğinde yayınlanan pdf dosyasını görüntüleyecektir. Süreci onaylaması ile akış bilgilendirme kullanıcılarının Bilgilendirmeler kutusunda görünecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2012:%20Kullanıcı%20Onaylar%20Ekranı-46f6e0fb-bf2b-4957-903a-b0dda1b9b9f1.png)

Şekil 12: Kullanıcı Onaylar Ekranı

Yapılan örnek süreçte Kalite Uzmanı sadece yayınlanan dokümanı görüntüledi ve doküman akışta
bilgilendirme nesnesine eklenen kullanıcılara gönderildi. Eğer istenirse, Kalite Uzmanı onayına yayınlanacak doküman ile birlikte sürece ait form görüntülenerek bilgilendirme kullanıcılarını seçmesi ve bu kullanıcılara dokümanın bilgilendirme olarak gönderilmesi sağlanabilir.
Şekil 13’teki gibi akışa Doküman, Doküman Oluştur ve Fonksiyon nesneleri eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2013:%20Akışa%20Yeni%20Nesneler%20Ekleme%20Ekranı-606cc9d1-ec7b-4651-86e3-4057b6bfc127.png)

Şekil 13: Akışa Yeni Nesneler Ekleme Ekranı

Şekil 14’de, eklenen eBAForm adlı doküman nesnesine çift tıklanarak kullanıcıya gösterilecek süreç ve form seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2014:%20eBA%20Form%20Dokümanı%20Ekleme%20Ekranı-927604d0-4cf4-4b62-86a8-3294a45a1191.png)

Şekil 14: eBA Form Dokümanı Ekleme Ekranı

Şekil 15’te, eklenen Doküman Oluştur nesnesi ile oluşturulacak doküman nesnesi seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2015:%20Doküman%20Nesnesine%20Form%20Ekleme%20Ekranı-fcfdd9d5-5bb9-41b4-a6ca-7b4abdeeaa48.png)

Şekil 15: Doküman Nesnesine Form Ekleme Ekranı

Şekil 16’da, Bilgilendirme nesnesine form tarafına eklenen tablodaki kullanıcı atamak için nesne çift tıklanarak açılır. 2 numaralı alandaki butona tıklanır. Açılan pencerede From Document Object seçeneği seçildikten sonra İleri butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2016:%20Bilgilendirme%20Nesnesi%20Ekranı-d403703c-e625-490d-ada2-d49d8f31e198.png)

Şekil 16: Bilgilendirme Nesnesi Ekranı


Şekil 17’de, 1 numaralı butona tıklanarak nesnenin bulunduğu form seçilir. Object Type alanından
kullanıcıların tablo mu yoksa detaylar nesnesinden ekleneceği seçilir. Örnek süreçte tablo nesnesi eklendiği için Table Object seçeneği seçilir. Seçilen nesneden kullanıcı mı yoksa pozisyon bilgisi alınacağı Data Type
alanından seçildikten sonra İleri butonuna tıklanır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2017:%20Bilgilendirme%20Nesnesi%20Ekranı%202-065b59b2-151a-4679-8f49-c58c63bd983d.png)

Şekil 17: Bilgilendirme Nesnesi Ekranı 2

Şekil 18’de, 1 numaralı alandan formdaki tablo nesnesi, 2 numaralı alandan tabloda yer alan alanlardan
kullanıcı koduna karşılık gelen alan seçildikten sonra Bitir butonuna tıklanır.




![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2018:%20Bilgilendirme%20Nesnesi%20Ekranı%203-88793548-3688-4383-834a-3f84f5ee6480.png)

Şekil 18: Bilgilendirme Nesnesi Ekranı 3

Şekil 19’da, 1 numaralı alana eklenen tablo nesnesi alınacak kullanıcı bilgi alanı görünmektedir. Tamam
butonuna tıklanarak pencere kapatılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2019:%20Bilgilendirme%20Nesnesi%20Ekranı%204-3e497ffd-1f43-4793-88e9-37565bb3f7c1.png)

Şekil 19: Bilgilendirme Nesnesi Ekranı 4

İlgili pozisyonda oluşturulan formu göstermek için eklenen eBAForm adlı doküman nesnesi eklenir.
Şekil 20’de, Kalite Uzmanı adlı pozisyon nesnesine çift tıklanarak Dokümanlar nesnesi altında Ekle ikonu ile doküman nesnesi seçilir. Düzenleme seçeneğinin seçilmesi ile kullanıcı doküman üzerinde değişiklik yapma yetkisi verilir.



![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2020:%20Pozisyon%20Nesnesi%20Doküman%20Ekleme%20Ekanı%202-0bee5309-7a4a-4f1b-b08f-0d5e35f1115b.png)

Şekil 20: Pozisyon Nesnesi Doküman Ekleme Ekanı 2

Doküman Yönetiminde ilgili doküman için Yayınla butonuna tıklanıldıktan sonra ilgili pozisyon onayına Şekil 21’de, 1 numaralı alanda eBA Formu ve ilgili pdf dosyası listelenir. Kullanıcı istediği dokümanı
görüntüleyebilir. Değişiklik Yap butonuna tıklanarak form üzerinde düzenleme yapılabilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2021:%20Kullanıcı%20Akış%20Görüntüleme%20Ekranı-628897b3-90af-4ae5-bd28-ac2b7053bd5d.png)

Şekil 21: Kullanıcı Akış Görüntüleme Ekranı

Şekil 22’de, tablo nesnesine bilgilendirmenin gönderileceği kullanıcılar eklendikten sonra Onayla butonu ile akış ilerletilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2022:%20Bilgilendirme%20Kullanıcısı%20Ekleme%20Ekranı-db4fb470-ff24-4460-b65c-108d0ba474ea.png)

Şekil 22: Bilgilendirme Kullanıcısı Ekleme Ekranı

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2023:%20Akış%20Tarihçesi%20Ekranı-a09ae063-3f74-4a44-9584-49b4e8ec6fbf.png)

Şekil 23: Akış Tarihçesi Ekranı

İlgili doküman yaınlandıktan sonra Doküman Yönetiminde, Yayınlanmış alanında yayınlama bilgisi tutulur.
Yayınlama akışı bulunan dökümanlar için yayınlama değerinin true olarak ayarlanması için akış tarafına
eklenen bir fonksiyon nesnesi ile akışın istenilen adımında true değeri atanır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2024:%20Doküman%20Yönetimi%20Ekranı-76105580-e470-447b-9b87-08dee96c92f6.png)

Şekil 24: Doküman Yönetimi Ekranı

Akışa eklediğimiz Fonksiyon 2 nesnesine Şekil 25’teki kod yazılır. Bu kod akışa eklenmezse Doküman
 Yönetiminde Yayınlanmış alanı ilgili doküman için false olarak kalacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2025:%20Yayınlamış%20Kodu%20Ekleme%20Ekranı-eb6fcd64-5584-47ad-b11c-3b489c0aa435.png)

Not: Kullanıcı kendisine bilgilendirme olarak gelen dokümanı görüntüleyebilmesi için Doküman Yönetimin’de
Güvenlik altında görüntüleme yetkisinin tanımlanması gerekmektedir. Yetki tanımlanmamış ise kullanıcı
dokümanı görüntüleyemecektir. Yetkilendirme işleminin nasıl yapıldığı eBA Doküman Yönetimi:Yetkilendirme Dokümanı’nda anlatılmaktadır.