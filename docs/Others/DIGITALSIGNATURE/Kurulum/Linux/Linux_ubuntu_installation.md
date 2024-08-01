# Linux Ubuntu Kurulumu
## Linux (Ubuntu) Cihazlar İçin Kurulum

### 1 - Gereksinimler

Dijital İmza uygulamasını cihazınıza kurmadan önce aşağıda belirtilen Java kütüphanesinin cihazınızda kurulu olması gerekmektedir.
JRE (Java Runtime Environment). Javayı kurmak için aşağıdaki kodu Linux cihazınızın terminalinde çalıştırabilirsiniz.

```sh 
	sudo apt-get install openjdk-8-jre
```

Yukarıdaki kodu uyguladığınızda size sudo kullanıcı şifresi soracaktır şifrenizi giriniz. Eğer sudo kullanıcısı olmadığınızı belirten bir mesaj alırsanız aynı terminalde önce

```sh 
	su
```
kodunu uygulayın ve şifrenizi girin daha sonra

```sh 
	apt-get install openjdk-8-jre
```
komutunu uygulayarak Javayı kurabilirsiniz.

Not: kurulum işlemlerinin başarılı bir şekilde yürüyebilmesi için sudo kullanıcı olmanız tavsiye edilmektedir. Bu konuyla ilgili BT biriminizden destek alabilirsiniz.
### 2 - Kart Okuyucu Sürücülerinin Kurulumu

Dijital İmzanızı kullanabilmeniz için kart okuyucu ve kart yazılımlarının bilgisayarınızda yüklü olması gerekir.

<br/>

Akis kartlar için sürücü yazılımınızı linkteki adresten [<strong>KamuSM</strong>](https://kamusm.bilgem.tubitak.gov.tr/islemler/surucu_yukleme_servisi/)'ye giderek indirebilirsiniz. 
Bu adrese gittiğinizde bilgisayarınızın <strong>işletim sistemini</strong> , <strong>işletim sistemi versiyonunu</strong> ve  <strong>E-imza Token modelinizi</strong> seçerek  size sunulan  2 farklı sürücüyü indirip kurunuz. Eğer kart okuyucunuza ait sürücü çıkmaz ise  e-imzanızın kullanım kılavuzuna veya tedarikçinize başvurabilirsiniz.

Akis'i kurmak için aşağıdaki adımları izleyebilirsiniz.

Akıllı kart sürücüsü Akis in .deb uzantılı dosyasını arşivden çıkarın ve aşağıdaki kodu terminalde yazdıktan sonra dosyayı terminalin üzerine sürükleyip bırakın.

Kart okuyucu sürücüsü klasöründe ise birden fazla klasör olabilir bu klasörleri açıp işletim sisteminize en yakın olanın içerisindeki .deb uzantılı paketi yükleyiniz.

```sh 
		sudo dpkg -i 
``` 
<br/>

Eğer  E-Güven , Gemalto , SafeNet , Thales markalarına ait kart okuyucular kullanıyorsanız Cihazınızda SafenetAuthenticationClient'ı kurmanız gerekecektir. Safenet Authentication Client 10.8 sürümünü indirmek için  [<strong>tıklayınız.</strong>](https://portal.synergynow.io/#/_redirect/1i4nIJSoX7fjwRWlJ2ptYe)

<br/>

İndirdiğiniz klasördeki .deb uzantılı dosyasını arşivden çıkarın ve aşağıdaki kodu terminalde yazdıktan sonra dosyayı terminalin üzerine sürükleyip bırakın ve komutu uygulayarak yükleme işlemini yapın.

```sh 
		sudo dpkg -i 
``` 

Bu işlemlerden sonra bilgisayarınızın E-imzanızı gördüğünden emin olmak için terminalden 
 
 ```sh 
		akia 
```
komutunu uygulayarak kart okuyucunuzun tanınıp tanınmadığını görebilir ve içeriğini görüntüleyebilirsiniz.



### 3 - Dijital İmza Uygulamasının İndirilmesi ve Kurulumu - Linux

DSClient Linux Ubuntu versiyonunu indirmek için [<strong>tıklayınız.</strong>](https://portal.synergynow.io/#/_redirect/JJrhyLDhh9f12DPn6G8j8i)

Dijital İmza uygulamasının kurulumu için Linux cihazlarda bulunan terminal uygulamasından faydalanacağız.

Bunun için SetupFiles klasörünüzde boş bir alana sağ tıklayın ve gelen menüden "Terminalde Aç" veya "Open in Terminal"
seçeneğini seçin.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd63a8877-fb37-4665-9631-85395b359478)


Terminali açtığınızda aşağıdaki görsele benzer bir ekran gelecektir. 

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6aba1558-e38b-4532-a82b-da70a46319c8)



Bu ekranda şu komutu yazın :
```sh 
	bash
```

Ve bir boşluk bırakın

Ardından Setup Files klasöründeki DSClientMac.sh dosyasını tutup bu ekrana sürükleyin

```sh 
	bash /home/username/Downloads/SetupFiles/DSClientLinux.sh
```
Kod satırı yukardaki örneğe benzer şekilde görülecektir. Tek fark dosya konumunuz olacaktır.
Kod satırının sonudaki 1 adet boşluğu silmeniz gerekmektedir.
Ardından Entr'a basarak komutu uygulayın.

