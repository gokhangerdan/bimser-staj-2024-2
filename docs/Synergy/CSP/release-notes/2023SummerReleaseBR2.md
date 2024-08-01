---
sidebar_position: 2334
sidebar_label: "2023 Summer Release BR2"
custom_edit_url: ""
---

# Bimser Synergy 2023 Summer Release Notes BR2
*(1 Ekim 2023 - 31 Ekim 2023)*

## 1. Highlights / New Features

- 61329 [DR2123] - **GetFlowsByProjectName endpointi eklendi**. **Payload** bilgisinde
    **proje adı** yazıldığı zaman o projeye ait **Akış bilgilerinin getirilmesi** sağlandı.
- 54821 - Geliştirme arayüzünde **Bağlantılar** alanında **GPT bağlantı** seçeneği ve
    **Datasource tiplerine GPT seçeneği** eklendi.
- 56622 - Geliştirme arayüzünde **DataGrid** nesnesine **On Cell Prepared olayı** eklendi.
    Bu olay ile **Datagrid kolonlarında hücre üzerinde CSS özelliğinin girilebilmesi**
    sağlandı.
    **Örnek:**
    async DataGrid7_OnCellPrepared(args: Controls.EventArgs.ICellPreparedEventArgs) {

```
const uniqueDataField = this.DataGrid7.columns?.find(item =>
item.isPrimaryKey)?.name;
if (args.data[uniqueDataField] == 2) {
args.cellElement.style.backgroundColor = "yellow";
}
```
```
if (args.column.name === "NewColumn2") {
args.cellElement.style.color = args.data.NewColumn2 > 5? "green" : "red";
args.cellElement["className"] = args.data.NewColumn2 > 5?
"testClassGreen" : "testClassRed";
}
```
```
}
```
- 60995 – Web arayüzünde **Giriş** sayfasındaki **Kullanıcı Adı** ve **Parola** , **Erişim Anahtarı** ,
    **Mobil İmza** , **Harici Hesaplar** formlarındaki nesnelere ve **Sunucu Qr kodu** , **Dil Seçim** ,
    **App Store** ve **Google Play** yönlendirme nesnelerine **Data-Selenium-ID Attribute'ı**
    eklenmiştir. **Dijital imza formu IFrame içinde** olduğundan **güncelleme bu alana**
    **uygulanmamıştır.**
- 60999 – Web arayüzünde **Dashboard** sayfasındaki **reloadButton** , **recentApps** ,
    **countTiles, announcements, process, ProcessDetails, RecentFiles** ve **Tümünü Göster**
    elementlerine **Data-Selenium-ID Attribute'si** eklenmiştir.
- 61178 - Web arayüzünde **Düğüm İşlem Türü** içerisindeki **eBA Entegrasyonu** özelliğine
    ait Entegrasyon Türü içerisine **"Geçmiş İşler"** menüsü eklendi. Bu menü " **Menü Ekle** "
    seçeneği içerisinden eklenebilmektedir. CSP içerisinde açılan **eBA panelinin Geçmiş**
    **bölümünü** kullanıcıya getirir.


- 54826 - Geliştirme arayüzünde **DataSynchronizer** adında **yeni bir nesne** eklendi. Bu
    nesne aynı **ContextMenu gibi tasarım ekranının altında** bulunur. **Source** yani kaynak
    değeri için bir **Path** belirlendikten sonra **Target** yani Hedef **Pathleri de belirlemek**
    gerekir. Bu sayede **Kaynak Path** üzerinde bulunan veriyi, **Hedef nesnelerin** belirtilen
    **Path değerlerine atama işlemi** yapar. Bu işlemin ne zaman gerçekleşmesi gerektiği
    ise **triggerEvent** ile belirlenebilir. Hedef belirlerken **Prompt** kısmına bu veriyi nasıl bir
    işlemden geçirmesi gerektiğini **ChatGPT'de belirtmek** gerekir.
- 61663 - Geliştirme arayüzüne **Signature (İmza) nesnesi** eklendi. Bu nesne Web
    arayüzünde **formda bir çizim alanı olarak** kullanılır. İçerisine atılan imza
    kaydedilebilir. Kalem, el ya da fare ile imza atılabilir**. İçerisine atılan imza**
    **kaydedilebilir olarak tasarlandı**.
- 62623 - Geliştirme arayüzünde **RelatedDocuments** nesnesinin **Events** kısmının **Client**
    başlığı altına **OnBeforeFileUpload** adında **yeni bir client event** eklendi. Bu olay ile
    Web arayüzünde **nesneye yüklenen dosyanın adının başına** , **kod bloğunda belirtilen**
    **diğer ad** gelmektedir. Bu değişen isim aynı zamanda **Doküman Yönetiminde ilgili**
    **klasör içerisine yüklenen dosyanın adını da** değiştirmektedir.

```
async RelatedDocuments1_OnBeforeFileUpload(args: { name: string, file: File }) {
const name = "yeniAd" + args.file.name;
const file = new File([args.file], name, { type: args.file.type });
```
```
return file;
}
```
- 64089 - Geliştirme arayüzünde, **ServiceApi'deki GridData** sınıfına **DataSourceType** ve
    **SaveAction özellikleri eklendi**.

```
Control dataGridControl = Document1.Controls["DataGrid1"];
GridData dataGrid = GridData.FromControl(dataGridControl);
```
```
string dataSourceType = dataGrid.DataSourceType;
bool saveAction = dataGrid.SaveAction;
```
- 48309 - Web arayüzünde **GetProcessAvgTime, GroupByUserAvgTime,**
    **GroupByMonthlyProcesses Admin - Dashboard ekranı** için **endpointler** eklendi.
- 40655 - **Projelerin listesini ve o projeye ait aktif olarak üzerinde akış bulunan**
    **versiyonlarını döndüren bir endpoint** eklendi.

```
Url/api/ide/ProjectManager/GetActiveFlowProjectVersions
```
- 63268 - Geliştirme arayüzünde **Akış Yöneticisinde GetProcessesLean** endpointine
    **HasError** ve **ErroInfo propertyleri** eklendi.


- 63569 - Formun **mobilden açıldığı bilgisinin tutulacağı IsMobile: Boolean özelliği**
    eklendi.
- 64186 - Web arayüzünde **Allow Null** özelliği **kapalı** olan **Datagrid** kolonunda **uyarı**
    **tiplerinin düzenlenebilir** olması ve **verilen uyarının özelleştirilmesi** sağlandı.
    Kolonun **Allow Null** özelliği **Pasif** edildiğinde, **Customize Null text kolonu** aktif olur.
    **Null Text** alanına verilmek istenen **uyarı başlığı** girilir. **AlertType** seçeneğinden ise,
    **uyarı tipi(Info, Warning, Error)** seçilebilir.
- 64666 - **GetPackageVersions endpointi** eklendi. Girilen **Proje** ve **Flow** adına göre
    **paket versiyon bilgilerinin gösterilmesi** sağlandı.
    Url/DeployAgentId/deployagent/apps/ProjectName/latest/api/FlowName/GetPacka
    geVersions


## 2. Improvements

- 55339 - Web arayüzü **Doküman Yönetiminde Çalışma Başlat** denildikten **İçerikler**
    ekranından, **İçeriklerin isimleri** ve **açıklamalarının** düzenlenebilmesi için
    **RenameObject endpointine parametreler** geliştirildi.
- 60484 - **Vekalet ve Erişim anahtarları** için **Yetki Kapsamı** çekilen endpoint'e alternatif
    olarak istenilen kırılımdan başlayarak, istenilen kadar derinlikte **kapsamları dönen**
    **endpoint'in yazılması** sağlandı. **Postman üzerinde** ;

```
POST {{webinterfacewebapiurl}}/Permission/GetUserPermissionScopeTreeItem
{
"parent" : ["sysfullaccess"],
"depth" : 1
}
ve
{
"parent" : ["webfullaccess","web.announcement"],
"depth" : 2
}
body verileri ile denendiğinde 200 çıktısı dönmesi sağlandı.
```
- 60966 [DR8323] - Web arayüzünde **eBA Bekleyen İşler menüsü** eklenerek ve CSP
    içerisinde **entegrasyon** sağlayarak, **eBA** içerisindeki **bekleyen süreçlerin**
    **görüntülenmesi** sağlandı.
- 55495 - Web arayüzünde **Kullanıcı** , **Pozisyon** , **Grup** , **Departman, Unvan nesneleri** için
    **pasif** ve **bakımı ayarlanmış Kullanıcıların** , **İnsan Kaynaklarında** yerine belirlenen
    **Kullanıcılar ile değişimi** sağlandı.
- 56603 - Geliştirme arayüzünde **Akış** tarafında **Akış Genel Özelliklerinde** bulunan
    **Variables** alanına eklenen **Public** değişkenlerin **ProcessVariables tablosunda**
    **kaydedilmesi** sağlandı.
- 60767 - Web arayüzünde **Doküman Yönetiminde Yeni Dosya** yüklenirken **Profil**
    **Formu** panelinde doldurulan **Form değerlerinin kaydedilmesi** ve dosyaların eklendiği
    **Datagrid üzerindeki filtrelerde düzenleme** yapıldı.
- 61621 - Geliştirme arayüzünde **Akış** tarafında **OnSession(Start,End,Error)Arguments**
    modellerinde **Context değerine erişim** sağlandı.
- 61970 - Geliştirme arayüzünde **FlowStart nesnesine OnAfterEvent** ve
    **OnBeforeEvent olaylarının eklenmesi** durumu geliştirildi.
- 55337 - Web arayüzü **Doküman Yönetiminde dosya içeriklerinde** bir dosya
    **düzenlenmek** istendiğinde **düzenleme işleminin yapılabilme özelliği** geliştirildi.
- 55757 - Web arayüzünde **FileSelector** nesnesinde **Seçili Dosya konumunun**
    **getirilmesi** geliştirildi.


- 60963 - Geliştirme arayüzünde **Service API CreateLink** endpointine **DocumentID**
    **bilgisinin gönderilmesi** ve **doldurulmuş formların düzenlenebilmesi** sağlandı.

```
POST {{webinterfacewebapiurl}}/Shared/CreateLink
{
"linkType": 5,
"payload":
"{\"ProjectName\":\"projectname1\",\"FormName\":\"formName1\",\"DocumentId
\":7}",
"embeddedView": true,
"language": "tr-TR",
"requestlimit": 100,
"scope": [
"sysfullaccess",
"webfullaccess",
"dmfullaccess",
"appsfullaccess",
"appsfullaccess",
"procmanfullaccess",
"web.announcement",
"web.announcement.read",
"webaccess",
"sysaccess",
"menufullaccess"
],
"userid": 1,
"Status": true,
"expiredate": null,
"viewHideInfo" : {
"hideLeftMenu":true,
"hideBreadcrumbNavigation":true,
"hideBreadcrumbItems":true,
"hideAppSearch":true,
"hideAdminTools":true,
"hideProfileMenu":true,
"hideApprovals":true,
"hideLastVisitedDocuments":true,
"hideAnnouncements":true
}
}
```

- 60406 - Geliştirme arayüzünde formda Scheduler nesnesinin Appearance başlığı
    altında First Day Of Week özelliği eklenmiştir.
- 60655 - Web arayüzünde **Giriş** ekranında **defaultLoginMethod** girişi **Configurations**
    içerisindeki **DefaultLoginMethod** değiştirildiğinde **Giriş** ekranının girilen **değere göre**
    **açılması** sağlandı.
    "digitalSignature","mobileSignature","usernamePassword","token","Azure
    AD","Google","LinkedId"
- 60656 - Web arayüzünde **İnsan Kaynakları** menüsünde **Yeni Kullanıcı** eklerken **Tarih**
    alanlarına **çarpı butonu** eklendi.
- 60811 - Web arayüzü **Doküman Yönetiminde Çalışma Başlat** denilip **İçerikler** alanına
    **açıklama eklenebilme** ve eklenen dosyaların **adlarının değişme özelliği** geliştirildi.
- 61128 - Web arayüzü **Doküman Yönetiminde Local Storage** alanına **CaptureEnable =**
    **true parametresi** eklenerek **Tara butonu modalı** geliştirildi.
- 34102 - Geliştirme arayüzünde **Datagrid Toolbar Button** ve **Action Button** tipindeki
    **Create A Form** ve **Start A Process** butonlarındaki **Project Name** ve **Form Name**
    **manuel olarak** yazılması yerine **mevcut projelerden seçilebilmesi** sağlandı.
- 53256 - Geliştirme arayüzünde **Scheduler** nesnesinin **dbType** seçimine göre **editType**
    düzenlemesi yapıldı. **DDL** isim alanına göre **dbType ColumnName** ve **entityPath**
    düzenlendi. **OnRowInserting** , **OnRowUptading** ve **OnRowRemoving Cancel**
    yapıldığında **Loading'de kalma problemi** düzeltildi. **Formatı olmayan DateTime** tipi
    için **Time** kısmının **gösterilmemesi** ve **Default Format eklenmesi** sağlandı.
    **Selectbox'da Datasource** seçildikten sonra **tekrar Datasource** seçim ekranına
    gelindiğinde **gösterilmeme hatası** düzeltildi. Geliştirme arayüzü tarafında **SelectBox**
    kolonu için **Datasource seçimi** ve Statik **öge ekleme Collapse'i görünmeme**
    **düzenlemesi** yapıldı.
- 61662 - Geliştirme arayüzünde **RelatedDocuments** nesnesinin **Advanced Edit**
    özelliğini **Aktif** ederek Web arayüzünde **RelatedDocuments** nesnesine eklenecek
    dosyalara **Görüntüle** dedikten sonra **Çalışma Başlat** butonuna basarak **versiyon**
    **başlatabilmesi** sağlandı.
- 61901 - Geliştirme arayüzünde **RelatedDocuments** nesnesinin **Behavior** başlığı
    altındaki **View Type** özelliğine " **Kutu Görünümü** " **özelliği** getirildi. Web arayüzünde
    **bar şeklinde gelen RelatedDocuments** nesnesinin sağdaki genişletici butonuna
    basıldığında **yüklenen dosyalar görülebilir** ve bu dosyalar üzerinde **Silme, İndirme** ,
    **Görüntüleme** ve **Açıklama girme gibi işlemler** yapılabilir.
- 62784 - Web arayüzü **Doküman Yönetiminde Üst menü** işlemlerinin **daha iyi bir**
    **performans verebilmesi için** geliştirme yapıldı.
- 43840 - Web arayüzünde **Onay** sırasında forma girilen **Aktivite mesajı Genel Aktivite**
    **ekranında görüntülenmeme özelliği** geliştirildi.
- 64547 - Web arayüzünde Doküman Yönetiminde **Depo** , **Klasör, Dosya sıkıştırılmış**
    **klasör olarak toplu indirme endpointi** geliştirildi.
- 62087 - **CSP Outlook Addon açılmama hatası** düzeltildi.


- 63981 - DataSource tipi **Aksiyon** olan **Datagrid'lerin** listelendiği **GetActionGrids**
    **endpointi** geliştirildi.

```
Örnek :
endpoint: https://dev.bimser.net/api/ide/ProjectManager/GetActionGrids
```
```
örnek request:
{
"projectName": "task63982_test",
"formName": "Form1"
}
```
```
Örnek response:
{
"result": {
"actionGrids": [
{
"id": "9609510f-cb4c-8d2e-e9fc-17693f696a3b",
"caption": "{\"tr-TR\":\"DataGrid2\"}",
"name": "DataGrid2",
"saveAction": "False"
},
{
"id": "cced0908- 9301 - a2b0- 7105 - 1a5dd33db862",
"caption": "{\"tr-TR\":\"DataGrid3\"}",
"name": "DataGrid3",
"saveAction": "False"
}
]
},
"success": true
}
```
- 62925 - Geliştirme arayüzünde **Datagrid** nesnesi **Boolean kolonu** özelliklerine
    **Default Value** seçeneği eklenerek, Default olarak **True ya da False olarak gelmesi**
    sağlandı.
- 62948 - Web arayüzünde **Dinamik ComboBox** nesnesinin belirlenen sorgudaki **dil**
    seçeneklerinin ortamın **diline göre değişerek nesneye yansıması** sağlandı.
- 63058 - Web arayüzünde formda **Label, Header** ve **FormMetaData** nesnelerini
    **textAlign özelliğinin olması** sağlandı.


- 63412 - Web arayüzünde formda **Signature** nesnesine **çizim** yaptıktan sonra **PDF'e**
    **Aktar** nesnesi kullanılan form, akışta devam ettirildikten sonra **Doküman**
    **yönetiminde PDF içerisinde imza gözükmeme hatası** düzeltildi.
- 63450 - Web arayüzünde formda **Signature nesnesine çizilen verinin** , akışa eklenen
    **PDF'e Aktar nesnesi** aracılığıyla **Doküman Yönetimi** içerisinde **belirtilen klasöre PDF**
    **dosyası olarak aktarılması** sağlandı.
- 63529 - Web arayüzünde **Vekalet yetkisi** verilmiş **Kullanıcının hesabı açıkken**
    **Vekalete ait olan hesaptan bir akış ilerletildiğinde** , diğer Kullanıcıya gelen
    " **Vekaleten onayınıza sunuldu** " bildirimine **tıklayıp sürecin açılamama düzenlemesi**
    yapıldı.
- 63689 [DR9967] - Web arayüzünde **DataGrid** nesnesine **kod ile kolon ekleme örneği**
    geliştirildi. Yapılan düzenleme
    ile **"CheckBox"** yerine **Controls.FormItemTypes.EControlTypes.CheckBox**
    kullanılmalı **addColumns metodu eklendi**. Aşağıdaki şekilde kullanılabilir.

```
Örnek kullanım:
this.DataGrid1.addColumns([
{
"caption": {
"tr-TR": "NewColumn2"
},
"width": "100",
"align": "left",
"wordWrapEnabled": false,
"sorting": {
"index": 0,
"order": "asc",
"enabled": true
},
"filtering": {
"operation": "contains",
"value": "",
"enabled": false
},
"editingEnabled": true,
"summaryTypes": [],
"summaryTypePrefixes": [],
"defaultValue": null,
"isPrimaryKey": false,
"isGeneratedColumn": false,
"visible": true,
"autoIncrement": false,
```

"disableToExport": false,
"precision": 0,
"useThousandSeparator": false,
"formula": null,
"format": null,
"culture": "",
"cultureMember": "",
"multiLanguagePath": "",
"multiLanguageLoadOptions": [],
"sourceFieldKey": null,
"dbType": {
"type": "decimal",
"columnName": "NewColumn2"
},
"editControl": {
"min": null,
"max": 99999999999999,
"step": 1,
"precision": 0,
"useThousandSeparator": false,
"sizeType": null,
"onlyNumber": false,
"value": null,
"placeholder": {},
"textAlign": "right",
"text": "",
"tabIndex": 0,
"EntityPath": "NewColumn2",
"readOnly": false,
"DefaultReadOnly": false,
"required": false,
"indexable": false,
"visible": true,
"clientVisible": true,
"enabled": true,
"DefaultEnabled": false,
"clientEnabled": true,
"DefaultClientEnabled": false,
"style": {
"padding": "",
"backgroundColor": "",
"backgroundImage": "",


"height": null,
"backgroundImageLayout": "none"
},
"containerStyle": {
"padding": "",
"backgroundColor": "",
"backgroundImage": "",
"height": null,
"backgroundImageLayout": "none"
},
"title": {},
"caption": {
"text": {},
"position": "left",
"size": {
"width": 120,
"height": null
},
"font": {
"family": "Source Sans Pro, sans-serif",
"size": "13",
"color": "#25241f",
"bold": false,
"italic": false,
"underline": false,
"strikethrough": false
},
"visible": true,
"ellipsis": true,
"horizontalAlign": "left",
"verticalAlign": "top",
"markSettings": {
"char": "",
"position": "atFirst",
"style": {
"padding": "",
"backgroundColor": "",
"backgroundImage": "",
"height": null,
"backgroundImageLayout": "none"
}
},


"showColon": false
},
"loading": false,
"customClassName": "",
"contextMenuKey": null,
"contextMenuTarget": "Container",
"controlId": null,
"name": null,
"controlType": "NumberBox",
"serverEvents": [],
"clientEvents": [],
"executedServerEvents": []
},
"formatType": {
"type": "label",
"format": ""
},
"editType": "numberBox",
"iconMatchers": [],
"iconSourceField": null,
"allowHiding": true,
"allowNull": true,
"headerFilterEnabled": false,
"style": {},
"showEditorAlways": false,
"hidingPriority": null,
"sourceType": "base64",
"enlargeOnClick": false,
"imageWidth": 100,
"defaultImage": null,
"sizeUnit": "pixels",
"imageType": "smallImage",
"preferredWidth": 0,
"checkUniqueValue": false,
"index": 0,
"name": "NewColumn2",
"summaryValue": {}
}
])


