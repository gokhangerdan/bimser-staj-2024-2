# Violation of Primary Key

![](https://docsbimser.blob.core.windows.net/imagecontainer/eba-pk_files%20(1)-0a688562-ae8c-4814-8a06-ab7b0225cfce.png)


FSIDENTITIES tablosunda LIBRARY ID'si 1-2-3 olan, ID'leri 100 binlerde olan üç adet satır olmasına rağmen en altta LIBRARYID'si 2 olan bir FILEDATA satırı mevcuttu. Onun ID'si ile eba formunda alınan hatanın ID'lerinin aynı olduğu görülünce FSIDENTITIES tablosunda bu satır silindikten sonra eba servisleri restart edilip test gerçekleştirildi. Bu testte sorunun çözüldüğü görüldü.