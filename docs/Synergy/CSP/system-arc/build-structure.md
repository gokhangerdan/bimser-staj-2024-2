---
sidebar_label: Proje Derleme Yapısı
sidebar_position: 4
custom_edit_url: ""
---

# Proje Derleme Yapısı

![Derleme Yapısı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd4dc0c3-cf58-430c-9142-ab1200ba52cb)

Synergy yapısında proje derleme işlemi, birbirinden bağımsız (asenkron) şekilde yapılan **İstemci Derleme (Client Build)** işlemi ve **Sunucu Derleme (Server Build)** işlemi olarak ikiye ayrılır.

Entegre Geliştirme Ortamı’nda oluşturulan bir proje derlendiğinde, görseldeki Build aşamalarından geçtikten sonra, artık kendi başına çalışabilir bir **MicroService** haline gelir. Projenin, Form ve Akış (Flow) kısımları derlenip birleştirilerek Build işlemi sonunda, Docker Registry’de Container oluşturulabilecek bir **image** haline getirilir. Bu image yapısının içinde;

- Form Engine
- Workflow Server
- Integration Manager Server (DataSource)

gibi modüller bulunur. Bu image yapısına gerekli parametreler (mail server adresi, gRPC bağlantı adresi, database bilgileri, script’ler vs.) verildiğinde, istenen her yerde bağımsız çalıştırılabilir.

Synergy yapısında, kiracılara ait tüm projeleri, kiracıya tahsis edilmiş ve diğer kiracı ortamlarından tamamen izole edilmiş isim uzaylarında (Namespace) çalıştıran **User Applications Kubernetes Cluster** ortamı mevcuttur. Kiracının kendisine tahsis edilmiş Namespace’inin içinde bir Container yaratılarak, kiracıya ait projeler bu Container içinde Build edilir.

Her derleme işlemi sonrası projenin yeni bir versiyonu oluşmaktadır. Derleme sonucu oluşan Container içerisinde projenin yeni versiyonu ile birlikte o projenin, devam etmekte olan eski versiyonlarına ait paketler de bulunur. Böylece derleme sonucu proje yeni versiyonu ile kullanılabileceği gibi, projenin devam etmekte olan eski versiyonlu halleri de çalışabilir durumda olur.

Derleme işleminden sonra oluşan Container, ilgili Namespace’de çalışmaya hazır haldedir. Bu Namespace içinde ihtiyaca göre projeye ait Container scale olabilir. Örneğin; çok yoğun kullanılan bir projeye ait Container, ihtiyaç durumunda scale olarak ihtiyacı karşılayacak şekilde çoğaltılabilir.

Proje paketlerinin içinde Integration Manager servisi de bulunur. Bunun sebebi, her projenin kendi Integration Manager servisini kullanmasını sağlamak ve yoğunluk durumunda projeye ait Container’ın çoğaltılması ile Integration Manager’daki yükü de dengelemektir. Bu durum, aynı zamanda herhangi bir projede kullanılan performanssız bir sorgunun, sistemdeki diğer tüm projelerin performansını olumsuz etkilemesinin de önüne geçmektedir.

Sistemde bulunan **İzleme (Monitoring)** yapısı sayesinde, projelerde kullanılan sorguların performansları değerlendirilebilir, sorgunun çalışması sırasında sistem üzerinde dolaştığı adımlar incelenerek hangi adımda ne kadar gecikme yaşandığı gözlemlenebilir.