# Akış'ta Pasif Kullanıcı Uyarısı

Configurations tablosunda aşağıdaki key value değerlerini girerek, akış başlatıldığında eğer ilgili adımda pozisyon grubunda veya pozisyonda herhangi bir kullanıcı pasif statüsündeyse, kullanıcı ekranında uyarı verdirir ve pasif kullanıcı olduğuyla ilgili hata döndürür, akışı ilerletmez mevcut adımda durdurur.

```
KEYNAME                                        VALUE
Workflow.Settings.ErrorOnInactiveAssignment    true

```

![](https://docsbimser.blob.core.windows.net/imagecontainer/exceptionImg-abcb5476-184c-40b5-90c5-ffb04eed2d7f.png)

