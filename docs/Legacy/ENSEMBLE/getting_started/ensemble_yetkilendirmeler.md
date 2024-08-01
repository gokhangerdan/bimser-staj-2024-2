# Ensemble Yetkilendirmeler

## Menü Yetkileri ve Modül Yöneticisi Yetkilendirmeleri

Ensemble uygulamasında 2 farklı yetkilendirme bulunmakta. Bunlardan ilki menü yetkilendirmesidir. Menü yetkilendirmesi ilgili kullanıcın menüleri görüntüleyebilmesi ve tıklayabilmesini sağlar, bu sayede ilgili sayfa açabilecek duruma gelecektir.
Bir diğer yetkilendirme ise, ilgili sayfalar üzerinde bulunan/yapılan tanımlamalara dair yetkilendirmedir. İlgili sayfayı herhangi bir kullanıcın açabilmesi, o sayfada tüm işlemleri yapabileceği anlamını taşımamaktadır.
(Örn: Süreçler sayfasını açabilen bir kullanıcı yeni süreç ekleyemez, yeni süreç ekleme sadece süreç yönetimi modülü yöneticileri tarafından yapılabilir.
Bu durumda yeni süreç ekleyebilmek için kullanıcının menü yetkisinin bulunması ve süreç yönetimi modülü yöneticisi olarak tanımlı olması gerekir.)
Dolayısıyla bir kullanıcı için yetkilendirme yapılırken öncelikle ilgili sayfanın menüsünde yetkisi var mı yani sayfayı açabiliyor mu kontrol edilmelidir. Akabinde ilgili sayfada yapması istenen işlem üzerinde yetkilendirme sağlanmalıdır.
(Örn: Tanımlı bir süreci görüntülemek için öncelikle menü yetkisi olması gerekir, sonrasında ilgili süreç üzerinde görüntüleme yetkisi olmalıdır. Görüntüleme yetkisi olmayan bir süreç ilgili kullanıcıda, ilgili sayfayı açabildiği halde gözükmez)
Modül yöneticisi olarak tanımlı bir kullanıcı ise, menü yetkisine sahip olduğu tüm sayfalarda herhangi bir yetki kısıtına takılmaksızın tüm işlemleri gerçekleştirebilir, ancak sadece yönetici olmak yetmeyecektir çünkü menüleri görebilmesi ve sayfaları açabilmesi gerekir. 

___

Menü Yetkisi; QDMS uygulaması üzerinden kullanıcı grubu bazlı verilebilmektedir. Kullanıcının bağlı olduğu kullanıcı grubu ile ilişkili olan yetki grubuna üzerinden menü yetkileri tanımlanır ("Sistem Altyapı Tanımları > BSAT > Tanımlar > Yetki Grupları Tanımlama"). Bu durumda, yetki grubu ile ilişkili olan kullanıcı grubundaki her bir kullanıcı için bu menü yetkileri verilmiş olacaktır.

Modül Yönetici Yetkisi; Bir kullanıcıyı ilgili modül(ler)de yönetici olarak tanımlamak için QDMS uygulaması ara yüzünden 
"Sistem Altyapı Tanımları > BSAT > Konfigürasyon Ayarları > Yönetici Tanımlama" menü yolunu takip ederek açılan sayfada kullanıcı için istenilen modüllerde ekleme yapılmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-32b70c3b-d03d-41e4-bef9-db5f1a0debf4.png)

___

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-e7198b41-0c58-40ba-9b70-da02297e7f1a.png)

___

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-702b23cf-09d4-4f72-8051-9e5a14a786fa.png)

___

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-56f054d0-ebf8-479e-a396-11ebd066cbb6.png)