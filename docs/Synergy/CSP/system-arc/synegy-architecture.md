---
sidebar_label: Synergy Mimari Dokümanı
sidebar_position: 3
custom_edit_url: ""
---

# Synergy Mimari Dokümanı

![Synergy Mimari](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload24278aa3-2ea2-4cc3-a97d-f509360481ce)

Bimser Synergy mimarisi temel olarak 3 adet **Kubernetes Cluster** yapısından oluşmaktadır;

- Tüm sistemsel işlemlerin yürütüldüğü ana **Bimser Kubernetes Cluster**,

- Yine sistem altyapısında çalışan ancak, kullanımı gereği çok fazla kaynak tüketebilecek potansiyelde olan (Indexing, Elastic Search, Alert Manager, Logging gibi) işlemlerin yürütüldüğü **Utility Kubernetes Cluster**,

- Ve kiracılara ait tüm projeleri, kiracıya tahsis edilmiş ve diğer kiracı ortamlarından tamamen izole edilmiş isim uzaylarında (namespace) çalıştıran **User Applications Kubernetes Cluster** mevcuttur.

Bu Kubernetes ortamlarının yönetimi, **Azure Kubernetes Service (AKS)** tarafından gerçekleştirilir. AKS, uygulamayı çevrimdışı duruma getirmeden, yükseltme (upgrading) ve ihtiyaç üzerine kaynak ölçeklemesi (scaling) sağlayarak, devam eden operasyonların ve bakımın yükünü ortadan kaldırır.

Uygulama içerisinde bir Container teknolojisi olan **Docker** teknolojisi kullanılmıştır. Docker, uygulamaların Container olarak bulutta ya da On-premise de çalıştırılabilmesini sağlayan teknolojidir. Container’ları kullanarak uygulamaların, oluşturma (create), dağıtım (deployment) ve çalıştırma (run) işlemlerini kolaylaştırmayı sağlar.

Bir Kubernetes Cluster yapısının temel bileşenleri; **Container**, **Pod** ve **Node** elemanları olarak belirtilebilir.

![Synergy Mimari](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac4371dc-4fd6-4ac9-9249-b371738c4db6)

**Container**, birbirinden izole edilmiş, kendisine ait yazılım, kütüphane ve konfigurasyon dosyalarını içinde barındıran, iyi tanımlanmış kanallar ile birbirleriyle haberleşebilen yapılardır. Bu Container yapıları, container çalışma alanı denilen **Pod**’ların içerisinde konumlanır. Bir Pod içerisinde birden fazla Container çalışabilir. Pod yapıları ise, Kubernetes de çalışan bir makine olan Node’ ların içerisinde çalışır. **Node**’lar, Cluster’a bağlı bir sanal makine (VM) veya fiziksel makine olabilir. Her Node, Pod’ların çalışması için gerekli servisleri içerir ve ana bileşen tarafından yönetilir.

Sistem kullanım yoğunluğu arttığında ihtiyaca göre Node’ların çoğaltılması (scaling) işlemi AKS tarafından gerçekleştirilir. İhtiyaç duyulan Node yapısı ile aynı yapıya sahip yeni bir Node oluşturulur ve gelen yeni istekler bu Node tarafından karşılanarak yoğunluk durumu yönetilir. İhtiyaç ortadan kalktığında ise fazla Node’lar, içerisinde çalışan Pod varsa diğer Node’lara devredilerek kapatılır. Aynı şekilde Pod ların duruma göre scale olma ya da azaltılma işlemleri ise Kubernetes tarafından yönetilir. İhtiyaca göre ölçeklenebilen bu yapı, sistemin esnek ve performanslı çalışmasını sağlar. Bununla birlikte, kaynak yönetimi sistem tarafından ihtiyaca göre otomatik gerçekleştirilmiş olur.

![Synergy Mimari](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf422234-74ca-44f9-b47e-9dee444e29ab)

