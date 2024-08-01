---
title: Sistem Altyapı Tanımları
description: Sistem Altyapı Tanımları Yardım Dokümanı
sidebar_position: 1
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::



**Sistem Altyapı Tanımları Modülü(v.5.26) Kullanıcı Yardım Dokümanı**

**Modül Versiyonu:** 5.26

## **1.GİRİŞ**

**“QDMS SİSTEM ALTYAPI TANIMLARI”**, Personel bilgilerinin tanımlandığı ve diğer modüller için gerekli olan altyapının kurgulanmasının yapıldığı menüdür.

## **2.AMAÇ** 

Bu yardım kılavuzunun amacı; QDMS “Sistem Altyapı Tanımları” Modülünün çalışma sürecini anlatmaktır. Sistem Altyapı Tanımlarındaki tanımlamalar ile birlikte, parametrik ayarlamalar ve diğer teknik altyapı çalışmasının uygulanması amaçlanmaktadır.

## **3.SORUMLULUKLAR**

QDMS Sistem Yöneticileri

## **4.KISALTMALAR**

**QDMS**: Kalite Dokümanları Yönetim Sistemi “Quality Document Management System”

## **5.Sistem Altyapı Tanımları Modülü**
Qdms sisteminde diğer modüller için gerekli olan altyapının kurgulanmasının  yapıldığı modüldür. Diğer modüllerin çalışması için gereken tanımlar ile beraber parametreler, genel sistem parametreleri, ünvan, departman, pozisyon, personel, ürün/hizmet, müşteri/tedarikçi, işyeri, yönetim sistemleri ve madde no tanımlamaları, kullanıcı erişim yetkileri için gereken kullanıcı gurupları ve yetki grupları, uyarı ve aksiyon mailleri için gereken mesaj tanımlamaları, kullanıcı tarafından değiştirilebilen rapor formatları gibi çeşitli menüler kapsamında  yer almaktadır. Qdms yapısındaki tüm modüller bu  modülün üzerinde entegre bir şekilde çalışmaktadır.


**QDMS Giriş**

Qdms Ana giriş ekranında Qdms’in versiyon bilgisi yer alır, kullanıcı adı ve parola bilgisi ile sistemede giriş yapılır. Sisteme ilk girişte personeller kullanıcı adı ve şifre olarak kendilerine ait olan sicil numaralarını kullanırlar. Eğer personeller tarafından, bilgisayarlarına giriş yaptıkları kullanıcı adı ve şifre ile sisteme giriş yapılması isteniliyorsa, “Active Directory” özelliği aktif hale getirilir. Bu özelliğin aktifleştirilmesi için Bimser Teknik Ekibi ile iletişime geçilmesi gerekmektedir.Qdms ana giriş ekranında Diller arasına  ve Mobil uygulama geçiş işlemleride yapılır. Ekran görüntüsündeki Qdms’in versiyon bilgisi 5.26.0.0 olarak görülmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_7.png)

Mobil Uygulamaya geçiş işlemi için ana giriş ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_8.png)butonu tıklarak geçiş işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_9.png)

Açılan Mobil Uygulama İçin Barkod ekranında kullanıcı telefonunda  barkod okuyucu ile barkodu okutma işlemi yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_10.png)

Qdms Ana giriş ekranında mobil uygulamaya geçiş işlemi için ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_11.png) butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_12.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_13.png) 

Açılan Ayarlar ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_14.png) butonu tıklanılır. Qdms ana giriş ekranında Mobil Uygulama İçin Barkod ekranında barkod  Karekod tarama alanı ile taranır. Açılan Sunucu seçiniz alanında sunucu seçeneklerinde seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_15.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_16.png) 

Ayarlar ekranında sunucu seçim işleminden sonra mobil uygulamanın  link bilgisi görüntülenek Kaydet butonu tıklanarak  Mobil uygulama geçiş işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_17.png)  ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_18.png)

Qdms sistemi yapısında diller arası geçiş işlemi yapılmaktadır.Qdms sisteminde çoklu dil desteği özelliği bulunduğundan Qdms sistemin yapısının farklı dillerde çalıştırılması işlemi sağlanmıştır.Qdms sisteminde ingilizce dilinde sistemi çalıştırmak kurulu gelmektedir. Diğer dillerde Qdms sistemi çalıştırmak için çoklu dil desteği özelliğinin kurulması için Bimser Teknik Destek Ekibinden yardım almak gerekmektedir .Diller arası geçiş işlemi için ana giriş ekranında  ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_19.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_20.png)

Açılan Giriş Ayarları ekranında Dil alanında açılır Dil listesinde İngilizce dil seçeneği seçilir. Qdms sistemin ingilizce olarak çalıştırılma işlemi yapılır.  Ana giriş ekranı dil seçeneği ingilizce olarak çalıştırıldığında alanların ingilizce dil karşılıkları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_21.png)

Qdms Bekleyen İşler sayfasında ilgili alanlar ekran görüntüsünde olduğu gibi ingilizce olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_22.png)

Qdms kapsamında tüm modüllerin dil seçeneği ingilizce olarak çalıştırılır. Doküman işlemleri modülünde olduğu gibi diğer modüllerde de sistem ingilizce çalıştırıldığında tüm menülerin ingilizce dil karşılıkları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_23.png)

**QDMS şifre Hatırlatma;**

“Şifremi unuttum” seçeneği ile kullanıcı sicil numarası, e-mail adresi  ve sms ile şifresini alabilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_24.png)

Sistem Altyapı Tanımları parametrelerinde 93 numaralı “Şifre hatırlatma yöntemi(Mail(M),Sicil(S),Sms(T))” parametre değerine göre girilen değere göre şifre hatırlatma yöntemi belirlenir. Unutulan şifrelerin hatırlatma yönteminin belirlendiği parametredir.Login ekranında "şifremi unuttum" butonuna tıklanınca açılan QDMS şifre Hatırlatma ekranında  parametre değerine göre;Sadece e mail ile sorgulama yapılmak isteniyorsa parametre değeri :M ,Sadece Sicil numarasına göre sorgulamalarda parametre değeri :S ,Sms numarasına göre sorgulamalarda parametre değeri :T Her üç sorgulama için parametre değeri M,S,T değerleri yazılmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_25.png)

Ana giriş ekranında “Şifremi Unuttum” alanı  tıklanılır. Açılan Qdms Şifre Hatırlatma ekranında parametreye bağlı gelen seçeneklerde seçim yapılır. Seçim alanın Sicil No seçilirse personelin Sicil no alanına sicil no bilgisi yazılarak şifre gönderme şekli alanın ilgili seçenek E-mail seçilerek ![ref1] butonu tıklanarak Personel tanımlama ekranında tanımlı mail adresine şifre bilgisi gönderilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_27.png)

Aynı şekilde Şifre Gönderme şekli SMS seçilirek ![ref1] butonu tıklanarak Personel Tanımlama ekranında tanımlı Cep numarasına  şifre bilgisi gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_28.png)Qdms Şifre Hatırlatma ekranında  Seçim işleminde E-mail seçildiğinde E-mail alanı görüntülenir ve personelin mail adresi yazılarak ![ref1] butonu tıklanarak şifre bilgisi mail adresine gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_29.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_30.png)

Qdms Şifre Hatırlatma ekranında  seçim işleminde Sms seçildiğinde Sms alanı görüntülenir ve personelin cep numarası bilgisi yazılarak ![ref1] butonu tıklanarak şifre bilgisi mail adresine gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_31.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_32.png)

Qdms Ana giriş ekranında Güvenlik kodu doğrulaması işlemi yapılması için Sistem Altyapı Tanımları parametrelerinde 248 numaralı “Şifre Hatırlatma sayfasında güvenlik kodu doğrulaması kullanılsın mı?”parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_33.png)

248 numaralı parametre aktif edildikten sonra Qdms Şifre Hatırlatma pop-upn’da seçim alanın seçenekleri için ayrıca Güvenlik kodu alanı görüntülenir. Şifre hatırlatma sayfasında güvenlik kodu doğrulaması yapılması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_34.png)

**Bekleyen İşlerim;**

Personel sisteme giriş yaptığı zaman QDMS ana ekranı karşısına çıkmaktadır. Bu ekran  üzerinde bekleyen tüm görevler görülmektedir. Qdms sisteminde bekleyen işler menüsü mobil uygulamasında olduğu gibi modül modül olarak gruplandırılarak sistemde gelmektedir. Bekleyen işlerimde Toplam alanında sistem giren kullanıcının üzerinde bulunan toplam görevlerin yani iş  bilgisi gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_35.png)

Modüllerin temsil eden ikonları ve adları birlikte bekleyen işlerde modüller listelenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_36.png)

Modül Modül gruplanarak gelen bekleyen işlerde herhangi bir modülde kullanıcının üzerinde görevleri görmek için ilgili modül tıklanılır.  İlgili Modül simgesi yanındaki açılır liste tıklanarak kullanıcının üzerinde bulanan o modüller ilgili görevleri listelenir.  Örneğin Düzeltici Ve Önleyici Faalieyetler modülünde modül simgesi yanındaki açılır liste tıklanıldığında Düzeltici Ve Önleyici Faaliyetler modülü ile ilgili kullanıcının üzerindeki iş olarak görevler  listelenir ve görevin toplam sayısı bilgisi karşısında verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_37.png)

Listelenen bu görevlerinde toplam sayısında modülün açılan görevi karşındaki yer almaktadır. Düzeltici ve Önleyici Faaliyetler Modülünde kullanıcının “Sonuç Raporu Yazılacak DÖF’ler Listesi ” görevi tıklanılır. İlgili görevde ilk 4 kolunda görev ilgili alanlar ve bu alanlar ilgili bilgiler görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_38.png)

İlgili görev listesi çok olduğunda görev arama çubuğunda istenilen görevin kodu yazılarak sadece o görev ilgili bilgillerin görüntülenmesi sağlanır. Görevi ilgili arama çubuğuna görev ilgili kod, metin gibi bilgiler yazılarak ilgili görevin sadece listelenmesi sağlanır. Düzeltici ve Önleyici Faaliyetler modülünde “Sonuç Raporu Yazılacak DÖF’ler Listesi”  görevindeki listesindeki herhangi bir görevin kodu arama çubuğuna yazılarak görevi sadece listede yer alması sağlanır.İstenirse görev ilgili kolonlardaki alanlarında metin bilgileri yazılarak da arama yapılır. Görev arama çubuğunda yazılana metin veya kod bilgisi  silinmesi işlemi için sağ taraftaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_39.png)(Sil) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_40.png)

Bekleyen işlerde listenen  görevlerdeki sağ üstteki ![ref2] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_42.png)

Bu buton tıklanarak modüldeki kullanıcının üzerindeki görevlerin detay bilgileri tam ekran olarak görüntülenerek ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_43.png)

Aynı şekilde![ref2] butonu tıklanarak açılan ekranda ilgili görevler ilgili kolon sayısı artarak bu kolonlardaki alanlar ilgili görevler ilgili detay bilgilere ulaşılır. Açılan bu ekranda arama çubuğu bulunur. İlgili görevde görev sayısı çok fazla olduğunda veya tek bir görevin listelenmesi istediğinde ilgili görev ilgili kod yada metin arama çubuğuna yazılarak istenilen görev bilgilerin sadece detay bilgilerde gelmesi ve görüntülenmesi sağlanır. Bu detay bilgiler görevinin görüntülendiği tam ekranda çıkmak için ekranın sağ üstte yer alan ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_44.png) butonu tıklanılır.

Bekleyen işlerde görevlerin gecikmede olup, olmadığı renklerle ifade edilerek  görüntülenir.

Örnek; Kullanıcın Bekleyen işlerinde Düzeltici ve Önleyici Faaliyetler  modülünde “Sonuç Raporu Yazılacak DÖFler Listesi” iş olarak düşen görevler belirtilen sürede yapılmadığı gecikmeye düştüğü kırmızı renk olarak gösterilerek belirtilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_45.png)

Örnek; Kullanıcın Bekleyen işlerinde  Düzeltici ve Önleyici Faaliyetler modülünde “Onay Bekleyen DÖFler Listesi” iş olarak düşen görevin gecikmede olmadığı sarı renk olarak gösterilerek görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_46.png)

Bu şekilde Bekleyen işlerde gecikmedeki işler Kırmızı ve gecikmede olmayıp süreci devam eden işlerde sarı renkte  ifade edilerek  bir işin gecikmede olup olmadığı bekleyen işlerde renkler ile görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_47.png) Qdms sisteminde  Ensemble programına Ensemble programına geçiş butonu tıklanarak geçiş işlemi , Bekleyen İşlerim , Sık kullanılanlar, Dashboard , modüllerin Entegre Yönetim Sistemi ve Sistem Altyapı Tanımları kısımları ilgili menüler açılmasını sağlayan menü butonudur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_48.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_49.png)butonu tıklanarak Ensemble programına geçiş işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_50.png)

Bekleyen İşlerim  tıklanarak bekleyen işlerim sayfasına geçiş bu kısımda yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_51.png): İlgili kısımlar , Modüllerin Entegre Yönetim Sistemi, Sistem Altyapı Tanımları kısmında menülerine hızlıca erişim sağlayan ara çubuğudur. Örneğin:Denetim Faaliyetler modülü ilgili menülerine hızlı erişim sağlamak için ara çubuğuna Denetim Faaliyetleri Modülün ismi yazılır. Modül ismi yazıldıktan Modülün Sistem Altyapı Tanımları ve Entegre Yönetim Sistemi kısımları ekrana gelir. Denetim Faaliyetleri Entegre Yönetim kısmı tıklanılır ve açılan menü listesinde ara çubuğuna ilgili menü ismi yazılarak menünün adının görüntülenmesi sağlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_52.png)

Listede görüntülenen menü ismi tıklanarak açılmak istenilen menü ekranına hızlı bir şekilde erişim sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_53.png)

**Sık Kullanılanlar :** Kullanıcının sık kullandığı menülerin listeye adının getirildiği kısımdır. Qdms sistemde bu kısımda herhangi bir ayar yapmaya gerek yoktur. Qdms sistemi kullanıcının sık olarak kullandığı 5 menüyü otomatik olarak bu kısma getirmektedir. Her kullanıcının Qdms sisteminde sık kullandığı menülerin  listesi farklı olduğu için sık kullanılanlar kısmıdaki menüleride farklılık gösterir. Kullanıcının Sık kullanılanlar kısmında Qdms sisteminde sık kullandığı menüyü hızlı bir şekilde erişim sağlayarak açılmasını ve işlem yapması olanak sağlar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_54.png)

Sık kullanılanlar listesinde Parametreler menüsü tıklanarak hızlı bir şekilde erişim olanağı sağlanılır.Açılan menüde gerekli işlem adımları yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_55.png)

**Dashboard:** Qdms sisteminde  kullanıcılara işlemleri, metrikleri, grafikleri ve raporları tek bir ekranda görüntülemelerine olanak sağlayan kısımdır. Dashboard, bilgi akışını ve/veya içeriğini özetlemek amacıyla kullanılan, grafikler ve tablolar yoluyla belirli bir durumu açıklamaya yarayan göstergeler ekranını, iş panosu ve  görtergeler tablosu ifade etmektedir. Amacı en kısa sürede, en az etkileşim ve düşünme gereksinimi ile gerekli olan bilginin sunulmasıdır. Genelde yönetici konumundaki kişileri sıklıkla kullandıkları ekrandır.Qdms Sistemi kapsamında ana modüller ve risk modüllerin bir kısmında bu özellik getirilmiştir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_56.png)

Dashboard  kısmında “Aksiyon  Yönetim” modülü tıklanarak bu özelliğin içeriği görüntülenir. Aksiyon Yönetim modülünde Dashboard menüsü tıklanıldığında liste ve filtre sekmesi olmak üzere iki sekme karşımıza çıkmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_57.png)

Filtre sekmesinde arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_58.png)

Aksiyon Yönetimi modülünde Aksiyon Dashboard ekranında Liste sekmesinde Toplam Aksiyon, Açık Aksiyon(Gecikmemiş), Açık Aksiyon(Gecikmiş) , Zamanında Kapanan ve Gecikmeli Kapanan alanları sabit alanlar olarak  ekrana gelerek üzerinde herhangi bir düzenleme işlemi yapılmamaktadır.Bu alanlarda Toplam Aksiyon sayısı bilgisi, açılan aksiyonların gecikmemiş olanların sayısı, açılan aksiyonların gecikmiş olanların sayısı ,  Zamanında Kapanan  Aksiyon bilgisi  ve yüzdelik dilimleri verilir. Aksiyon Dashboard ekranında ilk açılışta 6 tane varsayılan grafik görüntülenir.Modül Yöneticileri isterlersen grafik sayısı artırabilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_59.png)

Aksiyon Dashboard ekranında kaç tane grafik olacağı, grafiğin adının ne olacağı, grafiklerin sırasını ne olacağı Z ekseninde, Y ekseninde hangi alanlar olacağı, Grafik Boyu, Grafik Eninin ne olacağı ve grafik tipinin ne olacağı gibi ayarlarmalarla grafik tasarlama işlemini yapılır. Bu ayarlamalarının Aksiyon Dashboard ekranında yapılması gibi diğer modülerde bu işlemler içinde Kullanıcının ilgili Modülde Modül Yönetici olarak tanımlı olması gerekir. (SAT/BSAT/Konfigürasyon Ayarları/Yönetici Tanımlama  menüsünde  ilgili  Modülde modül yönetici tanımlama işlemi yapılır.) İlgili Modülde modül yönetici olarak tanımlama işleminde Aksiyon Yönetimi Modülünde olduğu gibi ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_60.png)(Grafik Ayarları) butonu görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_61.png)

Bu buton tıklanarak ilgili modülde  grafik tasarlama işlemide yapar. Modül Yöneticileri olmayan kullanıcılar ise Dashboard Konfigürasyonu ekranını Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Dashboard Konfigürasyonu/İlgili modüllün menüsü tıklanarak gerekli ayarlamalar yapılarak grafik tasarlama işlemide yapabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_62.png)

Bu menüde örneğin “Eğitim Planlama” modülü tıklanarak açılan ekranda butonlar yardımıyla grafik tasarlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_63.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref3]: Yeni bir Dashboard tanımlanır.

![ref4]: Listede seçili olan Dashboard bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. 

![ref5]: Listede seçili olan Dashboard bilgisi silinir.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Eğitim Planlama  Modülünde yeni bir Dashboard  ekleme işlemi için  ![ref3]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_70.png)

Dashboard Konfigürasyonu - Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler doldurulduktan sonra ekranın sol üstte yer alan ![ref9] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_72.png)

Sistem tarafından “Kaydetmek istediğinize emin misiniz?” uyarı mejasında “Tamam” butonu tıklanarak grafik ayarlarının başarı olarak kaydedilmesi işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_73.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_74.png)

Eğitim Planlama  Dashboard ekranında tanımlanan Dashboard görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_75.png)

**Hızlı Doküman Arama;** Qdms sistemdeki Doküman Yönetimi modülü yapısında sistemde yüklü olan bir  dokümana Hızlı Doküman arama alanı ile dokümanın kodu, adı ya da hatırlatıcı bir kelime girilerek hızlıca ulaşılabilmesi sağlanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_76.png)

Hızlı Doküman arama işlemi için Hızlı Doküman Arama alanına doküman kodu bilgisi yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_77.png)

Hızlı Doküman arama alanındaki ![ref10] butonu tıklanılır veya klavyeden “Enter” tuşuna basılır. Açılan Hızlı Arama ekranında “İçinde Ara” seçeneği ile  ilgili check box işaretlenirsede  hızlı arama alanına yazılan bir  kelime ise bu kelimenin geçtiği dokümanlarından listelenmesi sağlanır. Hızlı Arama ekranında Doküman Listesi sekmesinde listede yer alan Doküman Kodu alanındaki Doküman kodu link tıklanarak dokümanın görüntülenme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_79.png)

Açılan Doküman Görme ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_80.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_81.png)

Dokümanın bilgisayara indirilerek  görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_82.png)

Hızlı Arama ekranında Süreçler ile ilgili arama işlemi yapmak için Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Parametreler ekranında Modüller alanında “Sistem Altyapı Tanımları” modülü seçilerek Sistem Altyapı Tanımları modülü parametreleri listelenir. Listelenen bu parametrelerden 216 numaralı “Hızlı aramada Süreçler listelensin mi?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_83.png) Parametre aktif edildikten sonra Hızlı Arama ekranında Süreç Listesi sekmesinde Süreç Listesi görüntülenir. Süreç listesi sekmesinde Süreç listesinin görüntülenmesi Sistem Altyapı Tanımları modülü parametreleriden  süreçler ilgili yetkilendirme parametresi olan 211 numaralı “Süreç seçme sayfasında yetki kontrolü yapılsın mı?” parametresinin parametre değeri “Evet” seçilerek parametrenin aktif edilmesi gerekir

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_84.png)

Parametre aktif edildikten sonra Süreç listesi sekmesinde Süreç Listesi görüntülenmez. Yetki parametresi aktif olduğu için süreçler  görüntülenmesi ve üzerinde işlem yapılması yetki dahilinde olur. Parametre pasif olduğunda  Hızlı Arama ekranında Süreç Listesi sekmesinde Süreç listesi görüntülenir. Süreçlerin görüntülenme ve üzerinde değişiklik yapma yetkisi kullanıcılara verilir.

Qdms sistemi doküman hızlı arama çubuğunda ilgili süreçin kodu yada adı  yazılarak ![ref10] butonu tıklanılır veya klavyeden “Enter” tuşuna basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_85.png)

Hızlı Arama  ekranında Süreç Listesinde arama yapılan süreçin Süreç listesi sekmesinde listede yer aldığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_86.png)

Süreç Listesinde Süreç Kodu alanındaki süreçin  kodu linki tıklanarak süreçin detayı ekranının  görüntülenme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_87.png)

Süreç Detayı ekranında süreçin görsel modeline geçiş yapmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_88.png)buton tıklanarak süreçin görsel model ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_89.png)

**Favoriler:** Kullanıcıların Qdms sistemi üzerinde sık ziyaret ettikleri menülerin ekranlarını Favori olarak kaydedebilmelerinin sağlandığı kısımdır. Kullanıcılar, bu menü ekranlarına kolayca erişmek için erişmek istedikleri menü ekranı açıkken  Fovorilerim ekranında “Yeni Ekle” butonu yardımıyla favorilerine eklerler. Favorilerim  menüsü kullanıcılara Qdms sisteminde belirli menülerin ekranlarına   hızlı erişim sağlar. Favorilerim sayfasında sık kullanılan menüler ekleme ve eklenen menüleri açıklama kısmının düzenleme işlemleri yapılır. Sık Kullanılanlar ve Favorilerim menüleri farkı ise Sık Kullanılanlar kısmında  Qdms sisteminde kullanıcının  çok sık kullandığı ilk 5 menü sistem tarafından otomatik olarak bu bölümde yer alır. Favorilerim menüsünde ise kullanıcı isteği doğrultusunda bir menüye favori  olarak ekleme, listedeki Fovori olarak tanımlandığı menüyü  düzenleme, silme işlemleri yapmasına olanak sağlanmaktadır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_90.png)

Qdms ana ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_91.png) (Favorilerim) butonu tıklanılır.Açılan Fovorilerim ekranın iki buton karşımıza çıkar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_92.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref11]:Qdms sisteminde sık kullanılan menü açıkken Favorilerim menüsüne Favori olarak ekleme işlemi yapılır.

![ref12]:Favorilerim listesinde seçili olan Favorinin açıklama kısmı üzerinde düzenleme ve silme işlemleri yapılır.

Örnek: Doküman Yönetimi Modülü raporlarında “Doküman Onay Süreleri Raporu” favori olarak ekleme işlemi için;

1. Aşamada  Entegre Yönetim Sistemi/Doküman İşlemleri/Raporlar/ Doküman Onay Süreleri Raporu menüsü tıklanarak açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_95.png)

2\. Aşamada  ilgili menü açıkken Favorilerim menüsünde ![ref11] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_96.png)

Açılan Favori Ekle ekranında açıklama alanına Favori olarak eklenecek menünün adı bilgisi yazılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_97.png)

Gerekli alanlar ilgili bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_98.png) butonu tıklanarak Favori Kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_99.png)

Favorilerim ekranında Favorilerim listesinde kullanıcının sık olarak kullandığı menünün Favori ekleme işleminde sonra listede yer aldığı görülür. Kullanıcı bu listeden " Doküman Onay Süreleri Raporu " favorisini tıklayarak tek aşamada menü ekranına hızlıca erişim olanağı sağlar. Birkaç aşama işleminde menü açılma işleminden yerinde tek aşamada hızlı bir şekilde menü ekranın açılması işlemi gerçekleştirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_100.png)

Favorilerim menüsü ile Favori olarak kaydedilen menünün açıklama kısmının düzenlenmesi için ![ref12] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_101.png)

Favorilerim ekranında ![ref12]butonu tıklanarak Favori olarak tanımlanan menünün açıklama alanı üzerinde değişiklik ve düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_102.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_103.png)

Açıklama alanında yapılan değişiklikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_104.png) butonu tıklanarak favori güncelleme kayıt işlemi yapılır. Yapılan işlemden vazgeçmek içinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_105.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_106.png)

Favorilerim menüsü ile Favori olarak kaydedilen menünün açıklama kısmının silinmesi işlemi  için ![ref12] butonu tıklanılır. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_107.png)

Açılan Favorilerim ekranında eklenen Favoriyi ilgili açıklama alanı  listeden silmek için  ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_108.png) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_109.png)

Sistem tarafından “Seçili kaydı silmek istediğinizden emin misiniz?” mesajı verilirek “Tamam” butonu tıklanarak Favorilerim listesinde eklenen favorinin silinme işlemi yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_110.png)

Favorilerim listesinde silinme işlemi yapılan favori listede görüntülenmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_111.png)

**Duyurular:**

Qdms ana ekran üzerinde ![ref13] butonu tıklanılır. Qdms sisteminde “Duyuru oluştur” menüsünde tanımlı duyuruları görüntülenme işlemini yapıldığı butondur.Bu buton tıklanarak “Duyuru Oluştur” menüsünde tanımlı duyuruların sistemde görüntülenmesi sağlanır. Buton üzerindeki sayısal değer tanımlanan duyuru sayısı verir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_113.png)

Tanımlanan duyuru görüntelemek için ![ref13] buton tıklanılır.Duyurular ekranında sistemde tanımlı duyuruların listesi görüntülenir. Duyurular listesinde birden fazla duyuru olduğunda Arama çubuğunda arama işlemide yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_114.png)

Duyuru tanımlama işlemi Sistem Altyapı Tanımları/ BSAT/ Tanımlar/Duyuru Oluştur menüsünde tanımlanır.Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları /Duyuru Yetki Matrisi menüsünde ise tanımlanan Duyurular ile yetkilendirme işlemi yapılır.Kullanıcılar artık yetkili olduğu alanlarda duyuru yapabilecek ve kendi duyurularını yönetebileceklerdir. Duyuru oluşturulduğunda ilgili kişilere otomatik e-posta gönderilecek ve kullanıcılar sistemi açtıktan sonra  yeni duyuruları görebileceklerdir. Duyurular listesinde tanımlı duyuru tıklanarak Duyurunun detaylı bir şekilde görüntülenmeside sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_115.png)

**İletiler:** Qdms ana ekranı üzerinde ![ref14] butonu tıklanılır. Bu butonun Qdms ana ekranı üzerinde görüntülenmesi Sistem Altyapı Tanımları modülü parametrelerinde 139 numaralı “İleti Kullanılacak mı?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_117.png)

Parametre aktif edildikten Qdms ana ekranı üzerinde ![ref14] butonu görüntülenir. Bu buton tıklanarak İletiler ekranı görüntülenir. Açılan İletiler ekranında Gelen iletiler ve Gönderilen İletiler sekmesi olmak üzere 2 sekme görüntülenir. Gelen İletiler sekmesinde Gelen iletilerin ve Gönderilen İletiler sekmesinde Gönderilen iletilerin listelenmesi sağlanır. Bu menüde yeni ileti tanımlama iletiler üzerinde cevaplama, görüntüleme, silme ve iletiyi okundu yapma işlemleri butonlar yardımıyla yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_118.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref15]:Yeni bir ileti tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_120.png):Listede seçili iletiler silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_121.png):Listede seçili gelen ileti cevaplanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_122.png):Listede seçili iletili görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_123.png):Listede seçili gelen ileti okundu yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_124.png): Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

İletiler ekranına yeni bir ileti eklemek için ekranın sağ üst köşesindeki ![ref15] butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_125.png)**Açılan ekranda ilgili alanlar tanımlanır:**

**Modül Adı:** İleti Ekle ekranında gönderilecek iletinin  açılır liste tıklanarak açılan Modül listesinden seçildiği alandır. 	

**İletiyi Alacak Personeller:** İleti Ekle ekranında gönderilecek iletinin ![ref16] (Ekle) butonu tıklanarak sistemde tanımlı personel listesinde veya  ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_127.png)(Seç) butonu tılanarak açılan sistemde tanımlı Kullanıcı Grubu listesinden seçildiği alandır. 	

**Konu:** İleti Ekle ekranında gönderilecek iletinin konu bilgisinin yazıldığı alandır.

**Açıklama:** İleti Ekle ekranında gönderilecek iletinin varsa detay açıklama bilgisinin yazıldığı alandır.

**İleti Gizli Olsun Mu?:** İleti Ekle ekranında  gönderilecek iletinin gizli olması isteniyorsa ilgili check box işaretlenir.

İleti ekle ekranında İleti gönderilecek  personellerin  ![ref16] (Ekle) butonu tıklanarak açılan sistemde tanımlı Personel listesinde seçilir. Konu alanında gönderilecek iletinin hangi konuyla ilgili ise bilgisi yazılır. Açıklama alanında gönderilecek iletinin detaylandırılarak bilgisi yazılır. Varsa ileti ile ilgili dosya, doküman Ek dosya alanında yüklenir. Son olarak iletinin gizli olması isteniyorda “ileti gizli olsun mu?” alanı ilgili check box işaretlenir. Gerekli alanlar ilgili bilgiler doldurularak ![ref17] butonu tıklanarak İleti ekleme kayıt işlemi gerçekleştirilir.

İleti ekleme işleminde gönderilme işlemi yapılan iletinin gönderildiği personellerin  Qdms Ana giriş ekranından kullanıcı adı ve parolası ile giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_129.png)

İleti Gönderilen personelinin Qdms ana giriş ekranında giriş yapıldıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_130.png) butonu tıklanılır. Buton üzerindeki sayısal değer kullanıcıya gelen ileti sayısı gösterir.İletiler ekranından Gelen iletiler sekmesinde kullanıcıya gelen iletilerin listesi görüntülenir. Kullanıcı bu aşamada kendisine gelen iletiyi görüntüleme ,cevaplama ve okundu yapma işlemi yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_131.png)

Kullanıcı İletiler ekranında Gelen İletiler sekmesinde listede kendisine gelen  iletiyi seçme işlemi yaparak  ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_132.png) butonu tıklayarak kendisine gelen iletinin içeriği görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_133.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_134.png)

Kullanıcı İletiler ekranında Gelen İletiler sekmesinde listede kendisine gelen iletiyi seçme işlemi yaparak içeriğini okuduysa   ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_135.png) butonu tıklayarak  iletiyi okundu yapma işlemi yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_136.png)

Kullanıcı İletiler ekranında Gelen İletiler sekmesinde listede kendisine gelen iletiyi seçme işlemi yaparak  ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_137.png) butonu tıklayarak  iletiyi cevaplama işlemi yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_138.png)

Açılan İleti Görüntüleme ekranında kullanıcı kendisine gelen iletinin içeriğini inceyerek Açıklama alanında ileti ile ilgili açıklama bilgisi yazarak ekranın sol üst köşesideki ![ref17] butonu tıklayarak ileti cevaplama kayıt işleme gerçekleştirir.

**Yardım:** Qdms ana ekranı üzerinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_139.png) butonu tıklanılır. Açılan Yardım menüsünde Qdms ürünü hakkında bilginin verildiği, kullanıcıların kullanıcı yardım dokümanları görüntülenip, bu dokümanları bilgisayarına indirebildiği ve QDMS Destek seçeneği tıklanarak kullanıcıların en hızlı ve kolay destek alabilecekleri platform olan BSS ulaşabildiği menüdür.

Yardım Menüsü ekranında “Hakkında” ilgili seçenek tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_140.png)

Açılan ekranda Qdms sistemi  adı , versiyon bilgisi ve   Qdms ürünün Bimser Çözüm Yazılım ve Danışmanlık A.Ş.kurumu  ait bilgisinin ulaşıldığı yardım menüsü seçeneğidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_141.png)

Kullanıcılar ilgili modül kullanıcı yardım dokümanın Yardım menüsünden seçerek bilgisayarına indirip, o dokümanı kullanabilir. Yardım Menüsünde arama çubuğunda indirilecek yardım menüsünde yüklü olan Modül Kullanıcı Yardım Dokümanı  adı yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_142.png)

Arama çubuğuna yazılan yardım menüsündeki kullanıcı yardım dokümanı adının bulunduğu linki tıklanarak, kullanıcı yardım dokümanı bilgisayara indirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_143.png)



Kullanıcı Yardım dokümanları modüllerin ve sistemlerin nasıl kullanıldığı bilgisini anlatır. Bu dokümanlarda modülün Sistem Altyapı tanımları  kısmındaki  menülerde altyapı kurgusunun anlatılır. Entege Yönetim Sistemi kapsamındaki  menülerin , raporların ve grafikleri  kullanımı anlatılır. Bu kısımlar dokümanlarda Qdms sisteminin ekran görüntüleri desteklenmiş şekilde içeriğinde sunulur. Kullanıcılar, bu dokümanlar ile modülün işlevlerini ve özelliklerini nasıl kullanacaklarını daha iyi anlayabilirler ve Qdms sistemde uygulayabilir. Modül kapsamında parametreler ayarları ile kullanıcıların belirli parametreleri nasıl ayarlayabilecekleri ve kişiselleştirebilecekleri gibi bilgileri içerir. Kullanıcıların belirli bir modül veya işlev hakkında daha fazla bilgiye ihtiyaç duyduklarında bu dokümanları başvurarak sorunlarını çözebilirler. Bu, kullanıcı deneyimini iyileştirmeye yardımcı olur ve kullanıcıların Qdms sistemini daha etkili bir şekilde kullanmalarına olanak tanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_144.png)

Kullanıcılar Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Yardım Menüsü Tanımlama menüsü ile istedikleri Kullanıcı Yardım dokümanı yardım menüsüne Ek Dosya  olarak yükleme ve ilgili adreslerin link şeklinde ekleme işlemi yapabilirler. Eklenen Ek Dosya ve  ilgili adreslerin link bilgisi  üzerinde değişiklik yapma ve silme işlemleri yaparlar.

**QDMS Destek:** Bimser Yazılım ve Danışmanlık A.Ş tarafından üretilen yazılımların kullanıcı desteğinin sağlandığı platforma adıdır.QDMS Destek adı olarak  bilenen BSS-Bimser Support System ile  yazılım ürünlerini kullanan kullanıcılardan gelen şikayet ve taleplere bu platform aracılığı ile destek verilir.

Yardım menüsünde arama çubuğuna QDMS Destek seçeneği yazılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_145.png)

Görüntülenen QDMS Destek adının bulunduğu link tıklanarak BSS-Bimser Support System platforma ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_146.png)

Yazılım ürünlerini kullanan kullanıcılardan gelen şikayet ve taleplere bu platform aracılığı ile destek verilir. Kullanıcıların en hızlı ve kolay destek alabilecekleri platform BSS’dir. BSS sistemine, <http://bss.bimser.com.tr/\> adresi üzerinden kullanıcı adı olarak mail adresi, şifre olarakta hesap şifresi girilerek login olunur. Kullanıcı şifresi, ilk olarak BSS hesabını oluşturan uzman tarafından verilir. Kullanıcı daha sonra şifresini yenileyebilir. Unutulan şifreler için şifremi unuttum özelliği kullanılarak şifre mail adresine gönderilebilir. Aşağıdaki konularda BSS platformdan destek verilir.

- **Talep şikayet kaydı oluşturabilirler:** Login olduktan sonra, Destek / Yeni Bildirim sayfasından Talep- Şikayet bildirimleri yapılır.
- **Bilgi Alma Kayıtları:** Bilgi alma amaçlı oluşturulan kayıtlara destek uzmanı personeller tarafından kısa süre içerisinde yanıt verilir ve kullanıcılar bilgilendirilir. 
- **Şikayet Kayıtları Değerlendirme Süreci:** Uygulamalar ile ilgili şikayetler ilk olarak destek departmanında tarafından değerlendirilir
- **Geliştirme Kayıtları Değerlendirme Süreci:** Uygulamada var olmayan yeni özelliklerin eklenmesi yada var olan özelliklerin değiştirilmesi talep edildiğinde bu kayıtlar geliştirme kaydı olarak değerlendirilmesi yapılır.

Qdms ana ekranında Kullanıcı Adı ve Soyadı bilgisi bulunmaktadır. Kullanıcı Adı ve Soyadı Bilgisi kısmında açılır liste tıklanıldığında Vekalet verme işlemin yapıldığı Vekalet verme menüsü, Vekalet girişi işlemin yapıldığı vekalet girişi menüsü , Başkasının adına vekalet verme ,Başkasının adına Giriş (Süper Şifre)  ve Qdms sistemin tasarım gibi özelliklerin değiştirildiği Hesap Ayarları menülerine ulaşılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_147.png)

Başkasının adına vekalet verme ve Başkanın adına Giriş (Süper Şifre) menülerin açılır listede gözükmesi için kullanıcının Sistem Altyapı Tanımları modülünde modül yönetici olarak tanımlı olması gerekmektedir. Sistem Altyapı Tanımları modülünde modül yönetici olmayan kullanıcıların ekranında bu iki menü görüntülenmez.

**Başkasının Adına Vekalet Verme:** Sistem Altyapı Tanımları modülünde modül yönetici olan kullanıcıların ekranında görüntülenen bir menüdür. Bu menü ile başka kullanıcıların adına vekalet verme işlemi yapılır. Genelde yönetici konumundaki kullanıcıların kullandıkları menüdür. Kullanıcılar izindeyken, firma dışındayken, vb. durumlarda bekleyen görevlerinin gecikmeye girmemesi amacıyla kullanılan menüdür. Vekalet verme işleminde Yetkili Modüller alanında açılır Modül listesinde yetki verilecek Modüllerin seçim işlemi yapılarak hangi modüllerde yetkilendirme işlemi verileceği belirlenir. Yetkili Modüler alanında modül seçimi yapılmadığı takdirde tüm modüllerde yetki verme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_148.png)**Açılan ekranda ilgili alanlar tanımlanır:**

**Vekaleti veren:** Vekalet Yönetimi ekranında vekalet veren  kişi bilgisinin ![ref18] (Seç) butonu tıklanarak açılan sistemde tanımlı Personel listesinde seçildiği zorunlu alandır.

**Vekaleti alan:** Vekalet Yönetimi ekranında vekalet alan  kişi bilgisinin ![ref18] (Seç) butonu tıklanarak açılan sistemde tanımlı Personel listesinde seçildiği zorunlu alandır. 

**Başlama tarihi:** Vekalet Yönetimi ekranında  vekaletin başlama tarihi bilgisinin açılan takvim alanında seçildiği zorunlu alandır.	

**Bitiş tarihi:** Vekalet Yönetimi ekranında  vekaletin bitiş  tarihi bilgisinin açılan takvim alanında seçildiği zorunlu alandır.		 		

**Yetkili Modüller:** Vekalet Yönetimi ekranında vekaletin hangi modüllerde verileceği bilgisinin açılan açılır modül listesinde seçim yapıldığı alandır. Bu alanda modül seçimi yapılmadığı takdirde tüm modüller ilgili vekalet verme işlemi gerçekleşir.

Vekalet Yönetimi ekranında vekaleti veren ve vekaleti alan bilgisi personel listesiden seçilir. Vekaletin başlama ve bitiş tarihi bilgisi açılan takvim alanında seçilir. Vekalet verilecek modüller açılan modül listesinde seçim işlemi yapılır. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref19]  butonu tıklanarak Başkasına adına vekelet verme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_151.png) 

Başkasının adına vekalet verme işleminin uygulama için vekalet alan kullanıcının Qdms’sine kullanıcı adı parola bilgisi giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_152.png)

Kullanıcının local adresine giriş yapıldığında sistem hangi personelle sisteme giriş yapacağı bilgisi sorar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_153.png)Vekaleti verilen kullanıcı olan personel seçilerek kullanının adresine giriş yapılır. Kullanıcı adresine giriş yapıldığında vekalet verme işleminde vekalet işlemi için yetki verilen modüller sadece görüntülenir.  Başkanının adına vekalet verme işleminde Doküman Yönetimi ve Sistem Altyapı Tanımları Modüllerin yetkisi verildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_154.png)

**Vekalet Verme:** Bu menü ile kullanıcıların izindeyken, firma dışındayken, vb. durumlarda bekleyen görevlerinin gecikmeye girmemesi için bir başka kullanıcıya vekalet vermeleri işlemi yaparlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_155.png)

Kullanıcının Adı ve Soyadı bilgisi bulunduğu kısımda açılır liste tıklanarak açılan menü listesinde Vekalet Verme menüsü tıklanarak Vekalet Görüntüleyici ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_156.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref20]: Yeni bir Vekalet verme işlemi gerçekleştirilir.

![ref21] : Listede seçili olan Vekalet bilgisi iptal edilir.

![ref22]: Kayıtlar filtrelenerek arama yapılabilir.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Yeni bir  vekalet verme işlemi gerçekleştirmek için ekranın sağ üst köşesindeki ![ref20] butonuna tıklanarak Vekalet Görüntüleyici ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_161.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Vekaleti veren:** Vekalet Yönetimi ekranında vekalet veren  kişi bilgisinin sistemin otomatik olarak verdiği alandır. Bu alanda sisteme giriş yapan  kullanıcının adı ve soyadı bilgisi verilir.

**Vekaleti alan:** Vekalet Yönetimi ekranında vekalet alan  kişi bilgisinin ![ref18] (Seç) butonu tıklanarak açılan sistemde tanımlı Personel listesinde seçildiği zorunlu alandır.  	 

**Başlama tarihi:** Vekalet Yönetimi ekranında  vekaletin başlama tarihi bilgisinin açılan takvim alanında seçildiği zorunlu alandır.	

**Bitiş tarihi:** Vekalet Yönetimi ekranında  vekaletin bitiş  tarihi bilgisinin açılan takvim alanında seçildiği zorunlu alandır.		 		

**Yetkili Modüller:** Vekalet Yönetimi ekranında vekaletin hangi modüllerde verileceği bilgisinin açılan açılır modül listesinde seçim yapıldığı alandır. Bu alanda modül seçimi yapılmadığı takdirde tüm modüller ilgili vekalet verme işlemi gerçekleşir.

Vekalet Yönetimi ekranında vekaleti alan bilgisi personel listesiden seçilir. Vekaletin başlama ve bitiş tarihi bilgisi açılan takvim alanında seçilir. Vekalet verilecek modüller açılan modül listesinde seçim işlemi yapılır. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref19] butonu tıklanarak vekalet verme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_162.png)

Qdms Ana giriş ekranında Vekalet alan kişinin kullanıcı ve parolası ile Qdms sistemine giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_163.png)

Vekalet verme işleminde sonra sistem hangi personelle sistem giriş yapmasını sorar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_164.png)

Vekalet veren kullanıcı personel seçimi yapılarak Qdms’sine giriş yapılır. Kullanıcı adresine giriş yapıldığında vekalet verme işleminde vekalet işlemi için yetki verilen modüller sadece görüntülenir.  Vekalet verme işleminde Doküman Yönetimi,  Sistem Altyapı Tanımları ve Düzeltici ve Önleyici Faaliyetler Modüllerin yetkisi verildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_165.png)

Vekalet Görüntüyeci ekranında listede vekalet bilgisi seçili iken   ![ref21] butonu tıklanarak iptal işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_166.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_167.png)

Sistem Altyapı Tanımları modülü parametrelerinde  249 numaralı “Vekalet verme süresi” parametresine girilen değere göre maksimum vekalet verilecek süre bilgisi gün bazında değeri yazılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_168.png)

Vekalet Verme işlemi yapılan ekranında parametrede tanımlı maksimum vekalet süresi aşıldığında sistem uyarı mesajı verir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_169.png)

Girilen bu değerlere göre vekalet süresi belirlenir. Bu belirlenen  vekalet süresi vekalet verme süresi parametre değerindeki süreyi aştığında "Vekalet süresi maksimum vekalet süresinden büyük olamaz" uyarı mesajı sistem verir. Kullanıcılar istedikleri takdirde bu parametreye maksimum vekalet verilecek süre bilgisi gün bazında değeri yazarak parametresel ayarlama yapabilir.

**Vekalet Girişi:** Vekalet menüsünde vekalet verilme işlemi yapıldıktanın sonra Vekalet girişi işlemi  gerçekleştiği menüdür.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_170.png)

Bu menü tıklanarak  açılan personel listesinde personel seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_171.png)

Vekalet verilen kişinin yetki verilen modüllerin verildiği local adresinde  giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_172.png)

**Başkasının Adına Giriş (Süper Şifre):** Sistem Altyapı Tanımları modülünde modül yönetici olan kullanıcıların ekranında görüntülenen bir menüdür. Bu menü tıklanarak  Personel Tanımlama ekranı görüntülenir. Personel Tanımlama ekranında personel listesinde ilgili personel seçilerek butonlar kullanılarak vekalet girişi ve yerine giriş işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_173.png)**Ekranda bulunan butonlar yardımıyla;**

![ref24]: Listede seçili personelin vekalet giriş işlemi yapılır.

![ref25]:Listede seçili personelin sistemine giriş yapılır.

Personel Tanımlama ekranında listede seçili personel seçili iken ![ref24]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_176.png)

Seçili personelin Qdms local adresine giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_177.png)Vekaleten girişte sisteme vekaleten giriş yapılarak vekalet işlemlerinde olduğu gibi sistemde tüm işlemler yapılır ama raporlarda yapılan işlemlerde vekaleten  yapıldığı bilgisi yer alır.

Personel Tanımlama ekranında listede seçili personel seçili iken ![ref25]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_178.png)

Yerine Giriş işleminde personelin local adresine giriş yapan kullanıcı tüm işlemleri yerine giriş yaptığı kişi yapıyor şeklinde yapar.




**Hesap Ayarları:** Kullanıcının tema ayarları, Bilgileriniz, Dil ve Şifre değiştir menülerin yer aldığı ve bu menülerle  ile ilgili ayarlarının yapıldığı ve kullanıcıların bilgisayarlarının görünümünü kişiselleştirmelerine,  görsel deneyimlerini özelleştirmelerine olanak tanıyan  kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_179.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_180.png): Qdms sisteminin kullanıcı arayüzünün renklerinin  ve  arka planla zemin renginin değiştirme işlemi ayarlarının yapıldığı kısımdır. Qdms sisteminde bu menüde arka plan zemin rengi ve görüntüsü, kullanıcının tercihlerine göre değişme olanağını sağlar. Kullanıcı Hesapları ekranında Tema Ayarları kısmı tıklanılır.Açılan Tema Ayarları ekranında Ön İzleme, Zemin Görseli ve Tema Rengi alanları bulunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_181.png)

Ön İzleme alanında seçilen Zemin Görseli seçenekleri seçim işleminde ön izlemesi işlemi yapılır. Zemin Görseli alanında hangi zemin görseli seçeneği seçilirse o seçenek ön izlemede yer alarak görsel olarak görümünün takip edilip görüntülenir. Ön izleme alana göre kullanıcıların hangi zemin görseli Qdms sisteminde uyarlayacağı ve tasarlayacağı bilgisini bu kısımda elde eder. 

**Zemin Görseli:** Qdms sisteminde arka plan zemin rengi seçenekleri yer aldığı kısımdır. Kullanıcılar ilgili 4 seçenekten Qdms sisteminde uygun olanı zemin görseli seçimin ayarını yaparlar. Hesap Ayarları/Tema Ayarları/Ön izleme kısmında ise arka plan zemin seçeneklerinde seçtikleri arka plan zemin  görseli görüntüler ve uygun olanın seçimi yaparlar.

Kullanıcı Qdms sisteminde zemin Görseli alanında 3 numaralı seçenek seçilir.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_182.png)

Zemin görseli değişmesi için ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_183.png)  butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_184.png)

Qdms sisteminde “Tema değiştiğinde açık ekran ve panelleriniz kapanacaktır. Temayı değiştirmek istediğinizden emin misiniz?”  verdiği web sistesinin mesajında "Tamam" butonu tıklanarak Zemin görseli kayıt işlemi yapılır.Zemin Görseli kayıt işleminde sonra Qdms sistemi ekran görüntüsünde olduğu gibi zemin görseli görümünü alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_185.png)

Sistem Altyapı Tanımları modülü parametrelerinde 268 numaralı “Varsayılan arka plan duvar kağıdı” parametresi ile arka plan zemin rengi seçeneklerinde varsayılan arka plan zemin renginin ayarlama işlemi yapılır.  268 numaralı “Varsayılan arka plan duvar kağıdı” parametresi seçili iken ![ref26]   butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_187.png)

Açılan Parametreler ekranında Parametre değerine arka plan zemin rengi duvar kağıdı kod bilgisi yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_188.png)

Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_189.png) butonu tıklanarak paramete kayıt güncelleme işlemi yapılır. Kayıt işleminde sonra varsayılan arka plan zemin rengi ayarı yapılmıştır. Arka Plan Duvar Kağıdı kodları: Theme1;Theme2;Theme3;Theme4; 4 arka plan zemin rengi seçeneğin sırasıyla verilen kodlardır.Kodlar ilgili parametre açıklaması alanında yada Bimser Teknik Destek ekibinde destek  alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_190.png)

268 numaralı parametrede ayarlama işleminde sonra varsayılan arka zemin görselin seçeneğin uygulanması için Hesap Ayarları menüsünde Tema Ayarları kısmında   ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_191.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_192.png)Sistem otomatik olarak 268 numaralı parametredeki ayarlama işlemi yapılan arka plan zemin rengi seçeneklerinde varsayılan arka plan zemin renginin seçim işlemi yapar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_193.png)

Varsayılan arka plan zemin renginin seçim işleminden sonra uygulanması için ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_194.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_195.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_196.png)Qdms sistemin “Tema değiştiğinde açık ekran ve panelleriniz kapanacaktır. Temayı değiştirmek istediğinizden emin misiniz?” verdiği web sistesinin mesajında "Tamam" butonu tıklanılmasında sonra varsayılan arka plan zemin görsel seçeneği Qdms sistemine uyarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_197.png)

**Tema Rengi:** Qdms sisteminde  tema renginin renk paleti alanında ilgili renk seçeneği seçilerek değiştirme işleminin ayarının yapıldığı kısımdır. Hesap Ayarları /Tema Ayarları/Tema Rengi alanında Qdms sistemin tema renginin renk paleti alanında ilgili renk seçeneği seçilerek değiştirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_198.png)Hesap Ayarları /Tema Ayarları/Tema Rengi alanında Qdms sistemin tema renginin renk paleti alanında ilgili renk seçeneği seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_199.png)

Renk paleti alanında ilgili renk seçeneği seçildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_200.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_201.png)

Qdms sistemin “Tema değiştiğinde açık ekran ve panelleriniz kapanacaktır. Temayı değiştirmek istediğinizden emin misiniz?” verdiği web sistesinin mesajında "Tamam" butonu tıklanılmasında sonra tema rengi değiştirme işlemi yapılır.

Qdms sistemin Hesap Ayarları /Tema Ayarları/Tema Rengi alanında seçilen renge göre ekranında bekleyen işlerim kısmının  görüntülenmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_202.png)

Qdms sisteminde ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_203.png) butonu tıklanarak Modüllerin Entegre Yönetim Sistemi ve Sistem Altyapı Tanımları kısmının seçilen tema rengine göre görsel olarak görümü görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_204.png)

Örneğin Doküman Yönetimi Modülünde Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman Askıya Alma menüsü tıklanarak menünün seçilen tema renginde göre görsel görümü görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_205.png)

Qdms sisteminde tema rengini kullanıcı isteği doğrultusunda Hesap Ayarları /Tema Ayarları/Tema Rengi alanında  değiştirilme işlemi bu şekilde yapar.Sistem Altyapı Tanımları modülünde parametrelerde tema rengi varsayılan olarak ayarlama işlemi yapılır. Sistem Altyapı Tanımları  parametrelerinde 267 numaralı “	Varsayılan arka plan rengi” parametresinde parametre değerine  varsayılan olarak istenilen  rengin Hesap Ayarları/Tema Ayarları/Tema Rengi ekranında renk platetindeki rengin kodu bilgisi yazarak varsayılan arka plan rengi ayarlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_206.png)

Bu işlemin yapılması için 267 numaralı“	Varsayılan arka plan rengi”  parametresi seçili iken ![ref26]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_207.png)

Açılan Parametreler ekranında parametre değerine Hesap Ayarları/Tema Ayarları/Tema Rengi ekranında renk plaletindeki rengin kodu bilgisi yazılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_208.png)

Parametreler ekranında gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_209.png)  butonu tıklanarak parametre kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_210.png)

Parametrede tema renginin  varsayılan olarak ayarlama işleminde sonra Hesap Ayarları/Tema Ayarları/Tema Rengi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_211.png) butonu tıklanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_212.png)

Buton tıklanıldıktan sonra Sistem Altyapı Tanımları modülü parametrelerinde ayarlama işlemi yapılan varsayılan zemin görseli seçeneği ve tema rengi seçim işlemi sistem otomatik olarak yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_213.png)

Varsayılan zemin görseli ve tema renginin sistem otamatik olarak seçim işlemi yaptıktan sonra yapılan işlemleri uygulanması için  ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_214.png) butonun tıklanması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_215.png)

Qdms sistemin “Tema değiştiğinde açık ekran ve panelleriniz kapanacaktır. Temayı değiştirmek istediğinizden emin misiniz?” verdiği web sistesinin mesajında "Tamam" butonu tıklanılmasında sonra varsayılan zemin görseli ve tema rengine geçiş işlemi yapılır. Aşağıdaki ekran görüntüsünde olduğu gibi parametrede parametre değerinde varsayılan olarak ayarlanan zemin görseli seçeneği ve tema rengine geçiş yapıldığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_216.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_217.png): Profil Bilgileri, Kullanıcı İmza Yükleme ve QDMS Kullanım Sayaçları kısımların yer aldığı ve kısımlar ilgili ayarlamaların yapıldığı kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_218.png)**Profil Bilgileri:** Qdms sisteminde kullanıcının kişisel bilgilerin yer aldığı  ve kullanıcının isterse profil resminin yüklendiği kısımdır. Kullanıcının adı ve soyadı bilgisi, varsa mail adres bilgisi (Personel Tanımlama menüsünde mail adresi tanımlı ise bu kısma sistem tarafından otomatik olarak getirmektedir.) görüntülendiği  ve kullanıcının isteğine bağlı profil resmi yükleme işlemi ayarlamaları yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_219.png)

Hesap Ayarları/Bilgileriniz/Profil Bilgiler kısmında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_220.png) butonu tıklanılarak profil resmi yükleme işlemi yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_221.png)

Açılan Dosya Ekleme ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_222.png) butonu tıklanarak profil resmi için seçeciği bilgisayar ortamında kayıtlı profil resminin seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_223.png)

Qdms sisteminde kullanıcı adının  ve soyadı bilgisinin bulunduğu kısımda eklenen profil resmi görüntülenir. Eklenen resmi yüklemekten vazgeçmek isterse ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_224.png) butonu tıklayarak yükleme işleminden iptal edebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_225.png)

Eklenen Profil resmi Qdms sisteminde kullanıcı adı ve soyadı bilgisinin bulunduğu kısımda yer alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_226.png)

**Kullanıcı İmza Yükleme:** Hesap Ayarları/Bilgileriniz/Kullanıcı imzası yükleme alanında kısmında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_227.png)butonu tıklanarak  açılan Dosya Yükle ekranında kullanıcı imzasını bilgisayar ortamında Qdms sisteminde yükleme işlemini kullanıcı isterse yapabilir. 

**QDMS Kullanım Sayaçları:** Hesap Ayarları/Bilgileriniz/QDMS Kullanım Sayaçları menüsü tıklanarak açılan ekranda kullanıcı ve toplam bazlı Qdms sistemine günlük, aylık, yıllık giriş sayıları bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_228.png)


![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_229.png): Şifre değiştirme işleminin yapıldığı menüdür. Şifre Değiştir ekranında şu anki şifreniz alanın mevcut şifre bilgisi girilir. Yeni şifreniz alanında yeni şifre bilgisi girilir. Yeni şifreniz Tekrar alanında yeni şifre bilgisi tekrar yazılır. Şifre Değiştir alanın gerekli alanlar dolduruldıuktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_230.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_231.png)

Sistem tarafından “Şifreniz başarıyla değiştirildi. Mevcut kullanıcı adınız ve yeni oluşturduğunuz şifre ile QDMS uygulamanıza giriş yapabilirsiniz.” mesajında “Tamam” butonu tıklanarak şifre değiştirme kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_232.png)

Eğer active directory var ise şifre bilgisayar şifresi değişimi sırasında değişir, bu menü kullanılmaz.

![ref27]Dil: Qdms ana giriş ekranında sisteminde kullanılan diller arasında geçiş yapıldığı ve çoklu dil desteğin sağlandığı kısımdır. İngilizce dil seçeneği sistemde otomatik olarak kurulu gelmektedir. Diğer dil seçenekleri firmaların ihtiyacına göre sisteme yüklenmektedir. Dil kısmında sistemi ingilizce olarak çalıştırmak için açılır dil listesinde  “EN” seçeneği seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_234.png)

Dil seçeneği “EN” olarak seçildikten sonra Qdms sistemin verdiği “Dil değiştiğinde açık ekran ve panelleriniz kapanacaktır. Dili değiştirmek istediğinizden emin misiniz?” web sistesinin mesajında " “Tamam” butonu tıklanarak Qdms sisteminin program dili ingilizce olarak değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_235.png)

Qdms sisteminde  Bekleyen İşlerim ve diğer kısımlarda program dili ingilizce olarak görüntülenir.Qdms ana giriş ekranında bulanan  ![ref27] bu  buton ile diller arası geçiş işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_236.png)

**QDMS Sisteminde Menülerin Özellikleri;**

**Grid Özelliği:** Qdms gridlerinde özelliği yeni gelen 5.26.0 versiyon ile değişmiştir.Qdms gridlerinde gruplama özelliği getirilmiştir. Qdms sisteminde gridlerdeki veri yönetimini daha kolay ve esnek hale getirmek için alan editörü eklenmiştir, böylece kullanıcılar sütunları istedikleri gibi ekleyip kaldırabilir ve veri görüntüleme deneyimini kişiselleştirilmesi sağlanmıştır. Ayrıca Qdms sisteminde sütunlara göre gruplama özelliği de artık mevcut, bu sayede kullanıcılar verileri daha düzenli ve anlamlı gruplar halinde görüntüleyebilir ve istedikleri bilgilere daha hızlı erişebilirler.Örneğin: İl Tanımlama menüsünde gridlerde getirilen yeni özelliği görüntüleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_237.png)

Gruplama özellğini uygulamak için  girid ekranında kolanların karşılığı olan alanları için mouse ile alanın üzeri tıklanarak süreklenerek “Sütun başlığını o sütuna göre gruplamak için buraya sürükle” alana getirilerek Qdms sisteminde gridlerde gruplama özelliği yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_238.png)

**“Filtre Temizleme” Özelliği:** Qdms menü ekranlarında Filtre temizleme işlemi yapılır.Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.Bu buton ile kullanıcının filtre arama kriterlerinde  filtreleme işlemlerinde yazılan  verilerin silinme işlemi yapılır. Veri filtreleme işlemleri için ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_239.png) (Filtreyi Temizle) butonu eklenerek kullanıcılar filtreleri kolayca temizleyip yeni filtrelemelere geçebilmeleri bu buton sayesinde Qdms sisteminde sağlanmıştır. Örn:İl Tanımlama menüsünde gridde İl Adı alanında arama kriteri yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_240.png)

İl Tanımlama ekranında gridde filtreleme işleminin temizlemek için ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_241.png)(Filtreyi Temizle) butonu tıklanılarak griddeki arama  kriterlerindeki verinin silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_242.png)

**“Kullanıcı Ayarlarını Temizle” Özelliği:** Kullanıcıların menü ekranlarında filtreleme, kolon gizleme, gridde gruplama özelliği  gibi işlemlerden sonra menü ekranın tekrar varsayılan ayarlama gelmesini işlemi sağlayan bir özelliktir. Qdms sisteminde kullanıcıların kişisel tercihleri, sütun sıralamaları ve filtreleme geçmişini sıfırlamak için ![ref28] (Kullanıcı Ayarlarını Temizle) butonu eklenerek bu özelliğin kullanılması  sağlanmıştır. Örn: İl Tanımlama ekranında gridde gruplama özelliği

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_244.png)

İl Tanımlama ekranında tekrar varsayılan ayarlarına yani menü ekranın ilk kez kullanılmaya başlandığında veya herhangi bir yapılandırma değişikliği yapılmadığında durumuna getirmek için ![ref28] (Kullanıcı Ayarların Temizle) butonu tıklanılır. Buton tıklanıldıktan sonra menü ekranın vasayılan ayarlarında getirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_245.png)

**“Kolon Seçiçi” Özelliği:** Qdms sistemi menü ekranlarda grid ekranlarındaki kolon karşılığı alanları saklama işlemi yapılır.Bu özelliğin kullanılması için ![ref29] (Kolon Seçici) butonu tıklanarak Alan seçici ekranı açılır. Açılan Alan seçiçi ekranında kullanıcı menü ekranı istemediği gridde alanları ekleyerek kendi isteğine göre menü ekranın tasarlama işlemi yapar.Kolon seçici ekranında açılan alan seçici ekranın gridde bulunan görüntülenmesi istemediği alanları mouse tutup -sürekle yöntemi ile Alan seçici ekranı ekleyerek alanın menü ekranında görüntülenmemesi sağlar.İstediği şekilde alanları menü ekranların gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapar. Qdms sisteminde kullanıcı bazlı yapılan bu özellikle ile her kullanıcı kendi menü ekranlarınında tasarlama işlemi yapılması sağlanmıştır.Örn: İl Tanımlama menüsünde  İl Kodu alanı Alan Seçici ekranı eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_247.png)

Alan Seçisi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_248.png)(Kapat) butonu tıklanarak Alan Seçici ekranı kapatılır. Kullanıcı menü ekranın istediği şekilde tasarlama işlemi yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_249.png)

![ref29] (Kolon Seçici) butonu ile gizlenen kolonların tekrar varsayılan ayarlarına getirilmesi için ![ref28] (Kullanıcı Ayarları Temizle) butonu tıklanarak  menü ekranın eski haline getirilmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_250.png)


### **5.1. BSAT (Bimser Sistem Altyapı Tanımları)/ Tanımlar**
**Menü Adı:** Sistem Altyapı Tanımlamaları/ BSAT/ Tanımlar

Qdms sisteminin kullanımı için gerekli olan personel bilgileri, müşteri bilgileri, ürün bilgiler, gibi bilgiler olan altyapı tanımlamalarının sistemde tanımlandığı kısımdır. Sistem Altyapı Tanımları/ BSAT/ Tanımlar ekranından yapılan önemli tanımlamalar unvan, departman, personel ve pozisyon tanımlamalarıdır. Firmanın personel verilerinin bulunduğu program ile Qdms arasında bir entegrasyon sağlanarak (HR Entegrasyonu) personel verilerinin otomatik olarak Qdms sistemine aktarılması sağlanabilir. Böyle bir durumda ilk 4 menüde herhangi bir işlem yapmaya gerek kalmaz. Eğer firmada Personel Entegrasyonu sağlandıysa, yeni bir personel ekleneceği zaman veya bir personel işten ayrıldığı zaman sistemde herhangi bir işlem yapmaya gerek kalmadan entegrasyon ile personel durumu otomatik olarak güncellenmiş olur.
#### **5.1.1.Duyuru Oluştur**
**Menü Adı: Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/Duyuru Oluştur

Duyuru tanımlama işleminin yapıldığı menüdür. Bu menüde tanımlanan duyurularının güncelleme ve silme işlemleri  yapılır. Tanımlanan Duyuruların  yetkilendirme işlemi Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları /Duyuru Yetki Matrisi menüsünde yapılmaktadır. Yetkilendirme işlemi yapılan duyurular kullanıcının giriş ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_251.png) butonu tıklanarak açılan Duyurular ekranında listede yer alır. İlgili Duyuru tıklanarak duyurunun içeriğinde detay bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_252.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref3]: Yeni bir duyuru  tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_253.png): Listede seçili duyuru bilgisi üzerinde değişiklik/güncelleme işlemi yapılır. Kod bilgisi güncellenemez.

![ref5]: Listede seçili duyuru bilgisi silinir.

![ref30]:Arama kriterlerine göre filtreleme işlemi yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Duyuru Oluştur ekranına yeni bir duyuru tanımı eklemek için ekranın sol üst köşesindeki ![ref31] butonuna tıklanarak Duyuru oluştur/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_256.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kod:** Duyuru Oluştur - Yeni Kayıt ekranında tanımlanan duyurunun kod bilgisinin yazıldığı zorunlu alandır.  Kod bilgisi iş yeri, Departman ve Kullanıcı grubu listesinde seçim yapılmasına göre gelmektedir. 

İş yeri seçimi yapıldığında verilen kod- İş yeri kodu şeklinde tanımlanmaktadır.  

Departman seçimi yapıldığında verilen kod- Departmanın kodu şeklinde kod bilgisi tanımlanmaktadır. 

Kullanıcı Grubu seçimi yapıldığında verilen kod-Kullanıcı Grubu kodu şeklinde tanımlı gelmektedir.

İş Yeri seçimi yapıldığı için D.009-001 şeklinde verilen kod  -iş yeri kodu gelecek şeklinde kod atamasını sistem yapar.

**Duyuru Başlığı:** Duyuru Oluştur - Yeni Kayıt ekranında tanımlanan duyurunun başlığının yazıldığı zorunlu alandır.

**Duyuru Detayı:** Duyuru Oluştur - Yeni Kayıt ekranında tanımlanan duyurunun detay bilgisinin yazıldığı zorunlu alandır.

**Geçerlilik Tarihi	:** Duyuru Oluştur - Yeni Kayıt ekranında tanımlanan duyurunun geçerlilik tarihi bilgisinin açılan takvim alanında seçildiği yazıldığı zorunlu alandır.

**İş Yeri:** Duyuru Oluştur - Yeni Kayıt ekranında tanımlanan duyurunun işyeri bilgisinin ![ref32] (Ekle) butonu tıklanarak açılan iş yeri listesinde seçildiği  zorunlu alandır. İş Yeri  listesi bilgisi Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları /Duyuru Yetki Matrisi menüsünde yetkilendirme işlemi yapılan iş yerlerinden oluşmaktadır.

**Departmanı:** Duyuru Oluştur - Yeni Kayıt ekranında	tanımlanan duyurunun varsa departman bilgisinin ![ref32] (Ekle) butonu tıklanarak açılan departman listesinde seçildiği  zorunlu alandır. Departman  listesi bilgisi Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları /Duyuru Yetki Matrisi menüsünde yetkilendirme işlemi yapılan Departmanlardan  oluşmaktadır.

**Kullanıcı Grubu:** Duyuru Oluştur - Yeni Kayıt ekranında tanımlanan duyurunun varsa kullanıcı grubu bilgisinin ![ref32] (Ekle) butonu tıklanarak açılan kullanıcı grubu listesinde seçildiği  zorunlu alandır. Kullanıcı grubu  listesi bilgisi Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları /Duyuru Yetki Matrisi menüsünde yetkilendirme işlemi yapılan Kullanıcı gruplarından  oluşmaktadır.

Duyuru Oluştur - Yeni Kayıt ekranında	tanımlanan duyurunun kod, duyuru başlığı, duyuru detay bilgileri yazılır. Duyuru yetki matrisinde yetkilendirme yapılan iş yeri bilgisi  seçilir.   Duyuru Tanımlama ekranında iş yeri, departman ve kullanıcı grubu seçimi yapıldığında duyuru tanımlama işlemi seçime göre tanımlanmaktadır. Eğer Duyuru Tanımlama ekranında departman ve kullanıcı grubu  seçimi yapılmış olsaydı bu alanlara göre sistem  ek olarak duyuru tanımlama işlemi yapacaktır. 

**Duyuru Tanımlama ekranında seçime göre kod ataması ve duyuru oluşturulması:**

**İş yeri:** Tanımlanan kod- İşyeri Kodu  gelecek şekilde  kodu olan bir duyuru tanımlama işlemi yapar.

**Departman:** Tanımlanan kod-Departman kodu  gelecek şekilde kodu olan bir duyuru tanımlama işlemi yapar.

**Kullanıcı Grubu:** Tanımlanan kod-Kullanıcı grubu kodu  gelecek şekilde kodu olan bir duyuru tanımlama işlemi yapar.Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_258.png) butonu tıklanarak duyuru tanımlama kayıt işlemi yapılır. Sadece İş yeri seçimine göre duyuru tanımlama işlemi yapıldığında D.009-001 kodlu duyuru tanımlama işlemi yapılmıştır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_259.png)

Duyuru tanımlama ve Duyuru Yetki matrisinde yapılan yetkilendirme işlemlerinde  sonra kullanıcının Qdms ana giriş ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_260.png) buton tıklanarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_261.png)

Açılan Duyurlar ekranında duyuru tıklanarak  duyurun görüntülenmesi işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_262.png)

Filtre sekmesinde arama kriterleri olan  Kod, Duyuru başlığı, Duyuru detayı gibi alanlara veri girilip, ![ref30] (Ara) butonu tıklanarak  arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_263.png) 
#### **5.1.2. Unvan Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Unvan Tanımlama

Personel tanımlaması için gerekli olan unvanların tanımlamasının yapıldığı menüdür. Firma içerisinde kullanılan unvanlar tanımlanır.Müdür, Uzman, Direktör gibi. HR Entegrasyonu mevcutsa tüm unvanlar otomatik olarak Qdms sistemine aktarılır. Unvanlar kullanıcıya özgü değildir, yani birden fazla kullanıcıya aynı unvan tanımı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_264.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref31]: Yeni bir unvan tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_265.png): Listede seçili olan unvan bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi güncellenemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_266.png): Listede seçili olan unvan bilgisi silinir.  Eğer seçilen unvan bilgisi personel tanımlama ekranında bir personelle eşleştirildiyse bu unvan bilgisinin silinmesine sistem tarafından izin verilmez.

![ref22]: Kayıtlar filtrelenerek arama yapılabilir.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

Unvan Tanımlama ekranına yeni bir unvan tanımı eklemek için ekranın sol üst köşesindeki ![ref31] butonuna tıklanarak Unvan Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_267.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Unvan Kodu:** Unvan Tanımlama-Yeni Kayıt ekranında Unvan kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Unvan Tanımı:** Unvan Tanımlama-Yeni Kayıt ekranında Unvan tanım bilgisinin tanımlandığı zorunlu alandır. Örnek olarak; Müdür, yönetici, uzman, mühendis vb. olacak şekilde tanımlama yapılır. Diğer dil seçenekleri de kullanılacaksa ilgili bayrağın bulunduğu yere ilgili unvan tanımın  dil karşılığı yazılır.

**Üst Unvanı:** Unvan Tanımlama-Yeni Kayıt ekranında Üst unvan bilgisinin açılır unvan listesinden seçildiği alandır. Tanımlama yaparken en üst unvandan başlanmalıdır. Bu sayede alt unvanlar tanımlanırken üst unvanlar ile ilişkileri kurulabilir.

**Durum:** Unvan Tanımlama-Yeni Kayıt ekranında Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar unvanların sistemde artık kullanılmadığına bir işarettir. Kullanılmayan unvanları görmek için filtre sekmesinden arama kriterlerinde durum alanında  "Pasif" olarak arama yapılması yeterlidir. Pasif özelliği Departman Tanımlama, Pozisyon Tanımlama menülerinde de aynı şekilde çalışmaktadır

Unvan Tanımlama-Yeni Kayıt ekranda unvan kodu, tanımı, varsa bir üst unvan ve durum alanında “Aktif” seçeneği seçim işlemleri yapılır. Unvan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref33] butonuna tıklanarak Unvan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_269.png)

Unvan Tanımlama ekranında Filtre sekmesinde Unvan Kodu, Unvan Tanımı, Durum ve İş Yeri gibi alanlara veri girilip,  ![ref22] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_270.png)
#### **5.1.3. Departman Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Departman Tanımlama

Firma içerisinde bulunan belli bir işi yapmak üzere ayrılmış, oluşturulmuş bölümler olan departmanların tanımlama işlemi yapılır. Üretim, Pazarlama, Muhasebe, Ar-ge (Araştırma-Geliştirme) gibi. HR Entegrasyonu mevcutsa firma içerinde olan departmanlar otomatik olarak Qdms sistemine aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_271.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref34]: Yeni bir departman tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_273.png): Listede seçili olan departman bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi güncellenemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_274.png): Listede seçili olan departman bilgisi silinir.  Eğer seçilen departman bilgisi personel tanımlama ekranında bir personelle eşleştirildiyse bu departman bilgisinin silinmesine sistem tarafından izin verilmez.

![ref35]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

Departman Tanımlama ekranına yeni bir departman tanımı eklemek için ekranın sol üst köşesindeki ![ref34]  butonuna tıklanarak Departman Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_276.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Departman Kodu:** Departman Tanımlama-Yeni Kayıt ekranında departman kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Departman Adı:** Departman Tanımlama-Yeni Kayıt ekranında Departman tanım bilgisinin tanımlandığı zorunlu alandır. Örnek olarak; Pazarlama, Finans, Muhase, İnsan Kaynakları, Halkla İlişkiler vb. olacak şekilde tanımlama yapılır. İlgili bayrakların bulunduğu alanlarda departman adı bilgisinin dil karşılıkları yazılır.

**Departman Sorumlusu:** Departman Tanımlama-Yeni Kayıt ekranında Departman Sorumlusu ![ref36] (Seç) butonu  tıklanarak açılan sistemde tanımlı olan pozisyon listesinden seçildiği alandır. Qdms sisteminde departman sorumluları modüllerin akışında kullanılabilir.

**Üst Departman:** Departman Tanımlama-Yeni Kayıt ekranında Üst Departman bilgisinin açılır departman listesinde seçildiği alandır.

**Masraf Yeri:** Departman Tanımlama-Yeni Kayıt ekranında Masraf yeri bilgisinin açılır masraf yeri listesinde seçildiği alandır. Masraf yeri listesi Sistem Altyapı Tanımları /BSAT/Tanımlar/Masraf Yeri Tanımlama menüsünde tanımlı gelmektedir.

**Durum:** Departman Tanımlama-Yeni Kayıt ekranında Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar departmanlar sistemde artık kullanılmadığına bir işarettir. Kullanılmayan departmanlar görmek için filtre sekmesinden arama kriterlerinde durum alanında  "Pasif" olarak arama yapılması yeterlidir.

**Departman Haritası**: Departman Tanımlama-Yeni Kayıt ekranında Departman ait harita bilgisi varsa ![ref36] (Ekle) butonu tıklanarak eklendiği alandır. İç İş İzni Takibi modülünde kullanılanan bir alandır. Departman İçin Çalışma yapılacak harita bilgisinin eklenmesi sağlanır. 

Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsünde Modül listesinden  Sistem Altyapı Tanımları modülü  seçilir ve Sistem Altyapı Tanımları ile ilgili dil tanımları görüntülenir. Başlıklar sekmesinde gridde adı alanına “lblDepartmanHarita” label kod bilgisi yazılarak  pasif alan seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_278.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_279.png)

Açılan Dil Ayarları ekranında  değeri alanında alanın adı bilgisi yazılarak, ilgili bayrağın bulunduğu alanlanın ingilizce dil karşılığı, alanın zorunlu, olup olmayacağı belirlenir. İstenirse başlık notu bilgisi yazılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_280.png)

Gerekli alanlar ilgili bilgiler yazıldıktan ekranın sol üst köşesindeki ![ref33]  butonu tıklanarak Dil ayarları kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_281.png)

Departman  Haritası alanında ![ref36] (Ekle) butonu ile eklenen harita İç İş İzni Takibi Modülünde  Entegre Yönetim Sistemi/İç İş İzni Takibi/İç İş İzni Talep Formu İşlemleri ekranında yeni bir form tanımlama işleminde Departman seçimi yapıldığında ilgili departmanda tanımlama ekranında eklenen harita çalışma yapılacak harita alanında  görüntülenir. Aynı şekilde Yüklenici İş İzni Takibi Modülünde  Entegre Yönetim Sistemi/Yüklenici İş İzni Takibi/Yüklenici İş İzni Talep Formu İşlemleri  ekranında çalışma yapılacak harita alanında   departman tanımlama ekranında eklenen harita görüntülenir ve çalışma yapılacak kısımlar işaretlenir.

Açılan Departman Tanımlama-Yeni Kayıt ekranda Departmanın Kodu, Departman Adı yazılır. Departman Sorumlusu sistemde tanımlı olan pozisyon listesinden seçilir. Varsa Üst Departman bilgisi açılır departman listesinde seçilir. Durum bilgisi "Aktif"seçeneği olarak seçelir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref33]  butonuna tıklanarak Departman Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_282.png)

Departman Tanımlama ekranında Filtre sekmesi ile Departman Kodu, Departman Adı, Departman Sorumlusu, Durum ve İş Yeri gibi alanlarına veri girilip,  ![ref35] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_283.png)
#### **5.1.4. Personel Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları / BSAT/ Tanımlar/ Personel Tanımlama

Firmada çalışan personellerin Qdms sistemine tanımlandığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_284.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref37]: Yeni bir personel tanımlanır.

![ref38]: Listede seçili olan personel bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. Sicil No bilgisi değiştirilemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_287.png):Listede seçili personel bilgisi silinir.

![ref39]: Listede seçili olan personel için TC Kimlik No, Cinsiyet, Boy, Kilo gibi ek bilgilerin girişi yapılır. Bu bilgiler İşbaşı ve Periyodik Muayene ve Eğitim Planlama modüllerinde kullanılır (Sistem Altyapı Tanımları modülü parametrelerinde 76 numaralı “Personel Tanımlamada Ek Alanlar Kullanılsın Mı?” paramatre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_289.png)

Parametre aktif edildikten sonra Personel Tanımlama ekranında ![ref39]  butonu görüntülenir.

![ref35]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Personel Tanımlama ekranına yeni bir personel eklemek için ekranın sol üst köşesindeki ![ref37]  butonuna tıklanarak Personel Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_290.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sicil No:** Personel Tanımlama - Yeni Kayıt ekranında personelin  Sicil no bilgisinini girildiği zorunlu alandır. Qdms ana giriş ekranında kullanıcı adı kısmında sicil no  ve  parola kısmında parola bilgileri yazılarak  personel  Qdms local adresine giriş yapar. Eğer Active Directory Entegrasyonu sağlandıysa; personel, bilgisayarını açtığı kullanıcı adı/ şifre bilgisi ile Qdms local adresine giriş yapabilir. Active directory entegrasyonunun sağlanması için Bimser Teknik Personelinden destek alınmalıdır.

**Adı:** Personel Tanımlama - Yeni Kayıt ekranında personeli adı bilgisinin tanımlandığı zorunlu alandır.

**Soyadı:** Personel Tanımlama - Yeni Kayıt ekranında personelin soyadı bilgisinin tanımlandığı alandır.

**Parola:** Personel Tanımlama - Yeni Kayıt ekranında personelin parola bilgisinin tanımlandığı alandır.Tanımlanan bu parola ile Qdms ana giriş ekranında  kullanıcı adı ve parola alanı parola bilgisini yazarak personel Qdms local adresine giriş yapar.

**Parola Tekrar:** Personel Tanımlama - Yeni Kayıt ekranında tanımlanan parola bilgisinin tekrar edildiği alandır.

**İş Yeri:** Personel Tanımlama - Yeni Kayıt ekranında Personelin işyeri bilgisinin  ![ref40] (Seç) butonu tıklanarak açılan sistemde tanımlı İş yeri listesinde seçildiği alandır. İş Yeri Listesi Sistem Altyapı Tanımları/BSAT/Tanımlar/ İş Yeri Tanımlama menüsünde tanımlı olarak gelmektedir. Firma birden fazla lokasyonu olan bir işyeri ise “İşyeri Tanımlama” menüsünde tanımlanan işyeri bilgilerinden seçim yapılarak personelin çalıştığı işyeri belirlenir. Tek lokasyonu olan işyerleri için de işyeri tanımının yapılması gerekmektedir. Personel tanımlama ekranında bu ayrım yapıldığı zaman işyerleri bazında filtre uygulanarak personelin kendi işyerinde açılmış olan görevleri görmesi sağlanabilir.  Personel tanımlama ekranında iş yeri alanın gelmesi parametreye bağlı olarak gelmektedir. Sistem Altyapı Tanımları modülü parametrelerinde 21 numaralı “İş yeri Kullanılsın mı?(E/H)” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_292.png)

Parametre aktif edildikten sonra Personel Tanımlama -Yeni Kayıt ekranında İş Yeri alanı görüntülenir ve personellerin iş yeri bilgisi görüntülenen bu alanla ilişkilendirilir.

**Masraf Yeri:** Personel Tanımlama - Yeni Kayıt ekranında personelin ait olduğu masraf yeri bilgisi ![ref40] (Seç) butonu tıklanarak açılan sistemde tanımlı masraf yeri listesinden seçildiği alandır. (Masraf  Yeri listesi Sistem Altyapı Tanımları/BSAT/Tanımlar/Masraf Yeri Tanımlama menüsünde tanımlı olarak gelmektedir.)

**Unvan:** Personel Tanımlama - Yeni Kayıt ekranında personelin unvan bilgisinin ![ref40] (Seç) butonu tıklanarak açılan sistemde tanımlı unvan bilgisinden seçildiği alandır.(Unvan Listesi Sistem Altyapı Tanımları/BSAT/Tanımlar/ Unvan Tanımlama menüsünde tanımlı olarak gelmektedir.)

**Departman:** Personel Tanımlama - Yeni Kayıt ekranında personelin bulunduğu departman bilgisinin ![ref40] (Seç) butonu tıklanarak açılan sistemde tanımlı departman bilgisinden seçildiği alandır.(Departman Listesi Sistem Altyapı Tanımları/BSAT/Tanımlar/ Departman Tanımlama menüsünde tanımlı olarak gelmektedir.)

**Bağlı Bulunduğu Pozisyon:** Personel Tanımlama - Yeni Kayıt ekranında personelin bağlı bulunduğu poazisyon bilgisi ![ref40] (Seç) butonu tıklanarak açılan sistemde tanımlı Pozisyon listesinde seçildiği alandır.( Pozisyon Listesi Sistem Altyapı Tanımları/BSAT/Tanımlar/ Pozisyon Tanımlama menüsünde tanımlı olarak gelmektedir.)Personelin bekleyen işlerindeki görevin gecikmeye düştüğü zaman üst amirine bilgilendirme maili gitmesi isteniyorsa personelin “Bağlı Bulunduğu Pozisyon” bilgisi dolu olması gerekmektedir. Bu alana personelin ilk amiri kimse o kişinin pozisyonu seçilmelidir. Ayrıca bu bilgi, modüllerdeki planlanan işler için bilgilendirme maili gitmesi amacıyla, modül onay akışlarında eğer onaycı olarak üst amir kullanılacaksa akışın çalışması amacıyla kullanılabilir

**Durum:** Personel Tanımlama - Yeni Kayıt ekranında personelin durum bilgisinin  açılır liste tıklanarak açılan sistemde tanımlı durum seçeneklerinde seçildiği alandır. Durum” alanı kısmında “Aktif, İşten Ayrıldı, Misafir ve İş Başvurusu” seçeneklerinden uygun olan seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_293.png)

Bir personel işten ayrıldığı zaman (eğer entegrasyon yoksa)  personel tanımlama ekranından işten ayrılan personel seçilir. Personel seçili iken  ![ref38]  butonuna kullanılarak, durum alanından ilgili personel için “İşten ayrıldı” seçilir ve kayıt edilir. Ardından Pozisyon Tanımlama menüsündeki kişinin bulunduğu pozisyon bilgisi seçilerek pozisyon sahibi alanından işten ayrılan kişi bilgisi temizlenir ve pozisyon kaydedilir. Aynı görevle işe başlayan personel geldiğinde ya da görev değişiklikleri olduğunda boş olan pozisyon sahibi alanı doldurulursa, işten ayrılan personelin üzerinde bulunan görevler, yeni gelen personele aktarılmış olur. HR Entegrasyonu sağlandığı durumlarda personel işe giriş çıkışları otomatik olarak gerçekleşir. Durum kısmı seçenekleri görüntülemesi işlemi için Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Sabitler menüsü tıklanılır.  Açılan Sabitler ekranında Filtre sekmesinde Modüller alanında Modül olarak Sistem Altyapı Tanımları modülü seçilerek ![ref41] (Ara) butonu tıklanarak ilgili modülle ilgili sabit değerlerin listelenmesi sağlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_295.png)

Liste sekmesinde listelenen Sabit değerleri listesinde Durum alanı sabit değeri “Durum” alanı seçili iken ![ref38]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_296.png)

Açılan Sabitler ekranında Durum alanın  sabit değerleri seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_297.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_298.png)

Açılan Sabit Değerleri- Kayıt Güncelle ekranında sabit değerin Durum alanında seçeneklerinden “Pasif” seçeneği seçilir. İstenirse Sabitler ekranında Durum alanın seçeneklerinin aktif olarak seçilen sabit değerin varsayılan olarak ayarlama işlemide yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_299.png)

Sabit Değerleri -Kayıt Günceleme ekranında durum alanı üzerideki değişiklikten sonra ekranın sol üstte köşede yer  alan ![ref33]  butonuna tıklanarak sabit değeri kayıt güncelleme işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_300.png)

Sabit Değerleri ekranında Durum alanın sabit değeri  durumu “Pasif” edildikten sonra ekranın sol üst köşesindeki ![ref33] butonu tıklanarak kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_301.png)

Bu kayıt işleminde sonra Personel Tanımlama-Yeni Kayıt ekranında Durum alanında “Misafir” seçeneğinin görüntülenmemesi sağlanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_302.png)

**Kategori:** Personel Tanımlama - Yeni Kayıt ekranında personelin kategori bilgisinin açılır liste tıklanrak açılan kategori listesinde seçildiği alandır. Kategori alanında personelin kapsam içi, kapsam dışı, sözleşmeli, müteahhit, transfer gibi çalışma durumları belirlenir. Personeller, otomatik olarak sistemde kapsam içi tanımlanmaktadır. Dışarıdan hizmet alımıyla gerçekleştirilen danışmanlık gibi işlemler için Qdms sisteminde  personel tanımlanması yapılmak isteniyorsa bu personeller kapsam dışı olarak sisteme tanımlanmalıdır. Eğer HR Entegrasyonu varsa ve belirlenen periyodlar için gerçekleşen entegrasyon kapsamında HR verisi çekilecek programdan gelen personeller dışında sistemde manuel tanımlanan olan personelin (örneğin; danışman, denetçi gibi) entegrasyon sonucu sistemden çıkarılması istenmiyorsa personelin “transfer dışı” olarak kaydedilmesi sağlanmalıdır. Bu işlemi gerçekleştirebilmek için öncelikle transfer dışı özelliğinin aktif edilmesi gerekmektedir. Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametreler menüsünden Filtre sekmesinde modüller alanında modül listesinde  “Sistem Altyapı Tanımları” modülü seçilir.Parametre No alanında parametre numarası bilgisi yazılarak  ![ref42] (Ara) butonu tıklanarak parametrenin görüntülenip, seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_304.png)

30\.parametre olan “Personel kategorileri (Birden fazla için virgül ile ayırarak yazınız)” parametresine “Transfer Dışı” seçeneği eklenmelidir.

Parametler ekranında liste sekmesinde listede 30 numaralı “Personel kategorileri (Birden fazla için virgül ile ayırarak yazınız)”  parametresi seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_305.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_306.png)

Açılan Parametreler ekranında Parametre değeri alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_307.png)   butonu tıklanarak yeni bir kategori ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_308.png)

Açılan Listeye Ekle - Yeni Kayıt ekranında tanımlanacak kategorinin kodu ve değer alanları ilgili bilgileri girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_309.png)

Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref43]   butonu tıklanarak   kayıt işlemi yapılır. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_311.png)

Parametreler ekranında değişiklerin kaydedilmesi için tekrar ekranın sol üstte yer alan ![ref43] butonu tıklanarak parametre kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_312.png) Parametre Kayıt işleminde sonra Personel Tanımlama-Yeni Kayıt ekranında Kategori alanında “Transfer Dışı” seçeneğinin seçeneklerde yer aldığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_313.png)

**Doğum Tarihi:** Personel Tanımlama - Yeni Kayıt ekranında personelin doğum Tarihi bilgisinin açılan Takvim alanında seçildiği alandır.( Eğitim Modülü kullanılacaksa ve bu Modüldeki personel eğitim kartı gibi raporlar sistemden çekilecekse bu alanın doldurulması gerekmektedir.)

**İşe Giriş Tarihi:** Personel Tanımlama - Yeni Kayıt ekranında personelin İşe giriş Tarihi  bilgisinin açılan Takvim alanında seçildiği alandır. ( Eğitim Modülü kullanılacaksa ve bu Modüldeki personel eğitim kartı gibi raporlar sistemden çekilecekse bu alanın doldurulması gerekmektedir.)

**İşten Çıkış Tarihi:** Personel Tanımlama - Yeni Kayıt ekranında personelin İşten Çıkış Tarihi bilgisinin açılan Takvim alanında seçildiği alandır. ( Eğitim Modülü kullanılacaksa ve bu Modüldeki personel eğitim kartı gibi raporlar sistemden çekilecekse bu alanın doldurulması gerekmektedir.)

**Eğitim Seviyesi:** Personel Tanımlama - Yeni Kayıt ekranında personelin eğitim seviyesinin açılır liste tıklanarak açılan eğitim seviyesi listesinde seçildiği alandır. ( Eğitim Modülü kullanılacaksa ve bu Modüldeki personel eğitim kartı gibi raporlar sistemden çekilecekse bu alanın doldurulması gerekmektedir.)Eğitim seviyesi alanında kayıtlı seçenekte üzerinde  değişiklik yapma işlemleri Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Sabitler menüsünde yapılmaktadır.Sabitler menüsünde Filtre sekmesinde modüller alanında “Sistem Altyapı Tanımları “ modülü seçilerek  ve sabit No alanında sabit numarası “5” yazılarak  ![ref42] (Ara) butonu tıklanarak “Öğrenim Durumu” sabitini görüntülenip, seçilme işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_314.png)

Sabitler ekranında “Öğrenim Durumu “ sabiti seçili iken ![ref44]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_316.png)

Sabitler ekranında sabit değeri seçili iken ![ref44]  butonu  tıklanarak sabit değeri ile ilgili düzenleme/Değişiklik/Günceleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_317.png)

Sabit Değerleri - Kayıt Güncelle ekranında değer alanı ile ilgili güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_318.png)

Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref43]  butonu tıklanarak sabit değeri kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_319.png)

Sabitler ekranında yapılan değişiklerden sonra ekranın sol üstte yer alan  ![ref43]  butonu tıklanarak sabit kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_320.png)

Sabitler kayıt günceleme işleminde sonra Personel Tanımlama-Yeni Kayıt ekranında Eğitim Seviyesi alanında yapılan seçenek üzerinde değişiklik yapıldığı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_321.png)

**Active Directory Kullanıcı Adı:** Personel Tanımlama - Yeni Kayıt ekranında personelin Active Directory Kullanıcı Adının tanımlandığı alandır. Eğer Active Directory entegrasyonu sağlanacaksa (yani personelin bilgisayarını açtığı kullanıcı adı ve şifre ile Qdms sistemine giriş yapması isteniyorsa) “Active Directory User Name” kısmı tanımlanır. Bu alana personelin bilgisayarını açarken girdiği kullanıcı adı bilgisi yazılır.

**E-posta:** Personel Tanımlama - Yeni Kayıt ekranında personelin E-Posta adresinin tanımlandığı zorunlu alandır. Mail adresleri tanımlı olan personel için ilgili modüllerdeki akışların devamlılığını sağlayacak olan, gecikmelerden gelen maillerin gönderimleri sağlanır. Ayrıca maili tanımlı olan personellere atanan görevler mail olarak da kişiye iletilir.

**Cep Telefonu:** Personel Tanımlama - Yeni Kayıt ekranında personelin cep telefonu bilgisinin tanımlandığı alandır.

**Bağlı Olduğu Gruplar:** Personel Tanımlama - Yeni Kayıt ekranında personelin bağlı olduğu grupların ![ref45] (Ekle) butonu tıklanarak açılan sistemde tanımlı kullanıcı grubu listesinde seçim yapıldığı alandır. (Kullanıcı Grubu Listesı Sistem Altyapı Tanımları/BSAT/Tanımlar/Kullanıcı Grubu Tanımlama menüsünde tanımlı olarak gelmektedir.)“Bağlı Olduğu Gruplar” alanından personel ilgili olduğu kullanıcı gruplarına tanımlanabilir. Eğer bu alan boş bırakılırsa Kullanıcı Grubu Tanımlama menüsünden de kullanıcı gruplarına ilgili personeller atanabilir.

**Bağlı Kişiler:** Personel Tanımlama - Yeni Kayıt ekranında personelle bağlı kişileri varsa sistemin otomatik olarak  bu alanda görüntüler. Personele bağlı olan alt personeller varsa “Bağlı Kişiler” alanında tanımlı olarak gelmektedir. Bu alanda işlem yapılamaz. Bu personel başka personellere üst amir olarak atandıkça bu alan otomatik olarak sistem tarafından dolar.

**Kullanıcı Kilitli:** Personel Tanımlama - Yeni Kayıt ekranında ilgili alanla ilgili check box işaretlendiğinde kullanıcının şifresini yanlış girdiğinde Qdms giriş ekranın kilitlenme işlemi yapılır.

Sistem Altyapı tanımları parametrelerinden 106 numaralı “Personel şifresini üst üste kaç kez yanlış girdiğinde kullanıcı kilitlensin”  parametresine parametre değerine girile değere göre  personelin şifre bilgisinini kaç kez üst üste yanlış girdiğinde Qdms Giriş ekranın kilitlenmesi işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_323.png)

Parametrede parametre değerine göre kullanıcının 2 kez üst üste şifre bilgisinin yanlış girdiğinde Qdms giriş ekranın kilitlenme işlemi yapılır. 

Personel Tanımlama - Yeni Kayıt ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki  ![ref33]  butonuna tıklanarak Personel Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_324.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_325.png)

Personel Tanımlama ekranında 76 numaralı “Personel Tanımlamada Ek Alanlar Kullanılsın Mı?” parametresinin aktif edilerek gelen ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_326.png)  butonu görüntülenir. Bu buton tıklanarak Personel Tanımlama - Ek Bilgiler – Yeni Kayıt ekranı açılır. Ek Bilgiler sekmesinde tanımlı olan kişinin kişisel bilgileri girilir. Bu sekmede girilen bilgiler İş Başı ve Periyodik Muayene ve Eğitim Planlama modülünde kullanılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_327.png)

Önceki İşyerleri sekmesinde kişinin daha önce çalıştığı işyerlerinin bilgisi girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_328.png)**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_329.png):Yeni bir iş yeri tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_330.png):Listede seçili iş yeri bilgisi değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_331.png):Listede seçili iş yeri bilgisi silinir.

Bu alanlarda tanımlanan iş yerleri personellerin karşılaştıkları meslek hastalığı ilgili durumlarda kullanılmaktadır.Personel Tanımlama - Ek Bilgiler – Yeni Kayıt ekranında  personelin varsa önceki iş yerleri tanımlama işlemi yapılır. Ek Bilgiler alanında kişisel bilgileri girilir. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_332.png)  butonu tıklanarak kayıt işlemi yapılır.

Sistem ilk kuruluş aşamasındayken, firmada çalışan kullanıcı personeller “Personel Aktarım Şablonu” ile QDMS sistemine toplu olarak aktarılır. Bunun için QDMS Yetkilisi tarafından paylaşılan “Personel Aktarım Şablonu” nun formata uygun şekilde doldurulması ve Bimser Teknik Personeli ile paylaşılması gerekmektedir. 

Personel Aktarım Şablonu örneği aşağıda yer almaktadır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_333.png)

Personele ait olan sicil no, adı, soyadı, ünvan kodu, ünvan açıklaması (tanımı), departman kodu, departman adı, departman sorumlusunun pozisyon kodu veya sicil numarası, pozisyon kodu, pozisyon tanımı, üst pozisyon kodu (personelin bağlı olduğu ilk amirinin pozisyon kodu), işyeri kodu, işyeri adı, e-posta adresi doldurulur. Aktarım şablonundaki kırmızı ile işaretli başlıklar zorunlu alanlar olup, gri ile işaretli olan başlıklar zorunlu değildir. Active Directory Entegrasyonu sağlanacaksa, logon username kısmı doldurulur.

Not: Sicil No, Kod gibi tanımlarda herhangi bir boşluk veya Türkçe karakter kullanılmamalıdır.

Personel Tanımlama ekranında Filtre sekmesi ile Personelin Sicil no,  adı, soyadı, Departman, ,Unvan, İş Yeri ve Durum gibi alanlara veri girilip, ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_334.png) (Ara) butonu tıklanarak arama kriterlerine göre filtreleme yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_335.png)
#### **5.1.5. Pozisyon Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları /BSAT/Tanımlar/ Pozisyon Tanımlama

Firma içerisinde bulunan tüm pozisyonların tanımlandığı menüdür. Örnek pozisyonlar; bilgi işlem uzmanı, insan kaynakları müdürü,  üretim planlama mühendisi, finans şefi vb. Qdms sistemi  pozisyonlar üzerine kurulu bir sistemdir; personelin bağlı olduğu üst pozisyona göre tüm gecikmeler, bilgilendirmeler, görevler ilerler. Görevler kişiye değil, kişinin bağlı bulunduğu pozisyona göre atanır. Sistemin personel üzerinden değil de pozisyon üzerinden ilerlemesinin nedeni sistemleri kişiye değil pozisyona bağlayarak sistemin tıkanmasını engellemektir. Kişi işten ayrılsa bile, görevler yeni pozisyona aktarılarak sistemin yavaşlaması/ durması engellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_336.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref46]: Yeni bir pozisyon tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_338.png): Listede seçili olan pozisyon bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi güncellenemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_339.png): Seçili olan pozisyon bilgisi silinir. Pozisyon bilgisi herhangi bir kayıtta kullanılmamışsa silme işlemi yapılır, ancak ilgili pozisyon herhangi bir işlemde kullanıldıysa silinmesine sistem tarafından izin verilmez. Bunun yerine mevcut durumu pasif yapılarak kayıt edilir

![ref35]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Açılan Pozisyon Tanımlama ekranına yeni bir Pozisyon eklemek için ekranın sol üst köşesindeki ![ref46]  butonuna tıklanarak Pozisyon Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_340.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Pozisyon Kodu:** Pozisyon Tanımlama - Yeni Kayıt ekranında  Pozisyon kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Pozisyon Tanımı:** Pozisyon Tanımlama - Yeni Kayıt ekranında  Pozisyon tanım bilgisinin tanımlandığı zorunlu alandır. İlgili bayrakların bulunduğu alanlarda Pozisyon tanımın dil karşılıkları bilgisi yazılır. Örnek olarak; bilgi işlem uzmanı, insan kaynakları müdürü,  üretim planlama mühendisi, finans şefi

**Pozisyon Sahibi:** Pozisyon Tanımlama - Yeni Kayıt ekranında Pozisyon Sahibi bilgisinin ![ref47] (Seç) butonu tıklanarak açılan sistemde tanımlı personel listesinden seçildiği alandır. (Personel Listesi bilgisi Sistem Altyapı Tanımları/BSAT/Tanımlar/Personel Tanımlama menüsünde tanımlı olarak gelmektedir.)

**Durum:** Pozisyon Tanımlama - Yeni Kayıt ekranında Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar Pozisyonlar sistemde artık kullanılmadığına bir işarettir. Kullanılmayan Pozisyonları görmek için filtre sekmesinden arama kriterlerinde durum alanında  "Pasif" olarak arama yapılması yeterlidir.

Pozisyon Tanımlama - Yeni Kayıt ekranda pozisyon kodu, pozisyon tanımı yazılır. Pozisyon sorumlusu ![ref47] (Seç ) butonu tıklanarak açılan sistemde tanımlı olan personel listesinden seçilir. Durum bilgisi "Aktif" ve "Pasif" olarak ikiye ayrılmaktadır. Aktif olarak tanımlı pozisyonlar sistemde kullanılan pozisyonları ifade etmektedir. Eğer bir pozisyon tanımı sistemde artık kullanılmayacaksa,  durumu bilgisi “Pasif” olarak değiştirilmelidir. Böylece hem geçmişteki mevcut kayıtlar etkilenmez, hem de yeni pozisyon seçim ekranlarında pasife alınan pozisyon bilgisi görüntülenmez. Gerekli alanlar doldurulduktan sonra sol üst köşedeki  ![ref43]  butonuna tıklanarak Pozisyon Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_342.png)

Pozisyon Tanımlama ekranında Filtre sekmesi ile pozisyon sahibinin Adı, Soyadı, Pozisyon Kodu, Pozisyon Tanımı, Durum gibi alanlara veri girilip, ![ref35] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_343.png)
#### **5.1.6. İl Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları /BSAT/ Tanımlar/ İl Tanımlama

İl tanımlarının varsayılan olarak geldiği, yeni bir il tanımlamasının yapıldığı ve var olan il bilgisinin güncellendiği menüdür. Bu menü ile tanımlanan il bilgileri müşteri/ tedarikçi tanımlama ekranlarında kullanılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_344.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref48]: Yeni bir il tanımlanır.

![ref49]: Listede seçili olan il bilgisi için düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi güncellenemez.

![ref50]: Listede seçili olan il bilgisi silinir.

![ref35]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

İl Tanımlama ekranına yeni bir il eklemek için ekranın sol üst köşesindeki ![ref48] butonuna tıklanarak İl Tanımlama  ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_348.png)




**Açılan ekranda ilgili alanlar tanımlanır:**

**Ülke:** İl Tanımlama ekranında tanımlanacak ilin bulunduğu ülke bilgisinin açılır liste tıklanarak açılan Ülke listesinde seçildiği zorunlu alandır.(Ülke Listesi bilgisi Sistem Altyapı Tanımları/BSAT/Tanımlar/Ülke Tanımlama menüsünde tanımlı olarak gelmektedir.)

**İl Kodu:** İl Tanımlama ekranında  İl kodu bilgisi tanımlandığı zorunlu alandır. 

**İl Adı:** İl Tanımlama ekranında  il adının tanımlandığı zorunlu alandır.

İl Tanımlama  ekranda tanımlanacak ilin bulunduğu ülke bilgisi ülke listesinden seçilir. İl Kodu ve İl Adı bilgileri yazılır.Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref43] butonuna tıklanarak İl Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_349.png)

İl Tanımlama ekranında Filtre sekmesi ile İl Kodu ve İl Adı gibi alanlara veri girilip,  ![ref35] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_350.png)
#### **5.1.7. Ülke Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Ülke Tanımlama 

Ülke tanımlarının varsayılan olarak geldiği, yeni bir ülke tanımlamasının yapıldığı ve var olan ülke tanımının güncellenebildiği menüdür. Bu menü ile tanımlanan ülke bilgileri müşteri/ tedarikçi tanımlama ekranlarında kullanılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_351.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref48]: Yeni bir ülke tanımlanır.

![ref49]: Listede seçili olan ülke bilgisi için düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi güncellenemez.

![ref50]: Listede seçili olan ülke bilgisi silinir.

![ref35]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Ülke Tanımlama ekranına yeni bir ülke eklemek için ekranın sol üst köşesindeki ![ref48]  butonuna tıklanarak Ülke Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_352.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Ülke Kodu:** Ülke Tanımlama ekranında  Ülke kodu bilgisi tanımlandığı zorunlu alandır.

**Ülke Adı:** Ülke Tanımlama ekranında  Ülke adının tanımlandığı zorunlu alandır.

Ülke Tanımlama ekranda Ülke Kodu ve Ülke Adı bilgileri girilir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref43] butonuna tıklanarak Ülke Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_353.png)

Ülke Tanımlama ekranında Filtre sekmesi ile Ülke Kodu ve Ülke Adı gibi alanlara veri girilip,  ![ref35] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_354.png)

#### **5.1.8. Kullanıcı Grupları Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Kullanıcı Grupları Tanımlama

Sistemde kullanılacak kullanıcı gruplarının tanımlandığı menüdür. Kullanıcı grupları; menü yetkilendirme işlemlerinde, bilgilendirme alanlarını daha kolay ve etkin kullanabilmede, müdür/ uzman/ mühendis gibi eş değer yetkinliklere sahip personelleri gruplamakta, aynı işyerinde/ departmanda bulunan kullanıcıları gruplamakta, modül bazlı kullanıcı grupları tanımlamada ve akış tanımlamalarında kullanım kolaylığı sağlamaktadır. Bir kişi birden fazla gruba dahil edilebilir. Sistem ilk kurulumunda “Sistem Yöneticileri” ve “Standart Kullanıcılar” diye tanımlı kullanıcı grubu tanımlı olarak gelmektedir. Qdms yöneticileri “Sistem Yöneticileri” grubuna dahil edilirken, diğer tüm kullanıcılar “Standart Kullanıcı” grubuna dahil edilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_355.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref51]: Yeni bir kullanıcı grubu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_357.png): Listede seçili olan kullanıcı grubu bilgisi için düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi değiştirilemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_358.png): Listede seçili olan kullanıcı grubu bilgisi  silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_359.png): Listede seçili olan kullanıcı grubu bilgisi kopyalanarak çoğaltılır. Mevcut bir grubun içindeki kişiler, başka bir grup adı ile tekrar kullanılacak ise kopyalama butonuna ile grup kopyalama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_360.png): Çeşitli kategorilerde grup kuralları oluşturulur. (HR Entegrasyonu mevcutsa)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_361.png): Kullanıcı Grubu içerisindeki personel bilgileri Excel’e aktarılır.

![ref35]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Kullanıcı Grubu Tanımlama ekranına yeni bir Kullanıcı Grubu eklemek için ekranın sol üst köşesindeki ![ref51]  butonuna tıklanarak Kullanıcı Grubu Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_362.png)

**Kullanıcı Grup Kodu:** Kullanıcı Grubu Tanımlama - Yeni Kayıt ekranında kullanıcı grup kodu bilgisinin tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Sistem Altyapı Tanımları parametrelerinde 113 numaralı “Kullanıcı Grubu oto kod şablonu” parametresine tanımlanan kod şablonuna göre sistem otomatik olarak kod şablonu tanımlar. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_363.png)

113 numaralı parametrede kod şablonu tanımlama işleminden sonra 114 numaralı “Kullanıcı Grubu oto kod sayacı” parametresindeki sayac değerindeki değeri göre kod şablonu hangi değerden başlaması sağlanır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_364.png)

114 numaralı parametredeki sayac değeri “0” olduğunda 113 numaralı parametredeki kod şablonu sırasıyla tanımlanan kullanıcı grublarının kodlarını B.001,B.002, B.003 şeklinde otomartik olarak kod şablonu tanımlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_365.png)

**Açıklama:** Kullanıcı Grubu Tanımlama -Yeni Kayıt ekranında Kullanıcı Grubunun tanım bilgisinin tanımlandığı zorunlu alandır. İlgili bayrakların bulunduğı alanlarda açıklama alanın dil karşılıkları yazılır. Ör: Sistem Yöneticileri, Standart Kullanıcılar, Aksiyon Yönetimi Yöneticileri gibi

**İlişkili Modüller:** Kullanıcı Grubu Tanımlama -Yeni Kayıt ekranında kullanıcı grubunun ilişkili olduğu modüllerin açılır liste tıklanarak açılan sistemde tanımlı modül listesinde seçildiği alandır. ilişki modülller alanında kullanıcı grubu herhangi bir modülle ilişkilendirildiğinde o modülde ilgili alanlarda kullanıcı grubu ekleme işleminde listede yer alır. Tanımlanan kullanıcı grubu herhangi bir modüller ilişkilendirilemesi yapılmadığı zaman tüm modüllerin ilgili alanlarda kullanıcı grubu ekleme işleminde tüm listelerde gelmesi sağlanır.

**Grup Üyeler:** Kullanıcı Grubu Tanımlama -Yeni Kayıt ekranında  kullanıcı grubuna eklenecek grup üyeleri bilgisi ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_366.png)(Ekle) butonu tıklanarak açılan sistemde tanımlı personel listesinde veya ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_367.png)(Seç) butonu tıklanarak açılan sistemde tanımlı Kullanıcı Grubu listesinde seçim yapıldığı alandır. Bu alanda  ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_368.png) (Sil) butonu tıklanarak seçili personelin silinme veya ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_369.png)(Tümü Sil) butonu ile de eklenen tüm personellerin silinme işlemi yapılır.

**Tüm Personelleri Gruba Ekle:** Kullanıcı Grubu Tanımlama -Yeni Kayıt ekranında  ilgili alanla ilgili check box işaretlendiğinde kullanıcı grubuna tüm personellerin ekleme işlemi yapıldığı alandır.

**E-posta:** Kullanıcı Grubu Tanımlama -Yeni Kayıt ekranında   e-posta adresinin yazıldığı alandır.

Kullanıcı Grubu Tanımlama -Yeni Kayıt ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref52]  butonuna tıklanarak kullanıcı grubu tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_371.png)

Kullanıcı Grubu Tanımlama ekranında Kullanıcı Grubu seçili iken ![ref53] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_373.png)

Kullanıcı grubu tanımlama ekranında sağ üst köşedeki ![ref53] butonuna ile kullanıcı grubuna kural tanımlanabilir. Bu kural, HR Entegrasyonu olduğu durumlarda çalışır. Entegrasyon çalıştığı zamanlarda, bu ekranda oluşturulan kurallara göre personeller ilgili kullanıcı grubuna aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_374.png)

Örnekte olduğu gibi departman kodları D.001,D.002  olan departmanlarda bulunan personeller veya unvan kodu U.002  personellerin bu gruba otomatik olarak eklenmesi kuralı tanımlanmıştır. Sol üst köşedeki ![ref52]  butonuna tıklayarak Kullanıcı Grup Kuralı Oluştur kayıt işlem gerçekleştirilir. Personel entegrasyonu gerçekleştiği zamanlarda uygulanan grup kuralına göre personeller ilgili kullanıcı gruplarına aktarılmaktadır.

Açılan Kullanıcı Grubu Tanımlama - Kayıt Güncelle ekranında sistem tarafından “Bu grup için tanımlanmış bir kural bulunmaktadır, grup üyelerinde yapmış olduğunuz değişiklikler transfer programı çalıştığında iptal olacaktır.” mesajını  verir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_375.png)

Kuralın belirlendiği seçenekte eğer “Benzeyen” kullanıyor ise karşısına gelen kodun sonuna % işareti konulmalıdır. Örneğin 50000498-01, 50000498-02 gibi pozisyonlardan 50000498 benzeyenler kuralı koyulacaksa 50000498% şeklinde yazılmalıdır.

Eğer Tüm Kullanıcılar Grubuna sisteme dahil olan herkesin eklenmesi isteniyorsa bu durumda Kategori alanından Eşittir seçili olan ilgili alana 0 (sıfır) yazılıp kaydedilmelidir. 

Burada Operatör dediğimiz “ve – veya”  bağlacı çok önemlidir. Ve bağlacı kullanıldığında; kuralların hepsinin sağlanması durumunda kullanıcı grubuna personeller eklenir. Veya bağlacı kullanıldığında kuralların sadece birinin sağlanması durumunda kullanıcı grubuna personeller eklenir.

Kullanıcı Grubu  Tanımlama ekranında Filtre sekmesi ile Kullanıcı Grup Kodu, Açıklama,ve Departman  gibi alanlara veri girilip,  ![ref54] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_377.png)
#### **5.1.9. Yetki Grupları Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Yetki Grupları Tanımlama

Kullanıcıların QDMS üzerinde hangi menüleri göreceklerinin ayarlandığı menüdür. Kullanıcı gruplarına göre menü yetkilendirilmesi yapılmaktadır. Örneğin sistem yöneticileri kullanıcı grupları her menüyü görebilir şeklinde seçilirken, standart kullanıcılar için sadece Entegre Yönetim Sistemleri menüsünün altındaki hangi modülün hangi ekranını görebileceklerse o şekilde menüler seçilir. Aksiyon Yönetimi Yönetici  ekibinin Qdms üzerinde Aksiyon Yönetimi alt yapı kurgusunu da yapması isteniyorsa, Aksiyon Yönetimi Ekibi diye bir yetki grubu oluşturulup Sistem Altyapı tanımlarının altındaki Aksiyon Yönetim Modülüne ait tüm menüler ve Entegre Yönetim Sistemi menüsünün altındaki tüm Aksiyon Yönetimi menü yetkileri seçilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_378.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref55]: Yeni bir yetki grubu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_380.png): Listede seçili olan yetki grubu bilgisi için düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_381.png): Listede seçili olan yetki grubu bilgisi silinir.

![ref35]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Yetki Grubu Tanımlama ekranına yeni bir yetki grubu eklemek için ekranın sol üst köşesindeki ![ref55]  butonuna tıklanarak Yetki Grupları Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_382.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref56]:İlgili modülde seçilen menüleri ekleme işlemi yapılarak sağ tarafa menü görme yetkileri taşınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_384.png):Tüm menülerin ekleme işlemi yapılarak sağ tarafa menü görme yetkileri taşınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_385.png):İlgili modülde eklenen menü görme yetkisinin çıkarma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_386.png):Tüm menülerde menü görme yetkilerinin çıkarma işlemi yapılır.

Sistem Altyapı Tanımları (BSAT) kısmında açılan menüler Qdms sistemin Sistem Altyapı Tanımları  kısmındaki ilgili modüllerdeki menüleri kapsamaktadır.  Bu kısımda ilgili modüllerde menü yetkilendirme yapılacaksa seçim  işlemi yapılır.Entegre Yönetim Sistemi (QDMS)kısmında açılan menüler Qdms sistemin 	Entegre Yönetim Sistemi kısmındaki ilgili modüllerdeki menüleri kapsamaktadır.  Bu kısımda ilgili modüllerde menü yetkilendirme yapılacaksa seçim  işlemi yapılır.Başlıklarda parantez içinde  (ENS.COMMON) yazılan  Ensemble programın menüleri kapsamaktadır. Ensemble programı ile menü yetkilendirme işlemleri yapılacaksa bu başlıklar tıklanarak açılır listede menüler seçilerek ilgili butonlar tıklanarak yapılır.

Örn: Aksiyon Yönetimi modülünde Sistem Altyapı Tanımları ve Entegre Yönetimi Modülü ile ilgili menü görme yetkileri verileceği için ilgil modülde bu kısımlarda menüler işaretlenerek ![ref56]butonu tıklanılarak sadece Aksiyon Yönetimi Modülü ile menü görme yetkilerinin verilme işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_387.png)

Aksiyon Yönetimi modülün menü görme yetkileri  ile işlem adımlarından sonra ekranında sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_388.png)  butonu tıklanarak Yetki Grupları Tanımlama tanımalama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_389.png)
#### **5.1.10. Kullanıcı Yetkileri Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Kullanıcı Yetkileri Tanımlama

Kullanıcı grupları ile yetki gruplarının eşleştiği menüdür. Oluşturulan kullanıcı gruplarının, yetki grubu tanımlama menüsünde belirlenen yetkilerden hangisine sahip olmasını isteniyorsa, ilgili kullanıcı grubu ile yetki grubunun ilişkilendirmesi gerekir. Böylece toplu bir şekilde kullanıcılar için menü görme yetkilendirilmesi yapılmış olur. Qdms sisteminde kullanıcıları menü görme yetkisi verme işlemi üç aşamada olmaktadır. 

- İlk aşamada  menü görme yetkisi verilecek kullanıcılar için bir kullanıcı Grubu tanımlama işlemi yapılır. Bu tanımlanan kullanıcı grubuna menü yetkisi verilecek kullanıcılar sistemde tanımlı personel listesinde eklenir.Örn: Aksiyon Yönetimi Ekibi Kullanıcı Grubu
- İkinci aşamada kullanıcıları hangi menüleri görebileceğin menülerin seçildiği basamaktır.  Bu basamakta Yetki  Grubu tanımlama menüsünde yapılan aşamadır.Örn.;Aksiyon Yönetimi Ekibi. (Aksiyon Yönetimi modülünde Sistem Altyapı Tanımları ve Entegre Yönetim Sistemi menüleriden yetki verilme işlemi yapılmıştır. ) 
- Üçüncü basamakta Kullanıcı Yetkileri Tanımlama menüsünde tanımlanan kullanıcı grubu ve Yetki Grubu Tanımlama menülerin eşleştirilmesi işlemidir.

**Not:** Modüller içerisinde ve  parametrelere bağlı olarak yetkilendirme işlemleride Qdms sisteminde  olabilir. Örneğin: Doküman Yönetiminde yetki matrisinde yetkilendirme işlemi,  parametrelerde ilgili modülde iş yeri bazlı güvenlik gibi.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_390.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref57]: Yeni bir kullanıcı yetki tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_392.png): Listede seçili olan kullanıcı yetki eşleştirmesi silinir.

  ![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Kullanıcı Yetki Tanımlama ekranında yeni bir kullanıcı yetki eşleştirmesi yapmak için ekranın sol üst köşesindeki ![ref57] butonuna tıklanarak Kullanıcı Yetki Tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_393.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kullanıcı Grubu:** Kullanıcı Yetki Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_394.png) (Seç) butonu tıklanarak açılan sistemde tanımlı Kullanıcı Grubu listesinden Kullanıcı Grubu  seçim işlemi yapılan zorunlu alandır.

**Yetki Grubu:** Kullanıcı Yetki Tanımlama ekranında açılır liste tıklanarak açılan  Yetki Grubu listesinde Yetki Grubu seçim işlemleri yapılan alandır.

Açılan Kullanıcı Yetki Tanımlama ekranında kullanıcı grupları ve yetki grupları eşleştirilerek hangi kullanıcı grubunun hangi yetkiye sahip olacağı belirlenir. Gerekli alanlar seçildikten sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_395.png)  butonuna tıklanarak Kullanıcı Yetki Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_396.png)

Kullanıcı Yetkileri Tanımlama işleminden sonra ilgili kullanıcı grubuna ait personellerin menü görme yetkisi verildiğini görmek için kullanıcı grubuna ait personellenin Qdms ana  giriş ekranında  Qdms adresine giriş yapmak için kullanıcı adı ve parola bilgisi ile giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_397.png)

Kullanıcı Grubuna ait personelin Qdms adresine giriş yapıldığında Aksiyon Yönetimi Modülü ile sadece  Sistem Atyapı Tanımları ve Entegre Yönetim Sistemi kısmındaki menülerde menü görme yetkisi verildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_398.png)
#### **5.1.11. Tedarikçi Grupları**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Tedarikçi Grupları

Tedarikçi Tanımlama ekranında oluşturulan tedarikçilerin yapılan işe göre sınıflandırıldığı menüdür. Tanımlanan Tedarikçi Grupları, Tedarikçi Tanımlama ekranı ile eşleştirilerek hangi tedarikçinin hangi tedarikçi grubunda olduğu belirlenir. Bu veriler Tedarikçi Değerlendirme Modülünde tedarikçilerin grup bazında değerlendirilmesi amacıyla kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_399.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref58]: Yeni bir tedarikçi grubu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_401.png): Listede seçili olan tedarikçi grubu bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_402.png): Listede seçili olan tedarikçi grubu bilgisi silinir.

![ref35]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Tedarikçi Grupları Tanımlama ekranına yeni bir tedarikçi grubu eklemek için ekranın sol üst köşesindeki ![ref58]  butonuna tıklanarak Tedarikçi Grupları Tanımlama/ Yeni Kayıt ekranı açılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_403.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tedarikçi Grupları Tanımlama - Yeni Kayıt ekranında Tedarikçi Grubunun tanım bilgisinin tanımlandığı zorunlu alandır. İlgili bayraklarda tanımlanan Tedarikçi Grubunun tanım kısmının dil karşılıkları bilgisi yazılır.

Açılan Tedarikçi Grupları Tanımlama - Yeni Kayıt ekranda Tedarikçi Grupları tanım bilgisi girilir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_404.png)  butonuna tıklanarak Tedarikçi Grupları Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_405.png)

Tedarikçi Grupları tanımlama ekranında Filtre sekmesinde arama kriterleri olan Grup ID ve Tanım gibi alanlara veri girilip , ![ref35] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_406.png)
#### **5.1.12. Müşteri-Tedarikçi Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Müşteri-Tedarikçi Tanımlama

Firmanın çalıştığı müşterilerin ve tedarikçilerin sisteme tanımlandığı menüdür. Bu tanımlar Düzeltici Faaliyetler, Aksiyon, Müşteri Şikayetleri ve Tedarikçi Değerlendirme gibi modüllerde kullanılır. Müşteri/ Tedarikçi Tanımlama işlemi aşağıdaki maddelerde olduğu gibi 3 şekilde kullanılarak sisteme aktarım işlemi gerçekleştirilebilir. 

- Manuel Tanımlama (Müşteri -Tedarikçi Tanımlama menüsünde yapılır.)
- Toplu Aktarım (Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Müşteri-Tedarikçi Aktarma menüsünde)
- Entegrasyon Yöntemleri(Bimser Teknik Destek Ekibinde Yardım alınarak yapılır.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_407.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref59]: Yeni bir müşteri-tedarikçi bilgisi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_409.png): Listede seçili olan Müşteri-Tedarikçi bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_410.png): Listede seçili olan Müşteri-Tedarikçi bilgisi silinir.

![ref35]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Müşteri-Tedarikçi tanımlama ekranına manuel olarak yeni bir Müşteri-Tedarikçi eklemek için ekranın sol üst köşesindeki ![ref59]  butonuna tıklanarak Müşteri-Tedarikçi Tanımlama/Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_411.png)

**Şirket Kodu:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında Müşteri - Tedarikçi kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’. Kod alanı Tür alanında Bireysel türü seçildiğinde parametrelerde yapılan ayarlamalara göre otomatik olarak kod şablonu tanımlama ve sayac değerine göre otomatik olarak sistem ayarlama işlemi yapar. Müşteri -Tedarikçinin Bireysel olarak türünün seçilmesine bağlı olarak Sistem Altyapı Tanımları modülü parametrelerinde 33 numaralı “Bireysel müşteri tanımlama otomatik kod şablonu” şablonu tanımlanır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_412.png)  Bireysel Müşteri Türüne göre parametre tanımlanan kod şablonun sayac değerinin kaçtan  başlayacağı 34 numaralı “Bireysel Müşteri tanımlama otomatik kod şablon sayacı” parametresindeki parametre değerindeki sayac değerine göre sistem tarafından otomatik olarak kodun verilmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_413.png)

33 numaralı parametreye göre Bireysel Kod şablonu “BM\_###” ve 34 numaralı parametredeki sayac değeri “0” göre  BM\_001, BM\_002, BM\_003 olarak sırasıylama kod tanımlaması  bireysel müşteri türü için yapılacaktır.Sistem kod alanında bu tanımlamadan sonra kod tanımlamasına izin vermez ve otomatik olarak bireysel müşteriler için kod tanımlaması yapar.

**Ad:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında Müşteri - Tedarikçi tanım bilgisinin tanımlandığı zorunlu alandır.İlgili bayrakların bulunduğu kısımda Müşteri-Tedarikçi tanım bilgisinin dil karşılığı yazılır.

**Tür:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında tür kısmında açılır Tür listesinde Müşteri – Tedarikçinin türünün seçildiği alandır. Kurumsal, Bireysel ve Tedarikçi tür seçeneklerinde seçim yapılır. Bu kısım parametreye bağlı olarak gelmektedir. Sistem Altyapı Tanımları modülü parametrelerinde 32 numaralı “Bireysel müşteri tanımlama seçili gelecek tür: Kurumsal(K),Tedarikçi(T),Bireysel(B)” parametresinde parametreye değerinde  tanımlı tür seçeneklerin baş harflerine göre seçenek olarak gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_414.png)

Bu parametrede Kurumsal tür için parametre değerine “K” , Tedarikçi türü için parametre değerine “T” ve Bireysel Tür içinde parametre değerine “B” değeri yazılır.  Tür alanında Müşteri -Tedarikçi için bütün tür seçenekleri için parametreye müşteri -Tedarikçi türlerin parametreye baş harfleri yazılarak tür alanında tüm seçeneklerin görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_415.png)

**Durum:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar Müşteri - Tedarikçi bilgisi sistemde artık kullanılmadığına bir işarettir. Kullanılmayan Müşteri – Tedarikçi bilgisini   görmek için filtre sekmesinden arama kriterlerinde durum alanında  "Pasif" olarak arama yapılması yeterlidir.

**İş Yeri Kodu:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında  ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_416.png) (Seç) butonu tıklanarak açılan sistemde tanımlı iş yeri listesinde Müşteri – Tedarikçinin  iş yeri bilgisinin seçildiği alandır.

**Adres:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında  Müşteri – Tedarikçinin   adres bilgisinin tanımlandığı alandır.

**Şehir:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında  Müşteri – Tedarikçinin  şehir  bilgisinin  açılan açılır şehir listesinde seçildiği alandır.

**Ülke:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında  Müşteri – Tedarikçinin  ülke  bilgisinin  açılan açılır ülke listesinde seçildiği alandır.

**Telefon:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında  Müşteri – Tedarikçinin  telefon  bilgisinin  tanımlandığı alandır.

**Cep Telefonu:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında  Müşteri – Tedarikçinin  Cep telefon  bilgisinin  tanımlandığı alandır.

**Fax:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında  Müşteri – Tedarikçinin  Fax bilgisinin  tanımlandığı alandır.

**Sorumlu:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında  Müşteri – Tedarikçinin  sorumlu bilgisinin  tanımlandığı alandır.

**E-posta:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında  Müşteri – Tedarikçinin  E-Posta bilgisinin  tanımlandığı alandır.

**Dil:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında  Müşteri – Tedarikçinin  Dil bilgisinin  açılan açılır dil listesinde seçildiği alandır.

**Açıklama:** Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında  Müşteri – Tedarikçinin  varsa açıklama bilgisi girildiği alandır.Müşteri -Tedarikçi Tanımlama ekranında Açıklama alanı zorunlu yapılması istendiğinde Sistem Altyapı Tanımları Modülü parametrelerinde 35 numaralı “Bireysel müşteri tanımlama açıklama alanı zorunlu olsun mu? (E/H)” parametresi seçilerek parametre değeri “Evet” seçilerek parametre aktif edilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_417.png)

Parametre aktif edildiğinde Müşteri -Tedarikçi Tanımlama -Yeni Kayıt ekranında Tür alanında Bireysel Müşteri seçilerek tanımlama işlemi yapıldığında Açıklama alanın zorunlu alan olarak girilmesi sağlanır.

Müşteri - Tedarikçi Tanımlama - Yeni Kayıt ekranında   şirket kodu, adı, türü (bireysel müşteri, kurumsal müşteri, tedarikçi), e-posta adresi vb. iletişim bilgileri tanımlanır. Eğer ilgili modüllerde açılan kayıtla ilgili Müşteriye/ Tedarikçiye bilgi maili gitmesi isteniliyorsa mail tanımlamaları yapılmalıdır. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_418.png)  butonuna tıklanarak Müşteri-Tedarikçi Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_419.png)

Müşteri -Tedarikçi Tanımlaama  ekranında Filtre sekmesi ile Şirket Kodu, Ad ve Tür gibi alanlara veri girilip,  ![ref54] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_420.png)

#### **5.1.13. Ürün Tipi Tanımlama**
**Menü Adı**: Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Ürün Tipi Tanımlama

Ürün tiplerinin tanımlamasının yapıldığı menüdür. Ürünlerin sınıflandırılması için, filtreleme ile aramada kolaylık sağlanması açısından, ürünlerin tiplerinin tanımlanmasında fayda vardır. Ürünlerin sınıflandırılması kapsamında ürün tipi oluşturulur, örneğin mamul, bitmiş ürün, yazılım ürünleri, donanım ürünleri gibi.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_421.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref60]: Yeni bir ürün tipi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_423.png): Listede seçili olan ürün tipi bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi değiştirilemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_424.png): Listede seçili olan ürün tipi bilgisi silinir.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Ürün Tipi Tanımlama ekranında yeni bir ürün tipi eklemek için ekranın sol üst köşesindeki ![ref60] butonuna tıklanarak Ürün Tipi Tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_425.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Ürün Tipi Kodu:** Ürün Tipi Tanımlama -Yeni Kayıt ekranında tanımlanan kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Ürün Tipi Tanımı:** Ürün Tipi Tanımlama -Yeni Kayıt ekranında Ürün Tipi tanım bilgisinin tanımlandığı zorunlu alandır. 

Ürün Tipi Tanımlama -Yeni Kayıt ekranda Ürün Tipi Kodu ve Ürün Tipi Tanımı bilgisi girilir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref61]  butonuna tıklanarak Ürün Tipi Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_427.png)
#### **5.1.14. Ürün Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Tanımlar/ Ürün Tanımlama

Ürün tanımlamalarının yapıldığı menüdür. Diğer modüllerde ürünler ile ilgili işlemler yapılması kapsamında kullanılmaktadır. Ürün Tanımlama işlemi aşağıdaki maddelerde olduğu gibi 3 şekilde kullanılarak sisteme aktarım işlemi gerçekleştirilebilir.  

- Manuel tanımlama (Ürün Tanımlama menüsünde yapılır.)
- Toplu aktarım (Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Ürün Aktarma menüsünde yapılır)
- Entegrasyon yöntemleri (Bimser Teknik Destek Ekibinde yardım alınarak yapılır.) 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_428.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref62]: Yeni bir ürün tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_430.png): Listede seçili olan ürün bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi değiştirilemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_431.png): Listede seçili olan ürün bilgisi silinir.

![ref35]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

Ürün Tanımlama ekranına manuel olarak yeni bir ürün eklemek için ekranın sol üst köşesindeki ![ref62]  butonuna tıklanarak Ürün Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_432.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Ürün Grup Kodu:** Ürün Tanımlama ekranında sistemde tanımlı olan bir Ürün altına o ürüne bağlı olan yeni bir ürün tanımlanmak isteniyorsa ![ref63] (Seç) butonu tıklanarak açılan sistemde tanımlı ürün listesinden seçim yapıldığı alandır.		

**Ürün Kodu:** Ürün Tanımlama ekranında Ürün kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Ürün Adı:** Ürün Tanımlama ekranında Ürün adı bilgisinin tanımlandığı zorunlu alandır	

**Ürün Tipi:** Ürün  Tanımlama ekranında Ürün Tipi  bilgisinin açılır liste tıklanarak açılan Ürün Tipi listesinde seçildiği alandır.( Ürün Tipi listesi Sistem Altyapı Tanımları/BSAT/Tanımları/Ürün Tipi listesinde tanımlı gelmektedir.)	 	

**Durum:** Ürün Tanımlama  ekranında Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar Ürünler sistemde artık kullanılmadığına bir işarettir. Kullanılmayan ürünleri görmek için filtre sekmesinden arama kriterlerinde durum alanında  "Pasif"seçeneği seçilerek arama yapılması gerekir.	 	

**Ürün Grup Sorumlusu:** Ürün Tanımlama ekranında ürün grup sorumlusunun ![ref63] (Seç) butonu tıklanarak açılan sistemde tanımlı Personel listesinden seçildiği alandır. Ürün grup sorumları ilgili modüllerde ürünle ilişkilendirilme işlemi yapıldığında parametresel ayarlama yapıldığında  bilgilendirme alanlarında kullanılmaktadır.		

**İlgili İş Yeri:** Ürün Tanımlama  ekranında ürünün ilgili olduğu işyeri bilgisinin ![ref63] (Ekle) butonu tıklanarak açılan sistemde tanımlı İşyeri listesinden seçildiği alandır.

Ürün Tanımla ekranda varsa Ürün Grup Kodu sistemde tanımlı olan ürün listesinden seçilir. Ürün Kodu ve Ürün Tanımı yazılır.  Ürün Tipi bilgisi sistemde kayıtlı ürün tiplerinden seçilir. Durum bilgisi “Aktif” seçilir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref61]  butonuna tıklanarak Ürün Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_434.png)

Ürün Tanımlama ekranında Filtre sekmesinde Ürün Kodu, Ürün Adı ve Ürün Tipi gibi arama kriterleri olan alanlara veri girilip, ![ref35] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_435.png)
#### **5.1.15. Mesaj Gövdesi Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Tanımlar/ Mesaj Gövdesi Tanımlama

Modüllerde yapılan işlemler sonrası gidecek olan maillerin içeriklerinin tanımlandığı menüdür. Sistemde mesaj gövdeleri tanımlıdır, gerekli durumlarda mail içeriklerinde güncelleme yapılır veya yeni mesaj gövdeleri tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_436.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref64]: Yeni bir mesaj gövdesi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_438.png): Listede seçili olan mesaj gövdesi bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_439.png): Listede seçili olan mesaj gövdesi bilgisi silinir.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref66]: Veriler Excel’ e aktarılır.

![ref67]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref68]: Menü ekranın tekrar varsayılan ayarlarına gelmesi işlemi yapılır.

![ref69]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Mesaj Gövdesi Tanımlama ekranına yeni bir mesaj gövdesi eklemek için ekranın sol üst köşesindeki ![ref64] butonuna tıklanarak Mesaj Gövdesi Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_445.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Modüller:** Mesaj Gövdesi Tanımlama - Yeni Kayıt ekranında Modüller alanında açılır liste tıklanarak açılan  Modül listesinde mesaj gövdesinin ilgili olduğu modülün seçildiği alandır.

**Mesaj Kodu:** Mesaj Gövdesi Tanımlama - Yeni Kayıt ekranında Mesaj Gövdesi kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. MSG.1.221, MSG.1.222 gibi

**Mesaj Konu:** Mesaj Gövdesi Tanımlama - Yeni Kayıt ekranında Mesaj Gövdesi tanım bilgisinin tanımlandığı zorunlu alandır

**Mesaj Gövdesi:** Mesaj Gövdesi Tanımlama - Yeni Kayıt ekranında Mesaj Gövdesi bilgisinin tanımlandığı alandır.İlgili bayrakların butlunduğu kısımlarda Mesaj gövdesinin dil karşılığı yazılır.

**SMS İçeriği:** Mesaj Gövdesi Tanımlama - Yeni Kayıt ekranında SMS içeriği bilgisinin tanımlandığı alandır.

Mesaj Gövdesi Tanımlama - Yeni Kayıt ekranda ilgili modül seçilir. Mesaj Kodu ve Mesaj Konusu yazılır. Mesaj gövdesi tanımlanır. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_446.png)  butonuna tıklanarak Mesaj Gövdesi tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_447.png)

Mesaj Gövdesi Tanımlama ekranında Filtre sekmesinde Modüller, Mesaj Kodu ve Mesaj Konu gibi arama kriterlerinden olan alanlara veri girip, ![ref65] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.	

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_448.png)
#### **5.1.16. İş Yeri Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Tanımlar/İş Yeri Tanımlama

Sistemde tanımlı olan personellerin işyerlerinin tanımlandığı menüdür. İşyeri bilgisi personel tanımlama ekranında kullanıldığı gibi modüllerde yapılan işlemin hangi işyerinde yapıldığını belirlemek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_449.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref70]: Yeni bir iş yeri tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_451.png): Listede seçili olan iş yeri bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_452.png): Listede seçili olan iş yeri bilgisi silinir

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref66]: Veriler Excel’ e aktarılır.

İş Yeri Tanımlama ekranına yeni bir iş yeri eklemek için ekranın sol üst köşesindeki ![ref70]  butonuna tıklanarak İş Yeri Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_453.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Üst İş Yeri:** İş Yeri Tanımlama - Yeni Kayıt ekranında sistemde tanımlı olan bir İş Yerinin altına o İş Yeri  bağlı olan yeni bir İş Yeri  tanımlanmak isteniyorsa  yani  alt kırılım oluşturulmak isteniyorsa ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_454.png) (Seç) butonu tıklanarak açılan sistemde tanımlı İş Yeri listesinden seçim işlemi yapılan alandır.

**İş Yeri Kodu:** İş Yeri Tanımlama - Yeni Kayıt ekranında İş Yeri   kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’	   

**İş Yeri Adı:** İş Yeri Tanımlama - Yeni Kayıt ekranında İş Yeri  tanım bilgisinin tanımlandığı zorunlu alandır   	

**Meslek Grubu:** İş Yeri Tanımlama - Yeni Kayıt ekranında Meslek Grubu bilgisinin ![ref71] (Seç) butonu tıklanarak açılan sistemde tanımlı Meslek Grubu  listesinden seçim işlemi yapılan alandır.	 (Meslek Grubu listesi Sistem Altyapı Tanımlar/BSAT/Tanımlar/Meslek Grubu Tanımlama menüsüden tanımlı olarak gelmektedir. )		

**Sorumlusu:** İş Yeri Tanımlama - Yeni Kayıt ekranında İş Yeri Sorumlusunun bilgisinin ![ref71] (Seç) butonu tıklanarak açılan sistemde tanımlı Personel  listesinden seçim işlemi yapılan alandır.   	   			

**SGK No:** İş Yeri Tanımlama - Yeni Kayıt ekranında İş Yerinin SGK No bilgisinini girildiği alandır.

**Tehlike Sınıfı:** İş Yeri Tanımlama - Yeni Kayıt ekranında İş Yerinin Tehlike Sınıfı bilgisinin açılır liste tıklanarak açılan Tehlike Sınıfı listesinden seçildiği alandır.  (Tehlike Sınıfı listesi Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Sabitler menüsünde tanımlı olarak gelmektedir. )	

**Durum:** İş Yeri Tanımlama - Yeni Kayıt ekranında Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar İş Yerleri sistemde artık kullanılmadığına bir işarettir. Kullanılmayan İş Yerlerini  görmek için filtre sekmesinden arama kriterlerinde durum alanında  "Pasif" olarak arama yapılması yeterlidir.	   	   	   

**İşyeri haritası:** İş Yeri Tanımlama - Yeni Kayıt ekranında iş yeri haritasının ![ref71] (Ekle) butonu tıklanarak ekleme işlemi yapılacak alandır. Bu alan Sistem Altyapı Tanımları/BSAT/Dil Ayarları/Konfigürasyon Ayarları/ Dil Ayarları menüsünde Modülller alanından Modül olarak Sistem Altyapı Tanımları modülü seçilerek , Dil Tanımların görüntülenir. Bu Dil Tanımlarında Başlıklar sekmesinde Adı alanına “lblIsyeriHarita” label kodu bilgisi  seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_456.png)

Label kod bilgisi seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_457.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_458.png)

Açılan Dil Ayarların ekranında Değeri  kısmında alanın tanım kısmı yazılır, varsa dil karşılığı bilgisi ve alanın zorunlu olup, olmayacağı bilgileri ayarlanarak gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref61]  butonu tıklanarak  dil ayarları kayıt işlemi yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_459.png)

Tanımlama işlemi yapılan alan İş Yeri Tanımlama ekranında görüntülenir.  Yüklenici İş İzni Takibi Modülünde  Yüklenici İş İzni Talep Formu İşlemleri  tanımlama ekranından Talebi Yapan Tipi “İş Yeri” seçildiğinde  Çalışma Yapılacak Harita alanında bu alanda eklenen Harita görüntülenir ve çalışma yapılan alanların işaretlenme işlemi yapılır.

İş Yeri Tanımlama - Yeni Kayıt ekranda İş Yeri Adı ve İş Yeri Kodu bilgisi girilir. Varsa Üst İş Yeri bilgisi sistemde tanımlı İş Yeri Seç Listesinden seçilir. Meslek Grubu sistemde tanımlı Meslek Grubu Seç ve Sorumlu bilgisi sistemde tanımlı Personel Listelerinden seçilir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref72]  butonuna tıklanarak İş Yeri Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_461.png)

İş Yeri Tanımlama ekranında Filtre sekmesinde İşyeri Kodu, İş yeri Adı, Sorumlusu ve Durum alanlarına veri girilip,  ![ref65] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_462.png)

#### **5.1.17. Şirket Profili Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Şirket Profili Tanımlama

Şirketin lokasyon bilgilerinin tanımlama işleminin gerçekleştiği menüdür. Cihaz Yönetim Sistemi, Saha Tespit Yönetimi Modüllerinde kullanılır. Cihaz Yönetim modülü kapsamında kalibrasyon yapılacak cihazların firmada bulunduğu yerlerin tanımlamasında kullanılır. Saha Tespit Yönetimi kapsamında ise denetim yapılacak sahaların tanımlamasında kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_463.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref73]: Yeni bir şirket profili tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_465.png): Listede seçili olan şirket profili bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi değiştirilemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_466.png): Listede seçili olan şirket profili bilgisi silinir.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref66]: Veriler Excel’ e aktarılır.

Şirket Profili Tanımlama ekranına yeni bir şirket profili eklemek için ekranın sol üst köşesindeki ![ref73] butonuna tıklanarak Şirket Profili Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_467.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Ana Ünite:** Şirket Profili Tanımlama - Yeni Kayıt ekranı sistemde tanımlı olan bir Şirket Profili altına Şirket Profili bağlı olan yeni bir Şirket Profili tanımlanmak isteniyorsa alt kırılım oluşturulmak  isteniyorsa ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_468.png) (Seç) butonu tıklanarak açılan sistemde tanımlı Şirket Profili listesinden Şirket Profili seçim işlemi yapılan alandır.	

**Birim Kodu:** Şirket Profili Tanımlama - Yeni Kayıt ekranı ekranında tanımlanan şirket profilinin kod bilgisinin tanımlandığı alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’   

**Birim Adı:** Şirket Profili Tanımlama - Yeni Kayıt ekranı  Şirket Profili  tanım bilgisinin tanımlandığı zorunlu alandır.  	

**Birim Sorumlusu:** Şirket Profili Tanımlama - Yeni Kayıt ekranı ![ref74] (Seç) butonu tıklanarak açılan sistemde tanımlı Personel listesinden şirket profilinin  sorumlusunun  seçim işlemi yapılan alandır.

**Şirket Profili Sorumlu Kullanıcı Grubu:** Şirket Profili Tanımlama - Yeni Kayıt ekranı Şirket Profili Sorumlu Kullanıcı Grubu ![ref74] (Ekle) butonu tıklanarak açılan Kullanıcı Grubu listesinde seçim yapılan alandır.Modüllerde bu alana bağlı olarak işlemler üzerinde yetkilendirme yapılır. 

**Durum:** Şirket Profili Tanımlama - Yeni Kayıt ekranı Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar Şirket Profili bilgisi sistemde artık kullanılmadığına bir işarettir. Kullanılmayan Şirket Profil bilgileri görmek için filtre sekmesinden arama kriterlerinde durum alanında  "Pasif"  seçeneği seçilerek arama  yapılması gerekmektedir.

Şirket Profili Tanımlama - Yeni Kayıt ekranda şirket profili tanımlamada varsa bir üst kod bilgisi sistemde kayıtlı Şirket Profili listesinden seçilir. Birim kodu ve birim adı tanımı yazılır. Birim sorumlusu sistemde tanımlı olan Personel  listesinden seçilir. Şirket Profili Sorumlu Kullanıcı grubu sistemde tanımlı Kullanıcı Grubu  listesinden seçilir. Durum bilgisi "Aktif" seçilir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_470.png)butonuna tıklanarak Şirket Profili Tanımlama kayıt işlemi gerçekleştirilir.

Şirket Profili Tanımlama ekranında Filtre sekmesinde Ana Ünite, Birim Kodu gibi  arama kriterleri olan alanlara veri girilip , ![ref65] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_471.png)
#### **5.1.18. Para Birimleri Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Tanımlar/Para Birimleri Tanımlama

Para birimleri tanımlama işleminin gerçekleştiği menüdür. Para birimleri varsayılan olarak ekrana gelmektedir. Para birimleri sistemde Düzeltici Faaliyetler, Aksiyon Yönetimi Müşteri Şikayetleri(İç ve Dış Müşteri Şikayetleri), Cihaz Yönetimi Sistemi, gibi modüllerde kullanılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_472.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref75]: Yeni bir para birimi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_474.png): Listede seçili olan para birimi bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_475.png): Listede seçili olan para birimi bilgisi silinir.

![ref66]: Veriler Excel’ e aktarılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Para Birimi Tanımlama ekranına yeni bir para birimi eklemek için ekranın sol üst köşesindeki ![ref75]  butonuna tıklanarak Para Birimleri Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_476.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Para Birimi:** Para Birimi Tanımlama ekranında tanımlanan para biriminin adı bilgisinin yazıldığı alandır.	      	

**Kur Çarpanı:**	Para Birimi Tanımlama ekranında tanımlanan para birimin kur çarpanı bilgisinin yazıldığı alandır.      	

**Varsayılan:** Para Birimi Tanımlama ekranında ilgili check box işaretlendiğinde tanım bilgisinin sistem tarafından otomatik olarak alana gelmesinin sağlandığı alandır.

Para Birimi Tanımlama ekranında para biriminin tanımı, kur çarpanı bilgisi, istenirse tanım bilgisinin sistem tarafından otomatik olarak alana gelmesi için ilgili check box işaretlenmesi gibi gerekli alanlarla ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref76] butonu tıklanarak para birimi kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_478.png) Para Birimi Tanımlama Filtre sekmesinde Id, Para Birimi gibi alanlara veri girilip, ![ref65] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_479.png)
#### **5.1.19. Süreç Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Süreç Tanımlama

Firmanın süreçlerinin tanımlandığı menüdür. Tanımlanan süreçleri birçok modül ile ilişkilendirilme işlemi yapılmaktadır. Doküman Yönetimi, Düzeltici faaliyetler, denetim, risk modülleri, olay modülü gibi birçok modül ile sistemde tanımlı süreçlerle ilişki kurulabilir. Süreç tanımlama işlemi manuel ya da Ensemble programında görsel model ekranında çizilerek süreç detay kısmında ilgili alanlar ilgili bilgiler girilerek gerçekleştirilir. Firma tarafından Ensemble Süreç Yönetimi programı kullanıyorsa  ise süreç tanımlamaları Ensemble Süreç Yönetim Programı ile çizilir ve Qdms  sistemine bu menüye  listesi aktarılır. Ensemble programı  olmadığı durumlarda süreçler manuel olarak tanımlanabilmektedir. Bu menüde manuel tanımlamada çizim yapmadan sadece sürecin kodu, ismi ve sürecin sahibi tanımlamaları yapılıp kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_480.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref66]: Veriler Excel’ e aktarılır.

Süreç Tanımlama ekranında ![ref66] (Excel Aktar) butonu tıklanarak Süreç listesinin Excel formatında raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_481.png)
#### **5.1.20. Ölçü Birimleri**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Ölçü Birimleri 

Ölçü birimleri tanımlama işleminin gerçekleştirildiği menüdür. Adet, kilogram, litre, metre gibi ölçü birimleri bir kısmı sistemde tanımlı olarak gelmektedir. Ölçü birimleri sistemde Düzeltici Faaliyetler, Denetim Faaliyeti, Müşteri Şikayetleri(İç ve Dış Müşteri Şikayetleri), Cihaz Yönetimi Sistemi , Risk modülleri (İSG Risk Değerlendirme, Kurumsal Risk Değerlendirme gibi) gibi modüllerde kullanılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_482.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref77]: Yeni bir ölçü birimi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_484.png): Listede seçili olan ölçü birimi bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_485.png): Listede seçili olan ölçü birimi bilgisi silinir.

![ref66]: Veriler Excel’ e aktarılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Ölçü Birimi Tanımlama ekranına yeni bir ölçü birimi eklemek için ekranın sol üst köşesindeki ![ref77] butonuna tıklanarak Ölçü Birimi Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_486.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Ölçü Birimi Adı:** Para Birimi Tanımlama ekranında tanımlanan ölçü biriminin adı bilgisinin yazıldığı alandır.	      	      	

**Varsayılan:** Ölçü Birimi Tanımlama ekranında ilgili check box işaretlendiğinde tanımlanan ölçü birimi alana sistem tarafından otomatik olarak tanımın  gelmesinin sağlandığı alandır.

Açılan Ölçü Birimi Tanımlama - Yeni Kayıt ekranda Ölçü Birimi Adı bilgisi girilir.  Ölçü birimi tanımlanırken varsayılan olarak işaretlenirse, modüllerde işlem yapılırken varsayılan seçilen ölçü biriminin ekrana otomatik olarak sistem tarafından gelmesi sağlanır. Gerekli alanlar ilgili bilgiler doldurulduktan sonra sol üst köşedeki ![ref76]  butonuna tıklanarak Ölçü Birimi Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_487.png)

Ölçü Birimi Tanımlama ekranında Filtre sekmesinde Ölçü Id, Ölçü Birimi Adı gibi alanlara veri girilip, ![ref65] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_488.png)
#### **5.1.21. Yönetim Sistemleri**
**Menü Adı**: Sistem Altyapı Tanımları/BSAT/Tanımlar/ Yönetim Sistemleri

Yönetim Sistemlerinin tanımlandığı menüdür, ISO 9001, ISO 45001, ISO 14001, ISO 27001 gibi yönetim sistemlerinin tanımlandığı menüdür. Sistemde ilk kurulumda ISO 9001, ISO 45001, ISO 14001, ISO 27001 gibi yönetim sistemleri tanımlı olarak gelir. Firma tarafından kullanılan diğer yönetim sistemleri bu menüden tanımlanır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_489.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref78]: Yeni bir yönetim sistemi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_491.png): Listede seçili olan yönetim sistemi bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_492.png): Listede seçili olan yönetim sistemi bilgisi silinir.

![ref66]: Veriler Excel’ e aktarılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Yönetim Sistemi Tanımlama ekranına yeni bir yönetim sistemi eklemek için ekranın sol üst köşesindeki ![ref78]  butonuna tıklanarak Yönetim Sistemi Tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_493.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Sistem Kodu:** Yönetim Sistemi Tanımlama ekranında kodu sistem kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır.Örn:9001, 14001, 27001 gibi

**Açıklama:** Yönetim Sistemi Tanımlama ekranında yönetim sistemin tanım bilgisinin tanımlandığı zorunlu alandır. İlgili bayrakların bulunduğu alanlarda açıklama alanın dil karşılığı bilgisi yazılır.

**Sistem Sorumlusu:** Yönetim Sistemi Tanımlama ekranında Sistem Sorumlusu bilgisinin ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_494.png) (Seç) butonu tıklanarak açılan sistemde tanımlı personel listesinden seçildiği alandır.		

**Durum:** Yönetim Sistemi Tanımlama ekranında Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar Yönetim Sistemleri  sistemde artık kullanılmadığına bir işarettir. Kullanılmayan Yönetim Sistemleri görmek için filtre sekmesinden arama kriterlerinde durum alanında  "Pasif" olarak arama yapılması yeterlidir.

**KKD Standardı Mı?:** Yönetim Sistemi Tanımlama ekranında Kişisel Koruyucu Donanım standart ise ilgili check box işaretlendiği alandır.Örn: El Kol Koruyucu Ekipman Standartları;TS EN 388: Mekanik risklerden korunmak için üretilen eldivenler, TS EN 407: Termal risklere karşı üretilmiş koruyucu eldivenlerdir gibi. Bu standart sistemde tanımlandığında KKD standart olduğu için ilgi check box işaretlenir.

Açılan Yönetim Sistemi Tanımlama ekranında Sistem Kodu bilgisi ve  yönetim sistemide açıklama alanıda yönetim sistemin adı bilgisi yazılır. Tanımlanan yönetim sistemi KKD Standart olarak kullanıyor ise ilgili check box işaretlinir. Durum kısmı “Aktif” seçilir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref79] butonuna tıklanarak Yönetim Sistemi  kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_496.png)

Yönetim Sistemi Tanımlama ekranında Filtre sekmesinde Sistem Kodu, Açıklama, Sistem Sorumlusu ve Durum gibi alanlara veri girilip, ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_497.png) (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_498.png)
#### **5.1.22. Yönetim Sistem Madde No**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Yönetim Sistem Madde No 

Yönetim Sistemlerinin standart madde numaralarının tanımlandığı menüdür. İlk sistem kurulumda Yönetim Sistemleri menüsünde tanımlı olarak gelen ISO 9001, ISO 45001, ISO 14001, ISO 27001 gibi yönetim sistemlerinin ilgili standart madde numaraları da tanımlı olarak gelir. Firma tarafından kullanılan diğer yönetim sistemleri madde numaraları da bu menüden tanımlanır. Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Aktarımları/Madde No Aktama ve Toplu Pasif Etme menüsünde Madde No'ların toplu aktarımı ve toplu bir şekilde pasif etme işlemide yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_499.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref80]: Yeni bir madde no tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_501.png): Listede seçili olan madde no bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_502.png): Listede seçili olan madde no bilgisi silinir.

![ref66]: Veriler Excel’ e aktarılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Madde No Tanımlama ekranına yeni bir madde no eklemek için ekranın sol üst köşesindeki ![ref80]  butonuna tıklanarak Madde No Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_503.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Madde No:** Madde No Tanımlama ekranında madde no bilgisi sistem tarafından otomatik olarak verildiği alandır.	      	

**Sistem Kodu:** Madde No Tanımlama ekranında Sistem Kodu bilgisinin ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_504.png) (Seç) butonu tıklanarak açılan sistemde tanımlı Yönetim Sistemi  listesinden seçildiği alandır.	

**Tanım:** Madde No Tanımlama ekranında Madde no  tanım bilgisinin tanımlandığı zorunlu alandır.	 	

**Açıklama:** Madde No Tanımlama ekranında Madde No açıklama bilgisi girildiği alandır.	 İlgili bayrakların bulunduğu alanlarda yönetim sistemin madde no açıklama bilgisinin dil karşılıkların bilgisi yazılır.	 

**Durum:** Madde No Tanımlama ekranında Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar Madde No’lar sistemde artık kullanılmadığına bir işarettir. Kullanılmayan Madde No’ları  görmek için filtre sekmesinden arama kriterlerinde durum alanında  "Pasif" olarak arama yapılması yeterlidir.	

Açılan Madde No Tanımlama ekranında Madde No bilgisi sistem tarafından otomatik verilir. Sistem Kodu bilgisi sistemde tanımlı Yönetim Sistemi  Listesinden seçilir. Standart Madde No bilgisi Tanım kısmına yazılır. Madde açıklaması bilgisi girilir. Durum kısmı “Aktif” seçilir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref79] butonuna tıklanarak Madde No Tanımlama kayıt işlemi gerçekleştirilir. Bu şekilde ilgili yönetim sistemine ait  tüm madde no’ların tanımlama işlemi manuel şeklinde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_505.png)

Madde No Tanımlama ekranında Filtre sekmesinde Yönetim Sistemi, Madde No, Tanım ve Açıklama gibi alanlara veri girilip, ![ref65] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_506.png)
#### **5.1.23. Tatil Günleri Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Tanımlar/ Tatil Günleri Tanımlama

Milli ve dini bayramların tanıtıldığı, tatil günlerinin belirtildiği menüdür. Sisteme tanımlanan tatil günlerinde, QDMS üzerinden yapılan görev aktarımları, tatil günlerinden sonraki günlere aktarılır. Firmanın gecikmede olan işleri, yapılamayan işlemleri için gecikme mailleri tatil gününden sonraki ilk çalışma günü baz alınarak gönderilir, tatil günlerinde gecikme maillerinin gitmesi engellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_507.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref81]: Yeni bir tatil günü tanımlanır

![ref82]: Listede seçili olan tatil günü bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır.

![ref83]: Listede seçili olan tatil günü bilgisi silinir.

![ref66]: Veriler Excel’ e aktarılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_511.png) : Hafta sonları tanıtılır.

Tatil Günleri Tanımlama ekranına yeni bir tatil günü eklemek için ekranın sol üst köşesindeki ![ref81]  butonuna tıklanarak Tatil Günleri Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_512.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Tatil Günü:** Tatil Günleri Tanımlama ekranında tanımlanan  tatil günün tarih bilgisi açılan takvim alanında seçildiği alandır.

**Açıklama:** Tatil Günleri Tanımlama ekranında tanımlanan tatil günün adı bilgisinin yazıldığı alandır.

Açılan ekranda tatil günü tarihi ve açıklama bilgisi girilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![ref84] butonuna tıklanarak Tatil Günleri Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_514.png)

Tatil Günleri  Tanımlama ekranında Filtre sekmesi ile Tatil Günü ve Açıklama gibi alanlara veri girilip,  ![ref54] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_515.png)
#### **5.1.24.Masraf Yeri Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Tanımlar/ Masraf Yeri Tanımlama

Personelleri bağlı bulunduğu masraf yerleri tanımlanır. Personel tanımlanırken oluşturulan masraf yerleriyle ilişkilendirilir. Hangi personelin hangi masraf yerine bağlı olduğunu belirlemek için kullanılır. Ayrıca Stratejik Planlama modülü kapsamında  kullanılan bir menüdür. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_516.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref85]: Yeni bir masraf yeri tanımlanır

![ref86]: Listede seçili olan masraf yeri bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır.

![ref87]: Listede seçili olan masraf yeri bilgisi silinir.

![ref66]: Veriler Excel’ e aktarılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Masraf  Yeri Tanımlama ekranına yeni bir masraf yeri eklemek için ekranın sol üst köşesindeki ![ref85]  butonuna tıklanarak Masraf Yeri Tanımlama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_520.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Kodu:**	Masraf Yeri Tanımlama ekranında Masraf  Yeri kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’	

**Açıklama:** Masraf  Yeri Tanımlama ekranında Masraf  Yeri  tanım bilgisinin tanımlandığı zorunlu alandır.		

**Sorumlusu:** Masraf  Yeri Tanımlama ekranında Masraf  Yeri sorumlusunun ![ref88] (Seç) butonu tıklanarak açılan sistemde tanımlı personel listesinden seçildiği alandır.			

**Sorumlu Kullanıcı Grubu:** Masraf  Yeri Tanımlama ekranında Masraf  Yeri Sorumlu Kullanıcı Grubunun ![ref88] (Ekle) butonu tıklanarak açılan sistemde tanımlı Kullanıcı Grubu listesinde seçildiği alandır.

**Durum:** Masraf  Yeri Tanımlama ekranında Durum bilgisinin “Aktif” ve “Pasif” seçeneklerinde “Aktif” seçeneğinin seçildiği alandır. Durumu pasif olanlar Masraf  Yeri bilgisi sistemde artık kullanılmadığına bir işarettir. Kullanılmayan Masraf  Yeri bilgisi görmek için filtre sekmesinden arama kriterlerinde durum alanında  "Pasif" olarak arama yapılması yeterlidir.	

**Vergi No:** Masraf  Yeri Tanımlama ekranında Masraf  Yeri vergi numarasının tanımlandığı alandır.	

Açılan Masraf  Yeri Tanımlama ekranda Masraf  Yerinin Kodu ve Açıklama bilgisi girilir. Masraf Yeri Sorumlusu sistemde tanımlı Personel Listesinden seçilir. Durum kısmı “Aktif” edilir. Vergi Kimlik bilgisi girilir.Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref89]  butonuna tıklanarak Masraf  Yeri Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_523.png)

Masraf  Yeri Tanımlama ekranında Filtre sekmesinde Kodu, Açıklama, Sorumlusu ve Durum gibi alanlara  veri girilip, ![ref65] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_524.png)
#### **5.1.25. Kullanıcı Onay Transfer Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Kullanıcı Onay Transfer Tanımlama

Onay mekanizmasında onay işleminin asıl onaycıdan bir başka kullanıcıya devredilmesi işlemin gerçekleştirildiği menüdür. Bir kullanıcının bir kayıt üzerindeki onay görevi o kullanıcıdan başka bir kullanıcıya devredilebilir. Vekalet işleminde tüm menünün yetkisi verilirken onay mekanizması transfer menüsü ile sadece onaylama yetkisinin transferi verilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_525.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref85]: Yeni bir kullanıcı onay transfer tanımlaması yapılır.

![ref87]: Listede seçili olan kullanıcı onay transfer bilgisi silinir.

![ref66]: Veriler Excel’ e aktarılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Kullanıcı Onay Transfer Tanımlama ekranına yeni bir kullanıcı onay transfer bilgisi eklemek için ekranın sol üst köşesindeki ![ref85]  butonuna tıklanarak Kullanıcı Onay Transfer Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_526.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Asıl Kullanıcı:** Kullanıcı Onay Transferi Tanımlama ekranında Asıl Kullanıcı bilgisinin ![ref90] (Seç) butonu tıklanarak açılan sistemde tanımlı personel listesinden seçildiği alandır. Personel listesinde İşten Ayrıldı durumu olan personeller yer almaktadır.		

**Transfer Edilen Kullanıcı:** Kullanıcı Onay Transferi Tanımlama ekranında Transfer Edilen Kullanıcı alanında  ![ref90] (Seç) butonu tıklanarak açılan sistemde tanımlı personel listesinden seçildiği alandır. Personel listesinde Aktif durumu olan personeller yer almaktadır.		

**Yetkili Modüller:** Kullanıcı Onay Transferi Tanımlama ekranında	modüller alanında açılır modül listesinde yetki verilecek modüller seçilir.

Açılan Kullanıcı Onay Transfer Tanımlama ekranında ilk alanda asıl kullanıcı, 2.alanda transfer edilen kullanıcı bulunmaktadır. Açılan ekranda Asıl kullanıcı bilgisi işten ayrılan personeller listesinde ve Transfer Edilen Kullanıcı bilgisi sistemde tanımlı personel listesinden seçilir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref89] butonuna tıklanarak Kullanıcı Onay Transfer Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_528.png)

Kullanıcı Onay Transfer Tanımlama ekranında Filtre sekmesinde Asıl kullanıcı, Transfer Edilen Kullanıcı gibi ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_529.png) (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_530.png)

#### **5.1.26. İSG Uzman Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ İSG Uzman Tanımlama

Firma bünyesindeki İSG Uzmanının sisteme tanımlama işleminin yapıldığı menüdür. Eğitim Modülünde İBYS kapsamındaki eğitimlerin Bakanlığa iletilmesi sırasında kullanılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_531.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref85]: Yeni bir İSG Uzmanı tanımlanır

![ref86]: Listede seçili olan İSG Uzmanı  bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır.

![ref87]: Listede seçili olan İSG Uzmanı bilgisi silinir.

![ref66]: Veriler Excel’ e aktarılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

İSG Uzmanı Tanımlama ekranına yeni bir İSG Uzmanı eklemek için ekranın sağ üst köşesindeki ![ref85] butonuna tıklanarak İSG Uzmanı Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_532.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Personel:** ISG Uzmanı Tanımlama - Yeni Kayıt ekranında İSG Uzmanının Personel  bilgisinin ![ref90] (Seç) butonu tıklanarak açılan sistemde tanımlı personel listesinden seçildiği zorunlu alandır.	 

**İSG Uzmanlığı Belge No:** ISG Uzmanı Tanımlama - Yeni Kayıt ekranında İSG Uzmanının İSG Uzmanlığı Belge No bilgisinin yazıldığı zorunlu alandır.	 	

**İSG Uzmanlığı Belge Tarihi:** ISG Uzmanı Tanımlama - Yeni Kayıt ekranında İSG Uzmanının İSG Uzmanlığı Belge Tarihi bilgisinin açılan Takvim alanında seçildiği zorunlu alandır.	

**İSG Uzmanlığı Belge Sınıfı:** ISG Uzmanı Tanımlama - Yeni Kayıt ekranında İSG Uzmanının İSG Uzmanlığı Belge Sınıfı bilgisinin açılan açılır listeden seçildiği zorunlu alandır. İSG Uzmanı belgesine sınıfına göre;

**A Sınıfı:** Çok Tehlikeli işyerilerinde  çalışabilirler.

**B Sınıfı:** Az tehlikeli ve tehlikeli sınıflarda çalışabilirler.

**C Sınıfı:** Az Tehlikeli iş yerlerinde çalışabilirler.

İş Yerleri Tanımlama ekranında  Tehlike sınıfı alanındaki seçeneklere göre İSG uzmanın sınıfı belirlenmektedir. 

**İş Yeri:** ISG Uzmanı Tanımlama - Yeni Kayıt ekranında İSG Uzmanının bağlı bulunduğu İş  Yeri  bilgisi ![ref90] (Ekle) butonu tıklanarak açılan İş Yeri listesinde seçildiği zorunlu alandır.	

Açılan ISG Uzmanı Tanımlama - Yeni Kayıt ekranında Personel bilgisi sistemde tanımlı olan personel listesinden seçilir. İSG Uzmanlığı Belge No, İSG Uzmanlığı Belge Tarihi ve İSG Uzmanlığı Belge Sınıfı bilgileri girilir. Uzmanın bağlı bulunduğu işyeri bilgisi sistemde tanımlı iş yeri listesinden seçilir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref89] butonuna tıklanarak atanma onaya gönderme işlemi aşamasına geçilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_533.png)

ISG Uzmanı Tanımlama - Yeni Kayıt ekranında kayıt işleminden sonra sistem tarafından “Atamayı onaya göndermek istediğinizden emin misiniz ?” verilen web sitesi mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_534.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_535.png)

Atama Onay Talebinın onaylanması için tanımlanan kullanıcının Qdms Ana giriş ekranında  kullanıcı Adı ve parolası yazılarak Qdms adresine giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_536.png)

Ataması yapılan  kullanıcının  Bekleyen İşlerimi “Onay Bekleyen Atamalar Listesi” iş olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_537.png)

İlgili görevdeki Onay kodu alanındaki onay kodu linki tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_538.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref91]: İSG Uzmanın Atama Onayı onaylanır.

![ref92]: İSG Uzmanı Atama Onayı reddedilir. 

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Onay Bekleyen Atamalar ekranında  ![ref92]  butonu tıklanarak İSG Uzmanı Atama Onayında reddetme işleminde açılan Atama Ret pop-upn’da Ret Nedeni bilgi yazılarak İSG Uzmanı Atama Onayı Ret edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_541.png)

Onay Bekleyen Atamalar ekranında  ![ref91]  butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_542.png)

Atama Onay Pop- upn’da onay notu bilgisi yazılarak ![ref93]  butonu tıklanarak atama onaylama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_544.png)

Onay Notu alanı parametrik bir alandır. Sistem Altyapı Tanımları Modülü parametrelerinden 114 numaralı “Atama onaylarken onay notu girilsin?” parametresinin parametre değeri “Evet” seçilerek parametre aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_545.png)

Parametre aktif edildikten sonra Atama Onay pop-up’nda Onay Notu alanı görüntülenir.
#### **5.1.27. İş Yeri Sözleşme Tanımlama** 
**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Tanımlar/ İş Yeri Sözleşme Tanımlama

IBYS kapsamında muayene ve eğitim kayıtlarının bakanlığa gönderilmesi için yazılım firmasıyla sözleşmesinin olduğunu bildirmek için kullanıldığı menüdür. Sözleşme Girişi ekranında Sözleşme Başlangış Tarihi alanında açılır takvim alanında sözleşmenin başlangıç tarihi ve liste sekmesinde listede ilgili işyerleri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_546.png) butonu tıklanarak  Sonuç listede sözleşme durumu kısmında görülür. Sözleşme Giriş ekranında Sözleşme Bitiş Tarihi alanında açılır Takvim alanında sözleşmenin bitiş tarihi bilgisi seçilerek liste sekmesinde listede ilgili işyerleri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_547.png) butonu tıklanılanarak hizmetin silinme işlemi yapılır. Sözleşme gönderilmeden önce Sağlık kayıtları menüsünde bulunan muayene kayıtları ve Eğitim Kayıtlarında bulunan eğitim kayıtları bakanlığa gönderilmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_548.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_549.png):İşyeri ile ilgili sözleşmenin sözleşme başlangıç tarihi seçilerek bildirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_550.png):İş Yeri ile İlgili sözleşmenin sözleşme bitiş tarihi seçilerek silinme işlemi yapılır.
#### **5.1.28.  Qr Oluştur**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Qr Oluştur

Sistem Altyapı Tanımları Modülünde modüllerin ilgili menülerinde  Qr kodu alma işleminin yapıldığı menüdür. Qr Oluştur menüsünde menü alanında açılır menü listesinde menü seçilir. Menüde Qr kodu alındıktan sonra akıllı telefonunuzdaki Qr kodu okuyucu uygulama veya kamera açılır. Telefonunuzu Qr koduna doğrulturarak kamerayı hangi açıdan koda doğru tutarsanız tutun yine de gerekli bilgilere ulaşabilirsiniz. Veriler anında ekranınızda görünecektir;Qr kodları çok fazla veriyi saklayabilirler. Ancak ne kadar veri içeriyor olurlarsa olsunlar Qr kodları, taratıldıklarında kullanıcının bilgiye anında erişmesine olanak sağlarlar; bu yüzden Çabuk Tepki (Quick Response) kodu olarak adlandırılmışlardır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_551.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref94]:Seçilen Menünü Qr kodu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_553.png)

**Örn:** Menü olarak Doküman Görme menüsü seçilir. QR Kod Al ekranında menü olarak Doküman Görme menüsü seçildikten sonra ekranın sağ üstte yer alan![ref94]  buton tıklanarak menünün Qr kodu alma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_554.png)

Menüde QR kodu alındıktan sonra akıllı telefonunuzdaki Qr okuyucu uygulama veya kamera açılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_555.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_556.png)Tarayıcı aç :Or kodu alanın menünün tarayıcıdan açılma işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_557.png)Paylaş:Or kodu alanın menünün linki ilgili kişilere paylaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_558.png)Kopyala:Linkin panoya kopyalama işlemi yapılır.

Telefonunuzu Qr kodu okutularak seçilen menünün linki görüntülenir. Link tıklanarak seçilen menü olan Doküman Görme menüsünün ekranı gidilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_559.png)

Qr kodu okutularak açılan Doküman Görme menüsünde istenilen Doküman görme işlemleri ilgili işlemler yapılır. Menüde diğer menülerinde Qr kodu alınarak ve Qr kodu okutularak menü açılarak menü ile ilgili işlem aşamaları yapılır.
#### **5.1.29. Meslek Grubu Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Tanımlar/ Meslek Grubu Tanımlama

Meslek grubu tanımlama ekranında faaliyetin/ tesisin bulunduğu nace kodlarına göre meslek sınıfları yer almaktadır. Bu tanımlar sistemde tanımlı olarak bulunmaktadır. “Meslek Grubu Tanımı” bilgi amaçlı olup, işyeri tanımlama ekranında işyerinin ait olduğu meslek grubunu belirtmek ve personel tanımlama ekranında ek alanlardan personelin eski işyerinin ait olduğu meslek grubunu seçmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_560.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref85]:Yeni bir Meslek grubu tanımlanır.

![ref86]: Listede seçili olan Meslek grubu bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır.

![ref87]: Listede seçili olan Meslek grubu bilgisi silinir.

![ref95]: Veriler Excel’ e aktarılır.

![ref96]: Kayıtlar filtrelenerek arama yapılır.

![ref97]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref98]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Meslek Grubu Tanımlama ekranına yeni bir Meslek grubu eklemek için ekranın sağ üst köşesindeki ![ref85] butonuna tıklanarak Meslek Grubu Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_565.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Üst kod:** Meslek Grubu Tanımlama - Yeni Kayıt ekranında sistemde tanımlı olan bir meslek grubu altına o meslek grubuna  bağlı olan yeni bir meslek grubuna  tanımlanmak isteniyorsa “Üst  meslek grubu ” seçilir. 

**Kod:** Meslek Grubu Tanımlama - Yeni Kayıt ekranında meslek grubu kodu bilgisi tanımlandığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Tanım:** Meslek Grubu Tanımlama - Yeni Kayıt ekranında Meslek Grubu tanım bilgisinin tanımlandığı zorunlu alandır.İlgili bayrakların bulunduğu alanlarda ingilizce dil karşılığının bilgisi yazılır.

**Açıklama:** Meslek Grubu Tanımlama - Yeni Kayıt ekranında Meslek Grubu varsa açıklama  bilgisinin tanımlandığı  alandır.		

**Tehlike Sınıfı:** Meslek Grubu Tanımlama - Yeni Kayıt ekranında Meslek Grubunun Tehlike Sınıfı bilgisinin açılır Tehlike sınıfı listesinde seçildiği alandır.

Açılan Meslek Grubu Tanımlama - Yeni Kayıt ekranında meslek grubunun varsa üst kodu seçilir. Meslek Grubunun Kodu, Tanımı ve Açıklama bilgisi girilir. Tehlike sınıfı bilgisi “Az Tehlikeli, Tehlikeli ve Çok Tehlikeli” seçeneklerinden seçilir. Gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref89]  butonuna tıklanarak “Meslek Grubu Tanımlama” kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_566.png)

Meslek Grubu Tanımlama Filtre sekmesinde Üst Kod, Kod, Tanım ve Açıklama gibi alanlara  veri girilip, ![ref96] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_567.png)
#### **5.1.30. İşe Giriş Muayenesi Sonuçlandırma**
**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Tanımlar/İşe Giriş Muayenesi Sonuçlandırma

Firmaya işe girişi yapılan ancak firma sisteminde tanımlı olmayan yeni bir personel için, işe giriş muayenesi yapıldıktan sonra Qdms sistemi tarafından verilen geçici sicil numarasının, personel firma sistemine kayıt edildikten sonra verilen gerçek sicil numarası ile değiştirilme işleminin yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_568.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref86]: Listede seçili olan işe giriş muayenesi yapılan personel bilgisini düzeltme/ değişiklik/ güncelleme yapılır.

![ref87]: Listede seçili olan işe giriş muayenesi yapılan personel bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_569.png): Seçili personele ait ek bilgiler tanımlanır.

![ref95]: Veriler Excel’ e aktarılır.

![ref96]: Kayıtlar filtrelenerek arama yapılır.

![ref97]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref98]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

İş Başı ve Periyodik Muayene modülünde Entegre Yönetim Sistemi/İşbaşı ve Periyodik Muayene / İş Başvurusu Muayenesi menüsünde perrsonelin işe giriş muyanesi kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_570.png)

İş Başvurusu Muayenesi ekranında personele geçici bir sicil no’su verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_571.png)

İşe Giriş Muayenesi Sonuçlandırma ekranında personel seçili iken ![ref86]  butonuna tıklanarak Personel Tanımlama/ Kayıt Güncelleme ekranı açılır. Eğer personel Qdms sistemine kayıtlı durumdaysa “Kayıtlı Personelden Seç” diyerek sistemde tanımlı olan gerçek personel bilgisinin seçilerek kaydedilmesi yeterli olmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_572.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sicil No:** Personel Tanımlama – Kayıt Güncelle ekranında personelin  Sicil no bilgisinini girildiği zorunlu alandır. Qdms ana giriş ekranında kullanıcı adı kısmında sicil no  ve  parola kısmında parola bilgileri yazılarak  personel  Qdms local adresine giriş yapar. Eğer Active Directory Entegrasyonu sağlandıysa; personel, bilgisayarını açtığı kullanıcı adı/ şifre bilgisi ile Qdms local adresine giriş yapabilir. Active directory entegrasyonunun sağlanması için Bimser Teknik Personelinden destek alınmalıdır.

**Adı:** Personel Tanımlama - Kayıt Güncelle ekranında personeli adı bilgisinin tanımlandığı zorunlu alandır.

**Soyadı:** Personel Tanımlama - Kayıt Güncelle ekranında personelin Soyadı bilgisinin tanımlandığı alandır.

**Parola:** Personel Tanımlama - Kayıt Güncelle ekranında personelin parola bilgisinin tanımlandığı alandır.Tanımlanan bu parola ile Qdms ana giriş ekranında  kullanıcı adı ve parola alanı parola bilgisini yazara personel Qdms local adresine giriş yapar.

**Parola Tekrar:** Personel Tanımlama - Yeni Kayıt ekranında tanımlanan paralo bilgisinin tekrar edildiği alandır.

**İş Yeri:** Personel Tanımlama - Kayıt Güncelle ekranında Personelin işyeri bilgisinin  ![ref40] (Seç) butonu tıklanarak açılan sistemde tanımlı İş yeri listesinde seçildiği alandır.

**Masraf Yeri:** Personel Tanımlama - Kayıt Güncelle ekranında personelin ait olduğu masraf yeri bilgisi ![ref40] (Seç) butonu tıklanarak açılan sistemde tanımlı masraf yeri listesinden seçildiği alandır.( Masraf  Yeri listesi Sistem Altyapı Tanımları/BSAT/Tanımlar/Masraf Yeri Tanımlama menüsünde tanımlı olarak gelmektedir.)

**Unvan:** Personel Tanımlama - Kayıt Güncelle ekranında personelin unvan bilgisinin ![ref40] (Seç) butonu tıklanarak açılan sistemde tanımlı unvan bilgisinden seçildiği alandır.(Unvan Listesi Sistem Altyapı Tanımları/BSAT/Tanımlar/ Unvan Tanımlama menüsünde tanımlı olarak gelmektedir.)

**Departman:** Personel Tanımlama - Kayıt Güncelle ekranında personelin bulunduğu departman bilgisinin ![ref40] (Seç) butonu tıklanarak açılan sistemde tanımlı departman bilgisinden seçildiği alandır.(Departman Listesi Sistem Altyapı Tanımları/BSAT/Tanımlar/ Departman Tanımlama menüsünde tanımlı olarak gelmektedir.)

**Bağlı Bulunduğu Pozisyon:** Personel Tanımlama - Kayıt Güncelle ekranında personelin bağlı bulunduğu pozisyon bilgisi ![ref40] (Seç) butonu tıklanarak açılan sistemde tanımlı Pozisyon listesinde seçildiği alandır. 

**Durum:** Personel Tanımlama - Kayıt Güncelle ekranında personelin durum bilgisinin  açılır liste tıklanarak açılan sistemde tanımlı durum seçeneklerinde seçildiği alandır. 

**Kategori:** Personel Tanımlama - Kayıt Güncelle ekranında personelin kategori bilgisinin açılır liste tıklanrak açılan kategori listesinde seçildiği alandır. 

**Doğum Tarihi:** Personel Tanımlama - Kayıt Güncelle ekranında personelin doğum Tarihi bilgisinin açılan Takvim alanında seçildiği alandır.

**İşe Giriş Tarihi:** Personel Tanımlama - Kayıt Güncelle ekranında personelin İşe giriş Tarihi  bilgisinin açılan Takvim alanında seçildiği alandır. 

**İşten Çıkış Tarihi:** Personel Tanımlama - Kayıt Güncelle ekranında personelin İşten Çıkış Tarihi bilgisinin açılan Takvim alanında seçildiği alandır.

**Eğitim Seviyesi:** Personel Tanımlama - Kayıt Güncelle ekranında personelin eğitim seviyesinin açılır liste tıklanarak açılan eğitim seviyesi listesinde seçildiği alandır. 

**Active Directory Kullanıcı Adı:** Personel Tanımlama - Kayıt Güncelle ekranında personelin Active Directory Kullanıcı Adının tanımlandığı alandır. Eğer Active Directory entegrasyonu sağlanacaksa (yani personelin bilgisayarını açtığı kullanıcı adı ve şifre ile Qdms sistemine giriş yapması isteniyorsa) “Active Directory User Name” kısmı tanımlanır. Bu alana personelin bilgisayarını açarken girdiği kullanıcı adı bilgisi yazılır.

**E-posta:** Personel Tanımlama - Kayıt Güncelle ekranında personelin E-Posta adresinin tanımlandığı zorunlu alandır. Mail adresleri tanımlı olan personel için ilgili modüllerdeki akışların devamlılığını sağlayacak olan, gecikmelerden gelen maillerin gönderimleri sağlanır. Ayrıca maili tanımlı olan personellere atanan görevler mail olarak da kişiye iletilir.

**Cep Telefonu:** Personel Tanımlama - Kayıt Güncelle ekranında personelin cep telefonu bilgisinin tanımlandığı alandır.

**Bağlı Olduğu Gruplar:** Personel Tanımlama - Kayıt Güncelle ekranında personelin bağlı olduğu grupların ![ref45] (Ekle) butonu tıklanarak açılan sistemde tanımlı kullanıcı grubu listesinde seçim yapıldığı alandır. (Kullanıcı Grubu Listesı Sistem Altyapı Tanımları/BSAT/Tanımlar/Kullanıcı Grubu Tanımlama menüsünde tanımlı olarak gelmektedir.)“Bağlı Olduğu Gruplar” alanından personel ilgili olduğu kullanıcı gruplarına tanımlanabilir. Eğer bu alan boş bırakılırsa Kullanıcı Grubu Tanımlama menüsünden de kullanıcı gruplarına ilgili personeller atanabilir.

**Bağlı Kişiler:** Personel Tanımlama - Kayıt Güncelle ekranında personelle bağlı kişileri varsa sistemin otomatik olarak  bu alanda görüntüler. Personele bağlı olan alt personeller varsa “Bağlı Kişiler” alanında tanımlı olarak gelmektedir. Bu alanda işlem yapılamaz. Bu personel başka personellere üst amir olarak atandıkça bu alan otomatik olarak sistem tarafından dolar.

**Kullanıcı Kilitli:** Personel Tanımlama - Kayıt Güncelle ekranında ilgili alanla ilgili check box işaretlendiğinde kullanıcının şifresini yanlış girdiğinde Qdms giriş ekranın kilitlenme işlemi yapılır. Eğer personel Qdms sisteminde tanımlı olmayıp, açılan ekrandan tanımlanacaksa personele ait sicil no, adı, soyadı, unvan departman gibi alanlar doldurularak Personel Tanımlama kayıt güncelleme  işlemi yapılır. Personelin İş yeri bilgisi sistemde tanımlı iş yeri listesinden, Unvan bilgisi sistemde tanımlı Unvan listesinden, departman bilgisi sistemde tanımlı departman listesinden, bağlı bulunduğu Pozisyon bilgisi sistemden tanımlı Pozisyon listesinden, Masraf yeri bilgisi sistemde tanımlı Masraf yeri listesinden seçilir. Durum kısmı aktif, işten ayrıldı, iş başvurusu, Misafir seçeneklerinden biri seçilir. Active Directory User Name bilgisayarı açarken kullanılan kullanıcı adı ve şifresi bilgisi girilir. Sicil No, Adı, Parola bilgileri zorunlu alandır. “Kategori” kısmında personelin kapsam içi, kapsam dışı, sözleşmeli, müteahhit gibi çalışma durumları belirlenir.Personel Tanımlama – Kayıt Güncelleme ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki  ![ref33]   butonuna tıklanarak Personel Tanımlama kayıt güncelleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_573.png)

Personel Tanımlama iş giriş muayenesi tanımlama ekranında geçici sicil verilen personele İşe Giriş Muayenesi Sonuçlandırma ekranında  personel firma sistemine kayıt edildikten sonra verilen gerçek sicil numarası ile değiştirilme işleminin yapıldığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_574.png)

İşe Giriş Muayenesi Sonuçlandırma ekranında Filtre sekmesinde Sicil No, Adı, Soyadı, Departman gibi alanlara  veri girilip, ![ref96] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_575.png)
### **5.2. Konfigürasyon Ayarları**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları

Qdms sisteminde özel ayarların yapıldığı menülerdir. Bu menülerde yapılan ayarlar tüm Qdms kullanıcıları için geçerli olan ortak ayarlardır. 
#### **5.2.1. Servis Giriş Bilgileri Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/Servis Giriş Bilgileri Tanımlama

QDMS Web servislerini çalıştırmak için kullanılacak kullanıcı adı & şifre tanımlamasının yapıldığı ve her modül için Qdms arka planından yazılan web servisleri  bulunduğu bir menüdür.  QDMS Destek ekibinin modül uzmanları bu menüde işlem yapma yetkisine sahiptir. Örn: Doküman Yönetimde Doküman Toplu Aktarım programında kullanılan CDSA.Client programında kullanılacak kullanıcı adı&Şifre Tanımlaması bu menüden yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_576.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref86]: Listede seçili olan servis giriş bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır.

![ref99]: Veriler Excel’ e aktarılır. 

![ref100]: Kayıtlar filtrelenerek arama yapılır.

![ref101]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref102]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Servis Giriş Bilgileri Tanımlama ekranında listede CDSA.WebService/Main.asmx seçili iken ![ref86]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_581.png)

Servis Giriş Bilgileri Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![ref89]  butonuna tıklanarak Servis Giriş Bilgileri Tanımlama kayıt güncelleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_582.png)

Servis Giriş Bilgileri Tanımlama ekranında Filtre sekmesinde Servis ve Kullanıcı Adı gibi alanlara  veri girilip, ![ref96] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_583.png)
#### **5.2.2. Duyuru Yetki Matrisi**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/Duyuru Yetki Matrisi

Duyuru oluşturma menüsü için  yetkilendirme işlemi yapıldığı menüdür. Kullanıcı ve kullanıcı grubu seçimi yapılarak ilgili işyerleri, ilgili departmanlar ve ilgili kullanıcı gruplara bağlı yetkilendirme işlemi yapılır.Duyuru Yetkilisi alanında duyuru yetkisi olan kullanıcı  için seçilen iş yeri, departman ve kullanıcı grubu için duyuru oluşturma yetkisi verilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_584.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_585.png): Yeni bir duyuru yetkisi tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_586.png):Listede seçili duyuru yetkisi bilgisi silinir.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Duyuru Yetkisi Matrisi  Tanımlama ekranına yeni bir duyuru yetkisi  eklemek için ekranın sol üst köşesindeki ![ref85]  butonuna tıklanarak Duyuru Yetkisi Matrisi -Yeni Kayıt  ekranı açılır.![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_587.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Duyuru Yetkilisi:** Duyuru Yetki Matrisi -Yeni Kayıt ekranında duyuru yetkilisinin kullanıcı ve kullanıcı grubu seçeneklerinden seçim yapıldığı alandır.	Seçilen duyuru yetkilisi seçeneği  Kullanıcı ise Kullanıcı seçilen alan olan Kullanıcı alanı görüntülenir  ve sistemde tanımlı personel listesinde personel seçimi yapılır. Seçilen duyuru yetkili seçeneği Kullanıcı grubu ise Kullanıcı Grubu alanı görüntülenir ve sistemde tanımlı kullanıcı grubu listesinde Kullanıcı grubu seçim işlemi yapılır. 

**Kullanıcı:** Duyuru Yetki Matrisi -Yeni Kayıt ekranında duyuru yetkilisi alanında kullanıcı seçeneğine göre görüntülenen ve sistemde tanımlı personel listesinde seçim yapıldığı alandır.

**İş Yeri:** Duyuru Yetki Matrisi -Yeni Kayıt ekranında duyuru yetkilisi seçeneğine bağlı olarak duyuru ile yetkilendirme işlemi yapılacak iş yerinin ![ref103] (Ekle) butonu tıklanarak açılan sistemde tanımlı iş yeri  listesinden seçildiği alandır.

**Departmanı:** Duyuru Yetki Matrisi -Yeni Kayıt ekranında duyuru yetkilisi seçeneğine bağlı olarak duyuru ile yetkilendirme işlemi yapılacak departmanlarının ![ref103] (Ekle) butonu tıklanarak açılan sistemde tanımlı departman listesinden seçildiği alandır.	

**Kullanıcı Grubu:** Duyuru Yetki Matrisi -Yeni Kayıt ekranında duyuru yetkilisi seçeneğine bağlı olarak duyuru ile yetkilendirme işlemi yapılacak kullanıcı grubu ![ref103] (Ekle) butonu tıklanarak açılan sistemde tanımlı kullanıcı  listesinden seçildiği alandır.

Duyuru Yetki Matrisi -Yeni Kayıt ekranında duyuru yetkilisi seçeneği kullanıcı olarak seçilerek duyuru oluşturma  yetkilendirme işlemi yapılacak iş yerleri, departmanlar ve kullanıcı grupları sistemde tanımlı listeden seçilir. Gerekli alanlar ilgili bilgiler girildikren sonra ekranın sol üst köşesindeki ![ref104]  butonu tıklanarak  Duyuru Yetki Matrisi tanımlama kayıt işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_590.png)
#### **5.2.3. Parametreler**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametreler

Sistem Altyapı Tanımları modülü için kullanıcının istek ve ihtiyaçlarına göre çeşitli sistemsel ayarlamaların yapabildiği ve bunlara göre parametrelerin belirlendiği menüdür. Parametrelerde yapılan değişikler tüm Qdms kullanıcılarını kapsamaktadır.Parametreler ekranında Liste ve Filtre sekmesi olmak üzere iki sekme karşımıza çıkar. Liste sekmesinde Sistem Altyapı Tanımları Modülü ile ilgi tüm parametreler listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_591.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref105]: Listede seçili olan parametre bilgisi üzerinde düzenleme/değişiklik/güncelleme işlemi yapılır.

![ref22]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Parametreler  ekranında Filtre sekmesinde, Parametre No ve Parametre Tanımı gibi alanlara veri        girilip,  ![ref22] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_593.png)

Sistem Altyapı Tanımları Modülü parametrelerinde 100 numaralı “	Maillerin Sistemde Tutulma Süresi (Gün) “parametresi parametreler ekranında Filtre sekmesinde parametre no alanına numarası yazılarak ![ref106] (Ara) butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_595.png)

Arama işlemi için Parametreler ekranında liste sekmesinde gridde kolonların karşılığındaki alanlarda kullanılır. Parametre numarası bilinmiyorsa parametre liste sekmesinde gridde Tanım alanında parametre içerisinde geçen anahtar bir kelime yazılarak aratılma işlemi de yapılabilir. Yada Parametre numarası biliyorsa gridde parametre No alanınada parametre numarası yazılırak parametrenin aratılma işlemide yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_596.png)

Parametre seçildiktende sonra ![ref105] butonu tıklanılır.Açılan parametreler ekranında parametre değerinin değiştirilmek istenilen yeni değer bilgisi girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_597.png)

Parametreler ekranında parametre değerine girilen yeni değer bilgisinden sonra ekranın sol üst köşede yer alan ![ref104]  butonu tıklanarak parametre kayıt güncelleme işlemi yapılır.Yeni girilen parametre değerine göre  maillerin Sistemde Tutulma Süresi (Gün) bazında değeri belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_598.png)

Sistem Altyapı Tanımaları Modülü parametrelerinde 102 numaralı “SMS bildirimi kullanıcak mı?” parametresinin parametreler ekranında Filtre sekmesinde parametre no alanına parametre numarası yazılarak ![ref107] (Ara) butonu tıklanarak aratılarak seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_600.png)

Parametre seçildiktende sonra ![ref108] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_602.png)

Açılan parametreler ekranında parametre değeri seçeneklerinde  “Evet” ilgili check box seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_603.png)

Parametreler ekranında parametre değeri “Evet” seçildikten sonra ekranın sol üst köşesinde yer alan ![ref104] butonu tıklanarak parametre aktif etme kayıt işlemi yapılır.Parametre aktif etme işleminde sonra QDMS modüllerinde E-Posta ayarları ekranında “SMS gitsin mi?” alanı ile ilgili alan görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_604.png)

Aynı işlem basamakları yapılarak aktif durumundaki parametreyi  parametre değeri “Hayır” seçilerek pasif etme işlemi yapılır. Bu şekilde parametreler ekranında seçili parametreyi ![ref108]  butonu tıklanarak içeriği görüntülenerek pasif durumundaki parametreyi aktif etme, aktif durumundaki parametreyi pasif etme ve parametrenin parametre değeri değiştirme işlemi yapılır.
#### **5.2.4. Sabitler**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Sabitler

Menülerde yer alan sabit liste elemanların düzenlendiği menüdür. Filtre sekmesinde Modüller alanında uygun modül seçilerek, ![ref96] (Ara) botunu tıklanır.Liste sekmesinde seçilen Modül ilgili sabitlerin listesi listenir. Listelenen Sabitler listesinde düzenleme yapılacak Sabit listeden sabit seçilerek ![ref108] butonu tıklanarak açılan Sabitler ekranında sabit değerleri alanında yine ![ref108] butonu ile  statüsü Aktif ve pasif seçeneklerinden seçim yapılarak Aktif ve pasif edilme işlemi gerçekleştirilir. Statüsü Pasif edilen sabit değeri sistemde görüntülenmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_605.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_606.png): Listede seçili olan sabit bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır.

![ref66]: Veriler Excel’ e aktarılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Örneğin; Sabitler ekranında Filtre sekmesinde Modüller alanında açılır Modül listesinde Düzeltici  ve Önleyici Faaliyetler modülü seçilir ve  ![ref65] (Ara) butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_607.png)

Sabitler ekranında Liste sekmesinde Düzeltici  ve Önleyici Faaliyetler modülü ilgili sistemde tanımlı sabitler listelenir. 1 nolu sabit tanımında işlem kaynağı tipi yer almaktadır. Sistem Altyapı Tanımları/DÖF/DÖF İşlem Kaynağı menüsünde işlem kaynak tipleri karşımıza çıkmaktadır. 1 nolu sabit  tanımı “İşlem Kaynağı Tipi”  seçilerek  ![ref108]  butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_608.png)

Açılan Sabitler ekranında Sabit Değerleri alanın Sabit değeri seçilerek ![ref108]  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_609.png)

Açılan Sabitler ekranında Sabit Değerileri kısmında listeden sabit değeri seçili iken![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_610.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_611.png)

Sabit Değerleri -Kayıt Güncelleme ekranında sabit değeri Durum alanın durumu pasif edilerek ![ref109]  botunu tıklanarak Sabit değerleri kayıt güncelleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_613.png)

Sabitler ekranında ekranın sol üstte yer alan ![ref109]  butonu tıklanarak Sabitler kayıt gücelleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_614.png)

Sistem Altyapı Tanımları/DÖF/DÖF İşlem Kaynağı menüsünde ![ref78]  butonu tıklanarak açılan İşlem Kaynağı Tanımlama ekranında Sabitler menüsünde pasif edilen “Şirket Dışı” Sabit değerinin İşlem Kaynağı Tipi alanında görüntülenmez. Aynı şekilde aynı işlem basamakları yapılarak Sabitler menüsünde Sabit değerleri- Kayıt güncelleme ekranında statü alanında aktif edilerek sistemde İşlem kaynağı Tipi alanında görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_615.png)  

Qdms sistemdeki Modüllerinin sistemde tanımlı sabitleri için Sabitler ekranında Sabit değerlerin statüsünü aktif ve pasif yapma işlemi aynı işlem basamakları şeklinde yapılmaktadır.
#### **5.2.5. Modül Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Modül Tanımlama

Qdms sisteminde tanımlı olan modüller yer almaktadır. Firma tarafından kullanılacak bütün Modül tanımlamaları bu alanda Bimser tarafından tanımlanmış bulunmamaktadır. Kullanıcılar tarafından yeni bir modül tanımı yapılamaz. Bu menüde sadece modül tanımları üzerinde değişiklik yapılır. Bu modül tanımları menülerde bulunan modüller alanında açılan açılır modül listesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_616.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref108]: Listede seçili olan modül tanımı için düzeltme/ değişiklik/ güncelleme yapılır.

![ref66]: Veriler Excel’ e aktarılır. 

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Modül Tanımı ekranında listede Modül Tanımı seçili iken ![ref108]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_617.png)

Modül Tanımlama ekranında modül tanımı alanında değiştirilme işlemi yapılır. İlgili bayrakların olduğu alanında ingilizce dil karşılığı yazılır.Gerekli alanları ilgili bilgiler üzerinde değişiklik yapıldıktan sonra ekranın sol üst köşesindeki ![ref110]  butonu tıklanarak kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_619.png)

Modül Tanımlama işleminde sonra  menülerde açılan Modüller alanında açılan açılır Modül listesinde değişiklik yapılan modülün tanım bilgisi düzenlenmiş şekli ile listede yer alır.Örn:Parametreler menüsü.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_620.png)

#### **5.2.6. Parametrik Alan**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametrik Alan

Qdms sisteminde bulunmayan ancak firmaların Personel Tanımlama, Departman Tanımlama, İşyeri Tanımlama, Kontrol Tanımlama, Müşteri-Tedarikçi Tanımlama, Şirket Profili Tanımlama, Ürün Tanımlama menülerinde görmek istedikleri ekstra alanların tanımlandığı menüdür.
#### **5.2.6.1. Alan Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametrik Alan/ Alan Tanımlama

Personel, Departman, İşyeri, Kontrol, Müşteri-Tedarikçi, Şirket Profili ve Ürün Tanımlama ekranlarında görülmesinin istenilen parametrik alanların tanımlaması bu menü kullanılarak gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_621.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref111]: Yeni bir alan eklenir.

![ref105]: Listede seçili olan alan bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır.Kod bilgisi güncellenemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_623.png):Listede seçili olan alan bilgisi kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_624.png): Listede seçili olan alan bilgisi silinir.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_625.png) : Alanın değerleri tanımlanır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranında kullanıcı bazlı tasarlama işlemi yapılır.

Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sol üst köşesindeki ![ref3]  butonuna tıklanarak Alan Tanımlama\ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_626.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_627.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Kodu:** Alan Tanımlama-Yeni Kayıt ekranında Alan Kodu bilgisinin yazıldığı zorunlu alandır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan Tanımlama-Yeni Kayıt ekranında Alan Adı bilgisinin yazıldığı alandır. Diğer dil seçenekleri de kullanılacaksa ilgili bayrağın bulunduğu yere ilgili alan adının dil karşılığı yazılır.

**Başlık Notu:** Alan Tanımlama-Yeni Kayıt ekranında alanı veri girişinin yapılması ile ilgili  açıklayıcı bilgi içeren not bilgisinin girildiği alandır. Mouse ile alanın üzerine gelindiğinde görüntülenen bilgidir. Diğer dil seçenekleri de kullanılacaksa ilgili bayrağın bulunduğu yere ilgili alan başlık notu dil karşılığı yazılır.

**Giriş Tipi:** Alan Tanımlama-Yeni Kayıt ekranında giriş tipinin Hesaplanan veya Veri Girişi tipi bilgisinin seçilebildiği alandır. Giriş Tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir. Örneğin; Veri Girişi.

**Alan Tipi:** Alan Tanımlama-Yeni Kayıt ekranında alan tipinin bilgisinin seçilebildiği alandır. Alan Tipi ise oluşturulan alanın metin, numerik, tarih, liste vb. tiplerinden hangisi olduğunu gösterir. Örneğin; Personel

**Seçim Tipi:** Alan Tanımlama-Yeni Kayıt ekranında tanımlanan alanında tekli veya çoklu seçim seçeneklerinde seçim yapılan alandır. 

**Görünme Şartı:** Alan Tanımlama-Yeni Kayıt ekranında Görünme Şartı bilgisinin girildiği alandır. Bir alan eğer başka bir alanın şartına bağlı olarak görülecekse görünme şartı kullanılır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar. Kullanımı [ALANKODU]=ALAN\_DEĞERİ vb. şekildedir. (Örneğin, Bulgu var mı? Alanının  alan kodu 01; Bulgu alanının alan kodu 02 olsun. Eğer “Bulgu” Alanının, “Bulgu var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Bulgu” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan Tanımlama-Yeni Kayıt ekranında durumun Aktif veya Pasif olarak bilgisinin seçilebildiği alandır.

**Genişlik:** Alan Tanımlama-Yeni Kayıt ekranında genişlik bilgisinin girildiği alandır.

Alan Tanımlama-Yeni Kayıt alan kodu ve alan adı bilgisi girilir. Giriş Tipi  veri girişi ve alan tipi personel seçilir. Seçim Tipi alanında tekli seçim tipi seçilir.Durum kısmı Aktif olarak seçilir. Alan Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref9]  butonuna tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_628.png)

Sistem Altyapı Tanımları modülü ile ilgili menülerde ekranında görüntülecek alan tanımlama işlemi bu şekilde yapılarak alan havuzuna eklenir.

**Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir**;

**Metin:** Metin kutucuğu ekler.

**Metin Çok Satırlı:** Çok satırlı metin kutucuğu ekler.

**Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.

**Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.

**Tarih:** Takvim alanı ekler.

**Liste:** Birden fazla element arasından tek seçim yaptırır.

**Puanlı Liste:** Açılır menüden tekli seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.

**Arama Özellikli Liste:** Açılır menü altından birden fazla seçim yapılmasını sağlar.

**Ağaç Liste:** Ağaç dallanması şeklinde menü altından birden fazla seçim yapılmasını sağlar.

**Personel:** QDMS Personel veri tabanından kişi bilgisi seçilebilmesini sağlar.

**Departman:** QDMS Departman veri tabanından departman bilgisinin seçilebilmesini sağlar.

**Ünvan:** QDMS ünvan veri tabanından ünvan bilgisinin seçilebilmesini sağlar.

**Doküman:** QDMS Doküman veri tabanından doküman seçilebilmesini sağlar.

**Yönetim Sistemi:** QDMS Yönetim Sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.

**Müşteri:** QDMS Müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.

**Tedarikçi:** QDMS Tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.

**Ürün:** QDMS Ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.

**Şirket Profili:** QDMS Şirket Profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.

**Başlık:** Risk formuna ya da detay ekranına başlık ekler.

**Dosya:** Dosya ekler.

**Resim:** Resim ekler.

**Resim Liste**: Resim listesinden seçim sağlar.

**Çoklu Resim:** Çoklu resim seçilmesini sağlar.

**Tablo:** Tablo verilerinin kullanılmasını sağlar.

**Sorgu:** Sorgulama şeklinde seçim sağlar.

**Sorgu Ağaç:** Ağaç dallanması şeklinde sorgu yapılmasını sağlar.
#### **5.2.6.2.Fonksiyon Dizanyer**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametrik Alan/ Alan Tanımlama

Alan Tanımlama menüsünde oluşturulan alanların Personel Tanımlama, Departman Tanımlama, İşyeri Tanımlama, Kontrol Tanımlama, Müşteri-Tedarikçi Tanımlama, Şirket Profili Tanımlama ve Ürün Tanımlama ekranlarından hangisinde görüntüleneceğinin bu menü ile belirlenir.Fonksiyon Dizayner ekranında alan nerede kullanılacaksa Personel Tanımlama, Departman Tanımlama, İşyeri Tanımlama, Kontrol Tanımlama, Müşteri-Tedarikçi Tanımlama, Şirket Profili Tanımlama ve Ürün Tanımlama fonksiyonlarından seçim yapılıp ![ref112]  butonuna tıklanır ve bu alanın ilgili fonksiyonun sayfalarında görüntülenmesi sağlanır.

Alan Tanımlama menüsünde Departman Tanımlama menüsü için  “Üst Departman Sorumlusu” personel tipli alan tanımlaması yapıldığı için  Fonksiyon Dizanyer menüsünde 2 numaralı fonksiyon olan Departman Tanımlama menüsü seçilir ve  ![ref112] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_630.png)

Fonksiyon Dizayn - Alanlar - Departman Tanımlama ekranında ![ref112]  butonuna ile açılan ekranda seçili olan fonksiyonda kullanılacak alanlar ![ref85]  butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_631.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref111]: Listede seçili fonksiyona yeni bir alan eklenir.

![ref105]:Listede seçili eklenen fonksiyona eklenen alan bilgisi üzerinde değişiklik/düzenleme/güncelleme işlemi yapılır.

![ref113]: Listede seçili eklenen fonksiyona eklenen alan bilgisi silinir.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Açılan Fonksiyon Dizayn - Alanlar - Deparman Tanımlama ekranda seçili olan fonksiyonda kullanılacak alanlar  ![ref111]  butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_633.png) ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_634.png)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Alan Adı:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında tanımlanan ilgili alan adı seçilir.

**Zorunlu Mu? :** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için veri girişinin zorunlu olup olmadığı belirlenir. “Evet” seçeneği seçildiğinde alan için veri girişi zorunludur.

**Zorunluluk Mesajı:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için Zorunluluk Mesajı bilgisinin girildiği alandır. Zorunlu alanlar doldurulmadığında verilecek uyarı mesajı bilgisi yazılır.

**Sıra No:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alanın ekranda kaçıncı sırada görüntüleneceği bilgisinin girildiği alandır.

**Varsayılan Rol:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için, rol tanımlama ekranında bulunan hangi rol tarafından onaylanacağı bilgisinin girildiği alandır. 

**Varsayılan Değer Değiştirilmesin:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan varsayılan değer değiştirilmesi istenmiyorsa ilgili check box işaretlenir.

**Gridde göster:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alanın liste grid ekranında gösterilmesi isteniyorsa ilgili check box işaretlenir.

**Satır Sayısı**: Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için satır sayısı bilgisinin belirlendiği alandır.

**Kolon Genişliği:** Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında seçilen alan için kolon genişliği bilgisinin belirlendiği alandır.

Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında gerekli tüm alanlar doldurulduktan sonra ekranın sol üst köşesindeki  ![ref104]  butonuna tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_635.png)

Tanımlanan personel tipli alan Departman Tanımlama ekranında  ![ref111]  butonu tıklanarak açılan Departman Tanımlama-Yeni Kayıt ekranında görüntülenir. Tanımlanan personel tipli alanın mause ile üzerine gelindiğinde başlık notu bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_636.png)

Departman Tanımlama-Yeni Kayıt ekranında ilgili alanlar bilgiler girildikten tanımlanan personel zorunlu alan doldurulmadığında  sistem kayıt işlemine izin vermez zorunluluk mesajı bilgisi ile alanın doldurulmasının gerektiğini belirtir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_637.png)

Sistem Altyapı Tanımları Modülünde ilgili fonksiyonlarda alan tanımlama işlemi ve fonksiyonun sayfalarıyla ilişkilendirme işlemi aynı şekilde yapılmaktadır. Fakat Personel Tanımlama ekranında alan tanımlama işlemi diğer fonksiyonlardan farklı olarak yapılmaktadır.  İlgili fonksiyonun tanımlanan alanın ilişkilendirme işlemi yapıldığında açılan Alan Tanımlama - Fonksiyonlar - Yeni Kayıt ekranında Kullanılacak Yer alanında seçeneklere bağlı alanın görüntülenmesi sağlanır.

İlgili alanın İşbaşı Periyodik Muayene Modülü ve Sistem Altyapı Tanımları Modülün sayfalarında kullanımın seçimin belirlenir. Kullanılacak yer alanında Muayene seçimi yapıldığına İş Başı Periyodik Muayene Modülün Muayene Takibi Ana sekmesi ekranında tanımlanan alanın görüntülenmesi sağlanılır. Kullanılacak yer alanında Personel seçimi yapıldığında 76 parametreye bağlı olarak görüntülenen ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_638.png)   butonu tıklanarak açılan Personel Tanımlama-Ek Bilgiler- Kayıt güncelleme ekranında tanımlanan alan görüntülenmesi sağlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_639.png)
#### **5.2.7. Alt Modül Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Alt Modül Tanımlama

Modüllerde var olan açma, gerçekleştirme, geciktirme, kapatma onayları için kullanılan akışların modüllere tanıtıldığı; onay talep, bildirim ve red mesajlarının ilişkilendirildiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_640.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref114]: Listede seçili olan alt modül bilgisi üzerinde düzeltme/ değişiklik/ güncelleme işlemleri yapılır.

![ref66]: Veriler Excel’ e aktarılır. 

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır. 

Alt Modül Tanımlama ekranında gridde Modül Tanım alanına ilgili Modülün adı yazılarak Alt Modül Tanımları aratılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_642.png)

İlgili Modül tanımları aratıldıktan sonra Modül Tanımı seçili iken   ![ref114]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_643.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alt Modül No:** Alt Modül Tanımlama ekranında Alt Modül No bilgisinin sistem tarafından verildiği alandır.

**Alt Modül Tanımı:** Alt Modül Tanımlama ekranında Alt Modül Tanımı bilgisinin sistem tarafında verildiği alandır.İlgili alan üzerinde değişiklik ve düzenleme işlemine sistem izin verir.

**Akış Tanımı:** Alt Modül Tanımlama ekranında Akış Tanımı bilgisi açılır  liste tıklanarak açılan Akış Tanımı listesinden seçildiği alandır. (Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Akış Tanımlama menüsünde tanımlı Akış Tanımlarından tanımlı gelmektedir.)

**Onay Talep Mesajı:** Alt Modül Tanımlama ekranında Onay Talep Mesajı bilgisi açılır Onay Talep Mesajı listesinde seçildiği alandır. (Mesaj Gövdesi listesi Sistem Altyapı Tanımları/BSAT/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde tanımlı olarak gelmektedir.)

**Onay Tamam Mesajı:** Alt Modül Tanımlama ekranında Alt Modül Tanımlama ekranında Onay Tamam Mesajı bilgisi açılır Onay Tamam Mesajı listesinde seçildiği alandır. (Mesaj Gövdesi listesi Sistem Altyapı Tanımları/BSAT/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde tanımlı olarak gelmektedir.)

**Onay Ret Mesajı:** Alt Modül Tanımlama ekranında Alt Modül Tanımlama ekranında Onay Ret Mesajı bilgisi açılır Onay Ret Mesajı listesinde seçildiği alandır. (Mesaj Gövdesi listesi Sistem Altyapı Tanımları/BSAT/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde tanımlı olarak gelmektedir.) 

**Onaycı Başlatan İse Onay Aşaması Geçilmesin:** Alt Modül Tanımlama ekranında “Onaycı Başlatan İse Akış Geçilmesin” ilgili check box  işaretlendiği takdirde, eğer sisteme veri girişi yapıp onaya gönderen personel onaycının kendisi ise onay sürecini atlamada akış sürecini devam ettirerek bir sonraki basamağa geçmesini sağlayan alandır.

Alt Modül tanımlama menüsüne geldikten sonra ilgili modül tanımı üzerinde ![ref115]  butonuna tıklanarak akış tanımı, onay talep mesajı, onay tamam mesajı, onay red mesajı ilişkilendirmeleri yapılmaktadır. “Onaycı Başlatan İse Akış Geçilmesin” kutucuğu işaretlendiği takdirde, eğer sisteme veri girişi yapıp onaya gönderen personel onaycının kendisi ise onay sürecini atlamada akış sürecini devam ettirerek bir sonraki basamağa geçmesini sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_645.png)
#### **5.2.8. Rol Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama

Modüllerde kullanılan onay akışları için onaycı olarak hangi role gideceği bilgisinin tanımlandığı menüdür. Sistemde her modül için rol tanımları mevcuttur. Gerekli görüldüğü durumlarda risk modülleri, olay modülleri gibi modüller için yeni rol tanımlamaları yapılır.  Roller değiştirilmek istenildiğinde ya da yeni bir rol tanımlanmak istenildiğinde Bimser Çözüm Ekibinden destek alınabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_646.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref85]: Yeni bir rol tanımı yapılır.

![ref115]: Listede seçili olan rol bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır.

![ref87]: Listede seçili olan rol bilgisi silinir.

![ref99]: Veriler Excel’ e aktarılır. 

![ref100]: Kayıtlar filtrelenerek arama yapılır.

![ref116]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref102]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Rol Tanımlama ekranına yeni bir Rol eklemek için ekranın sağ üst köşesindeki ![ref85]  butonuna tıklanarak Rol Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_648.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Modül:** Rol Tanımlama - Yeni Kayıt ekranında modül bilgisi modül alanında açılır modül listesinde seçildiği alandır. Rol Tanımlaması yapılacak modül için bu alanda modül seçimi yapılır.

**Rol No:** Rol Tanımlama - Yeni Kayıt ekranında tanımlanacak rolün Rol No bilgisi sistem tarafından otomatik verildiği alandır.

**Rol Tanımı:** Rol Tanımlama - Yeni Kayıt ekranında  Rol tanım bilgisinin tanımlandığı  alandır.

**Bulma Yöntemi:**	Rol Tanımlama - Yeni Kayıt ekranında tanımlanacak rolün SQL sorgusu bilgisi girildiği alandır.Tek bir kullanıcıya gidecek şeklinde SQL Sorgusu;

**SELECT SICIL\_NO FROM BSAT001 WHERE SICIL\_NO='makcay'**  tırnak işaretleri içerisine personelin sicil numarası bilgisi yazılır. (Personellerin Sicil no bilgisi Sistem Altyapı Tanımları/BSAT/Tanımlar/Personel Tanımlama menüsünde alınır.)

Bir kullanıcı grubu gidecek şeklinde SQL sorgusu;

**SELECT SICIL\_NO FROM BSAT009A WHERE GRUP\_KODU='001'** tırnak işaretleri içerisine Kullanıcı Grubu kodu bilgisi yazılır.(Kullanıcı Grubu kod bilgisi Sistem Altyapı Tanımları/BSAT/Tanımlar/Kullanıcı Grubu Tanımlama menüsünde alınır.)

Bimser Destek Ekibinden farklı SQL sorgusuna bağlı roller tanımlamak için destek alınması sağlanır.	

**Rol Tipi:** Rol Tanımlama - Yeni Kayıt ekranında tanımlanan rolün tipinin açılır Rol tipi seçeneklerinde seçim yapıldığı alandır.		

**Not:** Rol Tanımlama - Yeni Kayıt ekranında tanımlanan Rol tipi ile ilgili varsa not bilgisinin girildiği alandır.	

Rol Tanımlama -Yeni kayıt ekranında  gerekli alanlar doldurarak ekranın sol üst köşesindeki  ![ref117]  butonu tıklanarak Rol Tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_650.png)

Tanımlama ekranında  Filtre sekmesinde Modüller alanında açılır modül listesinde modül seçilir ve ![ref100] (Ara) butonu tıklanılarak arama kriterine göre filtreleme işlemi yapılır.Seçilen Modül ilgili sistemde tanımlı Rol Tanımları ekranda görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_651.png)
#### **5.2.9. Akış Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama

Modüllerde kullanılan onay akışlarının tanımlamaları yer almaktadır. Sistemde her modül için akış tanımı mevcuttur. Gerekli görüldüğü durumlarda risk modülleri, olay modülleri gibi modüller için yeni akış tanımlamaları yapılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_652.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref85]: Yeni bir akış tanımlaması yapılır.

![ref86]: Listede seçili olan akış bilgisi üzerinde  düzeltme/ değişiklik/ güncelleme yapılır.

![ref87]: Listede seçili olan akış bilgisi silinir.

![ref66]: Veriler Excel’ e aktarılır. 

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Örneğin: İSG Risk değerlendirme modülünde “İSG Risk Değerlendirme Onay Akışı” düzenleme yapılmak istenilirse;

Akış Tanımlama ekranında  Filtre sekmesinde Modüller alanında açılır Modül listesinde ilgili “İSG Risk değerlendirme “Modül seçilir ve ![ref65] (Ara) butonu tıklanılır. Akış Tanımlama ekranında Liste sekmesinde  ![ref65] (Ara) butonu tıklandıktan sonra ilgili Modülle ilgili sistemde tanımlı varsa akışlar listelenir. Genelde Risk Modülllerinde akışlar kullanıcı tarafından tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_653.png) Akış Tanımlama ekranına yeni bir yeni bir akış  eklemek için ekranın sol üst köşesindeki ![ref85] butonuna tıklanarak Akış Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_654.png)

**Ekranda butonlar yardımıyla;**

![ref118] : Rol eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_656.png): Listede seçili eklenen rol silinir.

Akış Tanımlama- Yeni Kayıt ekranında ![ref118]  butonuna tıklandığında  ilgili modülle ilgili sistemde tanımlı olan rollerin listesi görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_657.png)

Tanımlanan akışın gideceği uygun olan rol listeden seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_658.png)  butonu tıklanarak akışa eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_659.png)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Modül:** Akış Tanımları - Yeni Kayıt ekranında açılır liste tıklanarak açılan modül listesinde akışın tanımlanacağı modül seçilir.	  

**Akış No:** Akış Tanımları - Yeni Kayıt ekranında tanımlanan akışının no bilgisinin sistem tarafında verildiği alandır.   

**Akış Tanımı:** Akış Tanımları - Yeni Kayıt ekranında tanımlanan akışının adının yazıldığı alandır.	  

**Akış Tanımlama Onaylama İşlemi :** Görselde yer aldığı şekliyle " ISG Risk Değerlendirme Onay Akışı” onaya gidecek kişi “ISG Risk Değerlendirme Uzmanı” roldeki kişidir. Birden çok Akış onaycısı tanımlanabilir. Ekranda sıra numarası onaycının kaçıncı sırada onay vereceğini belirtir.  Onayacı Sayısı alanında onay verecek kişi sayısı belirlenir. Onay akışında onaydaki rol bir kullanıcı grubuna gidiyorsa “0” onaycı sayısında tüm kullanıcı grubundaki grup üyelerinin onaylama işlemi yapmak zorundadır. Onaycı Sayısı alanında şayet belli bir sayısal değer belirtildiğinde kullanıcı grubundaki o sayısal değer kadar kişinin onayına gitmesi gerekir. Kullanıcı grubu için Onaycı sayısı örneğin “2” olarak belirtilmişse ise gruptaki “2” iki kişinin onay vermesi gerekir. Roldeki bir kullanıcı ise “0” sayısının bir hükmü olmaz sadece roldeki kişiye akış onaya gider. Doküman Yönetimi modülünde onay matrisinde onaylama işleminde olduğu  gibi Akış tanımlama bu kısım aynı şekilde çalışmaktadır. 

Sıra No alanında birden fazla onaycı olur. “0” sıfır son onaycıdır. Onay akışı ters mantıkla çalışmaktadı. Sıra No kısmında 0,1,2,  şeklinde ise onay sıralama 2 den başlayıp “0” doğru gider.

1\.Görselde akışa eklenen sadece ilgili role akış onaya gider.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_660.png)

2\. Görseldeki akışa eklenen  role onay gider.Onaycı sayısı “0” olmasının hükmü yoktur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_661.png)

3.Görseldeki akışa eklenen kullanıcı grubundaki onaycı sayısı “0” olduğunda tüm grup üyelerine onaya gider. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_662.png)

4\. Görseldeki akışa eklenen  kullanıcı grubundaki onaycı sayısı “3” olduğunda tüm grup üyelerine sadece 3 kişinin onayı gitmesi yeterlidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_663.png)

5\.Görseldeki akışa eklenen roller onaycı sayısı alanında ilk olarak “1”. onaycıdan onay işlemi başalayarak “0”. onaycıya doğru akışının onay akışı devam eder.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_664.png)

6\.Görselde akış eklenen role aynı anda onay gider. Belli bir sıralama yoktur. Onaylama işlemi için istenilen rolden başlanır. Paralel onay işlemidir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_665.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_666.png)

Açılan Akış Tanımlama- Yeni Kayıt ekranın gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref117]  butonu tıklanarak Akış tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_667.png)
#### **5.2.10. Rapor Formatları Düzenleme**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme

Modüllerde yer alan raporların rapor formatları şablonları ile  gerekli düzenlemelerin yapıldığı, yeni rapor formatları şablonların eklendiği, yüklenen rapor formatları şablonlarının görüntülendiği ve istenirse yüklenen rapor formatları şablonlarının  silindiği  menüdür. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_668.png)

**Ekranda bulanan butonlar yardımıyla;**

![ref119]: Sisteme yeni bir rapor formatı şablonu yüklenir.

![ref120]: Listede seçili olan rapor formatı şablonu görüntülenip, indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_671.png): Listede seçili olan rapor formatı şablonu silinir.

Varsayılan rapor Formatlarının Düzenlemesi ekranında sisteme yeni bir rapor formatı eklemek için ![ref119]  butonuna tıklanır. Dosya Yükleme ekranında Gözat butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_672.png)

Açılan ekranda sisteme yüklenmek istenilen rapor formatı şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_673.png)

Varsayılan Rapor Formatlarının Düzenlemesi ekranında seçilen rapor formatı yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_674.png)

Listede seçili Rapor formatı şablonu seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_675.png)  butonu tıklanarak rapor formatı şablonu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_676.png)

Rapor Formatı şablonun alanlarının karşılığında < \> işaretleri şeklinde tagler mevcuttur. Rapor formatı şablonu sistem yüklendiğinde ve ilgili raporu bulunduğu menüden rapor  alındığında ilgili tagler çalışarak alanların karşılığında girilen alan bilgisi verir. Örneğin: Denetim Planı Rapor formatı şablonunda  Plan No karşılığında <PLAN\_NO\> alanın tag yazıldığında plan no bilgisi sistemde alınan Denetim Planı raporuna basılır.

Qdms sisteminde sistemde mevcut Rapor formatı şablonu üzerinde düzenleme işlemi yapıldığında raporun sistem yükleme işleminde dikkat edilmesi gereken husus rapor formatı şabonun rapor formatları düzenleme menüsünde yüklü adı ve uzantısı aynı şekilde olacak şekilde yüklemek gerekir. Böylece sistemde değişiklik yapılan rapor formatının yerine, oluşturulan yeni rapor formatı tanımlanmış olur.Kullanıcılar rapor formatını bu menüden  ![ref120]butonu ile indirip, istedikleri şekilde düzenleme yapıp tekrar ![ref119] butonu tıklayarak rapor formatını aynı adı ve uzantısı ile sistem yükleme işlemi yapabilir.






#### **5.2.11. Vekalet Görüntüleyici**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Vekalet Görüntüleyici

Sistemde gerçekleştirilen vekalet işlemlerinin görüntülendiği, takibinin yapıldığı menüdür.Vekalet veren, vekalet alan, vekalet işlemini gerçekleştiren, vekalet başlangıç-bitiş tarihleri, vekalet işlem tarihi, vekalet verilen modüller ve vekalet durum bilgisinin görüntülendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_677.png)

**Ekranda bulanan butonlar yardımıyla;**

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref66]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.


Vekalet Görüntüleyici ekranında Filtre sekmesinde  Vekalet, Vekalet veren, vekalet alan, vekalet gibi alanlara  veri girilip, ![ref65] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_678.png)

#### **5.2.12. Dil Ayarları**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları 

Dil ayarları menüsünden QDMS üzerinde görülen menülerin isimleri, alanların isimleri değiştirilebilir. Modüllere yeni alanlar eklenebilir. Var olan alanların zorunluluk durumları düzenlenebilir. Alanların ekran üzerinde göründükleri sıralama değiştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_679.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref86]: Listede seçili alan bilgisi üzerinde değişiklik yapılır.

![ref66]: Veriler Excel’ e aktarılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

**Başlıklar Sekmesi;**

Başlıklar sekmesinde ilgili modül seçilerek modül ile ilgili pasif alanlar varsa parametrik alan tanımlama işlemi yapılır. Bu sekmede metin, metin(çoklu satır), liste, tarih gibi parametrik alan tipleri tanımlama, tanımlı parametrik alan adı üzerinde düzenleme ve tanımlı parametrik alanı kaldırma işlemleri yapılır.Mevcut bir alan değiştirilmek istenildiği zaman  Başlıklar sekmesinde gridde TR kısmı türkçe dil karşılığı yada Adı alanına label kod bilgisi yazılarak  seçilir. Dil Ayarlarında  mevcut alanların label kodları modüllere göre değişkenlik göstermektedir. DÖF, IMS ve DMS modüllerinde label kodları modülleri kapsamında yer alan sekmelere göre değişkenlik göstermektedir. Bu modüllerde ilgili label kodunun ait alanın hangi sekmede yer aldğı aşağıdaki şekilde olmaktadır.

|Label Koda ve kısaltmasına göre|<p>Örnek Label Kod</p><p>(DÖF Modülü metin tipli parametrik alan)</p>|<p>Örnek Label Kod</p><p>(MS Modülü metin tipli parametrik alan)</p>|Görüldüğü Sekme(IMS,DMS, DÖF)|
| - | - | - | - |
|lblPARAM|lblPARAM1|lblPARAM1|DÖF modülünde diğer bilgiler sekmesi, müşteri şikayetleri modüllerinde Şikayet Detayı Diğer Alanlar |
|lblG\_|lblG\_Param1|lblG\_Param2|Gelişme Raporu|
|lblKOK\_|lblKOKPARAM1|lblKOKPARAM1|Kök Nedenler|
|lblA \_|lblA\_Param1|lblA\_Param1|Aksiyonlar|
|lblS\_|lblS\_Param1|lblS\_Param3|Sonuç Raporu|
|lblK\_|lblK\_Param1|lblK\_Param3|Kapatma|

Doküman Yönetim modülünde ise “ALAN” ifadesi label kodlarında kullanılmaktadır.Ör: Diğer bilgiler sekmesinde görünülenen  lblALAN2 metin tipli parametrik alan gibi. Doküman Yönetim modülünde Kalite Kayıtları görüntüleme sekmesinde lblKK\_PARAM1 label kodu ile ilgili alan görüntülenir.

İlgili alan seçilerek değişiklik (isim değişikliği, zorunluluk durumu vb.)  yapılacak alan ![ref86] butonuna ile açılır. Açılan ekranda değiştirilmek istenilen kısımlar değiştirilerek kaydedilir.  

İlgili Modülde Mevcut parametrik alan tiplerini listesini görüntülemek için gridde Tipi alanında parametrik alan tipi adı yazılarak aratılır.Ör: Doküman Yönetimi Modülünde liste tipli parametrik pasif alanlar.Diğer Doküman Yönetim modülünde parametrik alanlar aynı şekilde aratılarak listesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_680.png)

Örnek olarak; Doküman Modülünde Diğer Bilgiler sekmesinde Liste tipli bir alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil ayarları menüsü açılır.Açılan ekranda modüller listesinde modül olarak Doküman Yönetimi Modülü seçilir ve dil tanımlamaları listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_681.png)

Dil Ayarları ekranında Başlıklar sekmesinde tanımlanacak parametrik alan tipi gridde tipi alanına Tipi  yazılarak, parametrik alan tipi ile ilgili pasif alanlar listelenir. Ör:Doküman Yönetimi modülünde liste tipli alan.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_682.png)

Tanımlanacak Liste tipli alan seçilerek ![ref121] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_684.png)

Açılan Dil ayarların ekranında tanımlanacak liste tipli alanın Adı alanında tanımlanacak liste tipli alanın adı yazılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_685.png)

Dil ayarların ekranında liste tipli alanın 1. liste elemanlarını tanımlamak için ![ref122] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_687.png)

Açılan Dil Ayarları-Yeni Kayıt ekranında liste elemanın ID değeri ve Değer alanın liste elemanın tanım bilgileri yazılarak ekranın sol üst köşesindeki ![ref117]  butonu  tıklanarak 1.liste elemanı kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_688.png)

Dil ayarların ekranında liste tipli alanın 2. liste elemanlarını tanımlamak için ![ref122]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_689.png)

Açılan Dil Ayarları-Yeni Kayıt ekranında liste elemanın ID değeri ve Değer alanın liste elemanın tanım bilgileri yazılarak ekranın sol üst köşesindeki ![ref117]  butonu  tıklanarak 2.liste elemanı kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_690.png)

Dil ayarları ekranında liste elemanlarının tanımlama işleminden sonra ilgili bayrakların bulunduğu kısımda tanımın istenirse dil karşılığı, alanın zorunlu olup, olmaması, gridde gösterilip, gösterilmemesi varsa başlık notu bilgisi yazılması  ile ilgili  işlem adımları yapılır. Gerekli alanlar ilgili bilgiler girildikten sonra ekranın sol üst köşesindeki ![ref123] butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_692.png)

Tanımlanan alanın görüntülenmesi için Doküman Yönetimi modülünde Entegre Yönetim Sistemi/Doküman Yönetimi/Doküman Hazırlama menüsü tıklanılır.

Açılan Doküman Hazırlama - Klasör Seçme ekranında  liste sekmesinde listeden doküman hazırlanacak klasör seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_693.png) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_694.png)

Açılan Yeni Doküman ekranında Diğer bilgiler sekmesinde dil ayarlarında tanımlanan liste tipli parametrik alan görüntülenir. Mouse üzerine gelindiğinde başlık notu bilgisi, zorunlu alan olduğu ve açılır liste tıklanarak liste elemanları seçenekleri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_695.png)**Dil Ayarlarında Tanımlanan Alanın kaldırılması;**

Doküman Yönetimi modülünde tanımlanan liste tipli parametrik alanın kaldırılması işlemi için dil ayarları ekranında Başlıklar sekmesinde  gridde liste tipli parametrik alanın biliniyorsa label kodu  veya adı bilgilesi  yazılarak görüntülenerek seçilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_696.png)

Liste tipli parametrik alanın seçilme işleminden sonra ![ref121] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_697.png)

Açılan Dil Ayarları ekranında tanımlanan liste tipli alanın adı, başlık notu bilgisi silinir. 2. Liste elemanları seçilerek ![ref124]butonu tıklanarak 2.liste tipli alanın liste elemanın silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_699.png)

1\. Liste elemanları seçilerek ![ref124] butonu tıklanarak liste tipli alanın 1.liste elemanın silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_700.png)

Gerekli alanlar ilgili bilgiler ve liste elemanların silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_701.png)

İşlem adımlarından sonra ekranın sol üst köşesindeki ![ref123] butonu tıklanarak liste tipli parametrik alanın silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_702.png)

**Tanımlanan parametrik tipli alanın label kod bilgisinin görüntülenmesi**

DÖF İşlemleri- Yeni Kayıt ekranında Diğer Bilgiler sekmesinde tanımlı metin tipli parametrrik alanın üzerinde sağ tıkla yönetimi ile açılan açılır listede “İncele” seçeneği tıklanarak tanımlı metin tipli parametrik alanın label kod bilgisine ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_703.png)

Açılan ekranda tanımlanan parametrik metin tipli alanın label kodu görüntülenir. Ürünün Lot Numarası metin tipli parametrik alanın label Kod bilgisi “lblPARAM1” ekran görütünde görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_704.png) Bu şekilde Qdms sisteminde ilgili modüllerde tanımlı parametrik alan tiplerinin label kod bilgisine ulaşılaşılır.



**Tablolar Sekmesi;**

Bu sekmede Dil Ayarların menüsünde İlgili modül seçilerek modülün sistemde tanımlı sekmelerini adı bilgisi üzerinde düzemleme ve değiştirilme işlemi yapılır. Tablo sekmesinde sekmenin  kısa kod ismi  seçilerek ![ref125] butonu tıklanarak değiştirilir. Örneğin: DÖF modülünde Gelişme Raporu sekmesi Acil Önlem Raporu sekmesi olarak Tablolar sekmesinde değiştirilmesi işlemi için pcDOF   tablosunda açılır liste  butonu ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_706.png) tıklanarak DÖF modülündeki sekmelerin listesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_707.png)

DÖF modülü sekme listesinde tabGelisme sekmesi seçili iken Değiştir butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_708.png)

Açılan Dil Ayaraları ekranında Gelişme Raporu sekmesinin değeri alanındaki adı Acil Önlem Raporu değiştirilir.İlgili bayrakların bulunduğu alanlarda varsa sekmenin  dil karşılığı  yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_709.png)

Gerekli alanlar ilgili bilgilerde düzenleme işleminde sonra ekranın sol üst köşesindeki ![ref123]  butonu tıklanarak Dil Ayarları kayıt güncelleme  işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_710.png)

Tablolar sekmesinde PcDÖF alanı kısmında DÖF modülünün Gelişme Raporu sekmesinin adının değiştirildiği görüntülemek için Gelişme raporu aşamasındaki bir DÖF Kaydı açılır. Açılan DÖF kaydında Gelişme Raporunun Dil ayarları menüsünde yapılan değişikliğe göre adının değiştiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_711.png)
**Butonlar sekmesi;**

Bu sekmede Dil ayarları menüsünde Modüller alanında ilgili Modül seçilerek Modülle ilgili sistemde tanımlı buton seçilerek buton isimleri ihtiyaç dahilinde değiştirilmesi ve düzenleme işlemi yapılır. Butonlar sekmesinde ilgili modül seçildiğinde sistemde tanımlı modülle ilgili buton isimleri listenir. Ör:Modül alanında Aksiyon Yönetimi modülü seçilerek Qdms kapsamında Aksiyon Modülü ile İlgili butonlar listenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_712.png)

Sistem Altyapı Tanımları/Aksiyon/Aksiyon Gerçekleştirici Değiştiri menüsündeki “Değiştir” butonun değiştirilme işlemi bu menüde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_713.png)

Aksiyon Yönetimi Modülünde “Değiştir” butonu seçilerek ![ref126] butonu tıklanarak içeriği görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_715.png)

Açılan Dil Ayarları ekranında “Değiştir”  butonun adı “Güncelle” olarak değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_716.png)

Dil Ayarları ekranında yapılan değişiklikten sonra ekranın sol üst köşesindeki ![ref123] butonu tıklanarak dil ayarları kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_717.png)

Dil ayarlarından buton isminin değişikliğinden sonra yapılan değişikliğin menüde görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_718.png)

**Meajlar Sekmesi;**

Bu sekmede Dil ayarları menüsünde Modüller alanında ilgili Modül seçilerek Modülle ilgili sistemde tanımlı mesaj tanımları listelenir ve listenen bu mesajlar bilgisi seçilerek ![ref126]  butonu tıklanarak üzerinde  düzenleme ve değiştirme işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_719.png)

Ör: Aksiyon Yönetimi Modülünde Aksiyon Kaynağı Tanımlama ekranında listeden seçili bir Aksiyon Kaynağı silme işleminde yanlış yazılmış  mesajın düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_720.png)

Dil Ayarlarında  Qdms Sisteminde silme işlemi  yapılırken görüntülenen  yanlış yazılmış mesajın içeriğinin değiştirmek için Dil Ayarlarında modül alanında Aksiyon  modülü seçilir ve Aksiyon modülü ile ilgili mesaj listesi görüntülenir. Mesajlar sekmesinde değiştirilmek istenilen mesaj seçilir ve ![ref126]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_721.png)

Açılan Dil Ayarları ekranında Değeri alanında mesaj bilgisi üzerinde istenildiği şekilde düzenleme işlemi yapılarak yanlış mesaj içeriği düzeltilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_722.png)

Dil Ayarları ekranında gerekli düzenleme işleminde sonra  ekranın sol üst köşesindeki ![ref123]  butonu tıklanarak Mesaj kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_723.png)

Aksiyon Kaynağı Tanımlama ekranında listede seçili kaydı ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_724.png)  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_725.png)

Aksiyon Tanımlama ekranında  silinme işlemi yapılırken düzenleme işlemi yapılan mesaj bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_726.png)

Bu şekilde Dil ayarları ekranında mesajlar sekmesinde ilgili modülde ilgili modül seçilerek ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_727.png)  butonu tıklanarak seçili mesaj bilgisi üzerinde düzenleme , değişiklik ve yanlış yazılmışları mesajları düzeltme işlemi yapılır.

Qdms sisteminde bu şekilde kullanıcılar isterler ise Dil Ayarları ekranında mesajları sekmesinde ilgili modülde modülle ilgili mesaj bilgisi seçilerek ekranın sağ üst köşesindeki ![ref127]  butonu tıklanarak mesaj bilgisi üzerinde değişiklik ve düzenleme işlemi  yapılır.  Genelde yanlış yazılmış mesajların düzenleme işlemi yapabilirler.

**Hata Mesajları Sekmesi;**

Bu sekmede Dil ayarları menüsünde Modüller alanında ilgili Modül seçilerek Modülle ilgili sistemde tanımlı hata mesaj tanımları listelenir ve listenen bu hata mesajlar bilgisi seçilerek ![ref126]  butonu tıklanarak üzerinde  düzenleme ve değiştirme işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_729.png)

Qdms Ana giriş ekranında Kullanıcı adı ve parola bilgisi yazıldığında görüntülenen hata mesajı aşağıdaki şekildedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_730.png)

Bu hata mesajında düzenleme ve değiştirme işlemi yapmak için Dil ayarları ekranında   modül olarak Sistem Altyapı Tanımları modülü seçilerek Hata mesajları sekmesi tıklanarak listelenen Hata mesajları listesinde değiştirilmek istenilen hata mesajı seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_731.png) Hata mesajı seçili iken ![ref127]  butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_732.png)

Açılan Dil Ayarları ekranında Değeri alanında Hata mesajının adı bilgisi üzerinde değişiklik ve düzenleme işlemi yapılarak ekranın sol üst köşesisinde yer alan ![ref128]  butonu tıklanarak dil ayarları kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_734.png)

Qdms Ana giriş ekranında kullanıcı adı ve parola bilgisi girildikten sonra Dil Ayarları ekranında Hata mesajları sekmesinde listede seçili mesaj bilgisi üzerindeki yapılan değişiklik görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_735.png)

Qdms sisteminde ilgili  modüllerde Dil Ayarları Menüsünde Hata mesajları sekmesinde bulunan Hata mesajların sistemden uyarı mesajı şeklinde görüntülendiği Hata pop-up’larının başlığına uygulamanın versiyon bilgisinin yazılması sağlandı. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_736.png)

Qdms sisteminde bu şekilde kullanıcılar isterler ise Dil Ayarları ekranında Hata mesajları sekmesinde ilgili modülde modülle ilgili hata  mesaj bilgisi seçilerek ekranın sağ üst köşesindeki ![ref127]  butonu tıklanarak hata mesaj bilgisi üzerinde değişiklik ve düzenleme işlemi  yapabilirler. 

**Radyo Butonlarlar Sekmesi;**

Dil ayarları menüsünde Modüller alanında ilgili Modül seçilerek Modülle ilgili sistemde tanımlı Radyo Butonlarının tanımları değiştirilir. Radyo butonları  sekmesinde ilgili modül seçildiğinde sistemde tanımlı modülle ilgili Radyo Butonları tanımları listenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_737.png)

Örnek olarak Aksiyon Yönetimi modülünde Aksiyon Türü alanında işaret Radyo butonları alanları üzerinde düzenleme işlemi yapılır.Aksiyon Kalemi  Planlama-Yeni Kayıt ekranında Aksiyon Türü alanında Radyo Butonları alanları ekran görüntüsündeki gibidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_738.png)

Dil Ayarları ekranında Radyo butonları sekmesinde ilgili alanla ilgi radyo butonların isimleri değiştirmek için “rpAksiyonTuru” alanı önündeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_739.png)buton tıklanarak radyo butonlarının alanlarının seçenekleri görüntülenir. Radyo butonları sekmesinde  değiştirilmek istenilen radyo butonu alanı seçili iken ![ref127] (Değiştir ) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_740.png)

Açılan Dil Ayarları ekranında Değeri  alanında değiştirilmek istenilen radyo butonun    karşılığı olan alanın adı bilgisi üzerinde düzenleme ve değiştirme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_741.png)

Dil Ayarları ekranında radyo botunun karşılığı olan alan üzerinde yapılan değişiklikten sonra ekranın sol üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_742.png) butonu tıklanarak dil Ayarları kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_743.png)

Aksiyon Kalemi Planlama-Yeni Kayıt ekranında Aksiyon Türü alanında Dil Ayarlarında Radyo butonları sekmesinde Aksiyon Yönetimi Modülü ile ilgili “rpAksiyonTuru” alanında Aksiyon türü ile ilgili radyo butonunda değiştirildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_744.png)

Qdms sisteminde bu şekilde kullanıcılar isterler ise Dil Ayarları ekranında Radyo Butonları  sekmesinde ilgili modülde modülle ilgili Radyo butonlarının karşılığı olan alanları seçilerek  ekranın sağ üst köşesindeki ![ref127]  butonu tıklanarak radyo butonları alanları bilgisi  üzerinde değişiklik ve düzenleme işlemi  yapabilir.

**İşaret Kutuları Sekmesi;**

Dil ayarları menüsünde Modüller alanında ilgili Modül seçilerek Modülle ilgili sistemde tanımlı İşaret Kutuları tanımları değiştirilir. İşaret kutuları sekmesinde ilgili modül seçildiğinde sistemde tanımlı modülle ilgili İşaret Kutuları tanımları listenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_745.png)

Departman Tanımlama -Yeni Kayıt ekranında Üst departman alanında ![ref129] (Seç) butonu tıklanarak açılan Departman Seç ekranında  Filtre sekmesinde İşaret Kutusu alanı “Alt departmanları da seç” alanı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_747.png)

Görüntülen “Alt departmanları da seç” bu işaret kutusu alanı Dil Ayarlarında İşaret Kutuları sekmesinde listelenen  işaret kutuları listesinde seçilerek ![ref127] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_748.png)

Açılan Dil Ayarları ekranında Adı alanın işaret kutusunun karşılığı olan alanın adı bilgisi üzerinde değişiklik ve düzenleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_749.png)

Dil Ayarları ekranında Değeri alanında işaret kutusunun karşılığı olan alanın adı bilgisi değiştirildikten sonra ekranın sol üst köşesindeki ![ref128] butonu tıklanarak Dil Ayarları kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_750.png)

Departman Tanımlama-Yeni Kayıt ekranında Üst departman alanında ![ref129] (Seç) butonu tıklanarak açılan Departman Seç ekranında Filtre sekmesinde Dil Ayarları ekranında İşaret kutuları sekmesinde  işaret kutusunun karşılığı olan alan üzerinde yapılan değişiklik görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_751.png)

Qdms sisteminde bu şekilde kullanıcılar isterler ise Dil Ayarları ekranında İşaret kutuları sekmesinde ilgili modülde modülle ilgili İşaret kutuları karşılığı olan alanları seçilerek  ekranın sağ üst köşesindeki ![ref127]  butonu tıklanarak İşaret kutuları alanları bilgisi  üzerinde değişiklik ve düzenleme işlemi  yapabilirler.

**İşlem Tipleri Sekmesi;**

Dil ayarları menüsünde Modüller alanında ilgili Modül seçilerek Modülle ilgili sistemde tanımlı İşlem Tipleri tanımları değiştirilir. İşlem Tipleri sekmesinde ilgili modül seçildiğinde sistemde tanımlı modülle ilgili İşlem Tipleri tanımları listenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_752.png)

Ör: İşlem Tipi olarak Entegre Yönetim Sistemi/Doküman İşlemleri/Doküman İptal menüsünde ilgili işlem tipi değiştirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_753.png)

Dil Ayarları ekranında İlgili modülle ilgili işlem Tipi değiştirilmek istendiğinde modül listesinde modül seçilerek İşlem tipi sekmesi tıklanılırak işlem tipleri listesi listenir. Listelenen işlem tiplerinde değiştirilmek istenilen işlem tipi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_754.png)  butonu tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_755.png)

Açılan Dil Ayarları ekranında Değeri alanında değiştirilmek istenilen işlem tipinin bilgisi değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_756.png)

Dil Ayarları ekranında işlem tipi ile gerekli düzenleme işlemi yapıldıktan sonra ekranın sol üst köşesindeki ![ref128]  butonu tıklanarak Dil ayarları kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_757.png)

Entegre Yönetim sistemi /Doküman İşlemleri /Doküman İptal İşlemi menüsünde  Dil Ayarları ekranında İşlem tipi sekmesinde düzenleme  yapılan işlem tipi üzerindeki değişiklik  görüntülenir. “Doküman İptal – Klasör Seçme” ekranın da yapılan değişiklikten sonra “Doküman İptal İşlemi- Klasör Seçme” olarak değiştiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_758.png)

**Menü Sekmesi;**

Dil ayarları menüsünde Qdms sistemde Entegre Yönetim Sistemi ve Sistem Altyapı Tanımları kısımlarında tanımlı Modüllerin ve modüllerle ilgili menü isimlerimleri listesinin bulunduğu sekmedir. Bu sekmede Qdms sistemde Entegre Yönetim Sistemi ve Sistem Altyapı Tanımları kısımlarında bulunan modül ve modüllerin kapsamında menüler isimleri seçilerek ![ref130]  butonu tıklanarak modül ve modül kapsamında menülerin isimlerin değiştirme ve düzenleme işlemi yapılır. Ayrıca bu sekmede Qdms sisteminde Entegre Yönetim Sistemi ve Sistem Altyapı Tanımları kısımlarında hangi sıralamada  yer alacağı bilgisi değiştirilme işlemide yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_760.png)

Menü sekmesinde değiştirilmek istenilen modül ismi seçilerek ![ref130]  butonu tıklanılır. Ör: Doküman İşlemleri Modülü seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_761.png)

Açılan Dil Ayarları ekranında değeri alanın yeni adı bilgisi yazılır ve gerekli alanlar üzerinde düzenleme işlemi yapıldıktan sonra ekranın sol üst köşesindeki ![ref131]  butonu tıklanarak Dil ayarları kayıt güncelleme işlemi  yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_763.png)

Menü sekmesinde ilgili modüllerin Entegre Yönetim Sistemi ve Sistemi Altyapı Tanımları   kısmında  menülerin sıralama yapılarak hangi sırada görüntüleceği ayarlaması bu sekmede yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_764.png)Menü sekmesinde ilgili modüldeki menüler seçilerek sıra no alanındaki sıralama numarası değiştirilerek menülerin ilgili kısımda bulunma sıralama değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_765.png)

Dil Ayarları ekranında sıra no alanında menünün sıra numarası değiştirildikten sonra ekranın sol üst köşesindeki ![ref131]  butonu tıklanarak dil ayarları kayıt güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_766.png)
#### **5.2.13. Pozisyon Kodu Değiştirme**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Pozisyon Kodu Değiştirme

Personellerin pozisyon kodları yanlış girilmiş olabilir veya değiştirilme ihtiyacı hissedilebilir. Böyle bir durumda pozisyon kodu değiştirme fonksiyonu kullanılır. Eski pozisyon kodu yazılır, yeni verilecek pozisyon kodu da yazılarak ![ref132]  butonuna tıklanarak pozisyon kodu değiştirme işlemi yapılır.  Bu menü ile pozisyon kodları tek tek manuel olarak değiştirilme işlemi yapılır. HR programı kullanan firmalarda yeni başlayan personellere yeni pozisyon kodları verilmektedir. Entegrasyon ile personel sisteme aktarıldıktan sonra, yeni personel için devraldığı pozisyonun kodu bu menüden değiştirilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_768.png)

**Ekranda bulanan butonlar yardımıyla;**

![ref133]: Pozisyonu kodu değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_770.png)

**Eski Pozisyon Kodu:** Pozisyon Kodu Değiştir ekranında sistemde tanımlı pozisyon kodu bilgisinin yazıldığı alandır. (Sistem Altyapı Tanımları/Tanımlar/ Pozisyon Tanımlama menüsünde pozisyon kodu bilgisi alınır)

**Yeni Pozisyon Kodu:** Pozisyon Kodu Değştir ekranın yeni pozisyon kodu bilgisinin  yazıldığı alandır.

Pozisyon Kodu değiştir ekranında Eski Pozisyon Kodu alanına değiştirilmek istenilen pozisyon kodu yazılır. Yeni Pozisyon Kodu alanı pozisyona verilecek yeni kod bilgisi yazılır. ![ref133] butonuna tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_771.png)

Pozisyon Kodu Değiştir ekranında sistem tarafında verilen “Pozisyon Kodunu değiştirmek istediğinize emin misiniz?”  uyarı mesajında “Tamam” butonu tıklanılır. Qdms sistemi tarafından pozisyon kodunun değiştirildiği ile ilgili mesaj verilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_772.png)
#### **5.2.14. Çoklu Pozisyon Kodu Değiştirme**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Çoklu Pozisyon Kodu Değiştirme

Qdms sisteminde Pozisyon Tanımlama menüsünde tanımlı çok sayıda pozisyon kodu bilgisinin  aynı anda değiştirilme işleminin yapıldığı menüdür.(Eski Kod, Yeni Kod şeklinde)  Bu işlemin yapılması için ![ref134]   butonu tıklanarak bilgisayara indirilen Çoklu Pozisyon Kodu Değiştirici şablonunda eski kod bilgisi alanında sistemde tanımlı eski kod bilgileri yazılarak  ve  yeni kod alanında değiştirilmek istenilen kod  bilgileri yeni kod alanı yazılırak Çoklu Pozisyon Kodu Değitirici şablonu doldurulur. Çoklu Pozisyon Kodu Değitirici şablonda ilgili alanlar bilgiler yazıldıktan sonra ![ref135]  butonu tıklanarak Çoklu Pozisyon Kodu Değitirici şablonu Qdms sisteminde menüye yüklenir.  Qdms sisteminde menüye yüklenen bilgilerin  kontrolünün sağlanması için, ![ref136]  butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref137]  butonu aracılığıyla aktarım gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_777.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Çoklu Pozisyon Kodu Değiştirici şablonu bilgisayara indirilir.

![ref135] : Doldurulan Çoklu Pozisyon Kodu Değiştirici şablon sisteme yüklenir.

![ref136]: Doldurulan  ve sisteme yüklenenen Çoklu Pozisyon Kodu Değiştirici şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref137]: Aktarım işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_778.png):Veriler Excel’e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Çoklu Pozisyon Kodu Değiştirme ekranında ![ref134]butonu tıklanarak  Çoklu Pozisyon Kodu Değitirici şablonu bilgisayara indirilir. İndirilen Çoklu Pozisyon Kodu Değitirici şablonunda  ilgili alanlar ilgili bilgiler yazılarak doldurularak  ve bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_779.png)

Çoklu Pozisyon Kodu Değiştirme ekranında doldurulan Çoklu Pozisyon Kodu Değiştirme  şablonu ![ref138] butonu tıklanarak sisteme yükleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_781.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_782.png)

Açılan ekranda doldurulan Çoklu Pozisyon Kodu Değiştirme şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_783.png)

Doldurulan Çoklu Pozisyon Kodu Değiştirme şablonun sisteme yüklenmesinde sonra 3. bir buton olan ![ref139] butonu görüntülenir. Bu buton tıklanarak verilerin  yani pozisyon kodlarının sistemde mevcuttur ve değiştirme için uygun olup, olmadığı kontrol edilir. ![ref139] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_785.png)

Sistem tarafından “Pozisyonlar sistemde mevcuttur ve değiştirme için uygundur.” Hata mesajı bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_786.png)

Verilerin aktarıma uygunluğu sağlandıktan sonra 4. Buton olan ![ref140]  butonu görüntülenir. Bu buton tıklanarak  eski pozisyon kodlarının yeni pozisyon kodları ile değiştirilerek sistem aktarılma işlemi yapılmasını sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_788.png)

Çoklu Pozisyon Kodu Değiştirme ekranında ![ref140]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_789.png)

Qdms sistemi tarafında “Eski pozisyon kodları silinip üzerlerindeki işler yeni tanımladığınız pozisyonlara aktarılacaktır.” mesajı verilerek “Tamam” butonu tıklanılır. Çoklu Pozisyon Kodu Değiştirme ekranında ilgili alanlada kodlarının değiştirildiği bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_790.png)
#### **5.2.15. Görev Transfer**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Görev Transfer

İşten ayrılan personelin üzerindeki işleri veya bir personeldeki işleri başka bir personele aktarmak için kullanıldığı menüdür. Bir pozisyon üzerinde var olan işlerin başka bir pozisyona aktarılmasını işlemi sağlanılır.Görev transfer ile okuma, onaylama, gözden geçirme, aksiyon gerçekleştirme gibi tüm görev tiplerine ait işlemler başka bir kullanıcıya devredilirken, onay transfer menüsü ile sadece seçilen onay yetkisi devredilebiliyor. Görev Transfer ekranında Yapacak Kişi alanında görevleri aktarılacak personelin ![ref141] (Seç) butonu tıklanarak açılan sistemde tanımlı Personel listesinde seçilerek ![ref142] (Ara) butonu tıklanarak görevleri aktarılacak personelerin Qdms sistemi kapsamında modüllerdeki  varsa görevlerinin listelenmesi sağlanır. Listelenen modüllerde aktarım yapılacak görevlerin seçimi yapılarak görevlerin devredileceği Pozisyon  alanında ![ref141] (Seç) butonu tıklanarak açılan sistemde tanımlı pozisyon  listesinde görev aktarımın yapılacak pozisyon  seçilerek ![ref143] butonu tıklanarak görev transfer işlemi yapılır. Bu menüde ilgili görevler ile atama mail gönderilmek istenirse ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_794.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_795.png): Seçili olan görevleri aktarılır.

![ref144]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Görev Transfer ekranında Yapacak Kişi alanında ![ref141] (Seç) butonu tıklanarak Sistemde tanımlı Personel listesinde görevleri aktarılacak Personel seçilerek ![ref142] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_797.png)

![ref142] (Ara) butonu tıklanıldıktanın ilgili personelle Qdms sistemi kapsamında varsa görevleri listenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_798.png)

Listelenen modüllerde ilgili modülde aktarım yapılacak görevlerin seçimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_799.png)

Listelenen modüllerde aktarım yapılacak görevlerin seçimi yapılarak görevlerin devredileceği Pozisyon  alanında ![ref141] (Seç) butonu tıklanarak açılan sistemde tanımlı pozisyon  listesinde görev aktarımın yapılacak pozisyon  seçilir. ![ref143]  butonu tıklanılır. Onay Atama mail ile ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_800.png)

Qdms sistemi tarafından “Seçmiş olduğunuz pozisyona görev aktarımı başarıyla gerçekleştirilmiştir.” Mesajı verilerek görev aktarım işleminin yapıldığı belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_801.png)
#### **5.2.16. Aktarımlar**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar

Sistemde toplu olarak aktarılmak istenilen Ürün, Müşteri-Tedarikçi, Denetim Sorusu, Denetçi, Cihaz, Muayene,  Kontrol  ve  Saha Tespit Sorusu, Madde No  aktarım menülerin bulunduğu kısımdır. Aktarımlar kısımında Madde No aktarımı işlemi yapılan “Madde No Aktarma ve Toplu Pasif Etme”  menüsünde yönetim sistemlerin madde no aktarım  işlemine ek olarak  sistemde yüklü olan madde no’ların toplu olarak pasif etme işlemi yapılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_802.png)
#### **5.2.16.1.Ürün Aktarma** 
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Ürün Aktarma

Ürünlerin aynı anda toplu bir şekilde sisteme aktarım işlemin yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_803.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Ürün Aktarım  şablonu bilgisayara indirilir.

![ref135] : Doldurulan Ürün Aktarım şablonu sisteme yüklenir.

![ref145]: Oluşturulan ve sisteme yüklenen Ürün Aktarım şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref146]: Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![ref134] butonu ile Ürün Aktarım şablonu indirilir, gerekli bilgiler doldurulduktan sonra  Ürün Aktarım  şablonu ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145] butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146] butonu aracılığıyla  ürün aktarım işlemi gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_806.png)

Ürün Şablonu Seç ekranında ![ref134] butonu ile Ürün Aktarım şablonu bilgisayara indirilir. Ürün Aktarım şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_807.png)

Ürün Şablonu Seç ekranında ![ref135] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_808.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_809.png)

Açılan ekranda doldurulan Ürün Aktarım  şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_810.png)

Ürün Şablonu Seç ekranında ![ref147] butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_812.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_813.png)

Ürün şablonu Seç ekranında  ![ref146]  butonu tıklanarak Ürün  Aktarma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_814.png)

Sistem tarafında “Ürünler başarıyla aktarılmıştır.” mesajı verilerek aktarım yapılan  ürün sayısının bilgisi verildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_815.png)
#### **5.2.16.2.Madde No  Aktarma ve Toplu Pasif Etme**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Madde No Aktarma ve Toplu Pasif Etme

Yönetim Sistemlerinde  Madde No ‘ların aynı anda toplu bir şekilde sisteme aktarma  ve sistemde yüklü olan madde no’ların toplu  bir şekilde pasif etme işlemin yapıldığı menüdür.

**Madde Numarası  aktarma işlemi;**

Madde No Aktarma ve Toplu Pasi Etme ekranında yönetim Sistemleri ile ilgili Madde numaralarının aktarma işlemi için  Madde Numaraı Aktarma alanı ile ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_816.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Madde No Aktarım şablonu bilgisayara indirilir.

![ref135] : Doldurulan Madde No Aktarım şablon sisteme yüklenir.

![ref145]: Oluşturulan ve sisteme yüklenen Madde No Aktarım şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref146]: Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![ref134] butonu ile Madde No Aktarım şablonu indirilir, gerekli bilgiler doldurulduktan sonra  Madde No Aktarım  şablonu ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145]  butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146]  butonu aracılığıyla  Madde No aktarım işlemi gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_817.png)

Madde No Aktama ve Toplu Pasif Etme ekranında ![ref134] butonu ile Madde No  Aktarım şablonu bilgisayara indirilir. Madde No  Aktarım şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_818.png)

Madde No Aktama ve Toplu Pasif Etme ekranında ![ref135]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_819.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_820.png)

Açılan ekranda doldurulan Madde No Aktarım  şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_821.png)

Madde No Aktama ve Toplu Pasif Etme ekranında ![ref147] butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediği kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_822.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_823.png)

Madde No Aktama ve Toplu Pasif Etme ekranında  ![ref146]  butonu tıklanarak Madde No   Aktarma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_824.png)

Sistem tarafında “Madde No aktarma işlemi başarıyla gerçekleşmiştir.” mesajı verilerek aktarım yapılan madde no sayısının bilgisi verildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_825.png)

**Madde No Toplu Pasif Etme**

Madde No Aktarma ve Pasif Etme menüsünde Madde Numarası  Pasifleştirme  seçeği seçilerek  aynı şekilde Madde Numarası toplu pasif işleminde olduğu gibi ekran üzerinde ![ref134] butonu ile Madde No toplu pasifleştirme şablon indirilir, gerekli bilgiler doldurulduktan sonra ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145] butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146]  butonu aracılığıyla aktarım gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_826.png)

Madde No Aktama ve Toplu Pasif Etme ekranında ![ref134] butonu ile Madde No toplu pasifleştirme şablonu bilgisayara indirilir. Madde No toplu pasifleştirme şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_827.png)

Madde No Aktama ve Toplu Pasif Etme ekranında ![ref135] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_828.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_829.png)

Açılan ekranda doldurulan Madde No Toplu pasifleştirme şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_830.png)

Madde No Aktama ve Toplu Pasif Etme ekranında ![ref147] butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediği kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_831.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_832.png)

Madde No Aktama ve Toplu Pasif Etme ekranında  ![ref146]  butonu tıklanarak Madde No  toplu pasifleştirme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_833.png)

Sistem tarafında “Madde No pasifleştirme işlemi başarıyla gerçekleşmiştir.” mesajı verilerek pasifleştirme yapılan madde no sayısının bilgisi verildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_834.png)
#### **5.2.16.3. Müşteri-Tedarikçi Aktarma**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Müşteri-Tedarikçi Aktarma 

Müşteri-Tedarikçilerin aynı anda toplu bir şekilde sisteme aktarma   işleminin yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_835.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Müşteri-Tedarikçi Aktarım  şablon bilgisayara indirilir.

![ref135] : Doldurulan Müşteri-Tedarikçi Aktarım şablon sisteme yüklenir.

![ref145]: Doldurulan ve sisteme yüklenen Müşteri-Tedarikçi Aktarım şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref146]: Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![ref134] butonu ile Müşteri-Tedarikçi Aktarım şablonu indirilir, gerekli bilgiler doldurulduktan sonra  Müşteri-Tedarikçi Aktarım  şablonu ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145] butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146]  butonu aracılığıyla  Müşteri-Tedarikçi aktarım işlemi gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_836.png)

Müşteri-Tedarikçi Aktarma ekranında ![ref134]  butonu ile Müşteri-Tedarikçi Aktarım şablonu bilgisayara indirilir. Müşteri-Tedarikçi Aktarım şablonunda ilgili alanlar ilgili bilgiler yazılırak bilgisayara kaydedilir. Aktarım şablonunda dikkat edilmesi husus  Müşteri için Türü olarak “M” Tedarikçi için türü olarak “S” yazılması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_837.png)

Müşteri-Tedarikçi Aktarma ekranında ![ref135] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_838.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_839.png)

Açılan ekranda doldurulan Müşteri-Tedarikçi Aktarma şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_840.png)

Müşteri-Tedarikçi Aktarma ekranında  ![ref147]butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_841.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_842.png)

Müşteri-Tedarikçi Aktarma ekranında  ![ref146]  butonu tıklanarak Müşteri-Tedarikçi işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_843.png)

Sistem tarafında “Müşteriler başarıyla aktarılmıştır.” mesajı verilerek aktarım yapılan  müşteri/Tedarikçi  sayısının bilgisi verildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_844.png)
#### **5.2.16.4. Denetim Sorusu Aktarma**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Denetim Sorusu Aktarma

Denetimlerde  sorulacak soruların aynı anda toplu bir şekilde sisteme aktarılma işleminin yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_845.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Denetim Sorusu  Aktarım  şablonu bilgisayara indirilir.

![ref135] : Doldurulan Denetim Sorusu  Aktarım şablonu sisteme yüklenir.

![ref145]: Doldurulan ve sisteme yüklenen Denetim Sorusu  Aktarım  şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref146]: Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![ref134] butonu ile Denetim Sorusu  Aktarım  şablonu indirilir, gerekli bilgiler doldurulduktan sonra  Denetim Sorusu  Aktarım  şablonu ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145] butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146] butonu aracılığıyla  Denetim Sorusu Aktarım  işlemi gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_846.png)

Denetim Sorusu Aktarma ekranında ![ref134]  butonu ile Denetim Sorusu  Aktarım  şablonu bilgisayara indirilir. Denetim Sorusu  Aktarım  şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir. Denetim Sorusu Aktarım işleminde Denetim Sorusu Aktarım şablonunda Soru no alanı Sistem Altyapı Tanımları/Denetim Faaliyeti/ Soru Havuzu ekranındaki son soru numarası baz alınarak yazılması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_847.png)

Denetim Sorusu Aktarma ekranında ![ref135]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_848.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_849.png)

Açılan ekranda doldurulan Denetim Sorusu  Aktarım  şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_850.png)

Denetim Sorusu Aktarma ekranında ![ref147]butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_851.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_852.png)

Denetim Sorusu Aktarma ekranında  ![ref146] butonu tıklanarak Denetim Sorusu  Aktarım  işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_853.png)

Sistem tarafında “Denetim soruları başarıyla aktarılmıştır.” mesajı verilerek aktarım yapılan  denetim sorusu  sayısının bilgisi verildiği görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_854.png)

**5.2.15.5.Denetçi Aktarma**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Denetçi Aktarma

Denetim  gerçekleştiren denetçilerin denetçi havuzunun toplu olarak aynı anda sisteme aktarılma işlemi yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_855.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Denetçi Aktarım  şablon bilgisayara indirilir.

![ref135] : Doldurulan Denetçi Aktarım şablon sisteme yüklenir.

![ref145]: Doldurulan ve sisteme yüklenen Denetçi Aktarım şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref146]: Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![ref134] butonu ile Denetçi Aktarım şablonu indirilir, gerekli bilgiler doldurulduktan sonra  Denetçi Aktarım  şablonu ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145] butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146] butonu aracılığıyla  Denetçi aktarım işlemi gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_856.png)

Denetçi Aktarma ekranında ![ref134] butonu ile Denetçi Aktarım şablonu bilgisayara indirilir. Denetçi Aktarım şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_857.png)

Denetçi Aktarma ekranında ![ref135]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_858.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_859.png)Açılan ekranda doldurulan Denetçi Aktarım  şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_860.png)

Denetçi Aktarma ekranında ![ref147]butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_861.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_862.png)

Denetçi Aktarma ekranında  ![ref146] butonu tıklanarak Denetçi  Aktarma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_863.png)

Sistem tarafından “Denetçiler başarıyla aktarılmıştır.” mesajı verilerek aktarılan denetçi sayısı verilen mesajda yer alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_864.png)
#### **5.2.16.5.Cihaz AKtarma**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Cihaz Aktarma

Cihaz Yönetimi modülünde işlem yapılan cihazların toplu olarak sisteme aktarımının yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_865.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Cihaz Aktarım şablon bilgisayara indirilir.

![ref135] : Doldurulan Cihaz  Aktarım şablon sisteme yüklenir.

![ref145]: Doldurulan ve sisteme yüklenen Cihaz Aktarım şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref146]: Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![ref134] butonu ile Cihaz Aktarım şablonu indirilir, gerekli bilgiler doldurulduktan sonra  Cihaz  Aktarım  şablonu ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145] butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146] butonu aracılığıyla, Cihaz aktarım işlemi gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_866.png)

Cihaz Aktarma ekranında ![ref134] butonu ile Cihaz  Aktarım şablonu bilgisayara indirilir. Cihaz Aktarım şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_867.png)

Cihaz  Aktarma ekranında ![ref135]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_868.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_869.png) Açılan ekranda doldurulan Cihaz Aktarım  şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_870.png)

Cihaz Aktarma ekranında ![ref147] butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_871.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_872.png)

Cihaz Aktarma ekranında  ![ref146] butonu tıklanarak Cihaz  Aktarma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_873.png)

Sistem tarafından “Kalibrasyon Cihazları başarıyla aktarılmıştır.” mesajı verilerek aktarılan cihaz sayısı verilen mesajda yer alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_874.png)
#### **5.2.16.6.Denetim Aktarma**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Denetim Aktarma

Denetim Faaliyetleri modülünde denetimlerin sisteme toplu olarak aktarılma işleminin yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_875.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Denetim Aktarma  şablonu bilgisayara indirilir.

![ref135] : Doldurulan Denetim Aktarma şablon sisteme yüklenir.

![ref145]: Doldurulan ve sisteme yüklenen Denetim Aktarma şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref146]: Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![ref134] butonu ile Denetim Aktarma şablonu indirilir, gerekli bilgiler doldurulduktan sonra  Denetim Aktarma  şablonu ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145] butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146] butonu aracılığıyla, Denetim Aktarma  işlemi gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_876.png)

Denetim Aktarım Şablonu ekranında ![ref134] butonu ile Denetim Aktarma  şablonu bilgisayara indirilir. Denetim Aktarma  şablonunda ilgili alanlar ilgili bilgiler yazılırak bilgisayara kaydedilir. İndirilen Şablon doldurulma işleminde dikkat edilmesi gereken husus Sistem Altyapı Tanımları/Denetim Faaliyeti/Denetim Tanımlama ekranında Denetim Listesinde bulunan tanımlı son denetim  nosundan sonra gelecek denetim nosu baz alınarak denetim sıra nosu  göre şablonda verilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_877.png)

Denetim Aktarım Şablonu ekranında ![ref135]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_878.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_879.png) Açılan ekranda doldurulan Denetim Aktarma şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_880.png)

Denetim Aktarma  ekranında ![ref147]butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_881.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_882.png)

Denetim Aktarma  ekranında  ![ref146] butonu tıklanarak Denetim Aktarma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_883.png)

Sistem tarafından “Denetim başarıyla aktarılmıştır.” mesajı verilerek aktarılan denetim sayısı verilen mesajda yer alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_884.png)
#### **5.2.16.7.Muayene Aktarma** 
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Muayene Aktarma 

İşe giriş muayenesi, periyodik muayene, periyodik test vb. muayene aktarım işlemlerinin gerçekleştiği menüdür. İşe giriş muayenesi, periyodik muayene, poliklinik muayene gibi firmada gerçekleştirilen muayenelerin toplu olarak sisteme aktarımının gerçekleştirilmesi isteniyorsa “Muayene Aktar” menüsü kullanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_885.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Muayene Aktarım  şablon bilgisayara indirilir.

![ref135] : Doldurulan Muayene  Aktarım şablon sisteme yüklenir.

![ref145]: Doldurulan ve sisteme yüklenen Muayene Aktarım şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref146]: Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![ref134] butonu ile Muayene Aktarım şablonu indirilir, gerekli bilgiler doldurulduktan sonra  Muayene  Aktarım  şablonu ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145] butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146] butonu aracılığıyla, Muayene aktarım işlemi gerçekleşmektedir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_886.png)

Muayene Aktarma ekranında aktarım yapılacak muayene türü listeden seçilerek  ![ref134] butonu ile  seçilen Muayene türü ile ilgili Muayene  Aktarım şablonu bilgisayara indirilir. Muayene Aktarım şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_887.png)

Muayene  Aktarma ekranında ![ref135]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_888.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_889.png)

Açılan ekranda doldurulan Muayene Aktarım  şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_890.png)

Muayene Aktar ekranında ![ref147] butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_891.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_892.png)

Muayene Aktar ekranında  ![ref146] butonu tıklanarak Muayene Aktarma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_893.png)

Sistem tarafından “Aktarım başarılıdır.” mesajı verilerek muayene aktarım işleminin yapıldığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_894.png)
#### **5.2.16.8.Eğitim Aktarma**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Eğitim Aktarma

Eğitim Planlama modülünde eğitimlerin  sisteme toplu olarak aktarılma işleminin yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_895.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Eğitim Aktarım şablon bilgisayara indirilir.

![ref135] : Doldurulan Eğitim  Aktarım şablon sisteme yüklenir.

![ref145]: Doldurulan ve sisteme yüklenen Eğitim Aktarım şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref146]: Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![ref134] butonu ile Eğitim Aktarım şablonu indirilir, gerekli bilgiler doldurulduktan sonra  Eğitim  Aktarım  şablonu ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145] butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146] butonu aracılığıyla, Eğitim aktarım işlemi gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_896.png)

Eğitim Aktar  ekranında ![ref134] butonu ile Eğitim  Aktar  şablonu bilgisayara indirilir. Eğitim  Aktar  şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_897.png)

Eğitim Aktar şablonunda Katılımcılar sekmesinde her katılımcı için Ana Plan ve Detay Plan kodu bilgisi yazılarak doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_898.png)

Eğitim  Aktar ekranında ![ref135]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_899.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_900.png) Açılan ekranda doldurulan Eğitim Aktar şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_901.png)

Eğitim Aktar ekranında ![ref147] butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_902.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_903.png)

Eğitim Aktar ekranında  ![ref146] butonu tıklanarak Eğitim Aktarma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_904.png)

Sistem tarafından “Veriler Aktarıldı” mesajı verilerek eğitim aktarma işleminin yapıldığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_905.png)
#### **5.2.16.9. Kontrol Aktarma**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Kontrol Aktarma 

Kontrol aktarma işleminin gerçekleştiği menüdür. Bilgi Güvenliği kapsamındaki EK-A kontrol maddelerinin ya da firmanın kontrol maddelerinin toplu olarak sisteme aktarımının gerçekleştirilmesi isteniyorsa “Kontrol Aktarma” menüsü kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_906.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Kontrol Aktarım şablon bilgisayara indirilir.

![ref135] : Doldurulan Kontrol Aktarım şablon sisteme yüklenir.

![ref145]: Doldurulan ve sisteme yüklenen Kontrol Aktarım şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref146]: Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![ref134] butonu ile Kontrol Aktarım şablonu indirilir, gerekli bilgiler doldurulduktan sonra  Kontrol  Aktarım  şablonu ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145] butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146] butonu aracılığıyla, Kontrol aktarım işlemi gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_907.png)

Kontrol  Aktarma ekranında ![ref134] butonu ile Kontrol Aktarım şablonu bilgisayara indirilir. Kontrol Aktarım şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_908.png)

Kontrol Aktarım şablonunda  Üst Kontroller, Kontrol Tipleri sekmelerinden  üst kontroller ve Kontrol tiplerinin kod bilgisi  ilgili alanlara yazılır. Modüller sekmesinde Modül Id bilgisi şablona yazılır.

Kontrol Aktarma ekranında ![ref135]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_909.png)Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_910.png) Açılan ekranda doldurulan Kontrol Aktarım  şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_911.png)

Kontrol Aktarma ekranında ![ref147] butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_912.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_913.png)

Kontrol Aktarma ekranında  ![ref146] butonu tıklanarak Kontrol  Aktarma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_914.png)

Sistem tarafından “Kontroller başarıyla aktarılmıştır.“ mesajı verilerek aktarılan Kontrol sayısı verilen mesajda yer alır. Aktarım yapılan kontroller aktarım şablonunda yazılan modüllünün Kontrol tanımlama menüsünde görüntülenir. Modül olarak Kurumsal Risk Değerlendirme Modülü Id yazıldığı için bu modülün Kontrol Tanımlama menüsünde aktarım yapılan kontroller görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_915.png)

Modül olarak Kurumsal Risk Değerlendirme Modülü Id yazıldığı için bu modülün Kontrol Tanımlama menüsünde aktarım yapılan kontroller görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_916.png)
#### **5.2.16.10.Saha Tespit Soru Aktarma**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Saha Tespit Soru Aktarma

Saha Tespit Modülünde saha denetimde sorulacak soruların toplu bir şekilde aktarılma işleminin yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_917.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref134] : Aktarım  şablonu bilgisayara indirilir.

![ref135] : Doldurulan  Aktarım şablonu sisteme yüklenir.

![ref145]: Oluşturulan ve sisteme yüklenen Aktarım şablonun hata verip vermediğine dair kontrol işlemi yapılır

![ref146]: Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![ref134] butonu ile  Aktarım şablonu indirilir, gerekli bilgiler doldurulduktan sonra Aktarım  şablonu ![ref135] butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![ref145] butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![ref146] butonu aracılığıyla  soru aktarım işlemi gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_918.png)

Soru Listesi Aktarma ekranında ![ref134] butonu ile  Aktarım şablonu bilgisayara indirilir. Aktarım şablonunda ilgili alanlar ilgili bilgiler yazılarak bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_919.png)

Soru Listesi Aktarma ekranında ![ref135]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_920.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_921.png)

Açılan ekranda doldurulan Aktarım şablonu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_922.png)

Soru Listesi Aktarma ekranında ![ref147]butonu tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_923.png)

Sistem  tarafından  “Veriler aktarım işlemi için uygun.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_924.png)

Soru Listesi Aktarma ekranında  ![ref146] butonu tıklanarak Aktarma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_925.png)

Sistem tarafında “Aktarım işlemi  tamamlandı.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_926.png)
#### **5.2.16.11. Eğitimleri İmzaya Gönder**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/ Eğitimleri İmzaya Gönder

Eğitim Planlama modülünde Eğitim Planlama ekranında Detaylar butonu tıklanarak açılan  Eğitim Detay Planlama ekranında  tanımlanan  ve SAT/BSAT/Konfigürasyon Ayarları/Aktarımlar/Eğitim Aktar menüsünde ise toplu aktarım işlemi yapılan bitti statüsündeki IBYS Eğitimlerin SAT/BSAT/Konfigürasyon Ayarları/Eğitim Kayıtları menüsünde görüntülenmeyen  Eğitim Detay Planlama ekranında  tanımlanan ve toplu aktarım işlemi yapılan IBYS  eğitimlerin  Eğitim Kayıtları menüsünde görüntülenmesi ve bakanlığa gönderilmeye hazır hale gelmesinin sağlandığı menüdür.  Bu menüde bitti statüsündeki IBYS kapsamındaki  Eğitim Kayıtları ekranında görüntülenmeyen bu eğitimlerin listesi yer alarak, listede tekli ve çoklu seçim yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_927.png) butonu tıklanarak Eğitim Kayıtları menüsünde görüntülemesi ve bakanlığa gönderime hazır hale getirilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_928.png)

**Ekrandaki bulunan butonlar yardımıyla;**

![ref148]:Listede seçili eğitim İmzaya gönderilme işlemi yapılır.

![ref144]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

Eğitimleri İmzaya Gönder ekranında listede IBYS kapsamında eğitimler seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_930.png)

IBYS kapsamında eğitimler seçili iken ![ref148] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_931.png)

Sistem tarafından “Eğitim detayları imzaya gönderilmiştir.” mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_932.png)

E-İmzaya gönderilen IBYS kapsamındaki eğitimler SAT/BSAT/Konfügürasyon Ayarları/Eğitim Kayıtları menüsünde görüntülenerek bakanlığa gönderilmeye hazır hale getirilir.
#### **5.2.17. Dashboard Konfigürasyonu** 
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/Dashboard Konfigürasyonu 

Qdms sisteminde  kullanıcılara işlemleri, metrikleri, grafikleri ve raporları tek bir ekranda görüntülemelerine olanak sağlayan kısımdır. Dashboard, bilgi akışını ve/veya içeriğini özetlemek amacıyla kullanılan, grafikler ve tablolar yoluyla belirli bir durumu açıklamaya yarayan göstergeler ekranı, iş panosu ve  görtergeler tablosu olarak ifade edilmektedir. Amacı en kısa sürede, en az etkileşim ve düşünme gereksinimi ile gerekli olan bilginin sunulmasıdır. Genelde yönetici konumundaki kişileri sıklıkla kullandıkları ekrandır. Modül Yöneticileri olmayan kullanıcılar  ilgili butonları kullanarak ilgili modülde gerekli ayarlamalar yapılarak grafik tasarım işlemide yaptıkları menüdür. Dashbord ekranında grafik tasarlama işlemi  bu menüde yapıldığı gibi Qdms sistemi yapısında ilgili modüllerin kapsamında yer almaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_933.png)

BSAT/Konfigürasyon Ayarları/Dashboard/Dış Müşteri Şikayetleri menüsü tıklanarak Dashboard Konfigürasyon Ayarları ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_934.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref3]: Yeni bir Dashboard tanımlanır.

![ref4]: Listede seçili olan Dashboard bilgisi üzerinde düzeltme/ değişiklik/ güncelleme yapılır. 

![ref5]: Listede seçili olan Dashboard bilgisi silinir.

- : Dashboard Konfigürasyonu ekranı kapatılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

Dış Müşteri Şikayetleri Modülünde yeni bir Dashboard  ekleme işlemi için  ![ref3] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_935.png)

Dashboard Konfigürasyonu - Yeni Kayıt ekranında gerekli alanlar ilgili bilgiler doldurulduktan sonra ekranın sol üstte yer alan ![ref9] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_936.png)

Sistem tarafından “Kaydetmek istediğinize emin misiniz?” uyarı mejasında “Tamam” butonu tıklanarak grafik ayarlarının başarı olarak kaydedilmesi işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_937.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_938.png)

Dış Müşteri Şikayetleri Dashboard ekranında tanımlanan Dashboard  Grafik tipi”Bar” olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_939.png)

Dış Müşteri Şikayetleri Dashboard ekranında tanımlanan Dashboard Dashboard Konfigürasyonu - Kayıt Güncelle ekranında  Grafik tipi “PieChart” seçilerek grafik tipi “PieChart” olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_940.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_941.png)  Grafiği aktar butonu tıklanarak grafiği açılır menüden seçilen format türüne (png,jpg,bmp,xls, vb. ) dönüştürerek dış ortama aktarılma işlemide yapılır.

Grafik Boyu min  değeri 500  maxsimum 1000 aralığında sınırlandırılmıştır. Grafik Eni min değeri 550 ve maxsimim değeri 1800 aralığında sınırlandırılmıştır. Bu değerler arasında grafik boyu ve Eni seçilmelidir. Dashboard Konfigürasyonu - Yeni Kayıt sıra numarası önceden kullanılmışsa kaydetme aşamasında sistem tarafında “Belirtmiş olduğunuz sıra numarası kullanımdadır, kullanımda olmayan bir sıra numarası belirtmelisiniz.”  hata mesajı verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_942.png)

Bu şekilde Grafik Ayarları butonu ile açılan ekranda yeni bir grafik eklenebilir.  Eklenen grafik bilgisi üzerinde düzenleme, güncelleme, değiştirme ve silme işlemleri yapılır. Listede  ilgili grafikler için filtreleme ekranı tanımlanmış ve indirilebilir olarak ayarlanmıştır.

#### **5.2.18. Karantinada Bekleyen Mailler**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Karantinada Bekleyen Mailler

Bu menü mail gitmesi istenmeyen karantina mailleri görüntülemek için kullanılır.QDMS üzerinde atanan görevlerin, gecikmelerin, bilgilendirmelerin bazı kullanıcılara mail yoluyla gitmesi istenmiyorsa Sistem Altyapı Tanımları menüsüne ait parametrelerden düzenleme yapılması gerekir.Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Parametreler menüsünde 55 numaralı “Karantina mail listesi(Sicil Numaraları)” parametresi değerine tanımlanan kullanıcı sicillerine kapsamındaki kullanıcılara mail gitmesi engellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_943.png)

Sistem Altyapı Tanımları Modülü parametrelerinde 253 numaralı” Karantina kullanıcı grupları(Grup Kodu)”parametresi değerine tanımlanan kullanıcı grubundaki grup üyelerine mail gitmesi engellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_944.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_945.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref149]: Listede seçili karantinadaki mail görüntülenmek için kullanılır.

![ref150]:Listede seçili  karantinadaki maili iletmek için kullanılır.

![ref151]:Listede seçili  karantinadaki maili silmek için kullanılır.

Karantinada Bekleyen Mailler ekranında Karantinadaki mail seçili iken ![ref149] butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_949.png)

Açılan pop-upn’da mail içeriği görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_950.png)

Karantinada Bekleyen Mailler ekranında Karantinaki mail seçili eken ![ref150]butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_951.png)

Sistem tarafından “Seçili maili göndermek istediğinizden emin misiniz?” mesajına “Tamam” butonu tıklanarak karantinadaki mail iletilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_952.png)

Karantinada Bekleyen Mailler ekranında listede karantinadaki mail seçili iken ![ref151] butonu tıklanılır.



![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_953.png)

Sistem tarafından “ Seçili kaydı silmek istediğinizden emin misiniz?” mesajında “Tamam” butonu tıklanarak karantinadaki mailin silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_954.png)
#### **5.2.19. Yardım Menüsü Tanımlama**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Yardım Menüsü Tanımlama

Bu menü, yardım menüsüne QDMS ile ilgili hazırlanan kullanıcı yardım dokümanlarının yüklenmesi amacıyla kullanılır.  Yardım dokümanı ile ilgili “Link” veya “Ek Dosya” ekleme işleminin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_955.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref152]: Yeni bir link veya ek dosya tanımlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_957.png): Listede seçili olan link veya ek dosya için düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_958.png): Listede seçili olan link veya ek dosya silinir.

**Yardım Menüsü Tanımlama ekranında Link eklemek;**

Yardım Menüsü Tanımlama ekranına yeni bir yardım konusu olarak link eklemek için ekranın sol üst köşesindeki ![ref152] butonuna tıklanarak Yardım Tanımlama  ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_959.png)

Açılan Yardım Tanımlama ekranda Menü Tipi Link seçilir. Link ve Linke verilecek Adı bilgisi girilir. Menü Kodu otomatik olarak sistmem tarafından atanmaktadır. Yardım Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref153] butonuna tıklanarak Yardım Menüsü Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_961.png)

QDMS Giriş sayfasında kaydedilen link, yardım menüsünün altında bulunan yardım konuları içerisinde yer alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_962.png)

Yardım menüsündeki kaydedilen link tıklanarak linkin bulunduğu sayfaya ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_963.png)

**Yardım Menüsü Tanımlama ekranında Ek Dosya eklemek;**

Yardım Menüsü Tanımlama ekranına yeni bir yardım menüsü eklemek için ekranın sol üst köşesindeki ![ref152] butonuna tıklanarak Yardım Tanımlama  ekranı açılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_964.png)

Açılan ekranda Menü Tipi Ek Dosya seçilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_965.png) (Ek dosya) butonu ile Ek dosya sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_966.png)

Dosya Yükle ekranında “Gözat” butonu tıklanılır. Açılan ekranda Yardım menüsüne eklenecek dosya seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_967.png)

Kullanıcı Yardım Dokümanın adı alanında yüklenen dosyanın adı olarak gelir  istenirse değiştirilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_968.png)

Yardım Menüsü Tanımlama ekranında gerekli alanlar doldurulduktan sonra sol üst köşedeki ![ref153] butonuna tıklanarak Yardım Menüsü Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_969.png)

Yardım menüsündeki yüklenen Ek Dosyanın linki tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_970.png)

Linki tıklanan ek dosyanın görüntülenmesi ve bilgisayara indirilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_971.png)
#### **5.2.20. Eğitim Kayıtları**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Eğitim Kayıtları

IBYS kapsamında tamamlanan eğitimlerin bakanlığa gönderilmesi için kullanılan menüdür. IBYS kapsamında tamamlanan eğitim kayıtlarının  bakanlığa gönderilmesi için altyapıdaki  konfigürasyon ayarlarının yapılması gerekir.İBYS kapsamında eğitim kayıtlarının gönderimi için altyapıda  yapılacak konfigürasyon ayarları aşağıda maddeler halinde yer almaktadır; 

- IBYS eğitimlerin gönderiminin yapılacağı bilgisayarda ArkSigner uygulaması kurulu olmalıdır.(<https://www.arksigner.com/indir\>)
- İmzalama işlemi sırasında sertifikanın doğrulanması için,  İmza kartı hangi servis sağlayıcısından alınmış ise;  Turktrust, E güven, Kamu SM, Etugra gibi, QDMS’in yüklendiği sunucunun o sertifika sağlayıcısının sitesine erişim izninin olması gerekmektedir.
- Sunucunun <https://ibys.bimser.com.tr:90\> adresine erişim için izni olmalıdır.
- Firmada IBYS eğitimlerin bakanlığa aktaracak İSG uzmanlarının Sistem Altyapı Tanımları/BSAT/Tanımlar/İSG Uzmanı Tanımlama menüden tanımlanması gerekmektedir.
- Firmada IBYS eğitimleri bakanlığa İSG uzmanı değilde İşyeri Hekimi tarafından aktarılacaksa  Sistem AltyapıTanımları/BSAT/Tanımlar/İş Yeri Hekimi Tanımlama menüden İşyeri Hekimin tanımlanması gerekmektedir.
- Sistem Altyapı Tanımları modülünün 148 nolu “Çalışma ve Sosyal Güvenlik Bakanlığı web servis entegrasyonu yapılacak mı?”  (E/H) parametresiyle ve Eğitim modülünün 59 nolu “Çalışma ve Sosyal Güvenlik Bakanlığı web servis entegrasyonu yapılacak mı?  (E/H)” parametre değerlerinin ‘Evet’ olarak güncellenmiş olması gerekmektedir. 
- Eğer Eğitim modülü yeni satın alınmışsa, Bakanlığın talep ettiği eğitim tanımları Bimser Destek tarafından yüklenmiş olacaktır. 
- Eğitimler tanımlanırken,  Entegre Yönetim Sistemi/Eğitim Planlama/Eğitim Tanımlama menüsünde  seçilebilir mi? alanı ile ilgili check box ve IBYS  Kapsamında mı? ile ilgili check box’ın işaretli olması gerekir.
- Eğitim Tanımlama Eğitim konusu alanın bakanlığı data setinde tanımlı olarak gelen Eğitim Konusu alanında yasal zorunluğu olan İş sağlığı ve İş Güvenliği ile ilgili eğitimleri seçilerek Eğitim tanımlama işlemin yapılması gerekir.
- Daha sonra sistem üzerinden IBYS kapsamında tanımlanan eğitimler Entegre Yönetim Sistemi Eğitim Planlama/Eğitim Planlama menüsünde eğitim planlarına bu eğitimleri eklendiği Eğitim Planlama Detay ekranında, Eğitim Türü ve Belge Tipi alanlarının değerlerini seçmeniz gerekmektedir. 
- Eğitim Planlama Detay ekranında Eğitim Veren alanında eğer eğitim veren  tipi Dış ise, Eğitim veren alanına kişinin adını soyadını, Eğitim Veren TC Kimlik No alanına mutlaka TC kimlik  numarası bilgisi yazılmadır.
- Eğitim sorumlusu alanı her durumda, firmada eğitimden sorumlu olan kişi seçilmelidir.(Eğitim verenden farklı kişi olabilir. Sistem üzerinden eğitimi kapatacak olan kişi, eğitim sorumlusudur.)
- Sistemde tanımlı olan İşyeri Hekimi ve İsg Uzmanın bağlı bulunduğu işyerinin Sistem Altyapı Tanımları /BSAT/Tanımlar/İş yeri Tanımlama menüsünde işyerinin SGK numarası alanın SGK numarasının tanımlı olması gerekmekdir. Birden çok lokasyona bağlı ise İşyeri Hekimi ve İSG uzmanın İşyerin Tanımlama menüsünde SGK numarası alanın SGK Numaraların tanımlı olması gerekmektedir.
- Firmada içerisinde eğitime katılımcı olarak katılacak çalışan personellerin TC kimlik numaralarının Sistem Tanımları/BSAT/Tanımlar/Personel Tanımlamla menüsünde açılan ekranda Ek bilgiler butonu tıklanarak açılan Personel Tanımlama-Ek bilgiler-Kayıt Güncelleme ekranında sistemde tanımlı olması gerekmektedir. Eğitime katılımcı olan personellerin işyeri ile bağlantısının kurulmuş olmalıdır. Bu tanımlamalar manuel olarak tanımlamaz ve HR transfer ile sistemde tanımlanır.
- IBYS kapsamında eğitimlerin gönderilme işlemi için Eğitim Yönetim Modülün IBYS Kapsamında Eğitim Tanımlama menüsünde eğitim tanımlanarak , ana bir eğitim planı oluşturulup, oluşturunan bu Eğitim plana eğitimleri aktarılma işlemi yapılır. Eğitime Katılımcıların eklenip Eğitim gerçekleştirip, bitti statüsüne getirildikten sonra Eğitimleri bakanlığa aktarabilmek için, Sistem Altyapı Tanımları/Konfigürasyon Ayarları/Eğitim Kayıtları menüsünde listelenen eğitim seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_972.png)  butonu tıklanarak gönderilir.Ayrıca SAT/BSAT/Konfigürasyon Ayarları/Aktarımlar/Eğitim Aktarım menüsünde toplu aktarım yapılarak bitti statüsünde  IBYS eğitimleride Eğitim Kayıtları menüsünde gönderilme işlemi yapılır.

Eğitim Tanımlama menüsünde Bakanlığın data setinde tanımlı eğitim konularında seçim yapılarak tanımlanan IBYS eğitimi  için  Eğitim Planlama menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_973.png) butonu tıklanılır. Açılan Eğitim Detay Planlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_974.png) butonu tıklanarak  IBYS kapsamında bir eğitim tanımlama işlemi yapılır.Tanımlanan IBYS kapsamındaki eğitime Katılımcılarının ekleme işleminde sonra gerçekleştirilmesi  ve bitti statüsüne geldiğinde  Eğitim Kayıtları menüsü listesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_975.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref154]: Listede seçili eğitim kayıtlarının Bakanlığa iletimi için imza onayını başlatır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_977.png): Listede seçili kayıtların güncelleme işlemini yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_978.png): Listede seçili eğitim kayıtlarının mobil imza olarak gönderilme işlemi yapılır.

![ref155]:Listede seçili eğitim kaydının onaylama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_980.png): Listede seçili eğitim kayıtlarının silinme işlemi yapılır.

![ref66]: Veriler Excel’ e aktarılır.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

**Açılan ekranda ilgili alanlar tanımlanır;**

**Kaydı Gönderen:** Eğitim Kayıtları ekranında gönderilecek IBYS eğitim kaydının  gönderecek İSG Uzmanı veya Hekim seçeneklerinden seçim yapıldığı alandır.

**Kaydı gönderen  İSG Uzmanı seçim işlemine bağlı olarak görüntülenen alan;**

**İSG Uzmanı:** Eğitim Kayıtları ekranında ![ref156] (Seç) butonu tıklanarak açılan sistemde tanımlı İSG Uzmanı listesinde seçim yapıldığı alandır. (ISG Uzmanı listesi Sistem Altyapı Tanımları/BSAT/ Tanımlar/ İSG Uzmanı Tanımlama menüsünde tanımlı olarak gelmektedir.)

**Kaydı gönderen  Hekim seçim işlemine bağlı olarak görüntülenen alan;**

**Hekim :** Eğitim Kayıtları ekranında ![ref156] (Seç) butonu tıklanarak açılan sistemde tanımlı Hekim listesinde seçim yapıldığı alandır.( Hekim  listesi Sistem Altyapı Tanımları/İş Başı ve Periyodik Muayene/İş Yeri Hekimi Tanımlama menüsünde tanımlı olarak gelmektedir.)

**Gönderim Durumu:** Eğitim Kayıtları ekranında IBYS eğitim kaydının gönderim durumun belirlendiği alandır. 

**Gönderim Durumu seçenekleri;**

**Gönderilecek :** Gönderilecek durumda olan IBYS kayıtları ifade eder.

**Kuyrukta:** Bakanlıkta gönderilmek için kuyrukta bekleyen IBYS kayıtlarını ifade eder 

**Gönderildi:** Gönderildi durumdaki IBYS kayıtları ifade eder.

**Hatalı Kayıt:** Hatalı IBYS Kayıtların ifade eder.

Eğitim Kayıtları ekranında IBYS Eğitim Kaydı seçili iken ![ref154] butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_982.png)Açılan Eğitim Görüntüleme ekranında IBYS kapsamında Eğitim kaydının detay bilgileri görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_983.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_984.png)  butonu tıklanarak IBYS kapsamındaki eğitim kaydının katılımcıların listesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_985.png)

![ref157] Kapat butonu IBYS kapsamındaki eğitimin görüntüleme ekrana geri dönülür. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_987.png)Eğitim Görüntüleme ekranında tekrar ![ref158] butonu tıklanarak ana menüye dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_989.png)

Eğitim Kayıtları ekranında Kaydı Gönderen alanında  IBYS kapsamındaki Eğitimleri gönderecek ISG Uzmanı ve Hekim  kaydı gönderecek seçenek seçilir. Kaydı gönderen alanında ilgili seçenek ilgili seçim yapılır. 

1\.Aşamada  Eğitim Kayıtları ekranında  Kaydı Gören alanında “İSG Uzmanı” olarak seçim yapılarak Uzman alanında sistemde tanımlı İSG Uzmanı listesinden Uzman Seçimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_990.png)

2\. Aşamada Eğitim Kayıtları ekranında IBYS kapsamındaki eğitimleri seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_991.png)

3\. Aşamada Eğitim Kayıtları ekranında  IBYS kapsamındaki eğitimlerin seçim işleminden sonra Gönderim Durumu alanında “Gönderilecek” seçeneği seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_992.png)

4\. Aşamada gönderim seçeneği seçildikten sonra ![ref155] butonu tıklanarak IBYS kapsamındaki eğitim kayıtlarının gönderilme işlemi başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_993.png)

Sistem tarafından “Eğitim kayıtlarını göndermek istediğinize emin misiniz?” mesajına “Tamam” butonu tıklanılır.İSG uzmanı e-imza kartı şifre bilgisini girerek IBYS Eğitimleri Kayıtlarının gönderileme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_994.png)
#### **5.2.21. Sağlık Kayıtları**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT /Konfigürasyon Ayarları/ Sağlık Kayıtları

İş sağlığı kapsamındaki periyodik muayeneleri EK-2 formatında bakanlığa iletmek için kullanılan menüdür.Tamamlanmış olan muayene kaydı, Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Sağlık Kayıtları sayfasına düşmektedir. İlgili kaydı seçerek gönder butonu ile açılan e imza ekranında şifre bilgisi girilerek kayıt gönderilebilir. Sağlık kayıtları ekranında bulunan  yenile butonu  sağlık kaydının güncel durumunu (Hatalı kayıt-başarılı işlem gibi.) güncellemek için kullanılmaktadır.Sağlık Kayıtlarının gönderimde altyapıda konfigürasyon ayarlarının yapılması için ilgili parametrelerin parametre değerlerine gerekli ayarlamaların yapılması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_995.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_996.png):Listede seçili Muayene kaydının güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_997.png): Listede seçili Muayene kayıtlarını elektronik imza ile imzalanarak bakanlığa gönderilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_998.png):Listede seçili Muayene kayıtların Mobil İmza ile gönderilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_999.png):Listede seçili Muayene kayıtlarının silinme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1000.png):Hatalı gönderilecek kaydın silinme işlemi yapar.

![ref65]: Kayıtlar filtrelenerek arama yapılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına  gelmesi işlemi yapılır.

**Açılan ekranda ilgili alanlar tanımlanır;**

**Gönderim Durumu:** Muayene Gönderim durumu ekranında muayene kaydının durumu alanı seçeneklerinden seçildiği alandır.

**Gönderim Durumu Seçenekleri:**

**Gönderilecek :** Gönderilecek durumda olan Muayene kayıtları ifade eder.

**Kuyrukta:** Bakanlıkta gönderilmek için kuyrukta bekleyen Muayene kayıtlarını ifade eder 

**Gönderildi:** Gönderildi durumdaki Muayene kayıtları ifade eder.

**Hatalı Kayıt:** Hatalı Muayene Kayıtların ifade eder.

**Muayene Türü:** Muayene Türü Durumu ekranında gönderim duruma bağlı olarak seçilecek Muayen türü seçeneklerin seçildiği alandır. İş Başı ve Periyodik Muayene modülü parametrelerinden yapılan ayarlamalara göre Muayene Türleri gelmektedir.Bakanlığa gönderilen Muayene türlerinin ID bilgisinin ilgili parametrelerde tanımlanarak muayene türleri alanında gelmektedir.İş Başı ve Periyodik Muayene Modülü parametrelerinden 42 numaralı “İşe Giriş Muayene Türü ID” parametresine Muayane Türü Tanımlama menüsünde alınan Id numarası tanımlanmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1001.png)

İş Başı ve Periyodik Muayene Modülü parametrelerinden 43 numaralı “Periyodik Muayene Türü ID” parametresine Muayane Türü Tanımlama menüsünde alınan Id numarası tanımlanmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1002.png)

İş Başı ve Periyodik Muayene Parametrelerinde yapılanan ayarlamalara göre Muayene Gönderim Durumu ekranında Muayene Türü alanında seçenek olarak görüntülenir.

**Muayene Tarihi:** Muayene Gönderim Durumu ekranında Muayene Tarihi bilgisinin açılan Takvim alanında seçildiği alandır.

1\.Aşamada Muayene Gönderim Durumu ekranında  gönderilecek muayene kayıtları olduğu için Gönderim Durumu alanında”Gönderilecek”  ve Muayene Türü alanında  Muayene türü seçeneği seçilir. Ör:Periyodik Muayene

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1003.png)

2\. Aşamada Muayene Gönderim Durumu ekranında seçilen Muayene türü ile ilgili muayene kayıtlarının listelenmesi ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1004.png) (Ara) butonu tıklanalarak ilgili Muayene türü  ilgili Muayene kayıtların listenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1005.png)

3\.Aşamada Muayene Gönderim Durumu ekranında listelene gönderim durumu “gönderilecek” periyodik muayene kayıtlarının listeden seçim işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1006.png)

4\.Aşamada Muayene Gönderim Durumu ekranında  Muayene Kayıtları seçili iken “Gönder” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1007.png)

Sistem tarafından “Muayene kayıtlarını göndermek istediğinize emin misiniz?” mesajında “Tamam” butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1008.png)

Hekimin e -imza ekranında şifre bilgisi girilerek kayıt gönderilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1009.png)
### **5.3. Raporlar**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Raporlar

Sistem Altyapı Tanımları Modülü ile ilgili tüm raporlara ulaşıldığı ve bu raporların excel formatında görüntülendiği menüdür. Bu raporlarda modüler bazlı olmayıp, sistemin  geneli ile ilgili raporlarıdır.
#### **5.3.1.Bsat Değişiklikler Raporu**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Raporlar/ Bsat Değişiklikler Raporu

HR transfer programının kullanıldığı durumlarda  kullanıcıların bulundukları değişen durumları hakkında bilgi verir. Bu raporda personellerin HR transferi ile verilerinin ne şekilde güncellendiği ve önceden ne tür bir veriye sahip olduğu bilgisi tutulmaktadır. Aktif veya pasif olma özellikleri, işten ayrılma durumları, Departman değişikliği, Pozisyon değişikliği gibi vb. konularda takip sağlanabildiği rapordur. Firmaya alınan personelerde  en son hangi tarihde ne değişiklik olduğu bilgisine ulaşmak amacı ile kullanılan rapordur. Bu raporla personelin ne zaman işten ayrıldığı, departman değişikliği yaptıysa hangi departmanda değişiklik yaptığı, pozisyon değişikliği yaptıysa hangi pozisyona sahip olduğu ve ne zaman durumu ile ilgili değişikliğin yapıldığı yeni durumun nasıl değiştiği bilgilerine ulaşılır. Bsat değişiklik Raporu iki sekmeden oluşur. Bu sekmeler Liste ve Filtre sekmesidir.  Liste sekmesinde filtre sekmesinde istenilen kriterlere göre filtreleme yapılarak alınan raporların listenilmesi sağlanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1010.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref159]: Kayıtlar filtrelenerek arama yapılır.

![ref160]: Veriler Excel’ e aktarılır.

Filtre sekmesinde Tarih aralığı alanında açılan Takvim alanında Tarih seçimi yapılarak ![ref159] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1013.png)


Arama kriterine göre filtreleme işleminde sonra ilgili kayıtların liste sekmesinde listede görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1014.png)

BSAT  Değişiklik Raporu ekranında ![ref160] butonu tıklanarak yapılanan filtre sekmesinde  arama kritterlerine göre  sistem otomatik olarak BSAT Değişiklik raporu  Excel formatında kullanıcıya sunar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1015.png)
#### **5.3.2.Kayıt Günlüğü Raporu**
**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Raporlar/ Kayıt Günlüğü Raporu

Kayıt Günlüğü raporu, Qdms Modüllerinde  yapılan her bir işlemin hangi tabloda, hangi kodlar ile kim tarafından değiştirildiğinin kayıt altına alınması işleminin görüntülendiği rapordur. Kayıt günlüğü raporun herhangi bir veri silme işlemi veya güncelleme işlemi yapılmış hangi tablodan silinmiş yada güncellenmiş olduğu kim tarafından yapıldığı bilgisine ulaşılır. Bu rapor örneğin herhangi veri silindiğin kim tarafından silindiği ne zaman silindiğine dair bilgilere ulaşmak için kullanılır. Kayıt Günlüğü Raporu iki sekmeden oluşur. Bu sekmeler Liste ve Filtre sekmesidir.  Liste sekmesinde filtre sekmesinde istenilen kriterlere göre filtreleme yapılarak alınan Raporların listenilmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1016.png)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1017.png): Listede seçili kayıtta eski değer ve güncel değer bilgilerin karşılaştırma işlemi yapılır.

![ref22]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Filtre sekmesinde  Modül adı, Tablo adı, Ana kod, Alt kod, İşlem yapan kullanıcı ve çalışma Tarihi gibi alanların bilgilerine göre arama yapılarak rapor alınır. Filtre sekmesinde Modül Adı alanında açılır liste tıklanarak ilgili modül seçilir. İşlem Yapılan Kullanıcı alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1018.png) (Seç) butonu tıklanarak açılan personel listesinde seçim yapılarak ![ref22] (Ara) butonu tıklanarak arama kriterlerine göre filtreleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1019.png)

Liste sekmesinde filtre sekmesindeki arama kriterlerine göre ilgili kayıtlar liste sekmesinde listede listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1020.png)

Kayıt günlüğü ekranında listede kayıt seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1021.png)butonu tıklanarak ilgili kaydının Eski değer ve Güncel değer bilgilerinin karşılaştırma işlemi yapıldığı ekran görünntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1022.png)

Kayıt Günlüğü ekranında ![ref160] butonu tıklanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1023.png)

Filtre sekmesinde  yapılan filtrede arama kritterlerine göre  sistem otomatik olarak Kayıt Günlüğü raporunu  Excel formatında kullanıcıya sunar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1024.png)
#### **5.3.3.Aktif Kullanıcı Raporu**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Raporlar/ Aktif Kullanıcı Raporu

Hangi modülde toplamda kaç kullanıcı işlem yapmış olduğunu gösteren rapordur. Modül No alanında ilgili modül seçildiğinde modülün hangi fonksiyonunları kaç kullanıcı aktif şekilde kullanmış olduğunun bilgisinede ulaşılmaktadır. Aktif Kullanıcı Raporu iki sekmeden oluşur. Bu sekmeler Liste ve Filtre sekmesidir.  Liste sekmesinde filtre sekmesinde istenilen kriterlere göre filtreleme yapılarak alınan Raporların listenilmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1025.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Filtre sekmesi Modül No, İşlem Tarihi ve  Durum alanların bilgilerine göre arama yapılarak rapor alınır. Modül No alanında Doküman İşlemleri  Modülü seçilerek işlem tarihi alanında tarih seçimi yapılarak ![ref22] (Ara) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1026.png)

Liste sekmesinde seçilen Doküman İşlemleri Modülü ile ilgili seçilen tarih aralığında modülün fonksiyonlarını kullanan aktif kullanıcı sayısı bilgisi verilir. Örneğin Raporda Doküman İşlemleri modülünde toplam Aktif kullanıcı sayısı “115” ve “Doküman Hazırlama” fonksiyonun kullanan aktif kullanıcı sayısı “71” olarak görüntülenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1027.png)

Aktif  Kullanıcı Raporu ekranında ![ref160] butonu tıklanarak yapılan filtre sekmesinde arama kritterlerine göre  sistem otomatik olarak Aktif Kullanıcı raporunu  Excel formatında kullanıcıya sunar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1028.png)

#### **5.3.4.Görev Transfer  Raporu**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Raporlar/ Görev Transfer Raporu

Qdms modüllerinde Görev transfer ve Onay  transfer menüleri ile  aktarılan görevlerin ve görevler ilgili aktarımla ilgili bilgilerin listesine ulaşıldığı rapordur.Raporda görevlerin aktarıldığı modül, işlem tipi, aktarılan görev, görevi aktarılan kullanıcı ve görevin aktarıldığı kullanıcı ve işlemin yapıldığı tarih gibi bilgilerine ulaşılır. Görev Tranfer  Raporu iki sekmeden oluşur. Bu sekmeler Liste ve Filtre sekmesidir.  Liste sekmesinde filtre sekmesinde istenilen kriterlere göre filtreleme yapılarak alınan Raporların listenilmesi sağlanılır.. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1029.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Filtre sekmesinde arama kriterlerinde Modül alanı alanında açılır liste tıklanarak ilgili modül seçilir.Görevin aktarıldığı kullanıcı  ve Görevi aktarılan kullanıcı alanlarına veri girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1030.png)

Görev Tranfer Raporu ekranında arama kriterlerine filtreleme işleminden sonra ![ref22] (Ara) butonu tıklanarak arama  kriterlere göre kayıtların liste sekmesinde listede görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1031.png)

Görev Transferi Raporu ekranında ![ref160] butonu tıklanarak yapılanan arama kriterlerine göre  sistem otomatik olarak Görev Transfer raporunu  Excel formatında kullanıcıya sunar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1032.png)
#### **5.3.5.QDMS Kullanım Raporu**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Raporlar/ QDMS Kullanım Raporu

Kullanıcılar bazında QDMS’ e giriş sayılarının tutulduğu rapordur. Kullanıcıların kaç defa sisteme giriş yaptığı son giriş tarihi ve saat bilgilerine ulaşılmak amacıyla kullanılan rapordur. Qdms Kullanım Raporu iki sekmeden oluşur. Bu sekmeler Liste ve Filtre sekmesidir.  Liste sekmesinde filtre sekmesinde istenilen kriterlere göre filtreleme yapılarak alınan Raporların listenilmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1033.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Filtre sekmesi İşlem Tarihi, Sicil no, Adı, Soyadı, Departman gibi alanların bilgilerine göre arama yapılarak rapor alınır. Departman alanında “Pazarlama” seçilerek ![ref22] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1034.png)

“Pazarlama” departmanında  bulunan personelerin  Qdms giriş sayısı bilgisi, son giriş tarihi ve saat bilgileri liste sekmesinde listede raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1035.png)

Qdms Kullanıcı Raporu ekranında ![ref160] butonu tıklanarak Filtre sekmesinde yapılanan arama kritterlerine göre  sistem otomatik olarak Qdms Kullanıcı raporunun  Excel formatında kullanıcıya sunar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1036.png)
#### **5.3.6.Bölümünde Bekleyen İşler Raporu**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Raporlar/ Bölümünde Bekleyen İşler Raporu

Qdms giriş yapan kullanıcının bulunduğu departmandaki personellerin bekleyen işlerininde   üzerinde beklediği işlerinin  (task üzerinde) raporunun alındığı menüdür. Bölümümde Bekleyen İşleri Raporu ekranında iki sekmeden oluşur. Bu sekmeler  Bekleyen İşler ve Arama sekmesidir.  Bekleyen İşler sekmesinde filtre sekmesinde istenilen kriterlere göre filtreleme yapılarak  kullanıcının üzerinde bulunan  işler ve işlerin sayasının bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1037.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Arama sekmesinde Yapacak kişi alanında  açılır liste tıklanarak üzerinde görevlerin listeneceği personel  seçim işlemi ve  iş tipi alanında ise “Tümü” seçeneği seçilerek ![ref22] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1038.png)

Arama sekmesindeki arama kriterlerine göre filtreleme işlemi yapıldıktan sonra Bekleyen İşler sekmesinde ilgili personellenin üzerindeki tüm görevleri listenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1039.png)

İş Tipi alanında personelin üzerinde listenen görevi yanındaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1040.png) butonu tıklanarak görevle ilgili detay bilgilere ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1041.png)

Bölümünde Bekleyen İşler Raporu ekranında ![ref23]  butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1042.png)Bölümümde Bekleyen İşler Raporu ekranında ![ref23] (Excel Aktar) butonu tıklanıldıktan sonra Bölümümde Bekleyen İşler Raporunun Excel formatında raporunu sistem otomatik olarak kullanıcıya sunar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1043.png)
#### **5.3.7.Kullanıcı Yetkileri Raporu**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Raporlar/ Kullanıcı Yetkileri Raporu

QDMS’ de tanımlı personellerin hangi kullanıcı grubunda, hangi yetkiye sahip olduğunu, hangi modülde hangi menüye erişebildiğinin raporunun alındığı menüdür. Hangi kullanıcının hangi modülde ne kadar yetkisi olduğunun görebildiği rapordur. Hangi personel Qdms’te nereye ulaşabildiği ve hangi menüye görebildiği bilgisine ulaşıldığı öğrenmek amacıyla kullanılan bir rapordur. Kullanıcı yetkileri raporu bir kullanıcının hangi menülere erişim yetkisini olduğunu sistem yöneticilerinin takip edebilmesi amacı için kullanılır. Veri kaybı gibi kritik durumlarda kullanılan bir rapordur. Kullanıcı Yetkileri Raporu iki sekmeden oluşur. Bu sekmeler Liste ve Filtre sekmesidir.  Liste sekmesinde filtre sekmesinde istenilen kriterlere göre filtreleme yapılarak alınan Raporların listenilmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1044.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Filtre sekmesinde Yetki Grubu, Kullanıcı Grubu, Kullanıcı Adı ve Modül gibi alanların bilgilerine göre arama yapılarak rapor alınır. Filtre sekmesinde Modül olarak Doküman İşlemleri ve Kullanıcı grubu  alanında  Kullanıcı Grubu  Listesinde  Kullanıcı Grubu seçilerek ![ref22] Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1045.png)

Kullanıcının hangi kullanıcı grubuna bağlı olduğu, yetki grubu bilgisi, Doküman İşlemleri  modülünde Sistem Altyapı Tanımları ve Entegre Yönetim Sistemi kısımların olan yetki tipi alanında hangi menülere erişebildiği bilgilerine ulaşılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1046.png)

Kullanıcı Yetkileri Raporu ekranında ![ref23] (Excel Aktar) butonu tıklanıldıktan sonra Kullanıcı Yetkileri  Raporunun Excel formatında raporunu sistem otomatik olarak kullanıcıya sunar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1047.png)
#### **5.3.8.Mail Raporu**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Raporlar/ Mail Raporu

Modüller bazında gönderilen maillerin raporunun alındığı menüdür. Qdms hangi modülde hangi  maili gönderilmiş , mailin içeriği , mailin oluşturulma tarihi bilgisi, mail alan gibi bilgilere ulaşılan bir rapordur. Müşterilerin gönderdiği maillerin takibini yapabilmesi amacı ile kullanılan bir rapordur. Mail Raporu iki sekmeden oluşur. Bu sekmeler Liste eve Filtre sekmesidir.  Liste sekmesinde filtre sekmesinde istenilen kriterlere göre filtreleme yapılarak alınan Raporların listenilmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1053.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref161]:Listede seçili mail’in detay bilgileri görüntülenir.

![ref162]: Kayıtlar filtrelenerek arama yapılır.

![ref66]: Veriler Excel’ e aktarılır.

![ref67]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref68]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref69]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Filtre sekmesi, Modüller, Konu, Mail Gönderen, Mail alan, Oluşturulma Tarihi, Durum ve Ek Dosya alanların bilgilerine göre arama yapılarak rapor alınır. Modüller Alan kısmında ilgili  Modülü seçilerek ![ref162] (Ara) butonu tıklanarak  gönderilen mailleri liste sekmesinde listelenmesi sağlanır. ![ref161] Görüntüle butonu ile listede seçili gönderilen maillerin içeriği açılır ve detay bilgisine ulaşılır. ![ref66] Excel’e aktar butonuna basılırsa, sistem otomatik olarak ilgili Modülü  için Mail  Raporu oluşturup kullanıcıya Excel formatında sunmaktadır.
#### **5.3.9.QDMS Giriş Raporu**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Raporlar/ QDMS Giriş Raporu

İlgili   kullanıcı sisteme ne zaman giriş yapmış ve  hangi IP üzerinden giriş yapmış bu logları gösteren rapordur. Qdms Giriş Raporu iki sekmeden oluşur. Bu sekmeler Liste eve Filtre sekmesidir.  Liste sekmesinde filtre sekmesinde istenilen kriterlere göre filtreleme yapıldığında alınan Raporların listenilmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1056.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Filtre sekmesi işlem Tarihi, IP adresi, Sicil No, Adı, Soyadı, Unvan, Departman ve İş yeri gibi alanların  bilgilerine göre arama yapılarak rapor alınır. Filtre sekmesinde departman alanında  “Bilgi İşlem” departman bilgisi seçilerek![ref22] ( Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1057.png)

Bilgi İşlem departmanında bulunan kullanıcıların sistem ne zaman giriş yapmış, hangi IP üzerinden giriş yapmış bilgisi liste sekmesinde raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1058.png)

QDMS Giriş  Raporu ekranında ![ref23] (Excel Aktar) butonu tıklanıldıktan sonra QDMS Giriş  Raporunu Excel formatında raporunu sistem otomatik olarak kullanıcıya sunar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1059.png)
#### **5.3.10.Personel Dosyaları**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Raporlar/ Personel Dosyaları

Sistemde olan personelerin sisteme yükledikleri ve erişebildikleri ek dosyaların listelendiği rapordur. Raporda firmada çalışan personellere eklenen ek dosyaları listelenmesi sağlanılıyor. Personeller üzerinde eklenen ek dosyalara tek ekrandan erişebilmek amacıyla yapılan bir rapordur. Sistem Altyapı Tanımları/BSAT/Tanımlar/Personel Tanımlama menüsünde Sistem Altyapı Tanımları Modülü 76 numaralı parametreye bağlı görüntülenen ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1060.png)butonu tıklanarak açılan Personel Tanımlama-Ek Bilgiler- Kayıt Güncelleme ekranında personele ait ek dosyalar  yüklenir. Bu personele ait yüklenen Ek Dosyaların ulaşıldığı ve listenildiği bir rapordur. Örneğin Personele ait Cv, Adli Sicil Sabıka Kaydı gibi dosyalara Personel Dosyaları raporundan ulaşılır. Firmada çalışan Personellerin ile ilgili özel bilgilerin yer aldığı Özlük Dosyalarına ulaşmak amacıylada kullanılan bir rapordur. Ayrıca hangi personelin, hangi ek dosyayı sisteme yüklemiş olduğunun görmek amacıyla kullanılan bir rapordur. 

Personel Dosyaları raporu iki sekmeden oluşur. Bu sekmeler Ek Dosya ve Filtre sekmesidir. Ek Dosyalar sekmesinde filtre sekmesinde istenilen kriterlere sicil no, adı ve soyadı bilgilerine göre arama yapılır. Ek dosyalar sekmesinde ![ref22] (Ara) butonu tıklanarak  personellere  ait yüklü tüm ek dosyaların listenmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1061.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

Ek Dosyalar sekmesinde personelin ait klasör seçilerek personele ait yüklü ek dosyaların listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1062.png)

Listenen ek dosyaların Dosya adı kısmındaki link tıklanarak ek dosyanın içeriği görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1063.png)

Ek Dosyalar ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1064.png) Excel’e aktar butonuna basılırsa, sistem otomatik olarak  Personel Dosyaları Raporu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1065.png)
#### **5.3.11.Onay Süre Raporu**
**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Raporlar/ Onay Süre Raporu

Qdms modüllerinde onaya giden  akışlarının   onay  başlangıç Tarihi,  onaycısı, statüsü, onay tarihi ve onay süresi gibi bilgilerin yer aldığı rapordur. Onay süresi  Raporu iki sekmeden oluşur. Bu sekmeler Arama  ve Onay Süreleri Listesi sekmesidir. Arama  sekmesinde arama kriterlere göre filtreleme yapılarak alınan raporlarının Onay Süreleri listesi sekmesinde listede listelenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1066.png)

**Ekranda bulunan butonlar yardımıyla;**

![ref22]: Kayıtlar filtrelenerek arama yapılır.

![ref23]: Veriler Excel’ e aktarılır.

![ref6]: Menü ekranlarındaki arama kriterleri arama işlemi yapılan gridde filtre alanlarında kalan verilerin  temizleme işlemi yapılır.

![ref7]: Menü ekranın tekrar varsayılan ayarlarına gelme işlemi yapılır.

![ref8]:Menü ekranlarında kolonların karşılığı olan alanların  gösterip- gizleme özelliği yani saklama özelliği ile menü ekranın kullanıcı bazlı tasarlama işlemi yapılır.

Arama sekmesinde Modüller, Alt Modül Tanımlaama, Onay Başlatan gibi  bilgilerine göre arama yapılarak rapor alınır. Modüller Alan kısmında açılır liste tıklanarak “ Sistem Altyapı Tanımları” Modülü seçilir.  Alt Modül  alanında açılır liste tıklanarak “ISG Uzmanı Atama Onayı” seçilir. Onay başlangıç Tarihi  seçilerek![ref22] (Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1067.png)Onay Süreleri Listesi sekmesinde ilgili modüldeki onay akışı ile ilgili  onayı başlatan, ana kod, alt kod, onaycı, statüsü (Onay Başladı, Onay Devam ,Onaylandı ve reddedildi)  ve onay süresi bilgileri verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1068.png)

Onay Süre Raporu ekranında ![ref23] (Excel Aktar) butonu tıklanıldıktan sonra Onay Süre   Raporunu Excel formatında raporunu sistem otomatik olarak kullanıcıya sunar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1069.png)



[ref1]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_26.png
[ref2]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_41.png
[ref3]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_64.png
[ref4]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_65.png
[ref5]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_66.png
[ref6]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_67.png
[ref7]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_68.png
[ref8]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_69.png
[ref9]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_71.png
[ref10]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_78.png
[ref11]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_93.png
[ref12]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_94.png
[ref13]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_112.png
[ref14]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_116.png
[ref15]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_119.png
[ref16]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_126.png
[ref17]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_128.png
[ref18]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_149.png
[ref19]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_150.png
[ref20]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_157.png
[ref21]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_158.png
[ref22]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_159.png
[ref23]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_160.png
[ref24]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_174.png
[ref25]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_175.png
[ref26]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_186.png
[ref27]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_233.png
[ref28]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_243.png
[ref29]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_246.png
[ref30]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_254.png
[ref31]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_255.png
[ref32]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_257.png
[ref33]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_268.png
[ref34]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_272.png
[ref35]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_275.png
[ref36]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_277.png
[ref37]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_285.png
[ref38]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_286.png
[ref39]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_288.png
[ref40]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_291.png
[ref41]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_294.png
[ref42]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_303.png
[ref43]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_310.png
[ref44]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_315.png
[ref45]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_322.png
[ref46]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_337.png
[ref47]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_341.png
[ref48]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_345.png
[ref49]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_346.png
[ref50]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_347.png
[ref51]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_356.png
[ref52]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_370.png
[ref53]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_372.png
[ref54]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_376.png
[ref55]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_379.png
[ref56]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_383.png
[ref57]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_391.png
[ref58]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_400.png
[ref59]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_408.png
[ref60]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_422.png
[ref61]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_426.png
[ref62]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_429.png
[ref63]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_433.png
[ref64]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_437.png
[ref65]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_440.png
[ref66]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_441.png
[ref67]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_442.png
[ref68]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_443.png
[ref69]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_444.png
[ref70]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_450.png
[ref71]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_455.png
[ref72]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_460.png
[ref73]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_464.png
[ref74]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_469.png
[ref75]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_473.png
[ref76]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_477.png
[ref77]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_483.png
[ref78]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_490.png
[ref79]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_495.png
[ref80]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_500.png
[ref81]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_508.png
[ref82]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_509.png
[ref83]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_510.png
[ref84]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_513.png
[ref85]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_517.png
[ref86]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_518.png
[ref87]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_519.png
[ref88]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_521.png
[ref89]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_522.png
[ref90]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_527.png
[ref91]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_539.png
[ref92]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_540.png
[ref93]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_543.png
[ref94]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_552.png
[ref95]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_561.png
[ref96]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_562.png
[ref97]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_563.png
[ref98]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_564.png
[ref99]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_577.png
[ref100]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_578.png
[ref101]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_579.png
[ref102]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_580.png
[ref103]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_588.png
[ref104]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_589.png
[ref105]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_592.png
[ref106]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_594.png
[ref107]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_599.png
[ref108]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_601.png
[ref109]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_612.png
[ref110]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_618.png
[ref111]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_622.png
[ref112]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_629.png
[ref113]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_632.png
[ref114]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_641.png
[ref115]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_644.png
[ref116]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_647.png
[ref117]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_649.png
[ref118]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_655.png
[ref119]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_669.png
[ref120]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_670.png
[ref121]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_683.png
[ref122]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_686.png
[ref123]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_691.png
[ref124]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_698.png
[ref125]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_705.png
[ref126]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_714.png
[ref127]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_728.png
[ref128]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_733.png
[ref129]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_746.png
[ref130]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_759.png
[ref131]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_762.png
[ref132]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_767.png
[ref133]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_769.png
[ref134]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_773.png
[ref135]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_774.png
[ref136]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_775.png
[ref137]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_776.png
[ref138]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_780.png
[ref139]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_784.png
[ref140]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_787.png
[ref141]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_791.png
[ref142]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_792.png
[ref143]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_793.png
[ref144]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_796.png
[ref145]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_804.png
[ref146]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_805.png
[ref147]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_811.png
[ref148]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_929.png
[ref149]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_946.png
[ref150]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_947.png
[ref151]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_948.png
[ref152]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_956.png
[ref153]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_960.png
[ref154]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_976.png
[ref155]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_979.png
[ref156]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_981.png
[ref157]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_986.png
[ref158]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_988.png
[ref159]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1011.png
[ref160]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1012.png
[ref161]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1054.png
[ref162]: https://docsbimser.blob.core.windows.net/imagecontainer/327425b1-dd08-4f71-99e4-b7455cabbdeb_1055.png
