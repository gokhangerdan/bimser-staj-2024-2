---
sidebar_label: Kural Yöneticisi Paneli
sidebar_position: 9
custom_edit_url: ""
---

# Kural Yöneticisi Paneli

Belirli bir şart sağlandığında, alınması istenen aksiyonlar Kural Yöneticisi panelinde tanımlanır.

Form ve form üzerinde bulunan nesnelerin, herhangi bir değerine göre, aynı veya farklı bir nesnenin özelliğini değiştirmek, değer atamak veya uyarı vermek gibi şart ve eylem kuralları, bu panelden yönetilir.

Örneğin;

- Form üzerindeki bir TextBox nesnesine girilen değer “XXX” ise, yine form üzerindeki CheckBox nesnesini seçili yap,
- Form üzerindeki ComboBox nesnesinden “001” değerli kayıt seçildiğinde, mesaj göster,
- Form üzerindeki NumberBox nesnesinin değeri 50 den büyükse ve CheckBox işaretliyse, formdaki TextBox nesnesine bir metin yazdır,
gibi pekçok kontrol, bu panelde tanımlanacak şart ve eylemlerle gerçekleştirilebilir.

Menüden, Görünüm başlığı altındaki “Kural Yöneticisi” ne tıklandığında panel, arayüze eklenecektir.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d13d292-80cc-4367-a299-1d0a3b99063a)

Panelde **“Yeni Kural”** seçeneği aktif olarak gelir. Bu seçeneğe tıklandığında, yeni kural tanımlama penceresi açılır.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddffc117b-e684-4541-8ae1-a5fd1b50c512)

Kural tanımlama penceresi; koşul veya koşulların tanımlandığı **Koşul**, tanımlanan koşul gerçekleştiğinde hangi eylemin oluşacağının belirlendiği **Eylem** ve bu kuralın hangi zaman diliminde çalıştırılacağının belirlendiği **“Uygulama Zamanı”** şeklinde 3 bölümden oluşur.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf847f5f3-57fc-4733-9c17-215f96503c7c)

**“Koşul Ekle”** butonuna tıklandığında, Koşul alanına bir **“IF”** koşulu oluşur. Bu if koşulunun altına, **“Add Group”** diyerek **AND – OR** operasyon satırları eklenebilir. **“Else If”** veya **“Else”** gruplarıyla farklı şartlar ve eylemler tanımlanabilir.

Aynı kuralın içerisinde tanımlı If-Else blokları sırasıyla çalıştırılır. “Else-If” veya “Else”, kendinden bir önceki If şartının Else ifadesi olacak şekilde çalışır.

Her bir “If”, “Else If” ve “Else” ifadesi için, belirtilen koşul sağlandığında hangi eylemin gerçekleşmesi isteniyorsa, Eylem kısmında oluşturulan ilgili eylemin seçimi yapılmalıdır.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a7e28d1-0e89-495a-8816-ed0749b84142)

Add Group seçeneğine tıklandığında, şarta bir **AND** operasyonu eklenir. And operasyonunda ise **“Grup Ekle”** ve **“Koşul Ekle”** seçenekleri listelenir.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8c78aa3-af3e-44d1-9b29-9900e90ea65e)

**“Grup Ekle”** seçeneği ile yeni AND – OR operasyonları aynı şartın altına oluşturulur. AND operasyon tanımına tıklanarak AND seçeneği, OR olarak değiştirilebilir.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadccb428b8-7909-43cf-be0f-276d8f0588b5)

**“Koşul Ekle”** seçeneği ile, ilgili operasyon içerisine koşullar eklenebilir.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade96a4bbc-25f1-48ec-8f1d-4ef80341f7e1)

Koşul satırına tıklandığında, form ve form üzerinde bulunan nesneler listelenir. Listelenen nesnelerin detaylarına gidildiğinde, koşul olarak hangi nesne özelliği kullanılmak istenirse onun seçimi yapılmalıdır.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6d7a6d3-05d3-431d-be0d-ef22cf0c7f12)

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4eaceca8-de6d-420d-9167-99a47359aa59)

Örneğin; “TextBox1’in değeri “XXX” ise” gibi bir koşul oluşturulmak istendiğinde, bu alanda **“TextBox1.value”** seçeneği seçilmelidir.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a711555-a0a8-4519-992b-a43f9c06820e)

Koşul değeri karşılığının sabit bir değer ile mi yoksa form üzerindeki başka bir nesnenin, herhangi bir değerine göre mi karşılaştırılacağı koşul seçenekleri butonu ile belirlenir.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42f2a1af-0a70-4a58-9fa8-1ba2e5b539db)

Burada seçenek olarak, **Değer Girişi (Value Entry Condition)** seçilirse, koşul karşılığına sabit bir değer girilmelidir.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada949bce1-4384-41a4-97df-475a3bd25d4b)

