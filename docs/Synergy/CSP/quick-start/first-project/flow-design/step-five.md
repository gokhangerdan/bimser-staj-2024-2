---
sidebar_label: Beşinci Adım
sidebar_position: 5
custom_edit_url: ""
---

# Beşinci Adım

Akışın son adımı olarak, akışı başlatan kişiye, yıllık izin talebinin onaylandığına dair bir bilgilendirme maili gönderilecek ve akış bitirilecektir.

Bilgilendirme maili göndermek için kullanılacak olan **Bilgilendirme** nesnesi, pozisyon grubu nesnesinden sonra akışa, bir önceki adımda yerleştirilmişti. Bilgilendirme nesnesinin **“Grup İçeriği”** özelliğinde;

- **Grup Tipi** alanında gruba hangi tipte kullanıcı atanacağının seçimi yapılır. Bilgilendirme nesnesi ile akışı başlatan kullanıcıya mail gönderileceği için burada “Pozisyon” seçeneği seçilir.

- **İçerik Tipi** alanında ise, bilgilendirme mailine hangi tipte kişi ekleneceğinin seçimi yapılır. Burada listelenen seçeneklerde **“Akışı Başlatan”** seçeneği de listelenmektedir ve akışı başlatan kullanıcıyı bilgilendirme nesnesine eklemek için bu seçenek seçilir.

![Beşinci Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload21bb525f-57ff-4635-8cd8-af5dee0539d1)

Eğer bilgilendirme mailine, doldurulan sürecin formu da ek olarak eklenmek istenirse, Bilgilendirme nesnesinin özelliklerindeki **Dokümanlar** alanından, formun bağlı olduğu doküman nesnesi seçimi yapılır.

![Beşinci Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3d3eabd-7b5b-430f-b50f-ad266bfd643e)

Gönderilecek mailin; başlık, mesaj ve mail içeriği kısımlarında düzenleme yapılabilir.

![Beşinci Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54962ed7-e908-49f4-b6e2-7f6153a51cff)

Bilgilendirme maili gönderildikten sonra akış tamamlanacağı için, Bilgilendirme nesnesinden çıkarılan ok, **Akış Bitişi** nesnesine bağlanır. Böylece, IK Departmanı grubundan bir kişi formu onayladığında akış, bilgilendirme nesnesi ile mail gönderir ve biter.

![Beşinci Adım](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcd718d0-d4d1-42d3-af60-8e3d1b7eec2f)