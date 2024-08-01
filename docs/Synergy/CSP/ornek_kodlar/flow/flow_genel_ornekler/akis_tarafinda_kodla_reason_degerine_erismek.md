# Akış Tarafında Kodla Reason Değerine Erişmek

## Örnek Kodlar

### Flow

Akış tarafında reason değerini almak istediğimiz pozisyon nesnesi için OnAfterEvent veya onBeforeEvent olaylarını tanımlayarak, kod tarafında bu bilgiyi args.Reason["tr-TR"] şeklinde alabiliriz. 



```
if(args.EventCode == 6) // Reason özelliğinin bulunduğu butonun numarası  
                LogExtension.Log("Position1_OnAfterEvent: " + args.Reason["tr-TR"], args.Context);
```

