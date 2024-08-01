---
sidebar_label: Mac Os Kurulumu
sidebar_position: 2
custom_edit_url: ""
---

# Mac Os Kurulumu
##  MAC Cihazlar İçin Kurulum

### 1 - Gereksinimler

Dijital İmza uygulamasını cihazınıza kurmadan önce aşağıda belirtilen Java kütüphanesinin cihazınızda kurulu olması gerekmektedir.
JDK (Java Development Kit). Bu kütüphaneyi aşağıdaki linkten cihaz türünüze uygun olanı seçerek indirebilirsiniz. [İndirmek için <strong>tıklayınız.</strong>](https://portal.synergynow.io/#/_redirect/cIOwCvluZ7fJ3Np4y3YO5c)

Yukarıdaki linkten Java'yı indirdikten sonra indirilenler klasörünüzde klasörünüzde görseldekine benzer bir kurulum dosyası olacaktır. Bu kurulum dosyasını açınız.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb60d56b-da2a-4996-8a73-badda90c532b)

Bu pakete çift tılayarak açın.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83309ed7-acf2-4bb9-b624-88eb72f63fa8)


Karşınıza çıkan bu ekranda open seçeneğini seçerek devam edin.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload98f3a4b5-340f-496e-8cc1-0fc9123b8a2b)

Install’a basarak kurulumu yapabilirsiniz.

<br/>
<strong>Hatırlatma :</strong> JAVA'yı kurduktan sonra lütfen versiyonu kontrol etmek için aşağıdaki komutu uygulayın.

```sh 
	java -version
```
Eğer halen "1.8.0_361" sürümünü göremiyor ve başka bir sürüme ait bilgiler görüyorsanız bu durum cihazınızda birden fazla java sürümü olduğunu göstermektedir. Bu durumda bilgisayarınızın default olarak kullanacağı Java sürümünü belirtmeniz gerekiyor veya diğer java sürümünü silmeniz gerekmektedir. Diğer Java sürümlerini silmek için MacintoshHD'yi açıp Library/Java/VirtualMachines klasörüne gidiniz, buradaki diğer java sürümlerini siliniz. Daha sonrasında tekrar terminal yardımı ile java versiyonu kontrolü yapınız. Eğer artık doğru sürümü görüntülüyorsanız diğer kurulum adımlarına geçebilirsiniz.

### 2 - Kart Okuyucu Sürücülerinin Kurulumu

Elektronik imza uygulamasını kullanabilmek için USB port erişim yetkilerini yöneten ve USB port çeşidine göre yetki sağlayan kart okuyucu ve kart yazılımlarının kurulu olması gerekmektedir. 

Akis kartlar için sürücü yazılımınızı linkteki adresten [<strong>KamuSM</strong>](https://kamusm.bilgem.tubitak.gov.tr/islemler/surucu_yukleme_servisi/)'ye giderek indirebilirsiniz. 
Bu adrese gittiğinizde bilgisayarınızın <strong>işletim sistemini</strong> , <strong>işletim sistemi versiyonunu</strong> ve  <strong>E-imza Token modelinizi</strong> seçerek  size sunulan  2 farklı sürücüyü  indirip kurunuz. Eğer kart okuyucunuza ait sürücü çıkmaz ise  e-imzanızın kullanım kılavuzuna veya tedarikçinize başvurabilirsiniz.

<img src="https://docsbimser.blob.core.windows.net/imagecontainer/ds-mac-other-composites1-c67536d0-bea5-48b4-8488-40e7dd5b0312.png" alt="Bimser Çözüm" style={{border: '3px solid #dee0df', borderRadius:'15px', boxShadow:'3px 5px #dee0df', margin:'10px 0'}}/>

<p align='center' style={{fontWeight:'bold', marginTop:'10px', fontSize:'17px'}}>Mac sürümünüze göre seçimleri yaptıktan sonrasında imza sertifika cihazınızın türünü seçmeniz gerekmektedir.</p>

<img src="https://docsbimser.blob.core.windows.net/imagecontainer/ds-mac-other-composites2-2147747d-ee25-4c23-950e-2e3a70b8c6b8.png" alt="Bimser Çözüm" style={{border: '3px solid #dee0df', borderRadius:'15px', boxShadow:'3px 5px #dee0df', margin:'10px 0'}}/>

<p align='center' style={{fontWeight:'bold', marginTop:'10px', fontSize:'17px'}}>Sırayla şu iki uygulamayı da kurmanız gerekmektedir: Akıllı kart sürücüsü ve Kart okuyucu sürücüsü</p>

### 3 - Dijital İmza Uygulamasının İndirilmesi ve Kurulumu - Mac

DSClient Mac Os versiyonunu indirmek için [<strong>tıklayınız.</strong>](https://portal.synergynow.io/#/_redirect/hlO9sR8DLDfKwYGZjQrtVn)

Dijital İmza uygulamasının kurulumu için Mac cihazlarda bulunan terminal uygulamasından faydalanacağız.

Terminal uygulamasını açmak için LaunchPad'e girin.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f925b83-1779-467e-af49-19d396be3496)


Arama kısmına terminal yazın.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadefe9d7ed-3147-4189-a276-4f3ccf8a9f79)

Gelen ekranda gördüğünüz terminal uygulamasını açın.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4551e8e-bdf5-46e3-b9cd-a59ac87683b6)

