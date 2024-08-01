
# Synergy Akış Tarafında Event için Sebep Girilmesi

Bu dokümantasyon, Synergy Akış tarafında bir event için sebep girilmesi gerektiğinde, bu değeri nasıl alabileceğinizi açıklamaktadır.

## Event İçin Sebep Alma

Bir event için sebep girilmesi isteniyorsa, bu değeri ilgili onaycı nesnesinin `OnAfterEvent` veya `OnBeforeEvent`'inde aşağıdaki şekilde alabilirsiniz:

```csharp
string reason = args.Reason["tr-TR"];
```

### Adımlar

1. **OnAfterEvent veya OnBeforeEvent Kullanımı:**

   İlgili onaycı nesnesinin `OnAfterEvent` veya `OnBeforeEvent` metodunda, sebep değerini almak için aşağıdaki kodu kullanabilirsiniz:

    ```csharp
    public void Position1_OnAfterEvent(object sender, OnBeforeEventArguments args)
    {
        string reason = args.Reason["tr-TR"];
        // Diğer işlemler
    }
    ```

    veya

    ```csharp
    public void Position1_OnBeforeEvent(object sender, OnBeforeEventArguments args)
    {
        string reason = args.Reason["tr-TR"];
        // Diğer işlemler
    }
    ```

## Sonuç

Bu yöntemle, Synergy Akış tarafında bir event için girilen sebep değerini kolayca alabilirsiniz.
