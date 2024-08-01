---
sidebar_label: Çalıştır
sidebar_position: 2
custom_edit_url: ""
---

# Çalıştır

Geliştirilen bir projenin kullanıma sunulması ya da kullanımda olan bir proje üzerinde yapılan değişikliklerin devreye alınması için gerekli işlem seçenekleri bu başlık altında bulunur.

Derleme; tüm proje bileşenlerinin, dizayn ve kod kısımlarının tek bir çıktı halinde toplanmasını sağlayan işlemdir. Geliştirme arayüzünde açık olan projeyi ya da çözümü derleme, projenin belirli bölümlerini derleme, derlenen projeyi yayınlama ya da işlemi iptal etme seçenekleri, Çalıştır başlığı altından yürütülür.

![Çalıştır](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8483729-d281-45c1-a461-2b019fe0a622)

- **Çözümü Derle :** Geliştirme arayüzünde açık olan çözümü derlemek için kullanılan seçenektir. Çözümü derle seçeneği ile, arayüzde açık olan çözüm içerisindeki proje veya projeler derlenmiş olur. Çözümün altında bulunan her proje için, Projeyi Derle işlemi çalıştırılmış olur.

- **Projeyi Derle :** Geliştirme arayüzünde açık olan projeyi derlemek için kullanılan seçenektir. Proje içerisinde bulunan tüm dosyalar, kodlar, dizayn ekranları ve diğer bileşenler, proje derleme işlemi sonrası yayınlamaya hazır bir paket haline gelir. Geliştirilen projenin kullanıma açılabilmesi için öncelikle başarıyla derlenebiliyor olması gerekmektedir. Başarıyla derlenen bir proje, yayınlanmaya hazır demektir.

- **İstemciyi Derle :** Projenin frontend kısmına yazılan, Html, TypeScript, Css kodlarının ve harici kaynaklardan projeye referans edilen frontend kütüphanelerinin derlenmesi için kullanılan seçenektir. Başarıyla derlenmiş bir projenin, sadece frontend kod kısımlarında değişiklik yapılmışsa, komple projeyi derlemektense İstemciyi Derle seçeneği ile sadece frontend kısımlarındaki değişiklikler derlenebilir. Derleme başarılı ise proje tekrar güncel frontend kodlarıyla yayınlanmaya hazır hale gelir.

- **Sunucuyu Derle :** Projenin backend kısmına yazılan, .NET Core kodlarının ve harici kaynaklardan projeye referans edilen backend kütüphanelerinin derlenmesi için kullanılan seçenektir. Başarıyla derlenmiş bir projenin, sadece backend kod kısımlarında değişiklik yapılmışsa, komple projeyi derlemektense Sunucuyu Derle seçeneği ile sadece backend kısımlarındaki değişiklikler derlenebilir. Derleme başarılı ise proje tekrar güncel backend kodlarıyla yayınlanmaya hazır hale gelir.

- **Workflowu Derle :** Projenin, tasarlanmış akış kısmının derlenmesi için kullanılan seçenektir. Projenin, sadece akış tasarımında ya da kodlarında herhangi bir değişiklik yapılmışsa, komple projeyi derlemektense Workflowu Derle seçeneği kullanılarak akış kısmının derlenmesi sağlanabilir. Derleme başarılı ise proje tekrar güncel akış yapısı ile yayınlanmaya hazır hale gelir.

- **İptal :** Derleme veya yayınlama işlemleri iptal edilmek istendiğinde kullanılabilecek seçenektir. Derleme ya da yayınlama işlemi sırasında iptal seçeneğine basıldığında o esnada çalışan işlem iptal edilmiş olur.

- **Yayınla :** Geliştirme arayüzünde oluşturulan bir projenin kullanıma açılabilmesi için öncelikle başarılı bir şekilde derlenmesi gerekmektedir. Başarıyla derlenen bir proje, kullanıma açılmak için yayınlamaya hazır demektir. Geliştirme arayüzünde tasarlanmış ve Yayınla seçeneği ile yayınlanmış bir proje, artık kullanıcılar tarafından veya sistem içerisinde belirlenen bir görevde, aktif olarak kullanıma hazır hale gelmiş bir proje olmuş olur. Aynı proje için her yayınla butonuna basıldığında, sistemde projenin yeni versiyonları oluşturulur. Oluşan her proje versiyonu ayrı bir proje gibi düşünülebilir ve kullanılabilir. Proje bileşenleri üzerinde herhangi bir değişiklik yapıldıktan ve derleme işlemi gerçekleştirildikten sonra yayınla butonuna basılmadığı sürece bu değişiklikler kullanıma açılmamış olacaktır.