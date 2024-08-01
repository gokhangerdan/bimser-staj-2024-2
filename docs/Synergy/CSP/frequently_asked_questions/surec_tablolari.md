# Synergy CSP Süreç Tabloları

## E_”PROJE ADI”_”FORM ADI”

Tasarlanan form tablosudur, bazı form tasarım nesneleri değerleri bu tablo üzerinde barındırılır.

| ID                     | bigint, not null            | PK                                                                                                                                                                                                                          |
|------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FORMID                 | bigint, not null            | FK, E_”PROJE ADI”_”FORM ADI”VR tablosundaki ID kolonu ile ilişkilidir.                                                                                                                                                      |
| VERSION                | bigint, not null            |                                                                                                                                                                                                                             |
| DOCUMENTID             | bigint, not null            |                                                                                                                                                                                                                             |
| UNIQUEID               | nvarchar(50)                | Forma tanımlanmış eşsiz id                                                                                                                                                                                                  |
| CREATEDAT              | datetimeoffset(7), not null | Oluşturulma tarihi                                                                                                                                                                                                          |
| CREATEDBY              | bigint, not null            | Oluşturan kullanıcı id’si                                                                                                                                                                                                   |
| MODIFIEDAT             | datetimeoffset(7)           | Değiştirilme tarihi                                                                                                                                                                                                         |
| MODIFIEDBY             | bigint                      | Değiştiren kullanıcı id’si                                                                                                                                                                                                  |
| DELETEDAT              | datetimeoffset(7)           | Silinme tarihi                                                                                                                                                                                                              |
| DELETEDBY              | bigint                      | Silen kullanıcı id’si                                                                                                                                                                                                       |
| MASKINPUT1             |                             | Form üzerindeki MaskInput nesnesine girilen bilginin bulunduğu kolondur. MASKINPUT1 adı, form üzerinde MaskInput nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                          |
| LOOKUP1                |                             | Form üzerindeki Lookup nesnesinde seçilen ögenin yazısının bulunduğu kolondur. LOOKUP1 adı, form üzerinde Lookup nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                          |
| RADIO1                 |                             | Form üzerindeki Radio nesnesi seçildiyse, seçimin bulunduğu kolondur. RADIO1 adı, form üzerinde Radio nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                                     |
| CHECKBOX1              |                             | Form üzerindeki CheckBox nesnesi seçildiyse, seçimin bulunduğu kolondur. CHECKBOX1 adı, form üzerinde CheckBox nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                            |
| NUMBERBOX1             |                             | Form üzerindeki NumberBox nesnesine girilen bilginin bulunduğu kolondur. NUMBERBOX1 adı, form üzerinde NumberBox nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                          |
| DATETIMEPICKER1        |                             | Form üzerindeki DateTimePicker nesnesine girilen bilginin bulunduğu kolondur. DATETIMEPICKER1 adı, form üzerinde DateTimePicker nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                           |
| DATERANGEPICKER1_START |                             | Form üzerindeki DateRangePicker nesnesinde başlangıç tarihi için girilen bilginin bulunduğu kolondur. DATERANGEPICKER1 adı, form üzerinde DateRangePicker nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir. |

| DATERANGEPICKER1_END |   | Form üzerindeki DateRangePicker nesnesinde bitiş tarihi için girilen bilginin bulunduğu kolondur. DATERANGEPICKER1 adı, form üzerinde DateRangePicker nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir. |
|----------------------|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RATE1                |   | Form üzerindeki Rate nesnesinde seçilen değer bilgisinin bulunduğu kolondur. RATE1 adı, form üzerinde Rate nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                            |
| TIMEPICKER1          |   | Form üzerindeki TimePicker nesnesinde seçilen tarih bilgisinin bulunduğu kolondur. TIMEPICKER1 adı, form üzerinde TimePicker nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                          |
| SWITCH1              |   | Form üzerindeki Switch nesnesinde aktif/pasif bilgisinin bulunduğu kolondur. SWITCH1 adı, form üzerinde Switch nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                        |
| BARCODE1             |   | Form üzerindeki Barcode nesnesinde gösterilen bilginin bulunduğu kolondur. BARCODE1 adı, form üzerinde Barcode nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                        |
| SLIDER1              |   | Form üzerindeki Slider nesnesinde seçilen değer bilgisinin bulunduğu kolondur. SLIDER1 adı, form üzerinde Slider nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                      |
| DOCUMENTMETADATA1    |   | Form üzerindeki DocumentMetadata nesnesinde gösterilen bilginin bulunduğu kolondur. DOCUMENTMETADATA1 adı, form üzerinde DocumentMetadata nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.             |
| USERMETADATA1        |   | Form üzerindeki UserMetadata nesnesinde gösterilen bilginin bulunduğu kolondur. USERMETADATA1 adı, form üzerinde UserMetadata nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                         |