## 3. Fixes

### 3.1. Web Arayüzü

#### 3.1.1. Doküman Yönetimi

- 61089 - Web arayüzü **Doküman Yönetiminde Çöp Kutusu boşken hata verme**
    **sorunu** düzeltildi.
- 61111 - Web arayüzü **Doküman Yönetiminde Çöp Kutusunda otomatik silme**
    **düğmesinin kapatılmak** istendiğinde **meydana gelen hata** düzeltildi.
- 60765 - Web arayüzü **Doküman Yönetiminde** MetaData ile gelen **Tablo**
    **görünümünde Date tipinde filtre ekranının gelmeme** hatası düzeltildi.
- 61120 - Web arayüzü **Doküman Yönetiminde** panoda seçilen **dosyanın açılıp**
    **kapanma** hatası düzeltildi.
- 61151 - Web arayüzü **Doküman Yönetimi DateRangePicker** tipinde **MetaData**
    eklendiğinde **Invalid Date hatası** düzeltildi.
- 34751 - Web arayüzü **Doküman Yönetiminde Dizin** ayarlarındaki **Dosya Tipi** alanının
    **tıklanamadan sürekli açılıp kapanma hatas** ı düzeltildi.
- 53925 - Web arayüzü **Doküman Yönetiminde Depo ve Klasör Özelliklerindeki Dizin**
    ayarlarında **işlemci yapılandırması alanının boş gelme hatası** düzeltildi.
