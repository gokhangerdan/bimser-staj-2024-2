---
sidebar_label: Form Bilgileri Bölümü
sidebar_position: 1
custom_edit_url: ""
---

# Form Bilgileri Bölümü

Öncelikle forma, form başlık bilgisi ekleyelim. Bunun için [Header](ide-objects/form/standart-form-controls/Header.md) nesnesi kullanılır. Header nesnesi, araç kutusundan sürükle/bırak yöntemi ile forma eklenir. Forma eklenen nesneye çift tıklandığında [Özellik Görüntüleyici](ide/menu-structure/view/property-inspector.md) paneli açılacak ve burada Header nesnesinin özellikleri listelenecektir. Header nesnesinin **Metin (Text)** alanına, form başlığı olarak gösterilmek istenen metin girişi yapılır.

![Form Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc99125c2-c420-42ec-8ba0-5b391e628726)

Form farklı bölümlerden (Form Bilgileri, Talep Eden Bilgileri, İzin bilgileri gibi) oluşacağı için, karmaşık görünmemesi açısından, bölüm bilgileri [Label](ide-objects/form/standart-form-controls/Label.md) nesnesi kullanılarak belirtilebilir. Böylece hangi nesne hangi bölüme ait ise ilgili bölüm başlığı altında bulunmuş olur.

![Form Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload108b62fd-9bd5-458f-81eb-b133ad18bccf)

Form bilgileri bölümünde, **Belge Numarası** ve **Belge Tarihi** alanları bulunacaktır. Forma ait bu iki bilginin de form yaratıldığında sistem tarafından otomatik dolması için [DocumentMetadata](ide-objects/form/user-and-document-data/DocumentMetadata.md)  nesnesi kullanılır.

**Belge Numarası** alanı için, DocumentMetadata nesnesi forma eklenir ve özelliklerindeki **Select Metadata Type** alanından **Id** seçeneği seçilir.

![Form Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca4d9e31-3b7c-4777-bf15-814f41bf950c)

**Belge Tarihi** alanı için, DocumentMetadata nesnesi forma eklenir ve özelliklerindeki **Select Metadata Type** alanından Oluşturulma Tarihi **CreateDate** seçeneği seçilir.

![Form Bilgileri Bölümü](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload659107e8-61f4-42f3-967c-d691749f6841)