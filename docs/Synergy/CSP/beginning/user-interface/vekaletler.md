---
sidebar_label: Vekaletler
sidebar_position: 5
custom_edit_url: ""
---

# Vekaletler
- Vekalet, bir kişinin başka bir kişiye kendi adına iş yapabilmesi için belirli bir süre boyunca belirli yetkiler çerçevesinde verdiği yetkidir.
- Genellikle bu durum, çalışanın yıllık izin veya mazeret izni gibi işten geçici süreliğine uzaklaştığı durumlarda çalışan tarafından yürütülmesi gereken işlerin aksamaması için tercih edilir.
- Vekalet veren kullanıcı, vekaleti hangi yetkiler ile tanımlamışsa, vekalet verilen kullanıcı yalnızca tanımlanan yetkiler kapsamında işlem yapabilir.
- Vekalet verilen kişinin, vekalet veren kişi adına yaptığı işlerde (süreç başlatma, bekleyen kayıtlara onay verme gibi) işi yapan kişi kısmında, bu işin vekaleten gerçekleştirildiği detayı yer alır. Böylece geçmiş kayıtlara bakıldığında işlemin vekaleten mi yoksa işin gerçek sahibi tarafından mı yapıldığı ayırt edilebilir olur.
- Vekalet veren kullanıcının belirlediği vekalet bitiş süresi sonunda, sistem vekaleti otomatikman pasife düşürür ve vekalet verilen kullanıcının hesabından bu vekalet kaydı kaldırılır.
- Vekaletleri listeleme ve yönetme işlemleri yetkiye bağlıdır. Bir kullanıcının vekalet verebilmesi veya vekaletleri listeleyebilmesi için öncelikle ilgili kullanıcıya yetki verilmesi gerekir.


## Vekalet Yetkisi Tanımlama
Web arayüzüne, yetkili sistem kullanıcısı ile giriş yapılarak **Ayarlar** alanına tıklanır. Ayarlar kısmında listelenen **Güvenlik** ayarları seçilir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekalet-yetki-tanımlama-1-8169ace5-3ccd-4d7a-9a4d-271b419e4176.png)

Güvenlik ekranında, sistemde tanımlı tüm kullanıcılara, dahil oldukları sistem grupları bazında yetkiler tanımlanır. Vekalet yetkisi verilmek istenen kişinin dahil olduğu yetki grubuna tıklanarak **Sistem -> Vekalet** başlıkları altındaki **Listele** ve **Yönet** fonksiyonları ayrı ayrı yetkilendirilebilir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekalet-yetki-tanımlama-2-e69c0a68-a987-46dc-b3aa-39f5d669e4c7.png)


## Vekalet Oluşturma
Yetkisi olan kullanıcı, başka bir kullanıcıya vekalet vermek için web arayüzüne kendi kullanıcı adı ve şifresi ile giriş yapmalıdır. Giriş yapıldığında, profil panelindeki **Hesabım** alanına tıklanır.
![](https://docsbimser.blob.core.windows.net/imagecontainer/profil-22891b76-f026-457e-b2c9-5f62144783bd.png)

Profil panelinde bulunan **Hesabım** alanına tıklandığında gelen ekranda **“Vekaletler ve Erişim Anahtarları”** ayarlarına tıklanır. **Vekalet Listesi**  seçilir
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekalet-ve-erişim-anahtarları-ekranı-220f8a8b-bf6b-4933-a9dd-25bcc50d6f0e.png)

 **Vekalet Listesi** alanında **Yeni** butonuna tıklandığında, oluşturulacak vekaletin detay bilgilerinin girileceği bir ekran açılır.
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekalet-oluştur-modal-49e7a8da-2a4b-428d-adfb-b20370b8049d.png)

**Vekalet Edecek Kişi:** Yerine vekalet edecek kişi seçilir. Birden fazla seçim yapılamaz; her seferinde yalnızca bir kullanıcıya vekalet verilebilir;. Farklı kullanıcılara da vekalet verilmek istenildiğinde tekrardan vekalet oluşturulması gerekmektedir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/kullanıcı-ara-96bb6e45-2261-4ace-b0df-dab250a7c592.png)

**Vekalet Verilecek  Pozisyon:** Vekalet veren kişinin pozisyonudur. Bir kullanıcının birden fazla pozisyonu olabilir. Belirlenen pozisyonların üzerine gelen işleri devredebilmek için pozisyon bazında vekalet verilmesi sağlanabilir.  Akış tarafında pozisyon bazında yönlendirmeler yapabildiğimiz için kullanıcının onayına o pozisyon üzerinden giden süreçler için ayrı bir vekalet sağlanabilir. 

