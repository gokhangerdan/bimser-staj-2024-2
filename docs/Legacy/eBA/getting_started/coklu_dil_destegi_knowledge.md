# Çoklu Dil Desteği

## 1.	Sisteme yeni bir  dil ekleme

eBA İş Akışı ve Döküman yönetim sistemine yeni bir dil eklemek için “eBA Kurulum dizini\Common”  içerisinde bulunan “eBAConfigurationEditor.exe” uygulaması kullanılır. 
Uygulamaya giriş yapıldıktan sonra “Language” sekmesinden isim ve açıklama girilerek ekleme yapılır. İşlem sonrası uygulama servisi ve web sitesi restart edilmelidir.

(Yeni eklenen dil tanımına dair eBA uygulamasının kurulu olduğu dizinde Languages klasörü altında Client ve Server klasörlerinde ilgili xml dosyaları bulunmalıdır.  Yoksa oluşturulmalıdır)


![](https://docsbimser.blob.core.windows.net/imagecontainer/1-%20Sisteme%20Yeni%20Dil%20Ekleme-7020282b-caa4-45ab-99db-35a53cb71114.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/1.1%20-%20Kurulumla%20gelen%20dil%20dosyaları%20örneği-157c6e92-daa8-4171-a77b-889c4705e395.png)

## 2.	Projeye yeni dil ekleme

Web arayüzünden sisteme giriş yapan kullanıcıların akışlar üzerindeki alanları giriş yaptığı dil ile görüntüleyebilmesi Workflow Designer uygulaması yardımıyla akış geliştirme sırasında düzenlenir. 
Geliştirme yapılan akışın “Proje” özellikleri sekmesinden “Multilanguage” özelliği aktifleştirilir. Bu işlem için ilgili projeninin eBA Workflow Studio da açılmış olması gerekir)


![](https://docsbimser.blob.core.windows.net/imagecontainer/2.1%20-%20Proje%20Multilanguage%20özellikleri-6b5f0f00-cd6f-464e-beb0-531aec0a4a88.png)

Açılan pencerede proje için multilanguage özelliği aktif edilir.
Dil ekleme butonuyla eklenmek istenen dil seçilir.  Yeni eklenen dil tanımı için boş satırlardan oluşan sütun eklenmiş olacaktır. Bu sütun üzerindeki tüm satırlar ilgili dil karşılıkları olacak şekilde doldurulabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/2.2-%20Projeye%20Dil%20Ekleme-4ae53c27-144d-47fb-8391-026834006b9c.png)

## 3.	Sorgulara Çoklu Dil Desteği Ekleme

System Manager uygulamasının Integration Manager sekmesinde düzenleme yapılacak sorgu seçilerek “Save an Compile” butonu ile sorgu derlenmeye başlanır. 
Columns sekmesinde bulunan 'Columns MultiLanguage' butonu tıklanır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/3.1%20-%20Sorgu%20Derleme2-7ac7dd4d-b565-409e-b7f6-045ec9a37025.png)

Tüm alanlar için belirlenen dildeki karşığı eklenerek işlem tamamlanır. 



![](https://docsbimser.blob.core.windows.net/imagecontainer/3.2%20-%20Sorgu%20Dil%20Karşılıkları-ee514dc1-fd62-4fc6-bb11-d4f0f47adbad.png)

## 4.	Menüye Dil Ekleme 

Web ara yüzünde uç kullanıcıların “Uygulamalar” sekmesi altında gördüğü menüye çoklu dil desteği eklemek için yine web ara yüzünde bulunan “Menü Yöneticisi” kullanılır. 
Seçilen Menü Sekmesi özelliklerinde çoklu dil başlığı altında dil karşılıkları girilerek kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/4.1%20-%20Menü%20Yöneticisi-7fd66610-fcdb-4899-87a3-fa4a7e0bbe94.png)

## 5.	Arşiv Yöneticisi Çoklu dil Desteği

System manager / Arşiv Yöneticisi altındaki tüm arşiv tanımlarında Genel sekmesinde Multi Language Caption başlığı altında dil karşılıkları girilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5.1%20-%20Arşiv%20Başlıklarında%20Dil%20karşılıkları-6d9bb0fe-9e63-4775-a179-32ab8b0b33b4.png)

