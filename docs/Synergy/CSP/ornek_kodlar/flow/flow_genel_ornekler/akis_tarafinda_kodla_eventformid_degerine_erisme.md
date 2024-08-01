# Akış tarafında kodla EventFormId değerine erişme

Event formdan  kaydettiğiniz formun documentID değerini almak için pozisyon nesnesinin (veya akış başlangıcı) OnAfterEvent olayının args değerinden döndürülen EventFormId değerini kullanabilirsiniz.
Bu değer DOCUMENTID değeridir ve ilgili olay formunun ID değerini içerir.

```
public void FlowStart1_OnAfterEvent(object sender,OnAfterEventArguments args)
		{
                    LogExtension.Log(args.EventFormId,args.Context);
		}
```

