---
title: "Masraf Detay Bilgileri Bölümü"
sidebar_position: 3
---

# Masraf Detay Bilgileri Bölümü
Masraf Detay Bilgileri bölümü için forma Label nesnesi ile yeni bir bölüm başlığı yazılır.
![masraf detayları label](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20detay%20bilgileri%20label-3ea7ccd6-e4b0-4ae8-92e7-d168dd26763c.png)

Masraf Detay Tablosu için forma **DataGrid** nesnesi eklenir.
![masraf detay DataGrid](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20detaylar%C4%B1-5031844a-e8f2-4520-b008-532d917865d5.png)

Masraflara ilişkin detayların girileceği tablo, bir başka formdan doldurulacak alanları içinde barındıracak şekilde tasarlanacaktır.

Bu işlem için ayrı bir form olarak [**Masraf Detay Formu**](../expense-detail-form-design.md)’nun tasarlanması gerekmektedir.

Masraf Detay Formu tasarlandıktan sonra Masraf Detayları Tablosu ile ilişkilendirilebilmesi için öncelikle Masraf Detay Tablosunun özelliklerinden **DataSource** özelliği **"İlişkili”** olarak seçilir.
![detay tablo-form ilişkisi](https://docsbimser.blob.core.windows.net/imagecontainer/detay%20tablo%20ve%20form%20ili%C5%9Fkisi-af785590-0942-4661-b2d4-2ee14c0b68d0.png)

Masraf Detay Formundaki alanların Masraf Detayları Tablosuna eklenebilmesi için nesnenin **Columns** özelliğindeki üç noktalı alana tıklanarak kolonların düzenlenebileceği pencere açılır. **İlişkili Kolonları Üret** butonuna tıklanarak DataGrid’de bulunması istenen kolonlar seçilir.
Varsayılan olarak gelen **“RELATIONDOCUMENTID”** kolonunun görünürlüğünün kapatılması için **visible** özelliği pasif yapılabilir.
Eklenen satırlardaki masraf detay formlarının içeriğinin düzenlenebilmesi için **“OPENRELATIONDOCUMENT”** kolonunun **Action Button** özelliklerinden **Action Type Properties** sekmesindeki **Editable** özelliğinin aktif edilmesi gerekir.
Eklenen masraf tutarlarının toplam değerinin de kolonun altında gösterebilmesi için Masraf Tutarı alanına karşılık gelen “NumberBox2” kolonunun **Summary Types** özelliğinden sum seçeneği seçilir.
![iliskili kolonlari uret](https://docsbimser.blob.core.windows.net/imagecontainer/iliskili%20kolonlari%20uret-9851ade2-aed9-4c66-bfcb-bde75d3cde58.png)

**Toplam Masraf Tutarı** alanı Masraf Bilgileri tablosuna girilen tüm satırlardaki toplam masraf tutarını içerecek alandır. Bu alan için forma **NumberBox** nesnesi eklenir. 
Caption değeri Toplam Masraf Tutarı olarak girildikten sonra kullanıcının bu alana giriş yapabilmesini engellemek için **Client Enabled** özelliği pasif duruma getirilir. 
Değerin virgülden sonra 2 basamak devam edebilmesi için **Precision** değeri **"2"** olarak verilir.
![toplam masraf tutari](https://docsbimser.blob.core.windows.net/imagecontainer/toplam%20masraf%20tutari-de5dcbdf-9e32-4595-a25c-54b1a9e885e4.png)

Masraf Detayları tablosundaki tüm satırlardaki masraf tutarı değerlerinin toplamını Toplam Masraf Tutarı alanına atayabilmek için DataGrid1 nesnesinin Client olaylarından **OnSummaryChanged** olayı eklenir.
![onSummaryChanged](https://docsbimser.blob.core.windows.net/imagecontainer/onSummaryChanged-99b2a93c-df84-4b7f-b411-d1c374c7dec0.png)
Metodun parametresi olan args’ın value değeri, Toplam Masraf Tutarı alanına karşılık gelen “NumberBox1” nesnesinin value değerine atanır.


Toplam Tutar değerinin hangi para biriminde olacağının seçimi için masraf tutarı alanının sağına bir **ComboBox** nesnesi eklenir. Nesne başlığının görünmemesi için Caption alanının Visible özelliği kapatılır. Datasource alanından **Statik** değerler **"TL"** ve **"EUR"** olarak eklenebilir.
![para birimi](https://docsbimser.blob.core.windows.net/imagecontainer/para%20birimi-f778b89c-c1a4-4109-87ed-8cf63b16a7fc.png)


Masraflara ilişkin ek açıklamaların girilebilmesi için **TextArea** nesnesi form üzerine eklenir. Nesnenin **MaxLength** özelliği için **"250"** değeri verilebilir ve kalan karakter sayısını gösteren **Show Character Counter** özelliği aktif edilir.
![aciklama masraf beyan](https://docsbimser.blob.core.windows.net/imagecontainer/MasrafBeyan%20Aciklama-93893647-7e64-499e-b014-1b35111a244e.png)

