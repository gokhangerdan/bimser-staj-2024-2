# Combobox Validasyondan Dönüldüğünde Readonly Bozulması

Combobox nesnesi form üzerinde Readonly=False olarak ayarlandığında.
Form herhangi bir validasyon adımından geçtiğinde ,Combobox otomatik olarak Readonly=true olmaktadır.

```
//Readonly =false olan combobox, formun  validasyon mesajına takıldıktan sonra geri dönüldüğünde readonyl=true şeklinde davranış sergiliyor.
Validasyondan dönüldükten sonra bozulma yaşanmaması için  Formun OnBeginEdit bölümünde Comboboxın Readonly ayarı yapılabilir. 

Formun  OnBeginEdit eventine aşşağıdaki kodu yazdırabilirsiniz .

public void OnBeginEdit()
	{
                Liste2.Enabled = false;
        }  
```

