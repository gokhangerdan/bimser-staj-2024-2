
# Synergy CONFIGURATIONS Tablosundan Veri Çekme Rehberi

Bu doküman, Synergy uygulamasındaki CONFIGURATIONS tablosundan `ServiceApi` aracılığıyla veri çekme sürecini detaylı bir şekilde açıklar. Bu işlem için doğrudan veritabanı bağlantısı kurmanıza gerek yoktur. İhtiyacınız olan `ServiceApi` instance'ıdır.

## Gereksinimler

- Synergy `ServiceApi` instance'ına erişim.
- İlgili `ConfigurationManager` kullanımı.

## Adımlar

1. **ServiceApi Erişimi**: Synergy `ServiceApi` instance'ına erişin. Eğer bir instance'ınız yoksa, uygun şekilde bir instance oluşturun.
2. **Configuration Key Belirleme**: İstediğiniz konfigürasyon değerinin anahtarını (`ConfigurationKey`) belirleyin.
3. **GetConfiguration Kullanımı**: `ConfigurationAPI.GetConfiguration` metodunu kullanarak istediğiniz konfigürasyon verisini çekin.
4. **Sonuç İşleme**: Elde ettiğiniz sonucu işleyin. Sonuçlar `Result.Result.ConfigurationData` içinde yer alacaktır.

## Örnek C# Kodu

Aşağıda, bir konfigürasyon değeri çekmek için kullanabileceğiniz C# kod örneği bulunmaktadır:

```csharp
var configurationValue = _serviceAPI.ConfigurationAPI.GetConfiguration(new Bimser.Synergy.Entities.Configuration.Business.DTOs.Requests.GetConfigurationRequest {
    ConfigurationKey = "Web.Dashboard.FormName"
}).Result.Result.ConfigurationData;
```

Bu kod, `Web.Dashboard.FormName` anahtarına sahip konfigürasyon değerini çeker ve değişken içinde saklar.