## E_”PROJE ADI”_”FORM ADI”ML

Form üzerindeki çoklu dil özelliğine (Multilanguage) sahip nesnelerin bulunduğu tablodur.

| ID           | bigint, not null       | PK                                                                                                                                                                                                                                                                                              |
|--------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PARENTID     | bigint, not null       | FK, E_”PROJE ADI”_”FORM ADI” tablosundaki ID kolonu ile ilişkilidir.                                                                                                                                                                                                                            |
| CULTURE      | nvarchar(50), not null |                                                                                                                                                                                                                                                                                                 |
| TEXTBOX1     |                        | Form üzerindeki TextBox nesnesine girilen bilginin bulunduğu kolondur. TEXTBOX1 adı, form üzerinde Textbox nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir. Nesnede çoklu dil girişi açıksa, CULTURE kolonunda diğer dil/diller için girilen bilgiler görülebilir.             |
| PASSWORD1    |                        | Form üzerindeki Password nesnesine girilen bilginin bulunduğu kolondur. PASSWORD1 adı, form üzerinde Password nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                                                                                                 |
| LOOKUP1      |                        | Form üzerindeki Lookup nesnesinde seçilen ögenin değerinin bulunduğu kolondur. LOOKUP1 adı, form üzerinde Lookup nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                                                                                              |
| TEXTAREA1    |                        | Form üzerindeki TextArea nesnesine girilen bilginin bulunduğu kolondur. TEXTAREA1 adı, form üzerinde TextArea nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir. Nesnede çoklu dil girişi açıksa, CULTURE kolonunda diğer dil/diller için girilen bilgiler görülebilir.          |
| SEACHBOX1    |                        | Form üzerindeki SearchBox nesnesine girilen bilginin bulunduğu kolondur. SEACHBOX1 adı, form üzerinde SearchBox nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir.                                                                                                               |
| HTMLTEXTBOX1 |                        | Form üzerindeki HTMLTextBox nesnesine girilen bilginin bulunduğu kolondur. HTMLTEXTBOX1 adı, form üzerinde HTMLTextBox nesnesine verilmiş isimlendirmeye göre değişkenlik gösterecektir. Nesnede çoklu dil girişi açıksa, CULTURE kolonunda diğer dil/diller için girilen bilgiler görülebilir. |

## E_”PROJE ADI”_”FORM ADI”RD

Form üzerinde ilişkili dokümanlar nesnesine eklenen dosyaların bilgisini tutan tablodur.

| ID         | bigint, not null | PK                                                                                              |
|------------|------------------|-------------------------------------------------------------------------------------------------|
| PARENTID   | bigint, not null | FK, Bağlı olduğu form bilgisi. E_”PROJE ADI”_”FORM ADI” tablosundaki ID kolonu ile ilişkilidir. |
| CATEGORYID | bigint, not null | FK, E_”PROJE ADI”_”FORM ADI”RDC tablosundaki ID kolonu ile ilişkilidir.                         |
| FILEID     | bigint, not null | Form üzerindeki İlişkili dokümanlar nesnesine yüklenen dosyanın ID bilgisidir.                  |

## E_”PROJE ADI”_”FORM ADI”RDC

Form üzerinde ilişkili dokümanlar nesnesinde kategori bilgisini tutan tablodur.

| ID        | bigint, not null       | PK                                                                                                                                                     |
|-----------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| KEY       | nvarchar(50)           | İlişkili Dokümanlar nesnesindeki Kategoriye tanımlanan benzersiz ID bilgisidir. E_”PROJE ADI”_”FORM ADI”RDCML tablosundaki KEY kolonu ile ilişkilidir. |
| PARENTID  | bigint, not null       |                                                                                                                                                        |
| CONTROLID | nvarchar(50), not null | Kategorinin tanımlandığı İlişkili Dokümanlar nesnesinin isminin bulunduğu kolondur.                                                                    |

## E_”PROJE ADI”_”FORM ADI”RDCML

Form üzerinde ilişkili dokümanlar nesnesinde kategori bilgisinin çoklu dil karşılıklarını tutan tablodur.

