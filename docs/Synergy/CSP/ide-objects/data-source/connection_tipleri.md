# DataSource Conncetion Tipleri
Synergy ortamından dış veri kaynakları ile sağlanacak bağlantılar için Connection(lar) oluşturulmalıdır.

1. Bağlantılar
    Oluşturulacak DataSource dosyaları için bağlantı sağlanacak ortamların bilgisini barındıran bölümdür. Bağlantı eklemek için IDE'de bulunan üst araç çubuğundaki Araçlar > Bağlantılar sekmeleri sırasıyla tıklanarak erişilir.
    ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-1fe7e9e2-32cd-4817-9d41-3a373ac5da06.png)

    Erişilen ekranda, mevcut bağlantılar görüntülenir. Yeni bir bağlantı tanımlanıp, tanımlanmış olan mevcut bağlantılar ya da yeni tanımlanacak bağlantılar **Test** butonuna tıklanarak test edilebilir.
    ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-2ff6b270-f4c6-43a8-965c-fedae9d707c0.png)

    ##   Yeni MSSQL, ORACLE, ODBC Bağlantısı
    1.  Genel
        Genel sekmesi altında tanımlanacak bağlantı için bir isim ve açıklama tanımlanır.

        ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-c5d40b41-3cac-4f14-a32d-6e7f2d48f80c.png)
    2.  Bağlantı Bilgileri
        Bağlantı sağlanacak ortam bilgileri tanımlanır.

        *   **Windows Oturum**
        
            ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-a445d814-ffa3-4bab-bf61-13dba61d7e58.png)

            Sunucu, Veritabanı ve Zaman aşımı bilgileri tanımlanarak bağlantı bilgileri tamamlanır.
        *   **Özel Kullanıcı**

            ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-4d8574bf-780b-414a-86b0-cd00d3c4c61c.png)

            Kullanıcı adı, Kullanıcı parolası, Sunucu, Veritabanı, Zaman aşımı bilgileri tanımlarak bağlantı bilgileri tamamlanır.
        *   **SSPI**

            ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-566eee5a-7b25-4f88-918c-32cced6047cc.png)

            Sunucu, Veritabanı, Zaman aşımı bilgileri tanımlanarak bağlantı bilgileri tamamlanır.
    3.  Gelişmiş

        ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-e55cbca8-01a2-49d7-9060-1fff57b79870.png)

        Tanımlanmış olan bağlantı bilgilerince bir ConnectionString oluşturulur, diğer bilgiler doldurulmadan direkt olarak ConnectionString ile bağlantı tanımlanmak isteniyorsa bu kısıma ConnectionString yazılarak tanımlanabilir.
    ## Yeni MySQL Bağlantısı
    1.  Genel
        Genel sekmesi altında tanımlanacak bağlantı için bir isim ve açıklama tanımlanır.

        ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-c5d40b41-3cac-4f14-a32d-6e7f2d48f80c.png)
    2. Bağlantı Bilgileri

        ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-e3ce4b38-3eda-494d-802e-9a0aba5a30f1.png)

        Kullanıcı adı, Kullanıcı parolası, Sunucu, Veritabanı ve Zaman aşımı bilgileri tanımlarak bağlantı bilgileri tamamlanır.
    3.  Gelişmiş

        ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-e55cbca8-01a2-49d7-9060-1fff57b79870.png)

        Tanımlanmış olan bağlantı bilgilerince bir ConnectionString oluşturulur, diğer bilgiler doldurulmadan direkt olarak ConnectionString ile bağlantı tanımlanmak isteniyorsa bu kısıma ConnectionString yazılarak tanımlanabilir.
    ## Yeni REST Bağlantısı
    1.  Genel
        Genel sekmesi altında tanımlanacak bağlantı için bir isim ve açıklama tanımlanır.

        ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-c5d40b41-3cac-4f14-a32d-6e7f2d48f80c.png)
    2. Bağlantı Bilgileri
        * Oturum Türleri
            *   **Gerekli Değil**

                ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-8eba1ae3-c29e-4936-9ff3-202eacbaead1.png)

                Direkt olarak sunucu bilgisi verilerek bağlantı bilgisi tamamlanır.
            *   **Kullanıcı adı ve şifre ile**

                ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-36181387-2b0b-4d54-80d0-83497f2c43ce.png)

                Bağlantı sağlanacak sunucuya kullanıcı adı ve şifre ile bağlantı sağlanması gerekiyor ise kullanıcı adı ve parola bilgisi doldurularak bağlantı bilgisi tamamlanır.
            *   **Sabit token ile**

                ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-a0bb87d0-e4ef-4a68-8afe-a1e25368f55e.png)

                Bağlantı sağlanacak sunucuya sabit bir token ile bağlantı sağlanması gerekiyor ise sabit token bilgisi doldurularak bağlantı bilgisi tamamlanır.
    3.  Başlıklar

        Bağlantı sağlanacak sunucuya gönderilecek başlıklar var ise key-value olarak doldurulmalıdır.
            ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-473d0180-388a-40d7-a0ee-f1ebe02c5f2b.png)