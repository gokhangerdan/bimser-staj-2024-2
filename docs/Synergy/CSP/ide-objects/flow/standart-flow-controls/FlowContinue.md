---
sidebar_position: 3
custom_edit_url: ""
---

# Akış Devam Ettirici

Akış Devam Ettirici nesnesi, tasarlanan projeler üzerinde akıştaki bir nesnede sürecin beklediği durumda kod yazılmadan ilgili sürecin bir sonraki adıma ilerletilmesini sağlayan nesnedir.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Akış Devam Ettirici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e658c25-8bf9-43a4-8e1a-b37d82b2b07e)

Akış Devam Ettirici nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

## Appearance

### Text Configs 

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Status

`ProcessId` - Devam ettirilecek akışın süreç numarasının tanımlandığı alandır, statik veya akışta kullanabilecek liquid veriler tanımlanabilir.

Örneğin ilerletilecek süreç numarası Değişken nesnesi içinde bulunuyorsa alana **{{DeğişkenAdı.Value}}** şeklinde tanım yapılmalıdır.

`ObjectName` - Devam ettirilecek akıştaki nesne adının yazıldığı alandır.

Örneğin devam ettirilecek süreçte Akış Durdurucu nesnesi üzerindeki bekleyen isteğin iletilmesi isteniyorsa, nesnenin adı ObjectName alanına tanımlanmalıdır.

:::caution DİKKAT

Tanımlama yapılırken nesnenin başlık bilgisi girilmemelidir.

:::

`EventId` - ObjectName alanında yazılan nesnede tanımlı hangi event üzerinden sürecin ilerletileceğinin belirlendiği alandır.

Örneğin ObjectName alanında Akış Durdurucu nesnesi tanımlı ve nesnede Onayla (Identity=5) ve Reddet (Identity=6) eventleri bulunuyor olsun. EventId alanında nesnenin Onayla bağlantısından ilerlenmesi istendiğinde Onayla eventine ait Identity numarası  yazılmalıdır.

:::tip İPUCU

![Akış Devam Ettirici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc30b241c-4784-4542-a3cb-5a318740d5c0)

Resimdeki akış senaryosunda akışı başlatan kullanıcı Gönder olayı üzerinden süreci gönderdiğinde akış Akış Durdurucu nesnesi üzerine gelir ve süreç bu adımda dışarıdan bir müdahale yapılana kadar beklemeye başlar.

Akışı başlatan kullanıcı bekleyen bir sürece ait süreç numarasını formdaki NumberBox nesnesine girip süreci Onayla olayı üzerinden ilerlettiğinde, süreç Akış Devam Ettirici nesnesine gelir. Nesnenin ProcessId alanında süreç numarası verisi için formdaki NumberBox nesnesinin seçildiği Değişken nesnesinin liquid ifadesi yazılmıştır. ObjectName alanında Akış Durdurucu nesnesinin Name alanındaki adlandırılması tanımlanmış olup, EventId bölümünde ise Akış Durdurucu nesnesine ait Onayla olayının Identity değeri girilmiştir.

:::

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![Akış Devam Ettirici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4044da8f-6b87-41db-814d-b9e889e760c4)

:::

## Events

Akış Devam Ettirici nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Events sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Events sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![Akış Devam Ettirici](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bf5520b-0daa-41cf-b1a0-af28abb76b72)