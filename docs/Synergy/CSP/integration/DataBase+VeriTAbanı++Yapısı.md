# DATABASE (VERİTABANI) YAPISI
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/dbDiagram-6c6593d5-5def-4c23-981f-0a066867a939.png)

E_"ProjeAdi"_"FormAdi" adlı ana tabloya bağımlı olan beş farklı tablo bulunmaktadır. 
Bunlar:
E_"ProjeAdi"_"FormAdi"ML tablosu: Bu tablo, E_"ProjeAdi"_"FormAdi" tablosunun ID bilgisini kullanarak bağımlıdır.
E_"ProjeAdi"_"FormAdi"SL tablosu: Bu tablo, E_"ProjeAdi"_"FormAdi" tablosunun ID bilgisini kullanarak bağımlıdır.
E_"ProjeAdi"_"FormAdi"SLML tablosu: Bu tablo, E_"ProjeAdi"_"FormAdi"SL tablosunun ID bilgisini kullanarak bağımlıdır.
E_"ProjeAdi"_"FormAdi"RD tablosu: Bu tablo, E_"ProjeAdi"_"FormAdi" tablosunun ID bilgisini kullanarak bağımlıdır.

E_"ProjeAdi"_"FormAdi"RD tablosuna bağımlı olan iki farklı tablo vardır: E_"ProjeAdi"_"FormAdi"RDML ve E_"ProjeAdi"_"FormAdi"RDC. Bu iki tablo, E_"ProjeAdi"_"FormAdi"RD tablosunun ID değerine göre bağımlıdır.

E_"ProjeAdi"_"FormAdi"RDC tablosuna bağımlı olan tek bir tablo vardır: E_"ProjeAdi"_"FormAdi"RDCML. Bu tablo, E_"ProjeAdi"_"FormAdi"RDC tablosunun ID'sine göre bağımlıdır.

