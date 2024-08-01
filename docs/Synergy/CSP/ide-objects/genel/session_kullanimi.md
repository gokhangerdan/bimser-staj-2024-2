# Session Kullanımı
### Session Nedir ?
-   Session kavramı kişiye özel içerik oluşturmak için kullanıcı bilgilerinin sunucu tarafında saklanmasınıdır.
-   Session'lar oturumun açılması ve kapanması arasında varlığını sürdürür.
- Session kullanımı Synergy projelerinde Form'lara özgü yapılardır ve yalnızca Form'lar tarafından erilişebilir.
-   Synergy ortamında kullanılan Session'ın örnek çıktısı ise şu şekildedir;  
```json
{
    "Instance": "danismanlik",
    "TokenId": "*****",
    "Token": "*****",
    "EncryptedData": "*****",
    "Language": "tr-TR",
    "User": {
        "Id": 13,
        "Name": "oselcuk",
        "InternalName": "oselcuk",
        "FirstName": "Şuayip Orhan",
        "LastName": "Selçuk",
        "Email": "oselcuk@bimser.com.tr",
        "CustomProperties": [],
        "Department": {
        "Id": 7,
        "Name": "Danışmanlık ve Proje Yönetim Ofisi Departmanı",
        "CustomProperties": []
        },
        "Position": {
            "Id": 11,
            "Name": "eBA-CSP Yazılım Danışmanı",
            "CustomProperties": []
        },
        "Profession": {
            "Id": 11,
            "Name": "Yazılım Danışmanı"
        },
        "Groups": [{
            "Id": 1,
            "Name": "Bimser Eveyone Group"
        },
        {
            "Id": 2,
            "Name": "Bimser Software Consultant Group"
        },
        {
            "Id": 3,
            "Name": "Bimser Danışmanlık Development Group"
        }],
        "InternalId": 13
    },
    "HasDelegation": false,
    "DelegationId": 0
}   
```
## Server-Side Session Kullanımı
- Örnek bir kullanıcının adını ve soyadını alan komut bloğu ise şu şekildedir;

```csharp
    string firstName = Session.User.FirstName;
    string lastName = Session.User.LastName;
    string fullName = firstName + " " + lastName;
```
## Client-Side Session Kullanımı
- Örnek bir kullanıcının adını ve soyadını alan komut bloğu ise şu şekildedir;

```typescript
    var firstName = this.session.User.FirstName;
    var lastName = this.session.User.LastName;
    var fullName = firstName + " " + lastName;
```