- 60953 - Web arayüzü **Doküman Yönetiminde yeni klasör** oluşturulurken **sayfanın**
    **yenilenme hatası** düzeltildi.
- 61221 - Web arayüzü **Doküman Yönetiminde Azerice** dilinde **uzun panel isminin**
    **titreme** hatası düzeltildi.
- 62182 - Web arayüzü **Doküman Yönetimi Tablo** görünümünde **dosya** ve **depo**
    **seçerken** meydana gelen **titreme hatası** düzeltildi.
- 52648 [DR8745] - Web arayüzü **Doküman Yönetiminde dosya yükleme yetkisi**
    **olmayan** kullanıcıda sürükleyerek **dosya yükleme hatası** ve yetkili **kullanıcı depo**
    **oluşturmak istendiğinde anlaşılır olmayan hata mesajı** düzeltildi.
- 53700 - Web arayüzü **Doküman Yönetiminde dosya yükleme yetkisi olmayan**
    kullanıcıda sürükleyerek **dosya yükleme hatası** ve yetkili **kullanıcı depo oluşturmak**
    **istendiğinde anlaşılır olmayan hata mesajı** düzeltildi.
- 61093 - Web arayüzü **Doküman Yönetiminde yeni depo** oluştururken meydana gelen
    butondaki **Loading icon hatası** düzeltildi.
- 64254 - Web arayüzünde **Doküman Yönetiminde** Depo veya Dosyanın içerisinde
    bulunan **Excel** dosyaları **kısayol** oluşturulup **panoya eklenip farklı bir yere**
    **taşındığında** , **açılmama** hatası düzeltildi.
- 64898 - Web arayüzü **Doküman Yönetiminde** bir depoya sağ tıklayıp **Özellikler**
    **sekmesine basınca** alınan hata düzeltildi.
- 56474 – Web arayüzünde **Doküman Yönetiminde Document transfer** uygulamasında
    **hatalı MetaData** parametresiyle ile **dosya yüklenmek** istendiğinde, **hata mesajının**
    **gelmeme durumu** düzeltildi.


- 56491 - Web arayüzünde **Doküman Yönetiminde Document Transfer** uygulamasında
    klasörde **MetaData** ile proje seçilen senaryoda uygulamada **dosya yüklendi**
    **gözükmesine** rağmen **dosyaların ortama yüklenmeme hatası** düzeltildi.
- 19424 - Web arayüzü **Doküman Yönetiminde Klasör Özellikleri** içerisinde **MetaData**
    **Form zorunluluğu** olan formlarda **birden fazla dokümanın eklenememe** hatası
    düzeltildi.
- 53953 - Web arayüzünde **Doküman Yönetiminde** depoya girilip **dosya seçildiğinde**
    atılan **aşırı istek atma hatası** düzeltildi.
- 55867 [DR9148] - Web arayüzü **Doküman Yönetiminde PDF Viewer’daki** yazıların
    **görünmeme** hatası düzeltildi.
- 61680 - Web arayüzü **Doküman Yönetiminde Profil formda** , Datasource bağlanan
    nesnelerin **Tablo** görünümünde **ID olarak görünmesi sorunu** düzeltildi.
- 39766 - Web arayüzünde **Doküman Yönetiminde Text dosyasına** karşılaştırma
    dendiğinde **dosya görüntülenememe sorunu** düzeltildi.
- 55575 - Web arayüzünde **Doküman Yönetiminde Profil form** ile birlikte klasör
    oluşturulurken meydana gelen **Max CallSized hatası** düzeltildi.
- 63089 - Web arayüzü **Doküman Yönetiminde Arama girişine** tıklandıktan sonra
    **kapanmama** hatası düzeltildi.
- 64262 - Web arayüzü **Doküman Yönetiminde masaüstünde aç** ikonunun
    **diğerlerinden büyük olma** hatası düzeltildi.
- 65148 - Web arayüzü **Doküman Yönetiminde Masaüstünde Aç** özelliği kullanımı
    sonrasında **yaşanan sistem kilitlenmesi hatası** düzeltildi.
- 65657 - Web arayüzü **Doküman Yönetiminde Yazdırılabilir Görüntüleyici** tipi seçimi
    sonrası **Yazdır butonunun pasif olma sorunu** düzeltildi.
- 65661 - Web arayüzünde **Statik Datagrid'de** yapılan **Düzenleme** işleminin **satıra**
    **yansımama hatası** düzeltildi.
- 65734 - Web arayüzünde **Process Arşivlere** eklenen **Header Filter Enabled** özelliğinin
    **çalışmama hatası** düzeltildi.


#### 3.1.2. İş Akış Yönetimi....................................................................................................................

- 56390 - Web arayüzünde **Digital Signature Required** ve **Fast approval** özelliği **Aktif**
    edilen butonda **İş Akış Yönetiminde tıklandığında hata vermesi** sorunu düzeltildi.
- 56410 [DR9195] - Web arayüzünde formdaki nesneye yazılan uzun karakterli verinin
    **İş Akış Yönetiminde** ve **Dashboard'da süreç bilgileri kısmında tamamının**
    **gözükmeme** hatası düzeltildi.
- 56381 - Web arayüzünde **İş Akış Yönetiminde Fast Approval** ve **Validate** özelliği **Aktif**
    **butonda zorunlu alan mesajının gösterilmeme** hatası düzeltildi.
- 61164 - Web arayüzünde **Güvenlik** kısmında **İzinler** menü butonlarının **monitör**
    **ekranının büyüklüğüne ya da küçüklüğüne göre görünmeme** hatası düzeltildi.
- 61192 - Web arayüzünde **İş Akış Yönetimi** menüsü **Taslaklar** sekmesinde **Sil**
    **butonunun gözükmeme hatası** düzeltildi.
