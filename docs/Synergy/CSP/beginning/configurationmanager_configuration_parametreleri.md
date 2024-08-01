# Configuration Manager

Configuration Manager' ın Synergy sistemi tarafından kullanılabilmesi için SYSTEMCONFIGURATIONS tablosuna eklenmesi gereken parametreler vardır. Bu ayarlar "System.ConfigurationManager" anahtarı (keyi) ile tutulur. Aşağıda örnek bir config ayarı mevcut.


```
{
	"ConfigurationManagement": {
		"RestService": {
			"Url": "https://dev-configuration.bimser.net/",
			"DeadLine": "60"
		},
		"GrpcService": {
			"Url": "https://dev-configuration.bimser.net/GrpcConfigurationManagement",
			"DeadLine": "60"
		},
		"ServiceDecider": {
			"ServiceType": "Rest"
		},
		"SignalRConnection": {
			"SignalRHubUrl": "https://dev-configuration.bimser.net/ConfigurationManagerAPIServiceHub"
		}
	}
}

```

### ConfigurationManagement

Parametrelerin tutulduğu ana etiketin adıdır.

___

### RestService / GrpcService

Configuration Manager ile RestService/GrpcService üzerinden haberleşirken RestService/GrpcService bilgilerinin tutulduğu configdir. Bu config URL ve DeadLine Parametrelerini içerir.

### Url

Rest isteklerin hangi adrese atılacağını belirler.

### DeadLine

Atılan istekleri timeout süresini belirler

___

### ServiceDecider

ServiceType  parametresini barındırır.  ServiceType  ise Synergy ve Configuration Manager' ın hangi yöntemle haberleşeceğine karar verir. Rest ve Grpc değerlerini alır.


___

### SignalRConnection

SignalR bilgilerini içerir. SignalRHubUrl parametresini barındırır.
SignalRHubUrl: Ayakta bulunan Configuration Manager SignalR Hub' ın adresidir.


___

### Instances.*

SYSTEMCONFIGURATIONS tablosunda Instance Keyler bulunmaktadır. Örneğin; Instances.Dev gibi. Bu Key' in  değerinde Enviroment ve ConfigurationManagementPublicKey değerleri bulunur.

### Enviroment

Configuration Manager uygulamasındaki Ortam bilgisidir. Orn. Dev, Prod vb.

### ConfigurationManagementPublicKey

Configuration Manager uygulamasına gelen isteklerin doğru kişi/uygulama tarafından atıldığını anlamak için PublicKey bilgisi tutulur. Bu PublicKey bilgisi ile Configuration Manager tarafında PrivateKey birbirini çözümleyebiliyorsa Configuration Manager uygulaması istemciye sağlıklı dönüş yapar.

