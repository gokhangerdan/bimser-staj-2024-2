# Kurulum & Konfigürasyon Teknik Gereksinim Dokümanı
# 1.Giriş
## Amaç
BEAM Kurulum ve Konfigürasyon Teknik Gereksinim Dokümanı, BEAM uygulamasının kurulumu ve konfigürasyon ayarları ile ilgili gerekli bilgilerin paylaşımı için oluşturulmuştur.

## Kapsam

BEAM Kurulum ve Konfigürasyon Teknik Gereksinim Dokümanı, sırası ile aşağıdaki işlemlerin gerçekleştirilmesi için gerekli çalışmaları kapsar.

1.  Giriş ve Kapsam
    1.  Sistem Gereksinimleri
        1.  IIS ve SQL Kontrolü
        2.  Redis Kurulumu
        3.  eBA Kurulumu
        4.  BEAM Kurulumu
        5.  Olası Hatalar

# Sistem Gereksinimleri

## Test Sistem Gereksinimleri

Uygulama ve Veri Tabanı Yönetim Sistemi Sunucuları aynı sunucu üzerinde çalışacaktır.

![Resim1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07262db9-e72d-4d1f-abbf-d59826e8a9bd) | **Sistem Gereksinimleri**                           |
|------------------------------------------------------------------------------------|-----------------------------------------------------|
|                                                                                    |                                                     |
| **Sunucu İşlemcisi**                                                               | Min Intel Xeon 4 çekirdekli işlemci                 |
| **Sunucu Ram**                                                                     | 16 GB                                               |
| **Sunucu İşletim Sistemi**                                                         | Windows 2012 veya üstü 64 Bit                       |
| **Web Server**                                                                     | IIS7 veya üstü                                      |
| **Framework**                                                                      | Microsoft .NET Framework 4.8                        |
| **Veritabanı**                                                                     | MS SQL Server 2012 veya üstü,Oracle 12.1c veya üstü |
| **DB Disk Alanı**                                                                  | 50 GB                                               |
| **Uygulama Disk Alanı**                                                            | 50 GB                                               |

## Canlı Sistem Gereksinimleri

![Resim2](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07262db9-e72d-4d1f-abbf-d59826e8a9bd) | **Sistem Gereksinimleri**           |
|------------------------------------------------------------------------------------|-------------------------------------|
|                                                                                    |                                     |
| **Sunucu İşlemcisi**                                                               | Min Intel Xeon 4 çekirdekli işlemci |
| **Sunucu Ram**                                                                     | 32 GB                              |
| **Sunucu İşletim Sistemi**                                                         | Windows 2012 veya üstü 64 Bit       |
|  *Web Server**                                                                     | IIS7 veya üstü,                     |
|  **Framework**                                                                     | Microsoft .NET Framework 4.8        |
|  **Veritabanı**                                                                    | MS SQL Server 2012 veya üstü,Oracle 12.1c veya üstü |
|  **DB Disk Alanı**                                                                 | 150 GB                              | 
|  **Uygulama Disk Alanı**                                                           | 75 GB                               |  


1.  **IIS ve SQL Kontrolü**

Kurulum işlemlerini gerçekleştirirken, kurulum dosyalarını yönetici olarak çalıştırın.Kuruluma başlamadan önce IIS ve SQL in kurulu olduğundan emin olun. Görsel 1.1.’de IIS kontrolünün yapılacağı lokasyon belirtilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada241be12-1d17-46c0-a22c-2a73a0ce6704)

**Görsel 1.1. Kontrol Lokasyonu**

IIS açıldığında **Default Web Site** altında herhangi bir sitenin olmaması gerekmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc1fcda5-e455-480e-aee1-1227626f496f)

**Görsel 1.2.Default Web Site**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1bb96b5b-f915-461b-9c0e-c7bedbeb163d)

SQL için gerekli kurulum dosyalarının kontrolünün yapılarak tüm isterlerin kurulu olduğu gözlemlenir. 

**Görsel 1.3.SQL Server ve Add-On lar**