- 64404 - Web arayüzünde **DataGrid** nesnesine **Dinamik kolon eklenebilmesi** sağlandı.
    Mevcut kolonlar **Entity** üzerinden doğrulanarak, sadece **db/entity mevcut olanlar**
    **işleme dahil edilmesi** sağlandı.


#### 3.1.3. İnsan Kaynakları

- 59751 - Web arayüzünde **İnsan Kaynakları** panelindeki **"Unvan" yazım hatası**
    **"Ünvan" olarak** düzeltildi.
- 56248 - Web arayüzünde **İnsan Kaynakları Kullanıcı Grubu** menüsünde **Yeni Kullanıcı**
    **Grubu** açıldığında **üç panel yan yanayken Kullanıcı Grubu başlığının yarım gözükme**
    hatası düzeltildi.
- 61031 - Web arayüzünde **İnsan Kaynakları Şirketler** filtresinde **iki filtre denendiğinde**
    **alınan konsol hatası** düzeltildi.
- 61053 - Web arayüzünde **İnsan Kaynakları** menüsünde **Yeni Vardiya** ve **Mesai**
    eklerken **MultiLanguage kolonundaki hiza sorunu** düzeltildi.
- 61018 - Web arayüzünde **İnsan Kaynakları** menüsü **Pozisyonlar** panelinde **Yeni**
    **kullanıcı** eklerken kullanıcı seçimi alanında **Placeholder hatası** düzeltildi.
- 61024 - Web arayüzünde, **İnsan Kaynakları** menülerinde **Yeni Kullanıcı / Pozisyon**
    gibi alanlarda formu doldurup **Kaydet** butonuna tıklandığında, **hem başarılı** hem de
    **kaydedilmedi** şeklinde **iki adet uyarı çıkma hatası** düzeltildi.
- 61059 - Web arayüzünde **İnsan Kaynakları** paneli **Organizasyon Bakımı** sekmesinde
    **Datagrid'deki Sil butonunun Pasif gelme** hatası düzeltildi.
- 63208 - Web arayüzünde **İnsan Kaynakları Özellik Tanımları** panelinde **List** tipinde
    **Ekle butonunun görünüm sorunu** düzeltildi.
- 64457 [DR10153] - Web arayüzünde **İnsan Kaynaklarında Kullanıcılar** panelinde bir
    Kullanıcıyı açtığımızda **amirler kısmının boş gelme hatası** düzeltildi.
- 64458 [DR10154] - Web arayüzünde **İnsan Kaynaklarında Kullanıcılar** panelinde bir
    kullanıcının **amiri değiştirilmek istendiğinde hata verme durumu** düzeltildi.


#### 3.1.4. Web Ana Sayfa

- 53618 - Web arayüzünde akışta **imzalanan dokümanların farklı süreçlerde tekrar**
    **tekrar imzalanamama hatası PDF'e Aktar nesnesiyle** birlikte düzeltildi.
- 56405 [DR9255] - Web arayüzünde **Binlik Ayraç** özelliği **seçili NumberBox** nesnesi
    **PDF'e Aktar** özelliği ile aktarıldığında **Binlik Ayraç özelliği olmadan aktarılma hatası**
    düzeltildi.
- 53074 - Web arayüzünde **CSP eBA Entegrasyonu** için menüye eklenmiş **eBA 6.**
    **versiyonu bağlantısına tıklandığında açılmama** hatası düzeltildi.
- 45417 [DR6767] - Web arayüzünde **Pozisyon Grubu** nesnesinde kullanıcı olmadığında
    **ProcessRequestDocuments tablosuna kayıt atılmama hatası** düzeltildi.
- 50600 - Web arayüzünde **Görünüm formu** olarak açtığımız formu **Kaydet**
    dediğimizde **hata vermesinden kaynaklı Kaydet butonu kaldırılarak hata** düzeltildi.
- 50277 - Web arayüzünde formda **FishBone** nesnesinin **Problem başlık kısmının boş**
    **gelme hatası** düzeltildi.
- 60354 [DR9458] - Web arayüzünde **Pozisyon Grubu** nesnesi **boşken raporda**
    **gözükmeme hatası** düzeltildi.
- 56139 - Web arayüzünde **NumberBox** nesnesinin **value** değerinin, nesne **Enabled** ve
    **Client Enabled yapıldığında gözükmeme hatası** düzeltildi.
- 56204 - Web arayüzünde **süreç verilerinin açılmama hatası** düzeltildi.
- 60329 - Web arayüzünde form ekranında **Akış Tarihçesi boş olduğunda proje adı**
    yerine **Akış adının yazma hatası** düzeltildi.
- 26707 - Web arayüzünde **Process Arşiv Datagrid'lerde kayıt bulanamadı mesajı**
    düzeltildi.
- 48157 - Web arayüzünde **Datagrid** nesnesi **DateTime kolonunun filtre hataları**
    düzeltildi.
- 50402 - Web arayüzündeki **Uygulama Gezgini menüsünde sıralama hatası** düzeltildi.
- 51735 - Web arayüzünde **Profil** butonunun altındaki **Başkası Adına Oturum Açma**
    modalındaki **Kullanıcı seçim** listesinde Pasif kullanıcılar ile **Oturumu açık** olan
    **kullanıcıların listelenme hatası** düzeltildi.
- 52106 - Web arayüzünde **Datagrid** nesnesi **Primarykey** kolonlarının **Düzenle**
    **modunda aktif gelme hatası** düzeltildi.
- 53101 - Web arayüzünde **Datagrid Boolean kolonu** filtrelerindeki **"evet"** ve **"hayır"**
    kelimeleri **"Evet", "Hayır" olarak değiştirilerek** hata düzeltildi.
- 53933 - Web arayüzünde **Dashboard’da son kullanılan uygulamaların ikonlarının**
    **gelmeme** hatası düzeltildi.
- 54694 - Web arayüzünde **TimePicker** nesnesi **Use 12 Hours özelliği açıkken** , açılan
    panelde **ÖÖ** ve **ÖS** diye gözükürken nesne üzerinde **Am, Pm olarak gözükme hatası**
    düzeltildi.
- 56203 - Web arayüzünde **Hesabım** kısmında **Başkası Adına Oturum Aç** panelinde
    kullanıcı seçmeden **Giriş butonuna tıklanıldığında panelin kapanma hatası** düzeltildi.


- 61665 - Web arayüzünde **Repeater** nesnesinin içindeki **formdan seçim yapınca**
    **hemen yansımama** ve **sonraki tıklamadan sonra seçilen verinin gelme hatası**
    düzeltildi.
- 59850 - Web arayüzünde **Dashboard'da Süreçler ekranındaki görünüm hatası**
    düzeltildi.
- 61757 - Web arayüzünde **Datagrid** nesnesi **DataType: Decimal EditType ComboBox**
    olan kolondaki veri **Allow Clear** ile **silince alınan konsol hatası** düzeltildi.
- 59984 - Web arayüzünde form ekranında **Lookup nesnesinde seçim yapıldığında**
    **oluşan hata** düzeltildi.
- 55667 [DR9141] - Web arayüzünde **Parametreli forma** eklenen **İlişkili Datagrid'den**
    **Düzenleme** modunda açılan form kaydedildiğinde " **Akış başarıyla kaydedildi** " hatası
    giderilerek " **Form başarıyla kaydedildi** " şeklinde düzenlendi.
- 56391 [DR9214] - Web arayüzünde **SearchBox** nesnesinin olduğu formda **TabIndex**
    **özelliğinin doğru çalışmama hatası** düzeltildi.
- 60140 - Web arayüzünde **Duyurular** Datagrid'inde " **Tarih kolonu** " başlığı " **Oluşturan**
    **Tarih** " olarak değiştirildi.
- 60242 - Web arayüzü **Aktivitelerde @ ile seçim yapılırken sayfanın hataya düşmesi**
    durumu düzeltildi.
- 60294 - Web arayüzünde **Duyuru** eklenirken **Multilanguage** alanına veri yazılıp
    **Türkçe** konu alanı **boş** bırakıldığında **Kaydet** butonunun **Aktif gelme hatası** düzeltildi.
- 60672 - Web arayüzünde **Güvenlik** yetkilerinde **Çeviri** özelliğine **izin verilmediği**
    senaryoda Geliştirme arayüzünde **Otomatik Çevir butonunun görünme hatası**
    düzeltildi.
- 60691 - Web arayüzünde **Modal** görünümü **açık bir nesne varken** proje **deploy**
    alındığında, " **Projenin yeni versiyonu yayınlandı** " uyarısına basıldıktan sonra Modalın
    açık kalma hatası düzeltildi.
- 61011 - Web arayüzünde **Akış** onaya gönderildikten sonra **Akış Tarihçesi ekranı**
    **açılıyor** menüsünden **aynı sürece tıklandığında açılmama** hatası düzeltildi.
- 61062 - Web arayüzünde **DocumentViewer** nesnesinde **Modal** ve **Drawer**
    özelliklerindeki açılan panelde **üst kısımdaki ikonların hizasız durma hatası** düzeldi.
- 43612 - Web arayüzünde **Datagrid’de** yer alan **Select** kolonu seçimleri birden fazla
    denemeden sonra **Panel açılıp kapanma hatası** düzeltildi.
- 49294 [DR7871] - Web arayüzünde **1366x768 çözünürlüğündeki** bilgisayarlarda
    formda bulunan **Lookup** nesnesinin içerisindeki **sorguların gözükmeme hatası**
    düzeltildi.