Seçenek olarak, **Alan Seçimi (Field Selection Condition)** seçilirse, koşul karşılığı olarak formdaki bir nesnenin herhangi bir değeri seçilebilir. Örneğin; Form üzerinde TextBox1 ve TextBox2 olarak iki adet nesne bulunsun. “TextBox1 in değeri, TextBox2 nin değerine eşitse” gibi bir koşul için, bu seçenek seçilir ve koşul karşılığı olarak TextBox2 nin Value değeri seçimi yapılır.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1a039da-c611-4a1f-941f-173664e64eb4)

Karşılaştırma operatörleri metin ifadeler için; **“Eşit”**, **“Eşit Değil”**, **“Boş”**, **“Dolu”**, **“İle Başlayan”**, **“İle Biten”**, **“İçeren”** ve **“İçermeyen”** şeklindedir. Sayısal ifadeler için listelenen karşılaştırma operatörleri ise; **“Eşit”**, **“Eşit Değil”**, **“Boş”**, **“Dolu”**, **“Büyük”**, **“Büyük Eşit”**, **“Küçük”** ve **“Küçük Eşit”** şeklindedir.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16466011-b1de-495e-ae55-153543dde24a)

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7c95141-fba6-48f0-bfe3-e23fd2146107)

- **“if(TextBox1.Value == “A” && NumberBox1.Value == 1)”** ifadesi, koşul kısmında aşağıdaki gibi belirtilir.

<div style={{textAlign: 'center'}}>

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc7b2a36-a5ef-4c22-9ef7-6276d3216bd3)

</div>

- **“if(TextBox1.Value == “A” && (TextBox1.Enabled == true || Checkbox1.Value == false))”** ifadesi, koşul kısmında aşağıdaki gibi belirtilir.

<div style={{textAlign: 'center'}}>

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload344eb0dd-182f-465b-937a-8968afb1bf83)

</div>

Eklenen koşullar sağlandığında, gerçekleştirilmek istenen aksiyonlar, **Eylemler** kısmında tanımlanır. **“Yeni Eylem”** butonuna tıklanarak, ilgili koşul sağlandığında **“Mesaj Gösterme“**,  herhangi bir nesnenin, herhangi bir değerine **“Girdi ile Değer Atama”** veya herhangi bir nesnenin, herhangi bir değerine **“Seçim ile Değer Atama”** seçenekleri ile eylemler tanımlanabilir.

<div style={{textAlign: 'center'}}>

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b41d964-23b8-45fd-89f4-ea47211d4dd9)

</div>

Eylem olarak “Mesaj Gösterme” seçildiğinde;

<div style={{textAlign: 'center'}}>

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ee1af1d-c9f2-4742-a90a-2699bdbbd187)

</div>

- **Adı :** Eylem adının yazıldığı alandır. Birden çok eylem tanımlanabildiği için eylemin adı bu kısımda belirtilir.
- **Mesaj :** Koşul sağlandığında gösterilmek istenen mesaj metni bu alana yazılır.
- **Mesaj Tipi :** Bu alanda, **“Mesaj Gösterme”** ve **“Onay”** seçenekleri listelenir. Mesaj Gösterme seçeneği ile, koşul sağlandığında ekranda ilgili mesaj metninin görünmesi sağlanır. Onay seçeneğinde ise, yazılan mesaj metninin, koşul sağlandığında onaylama penceresinde gösterilmesi sağlanır. Onaylama penceresinde Tamam ve İptal butonları bulunur.
- **Diyalog Tipi :** Mesajın ekranda **Popup**, **Toaster** veya **Summary** mesaj şeklinde gösterilmesi bu alandan belirlenir.
- **Uyarı Tipi :** Bu alanda ise mesajın tipi belirlenir. **Başarılı (Success)**, **Hata (Error)**, **Uyarı (Warning)** ve **Bilgi (Info)** seçenekleri listelenir.

Tanımlanan eylem ilgili koşulda seçildikten sonra, önizleme ekranında veya web arayüzde koşul sağlandığında mesaj gösterme eyleminin gerçekleştiği görülür.

**Örneğin;** Form üzerindeki Checkbox1 nesnesi işaretlendiğinde, bir mesaj metninin görünmesi istenirse, Koşul alanında **“CheckBox1.Value”** değeri **“true”** mu diye kontrol edilir. Eylem kısmında mesaj gösterme eylemi tanımlanır. Tanımlanan eylem koşul alanında seçilir ve ardından Kaydet butonuna basılır.

<div style={{textAlign: 'center'}}>

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9035fdd5-0a00-4af0-9b32-9ed339b71430)

</div>

