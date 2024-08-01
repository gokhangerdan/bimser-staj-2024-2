---
sidebar_label: Windows Kurulumu
sidebar_position: 1
custom_edit_url: ""
---
# Windows Kurulumu
## Windows Cihazlar İçin Kurulum

### 1- Gereksinimler

Dijital İmza uygulamasını cihazınıza kurmadan önce aşağıda belirtilen Java kütüphanesinin ve .NET Core 3.1'in cihazınızda kurulu olması gerekmektedir.

#### JRE (Java Runtime Environment) Kurulumu
JRE (Java Runtime Environment) aşağıdaki linkten cihaz türünüze uygun olanı seçerek indirebilirsiniz. [İndirmek için <strong>tıklayınız.</strong>](https://www.java.com/tr/download/manual.jsp)

Yukarıdaki linkten Java'yı indirdikten sonra indirilenler klasörünüzden kurulum dosyası çalıştırınız.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b3034bb-de50-499d-a550-459f1a8a6675)


Karşınıza çıkan bu ekranda 'install' seçeneğini seçerek devam edin.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81306133-840b-44d9-ab6b-75a078f463ff)

Yüklenme ekranı geçtikten sonrasında kurulumunuz tamamlanacaktır.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba31721f-4cae-4be9-819e-3c14dd4c50fb)

Kurulumunuz başarıyla tamamlandı.

#### Sistem Ortamı Değişkenlerinin Ayarlanması
JRE kurduktan sonrasında, JRE kurulum yerini sistem ortamı değişkenlerine 'JAVA_HOME' olarak eklememiz gerekmektedir. 
Aşağıdaki ekran resmine bakarak ekleyebilirsiniz

![title](https://docsbimser.blob.core.windows.net/imagecontainer/javahome-07be036f-614c-4e03-8fd0-1c6fe6eee1c1.png)

Ekledikten sonrasında JRE'nin doğru kurulup kurulmadığını anlamak için alttaki ekran resmindeki adımı doğrulayanız.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/cacerts-23970656-ddcb-41cd-aee1-b9f1375f0b44.png)

#### ASP.NET Core Runtime 3.1
ASP.NET Core Runtime 3.1 versiyonunu aşağıdaki linkten cihaz türünüze uygun olanı seçerek indirebilirsiniz. [İndirmek için <strong>tıklayınız.</strong>](https://dotnet.microsoft.com/en-us/download/dotnet/3.1)

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload57c25ced-a044-4ef1-b9b7-b548f3a9a244)

Burada build olanını değil sağ tarafta işaretli olan kısımda işletim sisteminize uygun olanını seçerek indiriniz. Ardından indirdiğiniz kurulum dosyasını açınız.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10770b5d-5041-43aa-a9b9-d5f7d563341c)

Gerekli alanı işaretleyip 'Yükle' butonuna basıp, kurulumu başlatınız.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0156f2e7-ed3d-4d70-9c4e-ca465c7de067)

Yüklenme tamamlandıktan sonra kurulum başarıyla tamamlanmış olacaktır.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91bb5b2f-5a80-4e2d-92e2-073bd9697ff4)

Sırayla bu işlemleri yaptıktan sonrasında kurulumu başarıyla tamamlamış bulunmaktasınız. 'Kapat' butonuna basarak kapatınız.

Uygulamamızı kullanırken ASP.NET Core Runtime 3.1 ile çalışmanızı öneriyoruz. Ancak şirket içi prosedürlerden kaynaklı ASP.NET Core Runtime 3.1 kullanılamaması durumunda ASP.NET Core Runtime 7.0 ı <a href ="https://dotnet.microsoft.com/en-us/download/dotnet/7.0"><b>bu linkten</b></a> indirip kurabilirsiniz.

<img src="https://docsbimser.blob.core.windows.net/imagecontainer/aspnet-downloadlink1-2e33ac59-6f92-4801-8016-7cc072951334.png" alt="Bimser Çözüm" style={{border: '3px solid #dee0df', borderRadius:'15px', boxShadow:'1px 2px #dee0df', margin:'10px 0'}}/>