- 50362 - Web arayüzünde **FileSelector** nesnesinden **dosya seçimi** yapıldığında
    **nesneye gelmeme hatası** düzeltildi.
- 59677 - Web arayüzünde formda **Statik Scheduler** nesnesinde veri girmek için
    hücreye tıklandığında **Bitiş tarihi** için **saat** belirlediğimizde, **belirlenen saatin dışına**
    **taşarak ilerleme hatası** düzeltildi.


- 59757 [DR9326] - Web arayüzünde **Scheduler** nesnesinin **Client** kısmının
    **onRowInserting** etkinliğinde başlığa atanan değer, **belirlenen kelimenin** girilmesine
    rağmen **gözükmeme hatası** düzeltildi.
- 59759 [DR9323] - Web arayüzünde **Scheduler** nesnesinin **Client** kısmında
    **OnRowInserting** etkinliğinde belirlenen kelimenin girilmesinden sonra **nesnenin**
    **donup üzerinde hiçbir işlem gerçekleştirememe hatası** düzeltildi.
- 61604 - Web arayüzünde **DataGrid** nesnesi olan formlarda belirli bir süre sonra **Scroll**
    **hareketi yapamama hatası** düzeltildi.
- 51450 - Web arayüzünde **Akış Tarihçesinde Lokasyon bilgisinin gözükmeme hatası**
    düzeltildi.
- 60638 - Web arayüzünde **Fast Approval** ve form seçimi yapılmış olan butona
    tıklandığında **olay formunun açılmama hatası** düzeltildi.
- 52884 - Web arayüzünde **Görev Yönetiminde Kullanıcı** üzerindeki **görevlerin**
    **listelenmeme** hatası düzeltildi.
- 53944 - Web arayüzü **Giriş** sayfasında **Mobil İmza** seçildikten sonra **sayfanın hataya**
    **düşme sorunu** düzeltildi.
- 61007 - Web arayüzünde akış ilerletilirken **Akış** mesajının **gelmeme hatası Akış**
    **Başlangıcı nesnesine** ve **Akış Bitişi nesnesine Web notification mesajları eklenerek**
    düzeltildi.
- 61013 - Web arayüzünde **bir form açıkken bildirim** ile gelen forma tıklandığında bu
    **iki formun yan yana açılabilme hatası** düzeltildi.
- 61080 - Web arayüzünde **Uygulama Gezgininde** önce var olan bir **Menü Düzenle**
    modunda açıldıktan sonra o kapatılıp **Yeni Menü Ekle'ye** tıklandığında **Düzenle**
    panelinde **açılan bilgiler gelme hatası** düzeltildi.
- 61220 - Web arayüzünde formda **Dinamik Datagrid** nesnesinde **Düzenleme**
    yapılırken **ilk veri girildikten sonra Inputtan atma hatası** düzeltildi.
- 61224 [DR9558] - Web arayüzünde **ProcessRequest** tipinde açılan **paylaşım**
    **linklerinde Dashboard ekranının açılma** hatası düzeltildi.
- 60896 [DR6055] - Web arayüzünde **User Custom Property null** olduğunda **Kaydetme**
    **işlemindeki hata** düzeltildi.
- 61496 - Web arayüzünde formda **Parametre** alan **RadioList** nesnesinin **arama barına**
    **veri yazarken girilen verinin silinme hatası** düzeltildi.
- 61500 - Web arayüzünde form ekranında **Dinamik Datasource** bağlantısı olan **ListBox**
    ve **Dropdown** nesnelerinin **form açıldığında yükleniyor olarak kalma hatası**
    düzeltildi.
- 61528 - Web arayüzünde form ekranında **ListBox** nesnesinde **arama** işleminde
    **yükleniyor olarak kalma hatası** düzeltildi.
- 62626 - Web arayüzünde **ilk defa onaya gelen form kaydedildiğinde Doküman No**
    **bilgisinin 0 olarak gözükme sorunu** düzeltildi.
- 62702 - Web arayüzünde **Fast Approval** ve **Visible False** özelliğine sahip olan
    butonun **süreç detaylarında gözükme hatası** düzeltildi.


- 61026 - Web arayüzü **Uygulamalar** menüsünde **uzun isimli menülerde** oluşan
    **görünüm hatası odak noktası** düzeltildi.
- 61331 [DR9610] - Web arayüzünde dil **İngilizce** seçili iken **yanlış bilgilerle giriş**
    **yapılmak** istendiğinde gelen uyarı bildirimi **Details** yerine **Credentials** olarak
    değiştirildi. Web arayüzünde **İnsan Kaynakları** kısmında **Vardiya** panelinden **Yeni**
    **Vardiya** penceresindeki **Time zone yazısı** düzeltildi. Geliştirme arayüzünde **Proje**
    **Yöneticisi** içerisinde **Form Indexle** panelinin **Kaydet** butonu ortam dili **İngilizce**
    olduğunda **Save** olarak değiştirildi.
- 61376 - Web arayüzünde form ekranında **Parametre** alan **Lookup** nesnesinde **veri**
    **olduğu halde veri yok mesajının gösterilme hatası** düzeltildi.
- 61553 - Web arayüzünde **Bekleyen İşler** alanından gönderilen akışta, **Akış Tarihçesi**
    **ekranı** geldiğinde oluşan **panelType hatası** düzeltildi.
- 62064 [DR9702] - Web arayüzünde, **İlişkili Datagrid** nesnesi içeren **Save on: Row**
    **Change** özelliği olan **Parametrik formu** menüden açmaya çalıştığımızda, verilerin
    gelmesi **60 saniyeden uzun sürdüğü için Timeout'a düşme hatası** düzeltildi.
- 63453 - Web arayüzünde **Row Change** özelliği açık olan **Datagrid'lerde Insert Row**
    **endpointinin iki kere tetiklenme hatası** düzeltildi.
- 62379 - Web arayüzünde **Görev Yönetiminde Olaylar bilgisinin gözükme hatası**
    düzeltildi.
- 62395 - Web arayüzünde **Fast Approval Dijital İmza** özelliğine sahip butonda,
    **Bekleyen İşler** alanından butona tıklanıp **modal** kapatıldığında **Dijital İmza** işlemi
    **başarısız mesajının gözükmeme hatası** düzeltildi.
- 62810 - Web arayüzünde **Horizontal** seçimli **ListBox** nesnesinin **Ellipsis** özelliğinde
    **uzun olan Text verilerinin yarım kalma hatası** düzeltildi.
- 62843 - **Csp Outlook Addon açılmama hatası** giderildi.
- 48405 - Web arayüzünde **E-İmza'nın Debian işletim sisteminde çalışmama hatası**
    düzeltildi.
- 34309 - Web arayüzünde **Dashboard** ekranında **arama** alanında **Uygulama**
    **Gezgininde olan verinin gelmeme hatası** düzeltildi.
- 35414 - Web arayüzünde **Duyurular Datagrid'indeki Konu kolonu filtre hataları**
    düzeltildi.
- 50403 - Web arayüzünde **Vekalet ve Erişim Anahtarları** panelinden oluşturulan bir
    vekaletin **Düzenle** ile **Bitiş süresi** değiştirildiğinde, **açık olan Vekalet sayfasının**
    **oturumuna yansımama** hatası düzeltildi.
- 45074 - Web arayüzünde **Yönetim Araçları** başlığı altındaki **Güvenlik Ayarlarında** bir
    **Yetki Grubuna** dahil edilen **Kullanıcı Grubu** daha sonra silindiğinde hala **yetkileri**
    **kısıtlanmış gibi kalma hataları** düzeltildi.
- 51184 - Web arayüzünde **Yönetim Araçları Güvenlik Ayarları** kısmında **Duyurular**
    paneli **devre dışı** bırakılmış üyeler için hem Kullanıcı adı ile hem de Anahtar ile
    ortama **girişte Anasayfa'da görünür olma hatası** düzeltildi.


- 63763 - Web arayüzünde **Menü Ekle** panelinden **eBA Entegrasyonu** seçeneğinde
    **Gelişmiş Parametre** içerisine yazılan **ebaVersion 6.4 verisi Kaydet** dedikten sonra
    tekrar girip bakıldığında **kaydedilmeme hatası** düzeltildi.
- 18258 - Web arayüzünde **Select Metadata Type** özelliği **"Custom"** ve **Custom**
    **Metadata Field Name** özelliği **"List"** olarak seçili bir **UserMetaData** nesnesi formda
    açıldığında eğer **ortam dili İngilizce ise nesne içerisindeki verinin gözükmeme hatası**
    düzeltildi.
- 54964 - Web arayüzü **Giriş** ekranında **GetClarifications endpointinin 500 dönme**
    **hatası** düzeltildi.
- 63255 - Web arayüzünde **Bekleyen İşler** ve **Ana sayfadaki Süreç detaylarında**
    Oluşturan, **Başlangıç** , **İstek numarası** gibi bilgilerin **karışık halde gelme hatası**
    düzeltildi.
- 64088 [DR10077] - **Database** ortamında **RelatedDocuments OCRDATA özelliği** ve
    **Datagrid CELLDATA** kolonları olmasa dahi Web arayüzünden veri eklendiği takdirde
    bu kolonların **Database ortamında oluşmama hatası** düzeltildi.
- 64172 [DR10097] - Web arayüzünde **Form** ekranında **Lookup nesnesinde oluşan**
    **yavaşlık sorunu** düzeltildi.
