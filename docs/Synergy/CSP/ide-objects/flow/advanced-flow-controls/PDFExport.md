---
sidebar_position: 2
custom_edit_url: ""
---

# PDF’e Aktar 

PDF’e Aktar nesnesi, proje formlarının PDF tipinde dosyaya çevrilmesi amacı ile kullanılır. Oluşturulan dosya, sistem içerisinde Doküman Yönetim Sistemi’nde saklanabilir ve akış içerisinde kullanıcılara iletilebilir.

:::caution DİKKAT

Proje formlarının PDF dosyasına çevrilmesi için, verilerin aktarılacağı şablon word dosyası hazırlanarak sistemde Doküman Yönetimi içine yüklenmelidir. Word şablonu içinde form nesnelerinin Name'leri kullanılarak liquid değişken etiketleri yazılır. (*{{Lookup1.Value}} gibi*)

**[Nesnede kullanılacak örnek Word şablonunu indirmek için tıklayın](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2eb294e-4a30-4763-9ad0-f6441b0db73e)**

:::

Araç kutusu panelinden PDF’e Aktar nesnesi sürüklenip akış üzerine bırakılır. Akış tasarım ekranında bulunan nesneye tıklandığında, Özellik Görüntüleyici panelinde, nesne özellikleri görünür.

PDF’e Aktar nesnesine tıklandığında Özellik Görüntüleyici panelinde "Appearance", "Properties" ve "Events" sekmeleri bulunmaktadır.

