---
sidebar_label: Uygulama Gezgini
sidebar_position: 7
custom_edit_url: ""
---

# Uygulama Gezgini

Geliştirme arayüzünde oluşturulan, başarıyla derlenen ve yayınlanan bir proje, kullanıma hazır demektir. Uç kullanıcıların, geliştirilen projeyi kullanabilmesi için projenin, web arayüzünde Uygulama Gezgini ekranından, uygulamalar menüsüne eklenmesi gerekir.

Uç kullanıcı, yetkisi olan uygulamaları, uygulamalar menüsünde görüp tıklayarak, ilgili formu açıp doldurabilir, yeni bir süreç başlatabilir veya rapor ekranlarına erişebilir.

Web arayüzüne yetkili bir kullanıcı ile giriş yapılarak **Ayarlar** menüsü altından Uygulama Gezgini ekranına ulaşılabilir.

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb62c9552-b32c-4831-b750-4d799907c1dc)

Uygulama Gezgini ekranı detaylarında bulunan **Ekle** seçeneği ile, uygulama menüsüne yeni bir kayıt eklenir. **Kaydet** seçeneği ile, uygulama menüsünde yapılan değişiklikler kaydedilir. **Kapat** seçeneği ile uygulama gezgini ekranı kapatılır.

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload17a023d0-cba1-4350-8d4d-9d97a4f39828)

Uygulama Gezgini işlemleri;

- Yeni Uygulama Düğümü Ekleme
- Yeni Profil Ekleme
- Profil Yetkilendirme 

ana başlıkları ile ele alınacaktır.

## Yeni Uygulama Düğümü Ekleme

Ekle seçeneğine tıklandığında ekrana, menüye eklenecek uygulamanın detaylarının girileceği bir pencere açılır. Ayrıntılar penceresi, **“Temel Bilgiler“, “Gelişmiş Parametreler”** ve **“Profiller”** olmak üzere 3 sekmeden oluşmaktadır.

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3ad0ae8-96af-4fec-a8cb-18e807f62c0b)

Temel Bilgiler sekmesinde;

- **Başlık :** Uygulamalar menüsünde görünecek uygulama adının girileceği kısımdır. Bu alanda çoklu dil desteği mevcuttur ve çoklu dil ikonuna tıklanarak uygulama adının, sistemde tanımlı diğer dillerdeki karşılıkları da girilebilir. Böylece arayüze giriş yapılan dile göre uygulama isimleri ilgili dil karşılıkları ile görüntülenecektir.

- **Panel Boyutu :** Menüden uygulama adına tıklandığında açılacak formun boyutunun belirlendiği kısımdır. Panel boyutu olarak 1,2,3 seçenekleri listelenir. 1 seçeneği ile form, ekranda daha az yer kaplarken, 3 seçeneği ile tam ekran açılır.

- **Sembol Rengi :** Uygulama menüsünde, uygulama adının başındaki sembol renginin belirlendiği kısımdır. Renk panelindeki seçeneklere göre uygulamalar istenilen renkte renklendirilebilir.

- **Düğüm İşlem Türü :** Bu alanda, hangi türde uygulama kaydı ekleneceğinin seçimi yapılmalıdır.

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf9447ec-798e-4c59-a483-bf6e01ac6c99)

</div>

***Yok*** seçeneği, ağaç yapısı oluştururken, aynı sürecin uygulamalarını veya benzer süreçleri tek bir başlık altında toplamak için, ana düğümde seçilen seçenektir. Düğüm işlem türü olarak “Yok” seçilen düğüme menü yapısında tıklandığında, bu düğümün altına eklenmiş diğer menü düğümleri açılacaktır.

> *Aşağıdaki örneğe göre; “Avans Talep Süreci” başlıklı kayıt için düğüm işlem türü “Yok” seçilmiştir.*

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e7d9ba2-05f4-4e19-bf1f-4ad5a147f664)

</div>

