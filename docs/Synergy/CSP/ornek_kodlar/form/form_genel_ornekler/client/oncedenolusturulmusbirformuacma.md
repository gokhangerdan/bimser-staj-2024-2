# Önceden Oluşturulmuş Bir Formu Açma

Daha önceden oluşturulmuş ve kaydedilmiş bir formu istemci tarafında kod aracılığıyla tekrardan görüntülemek,
düzenlemek ve benzeri amaçlarla tekrardan açmak istiyorsak kullanacağımız yöntem şu şekildedir;

```
this.openForm({
                projectName: "FormunBulunduguProjeIsmi",
                documentId: "AcilmakIstenenFormunDocumentIdDegeri",
                typeName: "OpenFormArgs",
                showOn: "drawer",
                size: 2,
                parameters: [
                   {}
                ]
            });
```

