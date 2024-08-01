---
title: "Üçüncü Adım"
sidebar_position: 3
---

# Üçüncü Adım
Mevcut senaryoda Masraf Beyan Formundaki Toplam Masraf Tutarı alanındaki değere göre akışın farklı kollardan ilerlemesi gerektiği için Masraf Beyan Formundaki toplam masraf tutarı alanının değerini tutan bir **Değişken** nesnesi akış üzerine eklenir.

Toplam masraf tutarı değeri ondalıklı bir değer olduğu için değişken nesnesinin özelliklerinden **Type** alanı **Ondalık Sayı** olarak seçilir. **Target Document** alanından Masraf Beyan Formuna karşılık gelen Document1 nesnesi seçilir. **Source Object** özelliğinde ise Toplam Masraf Tutarı alanına karşılık gelen NumberBox1 nesnesi seçilir.

Daha Sonra Akış üzerine bir **Karşılaştırma** nesnesi eklenir. Nesne özelliklerinden **Source Object** alanından Toplam Masraf Tutarı değerini tutan Değişken nesnesi(Variable1) değeri seçilir. **Results** özelliğindeki üç noktaya tıklanır ve açılan pencereden Ekle denilir. **Karşılaştırma Tipi** olarak “Daha küçük veya eşit”, Değer Türü olarak “Constant” seçilir ve **Değer** olarak 2000 değeri verilir.
![karsilastirma](https://docsbimser.blob.core.windows.net/imagecontainer/karsilastirma-de975159-9617-4983-8aac-cd6724d2f1ed.png)
