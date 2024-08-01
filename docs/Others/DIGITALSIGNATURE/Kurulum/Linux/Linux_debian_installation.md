# Linux Debian Kurulumu
## Linux (Debian ve Pardus) Cihazlar İçin Kurulum

### 1 - Gereksinimler

Dijital İmza uygulamasını cihazınıza kurmadan önce aşağıda belirtilen Java kütüphanesinin cihazınızda kurulu olması gerekmektedir.
Cihazınızda Javanın kurulu olup olmadığını ve varsa versiyon bilgisini öğrenmek için

```sh 
	java -version
```
Komutunu uygulayabilirsiniz. Eğer openjdk-11-jre sürümü yüklü değilse aşağıdaki talimatları takip ederek yükleyebilirsiniz.

JRE (Java Runtime Environment) . Javayı kurmak için aşağıdaki kodu Linux cihazınızın terminalinde çalıştırabilirsiniz.

```sh 
	sudo apt-get install -y openjdk-11-jre
```

Yukarıdaki kodu uyguladığınızda size sudo kullanıcı şifresi soracaktır şifrenizi giriniz. Eğer sudo kullanıcısı olmadığınızı belirten bir mesaj alırsanız aynı terminalde önce

```sh 
	su
```
kodunu uygulayın ve şifrenizi girin daha sonra

```sh 
	apt-get install -y openjdk-11-jre
```
komutunu uygulayarak Javayı kurabilirsiniz.

<strong>Not :</strong> kurulum işlemlerinin başarılı bir şekilde yürüyebilmesi için sudo kullanıcı olmanız tavsiye edilmektedir. Bu konuyla ilgili BT biriminizden destek alabilirsiniz.
<br/>
<strong>Hatırlatma :</strong> JAVA'yı kurduktan sonra lütfen versiyonu kontrol etmek için aşağıdaki komutu uygulayın.

```sh 
	java -version
```
eğer halen openjdk-11-jre sürümünü göremiyor ve başka bir sürüme ait bilgiler görüyorsanız bu durum cihazınızda birden falza java sürümü olduğunu göstermektedir. Bu durumda bilgisayarınızın default olarak kullanacağı Java sürümünü belirtmeniz gerekiyor. Bunun için 

```sh 
	sudo update-alternatives –config java
```
komutuyla uygulaın, açılan listede listelenen  birden fazla versiyon arasından  çalışmasını istediğiniz (DSClient Debian ve Pardus sürümleri için OpenJDK-11-JRE ) Java sürümünü seçebilirsiniz. 

### 2 - Kart Okuyucu Sürücülerinin Kurulumu

Dijital İmzanızı kullanabilmeniz için kart okuyucu ve kart yazılımlarının bilgisayarınızda yüklü olması gerekir.

<br/>

Akis kartlar için sürücü yazılımınızı linkteki adresten [<strong> KamuSM </strong>](https://kamusm.bilgem.tubitak.gov.tr/islemler/surucu_yukleme_servisi) 'ye giderek indirebilirsiniz. 
Bu adrese gittiğinizde bilgisayarınızın <strong>işletim sistemini</strong> , <strong>işletim sistemi versiyonunu</strong> ve  <strong>E-imza Token modelinizi</strong> seçerek  size sunulan  2 farklı sürücüyü  indirip kurunuz. Eğer kart okuyucunuza ait sürücü çıkmaz ise  e-imzanızın kullanım kılavuzuna veya tedarikçinize başvurabilirsiniz.

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

### 3 - Dijital İmza Uygulamasının İndirilmesi ve Kurulumu - Debian

DSClient Debian versiyonunu indirmek için [<strong>tıklayınız.</strong>](https://portal.synergynow.io/#/_redirect/lMA6PnodvPfl7MSuB4yZy)

Dijital İmza uygulamasının kurulumu için Linux (Debian) cihazlarda bulunan terminal uygulamasından faydalanacağız.

Bunun için SetupFiles klasörünüzde boş bir alana sağ tıklayın ve gelen menüden "Terminalde Aç" veya "Open in Terminal"
seçeneğini seçin.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe391b17-ebef-470a-91eb-51398cac161a)


Terminali açtığınızda aşağıdaki görsele benzer bir ekran gelecektir. 

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0f9b029-db13-4197-b089-736d2186c9b5)

