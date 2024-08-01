---
title: 4. Flow Manager Menüsü
sidebar_position: 13
---

# 4. Flow Manager Menüsü

Akış Yönetim menüsünde, oluşturulan iş akışlarını listelemesine, listelenen iş akışlarının detaylarını inceleme ve iş akışı üzerinde değişiklik yapma işlemleri yapılmaktadır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload897e65ea-bc15-4758-a12f-7c5a0f0a084b)

Şekil 43’te, Flow Manager menüsüne tıklanır. 2 numaralı bölümdeki alanlardan filtreleme yapılarak istenilen akışlar listelenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb8f706c-84b1-48af-ace0-ada402488b74)

Akış numarası bilinen süreci getirmek için  Şekil 44’te,Process ID alanına akış numarası yazıldıktan sonra Filter tuşuna basılır. Gelen akışa çift tıklanarak akış görüntülenir. Properties sekmesinde akışa ait özellikler görüntülenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9183d297-f2e6-42b7-aff7-da5828053f0d)

Şekil 45’te,  Steps sekmesinde akışın hangi adımda olduğu ve akış grafiği görüntülenir. Akış herhangi bir adıma geri çekilmek isteniyorsa ilgili adım seçildikten sonra 3 numaralı alandaki Rollback to step ikonuna tıklanır. 
Not:  Akış adımlarından, akışın geri alınmak istendiği adım seçildiği halde Rollback butonunun aktif görünmemesinin iki sebebi olabilir. Birincisi, akış geri alma aksiyonu sistemde aktif edilmemiş olabilir. İkincisi geri alınmak istenen akış, bitmiş bir akış olabilir.
1)	Sistemde akış geri alma aksiyonunu aktif etmek için; eBAConfigurationEditor.exe açılır ve Advance tabına gelinir. Burada Workflow düğümü altındaki Rollback düğümüne tıklanır.Yanda gelen parametrelerde “Enable” anahtarının değeri false ise, true yazılır ve File kısmı altından değişiklik kaydedilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d7bf829-136f-4d78-99c6-3282f0129265)

2)	Sistemde Rollback özelliği aktif ancak geri alınmak istenen akış, bitmiş bir akış olduğu için Rollback butonu aktif görünmüyorsa yine eBAConfigurationEditor.exe açılır ve Advance tabına gelinir. Burada Workflow düğümü altındaki Rollback düğümüne tıklanır. Yanda gelen parametrelerde “PeriodForFinishedWorkflows” anahtarının değeri, geri alınmak istenen akışın kaç gün önce bitmiş bir akış olduğuna göre tekrar gün bazında düzenlenir ve File kısmı altından değişiklik kaydedilir.
Eğer Rollback düğümü altında Enable ve PeriodForFinishedWorkflows keyleri mevcut değilse siz manuel ekleyebilir ve değerlerini atayabilirsiniz.
Config de bu değerler düzenlenip, sol üst köşedeki File kısmı altından ayarlar kaydedildikten sonra, System Manager ekranı açıksa kapatılır, eBA servisleri yeniden başlatılır ve System Manager tekrar açılarak akışı geri alma işlemi tekrar denenebilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb20a9979-d2b1-40f9-ada3-5097cd68c938)

Şekil 46’da, Codes sekmesinde süreçte akış tarafında yazılan kod görüntülenir. Başlatılmış akışlarda kod tarafında değişiklik yapmak için bu bölüm kullanılır. Değişiklik yapıldıktan sonra Compile butonu ile akış derlenir. Bu şekilde kod tarafında yapılan değişiklik, yalnızca ilgili süreçte geçerli olmuş olur.