| NAME        | nvarchar(100), not null | İlişkili Dokümanlar nesnesine eklenmiş kategorinin, “Kategori İsmi” alanına yazılmış bilginin bulunduğu kolon.                                       |
|-------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| DESCRIPTION | nvarchar(250)           | İlişkili Dokümanlar nesnesine eklenmiş kategorinin, “Açıklama” alanına yazılmış bilginin bulunduğu kolon.                                            |
| ID          | bigint, not null        | PK                                                                                                                                                   |
| PARENTID    | bigint, not null        | FK, E_”PROJE ADI”_”FORM ADI”RDC tablosundaki ID kolonu ile ilişkili.                                                                                 |
| CULTURE     | nvarchar(10), not null  | İlişkili dokümanlar nesnesinde Kategori İsmi, Açıklama alanında girilen bilgilerin hangi kültürde yazıldığını gösteren kolondur (tr-TR gibi)         |
| KEY         | nvarchar(50)            | İlişkili Dokümanlar nesnesindeki Kategoriye tanımlanan benzersiz ID bilgisidir. E_”PROJE ADI”_”FORM ADI”RDC tablosundaki KEY kolonu ile ilişkilidir. |

## E_”PROJE ADI”_”FORM ADI”RDML

Form üzerinde ilişkili dokümanlar nesnesine eklenen dosyalara ait açıklamanın çoklu dil bilgisini tutan tablodur.

| DESCRIPTION | nvarchar(250), not null | İlişkili Dokümanlar nesnesine yüklenen dosyaya girilen açıklama bilgisinin bulunduğu kolondur. |
|-------------|-------------------------|------------------------------------------------------------------------------------------------|
| ID          | bigint, not null        | PK                                                                                             |
| PARENTID    | bigint, not null        | FK, E_”PROJE ADI”_”FORM ADI”RD tablosundaki ID kolonu ile ilişkilidir.                         |
| CULTURE     | nvarchar(10), not null  | Açıklamanın girildiği kültür bilgisi (tr-TR gibi)                                              |

## E_”PROJE ADI”_”FORM ADI”SL

Form üzerinde seçim (Selection) tipindeki (Dropdown, Combobox, ListBox, RadioList, AutoComplete, Tagbox, Transfer) nesnelerin ismini ve seçilmiş değeri barındıran tablodur.

| ID        | bigint, not null       | PK                                                                                                                                                                       |
|-----------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PARENTID  | bigint, not null       | FK, E_”PROJE ADI”_”FORM ADI” tablosundaki ID kolonu ile ilişkilir.                                                                                                       |
| CONTROLID | nvarchar(50), not null | Formda kullanılan Dropdown, Combobox, ListBox, RadioList, AutoComplete, Tagbox, Transfer nesnesi varsa, bunların adının bulunduğu kolondur                               |
| VALUE     | sql_variant, not null  | Formda kullanılan Dropdown, Combobox, ListBox, RadioList, AutoComplete, Tagbox, Transfer nesnesi varsa, bunların her birinde seçilen ögenin değerinin bulunduğu kolondur |

## E_”PROJE ADI”_”FORM ADI”SLML

E_”PROJE ADI”_”FORM ADI”SL tablosundaki CONTROLID kolonundaki nesnenin, seçilen VALUE değerinin karşılığını kültürü ile barındıran tablodur.

| ID       | bigint, not null        | PK                                                                                                                   |
|----------|-------------------------|----------------------------------------------------------------------------------------------------------------------|
| PARENTID | bigint, not null        | FK, E_”PROJE ADI”_”FORM ADI”SL tablosundaki ID kolonu ile ilişkilir.                                                 |
| CULTURE  | nvarchar(10), not null  | Kültür adı (tr-TR gibi)                                                                                              |
| TEXT     | nvarchar(500), not null | E_”PROJE ADI”_”FORM ADI”SL tablosundaki CONTROLID kolonundaki nesnenin, seçilen VALUE değerinin yazısını barındırır. |

## E_”PROJE ADI”_”FORM ADI”_DataGrid (Statik/Dinamik Kolon, Veri Kaynağı Seçilmemiş)

Form üzerinde DataGrid nesnesi tipi Dinamik seçilip sorgudan beslenecek şekilde ayarlandıysa veya sorgular bağlanmadan statik kolonlar oluşturulduysa, belirli kolon tiplerine girilen bilginin barındırıldığı tablodur.

