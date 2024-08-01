# Sayfalar arası geçiş yaparken sorulan kaydetmek istiyormusunuz uyarısını iptal etmek 

Sayfalar arası geçiş yaparken sorulan kaydetmek istiyormusunuz uyarısını iptal etmek için aşağıdaki gibi confige key ekleyebilirsiniz. Yalnız bu yaptığınız değişiklik süreç bazlı değil tüm süreçlerde etkilidir.

Configuration editoru açın, advance sekmesine gelin burada web düğümüne tıklayın. Sağ tarafa gelen alana ShowDocumentEditModeConfirmation key ini ekleyip değerini false yapıp config i kaydedin.
Sonrasında servisleri restart ederseniz artık bu soruyu sormayacaktır. Yalnız bu yaptığınız değişiklik süreç bazlı değil tüm süreçlerde etkilidir.

Web.ShowDocumentEditModeConfirmation 


![](https://docsbimser.blob.core.windows.net/imagecontainer/Şekil1-48f9ffb6-ffe6-46bd-ba50-4779edbfcc44.png)