![PDF’e Aktar](https://docsbimser.blob.core.windows.net/imagecontainer/pdf-word-template.docx)
 
## Appearance

### Text Configs

`Object Name` - Nesnenin sistem tarafında kullanılacak ismidir. Kod tarafında nesneye, nesne adı alanında yazan değerle erişim sağlanır.

`Caption` - Nesnenin başlık metninin girildiği alandır.

`Is Lock` - Tasarım anında nesnenin yeri değiştirilmesin isteniyorsa bu alan aktif edilir.

`Size` - Nesnenin genişlik ve yükseklik ayarlarının yapıldığı kısımdır.

## Properties

### Value

`Type` - PDF’e Aktar nesnesinin tipinin alfanumerik mi, numerik mi yoksa lojik bir değer mi olacağı bilgisi bu sekmeden ayarlanır. Type alanında; Metin, Tam sayı, Ondalık sayı, Tarih, Para ve Doğru/Yanlış tipleri listelenmektedir.

`Value Type` - Sabit bir değer verilmek isteniyorsa değer türü olarak “Sabit seğer” seçeneği seçilmektedir.

`Value` - Value Type alanında seçilen Sabit değerin tanımlandığı alandır.

### Action

`Continue If Error Occurs` - Süreç PDF’e Aktar nesnesinden geçtiğinde nesne metodunun içinde yazılan kod bloğu çalıştırılıp, bu kodda herhangi bir hata ile karşılaşıldığında, web ara yüzünde sürecin hata vermeden devam etmesi isteniyorsa işaretlenir.

`Error Description Object` - PDF’e Aktar nesnesi kodlarında bir hata ile karşılaşıldığında, hatanın detaylı metninin atandığı bir Değişken nesnesi bu alandan seçilmektedir.

### Account

`Impersonation` - PDF’e Aktar nesnesinin "Properties" sekmesinde yapılan ayarlamalar, nesnenin Execute olayında sistem tarafından koda dönüştürülmektedir. Bir proje formunun PDF dosya tipine aktarılması sırasında kod tarafında bir bağlantı açılır. Açılan bu bağlantının sistem kullanıcısı yerine akıştaki bir pozisyon nesnesi tarafından oluşturulması ve PDF dosyasının bu pozisyon nesnesinde bulunan kişi tarafından oluşturulduğu görünmesi isteniyorsa bu alan işaretlenir.

`Creator` - Alan içerisinde akış tasarımında bulunan, Pozisyon nesneleri listelenir. PDF dosyasının, hangi nesne kullanıcısının oluşturması isteniyorsa bu alandan ilgili nesnenin seçimi yapılır.

### Documents

`Documents` - Kaynak olarak seçilen, dönüştürme işleminde kullanılacak formun bulunduğu doküman nesnesinin seçildiği alandır.

`Constant Document` - Documents alanında seçilen form verilerin aktarılacağı şablon Word dosyasının Doküman Yönetimi içinde seçildiği alandır.

![PDF’e Aktar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e3df0d7-4208-4c58-8e78-47b1ca150aee)

![PDF’e Aktar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a4ed7a9-802d-49e7-9696-2cec18567a6f)

:::danger UYARI

Documents içindeki formların Name bilgileri ve Constant Document içinde seçilen Word şablonu üzerindeki etiketler eşleşmelidir, aksi takdirde Word dosyası üzerine veriler aktarılamaz ve PDF içeriği hatalı oluşur.

:::

### Export Page Size

`Custom Page Size` - Oluşacak PDF formunun boyutları bu alanda belirlenir. Eğer özel sayfa boyutu değerleri girilmek isteniyorsa bu alan aktif edilir. Alan aktif edildiğinde ekrana; Page Type (sayfa türü), Unit (birim), Width (genişlik), Height (yükseklik) ve Margin (kenar) verilerinin girilebileceği alanlar aktif hale gelir.

`Page Type` - Oluşturulacak PDF’in boyutunun seçildiği alandır.

> Yapılabilecek seçimler: Özel, A3, A4, A5, B4, B5, EnvelopeDL, Executive, Folio, Ledger, Legal, Letter, Quatro, Statement, Tabloid, Paper10x14, Paper11x17

`Unit` -  Width ve Height alanlarında gösterilen değerlerin hangi tipde görünmesi için kullanılır. Listelenen değerler Piksel, Santimetre, Milimetre ve İnç’tir.

`Width` - Seçilen sayfa türüne ait genişliği gösterir. Custom sayfa türü haricindeki diğer türlerin genişliği sabittir.

`Height` - Seçilen sayfa türüne ait yüksekliği gösterir. Custom sayfa türü haricindeki diğer türlerin yüksekliği sabittir.

`Margin` - Oluşturulacak PDF’nin sayfa kenarlarında ne kadar boşluk olacağının belirlendiği alandır.

### Export Page Number

`Show Page Number` - Oluşturulacak PDF dokümanının sayfalama özelliklerinin girildiği alandır, pasif olarak gelmektedir. Aktif hale geldiğinde diğer özellikler görünür hale gelir.

`Show Page Number on the First Page` - Show Page Number özelliği aktif hale getirildiğinde görünür hale gelmektedir. Seçili olduğu durumda PDF’in ilk sayfasında sayfa numarası yazı halde dosya üretilir.

`Page Number Position` - Show Page Number özelliği aktif hale getirildiğinde görünür hale gelmektedir. Sayfa numarasının bulunması istenen yer bu panelden ayarlanmaktadır. 

> Yapılabilecek seçimler: Sol üst, Üst merkez, Sağ üst, Sol alt, Alt merkez, Sağ alt

`Custom Font` - Show Page Number özelliği aktif hale getirildiğinde görünür hale gelmektedir. Farklı bir yazı tipi kullanılması isteniyor ise aktif hale getirilmelidir.

`Font` - Custom Font aktif hale getirilince görünen alandır. Font tipi, büyüklüğü, rengi, kalın (bold), sağa yatık (italik) ve alt çizgi (alt çizgi) seçenekleri bulunmaktadır.

### Export Page Header

`Show Page Header` - Oluşturulacak PDF dokümanının başlık (header) bilgilerinin girildiği alandır, pasif olarak gelmektedir. Aktif hale geldiğinde diğer özellikler görünür hale gelir.

`Show on the First Page` - Show Page Header aktif hale getirildiğinde görünür hale gelmektedir. İçerik alanına girilen başlık bilgisinin ilk sayfada görünmesi isteniyorsa seçilir.

`Type` - Show Page Header aktif hale getirildiğinde görünür hale gelmektedir. Başlık alanına eklenmesi istenen verinin ne türde olacağını belirlemek için kullanılır. 

> Yapılabilecek seçimler: Metin, HTML, Görsel

`Content` - Show Page Header aktif hale getirildiğinde görünür hale gelmektedir. Başlık alanına yazılacak olan verinin girişi için kullanılır. Type alanında seçilen değer göre içerik alanının görünümü değişir. Type alanında Metin ve HTML seçimlerinde Content alanına ifade girişi yapılması gerekirken, Görsel seçildiğinde Doküman Yönetimi seçimi paneli açılmaktadır.

`Show Bottom Border` - Show Page Header aktif hale getirildiğinde görünür hale gelmektedir. Aktif hale getirildiğinde, içerik alanı içine girilen bilginin altında bulunan bir çizgi eklenir.

`Show Left Border` - Show Page Header aktif hale getirildiğinde görünür hale gelmektedir. Aktif hale getirildiğinde, içerik alanı içine girilen bilginin sol tarafında bulunan bir çizgi eklenir.

`Show Right Border` - Show Page Header aktif hale getirildiğinde görünür hale gelmektedir. Aktif hale getirildiğinde, içerik alanı içine girilen bilginin sağ tarafında bulunan bir çizgi eklenir.

`Show Top Border` - Show Page Header aktif hale getirildiğinde görünür hale gelmektedir. Aktif hale getirildiğinde, içerik alanı içine girilen bilginin üst tarafında bulunan bir çizgi eklenir.

`Custom Font` - Başlık içinde girilen bilginin farklı bir yazı tipi kullanılması isteniyor ise aktif hale getirilmelidir.

`Font` - Custom Font aktif hale getirildiğinde görünür hale gelmektedir. Font tipi, büyüklüğü, rengi, kalın (bold), sağa yatık (italik) ve alt çizgi (alt çizgi) seçenekleri bulunmaktadır.

### Export Page Footer

`Show Page Footer` - Oluşturulacak PDF dokümanının alt bilginin (footer) girildiği alandır, pasif olarak gelmektedir. Aktif hale geldiğinde diğer özellikler görünür hale gelir.

`Show on the First Page` - Show Page Footer aktif hale getirildiğinde görünür hale gelmektedir. İçerik alanına girilen alt bilginin ilk sayfada görünmesi isteniyorsa seçilir.

`Type` - Show Page Footer aktif hale getirildiğinde görünür hale gelmektedir. Alt bilgi alanına eklenmesi istenen verinin ne türde olacağını belirlemek için kullanılır.

> Yapılabilecek seçimler: Metin, HTML, Görsel

`Content` - Show Page Footer aktif hale getirildiğinde görünür hale gelmektedir. Alt bilgi alanına yazılacak olan verinin girişi için kullanılır. Tip alanında seçilen değer göre içerik alanının görünümü değişir. Type alanında Metin ve HTML seçimlerinde Content alanına ifade girişi yapılması gerekirken, Görsel seçildiğinde Doküman Yönetimi seçimi paneli açılmaktadır.

`Show Bottom Border` - Show Page Footer aktif hale getirildiğinde görünür hale gelmektedir. Aktif hale getirildiğinde, içerik alanı içine girilen bilginin sol tarafında bulunan bir çizgi eklenir.

`Show Left Border` - Show Page Footer aktif hale getirildiğinde görünür hale gelmektedir. Aktif hale getirildiğinde, içerik alanı içine girilen bilginin sol tarafında bulunan bir çizgi eklenir.

`Show Right Border` - Show Page Footer aktif hale getirildiğinde görünür hale gelmektedir. Aktif hale getirildiğinde, içerik alanı içine girilen bilginin sağ tarafında bulunan bir çizgi eklenir.

`Show Top Border` - Show Page Footer aktif hale getirildiğinde görünür hale gelmektedir. Aktif hale getirildiğinde, içerik alanı içine girilen bilginin üst tarafında bulunan bir çizgi eklenir.

`Custom Font` - Alt bilgi içinde girilen bilginin farklı bir yazı tipi kullanılması isteniyor ise aktif hale getirilmelidir.

`Font` - Custom Font aktif hale getirildiğinde görünür hale gelmektedir. Font tipi, büyüklüğü, rengi, kalın (bold), sağa yatık (italik) ve alt çizgi (alt çizgi) seçenekleri bulunmaktadır.

### Export Options

`Begin From a New Page for each Document` - Documents alanı içine birden fazla Doküman nesnesi eklendiğinde, bir Doküman nesnesi içindeki PDF dosyası oluşturulduğunda örneğin dosya sayfanın yarısında tamamlandığında; ikindi Doküman nesnesinden PDF oluşurken sayfada kalınan yer yerine yeni bir sayfada başlayarak oluşmasını sağlayan ayardır.

`Show Page Border` - Seçili hale getirildiğinde, PDF’de sayfanın dört tarafına sınırı gösteren çizgi (margin) eklenir.

`Add Watermark` - Oluşturulacak PDF üzerinde filigran bulunması isteniyorsa aktif hale getirilir. Aktif hale geldiğinde filigran ayarları görünür hale gelir.

`Watermark Source` - Add Watermark seçeneği aktif hale getirildiğinde görünür. Belge üzerinde kullanılmak istenen filigranın seçilmesinde kullanılır. Doküman Yönetimi seçimi paneli açılarak kullanılacak filigranın bulunduğu dizine gidilerek filigran seçilmelidir.

`Image Scale (%)` - Add Watermark seçeneği aktif hale getirildiğinde görünür. Eklenen filigranın belge üzerindeki büyüklüğünün ayarlanması bu seçenek ile yapılır.

`Image Rotation (Degress)` - Add Watermark seçeneği aktif hale getirildiğinde görünür. Eklenen filigranın belge üzerindeki döndürülmüş olarak görünmesi isteniyorsa bu seçenek ile yapılır.

`Image Transparency (%)` - Add Watermark seçeneği aktif hale getirildiğinde görünür. Eklenen filigranın belge üzerindeki saydamlık oranı değiştirilmek isteniyorsa bu seçenek ile yapılır.

`Add Watermark to the First Page` - Add Watermark seçeneği aktif hale getirildiğinde görünür. Eklenen filigranın çok sayfalı belgelerde, belgenin ilk sayfasında da gözükmesi isteniyorsa seçilmelidir.

### Export Properties

`Caption` - Oluşturulan PDF’in doküman özelliklerindeki başlık kısmında bulunacak bilginin girildiği alandır.

`Subject` - Oluşturulan PDF’in doküman özelliklerindeki konu kısmında bulunacak bilginin girildiği alandır.

`Keywords` - Oluşturulan PDF’in doküman özelliklerindeki anahtar kelimeler kısmında bulunacak bilginin girildiği alandır. Anahtar kelimeler dokümanın aranmasında yardımcı olur.

`Author` - Oluşturulan PDF’in doküman özelliklerindeki dokümanı oluşturan kısmında bulunacak bilginin girildiği alandır.

`Add Create Date` - Oluşturulan PDF’in doküman özelliklerinde doküman oluşturma tarihi kısmına eklecek tarihin olup olmayacağının belirlendiği alandır.

### Export Security

`Security Enabled` - Dışarı aktarılacak olan PDF üzerinde güvenlik ayarı bulunması isteniyorsa aktif hale getirilir.

`User Password` - Security Enabled seçeneği aktif hale getirildiğinde görünür. PDF’in görüntülenmeden önce kullanıcılar tarafından şifre girilmesi ve ardından görüntülenmesi isteniyorsa kullanılır.

`Owner Password` - Security Enabled seçeneği aktif hale getirildiğinde görünür. Şifrelenmiş PDF’te belge sahibine kullanıcılardan farklı olarak şifre verilmesi isteniyorsa kullanılır.

`Printing` -  Security Enabled seçeneği aktif hale getirildiğinde görünür. Belgenin kullanıcılar tarafından yazdırılması engellenmek isteniyorsa, Printing özelliği seçimi yapılmamalıdır.

`Document Assembly` - Security Enabled seçeneği aktif hale getirildiğinde görünür. Belgenin başka bir belgenin parçası olarak kullanılması veya belgeye sayfa eklenmesine izin verilmek isteniyorsa, Document Assembly özelliği seçilmelidir.

`Content Copying` - Security Enabled seçeneği aktif hale getirildiğinde görünür. Belge içeriğinin kopyala-yapıştır (Ctrl+C – Ctrl+V) ile kopyalanmasına izin verilmek isteniyorsa, Content Copying özelliği seçilmelidir.

`Commenting` - Security Enabled seçeneği aktif hale getirildiğinde görünür. Belge içeriğine yorum eklemesine izin verilmek isteniyorsa, Commenting özelliği seçilmelidir.

`Filling  of form Fields` - Security Enabled seçeneği aktif hale getirildiğinde görünür. Belge içeriğine doldurulabilen alanlara yazı yazılmasına izin verilmesi isteniyorsa, Filling  of form Fields özelliği seçilmelidir.

`Content Copying for Accessibility` - Security Enabled seçeneği aktif hale getirildiğinde görünür. Ekran okuyucu yazılımların PDF dosyasını okumak için PDF dosyasındaki metni kullanmasına izin verilmesi isteniyorsa, Content Copying for Accessibility özelliği seçilmelidir.

`Degraded printing` - Security Enabled seçeneği aktif hale getirildiğinde görünür. Kullanıcının belgenin yazdırılırken, taramalı görüntü olarak yazdırması isteniyorsa, Degraded printing özelliği seçilmelidir.

`Modifying content` - Security Enabled seçeneği aktif hale getirildiğinde görünür. Kullanıcının belge içeriğini değiştirmesine izin verilmek isteniyorsa, Modifying content özelliği seçilmelidir.

### Export

`Path` - PDF’in kaydedilmesi istenen dosyanın seçildiği bölümdür. Path özelliği yanındaki üç noktaya tıklanarak, Doküman Yönetiminde dosyanın kaydedileceği dizin seçimi yapılabilir.

`Naming Format` - PDF'in kaydedilmesi esnasında kullanılacak isim formatının belirlendiği bölümdür. {{ProcessId}}, {{ProjectName}} gibi önceden tanımlı liquid değişken verileri kullanılabileceği gibi akıştaki Değişken nesne içeriği de dosya adlandırılmasında kullanılabilmektedir. (Örneğin Masraf-{{Variable1.Value}} gibi)

> Yapılabilecek seçimler: {{ProcessId}}, {{FlowStarter.FirstName}}, {{FlowStarter.LastName}}, {{CreatedDate}}, {{CreatedTime}}, {{Title}}, {{Subject}}, {{Keywords}}, {{Author}}, {{ProjectName}}, {{ProcessName}}, {{ProcessCaption}}

`Assign File to the Flow Document Objects` - Dönüştürme sonra elde edilen PDF dosyasının akış üzerinde kullanılması isteniyorsa seçenek aktif hale getirilmelidir.

`Flow Document` - Assign File to the Flow Document Objects seçeneği aktif hale getirildiğinde görünür. Dönüştürme sonrası PDF dosyasını akıştaki farklı doküman nesnesine atamak için kullanılır.

:::info BİLGİ

Nesne üzerinde ekli özelliklerin doğru olduğu sistem tarafından kontrol edilmektedir. Eksik bir özellik bulunduğunda nesne üzerinde kırmızı ünlem ikonu gösterilerek, fare işaretçisi ile ikon üzerine gelindiğinde nelerin eksik veya hatalı olduğu görüntülenebilmektedir.

![PDF’e Aktar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf13178d4-e517-48d6-bf3f-6fcd3afc8b88)

:::

## Events

### Events

PDF'e Aktar nesnesinin sahip olduğu olaylar, Özellik Görüntüleyici panelindeki "Events" sekmesinde yer almaktadır. Her bir olay, farklı çalışma anlarında tetiklenerek kendilerine özgü işlemleri gerçekleştirir. Bu olaylara geliştirici tarafından yazılan kodlar da ilgili olayın tetiklendiği anda çalıştırılır. Herhangi bir olaya kod yazmak için, Olaylar sekmesinden ilgili olay satırına çift tıklanır. Ekran, “Akışadı.cs” isimli akış kod editörü kısmına yönlendirilir ve tıklanan olaya ait method bloğu otomatik olarak oluşturulur. Geliştirici bu method içerisinde istediği kod bloğunu kurgulayabilir. Olaylar sekmesinden tıklanarak kod tarafında methodu oluşturulmuş olayın yanında, method adı bilgisi otomatik oluşturularak, olayla method arasındaki ilişki belirtilmiş olur.

![PDF’e Aktar](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60a7e99d-f347-4d17-8b89-77dcd054bce5)

`OnBeforeExecution` - Akış PDF’e Aktar nesnesinden geçmeden önce tetiklenen olaydır.

`OnAfterExecution` - Akış PDF’e Aktar nesnesinden geçtikten sonra tetiklenen olaydır.

`Execute` - Akış, PDF’e Aktar nesnesinden geçtiğinde, nesnenin “Execute” olayı tetiklenmekte ve bu olay içerisinde yazan kod bloğu çalışmaktadır. Olaya çift tıklandığında nesneye ait kod metodu bloğu otomatik olarak akış tarafında oluşturulur.

:::tip İPUCU

Execute event'i içinde oluşturulacak PDF belgesi içine eklenecek verilere müdahale edebilirsiniz.

```csharp
public void ExportToPDF1_OnBeforeExecution(object sender, OnBeforeExecutionArguments args)
{
    ExportToPDF1.ExternalParameters = new System.Collections.Generic.Dictionary<string, object>();
    ExportToPDF1.ExternalParameters.Add("Subject", "Yeni konu");
    ExportToPDF1.ExternalParameters.Add("Yazar", "John Doe");
    // örnek olarak word şablon dosyası üzerindeki {{Subject}} parametresine kod ile değer belirlemek istendiğinde 
    // yukarıdaki satırlar gibi kullanım sağlanır varsa daha önceki değer yok sayılır.
    // Bu şekilde form elemanları haricinde de pdf ye değer gönderebilmiş oluruz.
}
```

:::