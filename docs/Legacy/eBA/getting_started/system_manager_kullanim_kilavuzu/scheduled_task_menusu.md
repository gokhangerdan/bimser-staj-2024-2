---
title: 8. Scheduled Task Menüsü
sidebar_position: 17
---

# 8. Scheduled Task Menüsü

Sistemde, otomatik süreç tetikleme işleminin planlanabileceği alan Schedule Task alanıdır. Yeni bir planlanmış iş tanımlamayı, var olan planlanmış işleri düzenlemeyi sağlamak için Zamanlanmış Görev menüsü kullanılır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload32af5b12-2cde-41f6-b3bf-0e35e86bf5b9)

Şekil 68’de, Scheduled Task menüsüne tıklanır. Bu menü içerisinde yeni iş tanımlanabilir, var olan düzenlenebilir, ya da iş silme işlemi yapılabilir.  Add New butonu ile yeni zamanlanmış görev eklenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91d96348-275d-4eae-a067-403800155ebb)

	Description: Eklenecek görevin açıklaması yazılır. 
	Task Type: Kaydın tipi belirlenir. Bu alanda “ProcessStart” seçeneği ile bir akış başlatılabilir veya “ProcessContinue” seçeneği ile başlamış bir akış, belirtilen adımdan devam ettirilebilir.
Akış başlatma seçilir ise yukarıdaki resimde olduğu gibi akışın adı ve akışa dışarıdan gönderilecek sabit parametreler girilebilir. 
Akış devam ettirme seçeneği seçilir ise process id,request id, flow object ve parametre girilebilecek ekran açılacaktır. 
	Schedule Type: Tanımlanan işin tek seferlik, günlük, haftalık, aylık periyodlar ile çalıştırılması sağlanabilir. Bu periyotların özellikleri ise Repeat Parameter kısmından düzenlenebilir. 
	Enable: Bu seçenek işaretli ise görev aktiftir. Pasif yapılmak isteniyorsa seçenek işareti kaldırılır.
	Start Date: Taskın başlama tarihinin belirlendiği alandır.
	Expire Date: Tanımlanan task belirli bir süre sonra iptal edilmek isteniyorsa bu alanda expire date tarihi ve saati belirtilir. Eğer task expire olmasın isteniyorsa Never seçeneği işaretli kalır.
	Process Name: Hangi süreç için görev oluşturuluyorsa bu alana süreç adı yazılır. 
	Process Parameters: Bu alana başlatılacak ya da devam ettirilecek sürece gönderilecek parametre değerleri yazılır. Burada Name alanına parametre adı, Value alanına parametre değeri yazılır. Name alanına yazılan parametre adı ile, ilgili sürecin akış kısmına eklenen değişken nesnesinin adı aynı olmak zorundadır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload24b89e33-e4b7-42ae-9df6-94693ec7ed93)

Şekil 70’de, 1 numaralı alanda eklenen görevler listelenmektedir. 2 numaralı alan; yeni görev eklemek için Add New, seçili görevi silmek için Delete, görevde değişiklik yapmak için Edit,  pasif tüm görevleri silmek için Delete All Passive Flows butonuna tıklanır. 
Sistemde Schedule Task servisi her tetiklendiğinde, bu alanda tanımlı taskın başlama tarih ve saati kontrol edilerek zamanı gelen task, verilen parametrelerle çalıştırılır.