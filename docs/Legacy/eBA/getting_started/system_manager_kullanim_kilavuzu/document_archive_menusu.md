---
title: 2.2 Document Archive Menüsü Ve 2.3 Data View Menüsü 
sidebar_position: 11
---

# 2.2 Document Archive Menüsü Ve 2.3 Data View Menüsü 

### 2.2 Document Archive Menüsü 

Süreçlere ait sadece form ekranı arşivden görüntülenmek isteniyorsa Document Archive kullanılır. Süreçlere ait rapor oluşturup formu görüntüleme, üzerinde değişiklik ve arama yapmak için doküman arşiv menüsü kullanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce816e02-7f4f-43df-955c-bf952ef64b4a)

Döküman arşiv oluşturma proses arşiv ile aynı adımlara sahip olup farklı olarak ID alanı bir global doküman numarası yani form ID numarası olmalıdır. Global doküman numarası DOCUMENTS tablosundaki ID alanı veya başka bir veritabanı tablosundaki Form ID alanından getirilebilir. Şekil 40’da, 2 numaralı alanda arşiv için oluşturulan sorguda kolon olarak getirilen Form ID değeri, ID seçilir. 

Document View alanı ise dokümanın hangi view ile görüntüleneceğidir. Metin bir alandır. Üç farklı tipte değer almaktadır; 

  	  Static : Sabit bir view ile view set edilebilir. 
Not Assigned : View değeri menü yöneticisinden girilir. 
             Bound : View değeri sorgudan dönen metin tipindeki bir alandan alınır. Dönen veriye göre dokümanın gösterimi değiştirilebilir. 


### 2.3 Data View Menüsü 

Süreçlere ait raporu görüntülemek için kullanılır. Döküman arşiv oluşturma proses arşiv ile aynı adımlara sahip olup farklı olarak formu görütüleme ve form üzerinde değişiklik yapılamaz.