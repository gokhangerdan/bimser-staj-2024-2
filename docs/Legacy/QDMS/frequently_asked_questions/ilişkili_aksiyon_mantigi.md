# İlişkili Aksiyon Mantığı

İlişkili aksiyonlar birbirlerini takip eden aksiyonlar olarak düşünülmeli. İlişkili bir aksiyon açıldığında ilgili aksiyonun statüsü "Bekliyor" şeklinde olacaktır
Örnek üzerinden aktaracak olursam;
5.5 numaralı bir aksiyon kaleminin 5.1 numaralı aksiyon ile ilişkili oluşturduğumuzu düşünelim. Bu durumda 5.5 numaralı aksiyon kalemi "Bekliyor" statüsünde olacaktır. 5.5 numaralı aksiyonun "Açık" duruma geçebilmesi için, ilişkli olduğu 5.1 numaralı aksiyonun "Kapalı" olması gerekiyor.

Eğer; "Gerçekleşme tarihine göre aç" seçeneğini işaretlediyseniz; sistemde 5.5 numaralı aksiyon kalemini 5.1 numaralı aksiyon kaleminin gerçekleştirildiği "an" açık duruma geçecektir.

Eğer; "Gerçekleşme tarihine göre aç" seçeneğini işaretlemediyseniz; sistem 5.5 numaralı aksiyon kaleminin başlangıç tarihi geldiği gün ajan sistemi (gecikme maillerini, ön bildirim mailleri, periyodik aksiyonları üreten sistem) çalıştığında açık duruma gecektir. Özetle "Gerçekleşme tarihine göre aç" seçeneği işaretlenmediyse ve test ortamında ajan sistemi aktif değilse ilişkili durumda olan bir sonraki aksiyon açılmayacaktır. Gerçekleşme tarihine göre aç seçeneği işaretlenmeyen aksiyonların açılması için bir sonraki aksiyonun başlangıç tarihi gelmiş olmalı ve ajan sistemi tanımlı olmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/ilişkili_aks1-ef73b95d-5a3f-4f14-a33e-534ec2d2178f.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/ilişkili_aks2-b7cc30f2-53d8-4aaf-9d6b-077bfb00c8f9.png)