| ID                                    | bigint, IDENTITY(1,1), not null | PK                                                                                                                                      |
|---------------------------------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| PARENTID                              | bigint, not null                | FK, E_”PROJE ADI”_”FORM ADI” tablosundaki ID kolonu ile ilişkilidir.                                                                    |
| CREATEDAT                             | datetimeoffset(7)               | Oluşturulma tarihi                                                                                                                      |
| CREATEDBY                             | bigint                          | Oluşturan kişi, OSUSERS’daki ID kolonu ile ilişkilidir.                                                                                 |
| MODIFIEDAT                            | datetimeoffset(7)               | Değiştirilme tarihi                                                                                                                     |
| MODIFIEDBY                            | bigint                          | Değiştiren kullanıcı id’si                                                                                                              |
| DELETEDAT                             | datetimeoffset(7)               | Silinme tarihi                                                                                                                          |
| DELETEDBY                             | bigint                          | Silen kullanıcı id’si                                                                                                                   |
| NUMBER, BOOLEAN, DATETIME, DATE, TIME |                                 | DataGrid nesnesinde Colums alanında Number, Boolean, DateTime, Date, Time tipinde kolonlar eklendiyse bu bilgilerin bulunduğu kolondur. |

## E_”PROJE ADI”_”FORM ADI”_DataGridML

Form üzerinde DataGrid nesnesinde Text tipindeki kolona girilen bilgiyi barındıran tablodur.

| ID       | bigint, IDENTITY(1,1), not null | PK                                                                                                |
|----------|---------------------------------|---------------------------------------------------------------------------------------------------|
| PARENTID | bigint, not null                | FK, E_”PROJE ADI”_”FORM ADI”_DataGrid tablosundaki ID kolonu ile ilişkilidir.                     |
| CULTURE  | nvarchar(10), not null          | Kültür adı (tr-TR gibi)                                                                           |
| TEXT     |                                 | DataGrid nesnesinde Colums alanında Text tipinde kolon eklendiyse bu bilginin bulunduğu kolondur. |

## E_”PROJE ADI”_”FORM ADI”_DataGridSL

Form üzerinde DataGrid nesnesinde Select tipindeki kolonda seçilen ögenin değerini (value) barındıran

tablodur.

| ID        | bigint, IDENTITY(1,1), not null | PK                                                                                                                                          |
|-----------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| PARENTID  | bigint, not null                | FK, E_”PROJE ADI”_”FORM ADI”_DataGrid tablosundaki ID kolonu ile ilişkilidir.                                                               |
| CONTROLID | nvarchar(50), not null          | DataGrid nesnesinde Colums alanında Select tipinde kolon eklendiyse, eklenen kolonun adının bulunduğu kolondur.                             |
| VALUE     |                                 | DataGrid nesnesinde Colums alanında Select tipinde eklenen kolonda seçilen ögenin değer (Value) alanında yazan bilginin bulunduğu kolondur. |

## E_”PROJE ADI”_”FORM ADI”_DataGridSLML

Form üzerinde DataGrid nesnesinde Select tipindeki kolonda seçilen ögenin yazısını (text) barındıran

tablodur.

| ID       | bigint, IDENTITY(1,1), not null | PK                                                                                                 |
|----------|---------------------------------|----------------------------------------------------------------------------------------------------|
| PARENTID | bigint, not null                | FK, E_”PROJE ADI”_”FORM ADI” \_DataGrid1SL tablosundaki ID kolonu ile ilişkilidir.                 |
| CULTURE  | nvarchar(10), not null          | Kültür adı (tr-TR gibi)                                                                            |
| TEXT     | nvarchar(500)                   | E_”PROJE ADI”_”FORM ADI” \_DataGrid1SL tablosunda bulunan değerin yazı (Text) kısmında yazan bilgi |

## E_”PROJE ADI”_”FORM ADI”_DataGrid (İlişkili Data Grid)

Form üzerinde veri kaynağı tipi “İlişkili” olarak seçilmiş DataGrid nesnesindeki bilgilerin tutulduğu tablodur.

