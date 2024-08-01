# Form Üzerinde Farklı Kaydet Butonu Kullanımı

Synergy üzerinde bir form oluşturulduğu zaman form üzerinde varsayılan olarak iki farklı toolbar button oluşmaktadır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/ToolbarButtons-603d7a2d-7f39-4e10-9037-ff6adca733a7.png)

Buradaki Farklı Kaydet butonu önceden kaydedilmiş bir formun verileriyle başka bir kayıt oluşturmak için kullanılır.

Bu butonu kullanabilmek için önceki bölümlerde anlatılmış olan openForm yöntemine "isSaveAsForm" parametresini geçmemiz gerekmektedir.

```
 this.openForm({
                    projectName: "FormunBulunduguProjeIsmi",
                    documentId: "KopyalanmakIstenenFormunDocumentIdDegeri",
                    typeName: "OpenFormArgs",
                    showOn: "drawer",
                    isSaveAsForm: true,
                    size: 2,
                    parameters: [
                        {  }
                    ]
                });
```

