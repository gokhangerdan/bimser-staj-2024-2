# Beam Windows Servis Açıklamaları

### Services Açıklamaları

BEAM uygulamasını sunucuya kurulurken toplamda 14 services ile beraberinde kurulmaktadır.
BEAM uygulama servicesleri her sunucuda aynı isimle başlar sonlarına uygulamanın instance gelir. 

### Services

eBAServer = Beam uygulamasının çalışmasını sağlar. Bu service çalışmazsa uygulamaya erişim olmaz.

Redis ve Redis(Instance) = Redislerin çalışması için gerekli services. Instance yazan yere müşterinin uygulama içerisindeki instance adı gelecektir. Aşağıdaki örneklerde instance adını BEAM olarak kabul ederek örneklendireceğiz.

BOYSWEB2Agent_BEAM = Merkez Bankasından döviz kuru bilgilerini alır.

BOYSWEB2AlertManager_BEAM = Uygulama içindeki alarmları ve uyarı kodlarını çalıştırır.

BOYSWEB2DailyCheckListManager_BEAM=Periyodik kontrolleri çalıştırır.

BOYSWEB2MailManager_BEAM = Mail gönderme işlemlerini gerçekleştirir.

BOYSWEB2MobileApi_BEAM= Mobil uygulamayı aktif eder.

BOYSWEB2PreventiveManager_BEAM= Periyodik bakımların otomatik iş emrine dönüşmesini sağlar.

BOYSWEB2PrintServerService_BEAM= Tanımlanan yazıcılara belirlenen kurallara göre otomatik çıktı alabilmesini sağlar.


BOYSWEB2PushMessageService_BEAM = Mobil'de beam uygulamasına bildirim atmasını sağlar.

BOYSWEB2ReportAutomation_BEAM= Oluşturulan otomatik raporların çalışmasını sağlar.


BOYSWEB2Server_BEAM= Log tutar.


