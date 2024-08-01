---
title: "Dördüncü Adım"
sidebar_position: 4
---

# Dördüncü Adım
Toplam Masraf Tutarının 2000 değerinden küçük olduğu durumda akış, İK Grubuna, büyük olduğu durumda ise Departman Yöneticisine yönlendirilecektir. İk Grubu için Akış üzerine bir **Pozisyon Grubu** nesnesi eklenir. **Group Content** alanının yanındaki üç noktaya tıklanır ve açılan pencereden **İçerikler>Pozisyon Grupları>Kullanıcı Grupları** seçilerek sistemde mevcut gruplardan İnsan Kaynakları Grubu eklenir. Daha sonra Oluştur'a tıklanır ve eklenen grup nesneye kaydedilir. Bu sayede onay bu gruba geldiğinde form, gruptaki tüm kullanıcıların onayına düşer.

Nesnenin Events özelliklerinden Reddet eventi kaldırılır. Gruptaki kişilerden yalnızca 1 kişinin onayı ile akışın devam edebilmesi için Onayla eventindeki **Condition** özelliğinden **Sayı** değeri seçilir ve **Condition Value** değerine **“1“** girilir.

Toplam Tutar değerinin 2000’den büyük olduğu durumda akışın Departman Yöneticisine yönlendirilebilmesi için öncelikle Akış üzerine bir **Departman** nesnesi eklenir ve nesnenin Properties özelliklerinden **Type** değeri **“Akış Başlatan Departman”** olarak seçilir. Karşılaştırma nesnesinin else kolundan(2000’den büyük olduğu durum) ilerlediği yöne bir Pozisyon nesnesi eklenir ve Doküman, nesne üzerine kaydedilir.

Karşılaştırma ve Pozisyon nesnesinin arasına bir Atama nesnesi eklenir. Atama nesnesinin Properties özelliklerinden **Target Object** alanından Departman Yöneticisi(Position3) seçilir. **Source Type** alanından Departman Yöneticisi seçilir ve altta açılan **Select Item** özelliğinden de Akış Başlatan Departman(Department1) seçilir.

Departman Yöneticisi’nin Red kararı sonucu akışı başlatan kullanıcıya bilgilendirme mesajı gönderilir ve Ardından Akış sonlanır. Onay kararı sonucunda ise İK birimine yönlendirilir.
![karsilastirma sonrasi](https://docsbimser.blob.core.windows.net/imagecontainer/karsilastirma%20sonrasi%20yonlendir-8a9f0628-232c-4f62-a7f6-ec2619dd12fc.png)