***Bir Akış Başlat*** seçeneği, geliştirme arayüzünde oluşturulmuş bir proje, menüden başlatılmak istendiğinde seçilir. Düğüm işlem türü olarak bu seçenek seçildiğinde ekranda, sistemde başarıyla yayınlanmış tüm projelerin listelendiği **“Projeler”** alanı ve seçilen projenin hangi akışına ait sürecin başlatılacağının seçileceği **“Akışlar”** alanı görünür olacaktır. Menüden, “Bir Akış Başlat” düğüm tipine tıklandığında, ilgili projeye ait form, akış başlatan adımında tanımlı aksiyon butonları ile birlikte açılır. Akışı başlatan formu doldurup, geliştirme esnasında belirlenen senaryoya göre akışı sonraki adıma ilerletir.

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8ba8a2d-05df-4d26-83cf-c61a0021f0d8)

</div>

***Bir Form Doldur*** seçeneği, geliştirme arayüzünde oluşturulmuş bir projeye ait formun web arayüzünde doldurulması istendiğinde seçilir. Formdaki alanlar doldurulup kaydedilerek, form verileri başka bir yerde kaynak verisi olarak kullanılabilir. Veya rapor olarak oluşturulan bir form menüye Form Doldur tipinde eklenebilir. Düğüm işlem türü olarak bu seçenek seçildiğinde ekranda, sistemde başarıyla yayınlanmış tüm projelerin listelendiği **“Projeler”** alanı ve seçilen projenin hangi formunun açılacağının seçileceği **“Formlar”** alanı görünür olacaktır.

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07978891-c5ce-43c6-b583-1dbd9538d9a0)

</div>

***Başlangıç, Doküman Yönetimi, İş Akış Yönetimi ve İnsan Kaynakları*** seçenekleri ile menüdeki temel web arayüz işlemlerinin gerçekleştirildiği düğümler, uygulama menüsüne eklenebilir.

***Dış Bağlantı*** seçeneği ise, harici bir adresi uygulama düğümüne bağlayarak, düğüme tıklandığında ilgili adresin açılması için kullanılan seçenektir. Bu seçenek seçildiğinde, link adresinin yeni sekmede mi yoksa panel üzerinde mi açılacağının seçilebileceği **“Dış Bağlantı Açma Tipi”** ve açtırılmak istenen adresin girileceği **“Dış Bağlantı”** alanları görünür olur.

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8642b8ab-39a1-4d4e-b182-e3c45e22a868)

</div>

***Kök Düğüm Ata :*** Bu seçenek, oluşturulan uygulama düğümünü direkt olarak uygulama menüsüne eklemek için ya da uygulama menüsünün altındaki başka bir düğümün altına eklemek için kullanılır. Bu seçenek pasif iken, uygulama direkt olarak uygulama menüsünün altına eklenir. Seçenek aktif edilip, alttaki seçim listesinden menüdeki herhangi bir düğüm seçilirse uygulama, seçilen menü düğümünün altına eklenmiş olur.

> *Aşağıdaki örneğe göre; “Avans Talep Formu” başlıklı düğüm için “Avans Talep Süreci” başlıklı kayıt, kök düğüm olarak seçilmiştir.*

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3473ac2-5023-4f13-90cb-cc9674088973)

**Gelişmiş Parametreler** sekmesinde, projenin akışına ya da formuna herhangi bir değeri parametre olarak göndermek için, parametre anahtarı ve değeri girilecek **Anahtar** ve **Değer** alanları mevcuttur.

> *Örneğin; Aynı süreç, uygulama menüsünde iki farklı menü düğümü olarak eklenmiş olsun. Sürecin akış kısmında ise tıklanan menü düğümüne göre akış farklı dallardan ilerletilecektir. Bu durumda aynı sürecin bağlandığı 1. menü düğümünde “X” anahtar değerine “1”, 2. menü düğümünde yine “X” anahtar değerine bu kez “2” değeri verilir. Sürecin akış kısmına ise parametre anahtar adıyla aynı, yani “X” isimli bir değişken nesnesi eklenerek özelliklerinden bu değişken nesnesi “Genel” işaretlenir. Karşılaştırma nesnesinde X isimli değişken karşılaştırılarak, değeri “1” ise, 1. menü düğümünden tıklandığı, “2” ise 2. menü düğümünden tıklandığı anlaşılmış olur.*

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62734b16-4953-4647-a96b-df37c508ce05)

</div>

