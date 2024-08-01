---
title: 3. Project Manager Menüsü
sidebar_position: 12
---

# 3. Project Manager Menüsü

Project Manager menüsünden, eBA sisteminde bulunan tüm süreç projelerini listeme, projenin detaylarını görüntüleme ve gereksiz projeleri sistemden silme işlemleri yapılabilir.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59a00ffa-8590-44d2-bd7c-250c5f2bb657)

Şekil 41’de, Project Manager menüsüne tıklanır. 2 numaralı alanda sistemde var olan süreçler listelenir. Oluşturulan süreci sistemden silmek için ilgili süreç seçildikten sonra Delete, ilgili sürecin özellikler penceresini açmak için Properties butonuna tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade51665e1-54d2-4a9e-a48b-b8a292ef92f8)

Proje özellikleri penceresinde proje ile ilgili bilgiler bulunmaktadır. Bu bilgilerden bazıları değiştirilebilir haldedir. 

	Process Name: Proje adı. 
	Process Caption: Proje başlığı. 
	Process Creator: Projenin hangi kullanıcı tarafından oluşturulduğunu belirtir. 
	Creation Date: Proje oluşturulma tarihi. 
	Version: Projenin son version sayısı. 
	Type: Proje tipini belirtir. Proje tipleri;
Standart: Bir iş akışı süreci ve bir veya daha fazla form bulunan proje tipidir. 
Workflow: Sadece bir iş akışı süreci barındıran proje tipidir. 
      Form: Bir veya daha fazla form barındıran proje tipidir. 
	Flow: Eğer iş akışı olan bir proje ise iş akışının adı belirtilir. 
	Fast Approve: Hızlı onaylama özelliğinin açık veya kapalı olduğunu belirtir. Hızlı onaylama web ekranlarında kullanılan, iş akışı isteğini açmadan direk onaylama veya reddetme gibi işlemlerinin yapılabilmesine imkan verir. 
	Project Path: Proje dosyasının sistemdeki yolunu belirtir. 
	Status: Projenin kullanıma açık olup olmadığını belirtir. Eğer proje pasif hale getirilmesi isteniyorsa bu seçenek kaldırılır. 

	Show Flow Graph: eBA web ekranında süreç iş akışı isteğinin gösterildiği bölümde iş akışının grafiğinin gösterimini belirtir. Seçilirse grafik kullanıcılar tarafından görünür. 

	Show Flow View: Akış durumlarını baloncuklar halinde web arayüzünde göstermek için aktif edilen seçenektir.

	Show In Web Approvals: Bu özelliğin işaretli olduğu projelerin onayları, web arayüzünde onaylar alanına tıklandığında görüntülenebilir olur. Bu özelliğin seçili olmadığı projelerin onayları, onay kutucuğunda gösterilmez.

	Delegable: Projenin vekaleten bir kişiye atanıp atanamayacağının ayarlandığı kısımdır.

	Show Messages: Web arayüzüde bu süreç için ileti tabının görünüp görünmeyeceğinin ayarlandığı özelliktir.

	Role Type / Id: Delegable alanı işaretli ise, vekaleti hangi yetkilere sahip kişilerin alabileceği bu alandan seçilir.

	Project Color: Bu alandan projeye bir renk seçildiğinde, web arayüzündeki onaylar sayfasında ilgili projeye ait onayların kutusu, burada seçilen renk ile renklendirilir.

	Project Ikon: Projeye ikon belirlemek için seçim yapılan alandır.

	Show Parent History: Bu özellik, alt akış projelerinde aktif edildiğinde, alt akışa ait bir sürecin akış tarihçesi web arayüzünde görüntülendiğinde hem alt akışın hem de alt akışı tetikleyen ana akışın akış tarihçesi adımları görünmüş olur. Alt akış projesinde bu özellik pasifken, alt akışın akış tarihçesinde yalnızca alt akışın akış tarihçe adımları gösterilir.

	Description : Projeye açıklama metni girilmek istenirse bu alana yazılabilir.

	Allow Multiple Approve If Event Has a Reason:  Onaylar ekranında bekleyen birden çok kayıt seçilerek bir event ile ilerletilebilir. Varsayılan olarak bu eventte Reason (Neden) alanı aktifse toplu aksiyon alınmasına izin verilmez. Reason alanı aktif olan eventler için de çoklu aksiyon alınmak isteniyorsa bu özellik aktif edilir.

	Allow Multiple Approve If Event Has an Event Form: Event form seçeneği aktif olan eventler için çoklu aksiyon alınmak isteniyorsa bu özellik aktif edilir.