# YAPILMAYAN GÜNLÜK BAKIMLAR

### GÜNLÜK PERİYODİK BAKIMDA DÜN YAPILMASI GEREKEN İŞEMRİ BİR SONRAKİ GÜN YAPILDI KAPATILDI, İŞEMRİ KAPATILINCA BUGÜN YAPILMASI GEREKEN PERİYODİK BAKIM İŞEMRİ AÇILDI. NE YAPILMALI? 

Senaryoma göre doğru rapor alınabilmesi için dün açılan “günlük bakım” yapıldıysa kapatılmalı; yapılmadıysa iptal edilmelidir. 
Sebebi şudur: raporlarda dün açılan periyodik bakım iptal edilmiş, bugün açılan yapılıp kapatılmış diye kontroller gerçekleştirebiliriz.
[İsteğe göre bu periyodik bakımı iptal eden kim, bu periyodik bakım neden iptal edildi diye sisteme sorgulatabilirim. Bu gibi artıları mevcut]
Raporlarda aşağıdaki şekilde takibini sağlayabilirim:


![](https://docsbimser.blob.core.windows.net/imagecontainer/gunlukbakim1-109b1e0a-1793-4c93-874b-5d0897ff528e.png)

RAPORLARDA HER GÜNE AİT PERİYODİK BAKIMLAR YAPILDI MI, İPTAL Mİ EDİLDİ, İŞEMRİ HALA AÇIK MI DİYE KONTROL EDEBİLİYORUZ. EĞER DÜN YAPILMASI GEREKEN PERİYODİK BAKIM YAPILMADIYSA YAPILMADI GÖSTERİLMELİ, BUGÜN YAPILDIYSA BUGÜNÜN İŞEMRİ KAPATILMALI. 

Örnek veriyorum ayın 28 inde yapılması gereken Forklif 6 Aylık mekanik bakım iptal edilmiş durumda gözükmektedir. 


Bu senaryoyu nasıl gerçekleştirebilirim?

1.adım

(BC050) - Periyodik Bakımlar Oluşturulurken, Her Koşulda Bakım Yapılacak Tarih İş Bildiriliş Tarihi Olarak Aktarılsın
Bu parametre aktif ise:

2.adım

Bakımcılar işemrindeki "Bildiriliş tarihi" alanına bakacak ve bakımı yaptıkları tarih, iş emrindeki bildiriliş tarihi ile aynıysa iş emrini kapatacaklar.

Bildiriliş tarihi bakım yaptıkları tarihten daha küçük ise (günlük bakımlarda) iş emrini iptal edecekler ve yeni oluşan iş emrinin tarihi günün tarihi ile aynı olduğunda iş emrini kapatacaklar.


