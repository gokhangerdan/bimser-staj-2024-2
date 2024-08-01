---
sidebar_label: Proje Geliştirme ve Kodlama Standartları
sidebar_position: 2
custom_edit_url: ""
---

# Proje Geliştirme ve Kodlama Standartları

Entegre geliştirme ortamı, kod yazmaya gerek kalmadan bir çok işlemi yerine getirebilecek hazır nesneler sunmaktadır. Geliştirme yapacak kullanıcı, bu nesneler sayesinde ihtiyaç duyulan süreç ve form tasarımlarını, kod yazmaya gerek duymadan gerçekleştirebilir. Geliştirme ortamı aynı zamanda, daha özelleştirilmiş kontroller ve işleyişler gerçekleştirmek isteyen geliştiricilerin kendi tasarladıkları senaryoları yürütebilmeleri için de kodlarını yazabilme opsiyonunu geliştiricilere sunmaktadır.

Geliştirme ortamını kullanan birden çok geliştirici olduğunda veya mevcut proje geliştiricisi değiştiğinde, sistemde benimsenmiş belirli bir proje geliştirme ve kodlama standardı mevcut değilse organizasyon bünyesindeki her bir proje, farklı formatlarda, anlaşılması ve yorumlanması mümkün olmayan karmaşık yapılarda olabilir. Organizasyonda bulunan tüm projelerin belirlenen bir formatta geliştirilmesi amacı ile bu başlık altında, geliştirme ortamında oluşturulan projelerde uyulması gereken bazı standartlardan bahsedilecektir.

## Çözüm ve Proje İsimlerinin Anlamlı Verilmesi

Entegre Geliştirme Ortamında oluşturulan bir çözümün, altında hangi tip projeleri barındırdığı veya bir projenin ne projesi olduğu bilgileri verilen isimlendirme ile anlaşılabilir olmalıdır. Böylece başka bir geliştirici projeleri incelemek istediğinde veya projeyi geliştiren kişi aradan geçen zamanın ardından geliştirdiği bir projeyi bulmaya çalıştığında, tek tek projeleri açıp ne projesi olduğunu anlamaya çalışarak zaman kaybetmemiş olacaktır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9903a076-169e-49f3-bb51-1230d512aeec)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd014a7bf-d7bb-47ae-9281-4039ce64159a)

</div>

:::

## Harici Bağlantı ve Sorgu İsimlerinin Anlamlı Verilmesi

Geliştirme arayüzünde oluşturulan harici bağlantı isimleri ve süreçlerde kullanılmak üzere oluşturulmuş sorgu isimleri anlamlı olmalıdır. Oluşturulan harici bağlantının, hangi harici kaynak ile yapıldığı veya sorgunun hangi verileri getirdiği bilgisi, verilen isimlendirme ile anlaşılabilmelidir. Böylece aynı bağlantı ve sorgu başka bir nesnede ya da projede kullanılmak istendiğinde anlaşılmaları vakit kaybına sebep olmayacaktır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload508703f3-7668-4d44-91ad-0e2fe26efa36)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b2463b1-e9dc-49c4-a18c-3f7f10f779ba)

</div>

:::

## Kod Girintileri ve Hizalamalara Dikkat Etme

Geliştirme Arayüzü kod editör ekranlarında yazılan kodlarda methodlar, if-else, try-catch gibi özel bloklar ve değer tanımlamaları arasında bulunan girintilere dikkat edilmelidir. Böylece daha okunaklı ve anlaşılır kod blokları oluşacaktır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload98b3fd12-5c79-4d06-a5e0-f7bdb548fff9)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59e8c708-608e-4f1c-a2cf-572edafb9ed5)

</div>

:::

## Boşluk Kullanımı

Birden fazla değişken tanımlarken değişken adları arasında virgülden sonra boşluk kullanılması, blok deyimler içerisinde, değişkenler ve operatörler arasında boşluk kullanılması, fonksiyon parametreleri arasında virgülden sonra boşluk kullanılması, kodlarınızın daha okunaklı olmasını ve belirli bir kuralla dahil edilmesini sağlayacaktır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadebcd772c-f43d-4fea-8f0c-bea3be5878ed)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07dfec9c-7445-4541-add8-179b8d9aa67e)

</div>

:::

## Blok Açıklama Kullanımları

Blok açıklamaları fonksiyon, modül ya da proje gibi kodların başına, daha sonraki kullanımlara gerekli olabilecek açıklamalar girilmesi için kullanılır. Açıklamalar, çok detaya girilmeden, ilgili kod bloğunun ne iş yaptığı ve gerekli diğer bilgileri içerecek şekilde yazılmalıdır. Blokta herhangi bir değişiklik yapılırsa açıklama alanı mutlaka güncellenmelidir. Açıklama blokları, kodun anlaşılır olması açısından büyük önem taşır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd34544ff-d3e0-4f11-aff9-8149785519dd)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73822793-72b3-401b-adf5-6d7c2baa65af)

</div>

:::

## Tek Satırlık Açıklamalar

Tek satırlık açıklamalar, alt kısımda bulunan kod bloğunu açıklar nitelikte, belirli işlemlerin gerçekleştiği kod bloklarının başına yazılmalıdır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8dc33cee-5686-4c57-888c-a4d27dfe558c)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb6476bb2-cc06-4413-859e-905523d12eff)

</div>

:::

## Satır İçi Açıklama Kullanımı

Satır içi açıklamalar, sadece bulunduğu satırdaki ifadeyi açıklar nitelikte ve sadece o satıra ait bilgileri ifade edecek şekilde kullanılmalıdır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade82743a7-d9c7-4259-9a71-5aebc92d41b8)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload743c1b2b-abec-4caf-bef8-117afef1cbb9)