- 64641 [DR10193] - Web arayüzünde **Archive** ve **Process Arşivi** oluşturulan
    formlardaki **nesnelerin verilerinin yansımama hatası** düzeltildi.
- 50479 - Web arayüzünde **TreeList** nesnesinde **verilerin yansımama hatası** düzeltildi.
- 52488 - Web arayüzünde **Dashboard** ekranında **Son Kullanılan Dokümanlarda**
    **Tümünü Göster** dediğimizde açılan **ekranın boş gelmesi sorunu** düzeltildi.
- 39671 - Web arayüzünde form ekranında **Lookup** nesnesinde **Tarih** filtresinde **daha**
    **küçük** veya **eşit filtresinin çalışmama hatası** düzeltildi.
- 51412 [DR8371] - Web arayüzünde **DateRangePicker** nesnesinde **saat seçilmediği**
    halde **Datagrid'de saatli olarak eklenme hatası** düzeltildi.
- 62705 - Web arayüzünde **Süreç** detaylarından ilerletilen akışta, akışın ilerleyeceği
    kullanıcıda da **aynı projenin süreç detayları açık olduğunda oluşan hata** düzeltildi.
- 62567 - Web arayüzünde **Dijital İmza** ekranı açıldığında **Konsol’da**
    **CustomElementRegistry pin-code verme hatası** düzeltildi.
- 62704 [DR9843] - Web arayüzünde **Client** tarafından bazı sekmeleri **false** yapılan
    **Tabs** nesnesinin, **sekmelerinin formda gözükme hatası** düzeltildi.
- 62796 - Web arayüzünde **konsoldan cash veri temizlendikten sonra ortam dilinin**
    **İngilizceye dönme** ve **Hesabım** menüsündeki **dil sekmesinin Türkçe olarak gözükme**
    hatası düzeltildi.
- 63184 - Web arayüzünde **Akış Özelliklerinde** nesne **proje ismi uzun olduğunda**
    eklenen nesnelerdeki **verilerin üst üste gözükme hatası** düzeltildi.
- 63612 [DR9978] - Web arayüzünde **Treeview** nesnesinde **Title** kısmına **boşluklu** bir
    yazı girildiğinde **formda boşluksuz şekilde gelme hatası** düzeltildi.
- 63989 - Web arayüzünde **RelatedDocuments** nesnesine dosya yükleyip **Görüntüle**
    dediğimizde **ortamın hata verme sorunu** düzeltildi.


- 64085 [DR10088] - Web arayüzünde **DataSource** ile **Field Selection** parametre
    verilen Datagrid'de **Sayfalandırma ve Arama kısmının çalışmama hatası** düzeltildi.
- 64149 - Web arayüzünde **Lookup** nesnesinden yapılan seçimlerin **nesne satırlarında**
    **görünmeme** hatası düzeltildi.
- 64151 - Web arayüzünde **Lookup** nesnesinden yapılan seçimlerin **kaldırılsa** bile
    **nesnede kalma hatası** düzeltildi.
- 64237 - Web arayüzünde **Vekalet ve Erişim Anahtarları** panelinin **Kullanıcı Ayarları**
    bölümünde **Aktif Vekaletlerin iptali** için kullanılan " **Geri Çek** " **butonunun çalışmama**
    hatası düzeltildi.
- 64252 - Web arayüzünde **Datagrid Boolean** kolonunda **Show Editor Always** özelliği
    açıkken yapılan **değişikliklerin alt kolonlara etki etmeme hatası** düzeltildi.
- 64439 - Web arayüzünde **Duyurular** sayfasında **Duyuru Formu** editörde
    **MultiLanguage butonunun görünmeme** sorunu düzeltildi.
- 64446 - Web arayüzünde **Lookup** nesnesinde yapılan seçim sonrası sayfa
    değiştirildiğinde, **seçimlerin görünmeme hatası** düzeltildi.
- 64500 [DR10162] - Web arayüzünde **Tarayıcı dili farklı olduğunda Onaylar** açılırken
    alınan **localeCompare is not a function hatası** düzeltildi.
- 64543 - Web arayüzünde **Datagrid** nesnesi **Select tipli** kolondaki verilerin **form**
    **açıldığında yüklenmeme hatası** düzeltildi.
- 64600 - Web arayüzünde **Index Raporu sayfası açılırken alınan hata** düzeltildi.
- 64621 - Web arayüzünde içerisinde **boş bir DataSynchronizer** nesnesi olan bir form
    açılacağı zaman **ortamın hata verme durumu** düzeltildi.
- 64635 [DR10191] - Web arayüzünde **Fast Approval** özelliğine sahip butonda formda
    doldurulması gereken alan yokken **zorunluluk uyarılarının gelme hatası** düzeltildi.
- 64864 - Web arayüzünde **eklenmiş nesnelerin Mirror karşılıklarının gözükmeme**
    hatası düzeltildi.
- 64899 - Web arayüzünde **Datagrid** nesnesi **CheckBox** kolonundan yapılan ilk
    seçimden sonra yapılan **seçimlerin Proxy olarak gelme hatası** düzeltildi.
- 65068 - Web arayüzünde **Datagrid'deki satırların silinmeme hatası** düzeltildi. Toplu
    silmek için **deleteRows methodu** eklendi. **Primarykey** alanının **value** değerini **Array**
    şeklinde vererek **silme işlemi gerçekleştirilmesi** sağlandı.
- 65341 - Web arayüzünde **akışın yanlış ilerleme hatası** düzeltildi.
- 65381 - Web arayüzünde **Karşılama** ekranındaki **Loading sorunu** ve **kullanıcı adının**
    **görünmeme sorunu** düzeltildi.
- 65392 - Web arayüzü **Dashboard'da süreçlerde Akış Tarihçesine tıklayınca** alınan
    hata düzeltildi.
- 65433 - **CSP Outlook Addon'da İş Akış Yönetimi Bekleyen İşler'den** açılan formdaki
    **Lookup** nesnesine **verinin yansımama** hatası, **CSP Outlook Addon'da İş Akış**
    **Yönetimi** Taslaklardan açılan formdaki **Statik ve Dinamik** nesnelerde **veri seçilmeme**
    hatası ve **CSP Outlook Addon'da** formdaki **UserMetaData** nesnelerine **veri gelmeme**
    **hatası** düzeltildi.


- 65874 - Web arayüzünde **Datagrid** nesnesinde **Cell** tipindeyken **10'dan fazla kolon**
    olduğunda **yatay scroll hareketinin yapılamama** hatası düzeltildi.
- 65901 - Web arayüzünde **Süreç detaylarından hızlı onay butonu** ile **ilerletilmek**
    **istenilen sürecin ilerlememe hatası** düzeltildi.


### 3.2. Geliştirme Arayüzü

- 61112 - Geliştirme arayüzünde **Aksiyon Durum Yöneticisindeki yazım yanlışları**
    düzeltildi.
- 61267 - Geliştirme arayüzünde **Bağlantıları Düzenle** işleminde kaydedilen bağlantının
    **bağlantı metinindeki şifre bilgisinin [Password] şeklinde olması** sağlandı.
- 61324 - Geliştirme arayüzünde **Akış** tarafında **Aksiyon Oluşturucu** nesnesinde **aynı**
    **Sınıf bilgilerinin birden fazla gelme sorunu** düzeltildi.
- 61344 - Geliştirme arayüzünde **Deploy** işleminde **Form Validation Warning mesajı**
    **anlamlı hale** getirildi.
- 61492 - Geliştirme arayüzünde, **Aksiyon Formu** olan projelerdeki **Deploy hatası**
    **Database** tarafında sorun oluşturan **Datagrid'in ACTIONID kolonu için int to**
    **decimal(19,5) tipine çevrilerek hata** düzeltildi.
- 62041 - Geliştirme arayüzünde **Datasource** sorgusunda **ExecuteNonQuery**
    **ExecuteScalar** çalıştırma tiplerinde, **Array tipli Parametre** kullanıldığında oluşan hata
    düzeltildi.
- 36576 - Geliştirme arayüzünde **ortam dili İngilizce** yapıldığında **menü başlıklarının**
    hala **Türkçe olarak kalma hatası** düzeltildi.
- 37294 - Geliştirme arayüzünde **Bağlantılar** işleminde **Düzenle** ekranında boş bırakılan
    alanlarda **Kaydetme** işlemi yapılırken çıkan **bilgilendirme mesajının tam olarak**
    **gözükmeme sorunu** düzeltildi.
- 48318 - Geliştirme arayüzünde **Pozisyon** ve **Pozisyon Grubu** nesnelerindeki **Flow**
    **Control** özelliğinde **butonların ID olarak gözükme sorunu** düzeltildi.
- 51992 - Geliştirme arayüzünde **nesnenin üzerine tıklayınca açılan ContextMenu** ,
    **başka nesnenin üzerine denk gelindiğinde tıklanmama hatası** düzeltildi.
- 54725 - Geliştirme arayüzünde **TreeList** nesnesinden kullanım açısından **Type**
    **seçeneği kısmında İlişkili ve Aksiyon kısımları** kaldırıldı.
- 55562 [DR9129] - Geliştirme arayüzünde **Datagrid Boolean** kolonlarında **Allow Null**
    **seçeneği kaldırılarak** hata düzeltildi.
- 56389 [DR9215] - Geliştirme arayüzünde **Datasource** sorgusunda **kolon başlığı**
    **değiştirilip sorgu çalıştırıldığında** , **başlığın eski haline gelme** hatası düzeltildi.
