# Form Yaşam Döngüsü ve Olayları

![lifecyle](https://docsbimser.blob.core.windows.net/imagecontainer/lifecycle-2be04462-9b6f-42e6-bd9d-cba48936a65d.png)

## Client ve Server Farkı

**Client** ile **Server** arasındaki temel fark , istemcinin(client) web üzerinden hizmet talep eden bir makine veya program, sunucunun(server) ise istemcinin isteklerine göre istemcilere hizmet sağlayan bir makine veya program olmasıdır.
Form üzerindeki herhangi bir nesneye belli bir anda değer atanmak isteniyorsa ya da nesnelerin görünür olup olmaması, değer girişine izin verilip verilmemesi, doldurulması zorunlu alanlar olup olmaması kontrol edilmek isteniyorsa, client olayları tercih edilmelidir. Bunun temel sebebi de Server tarafında yapılacak bir kodlama işleminde sunucuyla iletişime geçilmesinden kaynaklı yavaşlık yaşanmasıdır.
Ancak herhangi bir olay sırasında, bir veri kaynağından kod yazılarak veriler çekilmek isteniyorsa Server tarafında yazılması daha doğru bir yöntemdir. Bunun en temel sebebi de uygulamada güvenlik zaafiyeti oluşmasına engel olmaktır.
:::info BİLGİ
Tarayıcıların developer toolları ile client tarafında projeyi tekrar yayınlamaya gerek kalmadan da kodlar yazılabilir, debug yapılabilir ve yazılan kodların testleri de gerçekleştirilebilmiş olur.
:::

## Form Eventleri

**OnInit**
OnInit eventi, form yaratıldığı (initialize) anda tetiklenen bir olaydır. Bu olay, form yüklenirken veya oluşturulurken gerçekleşir.
OnInit eventi, sayfanın yaşam döngüsünün başlangıcında gerçekleştirilir. Formun ilk başlatılması sırasında yapılması gereken işlemleri gerçekleştirmek için kullanılır. Bu işlemler genellikle başlangıç değerlerini ayarlamak, kaynakları yüklemek, veritabanı bağlantılarını oluşturmak, diğer bileşenleri yaratmak veya formun başlangıç durumunu ayarlamak gibi işlemleri içerir. 

**OnLoad**
OnLoad eventi, form yüklendiği zaman tetiklenen bir olaydır. Bu olay, formun kullanıcıya görüntülendiği anda gerçekleşir.
OnLoad eventi,  formun yüklendikten sonra yapılması gereken işlemleri gerçekleştirmek için kullanılır. Bu işlemler genellikle kullanıcı arabirimi (user interface) ile ilgilidir. Örneğin, formun tam yüklenmesiyle birlikte, formdaki metinleri veya görselleri değiştirmek, kullanıcıya bir mesaj göstermek, veri tabanından veri çekmek veya diğer dinamik içerikleri oluşturmak gibi işlemler OnLoad eventinde gerçekleştirilebilir.

**OnPropertyChanged**
OnPropertyChanged eventi, formun özelliklerinde (properties) değişiklik olduğunda tetiklenen bir olaydır. Bu olay, bir özelliğin değeri değiştiğinde otomatik olarak tetiklenir ve bu değişikliği takip etmek veya buna tepki vermek için kullanılır.
OnPropertyChanged eventi, genellikle nesneler arasındaki iletişimi ve veri güncellemelerini kolaylaştırmak için kullanılır. Bir nesnenin bir özelliği değiştiğinde, diğer nesnelerin bu değişiklikten haberdar olması ve uygun şekilde tepki vermesi gerekebilir. OnPropertyChanged eventi, bu iletişimi sağlamak için bir araç olarak kullanılır.

**OnClick**
OnClick eventi, form üzerinde herhangi bir yere tıkladığında tetiklenen bir olaydır. Bu olay, kullanıcının fareyle bir butona, bir nesne alanına, bir resme veya başka bir öğeye tıkladığı zaman gerçekleşir.
OnClick eventi, kullanıcının etkileşimini algılamak ve bu etkileşime uygun tepki vermek için kullanılır. Bir öğeye tıklandığında gerçekleştirilmek istenen işlemler, onClick eventi içinde tanımlanır. Bu işlemler, örneğin bir metodu çağırmak, bir nesnenin değerini değiştirmek veya bir öğenin görünümünü değiştirmek gibi olabilir.

**OnPreRender**
OnPreRender eventi, form sunulmadan (render) önce tetiklenen bir olaydır. Bu olay, form tamamen işlendikten ve kullanıcıya gösterilmeden hemen önce gerçekleşir.
OnPreRender eventi, formun son düzenlemelerini yapmak veya son kontrolleri gerçekleştirmek için kullanılır. Bu olayda, formdaki verileri güncelleme, kontrollerin görünümünü veya durumunu değiştirme veya diğer nihai düzenlemeleri yapma gibi işlemler gerçekleştirilebilir.

**OnBeforeSave**
OnBeforeSave eventi, form kaydedilmeden önce (save) tetiklenen bir olaydır. Bu olay, kaydetme işlemi başlamadan önce gerçekleşir ve formun ve verilerin kaydedilme süreci üzerinde kontrol sağlar.
OnBeforeSave eventi genellikle verilerin geçerliliğini doğrulama, değişiklikleri kaydetme veya diğer ön-kaydetme kontrollerini yapma gibi işlemler gerçekleştirilebilir.

**OnAfterSave**
OnAfterSave eventi, form kaydedildikten sonra (save) tetiklenen bir olaydır. Bu olay, kaydetme işleminden sonra yapılması gereken işlemleri gerçekleştirmek için kullanılır.
OnAfterSave eventi genellikle veritabanı işlemlerinde, verinin durumunu güncelleme, kaydetme işlemi sonrası mesajları gösterme, iş akışını tetikleme veya diğer kaydetme sonrası işlemlerinde kullanılır.

**OnBeforeCommit**
OnBeforeCommit eventi, form veritabanına kaydedilmeden önce (commit) tetiklenen bir olaydır. Bu olay, işlemi gerçekleştirmek üzere veritabanına kaydetme adımına gelinmeden önce gerçekleşir.
OnBeforeCommit eventi,  işlemi tamamlamadan önce yapılan son kontroller veya işlemler için kullanılır. Bu olayda, işlemdeki verilerin doğruluğunu kontrol etme, işlem sırasında hata veya uyarı mesajları gösterme veya diğer ön-kaydetme kontrollerini yapma gibi işlemler gerçekleştirilebilir.

**OnCommit**
OnCommit eventi, veritabanı işleminin tamamlanmasından hemen sonra tetiklenen bir olaydır. Bu olay, işlem tamamlandıktan sonra ilgili işlem sonrası işlemleri gerçekleştirmek için kullanılır.
OnCommit eventi, formu kaydetme, onaya gönderme gibi form üzerinde herhangi bir olay gerçekleştiğinde tetiklenir.

**OnRollBack**
OnRollBack eventi, bir işlem veya veritabanı işlemi geri alındığında (rollback) tetiklenen bir olaydır. Bu olay, işlem geri alındıktan sonra ilgili işlem sonrası işlemleri gerçekleştirmek için kullanılır.
OnRollBack eventi genellikle veritabanı işlemlerinde kullanılır ve işlem geri alındıktan sonra gerçekleştirilmesi gereken işlemler için kullanılır. Bu olayda, işlem geri alındıktan sonra veri geri yükleme, loglama, hata işleme veya diğer geri alma sonrası işlemler gerçekleştirilebilir.

**OnValidating**
OnValidating eventi, bir girdinin doğrulama süreci sırasında tetiklenen bir olaydır. Kullanıcıdan alınan verilerin geçerliliğini kontrol etmek için kullanılır. Bu olay, verilerin geçerli olup olmadığını kontrol etmek, hataları yakalamak, zorunlu alanları kontrol etmek ve kullanıcıya geri bildirim sağlamak için kullanılır. OnBeforeSave olayından sonra OnAfterSave olayından önce çalışır.

**OnToolbarButtonClicked**
OnToolbarButtonClicked eventi, form üzerinde tanımlı bir toolbar button'a basıldığında tetiklenen bir olaydır. Form üzerindeki herhangi bir alanda değişiklik veya kontrol yapılmak istendiğinde, yeni bir formun açılması sağlamak veya mevcut form üzerindeki bir dokümanı indirmek gibi işlemler yapılmak istendiğinde kullanılabilir. 

**OnUnload**
OnUnload eventi, formun kullanıcı tarafından terk edildiği (unload) zaman tetiklenen bir olaydır. Bu olay, kullanıcı sayfadan ayrıldığında veya sayfayı yenilediğinde gerçekleşir.
OnUnload eventi, form kapatıldığı anlarda yapılması gereken işlemleri gerçekleştirmek için kullanılır. Bu işlemler formdan ayrılma öncesi kaynakları serbest bırakmak, verileri kaydetmek veya diğer temizleme işlemlerini yapmak gibi işlemleri içerir.
Kullanıcı, bir formu doldurup sayfadan ayrıldığında, bu olay tetiklenir ve formdaki verileri sunucuya göndermek veya bir veritabanına kaydetmek gibi işlemler gerçekleştirilebilir.

**OnChildFormReturn**
OnChildFormReturn eventi, mevcut formun bağlı olduğu farklı bir form bulunuyorsa o formdan dönen değerlerin yakalandığı olaydır.

### Eventlerin Tetiklenme Sırası
Form açıldıktan sonra sırasıyla OnInit > OnPreRender > OnLoad > OnRender > OnPropertyChanged > OnRender olayları çalışır. Formdaki kaydedildiğinde ya da akış üzerinde ilerletildiğinde ise sırasıyla OnBeforeCommit > OnBeforeSave > OnRender > OnAfterSave > OnCommit eventleri çalışır.

