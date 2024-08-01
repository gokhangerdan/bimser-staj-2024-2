# RelatedDocuments eklenen dosya sayısını bulma

RelatedDocuments eklenen dosyaların kategori bazlı dosya sayısını bulabilmekteyiz.  Client(ts) tarafında RelatedDocuments  eventlerinden aşağıdaki örnek kodu kullanabilirsiniz.

```
        var a = args;
        let defaultCategory=0;
        let testKategori=0;
        this.RelatedDocuments1.files.forEach(x=>{
            switch (x.category.id){
            case 1:{
                defaultCategory++;
                break;}
            case 2:{
                testKategori++;
                break;}
            default:{
                break;}
                }
            
        })
        alert("Default kategori: "+ defaultCategory + " Test Kategori: "+testKategori);
```