#### Sürücülerin Kurulması

Kart okuyucunuzun ve kartınızın Windows cihazınız tarafından algılanabilmesi için Akıllı Kart ve Kart Okuyucu yazılımları gerekmektedir. Cihazınızda daha önce dijital imza kullanmadıysanız veya Palma uygulamasını kurmadıysanız [<strong>bu linkten</strong>](https://kamusm.bilgem.tubitak.gov.tr/islemler/surucu_yukleme_servisi/) KamuSM adresine giderek cihazınıza uygun Kart Okuyucu ve Akıllı Kart sürücüsünü indirerek cihazınıza kurmanız gerekmektedir.

TürkTrust'a ait Kart Okuyucu kullanıyorsanız Palma uygulamasını da kurmanız tavsiye edilmektedir.
Gemalto Marka Kart okuyucularınız için Safenet Authentication Client'i kurmanız tavsiye edilmektedir.

<br/>

Artık DSClient'in kurulumuna geçebilirsiniz.

### 2- DSClient Kurulumu

DSClient .NET CORE versiyonlarına göre farklılık göstermektedir. Hangisi ile çalışıyor iseniz onu indirmeniz gerekmektedir. 

<table >
    <tr>
        <th colspan="2">İndirme Linkleri</th>
    </tr>
    <tr>
    <td><a href="https://portal.synergynow.io/#/_redirect/XailsZSvf6feV5FIWSuCTd" >DSClient Windows .NET CORE 3.1</a></td>
    <td><a href="https://portal.synergynow.io/#/_redirect/z3A753gCaVfL7BQMD8Z8Qu" >DSClient Windows .NET CORE 7.0</a></td>
    </tr>
</table>


İndirdikten sonrasında kurulum dosyasını rardan çıkarıp açınız ve ekran görüntülerindeki adımları uygulayınız.

<!-- ![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48f17684-674c-47ec-9a53-92b93cd89b5d)

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload504cc180-40da-4c8c-838e-c9b438c76990) -->

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66e21432-d514-46cb-8278-2d297dd3d2bc)

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8997fa9f-f1f4-4a54-9ab9-ff88c5162eb7)

Yüklenme ekranının tamamlanmasını bekleyiniz.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc7f0716-a038-4a94-8ee2-054320161392)

Başarılı bir şekilde kurulumu gerçekleştirdiniz. DSClient Windows Servisi olarak çalışmaktadır.

### 3- Log Dosyalarının Konumu - Loglara nasıl ulaşabilirim?

Uygulamanın dosyalarının bulunduğu konum: C:\Program Files\DSClient\

Log dosyasının konumu: C:\Program Files\DSClient\log

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1dd684d-84a7-4d35-be2f-c03f817c4651)

Burada tarihlere göre logları görebilirsiniz. Bir sorunla karşılaştığınızda en son, güncel tarihli log dosyasını bizimle paylaşmanız yeterli olacaktır.

### 4- DSClient'i Bilgisayarımdan Nasıl Silerim/Kaldırırım?

Eğer işletim sisteminiz türkçe ise 'Program' yazıp, 'Program Ekle ve Kaldır'ı seçmeniz gerek. Devamında izleyeceğiniz adımlar aynıdır. Gerekli adımları uygulayarak DSClienti kaldırabilirsiniz.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f6024dd-2782-405d-9bad-9dbacedd7d4b)

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40b278c3-5a08-4cd5-8337-35df8e086d0d)

En son 'Uninstall'a bastıktan sonrasında ekrana gelen yönetici iznini veriniz.

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbb616463-c4eb-46cc-b7d8-09b96f4311e9)

'Ok' butonuna bastıktan sonrasında bilgisayarınız yeniden başlayacaktır. Başarılı bir şekilde DSClienti kaldırmış bulunmaktasınız.