Sistem Cluster’ı içerisinde, servislerin kendi arasındaki mesajlaşmalarını yöneten araç olarak [Akka](https://doc.akka.io/docs/akka/2.4/intro/what-is-akka.html) kullanılır. Akka, aktör modelini kullanarak, soyutlama seviyesini artırıp, ölçeklenebilir, esnek ve duyarlı uygulamalar oluşturmak için kullanılmaktadır. Kendisine gelen isteği, o isteği yapacak olan **aktöre (Worker)**, kendi belirlediği yoldan yönlendirerek mesajlaşmayı sağlar.

Akka mesajlaşma yapısının en başında **LightHouse (LH)** yer alır. Sistemdeki her bir servis ayağa kalktığında, yapıya dahil olduğunu LightHouse’a haber verir. LightHouse ise kendisine gelen bu bilgiyi sistemdeki diğer servislere bildirir. Aynı mesajlaşma şekli, bir servis, yapıdan ayrılacağı zaman da gerçekleşir. Böylece LightHouse sayesinde sistemdeki servisler, birbirlerinden haberdar olmuş olurlar.

Client’dan bir istek geldiğinde bu istek, ilgili servisin WebAPI’ si tarafından karşılanır ve servisin Router’ ına gönderilir. Router, işi yapacak olan Aktör (Worker)’lerden o an uygun olana işi yönlendirir. **Aktör (Worker)**, iş yapabilen bir süreç veya iş parçacığıdır. Kendi sorumluluğundaki işi yerine getirmekle yükümlüdür.

Akka’nın da kendi içinde, ihtiyaç olması durumunda yoğunluğu karşılayabilmek için ölçekleme (scailing) mekanizması mevcuttur. Normalde Aktörlerin içinde 5 adet thread bulunur. Yoğunluk arttığında bu thread sayısı 10’a kadar artırılabilir. Ancak bu şekilde aynı Container içinde çoğalmış olunur. Akka’nın ölçeklemesi bununla sınırlıdır. Akka yeni Node veya yeni Pod oluşturamaz. Eğer, Aktör thread’leri sonuna kadar kullanılırsa ve hala genişlemeye ihtiyaç duyuluyorsa, yeni Aktör (Worker) oluşturma işi Kubernetes tarafından gerçekleştirilir.

Synergy mimari yapısında yer alan temel 3 Cluster’ın birbirleri arasında ve Client ile haberleşme adımları ve bu adımlarda kullanılan teknolojileri inceleyelim.

![Synergy Mimari](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadebfd6ca4-64f7-4778-af59-f2292213af74)

Clienttan gelen istek, ilk olarak [Azure Traffic Manager](https://docs.microsoft.com/tr-tr/azure/traffic-manager/traffic-manager-overview) tarafından karşılanır. Traffic Manager, trafiği farklı Azure bölgelerindeki hizmetlere en uygun şekilde dağıtırken, yüksek kullanılabilirlik ve yanıtlama hızı sağlayan DNS tabanlı bir trafik yük dengeleyicisidir. Trafiği istemci için en düşük ağ gecikme süresine sahip trafiğe yönlendirerek uygulama yanıt süresini kısaltır. Ayrıca, uç noktaları izleyerek uç nokta kullanım dışı kaldığında otomatik yük devretme sağlayarak kritik uygulamalar için yüksek kullanılabilirlik sağlar. Sistemde herhangi bir kesinti yaşamadan uygulamada planlı bakım çalışmaları yürütülmesine imkan verir. Uygulama bakımı devam ederken trafiğin, alternatif uç noktalara yönlendirilmesini sağlar.

Örneğin; Sistemde büyük bir güncelleme yapılacak olsun. Tüm sistemin bu güncellemeden etkilenmemesi için, mevcut Cluster yapısının aynısı yeni bir Cluster oluşturulur. Gelen isteklerin belirli bir yüzdesi (%10 civarı) yeni Cluster’a yönlendirilir ve güncellemenin etkileri gözlemlenir. Böylece güncelleme sonucu bir sorun yaşanması durumunda tüm istekler değil, isteklerin sadece yönlendirilen kadarı durumdan etkilenmiş olacak ve kontrollü bir geçiş sağlanmış olacaktır. Yeni Cluster’da sorun olmadığı gözlemlenirse gelen isteklerin daha büyük bir yüzdesi yeni Cluster’a aktarılır. Bu şekilde güncelleme sonucu herhangi bir sorun ile karşılaşılmadığı tespit edildiğinde, kontrollü olarak clienttan gelen tüm istekler yeni Cluster’a aktarılır. Tüm istekler yeni Cluster’a aktarıldığında eski Cluster kapatılarak, güncellenmiş Cluster üzerinden sistem çalışmaya devam eder. Sistemin bu şekilde durdurulmadan büyük güncellemeler alabilmesi için gerekli olan yönlendirme yapısı Traffic Manager ile sağlanır.

Traffic Manager’dan sonraki adım ise [Azure Content Delivery Network (CDN)](https://docs.microsoft.com/tr-tr/azure/cdn/cdn-overview) olarak bilinen İçerik Teslim Ağı’dır. CDN’ler gecikme süresini en aza indirmek için, önbelleğe alınmış içerikleri son kullanıcılara yakın olan bulunma noktası (POP) konumlarındaki uç sunucularda depolar. Kaynak sunucuya daha az trafik gönderilmesi için kullanıcı isteklerinin dağıtımı ve uç sunuculardan içerik sunulması işlemlerini yönetir.

Client’tan bir dosya isteği geldiğinde DNS, coğrafi olarak kullanıcıya en yakın ve en iyi performansa sahip bulunma noktası konumuna isteği yönlendirir. Bulunma noktasındaki uç sunucuların önbelleğinde dosya mevcut değilse bulunma noktası, kaynak sunucudan dosyayı ister. Bulunma noktasındaki uç sunucu, dosyayı önbelleğe alır ve dosya HTTP üst bilgileri tarafından belirtilen yaşam süresi (TTL) doluncaya kadar bulunma noktasındaki uç sunucuda önbelleğe alınmış şekilde kalır. Kaynak sunucu bir TTL belirtmediyse varsayılan TTL yedi gündür. Dosya için TTL’nin süresi dolmadıysa bulunma noktası uç sunucusu dosyayı doğrudan önbellekten döndürür. Bu işlem, daha hızlı ve daha duyarlı bir kullanıcı deneyimiyle sonuçlanır.

CDN sonrasındaki adım ise [Azure Application Gateway](https://docs.microsoft.com/tr-tr/azure/application-gateway/overview)’ dir. Azure Application Gateway, uygulamada trafik yönetimini sağlayan bir web trafiği yük dengeleyicisidir. Gelen URL’yi temel alarak trafiğin, URL ile ilişkili yapılandırılmış belirli bir sunucu kümesine yönlendirilmesini sağlayan yapıdır.

Bu adımlardan geçen istek, Kubernetes Cluster ı içerisindeki [Load Balancer](https://docs.microsoft.com/tr-tr/azure/load-balancer/load-balancer-overview) katmanı tarafından karşılanır. Yük Dengeleme , bir arka uç kaynak veya sunucu grubu genelinde yük devretme yükünü (gelen ağ trafiği) eşit bir şekilde dağıtmaktadır. Ana Cluster’a bir girdi geldiğinde ilk olarak LoadBalancer bu girdiyi karşılar ve Cluster içinde bunu nereye yönlendireceğine, girdinin ihtiyacına ve Cluster içindeki yoğunluğa göre karar verir. Bir Cluster’ın içinde birden çok Node mevcuttur. Cluster’a gelen girdinin hangi Node’a yönlendirileceğine karar veren yapıdır.

![Synergy Mimari](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b9bb56b-cc74-4fa9-aa92-2470bda87fe8)

Birbirinden izole Cluster’lar arasındaki haberleşmeyi sağlayan köprü bağlantısı için **gRPC** teknolojisi kullanılır. Kullanıcı Uygulamaları Cluster’ı ve Bimser Cluster’ı birbirleriyle güvenli gRPC kanalını kullanarak haberleşirler. Her bir kiracı, kendisine tahsis edilmiş jeton (token) ile diğer kiracılardan ayrıştırılmış olarak ana Cluster ile haberleşmesini gerçekleştirir.