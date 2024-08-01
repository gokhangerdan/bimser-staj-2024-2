# İş Akış Yönetiminde Süreçlerin Açılmaması

Eğer canlı ortamda ya da test ortamında Süreçler sekmesinde bir süreç seçildikten sonra Süreç Detayları ekranı gelmiyor ve sağ üst tarafta 'Bir hata ile karşılaşıldı' (vb.) uyarısı alıyorsanız bunun sebeplerinden biri  CSP'nin kurulu olduğu veritabanındaki CONFIGURATIONS tablosunda  KEYNAME='DataSource.Connections.Default.ID' değerine karşılık gelen verinin IMCONNECTIONS tablosunda karşılığının olmamasıdır. Bu verinin karşılığı olmadığı için tablolar birbiri ile bağlantı kuramamaktadır.

Bu sorunu çözmek için uygulanacak yöntemlerden biri adım adım aşağıda anlatılmıştır.

### 1. Adım

```
select * from CONFIGURATIONS where KEYNAME='DataSource.Connections.Default.ID'
```

sorgusundan dönen Value değerini aşağıdaki sorguya ekleyin.
Örnek değer : '123'

```
select * from IMCONNECTIONS con  
left join IMCONNECTIONSML ml on con.ID=ml.CONNECTIONID  
where  UID='123' 
```

### 2. Adım

Yukarıdaki sorgu sonucunda gelen ID değerini (örnek ID=2) ve canlı ya da test ortamında çalışan IMCONNECTIONSML tablosunda bağlantı (örnek=sqlconnection) bilgisinin Properties verisini (örnek=RV1Rxxxx) update sorgusuna ekleyin  


Buradaki bağlantının çalıştığına emin olduktan sonra DB tarafında seçebiliriz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/SS2-725afbb0-0c88-496f-93eb-0e346d5e632f.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/SS1-95781f38-dffa-4b5b-b977-b70ff4d122e8.png)

```
update IMCONNECTIONS set PROPERTIES='RV1Rxxxx', DELETEDAT = null, DELETEDBY=null where ID=2 
```

Yukarıdaki güncellemeden sonra süreçlere erişim sağlayabilirsiniz.

