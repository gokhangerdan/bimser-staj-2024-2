# RelatedDocuments Nesnesine Dosya Yüklenmeden Önce İsmini Değiştirme

Client kısmına eklenen OnBeforeFileUpload eventiyle file ismi kod ile değiştirilebilmektedir.

Bu event ile Web arayüzünde nesneye yüklenen dosyanın adının başına, kod bloğunda belirtilen diğer ad gelmektedir. 

Bu değişen isim aynı zamanda Doküman Yönetiminde ilgili klasör içerisine yüklenen dosyanın adını da değiştirmektedir.


```
 async RelatedDocuments1_OnBeforeFileUpload(args: { name: string, file: File }) {
        const name = "yeniAd" + args.file.name;
        const file = new File([args.file], name, { type: args.file.type });

        return file;
    }
```

![](https://docsbimser.blob.core.windows.net/imagecontainer/img1-5524969d-5b34-41b1-8e2f-741c490b25bb.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/img2-ccc890a6-a567-490d-933b-ff14b363641e.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/img3-cc2336bb-ff67-4386-823f-f645848028a2.png)

