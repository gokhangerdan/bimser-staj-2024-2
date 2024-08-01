# Akış Tasarımı
Oluşturulan projenin akışını tasarlamak için; Flows klasörü altındaki varsayılan olarak Flow1 adı ile gelen akışa çift tıklanır. Akış tasarım ekranı, arayüzde varsayılan akış dizaynı ile açılacaktır.
Masraf Beyan sürecinin akış senaryosu adımları aşağıdaki gibi olacaktır;

- **Birinci Adım:** Web arayüzünde, Masraf Beyan bildiriminde bulunacak kullanıcı, menüden Masraf Beyan Sürecini başlatır. Bu kullanıcı, akış ekranındaki Akışı Başlatan (FlowStarter1) nesnesine karşılık gelir. Akışı başlatan kullanıcı, masraf beyan formundaki alanları doldurup, “Gönder” aksiyon butonuna basarsa akış bir sonraki adımda Akışı Başlatanının Amiri pozisyonundaki kullanıcıya geçer.
  

-  **İkinci Adım:** Akışı Başlatanın Amiri formu tekrar düzenleyebilir, onaylayabilir, reddedebilir veya revizyona gönderebilir. “Reddet” veya “Revizyon” aksiyonlarından biri gerçekleştiğinde Akış Başlatan bilgilendirilir. Red kararı sonucu akış bitirilir, revizyon kararı verilirse Form tekrar Akış Başlatanın onayına düşer.
  

-  **Üçüncü Adım:** Amir onayından sonra akış, Masraf Beyan formunun “Toplam Masraf Tutarı” alanındaki değerin 2000’den küçük ya da büyük olmasına göre farklı kollara ayrılır.
  

-  **Dördüncü Adım:** Toplam masraf tutarı 2000’den küçük olduğunda akış İK Grubuna, büyük olduğu durumda ise Akışı Başlatanın Departman Müdürüne yönlendirilir. İK grubu formu sadece onaylayabilme yetkisine sahip iken, departman müdürü formu onaylayabilir ya da reddedebilir. Departman yöneticisi formu reddettiği durumda akış biter. Onayladığı durumda ise İK Grubunun onayına düşer.
  

-  **Beşinci Adım:** İK grubunda bulunan kullanıcılardan 1 kişinin onayından sonra akış, Muhasebe Departmanındaki kullanıcılara yönlendirilir. Departmandaki kullanıcılar form üzerinde sadece onaylama yetkisine sahiptir. Departmandaki 1 kişinin onayının sonucunda Akışı başlatana talebin onaylandığına dair bilgilendirme maili gönderilir ve Süreç tamamlanır.
