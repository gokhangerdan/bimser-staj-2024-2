---
sidebar_label: Erişim Anahtarları
sidebar_position: 6
custom_edit_url: ""
---

# Erişim Anahtarları
- Erişim anahtarları, bir kullanıcının hesabına başka bir kullanıcı tarafından token aracılığıyla giriş yapılabilmesini sağlayan bir sistemdir.
- Erişim anahtarı, bir kullanıcının ürettiği benzersiz bir anahtardır.
- Başka bir kullanıcıyla, kullanıcı adı ve şifre bilgilerini paylaşmak yerine, belli bir yetki çerçevesinde oluşturulabilecek bir anahtardır.
- Bu sistem vekalet sistemiyle karıştırılmamalıdır. Vekalet sisteminde, yerine geçilen kullanıcı için işlemleri vekalet edenler yaparken, erişim anahtarı ile yapılan işlemlerde **asli kullanıcı**nın kendi işlemi olarak geçmektedir.
- Erişim anahtarları, vekaletlere benzer bir özelliktir. Aradaki fark şudur: vekaletlerde, vekalet bilgisi arka planda tutulmaktadır. Yani bir kullanıcı bir işi yaparken veya bir süreç üzerinde onayda bulunurken, vekalet veren kullanıcı adına bu bilgi akış tarihçesinde gösterilmektedir (örneğin, "şu kişi vekaleten şunun yerine" gibi). Dolayısıyla, erişim anahtarı ile vekalet arasındaki fark burada ortaya çıkmaktadır. 
- Vekalet üzerinden giriş yapılan uygulamalarda ve süreçlerde belli bir takım kontroller ve validasyonlar sağlanabilir. İşlem yapan kişilerin bilgileri süreç arşivinde gösterilebilir. Erişim anahtarları ise daha çok o kullanıcının doğrudan yerine geçildiği bir durumu ifade eder.

## Erişim Anahtarı Yetkisi Tanımlama
------
Web arayüzüne, yetkili sistem kullanıcısı ile giriş yapılarak **Ayarlar** alanına tıklanır. Ayarlar kısmında listelenen **Güvenlik** ayarları seçilir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekalet-yetki-tanımlama-1-8169ace5-3ccd-4d7a-9a4d-271b419e4176.png)

Güvenlik ekranında, sistemde tanımlı tüm kullanıcılara, dahil oldukları sistem grupları bazında yetkiler tanımlanır. Erişim Anahtarı yetkisi verilmek istenen kişinin dahil olduğu yetki grubuna tıklanarak **Sistem -> Erişim Anahtarı** başlıkları altındaki **Listele** ve **Yönet** fonksiyonları ayrı ayrı yetkilendirilebilir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/yetki-tanımlama-91ec785d-f45d-42f1-94c5-25e959499a89.png)