| ID                 | bigint, IDENTITY(1,1), not null | PK                                                                   |
|--------------------|---------------------------------|----------------------------------------------------------------------|
| PARENTID           | bigint, not null                | FK, E_”PROJE ADI”_”FORM ADI” tablosundaki ID kolonu ile ilişkilidir. |
| RELATIONDOCUMENTID |                                 | Nesneye bağlanan ilişkili olduğu form ID’si                          |
| CREATEDAT          | datetimeoffset(7)               | Oluşturulma tarihi                                                   |
| CREATEDBY          | bigint                          | Oluşturan kişi, OSUSERS’daki ID kolonu ile ilişkilidir.              |
| MODIFIEDAT         | datetimeoffset(7)               | Değiştirilme tarihi                                                  |
| MODIFIEDBY         | bigint                          | Değiştiren kullanıcı id’si                                           |
| DELETEDAT          | datetimeoffset(7)               | Silinme tarihi                                                       |
| DELETEDBY          | bigint                          | Silen kullanıcı id’si                                                |

## E_”PROJE ADI”_”FORM ADI”_Scheduler

Form üzerinde Scheduler nesnesinde eklenen görevlere ait tarih bilgilerini barındıran tablodur.

| ID         | bigint, IDENTITY(1,1), not null | PK                                                                   |
|------------|---------------------------------|----------------------------------------------------------------------|
| PARENTID   | bigint, not null                | FK, E_”PROJE ADI”_”FORM ADI” tablosundaki ID kolonu ile ilişkilidir. |
| STARTDATE  |                                 | Scheduler nesnesine eklenen planın başlangıç tarihi bilgisi          |
| ENDDATE    |                                 | Scheduler nesnesine eklenen planın bitiş tarihi bilgisi              |
| CREATEDAT  | datetimeoffset(7)               | Oluşturulma tarihi                                                   |
| CREATEDBY  | bigint                          | Oluşturan kişi, OSUSERS’daki ID kolonu ile ilişkilidir.              |
| MODIFIEDAT | datetimeoffset(7)               | Değiştirilme tarihi                                                  |
| MODIFIEDBY | bigint                          | Değiştiren kullanıcı id’si                                           |
| DELETEDAT  | datetimeoffset(7)               | Silinme tarihi                                                       |
| DELETEDBY  | bigint                          | Silen kullanıcı id’si                                                |

## E_”PROJE ADI”_”FORM ADI”_SchedulerML

Form üzerinde Scheduler nesnesinde eklenen görevlere girilen açıklama bilgilerini barındıran tablodur.

| ID       | bigint, IDENTITY(1,1), not null | PK                                                                             |
|----------|---------------------------------|--------------------------------------------------------------------------------|
| PARENTID | bigint, not null                | FK, E_”PROJE ADI”_”FORM ADI”_Scheduler tablosundaki ID kolonu ile ilişkilidir. |
| CULTURE  | nvarchar(10), not null          | Kültür bilgisi (tr-TR gibi)                                                    |
| TITLE    | nvarchar(500)                   | Scheduler nesnesine eklenen plana yazılan açıklama bilgisi                     |

## E_”PROJE ADI”_”FORM ADI”VR

Formun versiyon bilgisini barındıran tablodur.

| ID      | bigint, IDENTITY(1,1), not null | PK, E_”PROJE ADI”_”FORM ADI” tablosunda FORMID kolonu ile ilişkilendirilebilir. |
|---------|---------------------------------|---------------------------------------------------------------------------------|
| VERSION | bigint, not null                | E_”PROJE ADI”_”FORM ADI” tablosunda VERSION kolonu ile ilişkilendirilebilir.    |

1.  Sistem Tabloları

DOCUMENTS

CSP sisteminde oluşturulmuş dokümanlarla ilgili bilgilerin tutulduğu tablodur.

| ID                | bigint, not null            | PK, Sürece ait E ile başlayan form tablosunda DOCUMENTID kolonu ile ilişkilidir. |
|-------------------|-----------------------------|----------------------------------------------------------------------------------|
| PROJECT           | nvarchar(255), not null     | Dokümana sahip olan sürecin adı                                                  |
| FORM              | nvarchar(255), not null     | Form adı                                                                         |
| UNIQUEID          | nvarchar(255)               | Tanımlı formatla özelleştirilmiş doküman numarası                                |
| CREATEDBY         | bigint, not null            | Dokümanı oluşturan kişi, OSUSERS tablosundaki ID kolonu ile ilişkilidir.         |
| CREATEDELEGATEDBY | bigint                      |                                                                                  |
| CREATEDAT         | datetimeoffset(7), not null | Dokümanın oluşturulma tarihi                                                     |
| DELETEDBY         | bigint                      | Dokümanı silen kişi, OSUSERS tablosundaki ID kolonu ile ilişkilidir.             |
| DELETEDAT         | datetimeoffset(7)           | Dokümanın silinme tarihi                                                         |
| DELETEDELEGATEDBY | bigint                      |                                                                                  |
| STATUS            | int                         |                                                                                  |
| MODIFIEDBY        | bigint                      |                                                                                  |
| MODIFYDELEGATEDBY | bigint                      |                                                                                  |
| MODIFIEDAT        | datetimeoffset(7)           |                                                                                  |