Uygulama menüsüne eklenen bir kaydı, sistemdeki kullanıcıların görebilmesi için, öncelikle kullanıcıya ilgili uygulama düğümünün yetkisinin verilmiş olması gerekir. Uygulama düğümleri yetkilendirmesi profil tanımları ile gerçekleştirilir. Varsayılan olarak **“admin”** isimli profil tanımı mevcuttur. Uygulama Gezgini ekranındaki Profil alanından, yeni profiller eklenebilir. Bu profillerde hangi uygulamaların görünebileceği ve bu profillerin hangi kullanıcılara yetkilendirileceği de ayrıca tanımlanmalıdır.

**Profiller** sekmesinde; eklenecek uygulama düğümünün, hangi profil ya da profillerde görünür olacağının seçimi yapılır.

- **Alt Düğümler** kısmı, eğer eklenecek düğümün altında başka düğümler de olacaksa ve hepsinin aynı menü profillerinde görünmesi isteniyorsa aktif edilebilir.

- **Profiller** kısmında ise, tanımlı tüm menü profilleri listelenir. Eklenecek uygulamanın hangi menü profillerinde görünür olması isteniyorsa bu alandan ilgili menü profilleri seçimi yapılır.

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5a83a1a-4ed2-4c1b-8c0b-cf075cccb8d4)

</div>

Böylece seçilen profil, hangi sistem kullanıcılarına yetkilendirildiyse, o kullanıcılar uygulama menüsünde profile dahil edilen uygulama başlıklarını görebilirler.

## Yeni Profil Ekleme

Uygulama menüsünde bulunan düğümlerin görünürlüğü profil bazlı belirlenir. Bir uygulama düğümü sistemdeki tüm kullanıcılar tarafından görülebilirken, başka bir uygulama düğümünün yalnızca belirli kullanıcılar tarafından erişilebilmesi istenebilir. Bu yüzden eklenen her bir uygulama düğümünün, hangi menü profillerinde görünür olacağı belirlenmelidir.

Menüye eklenen uygulama düğümlerinin erişilebilirliğini profillerle yönetmek; yalnızca belirli bir kişi ya da departmanın erişmesi gereken uygulamaları yönetebilmek, özel bilgiler içeren rapor ekranlarının yalnızca yetkili kişiler tarafından görünebilmesini sağlamak gibi bir çok erişim kontrolüne imkan tanır. Böylece her kullanıcı, uygulama menüsünde yalnızca yetkili olduğu uygulama başlıklarını görebilir ve kullanabilir olur.

Başlangıçta varsayılan olarak **“admin”** isimli profil mevcuttur. “admin” profilinde aktif edilen uygulama düğümleri, “admin” profilinde yetkilendirilen tüm kullanıcılar tarafından uygulama menüsünde görünür.

Yeni bir menü profili eklemek için, Uygulama Gezgini ekranındaki **Profil** alanından **“Ekle”** butonuna tıklanır.

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0aa6ad4-68d3-4b2a-b6c8-90ec506e6fee)

Ekle butonuna tıklandığında yeni profilin bilgilerinin girileceği bir pencere açılır. Bu pencerede, **“Copy From”** butonuna tıklandığında yandaki liste aktif hale gelir ve bu listede, mevcut tüm menü profilleri listelenir. Yeni profil, var olan bir başka menü profilinden kopyalanarak oluşturulabilir ve istenirse üzerinde değişiklik yapılabilir. Sıfırdan bir menü profili oluşturmak için ise **No** ve **Başlık** alanlarına profil numarası ve başlığı bilgileri yazılarak, Tamam butonuna tıklanır.

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5a05e68-0444-4ff2-9f2a-a1e5792997bd)

</div>

Bu işlemden sonra, Uygulama Gezgini ekranındaki Profil listesine, yeni eklenen profil tanımının da geldiği görünür. Yeni eklenen profil bu listeden seçildiğinde, uygulama menüsüne ekli tüm kayıtlar pasif olarak gelecektir.

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbf5b97-5da5-4f0e-8174-01aabc32228a)

Seçili profilde görünür olması istenen uygulama kaydının detaylarına tıklanarak **“Düzenle”** denir.

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc85ca56d-74a9-468a-9ba7-c053d16b88b7)

Açılan düzenleme penceresinde Profiller sekmesine gelinir ve yeni eklenen profil tanımı da bu alandan seçilerek değişiklikler güncellenir.

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b3d4697-17fb-48c1-a5cf-3a2dedc63e9a)

