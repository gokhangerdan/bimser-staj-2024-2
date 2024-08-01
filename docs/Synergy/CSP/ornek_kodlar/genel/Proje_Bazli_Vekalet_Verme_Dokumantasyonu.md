
# Proje Bazlı Vekalet Verme Dokümantasyonu

Synergy ortamında, proje bazlı vekalet vermek için aşağıdaki adımları takip edebilirsiniz. Bu dokümantasyon, gerekli olan kod parçacıklarını yorumlarla zenginleştirilmiş şekilde sunmaktadır.

## Gereksinimler

- Kullanıcının `userId` değeri
- Vekaletin başlangıç ve bitiş tarihleri
- Proje ID'si
- Pozisyon ID'leri

## Adımlar

### 1. Kullanıcı ID ve Tarih Bilgileri
```csharp
long toUserId = 13;
DateTime startDate = DateTime.Now;
DateTime endDate = DateTime.Now.AddDays(15);
```

### 2. Vekalet İsmi Sözlüğü
- Türkçe ve İngilizce açıklamalar içeren bir sözlük oluşturulur.
```csharp
var delegationNameDictionary = new Dictionary<string, string>();
delegationNameDictionary.Add("tr-TR", "Proje aracılığı ile oluşturulan vekalettir.");
delegationNameDictionary.Add("en-US", "The delegation created by project.");
```

### 3. Pozisyon ID'leri ve Scopes Listesi
- Pozisyon ID'leri ve Proje ID'si eklenir.
```csharp
List<long> positionIds = new List<long> { Convert.ToInt64(35) };
List<string> scopes = new List<string>();
scopes.Add("app.4b5c6b72-b570-4b2c-8eaf-f5d82301f105"); // ProjeId'si scopeslara app.projeid formatında eklenir.
```

### 4. CreateDelegationRequest Nesnesi
- Vekalet isteği oluşturulur.
```csharp
var createDelegationRequest = new CreateDelegationRequest(
    delegationNameDictionary,
    DelegationType.Delegation,
    toUserId,
    startDate,
    endDate,
    scopes,
    positionIds,
    CreationType.Simple,
    BasedType.Project
);
```

### 5. Vekaletin Oluşturulması
- Vekalet isteği gönderilir ve sonuç kontrol edilir.
```csharp
var delegateResult = synergyHelper.ServiceApi.Delegation.Create(createDelegationRequest).Result;
bool isDelegationSuccess = delegateResult.Success;
```

## Örnek Kod

Aşağıda, yukarıda açıklanan adımları içeren tam kod örneğini bulabilirsiniz:

```csharp
// Kullanıcı ID ve Tarih Bilgileri
long toUserId = 13;
DateTime startDate = DateTime.Now;
DateTime endDate = DateTime.Now.AddDays(15);

// Vekalet İsmi Sözlüğü
var delegationNameDictionary = new Dictionary<string, string>();
delegationNameDictionary.Add("tr-TR", "Proje aracılığı ile oluşturulan vekalettir.");
delegationNameDictionary.Add("en-US", "The delegation created by project.");

// Pozisyon ID'leri ve Scopes Listesi
List<long> positionIds = new List<long> { Convert.ToInt64(35) };
List<string> scopes = new List<string>();
scopes.Add("app.4b5c6b72-b570-4b2c-8eaf-f5d82301f105"); // ProjeId'si scopeslara app.projeid formatında eklenir.

// CreateDelegationRequest Nesnesi
var createDelegationRequest = new CreateDelegationRequest(
    delegationNameDictionary,
    DelegationType.Delegation,
    toUserId,
    startDate,
    endDate,
    scopes,
    positionIds,
    CreationType.Simple,
    BasedType.Project
);

// Vekaletin Oluşturulması
var delegateResult = synergyHelper.ServiceApi.Delegation.Create(createDelegationRequest).Result;
bool isDelegationSuccess = delegateResult.Success;
```

Bu adımlar takip edilerek Synergy ortamında proje bazlı vekalet verilebilir.