Sizden kullanıcı şifrenizi girmeniz istenecektir. 
Burada şuna dikkat edin ,linux terminalde şifrenzi yazdığınızda sanki hiçbirşey yazmıyormuş gibi görülebilir, bu normaldir.Şifrenizi yazın ve enter'a basıp onaylayın'

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf15b438e-c1e7-4155-a42d-26bd787dc86e)

İşlem başarılı olması durumunda Terminal görüntüsü yukardaki görseldeki gibi olacak ve terminal bir alt satıra geçecektir.
Herhangi bir sorunla karşılaşmanız halinde program kendi işlem ve hata kayıtlarını oluşturmaktadır. Bu dosyalardaki kayıt mesajlarını iletmeniz durumunda sorunlarınız daha hızlı çözüme kavuşacaktır.



### 4 - Log Kayıtlarına  Nasıl Ulaşılır - Linux

Örnek Ubuntu üzerinden anlatılmıştır.

Yan menüden Files'ı açın.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload211255ab-3534-4b94-889c-1de447ffafc5)

Açılan pencerede other locations’u seçin.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload479e8dbc-b388-4f6b-8331-17a6d56df183)


Computer’i açın

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7d48231-e413-48e9-be82-3520bc7799c5)

Usr'ı açın.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a5a118c-8004-4740-b7aa-90b5bcd11e8f)

Bin 'i açın

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload391c0e9d-3dbb-4736-a239-b1792025a8e5)

Bin içerisinde bulunan Setupfiles'ı açın

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload370886f6-c363-402c-84cb-47722ac8869b)


Setupfiles içerisinde “servicelog.err.txt” dosyası mevcuttur.
Kurulum sırasında veya bilgisayarınızı yeniden başlattıktan sonra dijital imza servisi herhangi bir hata ile karşılaşırsa buraya kayıt edecektir.
Bu dosyayı çift tıklayarak text editör ile açabilirsiniz.

Programa ait hata dışı kayıtlar yine aynı klasörde bulunan “servicelog.out.txt” dosyasında tutulmaktadır.



### 5- Kart Okuyucu Bulunamadı veya Sertifikalar Okunamadı Hatası 

Eğer sisteme giriş yaparken kart okuyucu cihaz ve sertifikalar listelenmiyorsa aşağıdaki adımları izleyiniz.

1. Aşağıda belirtilen kodu terminalinizde uygulayınız.

	```sh 
		sudo apt-get update

	``` 
	ve

	```sh 
		sudo apt-get install pcscd pcsc-tools opensc opensc-pkcs11 libpam-pkcs11 libstdc++6 libccid libusb-0.1-4 libpcsclite1 libssl1.1 pkcs11-data  openssl libssl-dev libcrypto++8

	``` 

	bu kodları çalıştırdıktan sonra bir hata oluştuysa 

	```sh 
		apt-get -f install
	``` 

	komutunu uygularsanız sorun çözülecektir.

	Daha sonra

	```sh 
		sudo systemctl enable pcscd
	``` 

komutunu uyguladığınızda kart okuyucunuz ve sertifikalarınız sistem tarafında görünür hale gelecektir.

Bazı durumlarda bilgisayarınıızı yeniden başlatmanız gerekebileceğinden kurulumların sonrasında yeniden başlatmanız tavsiye edilmektedir.


2. Eğer 1. yöntem sizin için faydalı olmadıysa https://kamusm.bilgem.tubitak.gov.tr/islemler/surucu_yukleme_servisi/ adresinden İşletim sisteminizi ve size uygun kart okuyucu cihazı seçiniz. Bu sayfada size 2 adet uygulama gösterilecektir. Akıllı kart sürücüsü ve Kart okuyucu sürücüsü'ni indirip cihazınıza kurunuz.

Kurmak için aşağıdaki adımları izleyebilirsiniz.

Akıllı kart sürücüsü Akis in .deb uzantılı dosyasını arşivden çıkarın ve aşağıdaki kodu terminalde yazdıktan sonra dosyayı terminalin üzerine sürükleyip bırakın.

Kart okuyucu sürücüsü klasöründe ise birden fazla klasör olabilir bu klasörleri açıp işletim sisteminize en yakın olanın içerisindeki .deb uzantılı paketi yükleyiniz.

```sh 
		sudo dpkg -i 
``` 


3. Eğer  E-Güven , Gemalto , SafeNet , Thales markalarına ait kart okuyucular kullanıyorsanız Cihazınızda SafenetAuthenticationClient'in kurulu olduğundan emin olunuz. Safenet Authentication Client 10.8 sürümünü indirmek için  [<strong>tıklayınız.</strong>](https://portal.synergynow.io/#/_redirect/1i4nIJSoX7fjwRWlJ2ptYe)

4. Eğer halen kart okuyucularınız görüntülenmiyorsa lütfen java versiyonunuzun  <strong>openjdk-11-jre</strong> olduğundan emin olunuz.

5. Eğer  log kayıtlarınızda " libeTKPCS11.so : paylaşımlı nesne açılamıyor " hatası alırsanız aşağıdaki kodu terminalde uygulayın().

```sh 
		sudo mv /usr/lib/libeTPkcs11.so /usr/lib/libeTPKCS11.so
```  

6. Eğer " init_openssl_crypto " hatası alınırsa aşağıdaki kodu terminalde uygulayın.

```sh 
		sudo ln -s /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 /usr/lib/libcrypto.so.6  
```  