## OSUSERS

Sistemdeki kullanıcıları ve kullanıcılara ait bazı bilgileri içeren tablodur. Ayrıca OS ile başlayan diğer tablolar ile JOIN yapılarak kullanılabilir.

| ID               | int, IDENTITY(1,1), not null | PK, Kullanıcı ID’si                                                                         |
|------------------|------------------------------|---------------------------------------------------------------------------------------------|
| USERNAME         | nvarchar(50), not null       | Kullanıcı sicili                                                                            |
| FIRSTNAME        | nvarchar(50), not null       | Ad                                                                                          |
| LASTNAME         | nvarchar(50), not null       | Soyad                                                                                       |
| PASSWORD         | nvarchar(255), not null      | Şifre                                                                                       |
| EMAIL            | nvarchar(200), not null      | E-posta                                                                                     |
| STATUS           | int, not null                | Kullanıcının aktif mi pasif mi olduğunu gösteren bilgi 0: Pasif 1: Aktif                    |
| TYPE             | int                          | Kullanıcı tipi 0: Normal 1:Özel                                                             |
| IMPORTSTATUS     | int                          | İnsan Kaynakları aktarımından mı geleceğini gösteren bilgi 0:Pasif 1:Aktif                  |
| BIRTHDATE        | datetimeoffset(7)            | Doğum tarihi                                                                                |
| EMPLOYEMENTSTART | datetimeoffset(7)            | İşe başlama tarihi                                                                          |
| EMPLOYEMENTEND   | datetimeoffset(7)            | İşten ayrılma tarihi                                                                        |
| CATEGORY         | int                          | Kullanıcı kategorisi 0: Mavi Yaka 1: Beyaz Yaka                                             |
| SEX              | int                          | Kullanıcı cinsiyeti 0: Kadın 1:Erkek                                                        |
| DEPARTMENT       | int, not null                | Kullanıcının bulunduğu departman kodu, OSDEPARTMENTS tablosundaki ID kolonu ile ilişkilidir |
| PROFESSION       | int, not null                | Kullanıcının unvan kodu, OSPROFESSIONS tablosundaki ID kolonu ile ilişkilidir               |

## PROJECTS

Proje özelliklerini içeren tablodur.

| ID                | nvarchar(38), not null      | PK                                                                             |
|-------------------|-----------------------------|--------------------------------------------------------------------------------|
| NAME              | nvarchar(100), not null     | Proje ismi                                                                     |
| CREATEDBY         | bigint, not null            | Projeyi oluşturan kişi, OSUSERS tablosundaki ID kolonunda yazan bilgi yazılır. |
| CREATEDELEGATEDBY | bigint                      |                                                                                |
| CREATEDAT         | datetimeoffset(7), not null | Proje oluşturulma tarihi                                                       |
| PROJECTPATH       | nvarchar(250)               | Projenin bulunduğu dizin                                                       |
| STATUS            | bit, not null               | Proje aktif mi pasif mi bilgisi Aktif: 1 Pasif: 0                              |
| BUILDVERSION      | int, not null               | Projenin derleme versiyonu                                                     |
| DEPLOYMENTID      | bigint                      |                                                                                |
| FASTAPPROVE       | bit, not null               | Hızlı onay 0: Kapalı 1: Açık                                                   |

| HIDEAPPROVALS     | bit, not null | Onaycıları gizle 0: Kapalı 1: Açık                        |
|-------------------|---------------|-----------------------------------------------------------|
| DELEGABLE         | bit, not null | Vekâlet verilebilir 0: Kapalı 1: Açık                     |
| SHOWPARENTHISTORY | bit, not null | Bağlı olduğu an akış tarihçesini göster 0: Kapalı 1: Açık |

## PROCESSES

