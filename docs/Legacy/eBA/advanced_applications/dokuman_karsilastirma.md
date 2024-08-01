# Doküman karşılaştırma

## eBA Doküman yönetimi modülünde barındırılan dokümanların eBA uygulaması üzerinden versiyonları arasında karşılaştırma yapabilme özelliği bulunur.

Karşılaştırma özelliği ile eBA üzerindeki Doküman yönetimi kütüphanelerinde bulunan dokümanların karşılaştırması yapılabildiği gibi, kullanıcı imzalama veya onay işlemlerinde, onaydaki dokümanın versiyonları da karşılaştırılabilmektedir.

Karşılaştırma özelliğinin kullanılabilmesi için öncelikle doküman görüntüleme amaçlı kullanılan viewer uygulamasının kurulu olması gerekir.

Viewer uygulaması eBA kurulumuyla paralel olarak ilk kurulumda yapılarak, viewer uygulamasında güncelleme yapıldıkça eBA ile birlikte güncellenmektedir.

___

1- Karşılaştırma özelliği için viewer uygulamasının kurulu olduğu dizinde yer alan web.config dosyasına aşağıdaki tanımların ilgili alana eklenmesi gerekir.

```
<httpProtocol>
      <customHeaders>
        <clear />
        <add name="X-UA-Compatible" value="IE=EDGE" />
        <add name="Access-Control-Allow-Origin" value="*" />
        <add name="Access-Control-Allow-Headers" value="Origin, X-Requested-With, Content-Type, Accept" />
        <add name="Access-Control-Allow-Methods" value="GET, POST, PUT, DELETE, OPTIONS" />
      </customHeaders>
</httpProtocol>
```

2- eBA uygulamasının kurulu olduğu dizinde common klasöründe yer alan eBAConfigurationEditor.exe içerisindeki Advanced sekmesinde "config > DocumentManagement > Comparison" altında 'BasePath' ve 'ServicePath' key'lerinin eklenmesi sırasıyla kullanılan viewer uygulamasının ve servisinin adresleri tanımlanmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/ComparisonComparison-305143c2-1207-4ca7-84fb-911662b26f85.png)

3- Kullanıcıların dokümanlarda karşılaştırma yapabilmesi için eBA üzerinde webComparisonVisible yetkisine sahip olması gerekir. Bu yetki eBA System Manager üzerinden ilgili kullanıcı, pozisyon ya da gruba tanımlanmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/webComparisonVisible%20yetkisi%20gruba%20tanımlama-483a2b8b-8459-4080-a398-963c4181771d.png)

4- Yapılan tüm ayarlar sonrasında eBA uygulamasında Karşılaştır butonu yer alacaktır. Butona tıklandığında versiyonların seçileceği bir pencere açılır. Butona tıklandığında işlevsiz bir durumdaysa aşağıdaki key'lerin eBA uygulamasının kurulu olduğu dizindeki eba.net klasöründe yer alan web.config dosya içerisine ilgili alana eklenmesi gerekmektedir.

```
<httpProtocol>
      <customHeaders>
        <clear />
        <add name="X-UA-Compatible" value="IE=EDGE" />
        <add name="Access-Control-Allow-Origin" value="*" />
        <add name="Access-Control-Allow-Headers" value="Origin, X-Requested-With, Content-Type, Accept" />
        <add name="Access-Control-Allow-Methods" value="GET, POST, PUT, DELETE, OPTIONS" />
      </customHeaders>
</httpProtocol>
```

___

Karşılaştırma özelliğine ait örnek ekran görüntüsü aşağıdaki şekildedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Comparison_Result-887bba29-239d-4378-945b-e7d23df29725.png)

