# Mobil ve Web Üzerinde Bildirim Mesajlarını Alabilmek İçin Yapılması Gerekenler

Mobil ve Web üzerinde bildirim alabilmek için sistem parametrelerinde bazı ayarlamaları yapmamız gerekmektedir. Bunun için aşağıdaki yol izlenerek sistem parametrelerine gelinir:
Ana Menü -> Sistem -> Sistem Parametreleri
İlgili parametrelerimiz aşağıdaki gibidir ve karşılığında ise ne doldurulması gerektiği yazmaktadır:
Message.ControlInterval - 5000,
Message.DropDownMessageCount - 7,
Message.Enable - true,
Message.MailNotification.ContentTemplateCode – test,
Message.MailNotification.ContentTemplateCode parametresi için gönderim formatlarında “test” adında bir gönderim formatı bulunması gerekmektedir.
İzlenmesi gereken adımlar aşağıdaki gibidir:
Ana Menü -> Bakım Yönetimi -> Tanımlar -> Gönderim Formatları -> Ekle -> Gönderim türü: fark etmeyecek şekilde bırakılabilir -> Gönderim formatı kodu: test -> Gönderim formatı tanımı: test -> Konu: test -> Format: test olarak yazılır.
Message.MailNotification.Enable - false,
Message.MessageControlInterval - 5000,
PushMessage.Active - true,
PushMessage.Culture - tr-TR,
PushMessage.InstanceName - INSTANCEADINIZ,
PushMessage.Interval - 1,
PushMessage.TryCount – 5


![](https://docsbimser.blob.core.windows.net/imagecontainer/BİLDİRİM1-0c009731-eb3c-484c-b63c-5056c486e50c.png)

İlgili ayarlar doldurulduktan sonra BOYSWEB2PushMessageService_INSTANCE adlı Windows servisimiz çalıştırılır.
Çalışır haldeyse de “Restart” edilir.