Bu ekranda şu komutu yazın :
```sh 
	su
```
Ardından gelen parola ekranında parolanızı girin ,bu size kurulum sırasında gereken izinleri sağlayacaktır.

Bu ekranda şu komutu yazın :
```sh 
	bash
```

Ve bir boşluk bırakın

Ardından Setup Files klasöründeki DSClientDebian.sh dosyasını tutup bu ekrana sürükleyin

```sh 
	bash /home/username/Downloads/SetupFiles/DSClientDebian.sh
```
Kod satırı yukardaki örneğe benzer şekilde görülecektir. Tek fark dosya konumunuz olacaktır.
Kod satırının sonudaki 1 adet boşluğu silmeniz gerekmektedir.
Ardından Enter'a basarak komutu uygulayın.



![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload880f2ed8-1eae-45ba-8228-cd75f762ed94)

İşlem başarılı olması durumunda Terminal görüntüsü yukardaki görseldeki gibi olacak ve terminal bir alt satıra geçecektir.
Herhangi bir sorunla karşılaşmanız halinde program kendi işlem ve hata kayıtlarını oluşturmaktadır. Bu dosyalardaki kayıt mesajlarını iletmeniz durumunda sorunlarınız daha hızlı çözüme kavuşacaktır.



### 4 - Log Kayıtlarına  Nasıl Ulaşılır - Debian

Örnek Debian11 üzerinden anlatılmıştır.

Yan menüden Files'ı açın.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload561baa93-4c64-4575-87a7-62386b37a05c)

Açılan pencerede other locations’u seçin.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e04a97b-bdb5-4d08-a1b3-d6241550847e)


Computer’i açın

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc09c8798-086b-416a-83d8-1dabe04a5c22)

opt'yi açın.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4dc6c23b-06ad-4bda-91d4-f9691f08fed7)

SetupFiles 'ı açın

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload14e5e33d-f63b-486d-9a25-0232c59b1197)


Setupfiles içerisinde “servicelog.err.txt” dosyası mevcuttur.
Kurulum sırasında veya bilgisayarınızı yeniden başlattıktan sonra dijital imza servisi herhangi bir hata ile karşılaşırsa buraya kayıt edecektir.
Bu dosyayı çift tıklayarak text editör ile açabilirsiniz.

Programa ait hata dışı kayıtlar yine aynı klasörde bulunan “servicelog.out.txt” dosyasında tutulmaktadır.

-
Dijital imza servisini  durdurmak zorunda kalırsanız  şu adımları izleyebilirsiniz.

Teminali açın
Önce yetki komutunu yazın ve parolanızı girin:

```sh 
	su
```

Servisi durdurmak için :  

```sh 
	 systemctl stop  dsclientservice.service
```
komutunu uygulayın.

Sizden parolanızı isteyebilir, parolanızı girin.
 
Servisi kapatmak için durdurma komutunu uyguladıktan sonra
```sh 
	 systemctl disable  dsclientservice.service
```
komutunu uygulayın.

Servisi tamamen cihazınızdan silmek için kapatma komutunu uyguladıktan sonra
```sh 
	 rm -r /lib/systemd/system/dsclientservice.service
```
komutunu ve bu kaldırma işlemininden kaynaklı değişikliklerin  kaydedilmesi için

```sh 
	systemctl daemon-reload
```

bu komutu uygulayın.


### 5 - Kart Okuyucu Bulunamadı veya Sertifikalar Okunamadı Hatası 

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