# Form İndex'leme İçin Gerekli Eklentiler

Aşağıda  ekli olan iki sorguyu ortamınızda çalıştırarak, Form İndex'leme aracını aktif edebilirsiniz.  İşlemi gerçekleştirdikten sonra, özelliği kullanabilmek adına ortamın çalıştığı sunucuya Apache Tika kurulumun gerçekleştirilmesi gerekmekte.


```
UPDATE CONFIGURATIONS SET VALUE ='[{"Name":"ApacheTikaProcessor","ProcessorType":4,"Parameters":{"ServiceUrl":"
http://tika.synergy.svc.cluster.local:9998/","Ocr":true,"OcrLanguage":"eng+tur+deu"},"FallbackConfiguration":null},{"Name":"AzureCognitiveComputerVisionOcr","ProcessorType":2,"Parameters":{"ClientSecret":"xxx","ServiceUrl":"https://westeurope.api.cognitive.microsoft.com/"},"FallbackConfiguration":null},{"Name":"Text","ProcessorType":1,"Parameters":{},"FallbackConfiguration":null}]' 
WHERE KEYNAME = 'DocumentManagement.Indexing.Processors'




UPDATE CONFIGURATIONS SET VALUE ='[{"IndexProviderType":3,"Parameters":{"ServerUrl":"http://elasticsearch-master:9200/","UserName":"elastic","Password": "8Mf9SJM0twFtiywe"},"Active":true},{"IndexProviderType":2,"Parameters":{"ServerUrl":"http://solr-cluster-solrcloud-headless.solr.svc.cluster.local:8983/"},"Active":false},{"IndexProviderType":1,"Parameters":{"ApiKey":"ApiKey","ServiceName":"ServiceName","MaxUploadTry":"3"},"Active":false}]' WHERE KEYNAME = 'Configurations.Section-sys.IndexerConfigKey'

```

