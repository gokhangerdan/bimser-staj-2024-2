# Deploy Management İle Aktarım Yapılırken Hata

Hata mesajı:

System.Exception: 

Error while compiling the form FORM ---> System.Collections.Generic.KeyNotFoundException: 


Verilen anahtar sözlükte yoktu.
   

konum: System.Collections.Generic.Dictionary`2.get_Item(TKey key)
   konum: n.z()
   konum: d.j()
   konum: n.j()
   konum: bk.v()
   konum: bk.h()
   konum: aj.b(eBADBProvider A_0)
   --- İç özel durum yığını izlemesinin sonu ---
   konum: aj.b(eBADBProvider A_0)
   konum: c6.a(String[] A_0)

Çözüm:

Bu hata bir workflow projesi SQL olan bir ortamdan alınıp Deploy Management ile Oracle olan bir ortama taşınırken alınmakta. Aktarım sırasında form nesnelerinin isimleri tamamen büyük harflerden yazılacak şekilde değiştirildiğinden Detay Tablo gibi nesnelere eski isimleriyle ekli olduklarından bu hata alınmakta. Detay Tablo'lardan çıkartılıp yeni halleri tekrar eklendiğinde hata düzelecektir.

