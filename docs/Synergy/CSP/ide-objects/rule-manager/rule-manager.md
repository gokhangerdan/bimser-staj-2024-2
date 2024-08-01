---
sidebar_label: Rule Manager
sidebar_position: 1
custom_edit_url: ""
---

# Kural Yöneticisi
Kural yöneticisi,  IDE'de yer alan bir özelliktir, **Görünüm > Kural Yöneticisi** seçeneği üzerinden erişilebilir. Bu araç, kullanıcıların form üzerinde yer alan nesnelerin görünüm özellikleri, sakladıkları veriler ve diğer özelliklerini kontrol ederek, nesnelerin davranışlarını belirlemelerini sağlar.

Kural yöneticisi, bir **tarayıcı üzerinde** çalışan yapıdır ve eklenen eylemler belirli bir koşula bağlı olabileceği gibi, koşul olmaksızın da zamanı geldiğinde çalışabilir. Arka planda çalışmak için, kendisi TypeScript kodlarını üreterek formun istemci tarafında yazılan kodlardan önce çalışır.

Kodlama bilgisi olmayan kullanıcılar, kural yöneticisi aracılığıyla kodlama işlemlerini rahatlıkla gerçekleştirebilirler. Kodlama bilgisi olan kullanıcılar ise kod karmaşıklığına boğulmadan kurallar yazabilirler. Bu sayede, bir form üzerine eklenmiş olan nesnelerin görünüm özellikleri ve sakladığı veriler gibi özellikleri kontrol ederek şekillendirmek mümkündür.

Kural yöneticisi, kullanıcıların işlerini kolaylaştırmak için tasarlanmış bir araçtır ve kodlama bilgisi olmayan kullanıcılar için özellikle kullanışlıdır. Ancak, kodlama bilgisi olan kullanıcılar da karmaşık kuralları yazarken kolaylıkla kullanabilirler.

# Kullanım Örnekleri 
## Akış Kullanıcısına Göre Nesne Gizleme



### Senaryo
1.  Formda, kullanıcıların ad ve soyad bilgilerini girerek kaydedebilecekleri bir alan bulunmaktadır. Bu alanın yanı sıra, kullanıcılar tarafından girilen bilgileri IK departmanına ekleyebilmek için bir buton mevcuttur.
    
2.  Bu buton, sadece akış başlatan kişinin bir üst yöneticisinde görünür olmalıdır. Bu şekilde, yalnızca doğru yetkileri olan kişilerin kaydedilen bilgileri IK departmanına aktarması sağlanmış olur.
## Akış Kullanıcısına Göre Nesne Gizleme Görsel Anlatım
 #### 1. Flow
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/FlowObject-fca68c5f-92a7-4eb8-86df-76faefb1a640.png)
 #### 2. Kural Yöneticisi
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/RManager-dca2052c-995d-4a8c-aa3f-6e2654135eac.png)
 #### 3. Form Görüntüsü
 ![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/Form-b5bce83e-7c22-4b75-be61-8e1a1e556d4d.png)
  #### 4. Akış Başlatan Form Görüntüsü
 ![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/FStarter-9b984157-5cdd-4b34-8301-8d7d5828547b.png)
  #### 5. Amir Onayı Form Görüntüsü
  ![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/FSManager-424c80de-54df-4c8e-8742-880326ed3d5c.png)

## Rate puanına göre başarılı mı başarısız mı yazdırmak
### Senaryo

 1.  Eğer Rate kutucuğuna girilen değer 3 ise "Sen iyisin"
2. 1 veya 2 ise "Kendini geliştirmen gerekiyor" 
3. 4 veya 5 puan ise "Harika bir başarı!"  
yazdıran bir kural yöneticisi yapısı kurmak.

### Akış Kullanıcısına Göre Nesne Gizleme Görsel Anlatım
#### Kural Yöneticisi Tanımlamaları
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/RM-Rate-124bdecb-41f2-46c2-a9af-6990df1f53f4.png)
Burada dikkat edilmesi gereken bir nokta txtSistemYorumu kısmının hem text hem de value alanlarında değer gösterebildiğidir. Bu özellik TextBox nesnesine özgüdür. Value ve Text alanları birbirleriyle bağımlıdır.
#### Proje Görüntüleri
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/RM-Rate-f1-7dc9e46e-3264-462f-ab70-d54e7ba80c25.png)
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/RM-Rate-f2-31cd6c53-5cb7-485b-aaf1-bbf65bda650e.png)
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/RM-Rate-f3-2bc6b3e7-95ee-4450-941a-1c4eb65aac7b.png)
## ComboBox'tan seçilen değere göre TextBox'ların görünüm özelliklerini değiştirme
### Senaryo

### Kural Yöneticisi Tanımlamaları
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/1-a4fdd0b0-52d8-4090-ab50-70caa900f69e.png)
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/2-7f514f1b-34f8-4bea-956e-ddeb4c88c434.png)
### Form Görünümleri
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/3-4ace14b6-3db2-4b8e-9af6-352d9365a601.png)
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/5-6775b8bd-4ad0-454a-af82-4278df7fbc0c.png)
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/6-1f6bad13-a904-4594-8795-41dd3e116d74.png)
