# Synergy Deploy Agent Process ve Deployment Takip Ayarları

Synergy uygulamasındaki deploy agent servisi projelerin processlerini, kaynak kullanımını azaltmak ve performansı arttırmak için takip edebilmektedir. Kurulum esnasında ilgili ayarlar istenilen değerlerde ayarlanarak process takibinin döngüsü belirlenebilmektedir. Belirlenen döngü içinde istek gelmeyen processler kapatılarak (kill) hem kaynak tüketimi azaltılmış hem de deploy agent servisinin performansı artırılmış olmaktadır.

İlgili ayar ismi : “DIAGNOSTICS_CONFIG: '{"CheckIntervalSec":20,"ProcessIdleThresholdMin":5}'”. Burada CheckIntervalSec değeri kaç saniyede bir process kontrolu yapacağını, ProcessIdleThresholdMin değeri ise process kontrolünün kaç dakika süreceğini belirlemektedir. Yukarıda gösterilen ayar değerlendirildiğinde; 5 dakika boyunca 20 saniyede bir çalışan processler kontrol edilmekte, 5 dakika içinde istek gelmeyen process kill yapılarak kapatılmaktadır.

Örnek olarak tavsiye edilen config ayarları;

Agresif Yönetim (proje sayısı çok ise önerilen):à {"CheckIntervalSec":20,"ProcessIdleThresholdMin":5}

Dengeli Yönetim:à{"CheckIntervalSec":60,"ProcessIdleThresholdMin":15}

Kaynak Değerleri Yüksek Ortam:à{"CheckIntervalSec":300,"ProcessIdleThresholdMin":60}

Deploy Agentta 1 proje var ve kapatılmasını kesinlikle istenmiyorsa: ilgili ayar değerleri boş bırakılabilir.

Bahse konu ayarlamalar Deploy Agent servisinin configmap dosyası üzerinden yapılabilmektedir. Halihazırda çalışan bir servis için değerler değiştirildikten sonra servis tekrar başlatılmasıyla ayarlar aktif olabilmektedir.

Yeni deployment süreçlerinin kontrol edilebilmesi içinde yine deploy agent servisi üzerinde SIGNALR_URL değeri kullanılmaktadır. İlgili ayar için küme üzerinde çalışan realtimeinteractionrouter servis url’i tanımlanarak ui servis socket’i üzerinden takip yapılabilmektedir. Örnek config değeri şöyledir:  
SIGNALR_URL: [http://realtimeinteractionrouter.synergy.svc.cluster.local:3639/realtimeinteractionhub](http://realtimeinteractionrouter.synergy.svc.cluster.local:3639/realtimeinteractionhub). İlgili değer deploy agent servis configmapi dosyası üzerinden düzenlenebilmektedir.
