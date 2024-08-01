# Synergy Sistemi Mesai Veri Tabanı Sorgusu

Bu dokümantasyon, Synergy sisteminde tutulan mesai bilgilerini veri tabanından almak için kullanılacak SQL sorgusunun detaylarını açıklamaktadır.

## Mesai Sorgusu

Web ara yüzünde İnsan Kaynakları altında yer alan mesai bilgilerini almak için aşağıdaki SQL sorgusunu kullanabiliriz.

### Sorgu Detayı

```sql
SELECT
    O.CODE,
    O.FACTOR,
    OML.NAME 
FROM OVERTIMES AS O
INNER JOIN OVERTIMESML AS OML ON OML.OVERTIMEID = O.ID AND OML.CULTURE = 'tr-TR'
WHERE O.DELETEDAT IS NULL
```

Bu sorgu, OVERTIMES tablosundaki kayıtları OVERTIMESML tablosu ile birleştirir ve Türkçe dilindeki mesai isimlerini getirir.

### INNER JOIN Açıklaması

`INNER JOIN` kullanımı, her bir mesai kaydını onun çok dilli (Multi-Language) tablosu olan OVERTIMESML ile ilişkilendirir. Bu ilişkilendirme `OVERTIMEID` ve `ID` alanları üzerinden yapılır. Ayrıca, `OML.CULTURE = 'tr-TR'` koşulu ile sadece Türkçe olan mesai adlarını getiririz.

### WHERE Koşulu Açıklaması

`WHERE O.DELETEDAT IS NULL` koşulu, silinmiş olan mesai kayıtlarını sorgu sonucundan çıkarır. Bu koşul, veritabanından sadece geçerli (silinmemiş) mesai bilgilerini almak için kullanılır.

Bu sorgu, Synergy sisteminde İnsan Kaynakları modülü altında çalışırken mesai bilgilerine ulaşmak için kullanılabilir ve kolayca entegre edilebilir.

