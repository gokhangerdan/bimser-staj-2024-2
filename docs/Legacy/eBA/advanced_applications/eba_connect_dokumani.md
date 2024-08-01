# eBAConnect Dokümanı
Bu doküman eBAConnect yapılandırmasını, içindeki endpointleri ve bu endpointlerin request-response modellerini anlatmaktadır.

## Yapılandırma
eBAConnect API'ını çalıştırabilmek için *eBAConnect/Web.Config* dosyasındaki **appSettings** kırılımı altında ki değerlerin aşağıdaki yönergelerde ayarlanması gerekmektedir.
- **eBAPath**: eBA'nın kurulu olduğu dizinde ki Common klasörünün konumu *(Örneğin C:\BimserCozum\eBA\Common)*.
- **Server**: Kurulu olan eBA'nın instance adı *(Örneğin PRODUCTION)*.

## Genel Bilgiler

API içerisinde 4 farklı controller bulunmaktadır, bunlar;
- **Login**
- **Menu**
- **Process**
- **ShareLink**

**NOT**: Doküman içerisinde response örneği bulunmayan endpointler geriye bir değer döndürmemektedir.

API içerisinde response wrapper bulunmaktadır, bundan dolayı tüm endpoint sonuçları sabit bir formatta döndürülmektedir. Formatı aşağıdan inceleyebilirsiniz.
#### Success
```json
{
  "Success": true,
  "Code": 200,
  "Result": null
}
```

#### Error
```json
{
  "success": false,
  "code": 200,
  "message": "An error occured",
  "stackTrace": "An error occured in PropertyController line:21"
}
```

## Authentication 
API içerisindeki endpointleri kullanabilmek için eBA sisteminde kayıtlı olan bir bir kullanıcı ile token alınmalıdır, daha sonra bu token ile diğer endpointler kullanılmalıdır. Token alabilmek için **api/Login/Login** `(POST)` endpointi kullanılır. Diğer endpointlerde bu oluşturulan tokenı **header** kısmında **token** değeri ile göndermemiz gerekli.

#### Request Example
http://localhost/eBAConnect/api/Login/Login

#### Request Body Parameters
- **UserId** (`string`): eBA kullanıcı adı.
- **ImpersonatingUserId** (`string`): Adına işlem yapılacak kullancının ID değeri.
- **Password** (`string`):eBA kullanıcı şifresi.
- **Language** (`string`): Kullanılmak istenen dil, English, Turkish gibi belirtilebilir.
- **ExternalUserType** (`string`): eBAConfiguration Manager tarafında tanımlanması gereken parametre değeri, Security.AcceptedExternalUserProperties key'ine tanımlanmalıdır, "," ile ayrılarak birden çok değer belirtilebilir. Bu tanımlanan değer ile aynı olacak şekilde SystemManager üzerinde bir custom property tanımlanmalıdır.
- **ExternalUserName** (`string`): Tanımlanan ExternalUserType propertysine verilecek olan değer. Bu değerin SystemManager üzerinde login olunması istenen kullanıcıya set edilmesi gerekmektedir.


#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": {
    "UserID": "admin",
    "ImpersonatingUser": "admin",
    "Token": "h7b9g1N+69N2X7VieO75Hd05UcK6YfzYTnwNIFnrJS8maKyK2pFxmrIpofVXBdeHw4CAkH8MlIDoD8VTr3FHMKC6xjUK0VLVX+7Ldaw+Gpc="
  }
}
```
## Endpoints

### api/Login/**Logout** `[POST]`
---
eBAConnect token'ını silerek oturumu sonlandırır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

### api/Menu/**GetMenuStructure** `[POST]`
---
Gönderilen token bilgisine göre kullanıcının görebildiği menüleri getirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ExcludeTypes": [
    0
  ]
}
```

