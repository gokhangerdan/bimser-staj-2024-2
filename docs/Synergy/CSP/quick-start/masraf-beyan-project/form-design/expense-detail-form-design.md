# Masraf Detay Formu Tasarımı
Masraf Beyan Formunda bulunan Masraf Bilgileri tablosuna satır eklemek için kullanıcının yönlendirileceği bu formun başlıca alanları aşağıdaki gibidir;

|	| 	|
|--- |--- |
|Masraf Tipi :|Masrafların hangi türde gerçekleştiğini belirten alandır ve parametrik formdaki tabloda kayıtlı verilerden seçilir|
|Fiş Tarihi :|Masrafa ait fişin kesildiği tarihtir|
|Kişi Sayısı :|Kaç kişinin masraf talebinde bulunduğunu belirten alandır|
|Masraf Tutarı :|Girilen masrafa ait tutarın girildiği alandır|
|Açıklama :|Masrafa ilişkin detaylı açıklamanın girilebileceği alandır|
|Dokümanlar :|Masrafa ilişkin dokümanların(fiş, fatura fotoğrafı vb.) eklenebileceği alandır|

Formu oluşturmak için öncelikle çözüm gezgininde Forms klasörü üzerinde sağ tıklanarak **CSP App Form** seçilir ve açılan pencereden form için “MasrafDetayFormu” şeklinde bir Dosya Adı girilir.
![detay form olusturma](https://docsbimser.blob.core.windows.net/imagecontainer/detay%20form%20olusturma-1c7949c6-4daa-4e11-a1cc-9667d0cfad12.png)

Masraf Tipi alanı için, kullanıcının belirli türlerde masraf tiplerinden seçim yapabilmesi beklenir, bu seçimin gerçekleştirilebilmesi için de forma bir **ComboBox** nesnesi eklenir.
![masraf tipi combobox](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20tipi%20cbx-17786c7c-6b18-42f4-a676-7444416a5d24.png)

Masraf tiplerinin, geliştirme sırasında belirlenmesi yerine belirli kullanıcılar tarafından eklenebilir ve düzenlenebilir olması uygulamanın daha dinamik bir yapıda olabilmesini sağlayacaktır. Bunun için bu alanda seçilebilecek veriler başka bir parametrik formdan alınacaktır.

Bu işlem için [**Masraf Tipleri Parametrik Formu**](expense-types-parametric-form-design.md) tasarlanır.

Masraf Tipleri Parametrik Formunun Tasarımı gerçekleştirildikten sonra Masraf Detay Formundaki ComboBox alanında MasrafTipleriniGetir sorgusundan gelen verilerin gösterilebilmesi için ComboBox nesnesinin özelliklerinden **DataSource** özelliğinde bu sorgu seçilir.

Sorgu seçildikten sonra DataSource özelliğinin altında **Value Expression** ve **Display Expression** olarak yeni alanlar açılır. Arka planda tutulması istenen değer için Value Expression alanında **Id** kolonu, Kullanıcıya görünmesi istenen değerler için Display Expression alanında ise **MasrafTipi** kolonu seçilir.
![masraf tipi combobox value-display](https://docsbimser.blob.core.windows.net/imagecontainer/masraftipi%20combobox%20value%20display-9eeb4950-09b7-4b17-ad36-93cbc6ceac22.png)

Fiş Tarihi alanı için **DateTimePicker** nesnesi forma eklenir. Nesne özelliklerinde Behavior sekmesi altındaki **Format** alanından gün-ay-yıl-saat içerebilmesi için **YYYY-MM-DD HH:mm** seçilir. **Show Time** seçeneği aktif edildiğinde nesnede saat seçim alanı da aktif edilir.

![fis tarihi](https://docsbimser.blob.core.windows.net/imagecontainer/fistarihi-a298c773-cf2f-41b7-b3a8-fd1deaa0a59a.png)

Kişi sayısının girilebileceği alan için **NumberBox** nesnesi forma eklenir. Geçerli olabilecek minimum değer için **Min** alanı 1 olarak değiştirilebilir, maksimum değer için de 10 olarak bir değer verilebilir. Kişi sayısı tam sayı olması gerektiğinden ondalıklı sayılar için virgülden sonrasını ifade eden **precision** alanı 0 olarak bırakılmalıdır.
![kisi sayisi](https://docsbimser.blob.core.windows.net/imagecontainer/kisi%20sayisi-d2db159c-d263-4ab8-a39a-2fd5c5d0c907.png)

Masraf Tutarı alanı için de forma tekrar bir NumberBox nesnesi eklenir. Masrafın negatif değerlere düşmesi mümkün olmadığı için Minimum girilebilecek değer için Min değeri 1 olarak verilmelidir. Binlik ayracının açılabilmesi için **Use Thousand Seperator** özelliği aktif edilir. Alanın hemen yanında bulunan yukarı ve aşağı yönlü oklara tıklanarak veya yön tuşları kullanılarak değer, **Step** özelliğine girilen miktar kadar arttırılıp azaltılabilmektedir.
![masraf tutari](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20tutari-a5d8edf1-e8e4-4995-ad78-bf9add564e3e.png)

Kullanıcının yaptığı masrafa ilişkin detayları yazabileceği **Açıklama** alanı için forma bir **TextArea** nesnesi eklenir. Nesne özelliklerinden giriş yapabileceği metnin karakter sınırı için **MaxLength** özelliğine 250 değeri verilebilir. Kullanıcının, girebileceği kalan karakter sayısının gösterilebilmesi için **Show Character Counter** özelliği aktif edilir.
![masraf detay aciklama](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20detay%20aciklama-05120b86-cb11-4fe2-9739-05c161047f4a.png)

Yapılan masrafa ait dokümanların(fiş, fatura fotoğrafı vb.) eklenebileceği** Dokümanlar** alanı için **DocumentMetaData** nesnesi forma eklenir. Nesne Forma eklendikten sonra doküman eklenebilmesi, silinebilmesi ve görüntülenebilmesi için gerekli özellikler varsayılan olarak aktif halde gelir. Nesneye resim türünde dosya eklendiğinde, dosyanın uzantı ikonunun yerine küçük resim olarak gösterilmesi istenirse **Show Content For Image Files** özelliği aktif edilmelidir.

Bu özelliğin kullanılabilmesi için **Show File Extension Icon** özelliğinin aktif olması gereklidir.

Nesne üzerine eklenen dokümanın Doküman Yönetiminde kaydedilmesi isteniyorsa **Save Path (DM)** özelliğinde bir dosya yolu tanımlanması gerekmektedir.

![masraf detay doküman](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20detay%20dok%C3%BCman-91e69e4c-37d4-4cf5-a79f-108d597534bf.png)

Masraf Tipi alanında **“Diğer”** seçeneği işaretlendiğinde Açıklama alanının, kullanıcı için doldurulması zorunlu bir alan olabilmesi sağlanabilir. Bunun için Masraf Detay Formunun Olaylarından **OnBeforeSave** seçilir. 

Masraf Tipi alanına karşılık gelen “ComboBox1” nesnesinden seçilen item’ın value değeri eğer 4 ise ve Açıklama alanına karşılık gelen “TextArea1” nesnesinin içeriği boş ise kullanıcıya uyarı verilir ve formun kaydedilmesi engellenir.
![masraf tipi diger](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20tipi%20diger-374c9cb7-689b-45c8-8b1a-8dd1878f5dad.png)

:::info BİLGİ
TextArea1 nesnesinin text alanı form yaratıldığında bu alan varsayılan olarak “undefined” değerde gelmektedir. Doldurulup silindikten sonra ise boş(“”) değer taşımaktadır. ComboBox1’in value değeri veri kaynağındaki Id değerine karşılık gelmektedir ve masraf tiplerinden “Diğer” seçeneğinin Masraf Detay Tablosundaki Id değeri 4‘tür.
:::

Tüm alanlar oluşturulduğuna göre Masraf Detay Formu, Masraf Beyan Formundaki Masraf Detay Tablosu ile ilişkilendirilmeye hazır hale gelmiştir.
