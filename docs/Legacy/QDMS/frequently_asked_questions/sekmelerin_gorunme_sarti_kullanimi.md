# Görünme Şartı Nasıl Eklenir?

Döf modülünde 219, 220, 221, 222, 223,  224 nolu parametreler içerisinde  sekmelerin görünme şartları kullanılabilmektedir. Bu parametrelerde yer alan şartlara bağlı olarak ilgili sekmeler aktif  ya da pasif olarak bulunabilir.  Örnek olarak işlem kaynağına bağlı bir sekmenin aktif olması isteniyor ise  [ALAN_ADI]=KOD şeklinde kullanılabilir. (Örn: [KAYNAK]=01) Bu alanda çoklu seçime bağlı şart kullanılmak isteniyorsa [ALAN_KODU]=01"+[ALAN_KODU]=02" şeklinde kullanılabilir. (Örn: [KAYNAK]=01"+[KAYNAK]=02") 

