---
title: "Birinci Adım"
sidebar_position: 1
---

# Birinci Adım
Geliştirme arayüzünde bir proje oluşturulduğunda varsayılan olarak gelen akış ekranında **Akışı Başlatan (Flow Starter 1)** nesnesi mevcuttur. Ve bu nesneye aksiyon butonu olarak **Gönder (Send)** olayı eklenmiş olarak gelir.

Doküman 1 nesnesinin **Properties** özelliklerinde **Project** alanında Masraf Beyan Süreci, **Form** alanında da Masraf Beyan Formu seçilir. **View** olarak da farklı bir view hazırlanmadığı için default view seçilir.

Ardından Akış Başlangıcı nesnesinin Properties özelliklerinde **Documents** alanından da Document1 nesnesi seçilir.

Bu sürecin senaryosu gereği akışı başlatan formu doldurduktan sonra akış, Amir onayı için akışı başlatanın amirine yönlendirilecektir.

Akışı başlatanın amirine atama işleme için Atama nesnesinde atamanın yapılacağı hedef nesne için **Target Object** alanından Akışı Başlatanın Amiri(Position1), atanacak değer için ise **Source Type** olarak **Akış Başlatanın Yöneticisi** seçilir.

Position1’in Properties özelliklerinden **Document** alanına Document1 eklenir.
![akis birinci adim](https://docsbimser.blob.core.windows.net/imagecontainer/akis%20birinci%20adim-c8a1638b-03ab-4382-8899-65ac0ba1076d.png)


