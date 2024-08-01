# SQL Query Kullanımı
SQL query sorgu tipi, SQL destekleyen veri tabanı yapılarıyla iletişim kurulması için oluşturulmuştur.

1. DataSource'da **'Yeni Öğe'** seçilmelidir ardından tip için ise uygun bir SQL dosya tipi seçilmelidir. (Örneklerimiz MSSQL Query üzerinden ilerleyecektir.)

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/1-03b1479a-613e-4753-b2ce-3de37bac6162.png)


2.  Açılan dosya üzerindeki editör'de istenen SQL ifadeleri yazılır.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/1-498a79ed-0c4a-4624-af75-dc8cf0fc85d8.png)
    ## NOT
    ##  Parametre Kulanımı
        - Parametre kullanımı için **{{PARAMETERNAME}}** şeklinde parametreler tanımlanır.
3. Alt panel ile beraber gönderilecek parametreler, SQL sonucu döndürülen kolonların bilgileri ve sonuçlar görüntülenir.
    ![](https://docsbimser.blob.core.windows.net/imagecontainer/1-020f5b54-a185-4c90-a92d-06373ae029bf.png)
    -  Parametreler
        - Sorguda eklenen parametreler direkt olarak alt panelin içerisindeki Parametreler ekranında görüntülenecektir. Burada parametre için varsayılan değer ve parametre tipi yapılandırılır.
    ![](https://docsbimser.blob.core.windows.net/imagecontainer/1-a49b0133-43f2-433f-849d-d33f35a67254.png)
    - Kolonlar
        - Sorgu sonucu getirilen değerlerde mevcut olan kolonların ismim ve tiplerin görüntülenmesi için kullanulan penceredir.
        ![](https://docsbimser.blob.core.windows.net/imagecontainer/1-88bce281-441d-4d3d-b3cd-bb844198373c.png)
    - Sonuç
        - Sorgu sonucu getirilen verilerin (yalnızca ilk 100 satır) görüntülenmesini sağlamak için kullanılan penceredir.
        ![](https://docsbimser.blob.core.windows.net/imagecontainer/1-b65c5afd-d002-4e6e-9506-b0251daf67e9.png)
4.  Özellik Görüntüleyici ile beraber, yazılacak sorgunun;
    * Özellikler
        * Açıklama
        * Bağlantı sağlanacak veri kaynağı
        * Zaman aşımı süresi
        * Çalıştırma tipi
            * ExecuteDataAdapter, veri kaynağından veri almak için kullanılır.
            * ExecuteNonQuery, veri kaynağı döndürmeyen, işlem yapmak için kullanılan sorgu tipidir.
            * ExecuteScalar, veri kaynağından yalnızca bir satır veri dönmesi şeklinde yapılandırılan sorgular için kullanılır.
        * Komut tipi
    * Önbellek
        * Önbellek aktifliği
        * Önbellek süresi
    
    gibi yapılandırmaları sağlanır.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/1-21bda695-6562-4e3d-9497-c018ca39c2f1.png)

