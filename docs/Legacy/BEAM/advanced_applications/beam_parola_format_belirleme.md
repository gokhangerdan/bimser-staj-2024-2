# BEAM KULLANICI ŞİFRELERİNİN REGEX FORMATINA UYARLANMASI VE ŞİFRE DEĞİŞİKLİK POLİTİKALARI

Beam uygulaması üzerinden, kullanıcıların şifrelerini belirleme ve yenileme süreçleri yönetilebilmektedir.
Şifre belirleme ve yenileme politikaların: 
Ana menü > Sistem > Sistem Parametreleri 
ekranı üzerinden, yönetici yetkisine sahip kullanıcı hesaplarıyla düzenleyebilirsiniz.

Eğer bu menüyü göremiyorsanız:
Ana menü > Sistem > Kullanıcı Grupları > Yönetici Grubu > Değiştir > Menü Yetkileri içerisinden "Sistem > Sistem Parametresi" kutucuğunu aktif ederek menüyü aktif edebilirsiniz.


## Şifre Yenileme ve Belirleme Ayarları

Aşağıda paylaşılan ilgili başlık altındaki parametre değerlerini, Sistem parametreleri içerisinde "Anahtar Dğer" sütununda aratınız. Parametre tanımlıysa karşısındaki değeri düzenleyebilirsiniz. Eğer parametre tanımlı değil ise "Ekle" butonunu kullanarak parametre satırı oluşturun ve "Anahtar Değer" sütunu içerisine ilgili parametreyi ekleyin ve Kaydet  butonu ile işlemi tamamlayın. Daha sonra parametrenin karşısında bulunan değeri güncelleyerek tekrar kaydedebilirsiniz.

### Şifre Yenileme Süresi Belirleme

Parametre Anahtar Değeri:
WebUISettings.User.PasswordChangePeriod

Bu parametre yardımıyla, kullanıcıların beam uygulama şifrelerini belirleyeceğiniz periyotlarla değiştirmelerini sistem zorunlu tutacaktır. Bu parametre karşısına yazılacak değer gün birimiyle çalışmaktadır. Örneğin 90 yazdığınız takdirde kullanıcıların her 90 günde bir şifrelerini yenileme zorunluğu devreye girmiş olacaktır.


### Şifre Yenileme Esnasında Geçmiş Şifrelerin Tekrar Kullanımını Engelleme

Parametre Anahtar Değeri:
WebUISettings.User.LastPassCount

Bu parametre yardımıyla, kullanıcıların şifre belirlerken beam uygulamasında geçmişte kullandıkları eski şifrelerini tekrar kullanmaları engellenebilmektedir. Örneğin değer olarak 5 yazılması durumunda kullanıcıların Beam uygulamasında geçmişte kullandıkları son 5 şifreyi yeni şifre olarak girmeleri durumunda bu işlem sistem tarafından engellenecek ve uyarı verecektir.


### Şifre Uzunluğu ve İçermesi Gereken Karakter Ayarları (Regex)

Parametre Anahtar Değeri:
WebUISettings.User.PasswordFormat 

Bu parametre yardımıyla belirlenecek şifrenin formatı uygun gördüğünüz koşulları sağlayacak şekilde düzenlenebilir.  Parametreinin karşısındaki değer sütununa aşağıdaki formatlardan uygun gördüğünüz kombinasyonu tanımlayıp uyguladığınız takdirde o andan itibaren belirlenecek şifrelerde bu yapı zorunluluğu devreye girecektir.

Format belirlemede kullanılacak ifadeler ve anlamları aşağıdaki gibidir: 

Format başlangıcı (Zorunlu): ^ 

Dizede en az bir rakam olması kontrolü sağlar: (?=.*\d)

Dizede [] arasında belirlenen karakterlerin kontrolünü sağlar: (?=.*[@#$%])

Dizede en az bir büyük harf kontrolü sağlar: (?=.*[A-Z])

Dizede en az bir küçük harf kontrolü sağlar: (?=.*[a-z])

Dizedeki minimum karakter sayısı kontrolünü sağlar (minimum 8 karakter vb.): {8,}

Format bitişi (Zorunlu): $ 

Örnek format ; 
" ^(?=.*\d)(?=.*[@#%])(?=.*[A-Z])(?=.*[a-z]).{8,}$ "

