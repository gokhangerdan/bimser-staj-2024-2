# Attachmentsta Bulunan Belgenin Tarihini Alma Örnek Kod

```
public getAttachmentDate()
{
    eBAConnection con = CreateServerConnection();
    try
    {
        con.Open();
        DMFile form = con.FileSystem.GetFile(FormPath);//FormPath = forma ait path bildisi. Örneğin Dokuman1.Path
        foreach(var item in form.GetAttachments("Default"))
        {
            DateTime dt = item.CreateDate.Value;
        }
    }
    finally
    {
        con.Close();
    }
}

```

