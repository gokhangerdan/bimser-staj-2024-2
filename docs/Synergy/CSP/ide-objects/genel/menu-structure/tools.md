---
sidebar_label: Araçlar
sidebar_position: 4
custom_edit_url: ""
---

# Araçlar

Araçlar başlığı altında; **“Ayarlar”**, **“Bağlantılar”** ve **“İkon Bulucu”** alt başlıkları listelenir.

![Araçlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade94e907d-03bb-471c-9b74-26b9ce24ffad)

## Ayarlar

Ayarlar kısmına tıklandığında ekranda **“IDE Configs”** ve **“Flow Designer”** ayarlarının yapılabileceği bir popup açılmaktadır.

![Araçlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f018c64-fa96-4f42-ac41-428a8004ad3f)

Ayarlar ekranında Arama Çubuğu, Sıfırla, İçe Aktar ve Dışa Aktar işlev butonları bulunmaktadır. Bu butonlar sayesinde dışa aktarılmış olan bir config yapısı içe aktarılarak kullanılabilir ya da mevcut config ayarları dışa aktarılarak saklanabilir.

Ide config ayarları, geliştirme arayüzünün genel ayarlarının düzenlenebildiği alanları barındırır. Sağdaki ve soldaki pencerelerin başlangıç konumları, kaydetme tipi vb. arayüzle ilgili yapılandırılabilecek kısımların ayarları buradan yapılmaktadır.

Akış dizaynı kısmında ise akış ekranlarındaki genel düzenlemeler yapılabilir. Arka plan renkleri, yazı tipleri, bağlantı ayarları vb. gibi akış ekranı yapılandırmaları için genel ayarlamaların yapılabildiği alanları barındırır.

Akış ve ide ayarlarında yapılan düzenlemeler, ayarlar ekranının altında bulunan Tamam butonuna basılarak kaydedilebilir ya da İptal butonuna basılarak iptal edilebilir.

## Bağlantılar

Dış kaynaklardan veri çekip, projelerde ve sistem içinde kullanılmak üzere, dış kaynak bağlantı bilgilerinin tanımlandığı alandır.

![Araçlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8daf4c3-4bc1-4c95-9d9e-993318f06d7a)

Bağlantılar alanına tıklandığında; varsa daha önceden tanımlanmış bağlantılar ve bağlantı detay bilgilerinin bulunduğu bir panel açılacaktır. Ekranda bulunan “Ekle” butonu ile; **SQL**, **Oracle**, **MySQL**, **POSTGRESQL**, **Web Servis**, **ERP** ve **Rest** bağlantıları tanımlanabilir. Burada seçilen bağlantı türüne göre, kaynak sisteme bağlanmak için gerekli bilgilerin girileceği “Bağlantı Bilgileri” sekmesi, oluşturulan bağlantıya isim vermek için “Genel” sekmesi ve bağlantı için gerekli parametrelerin belirtildiği “Başlıklar” sekmesine girilen değerlerle bağlanılmak istenen kaynağın bilgileri tanımlanır. Tanımlama sonrası bağlantıya erişimin ve girilen bilgilerin kontrolü için ekranın sağ üst köşesinde bulunan “Test” butonuna basılır. Test sonucu başarılı ise bilgiler doğru ve kaynak sunucuya erişim sağlanıyor demektir. Tanımlanan bağlantının sistem içerisinde kullanılmak üzere kaydedilmesi için yine sağ üst köşede bulunan “Kaydet” butonuna basılır. Böylece bu kaynaktan çekilecek sorgu ve istek sonuçları sistem içerisinde kullanabilir hale gelir.

Geliştirme arayüzünde oluşturulan bir projenin **“DataSource”** klasörüne sağ tıklanıp, “Yeni Öğe” seçeneği ile, Bağlantı alanında oluşturulan kaynaktan veri çekilebilir, çekilen veri projenin kod kısımlarında ve DataSource kaynağı alan nesnelerinde kullanılabilir.

## İkon Bulucu

İkon Bulucu, geliştirme arayüzü tarafından sunulan, farklı birçok ikonun listesini içerir. İkon Bulucu kısmına tıklandığında ekrana ikonların listelendiği bir tablo yapısı açılacaktır.

![Araçlar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada19c21f1-2a13-4aeb-af97-7ca7e0a89d65)

Açılan tablo yapısında, ikon ismine göre arama yapılmasını sağlayan arama çubuğu bulunmaktadır. Ekranda herhangi bir ikona tıklandığında, tıklanan ikonun kodu panoya otomatik kopyalanır ve ikon özelliği kullanılabilecek nesnelere bu kopyalanan değer yapıştırılarak, ikon bulucunun sunduğu ikonların projelerde kullanılabilmesi sağlanmış olur.