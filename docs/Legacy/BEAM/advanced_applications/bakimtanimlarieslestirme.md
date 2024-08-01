# Bakım Tanımlarını Eşleştirme

İş talebi ve iş emri kartı içerisinde süreçleri ilerletirken iş tipi, bakım arıza kodu vb. alanların veri girişi yapılır ve liste üzerinden uygun olan tanımlar seçilir. Bu tanımlar arasında eşleştirme yöntemiyle tanımların seçimi sırasında otomatik olarak filtreleme yapılması mümkündür.

Örneğin, iş talebi oluşturulurken içerisinde Switch Arızası olarak seçilmiş olan Bakım/Arıza Tanımı alanı, sonrasında teknisyen switch arızasının nedenini bulunca seçeceği arıza nedenleri listesinde sadece Switch Arızasına neden olabilecek arıza nedenlerini görüntüleyebilir. Aynı şekilde bu eşleştirme yapıldığında diğer arızalarda görünmesi engellenebilir. Bu sayede arıza nedenlerini listelerken sisteme eklenen alakalı alakasız tüm tanımların listelenmesi yerine switch arızası ile alakalı olanları gösterilmesini sağlayarak kullanıcıya kolaylık sağlanabilir. Bir tanım birden fazla tanımla eşleştirilebilir.

Bu işlemi yapabilmek için eşleştirelecek olan tanıma gidilir, tanım içerisinde yer alan sekmelerden uygun olanında eşlecek diğer tanım seçilir ve kaydedilir. Eğer sekme bulunmuyorsa, eşleştirme diğer tanımın içerisinde yer alıyor olabilir.

Yukarıdaki Örneğin benzerini iki tanım için gerçekleştirelim;

Bakım/Arıza Tanımı: REDÜKTÖR ARIZASI

Arıza Nedeni: REDÜKTÖR DİŞLİ SIYIRMASI

Bu iki tanımı eşleştirmek için, arıza nedeni tanımına gitmek gerekmektedir. Eşleştirmenin hangi tanımda olduğun anlamak için tanımların kartı içerisinden kontrol edilebilir.

Bakım Yönetimi > Tanımlar > Arıza Nedenleri sayfasından Redüktör Dişli Sıyırması tanımını bulup değiştir butonuna tıklayınız.

![](https://docsbimser.blob.core.windows.net/imagecontainer/1-1b1c736e-51d6-45f6-bfae-218fa078b9ef.png)

Açılan ekranda ilgili arıza nedeninin “Genel Bilgiler” sekmesi açılacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/2-1bf10e20-e675-4f1e-aaa1-ef97cab32ad2.png)

Sekmelerden “Kullanabileceği Bakım Kodları” sekmesine geliniz.
Sonrasında Bakım Arıza kodu ile eşleştirebilmek için “+” butonuna tıklayarak ilgili tanımı seçiniz. (Diğer butonlar sırasıyla, değiştir, seçili satırı sil, tüm listeyi sil anlamına gelmektedir)

![](https://docsbimser.blob.core.windows.net/imagecontainer/3-0c29ddd7-30cc-4764-ac2c-84f130d23cf1.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/4-1ec26415-9f62-47f3-829c-5734f699aa50.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5-6820cf2b-38a1-40fa-9206-3fbb1d739ef9.png)

### ÖNEMLİ: Eğer tablo eklediğiniz veriyi direkt onaylamadıysa onay tuşuna basarak eklediğiniz bilgiyi kaydediniz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/6-dcc5ef54-72c6-44cc-bd56-2d940a5ddbeb.png)

Tanımın içerisinde kaydettiğiniz değişiklik sonrasında tanım kartının kendisini de kaydediniz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/7-0ce45766-67a3-4df6-839c-fa1e757d6227.png)

Bu işlem sonrasında, “redüktör dişli sıyırması” sadece redüktör arızası seçilirse görünecektir.
Redüktör dişli sıyırması tanımını redüktör arızası dışında görünmesini engellendi.

Redüktör Arızası seçildiğinde hiç eşleştirilmemiş tanımlar ve sadece redüktör arızasıyla eşleştirilmiş olan arıza nedenlerini görüntüler. Eğer sadece eşleşmiş olanların görünmesi talep ediliyorsa aşağıdaki çözümü uygulayınız:

Sistem>Şirketler>İlgili Şirket’e değiştir ile tıklayın> Parametreler sekmesinde aramaya arıza nedeni yazın. Çıkan sonuçlardan resimde gösterilen parametreyi işaretleyiniz.
Bu sayede eşleştirilmesi olmayan arıza nedeni eşleştirme yapılana kadar gözükmeyecektir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/8-0003fe8f-6867-49a3-831c-9cd36922476c.png)

Benzer şekilde, hangi eşleştirme yapılıyorsa parametreler alanında eşleştirmeyle parametre bulunabilir.

Eşleştirme yapılabilecek tanımları aşağıda bulabilirsiniz;

![](https://docsbimser.blob.core.windows.net/imagecontainer/9-37611ecb-ac0c-4c04-9d9a-4cdf1b307be6.png)

Not: Bakım/Arıza Kodu içerisinde “Kullanılabileceği iş tipleri” bulunurken, iş tipi içerisinde bakım arıza kodunu eşleştirebileceği bir alan bulunmamaktadır. Bu nedenle eşleştirme hangi kartın içerisinde yapılacağını kontrol etmek gerekmektedir.

En sık yapılan eşleştirmeler için diagram;
Diagramdaki ok yönlerinden, Bakım arıza kartı içerisinden iş tipini eşleyebileceğimiz anlaşılmaktadır. Aynı zamanda Bakım arıza kodunu arıza nedenleriyle eşleştirmek için arıza nedeni kartı içerisine gitmek gerektiği okun yönü ile anlaşılmaktadır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/10-a18e6105-2014-4bf8-b295-b8825531693f.png)

