## Synergy Ortamında Vardiyalar

Synergy ortamında, vardiyalar farklı iş akışlarını ve zaman dilimlerini yönetmek için kullanılır. Bu dokümantasyon, Synergy'de yer alan vardiyaların nasıl sorgulanabileceğini açıklamaktadır.

### SQL Sorgusu

Aşağıdaki SQL sorgusu, Synergy veritabanında tanımlı olan vardiyaları çekmek için kullanılır. Bu sorgu, belirli bir kültür koduna (`tr-TR`) göre vardiya bilgilerini almak üzere tasarlanmıştır.

#### Sorgu Açıklaması:

- **`SHIFTS`** tablosu: Vardiya bilgilerinin tutulduğu ana tablo.
- **`SHIFTSML`** tablosu: Vardiya bilgilerinin çok dilli destek için tutulduğu tablo.
- `INNER JOIN` kullanılarak `SHIFTS` ve `SHIFTSML` tabloları ilişkilendirilir.
- Filtreleme, `SML.CULTURE` alanı üzerinden yapılarak sadece Türkçe dil ayarına sahip vardiyalar getirilir.

#### Kullanılan Alanlar:

- `S.CODE`: Vardiyanın kodu.
- `SML.NAME`: Vardiyanın adı.
- `S.STARTTIME`: Vardiyanın başlangıç saati.
- `S.ENDTIME`: Vardiyanın bitiş saati.
- `S.TOTALMINUTE`: Vardiyanın toplam süresi, dakika cinsinden.
- `S.BREAKMINUTE`: Vardiyanın ara verme süresi, dakika cinsinden.
- `S.TIMEZONE`: Vardiyanın geçerli olduğu zaman dilimi.

#### SQL Sorgusu:

```sql
SELECT 
    S.CODE,
    SML.NAME,
    S.STARTTIME,
    S.ENDTIME,
    S.TOTALMINUTE,
    S.BREAKMINUTE,
    S.TIMEZONE
FROM SHIFTS S
INNER JOIN SHIFTSML SML ON SML.SHIFTID = S.ID
WHERE SML.CULTURE = 'tr-TR'