**Vekalet Tarihi:** Vekaletin geçerli olduğu tarih aralığını belirtir. Bir yıldan uzun süreli veya geriye dönük bir tarihe vekalet verilemez. 

**Vekalet Kapsamı:**
**`Basit`**
**Kullanıcı:**  Kullanıcı üzerindeki bütün yetkilerin aktarılabilmesi sağlanır.
**Proje:**   Vekalet veren kullanıcının erişebildiği uygulamalar üzerinden bir sınırlama yapılarak kullanıcıya vekalet verilebilir.

**`Gelişmiş`** 
Kırılımlı bir yapıda özelleştirilebilir bir yetki paketi düzenlenerek, vekaletin bu yetki çerçevesinde verilmesi sağlanabilir. Vekalet verilen kullanıcı; uygulama, menü, genel arayüzdeki belirli özellikler, doküman yönetimi  gibi belirli işlevlerle sınırlı olabilir. Bu şekilde, kullanıcının yetkilendirildiği alanlarda işlem yapmasına izin verilirken, diğer alanlarla ilgili herhangi bir müdahalede bulunması engellenir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekalet-oluştur-gelişmiş-1ffdce27-48d2-47c2-bfe4-08c48ae5a165.png)


**Vekalet Özeti:**
Vekaletin kapsamıyla ilgili bir özet gösterir.

Tamam dedikten sonra oluşturulan vekalet **Vekalet Listesi** alanında listelenmiş olur. Bu alanda varsa daha önceden verilmiş vekaletler de listelenir. Verilen bir vekalet düzenlenebilir, silinebilir.
Bu tabloda vekalet edecek kişi, vekalet tarihi, bitiş tarihi alanları bulunur. **Aktif** veya **Pasife** çekilmiş bir vekalet varsa seçilerek listelenir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekalet-listesi-6ba30a09-d34f-4475-be07-944c36deb9b2.png)


## Vekaleti Kullanma
Vekalet verilen kullanıcı web arayüzüne kendi kullanıcı adı ve şifresi ile giriş yaptığında profil alanından kendisine verilen vekalet kaydını görebilir. Kimin verdiği, ne bazda verdiği, geçerlilik tarihi gösterilir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/kullanıcı-ayarları-873a4df7-5d10-4b6e-9804-38899ef2e5a3.png)

Vekalet kaydına tıklandığında, bir uyarı penceresi açılır. Eğer kullanıcı "evet" derse, yeni bir sekmede vekalet veren kullanıcının web arayüzüne giriş yapılır. Bu arayüzde, tanımlanan vekalet yetkisi kapsamında, vekalet veren kişinin yerine işlem yapılabilmesi sağlanır. Profil alanında ismin yanında vekaleten geçmiş olduğunu göstemek amacıyla (vekaleten) yazmaktadır.
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekaletine-geç-19141de4-fad0-4bdf-acd6-495f103f6c2c.png)

## Vekalet Düzenleme
Vekalet ve Erişim Anahtarları ekranında **Vekalet Listesi** bölümünde, varsa daha önceden verilmiş vekaletler listelenir. düzenlenmek istenilen vekalet üzerine tıklanarak seçilir ve **Düzenle** butonu tıklanarak Vekaleti Düzenle penceresi açılır. burada vekalet oluşturmayla aynı işlemler yapılabilir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekalet-düzenle-69a5c7a6-3ab3-4414-b1f4-33db49fdffaf.png)


## Vekalet Silme
Vekalet ve Erişim Anahtarları ekranında **Vekalet Listesi** bölümünde, varsa daha önceden verilmiş vekaletler listelenir. silinmek istenilen vekalet üzerine tıklanarak seçilir ve **Geri Çek** butonuna tıklanır
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekalet-sil-a2491030-e01e-4011-84b3-305cf8069bc8.png)

Verilen input alanına istenilen yazı girilir
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekaleti-geri-çek-1-e2bfcd55-c99c-4f90-941a-2b149a530e0d.png)

Doğru yazıldığı takdirde **Geri Çek** butonu aktif olur ve tıkladığımızda vermiş olduğumuz vekaleti geri alırız.
![](https://docsbimser.blob.core.windows.net/imagecontainer/vekaleti-geri-çek-2-f25210e9-9f2f-465b-bdfa-58d13bc5619b.png)

Geri çekilen vekaletler **Pasif** alanında yer alır. Pasif olan vekaletler daha sonra tekrar aktife çekilemez. İstenirse kaldır butonuna basarak bu alandan da kaldırılabilir.
![](https://docsbimser.blob.core.windows.net/imagecontainer/pasif-vekaletler-b327953c-33ad-4d20-b9cb-9ce9b37729a1.png)
