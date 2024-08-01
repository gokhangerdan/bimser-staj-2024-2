# Archive Manager Remote Operation Özelliği

Archive Manager ile hazırlanan raporların performanslı hale getirilebilmesi için Remote Operation özelliği kullanılır.  Yüksek kayıt sayısına sahip raporlarda verilerin tamamını ilk aşamada yüklemek yerine sayfa scroll kaydırıldıkça veriler yüklenecektir.

Özellik aktif edildikten sonra raporlama ekranına ait sayfa sayısı ve kayıt sayısı bilgileri gösterilmemekte. 

## Veritabanı Sorgusuna Eklenecek Parametreler

Archive ait sorguda Remote Operation özelliğine ait parametrelerin eklenmesi gerekmekte. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBA_DP_1-29b8b4de-51f1-4e91-ba93-441f503b952e.png)

PWHERE – PSORT – PSKIP – PTAKE parametreleri eklenerek ekran görüntüsündeki gibi default değerlerle doldurulmalıdır ve compile edilmelidir.
```
Örnek Sorgu : 
SELECT *
    FROM [EBA].[dbo].[FLOWREQUESTS]  WHERE <?=PWHERE>
ORDER BY <?=PSORT>
OFFSET     <?=PSKIP>  ROWS       -- skip 10 rows
FETCH NEXT <?=PTAKE> ROWS ONLY -- take 10 rows
```
## Archive Manager Özelliğin Aktif Edilmesi

SystemManager > Process Archive kısmında arşiv tanımlamaları yapılmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBA_DB_2-5ef55c55-172f-4ce7-9f33-5e86059f344e.png)

•	Bu aşamada Remote Operations tabında enabled olarak ayarlayarak sorgu üzerinde belirlenen parametrelere karşılık gelen alanlar ekran görüntüsündeki gibi seçilmelidir.

•      SortColumns kısmında isteğe bağlı birden fazla seçim yapılabilir.

•	Tüm alanların doldurulması gerekmektedir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/eBA_DB_3-6457c683-5022-47de-bcc5-8109923b73ac.png)