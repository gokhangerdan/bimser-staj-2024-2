# eBA Doküman Yönetimi: Oluşturma İş Akışı Dokümanı 

## Doküman Yönetiminde Oluşturma İş Akışını Seçme 

Doküman Yönetimine yeni doküman eklendiğinde istenilen kullanıcı/kullanıcılar onayına kazandırılan doküman gönderilerek yeni bir akış tetiklenebilir. Böylece doküman eklenir eklenmez akış tetiklenecktir. Bu işlem için yeni dokümanın eklenmesi yeterli olacaktır. 

Doküman yönetiminde kütüphane ve dizinlere eklenen doküman için oluşturma iş akışı sürecini seçmek için Şekil 1’de, ilgili nesne seçildikten sonra Özellikler tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%201-d70b5ae6-6792-45ba-a12f-83b52b77b614.png)

Şekil 2’de, Doküman sekmesi altında Oluşturma İş Akışı başlığı altında oluşturma işleminin başlatacağı süreç seçildikten sonra Kaydet butonuna tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%202-367ef79f-5a22-4bce-ad13-04e91b23d02e.png)

## 1.2. Oluşturma İş Akışı Sürecini Tasarlama 

Workflow Studio’da oluşturma iş akışı için yeni bir süreç tanımlanır. Yapılacak örnek süreçte, doküman eklendiğinde önce Kalite Uzmanı onayına doküman sunulacak ve süreci onaylaması ile seçilen kullanıcılara doküman bilgilendirme olarak gönderilecektir. Yeni bir süreç oluşturduğumuzda varsayılan olarak gelen Doküman Oluştur ve Doküman nesneleri akıştan silinir. Çünkü var olan doküman sürece eklenecek, yeni bir doküman oluşmayacaktır. Akış, Şekil 3’teki gibi tasarlanacaktır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/ŞEkil%203-8ce46fcf-a2ea-4ef2-a397-ba558af5a5ca.png)

Akışa yeni bir değişken eklenir. Bu değişken adının filename olması zorunludur. Akış tetiklendiğinde bu değişkene eklenen dokümanın yol bilgisi eBA tarafından atanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%204-ac971a6c-b5f3-4def-b08a-7f2f1a87715d.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%205-ad5d81ba-ce03-4f6d-9666-2177f317d75b.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%206-51a34af2-b42d-427b-aa63-11ac0959ec5f.png)

Alan referanslar eklenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%207-e747dd8d-fcf4-4406-b1d3-b2f28f76e828.png)

eBAPI.dll dosyası sürece eklenir. Şekil 8’de, ilgili süreç üzerinde sağ tuş tıklanarak Proje Özellikleri tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%208-65752606-8c60-430e-938b-47eac16a2e84.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%201-d70b5ae6-6792-45ba-a12f-83b52b77b614.png)

Pozisyona tanımlanır. Şekil 10’da, pozisyon nesnesine çift tıklanarak Özellikler penceresi açılır. Dokümanlar sekmesinde 3 numaralı ikon tıklanarak eklenen doküman nesnesi seçilir. Aynı işlem Bilgilendirme nesnesinde de yapılarak bilgilendirme kullanıcılarının dokümanı görüntülemesi sağlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2010-44e4f071-f459-4557-b0c1-78672f3828d9.png)

Yapılan işlemlerden sonra proje derlenir ve kaydedilir. 



![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2011-3adc9029-aefd-47b4-b60e-f13352826120.png)

Tıklanarak Zaman aşımı olmuş olayı eklenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%201-d70b5ae6-6792-45ba-a12f-83b52b77b614.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2012-dfc6db03-2f68-44b3-9246-bad57f629b52.png)

Az sürede devam etmesi için 1 dakika yazıldıktan sonra Tamam tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2013-ed71ffec-4e93-4644-8cb2-74a771a5f34b.png)

Tanımlanan profil formuna ait süreç, form ve view seçilir. Bu şekilde profil formunun alanlarına eklenen doküman nesnesi ile erişilecektir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2014-ba75aeee-d688-4ff5-bc77-2240eddca14e.png)

Bağlantı alanı seçilir. 3 numaralı alandan eklenen profil dokümanı, 4 numaralı alandan formda bulunan nesne seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2015-5a74ccca-af6e-4867-a6d0-d810cab098a5.png)

Karşılaştırma yapılacak değişken seçildikten sonra 4 numaları alana koşullar eklenir. Yapılan örnekte, 50’den büyükse koşulu eklenmiştir. Birden fazla koşul eklenebilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2016-00142846-fb40-48d5-8da8-758d6612118d.png)

 1 numaralı alandaki kod Fonksiyon nesnesinin içine yazılır. Yazılan kodda, açılan bağlantı ile doküman yönetimine bağlanır.GetFile ile filename değişkenindeki doküman, faturadokümanı adlı değişkene alınır. Akışa eklediğimiz profilFormu adlı doküman nesnesine, doküman yönetimine eklenen dosyanın profil formunun yolu atanır. Böylece, dokümana ait eklenen profil formuna erişilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2017-99a02df1-b900-43c1-abb3-1778e4310541.png)

eBA’da oluşturulan süreçler ve süreçlere ait formlar doküman yönetiminde workflow  kütüphanesinde form numarası ile birlikte ”.wfd” uzantılı olarak tutulur. faturaDokumanı.Profile ile dokümana ait profil formunun ID bilgisi alınır. Aşağıdaki kod ile profilFormu adlı dokümanın yol bilgisine, eklenen doküma ait profil formunun yol bilgisi atanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2018-73c53d7f-03c2-4e4b-a834-2238e5666e89.png)

Tıklandığında tanımlanan profil formu açılacaktır. Formdaki alanlar doldurulup Son tıklandığında hem doküman eklenecek hem de tanımlanan oluşturma iş akışı tetiklenecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2019-9d36b5b6-2ab8-47af-be32-fb16c44fe7a2.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2020-868184e1-3622-4abd-a73b-1bf11ebe2066.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2021-c9ca5f95-1dd1-4526-8b98-8b5d90da7ebb.png)

Doküman yönetimine eklenen dokümanı görüntülemektedir. Oluşturma Sürecini Göster butonu ile Akış tarihçe ve Akış Şeması görüntülenir. Onayla butonu ile akış ilerletilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2022-cd7f9985-3987-42e7-8817-72993f21beb5.png)

Not: Kullanıcı kendisine gelen dokümanı görüntüleyebilmesi için Doküman Yönetimin’de Güvenlik altında görüntüleme yetkisinin tanımlanması gerekmektedir. Yetki tanımlanmamış ise kullanıcı dokümanı  görüntüleyemecektir. Yetkilendirme işleminin nasıl yapıldığı eBA Doküman Yönetimi:Yetkilendirme Dokümanı’nda anlatılmaktadır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2023-5c5d5a28-07f2-45de-b887-a864b0d29ba2.png)

Nesnesinden sonra akış bu değere göre ilerlemiştir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil%2024-7f625329-003a-430a-a38f-b5b820c49726.png)