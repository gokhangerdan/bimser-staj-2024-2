# Sistem parametresi ile SSL kullanılan uygulamamızda Secure-Flag güvenlik açığını gidermek

- IIS içerisinde "Default Web Site" altında "HTTP Response Headers" alanından yeni başlık eklenmesi gerekiyor.

- Name =Strict-Transport-Security , Value= max-age=31536000

![](https://docsbimser.blob.core.windows.net/imagecontainer/Image01-a8732253-d20e-4711-8508-86fda039a24b.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/Image02-27ee7d39-0bad-46ef-84c9-2ee6c4fbbb1b.png)