Eğer sistem üzerinde IIS özelliği aktif değil ise Windows Features üzerinden (Görsel 1.4.’te Aktif edilecek features ), IIS aktif hale getirilerek ilgili adımlar ilerletilebilir.

**Görsel 1.4.’te Aktif edilecek features**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload23c27cdf-7da8-481c-b53e-ef0be62ef179)**

## Redis Kurulumu

Redis kurulum dosyalarının bulunduğu klasöre girdikten sonra aşağıdaki resimde işaretlenmiş olan dosya çalıştırılarak kurulum işlemi başlatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf62f60c-9736-493f-a7e9-f15bdd1a74bf)

Açılan kurulum ekranında “Next” butonu ile kurulum başlatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9b206cc-07d8-4f23-9e57-26f968b2dfb2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb95b53f-709f-4193-8556-4176638d55b8)

Kurulum ilerlemesi bittiğinde gelen ekranda ki “FINISH” butonu ile kurulum işlemi tamamlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26fa1451-033c-4ec8-a196-bf2ab8e408f2)

Redis kurulumunun yapıdlığı klasöre girilerek, aşağıdaki resimde kırmızı kutu içine alınmış olan .conf uzantılı dosya kopyalanarak redis.windows-service-\*\*\*\*.conf şeklinde yeniden isimlendirilir ve bu kopya aynı klasöre eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53007717-aca8-47c0-8b10-4f3af337b085)

Kopyaladığımız dosyayı, sağ tıklayıp “EDİT” seçeneği ile dosya düzenleme ekranına giriş yaparız. Açılan metin belgesi içerisinde bulunan “PORT” değerine sistemde uygun olan herhangi bir Numara girilmelidir.

\*\*\*Bu alanda girilen port değeri BEAM kurulumunda da kullanılacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload273b4470-4f08-43b5-91ee-ba44cc104263)

Daha sonra ise aşağıdaki “save” satırları, işaretlenmiş kısımdaki şekilde düzenlenmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad0ef833-0188-4d3c-ae3a-bb5b4a40b4b8)

Bu düzenlemeler yapıldıktan sonra dosya bu şekilde kaydedilir ve kapatılır.Save alanında yapılan düzenleme, orjinal .conf uzantılı dosyada da yapılmalıdır. (Eba İÇİN)

**cd "C:\\Program Files\\Redis"**

**redis-server.exe --service-install --service-name Redis_BEAM redis.windows-service-BEAM.conf**

**sc config Redis_BEAM DisplayName= "Redis (BEAM)"**

Yukarıdaki kod parçası, mavi olan yerler “İnstanceName”, Kırmızı olan yer ise düzenlediğimiz dosyanın adı olacak şekilde düzenlenir ve yönetici olarak komut isteminde(cmd) çalıştırılır.Daha sonra hizmetler’de oluşturmuş olduğumuz "Redis (BEAM)" hizmeti çalıştırılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7ccb556-b90b-446b-9435-8a70e9219b82)

## SQL İşlemleri

### **SQL Yeni Kullanıcı Oluşturma**

SQL Server uygulamasına girilerek, ekranda sol kısımda bulunan dizin üzerinde “Security” başlıklı dizin sağ tıklanır, ardından sırasıyla “New \> Login” seçenekleri ile yeni kullanıcı oluşturma ekranına giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ddbc195-9bfc-4f88-8c7f-92061779f210)

Açılan “Login” ekranında, Kullanıcı adı ve Parola bilgileri belirlenir. Ve işaretli kutucukların aşağıda bulunan resimdeki gibi olduğu kontrol edilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef4bc828-7a32-41ef-b46d-46e850e073b4)

Kullanıcı bilgileri belirlendikten sonra, sol üst kısımda bulunan sekmelerden “Server Role” seçilerek aşağıda resimde ki gösterilen kutucuklar işaretlenmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16ffa83d-11f3-400c-8c74-67646004d5b6)

Bu işlemler yapıldıktan sonra “OK” Butonu ile kullanıcı oluşturma işlemi tamamlanır.

