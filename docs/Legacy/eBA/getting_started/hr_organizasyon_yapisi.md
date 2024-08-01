# Organizasyon Bilgileri Transfer Yapıları

OSUSERS

•	Sistemdeki kullanıcıların tutulduğu tablodur.


![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel1-73c856cc-f29b-4688-9e5a-befa8cffce74.png)

OSPROFESSIONS

•	Ünvanların tutulduğu tablodur.


![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel2-87fa8586-d5a1-4030-8c79-3c46c8fcbc53.png)

OSDEPARTMENTS

•	Departmanların tutulduğu tablodur


![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel3-e0754ef7-b775-4bbc-b8fa-f86426daf3cf.png)

OSPOSITIONS

•	Pozisyonların tutulduğu tablodur.


![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel4-60af7ac9-5abf-411c-a5dc-6d2f863e3aad.png)

OSMANAGERKEYS

•	Üst kullanıcı (amir) anahtarlarının tutulduğu tablodur. Eba ile “default”  anahtarı birlikte gelir, bu anahtar default üst kullanıcıları tanımlamak içindir. Genelde bu idari olarak üst kullanıcıları tayin etmek için yeterlidir, ama eğer idari yapının dışında mesela teknik olarak üst kullanıcı bulmak istersek burada ikinci bir “teknik” manager key’ine ihtiyacımız olur. Bu durumda bir kullanıcının idari olarak üst kullanıcısı başka teknik olarak üst kullanıcısı başka tanımlanabilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel5-da6ca5f8-2cb3-4d30-8e2b-6f22024a4e5c.png)

OSMANAGERS

•	Üst kullanıcıların (amirler) tutulduğu tablodur.  Burada dikkat edilmesi gereken bir kullanıcının farklı manager key’lerle farklı üst kullanıcıları tanımlanabilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel6-bf4a578e-5979-4b24-9131-7e5fe8f76bc8.png)

OSGROUPS

•	Kullanıcı gruplarının tutulduğu tablodur.


![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel7-1cee7989-6630-49a1-a62e-fa6de4d12fad.png)

OSGROUPCONTENT

•	Grupların içerisindeki kullanıcıların tutulduğu tablodur.


![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel8-04a6aba6-6c31-4a26-ac6d-4ddbfe407a00.png)

OSPROPERTYTYPES

•	Özelliklerin tanımlandığı tablodur. Bu özellikler genel olarak eba ile birlikte gelmeyen ama müşterinin sonradan ihtiyacı olduğu her bir kullanıcıya, pozisyona, ünvana veya departmana bağlamak istediği verilerdir. Örneğin kullanıcıların kullanıdığı bilgisayarların modellerini  veritabanında saklamak istediğimizi düşünürsek,  yapmamız gereken bir tane bu tabloda string tipinde bir bilgisayar modeli özelliği tanımlamak ve bunu kullanıcılara bağlamak.


![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel9-951b40d8-467e-4589-b122-609497d5af2f.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel10-3fd94939-a5ea-4e0a-bd87-e46369af49ec.png)

OSPROPERTIES

•	OSPROPERTYTYPES tablosunda tanımlanmış olan özellikleri kullanıcılara, ünvanlara, departmanlara, pozisyonlara veya pozisyon gruplarına bağlamak için bu tablo kullanılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel10-e1a0d101-ae0f-46ab-ae65-ef5a10f4788b.png)

OSPROPERTYVALUES

•	OSPROPERTYTYPES tablosunda tanımlanmış olan özellikleri kullanıcılara, ünvanlara, departmanlara, pozisyonlara veya pozisyon gruplarına bağlamak için bu tablo kullanılır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/HRGorsel11-90d086b6-4df6-4c59-ad0c-df7d5c20cb87.png)

