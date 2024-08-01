# SCHEDULES
## Schedules Projesi Oluşturma
Tasarlanan çözüm içerisinde Schedules alanı kullanılıp belli bir zaman aralığında belirlenen aralıklarla projenin veri kaynağına eklenmiş Rest servise istek gönderilebilmektedir.
Bu işlemi yapabilmek için öncelikle geliştirme ara yüzünde (IDE) proje içerisindeki Çözüm Gezgini panelindeki Schedules bölümüne yeni öge eklenmelidir.![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/1-89311958-c0f6-4a7d-bd34-3abca78cc708.png)
Yeni Öge seçeneğine tıklanarak açılacak pop-up penceresine Scheduler seçeneği seçilir ve ad kısmına verilmek istenen plan adı yazılır.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/2-fa3e7273-86a9-4583-80b5-c846d00276d8.png)
Oluşturulan Schedule ögesi içerisinde İşler ve Takvimler olmak üzere iki farklı alan bulunur. İşler bölümünde çalışması istenen olay ve olayın tetikleyicisi tanımlanır, Takvimler bölümünde ise İş bölümüne tanımlanan olayın kullandığı tetikleyicinin etkin **olmaması** istenen tarih aralığı girilmelidir.
## Oluşturulan Schedule’da İşler Bölümü ve Yeni İş Eklenmesi
Projeye eklenen schedule ögesinde, İşler sekmesinde Ekle butonuna tıklanarak yeni iş eklenir.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/3-b623ad37-4656-49f2-8553-061282c9377f.png)
Eklenen “İş” içerisinde Eylemler ve Tetikleyiciler olmak üzere iki farklı sekme bulunmaktadır. Eylemler alanında yapılması istenen iş tanımlanırken (Metod Çağıran Aksiyon/RestApi Çağıran Aksiyon/Akış Başlatma Çağıran Aksiyon), Tetikleyiciler alanında eklenen eylemin çalışma türü (Basit tetikleyici/Günlük zaman aralığı tetikleyici/Cron tetikleyici) tanımlanır.
Eklenen iş alanında Ad, Açıklama ve Kişisel Erişim Anahtarı olmak üzere üç alan bulunur.
• **Ad**: İşe tanımlanan adlandırılmanın girileceği alandır. Çoklu dil girişi desteklemektedir.
• **Açıklama**: İşin hangi görevi yaptığının kısa açıklaması gibi alandır. Çoklu dil girişi desteklemektedir.
• **Kişisel Erişim Anahtarı**: Web ara yüzünde Hesabım bölümünde Vekâlet ve Kişisel Erişim Anahtarları bölümünden alınan Kişisel Erişim Anahtarının yazıldığı alandır. Yapılacak işleme uygun erişim anahtarı üretilip, bu alanda kullanılacaktır.
**Not** : Kişisel erişim anahtarı tanımlanmazsa veya anahtar yanlış/yetersiz yetki ile oluşturulursa tanımlanan iş çalışmaz.
İşler bölümü içinde birden fazla iş tanımlanması mümkündür. Oluşturulacak her yeni iş içinde farklı eylemler ve tetikleyicileri tanımlanabilir. Yeni iş oluşturulurken, her iş için kişisel erişim anahtarı tanımlanmalıdır.
### Yeni Eylem Ekleme
Eylemler sekmesindeki Ekle butonuna tıklanır, çalışması istenen eylem seçilir. Butona tıklanıldığında Metod Çağıran Aksiyon, RestApi Çağıran Aksiyon ve Akış Başlatma Çağıran Aksiyon seçenekleri listelenmektedir.
#### Metod Çağıran Aksiyon
Doküman Yönetimi bölümü içinde yüklü bir DLL dosyası içine yazılmış metodun kullanılması istenirse bu aksiyon tipi kullanılabilir.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/4-13e2db1f-f2dc-4b00-8e11-90399ad1ca63.png)
 Eylemler alanında Metod Çağıran Aksiyon eklendiğinde, ögenin Özellik Görüntüleyicisi bölümünde listelen alanlar şunlardır:
 |**AD**|**Gereklilik**|
 |-|-|