## Erişim Anahtarı Oluşturma
------
Yetkisi olan kullanıcı, erişim anahtarı oluşturabilmek için web arayüzüne kendi kullanıcı adı ve şifresi ile giriş yapmalıdır. Giriş yapıldığında, profil panelindeki **Hesabım** alanına tıklanır.
![](https://docsbimser.blob.core.windows.net/imagecontainer/profil-22891b76-f026-457e-b2c9-5f62144783bd.png)

Profil panelinde bulunan **Hesabım** alanına tıklandığında gelen ekranda **“Vekaletler ve Erişim Anahtarları”** ayarlarına tıklanır. **Erişim Anahtarları**  seçilir
![](https://docsbimser.blob.core.windows.net/imagecontainer/anahtar-olusturma-yeni-5f0e69f2-e38a-487c-84a0-f257878eb4fd.png)

 **Erişim Anahtarları** alanında **Yeni** butonuna tıklandığında, oluşturulacak olan erişim anahtarının detay bilgilerinin girileceği bir ekran açılır.
![](https://docsbimser.blob.core.windows.net/imagecontainer/anahtar-olusturma-modal-6e50a4c2-c6a8-405a-8b1e-03d0d230af85.png)


**`İsim:`**  Erişim anahtarına verilecek isim girilir.

**`Başlangıç/Bitiş Tarihi:`**  Erişim anahtarının geçerli olduğu tarih aralığını belirtir. Tarihler en fazla bir yıl sonrasına kadar belirlenebilir ve geçmişe yönelik tarih girilemez.

**`Yetki Kapsamı:`** 
**`Basit`**
**Kullanıcı:**  Kullanıcı üzerindeki bütün yetkilerin aktarılabilmesi sağlanır.
**Proje:**   Erişim anahtarını oluşturan kullanıcının erişebildiği uygulamalar üzerinden bir sınırlama yapılarak yetki kapsamı oluşturulur.
**`Gelişmiş`** 
Kırılımlı bir yapıda özelleştirilebilir bir yetki paketi düzenlenerek, erişim anahtarının bu yetki çerçevesinde oluşturulması sağlanabilir. Erişim anahtarına sahip olan kullanıcı; uygulama, menü, genel arayüzdeki belirli özellikler, doküman yönetimi  gibi belirli işlevlerle sınırlı olabilir. Bu şekilde, kullanıcının yetkilendirildiği alanlarda işlem yapmasına izin verilirken, diğer alanlarla ilgili herhangi bir müdahalede bulunması engellenir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/anahtar-olusturma-gelismis-a5ba1b9a-8b70-4f10-9a66-2d5a58242d9c.png)


Tamam dediğimizde anahtarın oluşturulduğu ve kopyalanabileceği yeni bir pencere açılır. Bu anahtar herhangi bir yerde saklanmaz; pencere kapatıldıktan sonra bu anahtara yeniden erişim mümkün değildir. Anahtarı tekrar üretmek mümkündür, ancak aynı olmayacaktır. Erişim anahtarı arayüzde herhangi bir yerde kayıtlı tutulmadığı için güvenli bir yerde saklanması faydalı olacaktır. Ancak daha sonra ihtiyaç olması halinde, "Yeniden Üret" butonu tıklanarak yeni bir anahtar üretilebilir. Yeni üretilen anahtar, ilgili kullanıcıyla tekrardan paylaşılmalıdır.

### Erişim Anahtarını Yeniden Üretme
Daha önce üretilen erişim anahtarına ulaşılamadığında, yeni bir anahtar üretmek için kullanılır. Yeni bir anahtar oluşturulduğunda eski anahtar kullanılamaz hale gelir. Pasif veya süresi dolmuş erişim anahtarları yeniden üretilemez
![](https://docsbimser.blob.core.windows.net/imagecontainer/anahtar-liste-yeniden-uret-bdd28f1b-e1d2-403c-b533-c1367c75963f.png)

Oluşturulan erişim anahtarları Erişim Anahtarları penceresinde listelenir. Bu alanda, anahtarın ismi, sona erme tarihi ve durumu yer almaktadır. Durum sütununda "Aktif", “Süresi Dolmuş”, "Aktif/Süresi dolmak üzere" veya "Pasif" ifadeleri bulunur. Aktif fakat süresi dolmak üzere olan anahtarlar için süre sonuna yaklaşıldığından dolayı, anahtarı oluşturan kullanıcıya her gün "Süresi dolmak üzere" şeklinde bir uyarı e-postası gönderilir. **Pasife** çekilmiş erişim anahtarını listelemek için Sadece alanından pasif seçilir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/anahtar-liste-2ddd621c-2dd4-4252-85a8-7168f1efcd2e.png)

## Erişim Anahtarını Kullanma
------
Giriş ekranında, giriş türünün seçildiği alanda **Erişim Anahtarı** seçeneği seçilir ve erişim anahtarı buraya girilerek giriş sağlanır. Vekaleten değil, bizzat o kişi olarak hesabına giriş yapılmış olur.
![](https://docsbimser.blob.core.windows.net/imagecontainer/anahtar-ile-giriş-f1526008-cf11-4d59-b736-7bac9c65b711.png)

Ayrıca, süreçleri geliştirirken kullandığımız ve takvimli iş yapabilecek şekilde organize edebildiğimiz bir "scheduler" bölümümüz vardır. Bu bölüm, belli aralıklarda belli aksiyonlar alınması istendiğinde kullanılır; örneğin, her gün belli bir saatte akış başlatmak veya belli bir servise istek göndermek gibi.  Bu işlemler için erişim anahtarı gereklidir, çünkü erişim anahtarı olmadan scheduler çalıştırılamaz. Erişim anahtarları giriş ekranında ve scheduler tarafında kullanılır.


## Erişim Anahtarını Düzenleme
------
Vekalet ve Erişim Anahtarları ekranında **Erişim Anahtarları** bölümünde, varsa daha önceden oluşturulmuş erişim anahtarları listelenir. düzenlenmek istenilen erişim anahtarının isim kolonunları üzerindeki 3 noktaya tıklanarak menü açılır ve **Düzenle** seçilir. Erişim Anahtarını Düzenle penceresi açılır. burada erişim anahtarı oluşturmayla aynı işlemler yapılabilir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/anahtar-liste-düzenle-dae3f3ea-9c87-4a1c-bfef-6e4d7814562a.png)

## Erişim Anahtarını Silme
------
Vekalet ve Erişim Anahtarları ekranında **Erişim Anahtarları** bölümünde, varsa daha önceden oluşturulmuş erişim anahtarları listelenir. silinmek istenilen erişim anahtarı seçilir ve **Geri Çek** butonuna tıklanır
![](https://docsbimser.blob.core.windows.net/imagecontainer/anahtar-sil-1c4e9d2a-21f3-4f51-9e00-4de2b3878fb0.png)

Verilen input alanına istenilen yazı girilir. Doğru yazıldığı takdirde **Geri Çek** butonu aktif olur ve tıkladığımızda oluşturmuş olduğumuz erişim anahtarını geri çekmiş oluruz.
![](https://docsbimser.blob.core.windows.net/imagecontainer/anahtar-sil-modal-d86cfdee-2842-4836-8eb5-96fa2fcad248.png)

Geri çekilen erişim anahtarı **Pasif** alanında yer alır. Pasif olan erişim anahtarı daha sonra tekrar aktife çekilemez. İstenirse kaldır butonuna basarak bu alandan da kaldırılabilir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/anahtar-liste-pasif-c16f331a-9c62-4d0d-b726-43f367d04943.png)

