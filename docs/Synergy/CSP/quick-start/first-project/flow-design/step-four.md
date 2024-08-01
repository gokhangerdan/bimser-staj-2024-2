---
sidebar_label: Dördüncü Adım
sidebar_position: 4
custom_edit_url: ""
---

# Dördüncü Adım

Bu adımda akışın, yönetici onayından sonra, İnsan Kaynakları Departmanı’nda bulunan tüm kullanıcılara düşürülmesi gerekmektedir. Yönetici nesnesinin **“Onayla”** aksiyon okunu bir önceki adımda akışa yerleştirilen **Pozisyon Grubu** nesnesine bağlamıştık.

Akışa eklenen Pozisyon Grubu nesnesine, sistemdeki İnsan Kaynakları Departmanı’nın seçilmesi gerekiyor. Bunun için grup nesnesinin özelliklerindeki **“Grup İçeriği”** alanından grup nesnesinde hangi kişilerin bulunacağının seçimi yapılmalıdır. Grup içeriği kısmında,

- **Grup Tipi** alanında gruba hangi tipte kullanıcı atanacağının seçimi yapılır. Tek tek kullanıcı ya da pozisyon ataması değil departmandaki toplu kullanıcıların ataması yapılacağı için bu alanda, **“Pozisyon Grupları”** seçeneği seçilir.

- **İçerik Tipi** alanında ise, hangi veri ile grup içeriğinin doldurulacağının seçimi yapılmalıdır. Biz departman tanımı ile o departmandaki kişileri gruba eklemek istediğimiz için bu alandan **“Departmana Göre Kullanıcı Grubu”** seçeneğini seçiyoruz.

- Bu seçimler sonrasında ekranın altına, sistemde tanımlı tüm ünvanları ve departmanları listeleyen bir yapı gelecektir. Departman listesinden **“İnsan Kaynakları Departmanı”** seçilir ve Tamam butonuna basılır.

![Dördüncü Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a527074-fdfa-42e4-a25a-33460e02ab2e)

Grup nesnesindeki kişiler, akışı başlatanın doldurduğu formu görerek o kişinin ilgili tarihlerde izinde olacağının kaydını gireceklerdir. Bu yüzden grup nesnesinin Dokümanlar alanından, akışı başlatanın doldurduğu form dokümanı seçimi yapılır.

![Dördüncü Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e29ad9f-4d39-41b5-9de9-284fb5512488)

Grup nesnesinin akışta alacağı aksiyon, gruptaki kullanıcılardan 1 kişi işlem yaptıktan sonra **“Onayla”** butonuna basarak akışı sonraki adıma göndermektir. Akış ekranına eklenen bir pozisyon grubu nesnesinin olayları varsayılan olarak “Onayla” ve “Reddet” dir. Senaryomuza göre grup nesnesinin Reddet aksiyonu olmayacağı için, varsayılan olarak gelen Reddet olayını nesneden kaldırıyoruz.

![Dördüncü Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71fabab3-0f85-445e-9c05-ce29364bcac2)

Grup nesnesinin olayları ile ilgili yapılması gereken bir başka işlem daha vardır. Senaryoya göre akışın ilerlemesi için gruptan **1 kişinin** “Onayla” aksiyon butonuna basması yeterli olmalıdır. Örneğin; İnsan Kaynakları Departmanı’nda 5 kişi olduğunu düşünelim. Akış pozisyon grubuna düştüğünde, bu 5 kişiye birden aksiyon talebi gönderilecektir. Akışın ilerleyebilmesi için gruptaki 5 kişinin de varsayılan olarak “Onayla” butonuna basması gerekmektedir.

Bu durumun, gruptaki 1 kişinin onaylaması ile akış ilerlesin şeklinde değiştirilmesi için, bu şekilde çalışması istenen olay tanımında, Koşul kısmında **“Sayı“**, Koşul Değeri kısmında ise **“1”** seçilmesi gerekir.

![Dördüncü Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadefb0d7da-edc5-47f2-bb41-d0d7a5d4ce62)

IK departmanından bir kullanıcı “Onayla” aksiyon butonu ile akışı ilerlettiğinde, bir sonraki adım olarak akışı başlatana bilgilendirme maili gönderilecektir. Bu yüzden pozisyon grubu nesnesinden sonra akışa bir Bilgilendirme nesnesi yerleştirilir ve pozisyon grubunun “Onayla” aksiyon oku bu **Bilgilendirme** nesnesine bağlanır.

![Dördüncü Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf18e92e3-0afb-46cd-9c01-257adf8855cc)