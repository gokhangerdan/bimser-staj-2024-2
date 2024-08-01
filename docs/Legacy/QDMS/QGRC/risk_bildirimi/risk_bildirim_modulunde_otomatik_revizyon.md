# Risk Bildirimi Modülünde Otomatik Revizyon

Risk bildirim modülünde önlemlere bağlı olarak otomatik revizyon görevi düşürmek mümkündür. Bunun için öncelikli şart statü kullanımıdır. Sistem Altyapı Tanımları> Risk Bildirimi>Parametreler menüsü açılmalıdır. Buradaki parametre listesinden 22 no’lu “Statü kullanılsın mı?” Parametresi ‘Evet’ olarak işaretlenmelidir.
Tüm önlemler tamamlandığında sisteme otomatik revizyon düşürmek için öncelikle 185 no’lu parametre ‘Evet’ olarak düzenlenip kaydedilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/185-3effc5b7-0273-42ca-9370-38055f003add.png)

185 no’lu parametreye bağlı 2 durum söz konusudur. Kullanıcı, Revizyon statüsü kullanmadan otomatik revizyonun herhangi bir statüde görev olarak düşmesini istiyorsa,128 no’lu parametre değerine ilgili statünün kodu yazılmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/128-7d79fc2d-e842-407f-bc23-beab4d50611f.png)

128 no’lu parametre kullanıldığında süreç baştan başlayabileceği için, kullanıcı direkt kapatma ya da onaya sunmayı tercih ederek ayrı bir revizyon statüsü oluşturur.  Bu durumda da 126 no’lu parametreyi kullanılmalıdır.
Eğer alınan önlemler tamamlandıktan sonra direkt revizyon statüsüne geçilmesi isteniyorsa  126 no’lu parametrede parametre değeri alanına ‘revizyon statüsünün kodu’ yazılmalıdır. Bu durumda önlemler tamamlandığında süreç her ne aşamada olursa olsun ilgili kişiye revizyon statüsünde görev düşer.


![](https://docsbimser.blob.core.windows.net/imagecontainer/126-89a2e877-998a-4864-9f74-4ab6dee90a8a.png)

Bu kurguyu yaparken 93 no’lu parametre mutlaka ‘Hayır’ olarak işaretlenmelidir. Aksi takdirde sistem revizyon görevi değil, revize edilmesi için aksiyon görevi düşürecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/93-493994ca-fe54-4dbf-89e2-8db8c439125d.png)

Otomatik revizyon akışında 185 no’lu parametre değeri ‘Evet’ ise sistem ilk olarak 126 no’lu parametreye bakar, eğer 126 no’lu parametre değeri boş ise 128 no’lu parametre değerini kontrol eder. İkisi de boş ise varsayılan statüye göre otomatik revizyon çalışmaktadır.

