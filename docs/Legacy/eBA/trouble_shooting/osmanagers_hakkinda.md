# OSMANAGERS Hakkında

### Sorun

şirkete vekaleten gelen şef ünvanlı çalışan var bu çalışana manuel kullanıcı açtım ve amir olarak diğer kullanıcıya tanımlamam gerekiyor, sql de

update OSMANAGERS set MANAGERUSERID='10000028' where USERID='00000243' bu şekilde update edip system managerda  da amir tanımlı görünmekte fakat işleyişte (form akışlarında) tanımlı şekilde ilerlememektedir bu sorunu nasıl çözebilirim yardımcı olabilir misiniz?

### Çözüm

Bu sql üzerinden atama işlemini otomatik yapan bir Bat dosyaları mevcut, bunu çalıştırarak her sabah sistem restartı sonrası atamaları yapıyorlar. Bunlar geçici çalışanlar olduğu için böyle bir yönteme başvuruyorlar. Atama sonrası eBA Servis restartı yapılınca sorun gideriliyordu ama her sabah manuel yapmak istemediklerini belirttiler. Windows schedule task kısmına eba restart bat'ını ekledik, ilk denemede olumlu sonuç alınmamış ama sonra windows schedule'da yapılan ufak bir değişiklik ile sorun giderilmiş.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload244ba490-179d-44c8-9800-d70e156e305f)