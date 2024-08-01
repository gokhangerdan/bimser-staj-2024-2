---
title: "LDAP Konfigürasyonu"
sidebar_position: 1
---

# LDAP Konfigürasyonu

eBA Sistemine giriş yöntemi olarak LDAP konfigürasyonunun yapılması.

1. Sunucu ayarları
2. eBA Configuration Tool ile yapılandırılması
3. IIS'in ayarlanması
4. eBA kullanıcıları ile LDAP kullanıcılarının eşleştirilmesi
5. Test ve sorun giderme

### 1. Sunucu ayarları

eBA nın kurulu olduğu sunucu network üzerinde LDAP'ın olduğu sunucuya erişebilmelidir. Sunucu domaine alınmalıdır.

### 2. eBA Configuration Tool ile yapılandırılma

eBA Configuration Tool ***[eBA Kurulum Dizini]\ConfigServer\eBAServerConfigTool.exe*** yolundan çalıştırılır. Program çalıştıktan sonra Security sekmesini seçerek aşağıdaki ekrana ulaşılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5372db69-02ba-48ce-9205-0c24ccb24a5f)

Bu ekranda aşağıdaki özellikler seçilmelidir.

    Authentication Mode : custom
    Authentication Type : LDAP

Eğer kullanıcılar login olurken sadece LDAP kullanıcı adlarını kullanacaklarsa ***LoginMode : external*** olmalıdır.

Hem eBA kullanıcı adı parolasını hemde LDAP kullanıcı adını parolasını kullanacaklarsa ***mixed*** veya ebadaki kullanıcı adını LDAP taki parolayı kullanacaklarsa ***internal*** olmalıdır.

eBA daki kullacı adları ile LDAP taki kullanıcı adları aynı ise ***ExternalUserMatch : equal*** olmalıdır.

Eğer aynı değilse eşleştirilmeleri gerekir. Bunun nasıl yapılacağı [4. eBA kullanıcıları ile LDAP kullanıcılarının eşleştirilmesi](### 4. eBA kullanıcıları ile LDAP kullanıcılarının eşleştirilmesi) adımında anlatılmaktadır.

Domain path sisteme girecek kullanıcıları sorgulayabilmelidir. Aksi durumda authentication yapılamaz. Default domain seçim kutusundan bu domain seçilmelidir.

Birden fazla domain varsa ***Allow Multiple Domain Entry*** seçim kutusu işaretlenmelidir. Böylece birden fazla domain girişi yapılabilir.

___

Eğer Allow Multiple Domain Entry seçim kutusunun işareti kaldırılıyor ve birden fazla domain zaten kayıtlı ise program Default Domain dışındaki tüm domain isimlerini ve yollarını silmek için kullanıcıdan onay bekleyecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20246e53-e829-4d9a-8c85-a6f7a4ebb631)

___

Domain Path, ***Test*** butonuna basılarak test edilebilir. Test butonuna basılarak aşağıdaki ekrana ulaşılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea5692f0-d2c0-420d-8089-1f55627eff53)

Bu ekranda ***Domain Name*** ve ***Domain Path*** gibi değerler ilgili alanlardan otomatik olarak gelmektedir. Username ve Password alanları doldurularak girilen domain path kontrol edilebilir.

Bu ayarların algılanabilmesi için Services sekmesine giderek ***eBAServer*** servisinin başlatılıp durdurulması gerekmektedir.

### 3. IIS'in ayarlanması

***Control Panel->Administrative Tools->Internet Information Services*** altında ***eba.net*** uygulaması özelliklerine girilmelidir. ***Features View***, ***Authentication*** çift tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb90c4464-48be-4e4c-b23e-8ce2dd1ddd86)

___

Gelen pencerde ***Anonymous access*** seçili olmalıdır (***Enabled***). En alttaki ***Windows authentication*** seçili olmamalıdır (***Disabled***).

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7de3fe3-b2c8-46b8-9eeb-2b8441984d88)

___

***eba.net*** uygulamasına ***Content View*** tıklanıp sağ taraftaki listeden ***WindowsAuthentication.aspx*** dosyası bulunup ***Features View*** özelliklerine girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload927f63d4-55ac-4bd0-b5f1-b75c01edd547)

___

***Authentication*** seceneği çift tıklanır. Gelen pencerede ***Anonymous authentication*** seçili olmamalıdır (***Disabled***). En allttaki ***Windows authentication*** seçili olmalıdır. (***Enabled***)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c93bcf2-45ca-4fb8-8a7b-fcf517f89a11)

### 4. eBA kullanıcıları ile LDAP kullanıcılarının eşleştirilmesi

Eğer eBA kullanıcıları ile LDAP kullanıcıları aynı değilse eşleştirme yapmak gereklidir. Bu sayede LDAP taki herbir kullanıcının eBA da hangi kullanıcıya karşılık geldiği anlaşılabilir.

Eşleştirme tanımları için kullanıcı tanımlamalarına ***ExternalUsername*** tanımlamasının eklenmesi gereklidir.

eBA System Managera girdikten sonra ***Organization Management->Property Definitions->Properties*** menüsü açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada31df319-165b-4f99-95fe-b638c43c528e)

___

Eğer ***Özellik Tanımları*** içinde ***ExternalUsername*** yok ise ***Yeni Özellik Tanımı Ekle*** butonuna basılır ve gelen pencerde ***Ad: ExternalUsername***, ***Başlık: ExternalUsername***, ***Tip: Metin*** seçilip ***Tamam***'a basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7924464-2892-4b4e-a116-75e932bc20de)

___

***Kullanıcı Özellikleri*** arasında ***ExternalUsername*** yok ise ***Yeni Özellik Ekle***'ye tıklanır.

***Özellik Tanımları*** listesinden ***ExternalUsername*** üstüne tıklanır. Bu özellik böylece ***Kullanıcı Özellikleri***'ne eklenmiş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c2b704d-a266-4dd8-bc9d-7acd82e4b68f)
