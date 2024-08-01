---
sidebar_label: Talep Eden Kullanıcı Bilgileri Bölümü
sidebar_position: 2
custom_edit_url: ""
---

# Talep Eden Kullanıcı Bilgileri Bölümü

Talep eden kullanıcı bilgileri bölümü için forma [Label](ide-objects/form/standart-form-controls/Label.md) nesnesi ile yeni bir bölüm başlığı yazalım.

![Talep Eden Kullanıcı Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8eac2cf1-fee9-4252-9a44-e9f51c3b899e)

Form web arayüzde açıldığı anda, menüden formu açan kullanıcının yani akışı başlatan kullanıcının **Ad-Soyad** ve **Departman** bilgilerinin, forma sistem tarafından otomatik yüklenmesi için [UserMetadata](ide-objects/form/user-and-document-data/UserMetadata.md) nesnesi kullanılır.

**Adı Soyadı** alanı için forma UserMetadata nesnesi eklenir ve nesne özelliklerindeki **Select Metadata Type** alanından **NameAndSurname** seçeneği seçilir.

![Talep Eden Kullanıcı Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9afa2898-47f3-43e2-ae76-b550e53290ba)

**Departmanı** alanı için forma yine UserMetadata nesnesi eklenir ve nesne özelliklerindeki **Select Metadata Type** alanından bu kez **Department** seçeneği seçilir.

![Talep Eden Kullanıcı Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae2fd7bf-0f3a-4403-93b0-161793cf4816)