Karşınıza yukardaki görseldekine benzer gibi bir ekran gelecektir.

Bu ekranda şu komutu yazın :
```sh 
	bash
```

Ve bir boşluk bırakın

Ardından Setup Files klasöründeki DSClientMac.sh dosyasını tutup bu ekrana sürükleyin

```sh 
	bash /Users/username/Desktop/SetupFiles/DSClientMac.sh
```

Kod satırı yukardaki örneğe benzer şekilde görülecektir. Tek fark dosya konumunuz olacaktır.
Kod satırının sonudaki 1 adet boşluğu silmeniz gerekmektedir.
Ardından Entr'a basarak komutu uygulayın.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16334685-fda9-4f80-a6dc-26b133c61a0a)

İşlem başarılı olması durumunda Terminal görüntüsü yukardaki görseldeki gibi olacak ve terminal bir alt satıra geçecektir.
Herhangi bir sorunla karşılaşmanız halinde program kendi işlem ve hata kayıtlarını oluşturmaktadır. Bu dosyalardaki kayıt mesajlarını iletmeniz durumunda sorunlarınız daha hızlı çözüme kavuşacaktır.



### 4 - Log Kayıtlarına  Nasıl Ulaşılır - Mac

Bu dosyalara erişmek için Cihazınızın masaüstünde bulunan diske erişin (Macintosh HD) bu disk adı sizin cihazınızda farklı olabilir.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3190d89-5cfb-4db0-b379-fe33dd5f76f0)

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31938a05-f973-4092-9c4d-75675dcccd80)

Karşınıza çıkan bu ekranda Cmd + shift + . tuşlarına aynı anda basarak gizli klasörleri görünür hale getiriniz.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41253da5-751b-4aa1-9b6f-810cce5e957f)

Gizli klasörleri görünür hale getirdiğinizde karşınıza görseldeki gibi bir ekran gelecektir.



![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3909ec66-2c0f-44a6-9436-b0a4429debfa)

Soluk renkli olarak görünen usr klasörünü açın.


![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcafca8d5-1635-40f0-b56c-d3df545fc9b0)

Daha sonra local klasörünü açın.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6571b604-38f3-427a-97c0-9e87c40980aa)

Local klasörü içerisindeki bin klasörünü açın.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46bffb3d-c2f0-464a-a8d0-257401136721)

Bin klasöründe SetupFiles klasörünü bulun ve açın.

Setupfiles içerisinde “servicelog.err.log” dosyası mevcuttur.
Kurulum sırasında veya bilgisayarınızı yeniden başlattıktan sonra dijital imza servisi herhangi bir hata ile karşılaşırsa buraya kayıt edecektir.
Bu dosyayı çift tıklayarak text editör ile açabilirsiniz.

Programa ait hata dışı kayıtlar yine aynı klasörde bulunan “servicelog.out.log” dosyasında tutulmaktadır.



Dijital imza servisini  durdurmak zorunda kalırsanız  şu adımları izleyebilirsiniz.

Teminali açın
Servisi durdurmak için :  

```sh 
	sudo launchctl stop  com.dsclient.bms
```
komutunu uygulayın.

 
Servisi kaldırmak için durdurma komutunu uyguladıktan sonra
```sh 
	sudo launchctl unload  /Library/LaunchDaemons/com.dsclient.bms.plist
```
komutunu uygulayın.
### 5 - Kart Okuyucu Bulunamadı veya Sertifikalar Okunamadı Hatası 

Eğer sisteme giriş yaparken kart okuyucu cihaz ve sertifikalar listelenmiyorsa aşağıdaki adımları izleyiniz.


1.  https://kamusm.bilgem.tubitak.gov.tr/islemler/surucu_yukleme_servisi/ adresinden İşletim sisteminizi ve size uygun kart okuyucu cihazı seçiniz. Bu sayfada size 2 adet uygulama gösterilecektir. Akıllı kart sürücüsü ve Kart okuyucu sürücüsü'ni indirip cihazınıza kurunuz.


2. Eğer  E-Güven , Gemalto , SafeNet , Thales markalarına ait kart okuyucular kullanıyorsanız Cihazınızda SafenetAuthenticationClient'in kurulu olduğundan emin olunuz. 

3. Eğer halen kart okuyucularınız görüntülenmiyorsa lütfen java versiyonunuzun  <strong>1.8.0_361*</strong> olduğundan emin olunuz.