Koşul sağlandığında mesaj metni aşağıdaki gibi gösterilir.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13298d15-d749-4d92-8848-99c0a903da37)

Eylem olarak “Girdi ile Değer Atama” seçildiğinde;

<div style={{textAlign: 'center'}}>

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c186115-a877-474f-8468-f10e44cdfbe1)

</div>

- **Adı :** Eylem adının yazıldığı alandır. Birden çok eylem tanımlanabildiği için eylemin adı bu kısımda belirtilir.
- **Hedef :** Koşul alanında belirtilen durum sağlandığında, form ya da form nesnelerinin herhangi bir özelliğine değer atanmak istenebilir. Hedef kısmında form ve form üzerindeki nesnelerin tüm özellikleri listelenir. Değer ataması yapılmak istenen özellik bu alandan seçilmelidir.
- **Değer :** Atanacak değer ifadesi bu alana yazılır.

**Örneğin;** Form üzerindeki NumberBox1 nesnesinin değeri 50 den büyükse, formdaki TextBox1 nesnesine “Sınır Aşıldı” metnini yazdıralım. Koşul alanında, **“NumberBox1.Value 50 den büyükse”** koşulu tanımlanır. Eylem kısmında, Hedef olarak **“TextBox1.Value”**, Değer olarak ise **“Sınır Aşıldı”** metni yazılır. Tanımlanan eylem, ilgili koşul satırında seçildikten sonra kural Kaydedilir.

<div style={{textAlign: 'center'}}>

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33b0628c-38d5-43c8-801a-b42af6ef3111)

</div>

Önizleme ekranında veya arayüzde koşul sağlandığında, tanımlanan eylemin gerçekleştiği görülür.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85c1f0f8-2ba7-4f2e-be13-705172b277d5)

Eylem olarak **“Seçim ile Değer Atama”** seçildiğinde;

<div style={{textAlign: 'center'}}>

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22ec5036-c61f-43fc-b0f5-107d72dda642)

</div>

- **Adı :** Eylem adının yazıldığı alandır. Birden çok eylem tanımlanabildiği için eylemin adı bu kısımda belirtilir.
- **Hedef :** Koşul alanında belirtilen durum sağlandığında, form ya da form nesnelerinin herhangi bir özelliğine değer atanmak istenebilir. Hedef kısmında form ve form üzerindeki nesnelerin tüm özellikleri listelenir. Değer ataması yapılmak istenen özellik bu alandan seçilmelidir.
- **Değer :** Bu alanda da form ve form üzerindeki nesnelerin tüm özellikleri listelenir. Hangi nesnenin hangi özellik değeri hedef özelliğe atanmak isteniyorsa, bu alandan seçimi yapılmalıdır.

**Örneğin;** NumberBox1 nesnesinin değeri 50 ise, TextBox2 nesnesinin görünürlüğü, Checkbox1 nesnesinin seçim durumuna bağlı olsun. Yani Checkbox1 seçili ise TextBox2 form üzerinde görünsün, seçili değilse görünmesin. Böyle bir senaryo için, koşul kısmında **“NumberBox1.Value değeri 50 mi”** koşulu tanımlanır. Eylem kısmında ise, Hedef alanında **“TextBox2.Visible”**, Değer kısmında ise **“CheckBox1.Value”** seçilir. Tanımlanan eylem, ilgili koşul satırında seçildikten sonra kural Kaydedilir.

<div style={{textAlign: 'center'}}>

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc3a6f97-b707-4e9f-9662-b303f08e0530)

</div>

Önizleme ekranında veya arayüzde koşul sağlandığında, tanımlanan eylemin gerçekleştiği görülür.

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c06a637-cf7b-4ff5-8e45-8b4750bb5e3b)

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9031a425-cf52-4a0d-ac27-20ac9effda88)

Uygulama zamanı alanında; **“Yüklendiğinde”**, **“Değiştiğinde”** ve **“Kaydedildiğinde”** seçenekleri listelenir. Bu seçenekler, yazılan kuralın, hangi anda çalıştırılacağını belirlemek için kullanılır. Yazılan kuralın form yüklendiği anda çalıştırılması isteniyorsa “Yüklendiğinde”, formda bir değişiklik yapıldığında çalışması isteniyorsa “Değiştiğinde” veya form kaydedilirken çalışması isteniyorsa “Kaydedildiğinde” seçeneğinin uygulama zamanı olarak seçilmesi gerekir.

Aynı uygulama zamanında çalışacak birden çok koşul, tek bir kuralın içine yazılabilir. Farklı uygulama zamanlarında çalışacak birden çok koşul için, farklı uygulama zamanlarında çalışan kurallar tanımlanmalıdır.

Tek kuralda birden çok koşul ve eylem tanımı örneği;

![Kural Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3cbcaaae-1b23-492a-a025-f694ff22d565)