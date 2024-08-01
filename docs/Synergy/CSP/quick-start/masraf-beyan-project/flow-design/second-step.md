---
title: "İkinci Adım"
sidebar_position: 2
---

# İkinci Adım
Akış üzerinde yeni bir aksiyon kolu olarak “Revizyon” kolunu eklemek için akışta boş bir alana çift tıklanır ve **Events** sekmesinden Revizyon eventi eklenir. Bu sayede akış üzerindeki herhangi bir pozisyona bu aksiyon kolu eklenebilir hale gelir.

Senaryo gereği Akışı Başlatanın Amiri, Form için bir revizyon talebinde bulunabileceği için pozisyonun Events özelliklerinden Revizyon kolu eklenir ve Revizyon için bir Sebep girilmesi zorunlu kılınır. Bunun için **Reason** alanı aktif edilir ve **Reason Title** alanına da “Revizyon Sebebi” başlığı girilir.

Revizyon ve Red kollarından sonra bir **Bilgilendirme** nesnesi eklenir ve  akışı başlatana bilgilendirme maili gönderilebilir. Bunun için Bilgilendirme nesnesi akış üzerine eklendikten sonra **Group Content** özelliğinden Akışı Başlatan eklenir.

Revizyon sonrası onayın Akış Başlatan’a geri döndürülmesi için yeni bir pozisyon nesnesi akış üzerine eklenir. Pozisyonun aksiyon kolundaki onayla ve reddet event’leri silinir, yerine gönder eventi eklenir. Akışı başlatanın onayına sunulacak doküman, nesnenin Document özelliklerinden seçilir.
![akisikinciadim](https://docsbimser.blob.core.windows.net/imagecontainer/akis%202.adim-cbc9ad69-d42f-4793-adf9-c30f5c0380db.png)

