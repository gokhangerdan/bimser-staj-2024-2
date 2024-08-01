# Denetim Planı Yayınlama Mailinde Plan İletiliyor mu?

Denetim planı yayınlanırken plan ek dosya şeklinde mail olarak iletilir. Ek dosya olarak ise DENETIM_PLANI.xls şablonu iletilir. Bu şablona Sistem Altyapı Tanımları > BSAT > Konfigürasyon Ayarları > Rapor Formatları Düzenleme menüsünden ulaşabilir ve düzenleyebilirsiniz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Screenshot%202024-03-21%20105513.png-e4de2877-ef60-4f59-93ee-6414400e107d.png)

Denetim planı yayınlamada ek dosya gönderilmesin isteniyorsa “18- Raporlar mail ekinde gönderilsin mi?” parametresi “Hayır” olarak güncellenmelidir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/Screenshot%202024-03-21%20105626.png-b97781ce-5259-4cf8-bff0-8dad7f9f2b58.png)

Ancak bu parametrenin “Hayır” seçilmesi sadece denetim planı yayınlama kısmını etkilemez. Denetim kapatma, denetim yayınlama gibi denetim modülünden yayınlanan tüm raporlarda ek dosya gönderimini engeller. Dolayısıyla bu parametre denetim modülünden gelen hiçbir raporda ek dosya gönderilmesi istenmiyorsa “Hayır” yapılmalıdır.

