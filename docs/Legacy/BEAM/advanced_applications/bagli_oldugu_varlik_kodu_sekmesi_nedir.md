# BAĞLI OLDUĞU VARLIK KODU SEKMESİ NEDİR?

![](https://docsbimser.blob.core.windows.net/imagecontainer/Bağlı%20Olduğu%20Varlık%20Kodu%20Sekmesi%20Nedir%201-a938f4c0-9956-4e10-b7dd-1d8c792599e1.png)

Yukarıdaki varlık ağacında görüldüğü gibi buzdolabı varlığının altında buzdolabı motoru bulunmaktadır. Buzdolabı motorunun altında alt varlık olarak motor fanı bulunmaktadır. Buzdolabı motor fanının altında motor fan pervanesi bulunmaktadır. Biz varlığı bu şekilde alt kırılımlarına ayırabiliriz. Alt kırılım gerçekleştirebilmek için excelde tanımlama şu şekilde yapılmaktadır: Varlığın bağlı olduğu bir başka varlığın kodunu “bağlı olduğu varlık kodu” sekmesine yazarak gerçekleştiririz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Bağlı%20Olduğu%20Varlık%20Kodu%20Sekmesi%20Nedir%202-09ff9151-6416-438c-83f6-74117e49e433.png)

### Peki biz hangi alt kırılıma kadar bunu gerçekleştirmeliyiz? En son kırılımımız ne olmalı?

Kendine özel bakımı olan ekipmanları alt varlık olarak tanımlama yapmalıyız. Örneğin: Buzdolabı “BZDLB.1”  kodu ile sistemimde varlık olarak tanımlı. “BZDLB.1” kodlu 1.buzdolabımın motorunun, fanının, pervanesinin herbirinin kendine ait özel bakımı bulunmaktadır. Bu ekipmanları sisteme alt varlık olarak tanıtıyorum (Buzdolabının alt varlığı olarak). 
Eğer kendine özel bakımı yok ise varlık olarak tanımlamayız, bu tanımlamaları genel tanımlamalar şablonunda bakım arıza kodu sekmesinde “bakım arıza kodu” olarak tanımlarız.  Özet olarak: kendine özel bir bakımı olmayacaksa genel tanımlamalar şablonunda “bakım arıza kodu” sekmesinde tanımlama yaparız. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/Bağlı%20Olduğu%20Varlık%20Kodu%20Sekmesi%20Nedir%203-4b3d267c-654d-4be7-b9fb-2915356ad158.png)

Varlık olarak “BZDLB.1” kodlu buzdolabını seçip, arıza kodu olarak “buzdolabı kompresör arızası” nı seçtiğimde ben bu varlığımda kompresörün arızalı olduğunu anlarım. Raporlamalarımda ise buzdolabının kodunu seçip, bakım arıza kodunda “ısıtıcı arızası” seçtiğimde bu varlıkta gerçekleşen ısıtıcı arızasının maliyetini çekebilirim. Veya sadece “buzdolabı ısıtıcı arızası”nı seçerek bütün buzdolaplarında bu arıza kaç kere tekrarlanmış, genel olarak bütün buzdolaplarında bu arıza kodunun maliyeti ne kadar çekebilirim.