- 56697 - Geliştirme arayüzünde **Scheduler Service basit tetikleyicide Enable Between**
    **seçimi anında oluşan hata** düzeltildi.
- 60061 - Geliştirme arayüzünde **form ekranında Görünümü Düzenle** işlemindeki hata
    düzeltildi.
- 60192 - Geliştirme arayüzünde **Yeni Boş Proje** oluştururken **Ad** alanına **uzun veri**
    **girildiği zaman alınan hata** düzeltildi.
- 60196 - Geliştirme arayüzünde **Başlangıç** ekranında **Yeni Boş Proje** oluştururken
    **Başlık** kısmındaki **MultiLanguage ikonuna** tıklayınca **Azeri seçeneği bulunmama**
    hatası düzeltildi.


- 60202 - Geliştirme arayüzünde **Yeni Proje Oluştur** dedikten sonra **Klasör Seç**
    panelinde içine girilen klasörün **sayfa sayısının olduğundan fazla gözükme hatası**
    düzeltildi.
- 60216 - Geliştirme arayüzünde **Yeni Boş Çözüm** oluşturulmak istenirken **Başlık**
    kısmında **MultiLanguage** özelliğinde **Azerbaycan dil seçeneğinin bulunmama** hatası
    düzeltildi.
- 60229 [DR9392] - Geliştirme arayüzünde **Toolbar Button'dan** görünümde başka bir
    görünüm seçilip Web arayüzünde **Print** butonuna basıldığında **seçilen görünümün**
    **gelmeme hatası** düzeltildi.
- 61152 - Geliştirme arayüzünde **Özellik Görüntüleyici** ekranında **İ harfi aramasının**
    **yapılmama hatası** düzeltildi.
- 44813 - Geliştirme arayüzünde **Datagrid** nesnesi **Hidden Row Column Name(string)**
    seçilip **Hidden Row Value Matchers** veri yazılıp **form kaydedilmek** istendiğinde
    verilen **konsol hatası** düzeltildi.
- 50523 - Geliştirme arayüzünde **Akış** tarafında yeni oluşturulan akışta, **Akış Başlangıcı**
    nesnesinde **Documents** içerisinde **görünüm bilgisinin gözükmeme** hatası düzeltildi.
- 50601 - Geliştirme arayüzünde **Akış** kısmı açıldığında gelen **Araç Kutusu** , forma
    geçtikten sonra **form üzerindeki nesnelere tıklasak bile gitmeme** hatası düzeltildi.
- 50825 - Geliştirme arayüzünde **Akış** tarafında **Flow Events** alanından **Seçerek Kaldır**
    işlemi yapıldığında, **buton bilgilerinin silinip akış linklerinin silinmeme** hatası
    düzeltildi.
- 52307 - Geliştirme arayüzünde **Akış** özelliklerinde **Confirmation Checkbox'ında Aktif**
    **- Pasif etme** senaryosundaki hata düzeltildi.
- 49785 - Geliştirme arayüzünde **Akış Durumu nesnesinde default name hatası**
    düzeltildi.
- 54231 - Geliştirme arayüzünde formun **Yerelleştirme** panelindeki **Datagrid'e Hepsini**
    **Temizle butonu eklenerek hata** düzeltildi.
- 54254 - Geliştirme arayüzünde **MultiLanguage butonu** ile **çeviri işlemi** yapıldıktan
    sonra **sekmenin kapanmama** hatası düzeltildi.
- 61185 [DR9583] - Geliştirme arayüzünde **Proje Aç** işleminde projelerdeki **alt**
    **dosyaların gözükmeme hatası** düzeltildi.
- 61671 - Geliştirme arayüzünde **ReportViewer** nesnesinin **Report** dosyasına
    tıkladığımızda **hata verme sorunu** düzeltildi.
- 56701 - Geliştirme arayüzünde **Akış** tarafında **Özellik Görüntüleyici** açıldığında **GetAll**
    **endpointinin 2 defa çalışma** hatası düzeltildi.
- 53984 [DR8842] - Geliştirme arayüzünde **Çözüm** içerisinde oluşturulan projede **form**
    **açılmak istenildiğinde oluşan hata** düzeltildi.
- 61196 [DR9582] - Geliştirme arayüzü görünümlerde **Tab nesnesi silindiğinde** diğer
    nesnelerden **silinmeme hatası** düzeltildi.
- 61603 - Geliştirme arayüzünde **Akış** tarafında **butonların çoklanma hatası** düzeltildi.


- 59760 [DR9299] - Geliştirme arayüzünde form üzerindeki nesnelere **Datasource**
    alanından **parametre doldurma** işleminde **valueEntry** olarak giriş yapıldığında
    **varsayılan değerin kaydedilmeme hatası** giderildi.
- 62553 - Geliştirme arayüzünde **Akış** tarafında **Aksiyon Oluşturucu** nesnesinde **Sınıf**
    **ekleme işleminde aynı Sınıf eklenebilme hatası** düzeltildi.
- 59663 - Geliştirme arayüzünde **Scheduler Service Basit Tetikleyici** eklendiğinde
    **missfire rule boş gelme hatası** düzeltildi.
- 60030 [DR9378] - Geliştirme arayüzünde **Datasource** sorgusunda **değişiklik**
    yapıldığında **parametrenin silinme hatası** düzeltildi.
- 61229 - Geliştirme arayüzünde **Yeni Proje Oluştur** dedikten sonra **Klasör Seç**
    panelinde içine girilen klasörün **sayfa sayısının olduğundan fazla gözükme hatası**
    düzeltildi.
- 61396 - Geliştirme arayüzünde **Proje Yöneticisinde proje silindiğinde** silinmiş
    projelerde sadece **yeni silinen projenin gözükme hatası** düzeltildi.
- 62372 - Geliştirme arayüzünde **Dinamik ListBox** nesnesinin ögelerinin **ts** tarafında
    **Selected True** olarak güncellendiğinde Web **arayüzüne yansımama hatası** düzeltildi.
- 62593 - Geliştirme arayüzünde **Akış** tarafında **Buton** özelliklerinde bulunan form
    seçiminde **mevcut belge tipinin de seçilebilir olma hatası** düzeltildi.
- 62605 - Geliştirme arayüzünde **Nesne Gezgininden seçilen objeye çift tıklanıldığında**
    **objeye odaklanmama hatası** düzeltildi.
- 62703 [DR9847] - Geliştirme arayüzünde **Flow Variables** alanına eklenen **değişken**
    nesnelerinin, Web arayüzünde **İş Akış Yönetimi, Bekleyen İşler** ve **Süreç** detaylarında
    **gözükmeme hatası** düzeltildi.
- 62989 - Geliştirme arayüzünde **Datasource** klasöründe **yeni eklenen GPT sorgusu**
    **değişiklik yapılmadan çalıştırmak istenildiğinde çalışmama** hatası düzeltildi.
- 63002 - Geliştirme arayüzünde **GetProject endpointinde tüm projelerin getirilme**
    **hatası** düzeltildi.
- 11074 - Geliştirme arayüzünde, Proje oluşturulurken **maksimum 100 karakter**
    sınırlamasıyla beraber **Proje adı** düzenlendiğinde **100'den fazla karakterli veri girişi**
    yapıldığı zaman **uyarı mesajı verilmesi** sağlandı.
- 50750 - Geliştirme arayüzünde **Proje Yöneticisi** üzerinden **İçe Aktar** işleminde **log**
    **bilgilerinin yazmama hatası** düzeltildi.
- 56207 - Geliştirme arayüzünde **Proje Yöneticisinde İçe Aktar işleminde** , **Aksiyon**
    **formu** içeren Proje aktarıldığında, **Deploy işleminde alınan hata** düzeltildi.
- 63387 - Geliştirme arayüzünde **GPT Datasource** sorgusunda **Aktif olmayan**
    **parametrenin kullanılma hatası** düzeltildi.
- 63513 - Geliştirme arayüzünde **Aksiyon formu eklenmek** istediğinde alınan **konsol**
    **hatası** düzeltildi.
- 63607 - Geliştirme arayüzünde **Proje Yöneticisinde Dışa Aktar işlemi yapılırken**
    alınan hata düzeltildi.


- 63724 [DR10027] - Geliştirme arayüzünde **Flow Variables Caption bilgileri**
    düzenlenen akışta, Web arayüzünde **Bekleyen İşler** alanında **değişken adını başlıktan**
    **almama** hatası düzeltildi.
- 64649 [DR10160] - Geliştirme arayüzünde **Flow Variables** alanına **PackageVersion** ,
    **MobileFormView** kolonları ile **Visible** , **Caption** gibi özellikleri **eklenerek** hata
    düzeltildi.
- 62063 [DR9708] - Geliştirme arayüzünde **Akış** tarafında **Pozisyon** nesnesinde
    doküman özelliğinde **Editable false** olduğunda, Web arayüzünde form ekranında
    **Datagrid** nesnesinin **ReadOnly gibi gözükme hatası** düzeltildi.
- 63000 - Geliştirme arayüzünde formda **Statik ComboBox** nesnesine **değer eklerken**
    **başlığın silinme hatası** düzeltildi.
- 64086 [DR10085] - Geliştirme arayüzünde **SQL** sorgusunda **Türkçe karakter** içeren
    kolonların **Display Expression** alanına girilmesi sonucunda **formun hata vererek**
    **açılmama sorunu** düzeltildi.