### **SQL Yeni Veri Tabanı Oluşturma**

SQL uygulamasında ekranın sol tarafında bulunan dizinde “Database” başlıklı dizin sağ tıklanır, açılan listeden “New Database…” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8319978-c2b3-4db1-bb02-872cd1857231)

Açılan Veritabanı oluşturma ekranı içerisinde, “Database Name” alanına herhangi bir isim yazılmalıdır “Owner” alanına ise oluşturulan kullanıcının ismi yazılmalıdır. Geri kalan alanlar ise aşağıda resimlerde gösterildiği şekilde düzenlenmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf600597d-5933-4d55-a9e5-e42f4c07ccef)

## eBA Kurulumu

”BEAM” klasörü içersindeki eBA 6.2.0 Server Setup.exe dosyasını tıklayarak, EBA kurulum sihirbazını başlatın.Alanları Görsel 4.1.’de görüldüğü üzere alanları doldurun ve Next butonuna tıklayın.

Not : PRODUCTION alanını kesinlikle değiştirmeyin.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload107c8547-f1c2-4ab7-8c3f-921990600679)

Görsel 4.1.

Ekrana gelen pencereye, bağlantı bilgilerini girin ve Next butonuna tıklayın.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload23691241-44d8-4a58-809e-56985914242c)

Görsel 4.2.

IIS üzerinden eba.net ve eba.net.dm uygulama application pool’larının oluşup oluşmadığı ve “Klasik ve versiyon 4.0 alanlarının seçili olup olmadığı kontrol ediniz.

Hata (application pool-virtual path hatası) oluşması durumunda uygulama havuzlarını IIS’ den oluşturun.

eba.net ve eba.net.dm application pool’ları oluşturmak için aşağıdaki adımları takip edin.

-   SitesDefaultWebSite’a sağ tıklayın.
    -   Addebanet/ebanet—ebanet/ebanetdm—ebanet/bchr application pathleri oluşturun.

Ekrana gelen pencerede, Install butonunu tıklayarak kurulumu tamamlayın.

Lisanslama işlemi için aşağıdaki adımları takip edin.

#### C:/Eba.net/common/ eBALicenceManager.exe’ yi açın.

-   Açılan pencerede Create License butonunu tıklayın.
    -   bss.bimser.com.tr’ den lisans talabinde bulunun.
    -   Lisans talabi onaylandıktan sonra lisans dosyasını indir ve common klasörünü içine kopyalayın.

        C:\\eba.net\\Common\\Install dosyasının içersindeki stopeba ve starteba’yı sırası ile çalıştırın.



## BEAM Kurulumu

BEAM 2.18…. setup dosyası yönetici olarak çalıştırılmalıdır. Ekrana ilk olarak gelecek “Extract” işlemi tamamlandıktan sonra aşağıdaki seçim ekranı gelecektir. Dil seçenekleri “Türkçe / English” olarak seçilebilmektedir. İlk kez kurulum yapılacağından dolayı “Kur/İnstall” seçeneği seçilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada201e775-5344-48a9-98bd-bcbe3db0a8a7)

Bu seçimler yapıldıktan sonra “BEAM Kurulum Sihirbazı” ekrana gelecektir. Bu ekranda “Next” butonu ile kurulum adımlarına başlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb196360-7fb6-413b-8b0c-38f40507e25e)

Lisans sözleşmesi ekranında, “Lisans sözleşmesi şartlarını Kabul ediyorum” seçeneği işaretlenir ve “Next” butonu ile kurulum adımlarına devam edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33747088-aea1-47ff-99f3-96e297b4eddd)

Kurulum yapılacak dizin aşağıda resimdeki gibi oluşturulacaktır. Dizin seçme işlemi tamamlandıktan sonra “Next” butonu ile kuruluma devam edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8410754c-660b-4fe6-b31b-333df8e96d3d)

Gelen “Server Configuration Editor” ekranı içerisine sağ tıklanarak “Add Database” seçeneği tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2dab4059-95e2-46e3-b3b8-e50665bab4ae)

