# Risk Tabanlı Modüllerde Sorgu ve Sorgu Ağaç Tipli Alanların Kullanımı

Risk tabanlı modüller yapısı gereği birçok farklı tipte alanın tanımlanabildiği ve kullanılabildiği modüllerdir. Bu modüllere tüm risk değerlendirme modülleri, Değişiklik Yönetimi, Olay Bildirimi gibi modüller örnektir. 

Bu modüllerde ve diğer modüllerin Alan Tanımlama&Fonksiyon Dizayner kullanılan taraflarında kullanılabilen alanlar içerisinde Sorgu ve Sorgu Ağaç tipli alanlar kullanımları itibariyle diğer alanlardan ayrışmaktadır. Sorgu tipli alanlar veri tabanının içerisinde yer alan herhangi bir veriyi, kullanılan sorgu ile ilgili risk tabanlı modülde kullanıma sunmaktadır. 

Örneğin, alan tanımlama ekranında ülke seçimi yapabilecek bir alan yoktur. Ancak sorgu tipli alan kullanılarak BSAT-Tanımlar-Ülke Tanımlama ekranındaki değerleri ilgili modül içerisinde seçimli hale getirebilmek mümkündür. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Ulke-f4aa35a1-c35e-48e6-b3ee-3855a312674c.png)

Çok sık karşılaşılan diğer bir örnek ise iş yeri tanımlamadır. BSAT-Tanımlar- İş yeri Tanımlama ekranında yer alan iş yerleri ancak sorgu veya sorgu ağaç tipli alanlar kullanılarak risk değerlendirme ya da diğer risk tabanlı modüllerde kullanılabilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Isyeri-49a84021-ef72-433c-88bc-eebbd3f41b2e.png)

Diğer bir örnek Ensemble tarafından verilebilir. Süreçlerle risk tabanlı modüllerin ilişkilendirilmesi gerektiğinde Süreçlerin parametrelerden aktif hale getirilmesi gerekir. Ancak bu parametrenin kullanılmayacağı ve süreçlerle ilişki kurmadan sadece raporda gözükecek şekilde süreçlerin risk formunda görülmesi talep edildiği bazı durumlarda Ensemble tarafındaki süreç listesi yine sorgu tipli alanlar ile QDMS tarafına getirilebilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Surec-0c7ba9fc-fd1d-459f-9774-f97095bf0171.png)

Sorgu ve Sorgu Ağaç (Kırılımlı yapı kullanılmak istendiğinde kullanılır) tipli alanların kullanımı için destek ekibinden yardım alınması gereklidir. BSS üzerinden ihtiyaç duyulan veri tabanı değerinin hangi sorgu ile modülde kullanılabileceğinin sorulması üzerine destek ekibi gerekli sorguyu ekran görüntüsü ile iletmektedir.

