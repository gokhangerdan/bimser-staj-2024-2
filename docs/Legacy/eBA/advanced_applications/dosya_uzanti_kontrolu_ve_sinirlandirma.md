# Dosya uzantı kontrolü ve sınırlandırma

## eBA uygulamasına ve eBA Document Management modülü kütüphanelerine eklenebilecek dosyaların uzantılarını sınırlandırma

___

1- eBA uygulama arayüzü kullanılarak Upload aşamasında yüklenecek dosya uzantılarının kontrolü için, uygulamanın kurulu olduğu dizindeki eba.net.dm ve eba.net.dm.remote klasörü altındaki web.config dosya içeriğine eklenebilecekler.


```
<WhiteLists>
    <add key=".exe" value="application/octet-stream"/>
    <add key=".gif" value="image/gif"/>
    <add key=".png" value="image/png"/>
    <add key=".doc" value="application/msword"/>
    <add key=".docx" value="application/vnd.openxmlformats-officedocument.wordprocessingml.document" />
    <add key=".jpeg" value="image/jpeg"/>
    <add key=".jpg" value="image/jpeg"/>
    <add key=".xls" value="application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"/>
    <add key=".xlsx" value="application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"/>
    <add key=".pdf" value="application/pdf"/>
    <add key=".txt" value="text/plain" />
    <add key=".mp4" value="video/mp4"/>
    <add key=".msg" value="application/octet-stream" />
    <add key=".tiff" value="image/tiff" />
    <add key=".tif" value="image/tiff" />
    <add key=".pptx" value="application/vnd.openxmlformats-officedocument.presentationml.presentation" />
    <add key=".vsdx" value="application/vnd.ms-visio.drawing,application/vnd.ms-visio.viewer" />
    <add key=".ppt" value="application/vnd.ms-powerpoint" />
    <add key=".udf" value="application/octet-stream" />
    <add key=".heic" value="image/heic"/>
    <add key=".heic" value="image/heic-sequence"/>
</WhiteLists>


  <appSettings>
    <add key="debug" value="false"/>
    <add key="PerformanceLogEnabled" value="false"/>
    <add key="ValidationSettings:UnobtrusiveValidationMode" value="None"/>
    <add key="WhitelistEnable" value="true"/>
  </appSettings>
```

![](https://docsbimser.blob.core.windows.net/imagecontainer/eba%20net%20dm%20web%20config-80108165-f7a0-44d8-8037-8c5a7e23def0.png)

___

2- Dışarıdan servis aracılığıyla işlem yapılan yerlerde dosya uzantılarının kontrolü için 
eBA uygulamasının kurulu olduğu dizinde common klasöründe yer alan eBAConfigurationEditor.exe içerisindeki Advanced sayfasındaki DocumentManagement sekmesine aşağıdaki keyler eklenerek ilgili uzantılar tanımlanır.

Burada eba,frm,sln gibi proje dosyalarına ait uzantılar olmazsa, workflow üzerinden yeni proje dahi açılamamaktadır.

```
CheckContentType: true
ExtensionWhiteListEnable: true
ExtensionWhiteList: pdf,msg,eml,txt,gif,png,jpg,jpeg,mp3,mp4,xls,xlsx,doc,docx,ppt,pptx,vsdx,tif,tiff,eba,frm,sln
```

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBA%20Config%20Editör%20WhiteList-fb19f7ef-8335-438c-8e3a-0d6caf73fe88.png)

___

3- Doküman Yönetimi Modülü Kütüphane özelliklerinde 'Yeni Dosya' başlığı altında izin verilen bu uzantılar kütüphaneye özgü sınırlandırılabilir.

```
pdf|msg|eml|txt|gif|png|jpg|jpeg|mp3|mp4|xls|xlsx|doc|docx|ppt|pptx|vsdx|tif|tiff|eba|frm|sln
```

![](https://docsbimser.blob.core.windows.net/imagecontainer/DM%20Kütüphane%20Yeni%20Dosya%20Sınırlandırması-1b18eba6-7052-438f-9b2b-8e10b1b9f7d5.png)