| ID                 | bigint, not null            | PK, Süreç numarası                                                                       |
|--------------------|-----------------------------|------------------------------------------------------------------------------------------|
| PROJECTID          | nvarchar(38), not null      | Proje ID’si. Projects tablosundaki ID kolonu ile ilişkilidir.                            |
| FLOWID             | nvarchar(38), not null      | Süreçte kullanılan akış ID’si.                                                           |
| DEPLOYMENTID       | bigint, not null            |                                                                                          |
| USERID             | int, not null               | Süreci başlatan kullanıcı ID’si. OSUSERS tablosundaki ID kolonu ile ilişkilidir.         |
| DELEGATIONID       | int                         | Süreci vekâleten başlatan kullanıcı adı. OSUSERS tablosundaki ID kolonu ile ilişkilidir. |
| FLOWSTATUSID       | bigint                      | FK, PROJECTFLOWSTATUSES tablosundaki ID kolonu ile ilişkilidir.                          |
| WORKFLOWINSTANCEID | nvarchar(38), not null      |                                                                                          |
| CREATEDATE         | datetimeoffset(7), not null | Sürecin başlatıldığı tarihi                                                              |
| FINISHDATE         | datetimeoffset(7)           | Sürecin tamamlandığı tarih                                                               |
| LASTEXECUTEDATE    | datetimeoffset(7), not null |                                                                                          |
| DELETEDATE         | datetimeoffset(7)           | Sürecin silindiği tarih                                                                  |
| PARENTPROCESSID    | bigint                      | Varsa bağlı olduğu ana akışın süreç numarası                                             |

PROJECTFORMS

Projelerde tasarlanan formları içeren tablodur.

| ID                | nvarchar(38), not null  | PK, Proje formunun ID’sidir.                                                                 |
|-------------------|-------------------------|----------------------------------------------------------------------------------------------|
| PROJECTID         | nvarchar(38), not null  | FK, PROJECTS tablosundaki ID kolonu ile ilişkilidir.                                         |
| NAME              | nvarchar(100), not null | Formun adı                                                                                   |
| FORMTYPE          | int, not null           | Form Tipi 0: Standart Form 1: Parametreli Form 2: Görünüm Formu 3: Onay Listesi Formu        |
| IDFORMATID        | bigint, not null        | Formda Özellik Görüntüleyicisinde Identity Format alanında seçilen form kimlik formatı id’si |
| IDFORMAT          | nvarchar(100), not null | Formda Özellik Görüntüleyicisinde Identity Format alanında seçilen form kimlik formatı adı   |
| ALLOWCOPYPASTE    | bit, not null           |                                                                                              |
| READONLY          | bit, not null           | Formda Read Only özelliği aktif olup olmadığını belirtir 0: Pasif 1: Aktif                   |
| PRINTINGENABLED   | bit, not null           | Formu yazdırmanın aktif olup olmadığını belirtir 0: Pasif 1: Aktif                           |
| PRINTVIEW         | nvarchar(100), not null | Formda yazdırılacak görünümün ismi                                                           |
| VERSIONINGENABLED | bit, not null           | Formda versiyonlama özelliğinin açık olmadığını belirtir                                     |

|   |   | 0: Pasif 1: Aktif |
|---|---|-------------------|

## PROJECTFLOWS

Projelerde tasarlanan akışları içeren tablodur.

| ID             | nvarchar(38), not null  | PK, Proje akışının id’si                             |
|----------------|-------------------------|------------------------------------------------------|
| PROJECTID      | nvarchar(38), not null  | FK, PROJECTS tablosundaki ID kolonu ile ilişkilidir. |
| NAME           | nvarchar(100), not null | Akışın ismi                                          |
| APPROVERFORMID | nvarchar(38)            |                                                      |

## PROCESSREQUESTDOCUMENTS

Süreç isteklerinde tanımlanmış dokümana ait detayların olduğu tablodur..

| ID                      | bigint, IDENTITY(1,1),not null | PK                                                                 |
|-------------------------|--------------------------------|--------------------------------------------------------------------|
| PROCESSREQUESTID        | bigint, not null               | FK, PROCESSREQUESTS tablosunda ID kolonu ile ilişkilidir.          |
| ORDERNO                 | int, not null                  |                                                                    |
| DOCUMENTID              | bigint, not null               | Doküman ID’si                                                      |
| FORMID                  | nvarchar(38), not null         | Formun Id’si. PROJECTFORMS tablosundaki ID kolonu ile ilişkilidir. |
| DOCUMENTTYPE            | int, not null                  |                                                                    |
| ALLOWEDIT               | bit, not null                  | Değişiklik yapılabilir mi bilgisi 0: Pasif 1: Aktif                |
| ISMODIFIED              | bit, not null                  |                                                                    |
| DIGITALSIGNATURETYPE    | int, not null                  |                                                                    |
| SHOWEVENTS              | bit, not null                  | Olayların görünüp görünmeyeceğini belirten veri 0: Pasif 1: Aktif  |
| DIGITALSIGNATUREOPTIONS | nvarchar(max), not null        | Dijital imza bilgileri                                             |

