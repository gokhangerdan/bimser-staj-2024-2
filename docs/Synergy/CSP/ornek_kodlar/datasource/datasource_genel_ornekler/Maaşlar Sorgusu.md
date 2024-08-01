## Synergy Ortamında Kullanıcı Maaş Bilgileri Sorgusu

Bu dokümantasyon, Synergy ortamında kullanıcıların maaş bilgilerine nasıl erişileceğini açıklamaktadır. Aşağıda, maaş bilgilerini çekmek için kullanılan SQL sorgusu ve detayları verilmiştir.

### SQL Sorgusu

Belirli kullanıcıların maaş bilgilerini çekmek için aşağıdaki SQL sorgusu kullanılır. Bu sorgu, silinmemiş kayıtları (yani hala geçerli olan maaş bilgilerini) getirir.

#### Sorgu Açıklaması:

- **`SALARIES`** tablosu: Kullanıcıların maaş bilgilerinin tutulduğu tablo.
- Sorgu, silinmiş kayıtları hariç tutmak için `DELETEDAT IS NULL` koşulunu kullanır.
- Sadece aktif maaş bilgileri getirilir.

#### Kullanılan Alanlar:

- `USERID`: Kullanıcının kimlik numarası.
- `STARTDATE`: Maaşın başladığı tarih.
- `ENDDATE`: Maaşın sona erdiği tarih.
- `FEE`: Maaş miktarı.
- `CURRENCY`: Maaşın para birimi.

#### SQL Sorgusu:

```sql
SELECT 
    USERID,
    STARTDATE,
    ENDDATE,
    FEE,
    CURRENCY
FROM SALARIES
WHERE DELETEDAT IS NULL
