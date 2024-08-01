# QDMS Girişinde Disk Doluluk Uyarısı(LOG_BACKUP)

### Örnek Hata

![](https://docsbimser.blob.core.windows.net/imagecontainer/LOG_BACKUP_hatası.jpg.png-f828f533-dfba-42ea-8c4f-18a92587bc4a.png)

Bu tür hatalarda uygulamanın veritabanlarının log dosyalarının şişmesinden kaynaklanmaktadır. Problemin o anda çözülmesi için shrink işlemi gerçekleştirilerek  sorun giderilebilir.

SHRINK;

	1. Server'a giriş yapılır..
	2. Uygulamanın Database'i seçilir. (örneğin: QDMS, QDMS_BSMS)
	3. Sağ click -> Tasks -> Shrink -> Database/Files seçeneğinden biri seçildikten sonra,
	4. OK denilir.



SHRINK: DB' nin veya DB içerisindeki bir dosyanın mevcut boyutunun küçültülmesi veya kısaltılması işlemine "shrinking" adı verilir.

### Problemin Tekrar yaşanmaması İçin;

- Bilgi işlem ekibinin, ilgili server sunucusundaki veritabanlarında transaction log alımı yapabilir veya  recovery modu Simple olarak güncelleyebilir. Bu yöntem uygulanılırsa alan problemi yaşanmayacaktır.
- Server sunucusundaki ilgili Databaselerin yer aldığı dizindeki Disk alanları kontrol edilir.  Alan yetersizliği mevcut ise diskin alan artırımına gidilmelidir.

### Recovery Model Önerisi

-Transaction logları şişiyor ise recovery model Full olarak ayarlıdır. Full modelde günlük backup ile birlikte Transaction backup’ında alması gerekir. Transaction backup alınmadığı için loglar şişmektedir. 

-Yedek alma prosedürünüze göre  sadece günlük yedek almayı tercih ederseniz recovery medel’i Full’den Simple’ye çekebilirsiniz. Bu durumda loglar şişmeyecektir. 

-İşlem örneği aşağıdaki gibidir, sarı taralı alan recovery modeli gösterir. Check box’ten seçim yapılıp ok butonu ile kaydedilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/recovery1.png-b0ed35e9-6639-4ef1-89a7-8571195d7b6f.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/recovery2.png-f75e70a8-8334-4dbf-b893-8a7b006f62ff.png)