İlgili uygulama düğümü, seçilen profilde aktif edildiğinde, menüde de aktif olarak görünecektir. Yapılan bu düzenleme, Uygulama Gezgini ekranından **“Kaydet”** butonuna basılarak kaydedilmelidir. Böylece, düzenlenen menü profilinin, yetki olarak verildiği kullanıcılar, uygulama menüsünde o profilde hangi uygulama düğümleri aktifse, onları görebilir ve kullanabilirler.

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3ee3c45-baf4-47cb-8023-6ac6a84356b4)

## Profil Yetkilendirme

Sistemdeki bir kullanıcı uygulamalar menüsünde, yetkisi dahilinde hangi uygulama başlıklarını görmesi gerekiyorsa, o uygulama başlıklarının aktif olduğu menü profili ile yetkilendirilmelidir.

Menü profili oluşturulup, profilde olması gereken uygulama başlıkları aktif edildikten sonra sıra, menü profilini kullanıcılara yetkilendirme aşamasına gelmiştir. Bu işlem, web arayüzünde Ayarlar menüsü altındaki **“Güvenlik”** kısmından yapılır.

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1679ebfd-cde2-4739-bf66-6aa8ed50f0ff)

Güvenlik ekranında, sol tarafta yetki düzenlemelerinin yapılacağı kullanıcı gruplarının listesi, sağ tarafta ise yetki tanımları ve yetkilendirme durumlarının olduğu kısımlar yer alır.

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e7a24c6-bcc7-4aa7-b9dd-6c45c23bfb30)

</div>

Yetki verilecek kullanıcı ya da kullanıcıları, bir grup içerisinde toplamak için **“Grup Ekle”** seçeneği ile yeni bir grup tanımı oluşturulur.

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac59f142-bbea-4f19-afc4-9370022dd1d0)

</div>

Yeni grup tanımı, Güvenlik ekranında gruplar listesine eklenmiş olarak görülür. Bu grup tanımına tıklanarak sağ taraftaki **“Üyeler”** sekmesinde gruba, kullanıcı, pozisyon, ünvan ya da departman üzerinden üye eklenir ve grup içeriği doldurulur.

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload293761c0-38dc-46a1-b015-6d45d24d21b8)

</div>

**Üye Oldukları** sekmesinde, ilgili grup başka bir gruba üye olarak seçilebilir. Bu durumda örneğin; X grubuna üye oldukları sekmesinden bir Y grubu eklendiğinde, Y grubunun yetkileri, X grubuna geçebilir. X grubundaki “Atanmamış” durumundaki tüm yetkiler Y grubundan alınır. X grubundaki “Atanmamış” durumu haricindeki yetkiler, X grubunda belirlenen yetki baz alınarak değerlendirilir.

**İzinler** sekmesinde, sistem üzerinde yetkilendirme yapılabilecek tüm alan ve işlem tanımları bulunmaktadır. Bu kısımda, uygulama profili yetkilendirmesi yapılacağı için, **Menü** başlığı genişletilir. Menü başlığı altında, Uygulama Gezgini alanında tanımlanan tüm menü profilleri listelenir. Oluşturulan gruba yetki olarak tanımlanacak menü profili için **“İzin Ver”** seçeneği seçilerek, gruptaki kullanıcıların uygulama menüsünü izin verilen profil içeriği ile görebilmesi sağlanmış olur. Sonrasında **“Değişiklikleri Kaydet”** butonu ile yetkilendirme işlemi tamamlanır.

<div style={{textAlign: 'center'}}>

![Uygulama Gezgini](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab721db8-6c54-4a7f-bf68-27b654458403)

</div>

Bir kullanıcı, farklı gruplar içine dahil edilmiş olabilir. Bu durumda, dahil edildiği tüm gruplarda izin verilmiş yetkilerin toplamından yararlanır.

**Örneğin;** “Ali Doğru” kullanıcısı, hem “Tüm Kullanıcılar” grubuna hem de “Muhasebe” grubuna dahil edilmiş olsun. “Tüm Kullanıcılar” grubunda **“Atanmamış”** olarak bırakılan bir yetki, “Muhasebe” grubunda **“İzin Ver”** olarak seçilmişse, “Ali Doğru” kullanıcısı o yetkiden yararlanır. Yani “İzin Ver” yetki durumu “Atanmamış” a baskındır. Ancak, “Tüm Kullanıcılar” grubunda **“İzin Ver”** olan bir yetki, “Muhasebe” grubunda **“İzin Verme”** olarak seçilmişse, bu kez kullanıcı o yetkiden yararlanamaz. “İzin Verme” yetki durumu baskındır.