|Ad| Eyleme verilmek istenen adı tanımlamak için kullanılır. Çoklu dil girişi desteklemektedir.|
|Açıklama| Eylemin yaptığı açıklamayı tanımlamak için kullanılır. Çoklu dil girişini desteklemektedir.|
|Assembly yolu| Alana tıklandığında açılan dizin panelinde doküman yönetimi içinde, eylemde çalıştırılmak istenen DLL dosyası seçilmelidir.|
|Tür adı| DLL dosyası içinde çalıştırılacak metodun bulunduğu namespace ve class bilgisi nokta işaretçisi ile birleştirilerek yazılmalıdır. Örneğin DDL dosyası içinde namespace ifadesi Bimser, class ise Synergy ise alana Bimser.Synergy yazılmalıdır.|
|Metod adı| Class içinde çalıştırılacak metod adının yazıldığı alandır.|
|Metod argümanları| Metod adı alanında tanımlanan metod bilgisi parametre değer alıyorsa, parametrelerin tanımlanması için kullanılır. Verilen argümanlara göre metod adı alanı baz alınarak, ilgili overload içinde kullanılacaktır.|
|Varsayılan değerler| DLL dosyası içindeki class ögesindeki aynı isimdeki ctor (constructor) parametre değer alıyorsa, bu değerlerin tanımlanması için kullanılmaktadır.|

