# Doküman Yönetimi - Onay Aşamasındaki Dokümanın Onay Matrisinde Pasif Pozisyon Varsa Ne Yapılmalı?

1. Doküman modülünde akışlar, pozisyon bazlı ilerlemektedir. Yetki, dağıtım, onay matrislerine eklediğiniz pozisyonlarda değişiklik olduğu zaman, yerine geçen kişi olduğunda veya değiştirilmesi gerektiğinde pozisyon kodu değiştirici menüsünü kullanmanız gerekmektedir.
Sahibi boş olan pozisyonu bulduktan sonra bu pozisyonda kalan işleri devretmelisiniz. 
Bunun için SAT--Tanımlar--Pozisyon Tanımlamadan işleri aktaracağınız kişinin pozisyon kodunu not edin .Daha sonra SAT--Konfig--Pozisyon Kodu Değiştiriciden eski kod yerine boşta kalan yeni kod yerine ise işlerin devredileceği kodu yazıp kaydedin.
Bu şekilde boş pozisyondaki dokuman kontrol onay yetki dağıtım matrisi gibi işlemler yeni kişiye geçecektir.(Bu işlem doküman modülü için geçerlidir.)

2. Doküman Modülü Modül Yöneticisi, Raporlar > Onay Bekleyen Doküman Listesinden ilgili dokümanı seçip, sağ üstte onay matrisi değiştir butonu ile onay matrisindeki pozisyonu kaldırıp, yerine başka bir onaycı ekleyip onay silsilesini yeniden düzenleyebilir.(Bu işlem yapıldığında bütün onaycılara onay işlemi baştan gidecektir.)

3. Modül Yöneticisi, Raporlar > Onay Bekleyen Doküman Listesinden ilgili dokümanı seçip, sağ üstte görüntüle butonu ile işten ayrılmış kullanıcı yerine dokümanı onaylayabilir.(Onaylayan kişi, modül yöneticisi olarak gözükecektir.)