## PROCESSREQUESTS

Süreç isteklerinin adımlarının bulunduğu tablodur.

| ID           | bigint, IDENTITY(1,1), not null | PK                                                    |
|--------------|---------------------------------|-------------------------------------------------------|
| PROCESSID    | bigint, not null                | FK, PROCESSES tablosundaki ID kolonu ile ilişkilidir. |
| REQUESTTYPE  | int, not null                   |                                                       |
| STATUS       | int, not null                   |                                                       |
| EVENTID      | int, not null                   | Süreçte işlem yapılmak için kullanılan butonun id’si  |
| EVENTFORMID  | int                             | Event form ID bilgisi                                 |
| OBJECTNAME   | nvarchar(100), not null         | Yapılan isteğin akış nesnesi bilgisi                  |
| REQUESTDATE  | datetimeoffset(7), not null     | İsteğin yapıldığı tarih                               |
| RESPONSEDATE | datetimeoffset(7)               | İsteğe cevap verilen tarih                            |

| POSITIONID      | int               | İstek pozisyon ile yapıldıysa pozisyon ID bilgisi                              |
|-----------------|-------------------|--------------------------------------------------------------------------------|
| USERID          | int               | İstek kullanıcı ile yapıldıysa kullanıcı ID bilgisi                            |
| DELEGATIONID    | int               |                                                                                |
| PROCESSSTEPID   | bigint, not null  |                                                                                |
| HIDDENTYPE      | int               |                                                                                |
| DELETEDFROMLIST | bit, not null     |                                                                                |
| OWNEDREQUESTID  | int               |                                                                                |
| OWNEDENABLED    | bit, not null     |                                                                                |
| OWNEDDATE       | datetimeoffset(7) |                                                                                |
| EVENTS          | nvarchar(max)     | Nesne üzerindeki olaylar                                                       |
| SHOWINHISTORY   | bit               | Akış tarihçesinde gösterilsin mi bilgisi 0: Pasif 1: Aktif                     |
| HIDEAPPROVER    | bit               | Onaylayan kişi bilgisinin gizlenip gizlenmeyeceğini gösterir 0: Pasif 1: Aktif |
| AUTOOPEN        | bit               | Onaylar otomatik onayda açılsın mı bilgisi 0: Otomatik aç 1: Otomatik Açma     |
| TIMEOUT         | nvarchar(max)     | Nesnedeki zaman aşımı bilgisi                                                  |

## PROJECTFLOWSTATUSES

Projede akış durumlarının detaylarını barındıran tablodur.

| ID           | bigint, not null        | PK, PROCESSES tablosundaki FLOWSTATUSID kolonu ile ilişkilidir.                                                                          |
|--------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| FLOWID       | nvarchar(38), not null  | FK, PROJECTFLOWS tablosundaki ID kolonu ile ilişkilidir.                                                                                 |
| DEPLOYMENTID | bigint, not null        | FK, PROJECTDEPLOYMENTS tablosundaki ID kolonu ile ilişkilidir.                                                                           |
| STATUSID     | int, not null           | Akış durumunun kimlik numarası                                                                                                           |
| ICON         | nvarchar(100), not null | Akış durumu için seçilen resim                                                                                                           |
| FLOWVIEW     | nvarchar(100), not null | Akış görünümü false: Akışta ilgili durumda akış görünümü özelliği seçili değil true: Akışta ilgili durumda akış görünümü özelliği seçili |

## PROJECTFLOWSTATUSESML

Projede akış durumlarının kültürlerine göre açıklamalarını barındıran tablodur.

| ID           | bigint, not null      | PK                                                              |
|--------------|-----------------------|-----------------------------------------------------------------|
| FLOWSTATUSID | bigint, not null      | FK, PROJECTFLOWSTATUSES tablosundaki ID kolonu ile ilişkilidir. |
| CULTURE      | nvarchar(5), not null | Kültür adı                                                      |
| CAPTION      | nvarchar(max)         | Akış durumunun ilgili kültürde açıklaması                       |
