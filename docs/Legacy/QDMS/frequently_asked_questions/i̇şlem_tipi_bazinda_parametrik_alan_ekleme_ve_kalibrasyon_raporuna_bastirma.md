# İşlem Tipi Bazında Parametrik Alan Ekleme ve Kalibrasyon Raporuna Bastırma

 İşlem Tipi bazında parametrik alan eklemek için;
SAT > Cihaz Yönetimi > İşlem Tipi Tanımlama menüsüne geliniz. Parametrik alan eklemek istediğiniz işlem tipini seçerek sağ üstte yer alan "Alan Tanımlama" butonuna basınız.

Açılan sayfada "Yeni" butonu yardımıyla ilgili işlem tipi üzerine parametrik alan ekleyebilirsiniz.

Bu işlemin ardından parametrik alan eklediğiniz cihaz için yeni bir iş emri açıldığında, işlem gerçekleştirme sayfasında parametrik alanlar eklenecektir. 

Eklediğiniz parametrik alanları "Raporu Oluştur" butonu ile oluşturduğunuz kalibrasyon raporuna eklemek için ise;

SAT > BSAT > Konfigürasyon Ayarları > Rapor Formatları Düzenlemem menüsüne gelerek bu menüde yer alan "KALRAP" isimli şablonu indiriniz.

İndirdiğiniz şablonda parametrik alanın gelmesini istediğiniz sütuna;

<ISL_KISAKOD> bilgisini yazınız.

KISAKOD= Parametrik alan oluşturma sayfasında girmiş olduğunuz Kısa Kod alanı. Örneğin Seri No adında bir parametrik alan için Kısa Kod alanına SERI yazdığınız düşünelim. Bu durumda Seri No alanını rapora basmak için kullanmanız gereken tag  <ISL_SERI> şeklinde olacaktır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/Parametrik%20Alan%20Eklemesi-a7f03ca3-fc3b-49d0-8844-273630474d59.png)