</div>

:::

## İsimlendirmelerde Büyük Küçük Harf Kuralları

Özellik ve değişken gibi ögeler isimlendirilirken, kelimenin ilk harfleri küçük, diğer harfleri büyük olacak şekilde isimlendirme yapılır. Sınıf ve method isimlerinde ise ilk harf büyük kullanılır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8b38fe8-2730-4bac-984a-9c629badcfda)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload56f2f811-1289-40bf-8c3b-bd18c31fcb20)

</div>

:::

Aynı tanımın hem büyük harf içeren versiyonu hem küçük harf içeren versiyonu kullanılmamalıdır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04320100-3a0b-43c1-ba09-5f1c1f004828)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05856e9a-f5f5-4587-999b-940abd53c202)

</div>

:::

## Türkçe Karakter Kullanımı

Türkçe karakterler kod içerisinde farklı algılanıp hatalara sebep olabileceği için, kod içinde Türkçe karakterler kullanılmamalıdır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ce02d60-0f5c-482d-b4d8-6b6b6a8535ad)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload799901d4-92c8-46d1-8a64-a38fb07a2634)

</div>

:::
	
## “Return” Kullanımı
Fonksiyonlarda değer döndürürken değişken kullanıp tek bir yerden return edilebilir veya return edilecek değerin oluştuğu yerlerde birden fazla return deyimi kullanılabilir. Ne şekilde return edileceği yazılan fonksiyonun koduna bağlı olarak, karmaşık kod yapılarında değişken kullanımı ve tek bir yerden return tercih edilmelidir. Yazılan fonksiyon değeri switch-case yapısında return edilecekse, değer “case” içerisinden return edilmelidir.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04ba4ee2-e5e6-4032-ab1f-eb200f8c0e23)

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb564fd8e-69dd-4141-b686-4b476632c36f)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload847ca557-b092-47cc-89ac-fc80c0395abc)

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84aaf9cb-49d5-43e1-8ff5-3f9a36a26e3d)

</div>

:::
	
## “If-Else” Yapısı Kullanımı
En çok kullanılan kod blokları arasındadır. Genel olarak koşul satırı bitiminden sonraki satırda “{” işareti kullanılmalı ve şart içindeki kodlama bittikten sonra da “}” işareti ile blok kapatılmalıdır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd79c6c2a-5ce3-4a13-ab41-4fd2a7c8f201)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2460c387-0016-4244-ad17-ee44a793dde6)

</div>

:::
	
Karmaşık karşılaştırmalar gerektiren koşullar “if” bloğu içerisine yazılmamalı, her bir koşul bir değişkene atanarak, “if” bloğunda değişkenlerin karşılaştırılması yapılmalıdır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a974b77-d94d-4d5f-a7cf-5a4edb18896a)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8bd8db2-7b9c-493b-b6ca-a7966f5fab51)

</div>

:::
	
Veri tipi “bool” olan karşılaştırmalarda direkt olarak karşılaştırma işlemi yapılır. “==” veya “!=” kontrollerinin yeniden işleme sokulmasına gerek yoktur.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc63098b-3fbc-4913-9725-dc07af8f005c)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac75e29d-f795-4251-ae71-6c9f5aaafa55)

</div>

:::
	
Koşul yapılarında gereksiz yere koşulun tersinin de kontrol edilmesi, kod karmaşıklığını artıracağı ve gereksiz kod satırı oluşturacağı için yapılmamalıdır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8fb1b5b-8561-418d-8c43-06390f67b73c)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3993458-eeb5-4c3d-9ba7-6620abf6b037)

</div>

:::
	
İç içe if blokları kullanmak yerine else if yapısı tercih edilmelidir.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload301a7e58-cee6-441e-b2bb-37586b60d2ee)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd381420d-2fc6-4fdc-88f5-efd4e3cedc39)

</div>

:::
	
## “For – Foreach” Yapısı Kullanımı
Bu iki döngü tipinde, döngü içerisinde sadece tek satır kod olsa dahi blok parantezleri mutlaka kullanılır. Ayrıca döngü içerisinde zorunlu kalınmadıkça değişken tanımlanmamalıdır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cfaaece-f8c7-4d54-bba2-bf8e7f478f86)

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7913800-c685-4c66-9636-05b701ab2bb5)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d2ba8cb-5d57-4450-80bd-4b6c55ba9772)

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec9eddf3-76be-47d5-b9cb-0e756d634f1e)

</div>

:::
	
## “While – do/while” Yapısı Kullanımı
Döngü çıkışı, döngü çıkış deyimi ile kontrol edilir. Mecbur kalınmadıkça döngü içerisinde if kontrolü ile çıkış yapılması önerilmez.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload824266c7-aab7-458d-8bde-2df8262ec876)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9d616aa-92e7-4767-8ee0-bea583273cbb)

</div>

:::
	
## “Try – Catch” Yapısı Kullanımı
Bu yapıda kesinlikle boş bir catch bloğu tanımlanmamalıdır. Catch bloğu, akış kontrol etmek için kullanılmamalı veya değerlendirilemeyen istisnai durum yakalanmamalıdır. Catch bloğu içerisinde başka bir try-catch bloğu kullanılmaz. İstisnai durum yakalanması, en çok yakalanma olasılığı olandan en azına doğru sıralanmalıdır.

:::danger YANLIŞ KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f23b5c7-e8ee-437f-b5c2-569b4f6ccb82)

</div>

:::

:::tip DOĞRU KULLANIM

<div style={{textAlign: 'center'}}>

![Standartlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c9d4f9c-56e4-48e3-b958-874608d92fac)

</div>

:::