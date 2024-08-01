---
sidebar_position: 1
custom_edit_url: ""
---

# Ünvan

Ünvan nesnesi, akış içerisinde bir ünvan değerini saklamak için kullanılan nesnedir. İçeriği sabit olarak belirlenebileceği gibi akış sırasında dinamik olarak da değiştirilebilir.

Ünvan nesnesi içeriğine değer atamak için Atama nesnesi, ünvan nesnesindeki değeri karşılaştırmak için Karşılaştırma nesnesi ile birlikte kullanılabilir.

Akış tasarımında Ünvan nesnesinden ok çıkarılmaz veya başka bir nesneden çıkan ok Ünvan nesnesine bağlanmaz. Ünvan nesnesi sadece ünvan bilgisini saklamak amacı ile kullanılır.

Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

![Resim1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa18b542-57f9-4b7a-9645-5884b8439e85)

Ünvan nesnesine tıklandığında Özellik Görüntüleyici panelinde **“Görünüm”** ve **“Özellikleri”** sekmeleri bulunmaktadır.

 

## Görünüm

### Metin Ayarları


- `Nesne Adı` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

- `Başlık` - Nesnenin başlık metninin girildiği alandır.

- `Kilitleme` -  Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

- `Boyut` -   Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.


## Özellikleri
 
### Değer

Ünvan nesnesinin başlangıç değerinin ayarlanacağı sekmedir. Bu sekmede, ünvan nesnesine sabit bir değer verilebilir.

- `Tip` - Ünvan nesnesinde tutulacak ünvan değerinin seçildiği alandır. Tip alanında **“Sabit Ünvan”** ve **“Akış Başlatan Ünvanı”** olarak iki seçenek listelenmektedir.

![Resim1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c4d2fcf-f5f0-40a0-aae8-a35a9005c1ab)

- `Sabit Ünvan` - Tip alanından **“Sabit Ünvan”** seçeneği seçildiğinde, sistemde tanımlı tüm ünvan kayıtlarının listelendiği bir ünvan seçimi alanı açılacaktır. Bu alandan seçilen ünvan tanımı, Ünvan nesnesinde saklanmış olur.
- `Akış Başlatan Ünvanı` -Tip alanından **“Akış Başlatan Ünvanı”** seçeneği seçildiğinde, Ünvan nesnesi, akışı başlatan kullanıcının ünvanını saklamış olur.