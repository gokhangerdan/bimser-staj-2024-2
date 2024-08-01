# Yetki Kodu Nedir, Nasıl Kullanılır?

Yetki kodu, iş talebi ve iş emri kayıtlarında filtreleme amaçlı, varlık kayıtlarında ise kayıt bazlı değiştirme yetkilendirilmesi için kullanılır.
Temel mantık, “yetki kodu atanmış kullanıcılar sadece aynı yetki kodu atanmış olan kullanıcıların açtıkları kayıtları veya yetki kodu olmayan kullanıcıların açtıkları kayıtları görebilir” şeklinde açıklanabilir.
Bir kullanıcı hesabına yetki kodu, kullanıcı kaydı detay sayfasında “Genel Bilgiler” sekmesi içerisinde bulunan “Yetki Kodu” başlıklı alanda atanır.


## İş Emri ve İş Talebinde Kullanımı

Kullanıcı hesabına yetki kodu atandıktan sonra; yeni bir iş emri ya da iş talebi oluşturduğunda ilgili kayıtların içerisine, kullanıcı hesabında tanımlı olan yetki kodu otomatik atanır.
Şirket parametrelerinde bulunan BC037 kodlu parametre aktif edilirse; Bu kullanıcı hesabı ile oluşturulan iş talep ve iş emirlerini sadece ilgili yetki kodu atanmış olan kullanıcılar ile hiç yetki kodu atanmamış olan kullanıcılar görebilir yani farklı yetki kodu atanmış olan kullanıcılar bu kayıtları göremezler.


## Varlıklarda Kullanımı

Yetki kodu varlıkların kayıt bazlı yetkilendirilmesi için de kullanılır. Bu özelliğin aktif olması için herhangi bir parametre yoktur.
Kullanıcı bir varlık kaydı oluşturduğunda, ilgili varlık kaydı içerisine yetki kodu otomatik taşınır. Daha sonra oluşturulan bu varlık kaydını sadece aynı yetki kodu atanmış olan kullanıcılar ile hiç yetki kodu atanmamış olan kullanıcılar değiştirebilirler.
Temel mantık, “yetki kodu atanmış kullanıcılar sadece aynı yetki kodu atanmış olan kullanıcıların açtıkları varlık kayıtlarını değiştirebilirler” şeklinde açıklanabilir.


