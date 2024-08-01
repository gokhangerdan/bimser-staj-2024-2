# Çoklu Dil Desteği

Bu döküman eBA İş Akışı ve Döküman Yönetim sistemi için çoklu dil özelliği kazandırma ile ilgili bilgileri içermektedir.

### 1. Sisteme yeni bir dil ekleme

eBa Üzerinde yeni dil için tarafınıza ekiplerimiz tarafından ulaştırılan Xml'i Sisteme eklemek istediğiniz dile uygun bir biçimde doldurmanız gerekmektedir . 



![](https://docsbimser.blob.core.windows.net/imagecontainer/t1-ea420833-753e-4171-bd2a-d8244c85c7ca.png)

Web arabiriminden giriş yapılırken giriş yapılacak dil seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c3-011731af-5f67-4970-89ef-16ffffb8d775.png)

Workflow designer aracı üzerinden dosya sekmesinden “Dil seçimi ” ile geliştirme yapılan dil değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c4-9fce7462-4971-438b-ac10-0571c4220a0e.png)

- butonuna basılarak sisteme eklenmiş olan seçili dil sistem dilleri arasından çıkartılır.

Default:Sisteme giriş yapan kullanıcılar giriş sırasında dil ayarını değiştirmedi ise belirlenen bu dil ile web arabirimini ve diğer araçları kullanacaktır.

### 2. Projeye yeni dil ekleme

Web arayüzünden sisteme giriş yapan kullanıcıların akışlar üzerindeki alanları giriş yaptığı dil ile görüntüleyebilmesi Workflow Designer uygulaması yardımıyla akış geliştirme sırasında

düzenlenir. Geliştirme yapılan akışın “Proje” özellikleri sekmesinden “Multilanguage” özelliği aktifleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/c5-fc3eb7ba-8d26-44bd-b426-b63936edebbe.png)

Multilanguage özelliği şeçildiğinde akış ve form tasarımında kullanılan tüm alanlar geliştirme yapan kullanıcıya gösterilir. Geliştirici “Add Language” butonu yardımıyla projeye yeni bir dil ekleme işlemine başlar

![](https://docsbimser.blob.core.windows.net/imagecontainer/c6-8ddad4c9-e826-417f-8a8e-5321d6a7f823.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/c7-2a396ca4-08f3-4d80-b4f9-b3c5cb73885e.png)

Kullanıcı “Add Language” butonuna bastığında sisteme kayıtlı diller arasından seçimini yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/a1-aca8f64d-161c-4ebf-abdd-b440d1ece68e.png)

Yeni dil eklendiğinde geliştirme sırasında kullanılan kelimeler gösterilerek düzenleme yapması sağlanır. Kullanıya gösterilen aksiyon butonlar , Durum ve nesne bilgileri değiştirilmektedir.

“Enable multilanguage for the project” seçeneği işaretlenerek projeyenin çoklu dil ile çalışacağı belirlenir ,ardından proje derlenerek proje çalıştırılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/a2-5f316b79-5bb1-44cb-96fb-a786bcaae724.png)

Kullanıcının web arabiriminden seçtiği dile göre süreç dil bilgisini güncelleyecektir.

### 3. Sorgulara Çoklu Dil Desteği Ekleme

System Manager uygulamasının Integration Manager sekmesiyle düzenleme yapılacak sorgu seçilerek “Save an Compile” butonu ile sorgu derlenmeye başlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/m7-02918421-413c-4286-b1d9-9d84dfe6ec8c.png)

Kolonlar sekmesinden “Columns Multilanguage” butonu ile çoklu dil desteği için gerekli işlemlere geçilir.

Tüm alanlar için belirlenen dildeki karşığı eklenerek işlem tamamlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/m6-bb6a5488-69a7-4934-9480-e402bc4169fb.png)

### 4. Menüye Dil Ekleme

Web arabiriminden uç kullanıcıların “Uygulamalar” sekmesi altında gördüğü menüye çoklu dil desteği eklemek için “ System Manager/Menü Manager” kullanılır.Seçilen Menü Sekmesi Multi Language özelliği ile güncellenir . Ardından Save Profiles işlemi ile kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/m1-eec47384-7e14-40bd-9dd9-53393211a093.png)

Menü Görünümü kullanıcının giriş yaptıgı dile göre değişecektir.

### 5. Arşiv Yöneticisi Çoklu dil Desteği

System manager / Arşiv Yöneticisi yardımıyla seçilen arşivin başlık bilgisi değişitirilerek açıklama bilgisine multi language özelliği kazandırılmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/o6-9d78e278-224b-48c3-86d3-4de10bac1bc6.png)