Assembly yolu içerinde DLL dosyası seçim işlemi gerçekleştirilmekte, tür adında DLL dosyası içindeki namespace ve class adı birleştirilerek yazıldı. Metod adı içinde çalışması istenilen metod, kaç adet parametreye ihtiyaç duyuyorsa, metod arhümanları alanında yazılan parametrelere göre uygun olan metodlar çalıştırılır. ctor (Constructor) içerisinde tanımlı olan parametre adlarıyla "Json Editör" içerisinde parametreler oluşturularak gönderilebilir.
**Not 1**: Varsayılan değerler alanı eylemin çalışması için zorunlu alan değildir, dll içinde ctor tanımlandıysa ve onun çalışması isteniyorsa kullanılabilir.
**Not 2**: DLL içeriğinde ctor ve metod bulunup, varsayılan değerler ve metod argümanları alanları içine de parametre bilgileri tanımlandıysa, girilen metod adı overload edilerek çalıştırılır. ctor ögesi çalıştırılmaz.
### RestApi Çağıran Aksiyon 
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/5-6161ce50-0b09-4e03-b394-edc38ab83b47.png)
Eylemin özellik görüntüleyici panelinde Ad, Açıklama ve Veri kaynağı seçenekleri bulunmaktadır.
• Ad: Eklenen eylemin adının tanımlanması için kullanılır. Çoklu dil girişi desteklemektedir.
• Açıklama: Eklenen eylemin ne iş yaptığına dair bilgi girilmesi için kullanılır. Çoklu dil girişi desteklemektedir.
• Veri kaynağı: Eylemin çalışırken kullanacağı Rest veri kaynağının seçildiği alandır. Projenin DataSource alanına eklenmiş REST Query tipindeki ögeler listelenmektedir.
### Akış Başlatma Çağıran Aksiyon
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/6-ec958722-525d-4a0a-98fd-90477a91f877.png)
Akış başlatma çağıran aksiyon seçeneğine tıklandığında, öge eylem içine eklenir. 
• Ad: Eyleme verilmek istenen adı tanımlamak için kullanılır. Çoklu dil girişi desteklemektedir.
• Açıklama: Eylemin yaptığı açıklamayı tanımlamak için kullanılır. Çoklu dil girişini desteklemektedir.
• Project: Sistemde başlatılması istenen süreç seçilmelidir.
• Flow: Project alanında seçim yapılması ile görünür. Projects alanında seçilen projede kullanabilen akışlar listelenir.
• Flow Parameters: Flow alanında seçim yapılması ile görünür. Seçilen akışta değişken nesnelerine değer gönderilmek istenirse kullanılmaktadır. Tanımlama yapılırken, paneli içinde yazılan değişkenlerde Özellik Görüntüleyici panelindeki General seçeneği aktif olmalıdır.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/7-4c10fc9a-c5c8-4e38-a040-7f10e34e910a.png)
**Not**: Akış başlatma çağıran aksiyon kulllanıldığında, seçilen akışta Akış Başlangıcı nesnesinde Doküman alanı içeriği boş ve Start Immediately seçeneği aktif olmalıdır. Akış Başlangıcı nesnesinden sonra Doküman Oluştur nesnesi kullanılarak yeni form oluşturularak ve mevcut form tanımlanması yapılır.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/8-3cd82c88-c78f-4f1d-bc04-a842b15effd9.png)
## Tetikleyici Ekleme
Tetikleyiciler sekmesindeki Ekle butonuna tıklanarak işe tanımlanmış eylemin çalışma planı şekli seçilir.
### Basit Tetikleyici
Bir işin belirli bir zamanda veya belirli bir anda tam olarak bir kez yürütülmesi ve ardından belirli bir aralıkta tekrarlanması gerektiğinde Basit tetikleyici ögesi kullanılır. Örneğin, tetikleyicinin 1 Haziran 2023 tarihinde sadece bir kere veya o gün belli aralıklarla tetiklenmesi isteniyorsa kullanılır. Tetikleyici eklendiğinde Özellik Görüntüleyici panelinde General ve Takvimler olmak üzere iki farklı tanım alanı bulunmaktadır.
![enter image description here](https://docsbimser.blob.core.windows.net/imagecontainer/9-300791a3-5b12-4ac8-98d1-00518fb74e46.png)
**General**
|Ad|Tanım|
|-|-|
|Ad| Tetikleyiciye tanımlanan ismin değiştirildiği alandır. Çoklu dil girişi desteklemektedir.|
| Açıklama| Tetikleyicinin ne iş yaptığına dair bilginin girildiği alandır. Çoklu dil girişi desteklemektedir.|
|Arasını etkinleştir|Tetikleyicinin çalışması planlanan zaman aralığının seçildiği alandır. Alanda seçilen tarih aralığı içinde tetikleyici aktif olur|.
| Sürekli tekrar et| Aktif olduğu durumda tekrar sayısı bölümü pasif hale getirilir ve “Arasını etkinleştir” bölümünde girilen tarih aralığı boyunca Aralık ve Aralık tipi referans alınarak sürekli tetikleme işlemi gerçekleşir.|
| Tekrar sayısı|Sürekli tekrar et bölümü değeri pasif olduğunda değer girilebilmektedir. Arasını etkinleştir bölümünde girilen tarih aralığında aralık ve aralık tipi referans alınarak belirlenen sayıda tetikleme işlemi yapılır.|
|Aralık|Tetikleyicinin çalışma aralığı değerinin tanımlandığı alandır, sayı değeri girilir.|
|Aralık tipi|Tetikleyicinin çalışma aralığı türünün seçildiği alandır. Seçilebilen değerler Dakika, Saat, Gündür.|
|Missfire rule|Tetikleyici herhangi bir sebeple çalışma zamanını kaçırırsa hangi işlemin yapılacağının seçimi yapılmaktadır.|

**Tekrar Olmayan Basit Tetiklemede Missfire Rule Seçimine Göre Gerçekleşecek İşlem**
|Ad|Açıklama| 
|-|-|
|FireNow| İş, planlayıcının (Scheduler) ateşlenmemesi (missfire) durumunu keşfettikten hemen sonra yürütülür. Örnek senaryo: Akış başlatma çağıran aksiyon kullanarak bir sürecin her 15 dakikada bir çalışmasını planladınız. Ancak uygulama bakım nedeniyle 30 dakika kapalıydı. Bu nedenle, misfire durumu oluşur ve scheduler, mümkün olan en kısa sürede çalıştırarak durumu kurtarmaya çalışır.|
|Ignore|İş, planlayıcının (Scheduler) ateşlenmemesi (missfire) durumunu keşfettikten hemen sonra yürütülür.|
|NextWithExistingCount| Hiçbir şey yapmaz, ateşlenmeyen tetiklemeler dikkate alınmaz ve bir sonraki ateşleme tetiklemesi yoktur. Yanlış ateşlenen tetiklemeyi tamamen atmak istenildiğinde bu seçenek kullanılır. Örnek senaryo: Tetikleyicinin bir işlemi başlatması gerekiyordu. Tetikleme işleminde hata oluştuğunda ve işlemin çalışması 2 saat geciktiğinde işleme başlamanın bir anlamı yoktur.|
|NowWithExistingCount| İş, planlayıcının (Scheduler) ateşlenmemesi (missfire) durumunu keşfettikten hemen sonra yürütülür.|
|NowWithRemainingCount|İş, planlayıcının (Scheduler) ateşlenmemesi (missfire) durumunu keşfettikten hemen sonra yürütülür.|
**Sabit Sayıda Tekrar İçeren Basit Tetikleme Tanımında Missfire Rule Seçimine Göre Gerçekleşecek İşlem**
|Ad|Açıklama| 
|-|-|
|FireNow| İlk ateşlenmeyen çalışma (misfire) hemen çalıştırılır. Kalan ateşlenmeyen çalışmalar dikkate alınmaz. Geri kalan ateşlenmemiş tetiklemeler tanımlanan aralıklarla çalışmaya devam eder.|
|Ignore|En kısa sürede kaçırılan tüm tetikleyicileri tetikler ve ardından normal programa geri döner. Örnek senaryo: Her sabah saat 9’da başlayıp 16:00’da biten saat başı çalışan bir tetikleyicide, sabah 9 ve 10’da tetikleme işleminin yapılamadığını ve bunun saat 10:15’de fark edildiğini düşünelim. Planlayıcı (scheduler) sabah 9 ve 10'da planlanan işleri hemen tetikleyecektir. Ardından saat 11'e kadar bekleyecek ve normal programa geri döner.| |NextWithExistingCount| Planlayıcı (Scheduler) hemen hiçbir şey yapmaz. Bunun yerine, bir sonraki planlanan zamanı bekler ve tüm tetikleyicileri planlanmış aralıklarla çalıştırır. Ayrıca; Planlayıcı ateşlenmeyen tetiklemeleri bir kenara atar ve bir sonraki planlanan zamanı bekler. Toplam tetikleme sayısı, belirlenen sayıdan daha az olacaktır. Örneğin, 10:15'te iki yanlış tetikleme köşeye atılır. Planlayıcı bir sonraki programlanan zamanı (11:00) bekler ve kalan tetikleyicileri 16:00'ya kadar tetikler. Etkili bir şekilde tetiklemenin kaçırılması (misfire) hiç olmamış gibi davranır.|
|NextWithRemainingCount|Planlayıcı ateşlenmeyen tetiklemeleri bir köşeye atar ve bir sonraki programlanan zamanı bekler. Toplam tetikleme çalıştırma sayısı, yapılandırılandan daha az olacaktır.| |NowWithExistingCount| İlk ateşlenmeyen tetikleyici hemen çalıştırılır. Ardından planlayıcı istenen aralığı bekler ve kalan tüm tetikleyicileri yürütür. Geçerli olarak ateşlenmeyen tetikleyicinin çalıştırılma zamanı başka bir değişiklik olmaksızın geçerli saate taşınır.|
|NowWithRemainingCount|İlk ateşlenmeyen tetikleyici hemen çalışır. Kalan ateşlenmeyen tetiklemeler bir köşeye atılır. Ateşlenmemiş tetiklemeler, istenen aralıkta çalıştırılır.|

**Sonsuz Sayıda Tekrar İçeren Basit Tetikleme Tanımında Missfire Rule Seçimine Göre Gerçekleşecek İşlem**
|Ad|Açıklama| 
|-|-|
| FireNow| İlk ateşlenmeyen çalışma (misfire) hemen çalıştırılır. Kalanlar dikkate alınmaz. Bir sonraki tetikleme işlemi, tanımlanan aralıktan sonra gerçekleşir. Geçerli olarak ilk yürütme zamanı şimdiki saate taşınır.|
|Ignore|Planlayıcı (Scheduler), tüm yanlış tetiklenen tetikleyicileri hemen çalıştıracak ve ardından plana göre devam edecektir.|
| NextWithExistingCount| Hiçbir şey yapmaz, ateşlenmeyen tetiklemeler bir köşeye atılır. Ardından planlayıcı bir sonraki programlanmış aralığı bekler ve yapılmış plana geri döner.|
|NextWithRemainingCount|Hiçbir şey yapmaz, ateşlenmeyen tetiklemeler bir köşeye atılır. Ardından planlayıcı bir sonraki programlanmış aralığı bekler ve yapılmış plana geri döner.| |NowWithExistingCount| İlk ateşlenmeyen tetikleyici hemen çalıştırılır, kalanlar bir köşeye ayrılır. Bir sonraki çalıştırma, istenen aralıktan sonra gerçekleşir. Geçerli olacak bir şekilde ilk yürütme zamanı şimdiki saate taşınır.|
|NowWithRemainingCount|İlk ateşlenmeyen tetikleyici hemen çalıştırılır, kalanlar bir köşeye ayrılır. Bir sonraki çalıştırma, istenen aralıktan sonra gerçekleşir. Geçerli olacak bir şekilde ilk yürütme zamanı şimdiki saate taşınır.|
**Takvimler**
**Arasını etkinleştir**: Schedule planının Takvimler bölümüne eklenen öge içeriğinin (Günlük, Haftalık, Aylık, Tatil, Yıllık, Cron) seçildiği alandır. Tetikletici ögesinde seçilen takvim ögesine göre, takvim içerisindeki tanımlı zaman aralığında tetikleme işlemi çalışmayacaktır.
### Günlük Zaman Aralığı Tetikleyici
Günlük zaman aralığı tetikleyici kullanılarak, tetikleyicinin ateşlenme programından zaman bloklarını hariç tutmak için kullanılır. Örneğin, hafta içi her gün saat 9:30'da bir işi başlatan bir tetikleyici oluşturulup, içinde kurumun tüm tatillerini hariç tutan bir Takvim eklenebilir. 
**General**
|Ad|Açıklama| 
|-|-|
|Ad|Tetikleyiciye tanımlanan ismin değiştirildiği alandır. Çoklu dil girişi desteklemektedir.|
| Açıklama| Tetikleyicinin ne iş yaptığına dair bilginin girildiği alandır. Çoklu dil girişi desteklemektedir.|
|Arasını etkinleştir| Tetikleyicinin çalışması planlanan zaman aralığının seçildiği alandır. Alanda seçilen tarih aralığı içinde tetikleyici aktif olacaktır.|
**Zamanlayıcı**
|Ad|Açıklama| 
|-|-|
|Aralık| Tetikleyicinin çalışma aralığı değerinin seçildiği alandır. Alanda değer Saat:Dakika:Saniye şeklinde seçimi gerçekleştirilmektedir.|
|Günlük Başlangıç/Bitiş zamanı| Tetikleyicinin çalışacağı saat aralığını belirlemek için kullanılır. Örneğin her gün saat 09:00-18:00 saatleri arasında belli bir eylemin çalışmasını istendiğinde alanda 09:00:00-18:00:00 seçimi yapılmalıdır.|
|Her gün çalıştır| Alandaki seçim aktif edilirse, seçili günlerde çalıştır alanındaki günler işaretlenmemiş olsa bile hepsi işaretli gibi algılanarak çalışacaktır. Aktif edildiğinde seçili günlerde çalıştır alanı tıklanamaz duruma geçer.|
|Tekrar sayısı| Alanda girilen değere göre, değer sayısında tetikleme işlemi gerçekleşir. (Misfire olmadığı durumda)|
|Seçili günlerde çalıştır|Tetikleyicinin çalışması istenilen günlerin seçildiği alandır.|
| Missfire rule| Tetikleyici herhangi bir sebeple çalışma zamanını kaçırırsa hangi işlemin yapılacağının seçimi yapılır. Alanda DoNothing, FireAndProceed ve Ignore seçenekleri bulunmaktadır. **DoNothing**: Tüm ateşlenmemiş tetiklemeler bir köşeye atılır, planlayıcı sadece bir sonraki programlanan zamanı bekler. **FireAndProceed**: Derhal ilk ateşlenmeyen tetiklemeyi çalıştırır ve diğerlerini bir köşeye atar (yani, tüm ateşlenmeyen tetiklemeleri bir araya getirilir). Ardından yapılan programa geri döner. Kaç tane tetikleme ateşlemesi kaçırılmış olursa olsun, yalnızca tek bir tetikleme gerçekleştirilir.**Ignore**: Tüm ateşlenmeyen tetiklemeler hemen yürütülür, ardından tetikleme yapılan programa göre çalışır.|
|Saat dilimi| Tetikleyicinin çalışacağı saatin hangi zaman dilimine hesaplanacağının belirlendiği alandır. Örneğin Günlük Başlangıç/Bitiş zamanı alanında 09:00-18:00 değeri seçildiyse ve Saat diliminde UTC+03 Istanbul seçildiyse ve sistemin bulunduğu sunucu UTC+03 ile çalışıyorsa tetikleyici çalışma aralığı 09:00-18:00 olacaktır. Ancak saat dilimine UTC-03 Greenland seçilip, sistemin çalıştığı sunucu UTC+03 olarak ayarlı ise, başlangıç/bitiş saatindeki değerler UTC+03 saatine göre 15:00-03:00 aralığında çalışacaktır. (Istanbul saati 15:00 iken Greenland’de 09:00 olacaktır)|

**Takvimler**

 - **Arasını etkinleştir**:  Schedule planının Takvimler bölümüne eklenen öge içeriğinin (Günlük, Haftalık, Aylık, Tatil, Yıllık, Cron) seçildiği alandır. Tetikletici ögesinde seçilen takvim ögesine göre, takvim içerisindeki tanımlı zaman aralığında tetikleme işlemi çalışmayacaktır.
 ### Cron Tetikleyici
 Basit tetikleyicinin tam olarak belirtilen aralıkları yerine takvim benzeri kavramlara dayalı olarak yinelenen bir iş başlatma programına ihtiyacınız varsa, Cron tetikleyici genellikle basit tetikleyiciye göre daha kullanışlıdır.
Cron tetikleyici ile "her Cuma öğlen" veya "hafta içi her gün ve sabah 9:30", hatta "Ocak ayı boyunca her Pazartesi, Çarşamba ve Cuma günü saat 9:00 ile 10:00 arasında her 5 dakikada bir" gibi ateşleme programları belirleyebilirsiniz.

**General**
|Ad|Açıklama| 
|-|-|
| Ad|Tetikleyiciye tanımlanan ismin değiştirildiği alandır. Çoklu dil girişi desteklemektedir.|
|Açıklama| Tetikleyicinin ne iş yaptığına dair bilginin girildiği alandır. Çoklu dil girişi desteklemektedir.|
| Arasını etkinleştir| Tetikleyicinin çalışması planlanan zaman aralığının seçildiği alandır. Alanda seçilen tarih aralığı içinde tetikleyici aktif olacaktır.|
| İfade| Çalışma şeklini belirleyecek cron ifadesinin yazıldığı alandır.|
|Missfire rule| Tetikleyici herhangi bir sebeple çalışma zamanını kaçırırsa hangi işlemin yapılacağının seçimi yapılmaktadır. Alanda DoNothing, FireAndProceed ve Ignore seçenekleri bulunmaktadır. **DoNothing**: Tüm ateşlenmemiş tetiklemeler bir köşeye atılır, planlayıcı sadece bir sonraki programlanan zamanı bekler. **FireAndProceed** : Derhal ilk ateşlenmeyen tetiklemeyi çalıştırır ve diğerlerini bir köşeye atar (yani, tüm ateşlenmeyen tetiklemeleri bir araya getirilir). Ardından yapılan programa geri döner. Kaç tane tetikleme ateşlemesi kaçırılmış olursa olsun, yalnızca tek bir tetikleme gerçekleştirilir. ** Ignore**: Tüm ateşlenmeyen tetiklemeler hemen yürütülür, ardından tetikleme yapılan programa göre çalışır.|
| Saat dilimi| Tetikleyicinin çalışacağı saatin hangi zaman dilimine hesaplanacağının belirlendiği alandır. Örneğin İfade alanında her gün öğlen saat 12:00 gibi bir cron tanımı yapıldığında, saat diliminde UTC+03 İstanbul seçili ve sistemin bulunduğu sunucu UTC+03 ile çalışıyorsa tetikleyici saat 12:00’de çalışacaktır. Ancak saat dilimine UTC-03 Greenland seçilip, sistemin çalıştığı sunucu UTC+03 olarak ayarlı ise, cron ifadesine göre Greenland’de (UTC-03) öğlen saat 12:00 yani İstanbul’da 18:00 olduğunda tetikleyici devreye girecektir.|

**Bazı Cron Örnekleri**
|Cron Metni|Açıklama| 
|-|-|
|0 * * ? * *|Her dakikada bir| 
|0 */30 * ? * *| Her 30 dakikada bir|
|0 0 * ? * *|Her saatte bir|
| 0 0 */12 ? * *| Her 12 saatte bir|
|0 0 0 * * ?|Her gün gece yarısında|
| 0 0 6 * * ?| Her gün sabah saat 6’da|
|0 0 12 * * ?|Her gün öğlen saat 12’de|
| 0 0 12 ? *| MON Her Pazartesi öğlen saat 12’de|
|0 0 12 ? * MON-FRI|Hafta içi her gün öğlen saat 12’de|
| 0 0 12 ? * SUN,SAT| Hafta sonu her gün öğlen saat 12’de|
|0 0 12 15 * ?|Her ayın 15’inde öğlen saat 12’de|
| 0 0 12 LW * ?| Her ayın son hafta içi günü öğlen saat 12’de|
|0 0 12 1L * ?|Her ayın son Pazar günü öğlen saat 12’de|
| 0 0 12 6L * ?| Her ayın son Cuma günü öğlen saat 12’de|
|0 0 12 1W * ?|Her ay ayın 1'ine en yakın hafta içi günü öğlen 12’de|
| 0 0 12 15W * ?| Her ay ayın 15'ine en yakın hafta içi günü öğlen 12’de|
|0 0 12 ? * 2#1|Her ayın ilk Pazartesi günü öğlen saat 12’de|
| 0 0 12 ? * 6#1| Her ayın ilk Cuma günü öğlen saat 12’de|
|0 0 12 ? JAN *| Ocak ayı boyunca her gün öğlen saat 12’de|
| 0 0 12 ? JAN,JUN *| Ocak ve Haziran ayı boyunca her gün öğlen saat 12’de|
|0 0 12 ? 9-12 *|Eylül ve Aralık ayları arasında her gün öğlen|

**Takvimler**
• Arasını etkinleştir: Schedule planının Takvimler bölümüne eklenen öge içeriğinin (Günlük, Haftalık, Aylık, Tatil, Yıllık, Cron) seçildiği alandır. Tetikletici ögesinde seçilen takvim ögesine göre, takvim içerisindeki tanımlı zaman aralığında tetikleme işlemi çalışmayacaktır

## Oluşturulan Schedule içinde Takvimler Bölümüne Öge Tanımlama
Oluşturulan Schedule planında çalışması istenen zaman aralığı içerisinde çalışmaması istenen tarihler olması isteniyorsa, bu tarihler Takvimler kısmından oluşturulmaktadır. Takvimler sekmesinde Ekle butonuna tıklanıldığında açılan pencerede seçilebilecek ögeler Günlük, Haftalık, Aylık, Tatil, Yıllık ve Cron’dur.
### Günlük
|Ad|Açıklama| 
|-|-|
| Ad| Takvime tanımlanan ismin değiştirildiği alandır. Çoklu dil girişi desteklemektedir.|
|Açıklama| Takvimin ne iş yaptığına dair bilginin girildiği alandır. Çoklu dil girişi desteklemektedir.|
|Günlük Başlangıç/Bitiş zamanı| Takvimin geçerli olduğu zaman aralığının seçildiği alandır. Alanda değer, Saat:Dakika:Saniye şeklinde seçimi gerçekleştirilir. Örneğin her gün saat 09:00-18:00 saatleri arasında belli bir eylemin çalışması engellenecekse alanda 09:00:00-18:00:00 seçimi yapılmalıdır.|
| Saat dilimi| Günlük takvim ögesinin tanımlı olacağı, saat Günlük başlangıç/bitiş zamanı alanında seçilen değerin hangi saat dilimine göre hesaplanacağının belirlendiği alandır.|
### Haftalık
|Ad|Açıklama| 
|-|-|
| Ad| Takvime tanımlanan ismin değiştirildiği alandır. Çoklu dil girişi desteklemektedir.|
| Açıklama| Takvimin ne iş yaptığına dair bilginin girildiği alandır. Çoklu dil girişi desteklemektedir.|
|Hariç tutulan günler| Seçim yapılarak tetikleyici içinde hangi günlerin çalışmayacağının belirlendiği alandır.|
|Saat dilimi|Takvimin tanımlı olacağı zaman diliminin belirlendiği alandır.|
###  Aylık
|Ad|Açıklama| 
|-|-|
| Ad| Takvime tanımlanan ismin değiştirildiği alandır. Çoklu dil girişi desteklemektedir.|
| Açıklama| Takvimin ne iş yaptığına dair bilginin girildiği alandır. Çoklu dil girişi desteklemektedir.|
|Hariç tutulan günler| Listelenen günler arasında seçim yapılarak, takvimde hangi günlerin dâhil edilmeyeceğinin belirlendiği alandır.|
| Saat dilimi| Takvimin tanımlı olacağı zaman diliminin belirlendiği alandır.|

###  Tatil
|Ad|Açıklama| 
|-|-|
| Ad| Takvime tanımlanan ismin değiştirildiği alandır. Çoklu dil girişi desteklemektedir.|
| Açıklama| Takvimin ne iş yaptığına dair bilginin girildiği alandır. Çoklu dil girişi desteklemektedir.|
| Hariç tutulan günler| Alanda yapılacak seçim ile hariç tutulacak günler tanımlanmaktadır. İçinde birde fazla hariç gün tanımı yapılabilir.
| Saat dilimi| Takvimin tanımlı olacağı zaman diliminin belirlendiği alandır.|
###  Yıllık
|Ad|Açıklama| 
|-|-|
| Ad| Takvime tanımlanan ismin değiştirildiği alandır. Çoklu dil girişi desteklemektedir.|
| Açıklama| Takvimin ne iş yaptığına dair bilginin girildiği alandır. Çoklu dil girişi desteklemektedir.|
| Hariç tutulan günler| Alanda yapılacak seçim ile hariç tutulacak günler tanımlanmaktadır. İçinde birde fazla hariç gün tanımı yapılabilir.|
|Saat dilimi| Takvimin tanımlı olacağı zaman diliminin belirlendiği alandır.|
###  Cron
|Ad|Açıklama| 
|-|-|
| Ad|Takvime tanımlanan ismin değiştirildiği alandır. Çoklu dil girişi desteklemektedir.|
|Açıklama| Takvimin ne iş yaptığına dair bilginin girildiği alandır. Çoklu dil girişi desteklemektedir.|
| İfade| Takvimin geçerli olacağı cron ifadesinin yazıldığı alandır.|
| Saat dilimi| Takvimin tanımlı olacağı zaman diliminin belirlendiği alandır.|