## Kullanıcı Profillerine Özel Menü Ağaç Yapısı Oluşturma Dokümanı

Bu doküman, uygulamanızda kullanıcıların belirli kullanıcı profillerine özel menü ağaç yapıları oluşturabilmesi için izlenmesi gereken adımları ve gerekli bilgileri içermektedir. Menü oluşturma işlemi için temel bilgilerin alındığı bir modal form açılacaktır.

### Temel Bilgiler

![menuekle](https://docsbimser.blob.core.windows.net/imagecontainer/menuekle-fab55117-521f-4ef9-a954-66a10d3e5dab.png)

1. **Başlık (string)**: Menü öğesinin başlığını belirtir.
2. **Düğüm İşlem Türü (seçilebilir)**: Menü öğesinin gerçekleştireceği işlemi belirler. Aşağıdaki seçenekler mevcuttur:
   - Yok
   - Alt Panel
   - Bir Akış Başlat
   - Bir Form Doldur
   - Aksiyon Formu
   - Başlangıç
   - Doküman Yönetimi
   - İş Akış Yönetimi
   - Aksiyon Yönetimi
   - İnsan Kaynakları
   - Dış Bağlantı
   - eBA Entegrasyonu
3. **Menü İkon Arkaplan Rengi (string)**: Menü ikonunun arkaplan rengini belirtir.
4. **Menü İkonu (string)**: İkon seti içerisinden bir ikon seçilir.
5. **Başlangıçta Aç (boolean)**: Uygulama açılır açılmaz bu menünün açık olup olmayacağını belirler.
6. **Üst Menü (object)**: Parent node, yani üst menü öğesi seçilir.
7. **Sıra Numarası (number)**: Menü öğesinin sıralamasını belirler.
8. **Projeler (object)**: Açılacak projeyi seçer.
9. **Akış (object)**: Seçili projeden açılacak flow'u belirler.
10. **Form (object)**: Seçili projeden açılacak formu belirler.
11. **Dış Bağlantı Açma Tipi (seçilebilir)**: Dış bağlantının nasıl açılacağını belirler (Yeni Sekmede, Panel Üzerinde).
12. **Dış Bağlantı (string)**: Bir URL girilir.
13. **eBA Entegrasyon Türü (seçilebilir)**: Menü elemanı anahtarı, bekleyen işler veya geçmiş işler seçeneklerinden biri seçilir.
14. **eBA Entegrasyon Başlığı (string)**: eBA entegrasyonu için başlık girilir.

### Profiller Alanları

![profiles](https://docsbimser.blob.core.windows.net/imagecontainer/profiles-8155b20f-97ac-4925-85e0-f5c8c0cab0a6.png)

1. **Alt Düğümlere Uygula (boolean)**: Bu profil seçimini alt düğümlere de uygulamak için kullanılır.
2. **Profiller (object)**: Menüyü görmesini istediğimiz bir kullanıcı grubu seçilir.

### Gelişmiş Parametreler

![advanced](https://docsbimser.blob.core.windows.net/imagecontainer/adv-f59154f8-8119-4469-ab99-670dc1c24f73.png)

Gelişmiş Parametreler sekmesinde, projenin akışına ya da formuna herhangi bir değeri parametre olarak göndermek için parametre anahtarı ve değeri girilecek alanlar mevcuttur. 

Örneğin, aynı süreç uygulama menüsünde iki farklı menü düğümü olarak eklenmiş olsun. Sürecin akış kısmında ise tıklanan menü düğümüne göre akış farklı dallardan ilerletilecektir. Bu durumda aynı sürecin bağlandığı 1. menü düğümünde “X” anahtar değerine “1”, 2. menü düğümünde ise “X” anahtar değerine “2” değeri verilir. Sürecin akış kısmına ise parametre anahtar adıyla aynı, yani “X” isimli bir değişken nesnesi eklenerek, özelliklerinden bu değişken nesnesi “Genel” işaretlenir. Karşılaştırma nesnesinde X isimli değişken karşılaştırılarak, değeri “1” ise, 1. menü düğümünden tıklandığı, “2” ise 2. menü düğümünden tıklandığı anlaşılmış olur.

Bu doküman, uygulamanızda kullanıcıların belirli kullanıcı profillerine özel menü ağaç yapıları oluşturmasını kolaylaştıracak adımları ve gereksinimleri detaylı bir şekilde açıklamaktadır.

## Menü Önizleme Ekranı

![](https://docsbimser.blob.core.windows.net/imagecontainer/ugezgini-d88f0177-8872-4bd4-81dc-3caf490ad12d.png)

Bu doküman, uygulamanızda kullanıcıların oluşturdukları menü ağaç yapılarının önizleme ekranında nasıl gösterileceği ve bu ekranda sunulan işlevsellikleri detaylı bir şekilde açıklamaktadır. Bu önizleme ekranı, menü elemanlarının ilgili profillere göre nasıl göründüğünü test etmeyi ve yönetmeyi sağlar.

### Profil Alanı

Profil alanında aşağıdaki işlemler gerçekleştirilebilir:

1. **Profil Seçimi**: Profil seçimi yapılarak ilgili profilin hangi menü elemanlarını gördüğü test edilebilir.
2. **Yeni Profil Ekleme**: 
   - **Şuradan Kopyala**: Mevcut bir profilden menü elemanlarını kopyalama seçeneği.
   - **No**: Yeni profilin numarasını belirtir.
   - **Başlık**: Yeni profilin başlığını belirtir.
3. **Profil Düzenleme**: Mevcut profiller üzerinde değişiklik yapma imkanı sağlar.

### Menü Elemanı Yönetimi

Menü elemanının üzerindeki üç noktaya tıklandığında aşağıdaki seçenekler bulunur:

![](https://docsbimser.blob.core.windows.net/imagecontainer/3nokta-2942c8a9-65e0-4df4-878e-bc0ac10af498.png)

1. **Başlangıca Sabitle**: Menü ekranı açıldığında sabitlenen menüler alanında gösterilmesini sağlar.
2. **Düzenle**: Menü öğesini düzenlemek için modal form açar.
3. **Sil**: Menü öğesini tamamen siler.
4. **Profilden Kaldır**: Menü öğesini silmeden, sadece bu profilden kaldırır.

### İşlevlerin Detaylı Açıklamaları

#### Profil Seçimi

Profil seçimi ile kullanıcı, seçili profilin hangi menü elemanlarını gördüğünü test edebilir. Bu, farklı kullanıcı gruplarının menü elemanlarına erişimini simüle ederek doğrulama yapmayı sağlar.

#### Yeni Profil Ekleme

Yeni profil eklemek için kullanıcı aşağıdaki adımları izler:

![](https://docsbimser.blob.core.windows.net/imagecontainer/newprofile-3fcb8a6d-3dd3-4961-8dab-63aef5c13c72.png)

- **Şuradan Kopyala**: Mevcut bir profilin menü elemanlarını yeni profile kopyalar. Bu, benzer yapıdaki profillerin hızlı oluşturulmasını sağlar.
- **No**: Yeni profil için bir numara girilir.
- **Başlık**: Yeni profil için bir başlık girilir.

#### Profil Düzenleme

Profil düzenleme ile kullanıcı mevcut profillerin adını, numarasını veya menü elemanlarını değiştirebilir.

#### Menü Elemanı Üç Nokta Menüsü

- **Başlangıca Sabitle**: Bu seçenek, menü elemanının sabitlenen menüler alanında gösterilmesini sağlar. Uygulama açıldığında bu menü elemanı öncelikli olarak gösterilir.
- **Düzenle**: Menü elemanını düzenlemek için bir modal form açar. Bu formda menü elemanının tüm özellikleri güncellenebilir.
- **Sil**: Menü elemanını tamamen siler. Bu işlem geri alınamaz ve menü elemanı tüm profillerden kaldırılır.
- **Profilden Kaldır**: Menü elemanını silmeden, sadece seçili profilden kaldırır. Diğer profillerde menü elemanı var olmaya devam eder.

Bu doküman, uygulamanızda kullanıcıların menü ağaç yapılarının önizleme ekranında nasıl yönetileceğini ve test edileceğini detaylı bir şekilde açıklamaktadır. Bu ekran, kullanıcıların menü yapılarını profillere göre test etmesini ve yönetmesini kolaylaştırır.