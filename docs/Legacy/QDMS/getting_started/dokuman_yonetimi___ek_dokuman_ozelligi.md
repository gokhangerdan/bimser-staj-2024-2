# Doküman Yönetimi - Ek Doküman Özelliği

Sistem üzerinde bir doküman, başka dokümanlarla ilişkili ise veya ana dokümana ek olarak eklenmiş ise ek doküman özelliği ile bu dokümanların birlikte revizyonu gerçekleştirilebilir.  Bu işlem için;
1. SAT > Doküman İşlemleri > Doküman Parametreleri menüsünden 137 numaralı parametre evet yapılır. Bu parametre evet yapıldığında, doküman hazırlama/revizyon aşamasında 'Ek Doküman' adında kulakçık gelecektir.

2. Doküman hazırlama/revizyon aşamasında Ek doküman kulakçığına girilip, ana doküman ile ilişkili doküman seçilir. Sistem, bu aşamada seçtiğiniz dokümanlara otomatik olarak revizyon başlatacaktır. Bu nedenle burada seçilen dokümanların, sisteme yüklenmiş olması gerekmektedir.

3. Ek Doküman kulakçığından ilgili dokümanı(ları) seçtikten sonra her bir doküman içine girip, revizyon işlemi yapılır. Ek doküman içinde revizyon ihtiyacı yoksa sadece revizyon bilgileri kulakçığından Revizyon Nedeni ve Revizyonda Yapılanlar yazılması yeterlidir. Sistem, bu alanları zorunlu tutmaktadır.

4. Ek dokümanlar seçilip revizyon işlemleri tamamlandıktan sonra ana doküman üzerinden revizyon işlemi ilerletilir. Bu aşamada ana dokümanın revizyonu tamamlanıp yayınlandığında, ek dokümanlarda otomatik olarak yayınlanacaktır.(Bu aşamada 211 no'lu doküman parametre değerininiz evet olmalıdır. Parametre değeri hayır olduğunda ek dokümanların onayları, kendi onay matrisine göre ilerleyecektir ve ilgili kişiler onayladıktan sonra yayınlanacaktır.)

Ek doküman özelliği için ayrıca 210 no'lu doküman parametresi ile ana doküman revizyonu tamamlandıktan sonra ek dokümanların yayınlandığı bilgisini, ana dokümanın dağıtım matrisine gönderilmesini sağlayabilirsiniz.
Bu parametre evet yapıldığında, revizyon mailleri ana dokümanın dağıtım matrisine gönderir.(Ek dokümanlar dahil)
Parametre değeri hayır yapıldığında, revizyon mailleri her dokümanın kendi dağıtım matrisine göre gönderecektir.


