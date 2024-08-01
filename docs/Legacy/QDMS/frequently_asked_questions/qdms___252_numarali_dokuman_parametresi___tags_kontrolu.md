# QDMS - 252 Numaralı Doküman Parametresi - Tags Kontrolü

Bu parametre evet olduğunda sistem, dosyada aşağıdaki alandaki 3 numaralı alana QDMSTag yazılmalı(sabit)
4 numaralı value alanına DokümanKodu_Revno_DilKodu şeklinde tanımlama yapılmalıdır. Bu özelliğimiz, şablon kontrolüne göre dokümanı yüklemektedir.

Kısacası, hazırlama şablonunu nasıl yüklediyse kullanıcılar, o klasöre doküman hazırlarken ilgili şablonu indirip yüklemelerini gerektiren yapı kurgulamıştır. 
Aşağıdaki resim, örnektir. 

Hiçbir ekleme yapmasak bile QDMS tarafında bir dokümanı revize ederken, dosya görüntüle butonuna tıklandığında indirilen dosyanın yüklenmesi zorunludur.
Farklı bir şablon üzerinden(dosya adları aynı olsa bile) sistem yükleme yapmayacaktır.



![](https://docsbimser.blob.core.windows.net/imagecontainer/TagsKontrolü.png-77771b20-9ab3-4b4c-89fc-72452f9931f6.png)

