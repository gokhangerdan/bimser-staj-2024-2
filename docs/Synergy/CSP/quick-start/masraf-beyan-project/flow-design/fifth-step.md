---
title: "Beşinci Adım"
sidebar_position: 5
---

# Beşinci Adım
İnsan Kaynakları Grubunun Onayından sonra Akış, Muhasebe Departmanına yönlendirilecektir. Akışa eklenen Pozisyon Grubu nesnesinin özelliklerinde **Group Content** alanının yanındaki üç noktaya tıklanır ve açılan pencereden **İçerikler>Pozisyon Grupları>Departmana Göre Kullanıcı Grupları** seçilerek sistemde mevcut departmanlardan Muhasebe Departmanı(Financial and Administrative Affairs) oluşturulur ve kaydedilir.

Akışın devam edebilmesi için Muhasebe Departmanından da bir kişinin onayı yeterli olacağı için nesnenin Events özelliklerinden Onayla eventi için **Condition** olarak **“Sayı”** seçilir ve **Condition value** değeri olarak **“1”** seçilir.
![muhasebe departmani](https://docsbimser.blob.core.windows.net/imagecontainer/muhasebedepartmani-7e5c895b-7ecb-4cda-9478-bd4d55b5cc2b.png)


Sürecin tamamlandığına dair bilgilendirmenin yapılabilmesi için Bilgilendirme nesnesi akışa eklenir. Nesne özelliklerindeki Group Content alanında Akışı başlatan seçilir. Kullanıcıya gönderilecek mesaj için ise Message alanından “Masraf Beyan talebiniz onaylanmıştır.” şeklinde bir mesaj içeriği yazılabilir.

Bilgilendirme nesnesinden sonra Akış, Akış Bitişine yönlendirilir ve böylece süreç tamamlanmış olur.
![akis bitisi bilgilendirme](https://docsbimser.blob.core.windows.net/imagecontainer/Akis%20bitisi%20bilgilendirme-d8b468d0-6056-445d-8211-cce43d9a1052.png)