#### Request Body Parameters
* **ExcludeTypes** (`integer[]`): Getirilmek istenmeyen menü tiplerini belirtir.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": [
    {
        "Id": 0,
        "ParentId": 0,
        "Text": "string",
        "Items": [
        {
            "Id": 0,
            "ParentId": 0,
            "Text": "string",
            "Items": [
            {}
            ],
            "NodeKey": "string",
            "NodeActionType": 0
        }
        ],
        "NodeKey": "string",
        "NodeActionType": 0
    }
  ]
}
```

### api/Process/**GetWaitingProcesses** `[POST]`
---
Gönderilen token bilgisine göre kullanıcıya ait onay listesi döndürülür.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": [
    {
        "ProcessName": "string",
        "ProcessCaption": "string",
        "Description": {},
        "Count": 0,
        "MultiLanguage": true
    }
  ]
}
```

### api/Process/**GetWaitingProcessRequests** `[POST]`
---
Gönderilen değerlere göre bekleyen süreçler ve değerleri döndürülür.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ProcessName": "string",
  "Skip": 0,
  "Take": 0
}
```

#### Request Body Parameters
* **ProcessName** (`string`): Detayları getirilmek istenen süreç adı.
* **Skip** (`integer`): Sayfalama işlemi için kaç değerin atlanacağını belirten parametre.
* **Take** (`integer`): Sayfalama işlemi için kaç değerin getirileceğini belirten parametre.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": [
    {
        "ProcessId": 0,
        "RequestId": 0,
        "Status": "string",
        "Fields": [
        {
            "Name": "string",
            "FieldName": "string",
            "Value": "string",
            "OrjValue": {},
            "FieldType": 0,
            "OrjName": "string",
            "DisplayFormat": "string"
        }
        ],
        "RequestDate": {}
    }
  ]
}
```

### api/Process/**GetFlowRequestEvents** `[POST]`
---
Gönderilen değerlere göre sürecin eventlarını getirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ProcessId": 0,
  "RequestId": 0
}
```

#### Request Body Parameters
* **ProcessId** (`integer`): Eventları getirilmek istenen sürecin ID değeri.
* **RequestId** (`integer`): Eventları getirilmek istenen sürecin Request ID değeri.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": {
    "Events": [
        {
        "Id": 0,
        "Text": "string",
        "ReasonRequired": true,
        "Validate": true,
        "EventForm": "string",
        "EventIcon": "string",
        "EventIconColor": "string",
        "Confirm": true,
        "FastApprove": true,
        "DigitalSignatureRequired": true
        }
    ]
  }
}
```

### api/Process/**ContinueProcess** `[POST]`
---
Gönderilen değerlere göre süreci belirtilen event üzerinden ilerletir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ProcessId": 0,
  "RequestId": 0,
  "EventId": 0,
  "Reason": "string",
  "EventFormId": 0
}
```

#### Request Body Parameters
* **ProcessId** (`integer`): İlerletilecek olan sürecin ID değeri.
* **RequestId** (`integer`): İlerletilecek olan sürecin Request ID değeri.
* **EventId** (`integer`): Sürecin hangi eventtan ilerletileceğini belirten Event ID değeri.
* **Reason** (`string`): Reason Required olan eventlar için reason değerinin girileceği alan.
* **EventormId** (`integer`): Event eğer bir form açacaksa bu formun ID değeri.

### api/ShareLink/**CreateLinkForProcessItem** `[POST]`
---
Gönderilen değerlere göre sürecin açılacağı bir URL döndürür.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ProcessId": 0,
  "RequestId": 0
}
```

#### Request Body Parameters
* **ProcessId** (`integer`): Link oluşturulmak istenen sürecin ID değeri.
* **RequestId** (`integer`): Link oluşturulmak istenen sürecin Request ID değeri.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": "http://localhost/eba.net/default.aspx?ep=63927904-EF0F-4748-9E68-8F9924831D37"
}
```

### api/ShareLink/**CreateLinkForMenu** `[POST]`
---
Gönderilen MenuItemKey değerine göre menü için link oluşturur. 

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "MenuItemKey": 0
}
```

#### Request Body Parameters
* **MenuItemKey** (`integer`): Link oluşturulmak istenen menünün değeri.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": "http://localhost/eba.net/default.aspx?ep=099A84FD-E43D-40E7-84DC-89B99608FB3C"
}
```