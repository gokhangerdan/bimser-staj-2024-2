# eBA Veritabanı Yetkileri 

eBA Server sistemin etkin şekilde Veritabanı operasyonlarını yerine getirebilmesi için  MS SQL Server üzerinde tanımlanmış Veritabano kullanıcısının bazı yetkilere ihtiyacı vardır. Bu yetkileri belirtmeden önce MS SQL Server üzerinde yer alan Veritabanı yetkilerinden bahsetmek gerekir.

## MS SQL Server Role Kavramı 

SQL Server yetkilendirme sürecini roller üzerinden 3 kısıma ayırmıştır. 
               
Bu roller; 

### Server Role

Server üzerinde gerekli yetkilendirmeyi yapmak için verilen rollerdir. 

### Database Role 

Oluşturulmuş Veritabanı üzerinde yetkilendirme yapmak için kullanılan

### Application Role 

## Server Role 

### Bulkadmin (Bulk Insert Administrator – Çoklu Kayıt Yöneticisi)

Bulk Insert komutuna yetkisi olan 

### Dbcreator (Database Creator – Veritabanı Yöneticisi) 

Database oluşturabilme, silebilme, düzenleyebilme yetkisi olan 

### Diskadmin (Disk Administrator – Dosya Yöneticisi)

Disk üzerinde bulunan dosyaları yönetme yetkisi olan 

### Processadmin (Process Administrator – İşlemci Yöneticisi) 

SQL Server üzerinde çalışan işlemcileri kontrol etme yetkisi olan. 

### Public (Herkese Kısıtlı Hak)

SQL Server üzerinde  standart ayarlarla giriş yapan herkesin rolüdür. Bu kural ile tüm kullanıcıların kısıtlı hakları vardır. Daha sonra bu kullanıcılara kural değişikliği yapılarak diğer kurallar atanabilir 

### Securityadmin (Security Administrator – Güvenlik Yöneticisi)

Server üzerinde kullanıcıların yetkilerini denetlemek, yönetmek ve şifrelerini sıfırlamak ya da istendiğinde değiştirme yetkisi olan 

### Serveradmin (Server Administrator – Server Yöneticisi)

SQL Server üzerinde yapı ayarları, başlat/durdur/yeniden başlat gibi yetkileri olan. 

### Setupadmin (Setup Administrator) 

SQL Server üzerinde farklı bir veritabanı kullanarak işlem yapma yetkisi olan 

### Sysadmin (System Administrator – Sistem Yöneticisi)

En yüksek yetkisi olandır. Sistem üzerinde tüm yetkilere sahiptir 

## Database Role 

### Db_owner

Veritabanında en yüksek yetkilidir. Silme, ekleme, düzenleme, başlatma/durdurma gibi yetkileri vardır 

### Db_accessadmin

Veritabanında kullanıcılara veritabanına erişim kural/yetki atayan yöneticidir 

### Db_securityadmin 

Veritabanındaki kural/yetkileri yönetir 

### Db_datareader

Veritabanındaki kullanıcıların “SELECT” sorgusunu çalıştırmasına izin verir 

### Db_datawriter

Veritabanındaki kullanıcıların “INSERT , DELETE , UPDATE sorgularını çalıştırmasına izin verir 

### Db_ddladmin 

Veritabanındaki kullanıcıların “DDL” komutlarını çalıştırmasına izin verir 

### Db_denydatareader

Veritabanındaki kullanıcıların “SELECT” sorgusunu çalıştırmasını kısıtlar 

### Db_denydatawriter 

Veritabanındaki kullanıcıların “INSERT , DELETE , UPDATE sorgularını çalıştırmasını kısıtlar 

### Db_backupoperator

Veritabanının yedeğini alma kuralı 

## Application Role 

Eğer “guest” hesabı oluşturursanız veritabanında, database için tek tek kullanıcı hesabı açıp tanımlamanıza gerek kalmaz.  

## eBA Sunucusunun Veritabanı Üzerinde İhtiyaç Duyduğu Operasyonel İşlemler 

eBA  Server’ ın kurulu olduğu Veri Tabanı  üzerinde ihityaç duyduğu yetkiler şunlardır:

Veri silme 

Veri Güncelleme 

Veri Ekleme 

Tablo ve kolon isimlerinde değişiklik  (ALTER) 

DB Schema düzenleme  

DB Yedeğini alabilme 

Yukarıda belirtildiği gibi eBA Server DB üzerinde belirtilen işlemleri programın kullanımı esnasında ve  uygulamanın güncellenmesi anında yapabilmesi gerekmektedir. Bu nedenle kurulum esnasında verilen SQL Kullanıcısının SQL Server DB Rolleri üzerinde karşılığı DB_owner olarak belirlenmektedir. 