- 64091 [DR10054] - Geliştirme arayüzünde formda **ProtectedTextBox** nesnesinin
    **görünümü gizlenerek kullanılması engellendi**.
- 64248 - Geliştirme arayüzünde **Info Extractor** tipindeki **GPT** sorgusunda **Fields**
    alanında **Description** bilgisinin **boş olarak kaydedilme hatası** düzeltildi.
- 64510 [DR10136] - Geliştirme arayüzünde formda **Değer Ata seçeneği** ile **Kural**
    **Yöneticisinden** otomatik kural oluşturunca **Önizleme** butonuna basıldığında **formun**
    **donma hatası** düzeltildi.
- 64575 - Geliştirme arayüzünde **Akış Yöneticisinde Has Error filtrelemesi** yapılıp **filtre**
    **silindiğinde oluşan hata** düzeltildi.
- 64580 - Geliştirme arayüzünde **Akış Yöneticisinde Project** bilgisinde, ortama giriş
    yapılan dil karşılığındaki **proje ismi boş** ise dolu olan **dildeki proje isminin yazılmama**
    hatası düzeltildi.
- 64626 - Geliştirme arayüzünde **Akışlar** açıldığında **nesnelerin gözükmeme hatası**
    düzeltildi.
- 64786 - Geliştirme arayüzünde **Akış özelliklerinde Değişkenler alanında Paket**
    **Sürümü** ve **Mobil Form Görünümü bilgilerinin silinmemesi** sağlandı.
- 64843 - Geliştirme arayüzünde **Akış Yöneticisinde filtre işlemi çarpı ile silindiğinde**
    Datagrid'in **yeniden yüklenme hatası** düzeltildi.
- 64863 - Geliştirme arayüzünde **Akış özelliklerinde Değişkenler** alanında **kontrol** ve
    **değişken ekleme** işleminde **başlık bilgisinin set edilmeme hatası** düzeltildi.
- 65039 - Geliştirme arayüzünde **Akış Değişkenleri** alanına eklenen **true/false** tipindeki
    öge değerlerinin Web arayüzünde form ekranında **Akış özelliklerinde gözükmeme**
    hatası düzeltildi.
- 65415 - Geliştirme arayüzünde formda **DateTimePicker** nesnesinin **Disable Before**
    özelliği **Aktif** edildiğinde altındaki **Year, Month, Day giriş kutularının görünmeme**
    **hatası** düzeltildi.


- 65240 - Geliştirme arayüzünde **form içeri aktarıldığında alınan konsol hatası**
    düzeltildi.
- 65482 - Geliştirme arayüzünde **ts** dosyasında **Fast Approval işleminde düzenleme**
    yapıldı.
- 65506 - Geliştirme arayüzünde **Akış** tarafında **Documents** özelliği içeren nesnelerde
    **görünüm seçme zorunluluğu** sadece **form tipindeki dokümanlar için geçerli olması**
    sağlandı.
- 65515 - Geliştirme arayüzünde formda **Name** alanının **değiştirilememesi** ve
    **sonrasında ortamın donma hatası** düzeltildi.
- 65802 - Geliştirme arayüzünde **Bağlantılar** alanında **Oracle** bağlantısını **Kaydetme** ve
    **Test işlemlerinde oluşan hata** düzeltildi. **Araçlar** menüsünden **Bağlantı** tanımlama
    işleminde **Oracle** bağlantısında **Bağlantı bilgileri sekmesi kaldırıldı**. Bağlantı işlemi
    **Gelişmiş** tabındaki **bağlantı metni ile sağlanacak**.

DATA SOURCE="(DESCRIPTION =(ADDRESS = (PROTOCOL = TCP)(HOST =
Adres)(PORT = port))(CONNECT_DATA =(SERVER = DEDICATED)(SERVICE_NAME =
service)))";PASSWORD=[Password];USER ID=UserId;

- 65809 [DR10411] - Geliştirme arayüzünde formda **RelatedDocuments** nesnesinde
    **Text** özelliğinin **Değer Atayın** kısmından atama yapıldığında **Kural Yöneticisi**
    panelinde **otomatik kural oluşmama hatası** düzeltildi.


### 3.3. Android

#### • 60561 – Android cihazların mobil arayüzünde, Webview görünümündeki formlarda

#### konum izninin Webden de gelme hatası düzeltildi.

#### • 44479 - Android cihazların mobil arayüzünde, Webview görünümündeki DataGrid

#### nesnesinde Dışa Aktar işleminde yükleme ekranında kalma hatası düzeltildi.

#### • 49425 - Android cihazların mobil arayüzünde, Native+ görünümündeki DataGrid

```
nesnesinde Selection Settings özelliklerinde seçilen satırda seçim işleminin geri
```
#### alınamama hatası düzeltildi.

#### • 61097 - Android cihazların mobil arayüzünde, Webview görünümündeki

```
DateRangePicker nesnesinde açılan menünün sol tarafının gözükmeme hatası
```
#### düzeltildi.

#### • 62442 - Android cihazların mobil arayüzünde, Native+ görünümündeki OSF

```
özelliğinde olan DataGrid nesnesinde Düzenleme işlemi yapıldığında bu
```
#### düzenlemenin satırdaki bilgiler kısmına geçmeme hatası düzeltildi.

#### • 62446 - Android cihazların mobil arayüzünde, Native+ görünümündeki OSF DataGrid

#### nesnesinde aynı anda Modal ve Drawer form eklenememe hatası düzeltildi.

#### • 62861 - Android cihazların mobil arayüzünde Required alanlar için düzenleme

#### yapıldı.

#### • 52304 - Android cihazların mobil arayüzünde, Native+ görünümündeki NumberBox

```
nesnesinde minimum değeri pozitif bir sayı olan alanda negatif sayı girişi
```
#### yapılabilme hatası düzeltildi.


### 3.4. IOS

- 46892 - **IOS** cihazların mobil arayüzüne, **Native+** görünümündeki **DataGrid**
    nesnesindeki **Tarih** kolonlarında **filtreleme işlemi yapılamama hatası** düzeltildi.

#### • 60561 – IOS cihazların mobil arayüzünde, Webview görünümündeki formlarda

#### konum izninin Webden de gelme hatası düzeltildi.

- 55853 - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki **Statik DataGrid**
    nesnesinde **Düzenleme** işleminde **ComboBox verilerinin gelmeme hatası** düzeltildi.

#### • 61097 - IOS cihazların mobil arayüzünde, Webview görünümündeki

```
DateRangePicker nesnesinde açılan menünün sol tarafının gözükmeme hatası
```
#### düzeltildi.

#### • 62861 - IOS cihazların mobil arayüzünde Required alanlar için düzenleme yapıldı.


## 4. Breaking Changes

1. Projeler **tekrar** yayınlanmalıdır.




<font size="5"><a href="https://portal.synergynow.io/#/_redirect/x9CgXmEf0dgs03aDQRxqVd"  target="_blank"><svg fill="currentColor" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" viewBox="0 0 40 40" style={{verticalAlign: "middle"}}><g><path d="m35.8 8.5q0.6 0.6 1 1.7t0.5 1.9v25.8q0 0.8-0.6 1.5t-1.6 0.6h-30q-0.9 0-1.5-0.6t-0.6-1.5v-35.8q0-0.8 0.6-1.5t1.5-0.6h20q0.9 0 2 0.4t1.7 1.1z m-9.9-5.5v8.4h8.4q-0.3-0.6-0.5-0.9l-7-7q-0.3-0.2-0.9-0.5z m8.5 34.1v-22.8h-9.3q-0.9 0-1.5-0.6t-0.6-1.6v-9.2h-17.1v34.2h28.5z m-11.4-13.2q0.7 0.6 1.8 1.3 1.3-0.2 2.6-0.2 3.3 0 4 1.1 0.4 0.5 0 1.2 0 0 0 0l0 0v0.1q-0.2 0.8-1.6 0.8-1.1 0-2.6-0.4t-2.9-1.2q-4.9 0.5-8.7 1.8-3.4 5.9-5.4 5.9-0.4 0-0.7-0.2l-0.5-0.2q0-0.1-0.1-0.2-0.3-0.2-0.2-0.8 0.2-0.8 1.3-2t2.9-2.1q0.3-0.2 0.5 0.1 0.1 0 0.1 0.1 1.1-1.9 2.4-4.4 1.5-3.1 2.3-5.9-0.5-1.8-0.7-3.5t0.2-2.9q0.2-0.9 0.9-0.9h0.5q0.5 0 0.8 0.4 0.4 0.4 0.2 1.5-0.1 0.1-0.1 0.2 0 0 0 0.1v0.7q0 2.8-0.3 4.3 1.2 3.7 3.3 5.3z m-12.9 9.2q1.2-0.6 3.1-3.5-1.2 0.8-2 1.8t-1.1 1.7z m8.9-20.6q-0.4 1-0.1 3 0.1-0.2 0.2-1 0-0.1 0.1-0.9 0.1-0.1 0.1-0.2 0-0.1 0-0.1t0 0 0 0q0-0.5-0.3-0.8 0 0 0 0v0z m-2.8 14.8q3-1.2 6.4-1.8-0.1 0-0.3-0.2t-0.4-0.3q-1.7-1.5-2.8-4-0.6 2-1.9 4.4-0.7 1.3-1 1.9z m14.4-0.4q-0.5-0.5-3.1-0.5 1.7 0.6 2.8 0.6 0.3 0 0.4 0 0 0-0.1-0.1z"></path></g></svg>PDF Download</a></font>