Ardından gelecek ekran üzerinde “Database Name” alanına “Instance Name” yazılır. Connection String alanında bulunan “Source, Catalog, UserID” alanlarının doğruluğu kontrol edildikten sonra,”Password” alanına oluşturulan kullanıcı parolasını girerek önce “Test Connection” butonu ile bağlantı test edilir. Eğer bir yanlışlık yapılmadıysa, “OK” butonu ile ekleme işlemi tamamlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cb8e0d7-bd40-43d7-8424-24e7b37bde72)

Cache sekmesine geçilerek aşağıda resimde gösterilen düzenlemeler yapılarak, “Password” alanına kullanıcı için belirlenen şifre girilir. Test connection butonu ile bağlantı test edilir ve bilgiler doğru girildiğinden emin olunur. Ardından “OK” butonu ile yapılan değişiklikler kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc278aec1-e391-4320-9fa6-8104b3f9184d)

Yukarıda bulunan sekmelerden “İnstance” sekmesine girilerek aşağıda resimdeki düzenlemeler yapılır. Ardından “OK” butonu ile değişiklikler kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b7ed105-0197-454d-bba7-9d6d52471f25)

Bu editor içerisinde son olarak “Settings” sekmesindeki ayarlar aşağıda resimde gösterildiği şekilde düzenlenerek “Save” butonu ile yapılan bütün düzenlemeler kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc5d2a8c-2167-4113-bf7d-e6fe3fd8a9f6)

Kayıt sonrası gelen ekran üzerinde bulunan “Default” işaretli alan çift tıklanarak düzenlemelerin yapılacağı ekrana giriş yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload412565d9-6d28-4c24-ad3d-7878c05884dc)

Açılan ekranda;

“Eba İnstance Name” alanına “PRODUCTION” yazılmalıdır.

“Application Name” alanına, sunucu adresinde görünmesi istenilen uygulama ismi bilgisi girilmelidir.

Bu bilgiler girildikten sonra “OK” butonu ile yapılan değişiklikler kaydedilir ve sonraki gelen ekranlarda “Next” butonu ile kurulum işlemi tamamlanır. “Finish” butonu ile kurulum ekranı kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd582bcf-05f7-4203-ad0a-fe671daf89d7)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf292291-1c88-435a-a1b4-9068ab217d98)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25bc38ae-0c1b-45de-be72-0bfcdc5bbd7e)


## Konfigürasyon Kontrolleri

Kurulum tamamlandıktan sonra kurulum işleminin yapıldığı klasöre girilerek içerisindeki “Common” isimli klasör açılır. Common klasörü içerisinden “eBAClientConfigurator.exe” uygulaması yönetici olarak çalıştırılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload17bf0f95-901b-4814-be38-4b1fe74036b2)

1.Açılan ekranda;

“Localhost/default” seçilerek alt kısımdan “Edit” butonu ile düzenleme sayfasına girilir ve “Instance Name” alanı doldurularak “Ok” butonu ile kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf09b7207-d8c3-42ce-86bd-3e3a6da7f07b)

Sonrasında, alt kısımda bulunan “New” butonu ile “Localhost/Controller1” oluşturulur. Ardından içerisindeki bilgiler aşağıdaki resimdeki şekilde doldurularak “Ok” butonu ile yapılan değişiklikler kaydedilir ve bu işlem tamamlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf677b6cb-464f-446d-a341-78d61f640c28)

1. Bir sonraki aşama olarak, “Common” klasörü içerisinde “eBAServerConfigurationEditor.exe” uygulaması yönetici olarak çalıştırılır.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d101c63-d855-440b-8c2d-3cf65b2c46e7)

 Açılan ekranda üst kısımda bulunan “Database, Cache, Instance” sekmelerine Eba’nın bağlantı ayarları da eklenmelidir.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload920641d8-e76a-40d0-bec6-5b25a8ae422f)

 Ayarlar tamamlandıktan sonra “Save” butonu ile ayarlar kaydedilir ve bu şekilde kurulum tamamlanmış olur.
