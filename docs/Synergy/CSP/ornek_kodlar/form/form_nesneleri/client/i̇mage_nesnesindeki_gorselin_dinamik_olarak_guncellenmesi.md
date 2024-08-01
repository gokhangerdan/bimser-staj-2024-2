# İmage Nesnesindeki Görselin Dinamik Olarak Güncellenmesi

İmage nesnesinin dinamik olarak güncellemesi için aşağıda örnek kod bulunmaktadır.


```
 TextBox1.Text = "a";
      TextBox1.Value = "a";
            if(TextBox1.Text !=""){
                Image1.FileName=TextBox1.Text.ToLower()
                .Replace("ç","c")
                .Replace("ğ","g")
                .Replace("ı","i")
                .Replace("ş","s")
                .Replace("ü","u")
                .Replace("ö","o")
                .Replace("Ç", "c")
                .Replace("Ğ", "g")
                .Replace("İ", "i")
                .Replace("Ş", "s")
                .Replace("Ü", "u")
                .Replace("Ö", "o")
                .Replace(" ","_")+".png";
            }
```

![](https://docsbimser.blob.core.windows.net/imagecontainer/img2-35df4e46-97b0-4e80-b4dd-e6ef63336033.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/img1-16fd54cc-9718-4f4e-be5c-7500bc10435d.png)

