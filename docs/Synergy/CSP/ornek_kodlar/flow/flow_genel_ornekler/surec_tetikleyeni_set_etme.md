# Kod İle Süreç Başlatırken Süreci Başlatan Kullanıcıyı Ekleme İşlemi

Kodla süreç tetikleme işleminde kullanıcıyı set edebilme için gerekli kod aşağıdaki örnekte bulunmaktadır.

```
           //process oluşturulur
            var process = ServiceApi.WorkflowManager.Create("tdeneme239","Flow2",0).Result;

            //akis baslatan kullanici set edilir (userid long tipte verilir)
            long userid = 2;
            process.SetStarterUserByUserId(userid).Wait();

            //akistaki forma erişilir
            var form = process.Documents["Document1"].FormInstance;

            //ornek olarak formda bulunan textbox set edilir
            form.Controls["TextBox1"].Value = "alt akış";

            //formu kaydedilir
            form.Save();

            //akisin hangi event ile ilerletilecegi secilir
            process.StartingEvent = process.Events[4];

            //akis ilerletilir
            process.SaveAndContinue();  



```

![](https://docsbimser.blob.core.windows.net/imagecontainer/img1-325936e8-3981-4034-a1b0-d76777e0edbb.png)

