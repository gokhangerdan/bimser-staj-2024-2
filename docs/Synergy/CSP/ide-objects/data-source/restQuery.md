# Rest Query Kullanımı
Rest query sorgu tipi, RestAPI olarak tasarlanmış yapılarla iletişim kurulması için oluşturulmuştur.Buradaki iletişimin **JSON** veriler ile sağlanması gerekmektedir.

1.DataSource'da **'Yeni Öğe'** seçilmelidir ardından tip için ise REST Query seçilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/RestQueryCreateFile-57d83346-92b0-475d-af75-b61b2cbdb92c.png)


![](https://docsbimser.blob.core.windows.net/imagecontainer/restGeneral-c816e4e1-179f-49c5-8ac8-cb03ac76d084.png)

- ## Rest Query İfadeleri
    * a - Bağlantı sağlanacak RESTAPI adresini ifade etmektedir.
    * b - Bağlantı sağlanacak API adresinin farklı controllerlarına erişmek için belirtilen yönlendirmeleri ifade etmektedir.
    * c - Yapılabilecek istek tiplerini belirtmektedir.
        - GET
        - POST
        - PUT
        - COPY
        - DELETE
        - HEAD
        - MERGE
        - OPTIONS
        - PATCH
    * d - İsteğe eklenebilecek alanları ifade eden, eklemeye olana sağlayan menüdür ve eklenebilecek ifadeler şu şekildedir.
        - ![](https://docsbimser.blob.core.windows.net/imagecontainer/restAdd-9c42e094-b9a8-4cc3-a3b9-a5a76734b5ed.png)
            1. Query Parameter için kullanılabilecek parametre tipleri ise şunlardır.
                - ![](https://docsbimser.blob.core.windows.net/imagecontainer/restAdd-167f6b09-1224-4800-bde8-0c424e927ed4.png)
            2. Body için kullanılabilecek parametre tipleri ise şunlardır.
                - ![](https://docsbimser.blob.core.windows.net/imagecontainer/restAdd-e85f2eca-f81f-487c-99b1-0d1bd4ae3173.png)
            3. Header için kullanılabilecek parametre tipleri ise şunlardır. 
                - ![](https://docsbimser.blob.core.windows.net/imagecontainer/restAdd-e9f6c12b-24ad-4a01-80f5-29d44b6e033a.png)
    * e - Eklenmiş olan query parameters'ları görüntülemek veya düzenlemek için kullanılır. 
    * f - İsteğin body kısmını görüntüleme ve düzenleme işlemleri için kullanılır. 
    * g - Body'e eklenen parametreleri görüntülemek ve düzenlemek için kullanılır.
        - ![](https://docsbimser.blob.core.windows.net/imagecontainer/bodyParametersType-e4e7cc9d-5b15-4f2a-a04a-0169e27723b6.png)
            1. **'None'** ifadesi herhangi bir gövde dahil etmeden kullanım için seçilir.
            2. **'Form-data'** ifadesi form-data verisi dahil edilerek kullanım için seçilir.
            3. **'Form-url-encoded'** ifadesi Form-url-encoded verisi dahil edilerek kullanım için seçilir.
            4. **'Raw'** ifadesi JSON editör ile beraber, JSON data gönderilmek için kullanılır.
                - Örnek kullanım
                - ![](https://docsbimser.blob.core.windows.net/imagecontainer/bodyParametersType-38541ee6-792a-4787-8fe3-5999bc1d4cc0.png)
                - Parametreli örnek kullanım
                    1. Parametre verilecek ifade çift tırnak ifadesi arasında, başında @ işareti olacak şekilde tanımlanır.
                        - ![](https://docsbimser.blob.core.windows.net/imagecontainer/bodyParametersType-450066de-3c9d-49db-9138-0c47efa3974d.png)
                    2. Ekle > Body > String denilerek string bir parametre eklenir.
                        - ![](https://docsbimser.blob.core.windows.net/imagecontainer/add-be19072d-5a1a-4cd3-96f9-8a8311c0c956.png)
                    3. Eklenen parametre **'Body Parameters'** kısmında düzenlenir.
                        - ![](https://docsbimser.blob.core.windows.net/imagecontainer/add-788ac2e1-b8fc-4a35-a4a6-c1ddf76ed697.png)
    * h - Headers'e eklenen parametreleri görüntülemek ve düzenlemek için kullanılır.
- ## İstek Yapılması
    - İstek parametreleri ve gereklilikleri tanımlarak istek sağlanır. İstek yapıldıktan sonra sunucuya bir veri döndürecektir.
    - ![](https://docsbimser.blob.core.windows.net/imagecontainer/a-f62a11e0-9fb9-470f-a3e7-89e538d8e7ae.png)
    - Bölüm a
        1. Gelen verinin haritası gözükecektir.
        2. Tüm veriyi kullanmak için Root seçilir.
        3. Gelen verinin belirli bir bölümünün kullanımı için Root altında bulunan alanlardan bir tanesi seçilir.
    - Bölüm b
        1. Gelen verinin içeriği görüntülenir.
    - Bölüm c
        1. Gelen verinin içerisinde bir array ya da sınıf içermesi durumunda **'>'** işaretilye beraber alt düğümlerine erişilir.