# eBAHRAPI Dokümanı

Bu doküman eBAHRAPI içindeki endpointleri ve bu endpointlerin request-response modellerini anlatmaktadır. eBAHRAPI, sistem içerisinde organizasyon ekranında yapabildiğimiz işlemleri başka uygulamalara entegre ederek yapabilmek için gerekli olan endpointleri sağlar.

API içerisinde 8 farklı controller bulunmaktadır, bunlar;
- **Login**
- **User**
- **Department**
- **Group**
- **Position**
- **Profession**
- **Property**
- **Role**

**NOT**: Doküman içerisinde response örneği bulunmayan endpointler geriye bir değer döndürmemektedir.

API içerisinde response wrapper bulunmaktadır, bundan dolayı tüm endpoint sonuçları sabir bir formatta döndürülmektedir. Formatı aşağıdan inceleyebilirsiniz.
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
API içerisindeki endpointleri kullanabilmek için eBA sisteminde kayıtlı olan bir bir kullanıcı ile token alınmalıdır. Bu kullanıcı **Admin** rolüne sahip olmalıdır. Daha sonra bu token ile diğer endpointler kullanılmalıdır. Token alabilmek için **api/Login/GetLogin** `(POST)` endpointi kullanılır. Diğer endpointlerde bu oluşturulan tokenı **header** kısmında **Token** değeri ile göndermemiz gerekli.

#### Request Example
http://localhost/eBAHRAPI/api/Login/GetLogin?userID=admin&password=12345

#### Request Query Parameters
- **userID** (`string`): eBA kullanıcı adı.
- **password** (`string`): eBA kullanıcı şifresi.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": {
    "UserID": "admin",
    "Token": "h7b9g1N+69N2X7VieO75Hd05UcK6YfzYTnwNIFnrJS8maKyK2pFxmrIpofVXBdeHw4CAkH8MlIDoD8VTr3FHMKC6xjUK0VLVX+7Ldaw+Gpc="
  }
}
```

## Endpoints

### api/Department/**GetDepartments** `[GET]`
---
Sistemdeki tüm departmanları getirir.

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
      "ID": "ArGe",
      "Description": "Araştırma ve Geliştirme",
      "ManagerDepartment": "",
      "Status": 1,
      "Type": 0,
      "ImportStatus": 1,
      "ManagerUserId": "hkar"
    },
    {
      "ID": "G2",
      "Description": "Finans ve Mali işler",
      "ManagerDepartment": "G0",
      "Status": 0,
      "Type": 0,
      "ImportStatus": 0,
      "ManagerUserId": "tkir"
    }
  ]
}
```

### api/Department/**GetActiveDepartments** `[GET]`
---
Sistemdeki tüm aktif departmanları getirir.

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
      "ID": "G0",
      "Description": "İdari İşler Departmanı",
      "ManagerDepartment": "",
      "Status": 1,
      "Type": 0,
      "ImportStatus": 0,
      "ManagerUserId": "hkar"
    },
    {
      "ID": "G3",
      "Description": "Kalite Güvence",
      "ManagerDepartment": "G0",
      "Status": 1,
      "Type": 0,
      "ImportStatus": 0,
      "ManagerUserId": "ykurt"
    }
  ]
}
```

### api/Department/**GetPassiveDepartments** `[GET]`
---
Sistemdeki tüm pasif departmanları getirir.

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
      "ID": "G0",
      "Description": "İdari İşler Departmanı",
      "ManagerDepartment": "",
      "Status": 0,
      "Type": 0,
      "ImportStatus": 0,
      "ManagerUserId": "hkar"
    },
    {
      "ID": "G3",
      "Description": "Kalite Güvence",
      "ManagerDepartment": "G0",
      "Status": 0,
      "Type": 0,
      "ImportStatus": 0,
      "ManagerUserId": "ykurt"
    }
  ]
}
```

### api/Department/**GetDepartmentDetail** `[POST]`
---
ID değerine göre sistemdeki bir departmanı getirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Department/GetDepartmentDetail?id=G2

#### Request Query Parameters
- **id** (`string`): Departman ID değeri.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": {
    "ID": "G2",
    "Description": "Finans ve Mali işler",
    "ManagerDepartment": "G0",
    "Status": 1,
    "Type": 0,
    "ImportStatus": 0,
    "ManagerUserId": "tkir"
  }
}
```

### api/Department/**ChangeDepartmentStatus** `[POST]`
---
Sistemdeki bir departmanı aktifleştirip/pasifleştirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Department/ChangeDepartmentStatus?id=G2&status=true

#### Request Query Parameters
- **id** (`string`): Departman ID değeri.
- **status** (`boolean`): Departmanın aktiflik durumu.

### api/Department/**AddNewDepartment** `[POST]`
---
Sisteme girilen bilgilerle yeni bir departman ekler.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ID": "IT",
  "Description": "Bilgi Teknolojileri",
  "ManagerDepartment": null,
  "Status": true,
  "Type": 0,
  "ImportStatus": true,
  "ManagerUserId": "tozer",
  "PropertyValues": [
    {
      "Name": "Example",
      "Value": "Example Test",
      "ImportStatus": true
    }
  ]
}
```

#### Request Body Parameters
* **ID** (`string`): Departman ID değeri.
* **Description** (`string`): Departman açıklaması.
* **ManagerDepartment** (`string`): Bağlı olacağı departman, eğer üst bir departmansa `null` geçilmelidir.
* **Status** (`boolean`): Departman aktiflik/pasiflik durumu.
* **Type** (`integer`): Departman türü.
* **ImportStatus** (`boolean`): HR transfer için içe aktarım durumu.
* **ManagerUserId** (`string`): Departman yöneticisi olan kullanıcının ID değeri.
* **PropertyValues** (`object[]`): Eklenecek olan departmana özel bir alan ekler. `null` geçilebilir.
    * **Name** (`string`): Özel alanın adı.
    * **Value** (`string`): Özel alanın değeri.
    * **ImportStatus** (`boolean`): Özel alanın HR transfer için içe aktarım durumu. 

### api/Department/**UpdateDepartment** `[POST]`
---
Var olan bir departmanın bilgilerini günceller.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ID": "IT",
  "Description": "Bilgi Teknolojileri",
  "ManagerDepartment": null,
  "Status": true,
  "Type": 0,
  "ImportStatus": true,
  "ManagerUserId": "hkar",
  "PropertyValues": [
    {
      "Name": "Example",
      "Value": null,
      "ImportStatus": false
    }
  ]
}
```

#### Request Body Parameters
* **ID** (`string`): Departman ID değeri.
* **Description** (`string`): Departman açıklaması.
* **ManagerDepartment** (`string`): Bağlı olacağı departman, eğer üst bir departmansa `null` geçilmelidir.
* **Status** (`boolean`): Departman aktiflik/pasiflik durumu.
* **Type** (`integer`): Departman türü.
* **ImportStatus** (`boolean`): HR transfer için içe aktarım durumu.
* **ManagerUserId** (`string`): Departman yöneticisi olan kullanıcının ID değeri.
* **PropertyValues** (`object[]`): Eklenecek olan departmana özel bir alan ekler. `null` geçilebilir.
    * **Name** (`string`): Özel alanın adı.
    * **Value** (`string`): Özel alanın değeri.
    * **ImportStatus** (`boolean`): Özel alanın HR transfer için içe aktarım durumu. 

### api/Group/**GetGroups** `[GET]`
---
Sistemdeki tüm grupları getirir.

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
      "ID": "everyone",
      "Description": "Everyone",
      "Status": 1,
      "ImportStatus": 0
    },
    {
      "ID": "BM",
      "Description": "Board Members",
      "Status": 0,
      "ImportStatus": 0
    }
  ]
}
```

### api/Group/**GetActiveGroups** `[GET]`
---
Sistemdeki tüm aktif grupları getirir.

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
      "ID": "everyone",
      "Description": "Everyone",
      "Status": 1,
      "ImportStatus": 0
    },
    {
      "ID": "BM",
      "Description": "Board Members",
      "Status": 1,
      "ImportStatus": 0
    }
  ]
}
```

### api/Group/**GetPassiveGroups** `[GET]`
---
Sistemdeki tüm pasif grupları getirir.

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
      "ID": "everyone",
      "Description": "Everyone",
      "Status": 0,
      "ImportStatus": 0
    },
    {
      "ID": "BM",
      "Description": "Board Members",
      "Status": 0,
      "ImportStatus": 0
    }
  ]
}
```

### api/Group/**GetGroupDetail** `[POST]`
---
ID değerine göre sistemdeki bir grubu getirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Group/GetGroupDetail?id=everyone

#### Request Query Parameters
- **id** (`string`): Grup ID değeri.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": {
    "ID": "everyone",
    "Description": "Everyone",
    "Status": 1,
    "ImportStatus": 0
  }
}
```

### api/Group/**ChangeGroupStatus** `[POST]`
---
Sistemdeki bir grubu aktifleştirip/pasifleştirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Group/ChangeGroupStatus?id=everyone&status=true

#### Request Query Parameters
- **id** (`string`): Grup ID değeri.
- **status** (`boolean`): Grubun aktiflik durumu.

### api/Group/**AddNewGroup** `[POST]`
---
Sisteme girilen bilgilerle yeni bir grup ekler.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ID": "BM",
  "Description": "Board Members",
  "Status": true,
  "ImportStatus": true,
  "PropertyValues": [
    {
      "Name": "Example",
      "Value": "Example Test",
      "ImportStatus": true
    }
  ]
}
```

#### Request Body Parameters
* **ID** (`string`): Grup ID değeri.
* **Description** (`string`): Grup açıklaması.
* **Status** (`boolean`): Grubun aktiflik/pasiflik durumu.
* **ImportStatus** (`boolean`): HR transfer için içe aktarım durumu.
* **PropertyValues** (`object[]`): Eklenecek olan gruba özel bir alan ekler. `null` geçilebilir.
    * **Name** (`string`): Özel alanın adı.
    * **Value** (`string`): Özel alanın değeri.
    * **ImportStatus** (`boolean`): Özel alanın HR transfer için içe aktarım durumu. 

### api/Group/**AddUserToGroup** `[POST]`
---
Sistemdeki bir gruba kullanıcı ekler.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Group/AddUserToGroup?groupId=BM&userId=tozer

#### Request Query Parameters
- **groupId** (`string`): Grup ID değeri.
- **userId** (`string`): Eklenecek olan kullanıcını ID değer.

### api/Group/**RemoveUserFromGroup** `[POST]`
---
Sistemdeki bir gruptan kullanıcıyı çıkarır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Group/RemoveUserFromGroup?groupId=BM&userId=tozer

#### Request Query Parameters
- **groupId** (`string`): Grup ID değeri.
- **userId** (`string`): Eklenecek olan kullanıcını ID değer.

### api/Position/**GetPositions** `[GET]`
---
Sistemdeki tüm pozisyonları getirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result":  [
    {
      "ID": "PG2001",
      "Description": "Finans Grup Yöneticisi",
      "UserID": "tkir",
      "Status": 0,
      "Type": 0,
      "ImportedPosCode": "",
      "ImportStatus": 0
    },
    {
      "ID": "PG0001",
      "Description": "Genel Müdür",
      "UserID": "hkar",
      "Status": 1,
      "Type": 0,
      "ImportedPosCode": "",
      "ImportStatus": 0
    }
  ]
}
```

### api/Position/**GetActivePositions** `[GET]`
---
Sistemdeki tüm aktif pozisyonları getirir.

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
      "ID": "PG2001",
      "Description": "Finans Grup Yöneticisi",
      "UserID": "tkir",
      "Status": 1,
      "Type": 0,
      "ImportedPosCode": "",
      "ImportStatus": 0
    },
    {
      "ID": "PG0001",
      "Description": "Genel Müdür",
      "UserID": "hkar",
      "Status": 1,
      "Type": 0,
      "ImportedPosCode": "",
      "ImportStatus": 0
    }
  ]
}
```

### api/Position/**GetPassivePositions** `[GET]`
---
Sistemdeki tüm pasif pozisyonları getirir.

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
      "ID": "PG1005",
      "Description": "Yazılım Uzmanı",
      "UserID": "sderin",
      "Status": 0,
      "Type": 0,
      "ImportedPosCode": "",
      "ImportStatus": 0
    },
    {
      "ID": "PG1006",
      "Description": "Yazılım Uzmanı",
      "UserID": "sak",
      "Status": 0,
      "Type": 0,
      "ImportedPosCode": "",
      "ImportStatus": 0
    }
  ]
}
```

### api/Position/**GetPositionDetail** `[POST]`
---
ID değerine göre sistemdeki bir departmanı getirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Position/GetPositionDetail?id=PG0001

#### Request Query Parameters
- **id** (`string`): Pozisyon ID değeri.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": {
    "ID": "PG0001",
    "Description": "Genel Müdür",
    "UserID": "hkar",
    "Status": 1,
    "Type": 0,
    "ImportedPosCode": "",
    "ImportStatus": 0
  }
}
```

### api/Position/**ChangePositionStatus** `[POST]`
---
Sistemdeki bir pozisyonu aktifleştirip/pasifleştirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Position/ChangePositionStatus?id=PG0001&status=true

#### Request Query Parameters
- **id** (`string`): Pozisyon ID değeri.
- **status** (`boolean`): Pozisyonun aktiflik durumu.

### api/Position/**AddNewPosition** `[POST]`
---
Sisteme girilen bilgilerle yeni bir pozisyon ekler.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ID": "PG1008",
  "Description": "Yazılım Teknik Lideri",
  "UserID": "tozer",
  "Status": true,
  "Type": 0,
  "ImportedPosCode": "PG1008",
  "ImportStatus": true,
  "PropertyValues": [
    {
      "Name": "Example",
      "Value": "Example Test",
      "ImportStatus": true
    }
  ]
}
```

#### Request Body Parameters
* **ID** (`string`): Pozisyon ID değeri.
* **Description** (`string`): Pozisyon açıklaması.
* **UserId** (`string`): Pozisyonun atandığı kullanıcının ID değeri.
* **Status** (`boolean`): Pozisyonun aktiflik/pasiflik durumu.
* **Type** (`integer`): Pozisyonun tipini belirtir.
* **ImportedPosCode** (`string`): Pozisyonun HR transfer için içe aktarım kodu.
* **ImportStatus** (`boolean`): HR transfer için içe aktarım durumu.
* **PropertyValues** (`object[]`): Eklenecek olan pozisyona özel bir alan ekler. `null` geçilebilir.
    * **Name** (`string`): Özel alanın adı.
    * **Value** (`string`): Özel alanın değeri.
    * **ImportStatus** (`boolean`): Özel alanın HR transfer için içe aktarım durumu. 

### api/Position/**UpdatePosition** `[POST]`
---
Var olan bir pozisyonun bilgilerini günceller.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ID": "PG1008",
  "Description": "Yazılım Takım Lideri",
  "UserID": "tozer",
  "Status": true,
  "Type": 0,
  "ImportedPosCode": "PG1008",
  "ImportStatus": true,
  "PropertyValues": [
    {
      "Name": "Example",
      "Value": "Example Test",
      "ImportStatus": true
    }
  ]
}
```

#### Request Body Parameters
* **ID** (`string`): Pozisyon ID değeri.
* **Description** (`string`): Pozisyon açıklaması.
* **UserId** (`string`): Pozisyonun atandığı kullanıcının ID değeri.
* **Status** (`boolean`): Pozisyonun aktiflik/pasiflik durumu.
* **Type** (`integer`): Pozisyonun tipini belirtir.
* **ImportedPosCode** (`string`): Pozisyonun HR transfer için içe aktarım kodu.
* **ImportStatus** (`boolean`): HR transfer için içe aktarım durumu.
* **PropertyValues** (`object[]`): Eklenecek olan pozisyona özel bir alan ekler. `null` geçilebilir.
    * **Name** (`string`): Özel alanın adı.
    * **Value** (`string`): Özel alanın değeri.
    * **ImportStatus** (`boolean`): Özel alanın HR transfer için içe aktarım durumu. 

### api/Profession/**GetProfessions** `[GET]`
---
Sistemdeki tüm ünvanları getirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result":  [
    {
      "ID": "T1",
      "Description": "Genel Müdür",
      "Status": 1,
      "Type": 0,
      "ImportStatus": 0
    },
    {
      "ID": "T2",
      "Description": "Grup Yöneticisi",
      "Status": 0,
      "Type": 0,
      "ImportStatus": 0
    }
  ]
}
```

### api/Profession/**GetActiveProfessions** `[GET]`
---
Sistemdeki tüm aktif ünvanları getirir.

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
      "ID": "T1",
      "Description": "Genel Müdür",
      "Status": 1,
      "Type": 0,
      "ImportStatus": 0
    },
    {
      "ID": "T2",
      "Description": "Grup Yöneticisi",
      "Status": 1,
      "Type": 0,
      "ImportStatus": 0
    }
  ]
}
```

### api/Profession/**GetPassiveProfessions** `[GET]`
---
Sistemdeki tüm pasif ünvanları getirir.

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
      "ID": "T1",
      "Description": "Genel Müdür",
      "Status": 0,
      "Type": 0,
      "ImportStatus": 0
    },
    {
      "ID": "T2",
      "Description": "Grup Yöneticisi",
      "Status": 0,
      "Type": 0,
      "ImportStatus": 0
    }
  ]
}
```

### api/Profession/**GetProfessionDetail** `[POST]`
---
ID değerine göre sistemdeki bir ünvanı getirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Profession/GetProfessionDetail?id=T1

#### Request Query Parameters
- **id** (`string`): Ünvan ID değeri.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": {
    "ID": "T1",
    "Description": "Genel Müdür",
    "Status": 1,
    "Type": 0,
    "ImportStatus": 0
  }
}
```

### api/Profession/**ChangeProfessionStatus** `[POST]`
---
Sistemdeki bir ünvanı aktifleştirip/pasifleştirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Profession/ChangeProfessionStatus?id=T1&status=true

#### Request Query Parameters
- **id** (`string`): Ünvan ID değeri.
- **status** (`boolean`): Ünvanın aktiflik durumu.

### api/Profession/**AddNewProfession** `[POST]`
---
Sisteme girilen bilgilerle yeni bir ünvan ekler.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ID": "T8",
  "Description": "Görevli",
  "Status": true,
  "Type": 0,
  "ImportStatus": true,
  "PropertyValues": [
    {
      "Name": "Example",
      "Value": "Example Test",
      "ImportStatus": true
    }
  ]
}
```

#### Request Body Parameters
* **ID** (`string`): Ünvan ID değeri.
* **Description** (`string`): Ünvan açıklaması.
* **Status** (`boolean`): Ünvanın aktiflik/pasiflik durumu.
* **Type** (`integer`): Ünvanın tipini belirtir.
* **ImportStatus** (`boolean`): HR transfer için içe aktarım durumu.
* **PropertyValues** (`object[]`): Eklenecek olan ünvana özel bir alan ekler. `null` geçilebilir.
    * **Name** (`string`): Özel alanın adı.
    * **Value** (`string`): Özel alanın değeri.
    * **ImportStatus** (`boolean`): Özel alanın HR transfer için içe aktarım durumu. 

### api/Profession/**UpdateProfession** `[POST]`
---
Var olan bir ünvanın bilgilerini günceller.

#### Headers
**Content-Type**: `application/json`\\
**Token**: `token`

#### Request Example
```json
{
  "ID": "T8",
  "Description": "Kıdemli Uzman",
  "Status": true,
  "Type": 0,
  "ImportStatus": true,
  "PropertyValues": [
    {
      "Name": "Example",
      "Value": "Example Test",
      "ImportStatus": true
    }
  ]
}
```

#### Request Body Parameters
* **ID** (`string`): Ünvan ID değeri.
* **Description** (`string`): Ünvan açıklaması.
* **Status** (`boolean`): Ünvanın aktiflik/pasiflik durumu.
* **Type** (`integer`): Ünvanın tipini belirtir.
* **ImportStatus** (`boolean`): HR transfer için içe aktarım durumu.
* **PropertyValues** (`object[]`): Eklenecek olan ünvana özel bir alan ekler. `null` geçilebilir.
    * **Name** (`string`): Özel alanın adı.
    * **Value** (`string`): Özel alanın değeri.
    * **ImportStatus** (`boolean`): Özel alanın HR transfer için içe aktarım durumu. 

### api/User/**GetUsers** `[GET]`
---
Sistemdeki tüm kullanıcıları getirir.

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
      "ID": "adogru",
      "FirstName": "Ali",
      "LastName": "Doğru",
      "Email": "eba@eba.net",
      "Status": 1,
      "Type": 0,
      "ImportStatus": 0,
      "BirthDate": null,
      "EmployementStart": null,
      "EmployementEnd": null,
      "Category": 0,
      "Sex": 1,
      "Department": "G0",
      "Profession": "T7",
      "Companies": [],
      "Managers": [
        {
          "Key": "default",
          "ID": "hkar",
          "Fullname": "Huseyin Kar"
        },
        {
          "Key": "report",
          "ID": "tozer",
          "Fullname": "Talha Özer"
        }
      ]
    },
    {
      "ID": "huzal",
      "FirstName": "Hakan",
      "LastName": "Uzal",
      "Email": "eba@eba.net",
      "Status": 0,
      "Type": 1,
      "ImportStatus": 1,
      "BirthDate": null,
      "EmployementStart": null,
      "EmployementEnd": null,
      "Category": 0,
      "Sex": 0,
      "Department": "G2",
      "Profession": "T4",
      "Companies": [],
      "Managers": []
    }
  ]
}
```

### api/User/**GetActiveUsers** `[GET]`
---
Sistemdeki tüm aktif kullanıcıları getirir.

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
      "ID": "adogru",
      "FirstName": "Ali",
      "LastName": "Doğru",
      "Email": "eba@eba.net",
      "Status": 1,
      "Type": 0,
      "ImportStatus": 0,
      "BirthDate": null,
      "EmployementStart": null,
      "EmployementEnd": null,
      "Category": 0,
      "Sex": 1,
      "Department": "G0",
      "Profession": "T7",
      "Companies": [],
      "Managers": [
        {
          "Key": "default",
          "ID": "hkar",
          "Fullname": "Huseyin Kar"
        },
        {
          "Key": "report",
          "ID": "tozer",
          "Fullname": "Talha Özer"
        }
      ]
    },
    {
      "ID": "huzal",
      "FirstName": "Hakan",
      "LastName": "Uzal",
      "Email": "eba@eba.net",
      "Status": 1,
      "Type": 1,
      "ImportStatus": 1,
      "BirthDate": null,
      "EmployementStart": null,
      "EmployementEnd": null,
      "Category": 0,
      "Sex": 0,
      "Department": "G2",
      "Profession": "T4",
      "Companies": [],
      "Managers": []
    }
  ]
}
```

### api/User/**GetPassiveUsers** `[GET]`
---
Sistemdeki tüm pasif kullanıcıları getirir.

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
      "ID": "adogru",
      "FirstName": "Ali",
      "LastName": "Doğru",
      "Email": "eba@eba.net",
      "Status": 0,
      "Type": 0,
      "ImportStatus": 0,
      "BirthDate": null,
      "EmployementStart": null,
      "EmployementEnd": null,
      "Category": 0,
      "Sex": 1,
      "Department": "G0",
      "Profession": "T7",
      "Companies": [],
      "Managers": [
        {
          "Key": "default",
          "ID": "hkar",
          "Fullname": "Huseyin Kar"
        },
        {
          "Key": "report",
          "ID": "tozer",
          "Fullname": "Talha Özer"
        }
      ]
    },
    {
      "ID": "huzal",
      "FirstName": "Hakan",
      "LastName": "Uzal",
      "Email": "eba@eba.net",
      "Status": 0,
      "Type": 1,
      "ImportStatus": 1,
      "BirthDate": null,
      "EmployementStart": null,
      "EmployementEnd": null,
      "Category": 0,
      "Sex": 0,
      "Department": "G2",
      "Profession": "T4",
      "Companies": [],
      "Managers": []
    }
  ]
}
```

### api/User/**GetUserDetail** `[POST]`
---
ID değerine göre sistemdeki bir kullanıcıyı getirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/User/GetUserDetail?userId=tozer

#### Request Query Parameters
- **userId** (`string`): Kullanıcı ID değeri.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": {
    "ID": "tozer",
    "FirstName": "Talha",
    "LastName": "Özer",
    "Email": "tozer@bimser.com",
    "Status": 1,
    "Type": 0,
    "ImportStatus": 0,
    "BirthDate": null,
    "EmployementStart": null,
    "EmployementEnd": null,
    "Category": 0,
    "Sex": 1,
    "Department": "G0",
    "Profession": "T4",
    "Companies": [],
    "Managers": []
  }
}
```

### api/User/**ChangeUserStatus** `[POST]`
---
Sistemdeki bir kullanıcıyı aktifleştirip/pasifleştirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/User/ChangeUserStatus?userId=tozer&status=true

#### Request Query Parameters
- **userId** (`string`): Kullanıcı ID değeri.
- **status** (`boolean`): Kullanıcı aktiflik durumu.

### api/User/**AddNewUser** `[POST]`
---
Sisteme girilen bilgilerle yeni bir kullanıcı ekler.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ID": "ycelik",
  "FirstName": "Yiğit",
  "LastName": "Çelik",
  "Password": "12345678",
  "Email": "ycelik@bimser.com",
  "Status": true,
  "Type": 0,
  "ImportStatus": true,
  "BirthDate": "2000-07-31T06:22:03.551Z",
  "EmploymentStart": "2024-03-27T06:22:03.551Z",
  "EmploymentEnd": "2024-03-27T06:22:03.551Z",
  "Category": 0,
  "Sex": 0,
  "Company": "Bimser,Test",
  "Department": "G4",
  "Profession": "T7",
  "PropertyValues": [
    {
      "Name": "Example",
      "Value": "this is test value",
      "ImportStatus": true
    }
  ],
  "Managers": [
    {
      "Key": "default",
      "ID": "tozer"
    }
  ]
}
```

#### Request Body Parameters
* **ID** (`string`): Kullanıcı ID değeri.
* **Firstname** (`string`): Kullanıcının adı.
* **Lastname** (`string`): Kullanıcının soyadı.
* **Password** (`string`): Kullanıcının şifresi.
* **Email** (`string`): Kullanıcının e-posta adresi.
* **Status** (`boolean`): Kullanıcının aktiflik/pasiflik durumu.
* **Type** (`string`): Kullanıcının türü.
* **ImportStatus** (`boolean`): HR transfer için içe aktarım durumu.
* **BirthDate** (`datetime`): Kullanıcının doğum tarihi.
* **EmploymentStart** (`datetime`): Kullanıcının işe giriş tarihi.
* **EmploymentEnd** (`datetime`): Kullanıcının işten çıkış tarihi.
* **Category** (`integer`): Kullanıcının mavi yada beyaz olacağını belirtir. 0-Mavi yaka, 1-Beyaz yaka.
* **Sex** (`integer`): Kullanıcının cinsiyeti. 0-Kadın, 1-Erkek.
* **Company** (`string`): Kullanıcının bağlı olduğu şirketleri belirtir. "," (Virgül) ile ayrılarak yazılmalıdır. 
* **Department** (`string`): Kullanıcının bağlı olduğu departmanın ID değeri.
* **Profession** (`string`): Kullanıcının sahip olduğu ünvanın ID değeri.
* **PropertyValues** (`object[]`): Eklenecek olan departmana özel bir alan ekler. `null` geçilebilir.
    * **Name** (`string`): Özel alanın adı.
    * **Value** (`string`): Özel alanın değeri.
    * **ImportStatus** (`boolean`): Özel alanın HR transfer için içe aktarım durumu. 
* **Managers** (`object[]`): Kullanıcının yöneticilerinin girildiği alandır.
    * **Key** (`string`): Yöneticinin key değeri.
    * **ID** (`string`): Yönetici kullanıcının ID değeri. 

### api/User/**UpdateUser** `[POST]`
---
Var olan bir kullanıcının bilgilerini günceller.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "ID": "ycelik",
  "FirstName": "Yiğit",
  "LastName": "Çelik",
  "Password": "12345678",
  "Email": "ycelik@bimser.com",
  "Status": true,
  "Type": 0,
  "ImportStatus": true,
  "BirthDate": "2000-07-31T06:22:03.551Z",
  "EmploymentStart": "2024-03-27T06:22:03.551Z",
  "EmploymentEnd": "2024-03-27T06:22:03.551Z",
  "Category": 0,
  "Sex": 0,
  "Company": "Bimser,Test",
  "Department": "G4",
  "Profession": "T7",
  "PropertyValues": [
    {
      "Name": "Example",
      "Value": "this is test value",
      "ImportStatus": true
    }
  ],
  "Managers": [
    {
      "Key": "default",
      "ID": "tozer"
    }
  ]
}
```

#### Request Body Parameters
* **ID** (`string`): Kullanıcı ID değeri.
* **Firstname** (`string`): Kullanıcının adı.
* **Lastname** (`string`): Kullanıcının soyadı.
* **Password** (`string`): Kullanıcının şifresi.
* **Email** (`string`): Kullanıcının e-posta adresi.
* **Status** (`boolean`): Kullanıcının aktiflik/pasiflik durumu.
* **Type** (`string`): Kullanıcının türü.
* **ImportStatus** (`boolean`): HR transfer için içe aktarım durumu.
* **BirthDate** (`datetime`): Kullanıcının doğum tarihi.
* **EmploymentStart** (`datetime`): Kullanıcının işe giriş tarihi.
* **EmploymentEnd** (`datetime`): Kullanıcının işten çıkış tarihi.
* **Category** (`integer`): Kullanıcının mavi yada beyaz olacağını belirtir. 0-Mavi yaka, 1-Beyaz yaka.
* **Sex** (`integer`): Kullanıcının cinsiyeti. 0-Kadın, 1-Erkek.
* **Company** (`string`): Kullanıcının bağlı olduğu şirketleri belirtir. "," (Virgül) ile ayrılarak yazılmalıdır. Var olan değerler eğer update işleminde gönderilmezse bu değerler kullanıcıdan silinir, girilen farklı değerler varsa onlarda kullanıcıya eklenir. 
* **Department** (`string`): Kullanıcının bağlı olduğu departmanın ID değeri.
* **Profession** (`string`): Kullanıcının sahip olduğu ünvanın ID değeri.
* **PropertyValues** (`object[]`): Eklenecek olan departmana özel bir alan ekler. `null` geçilebilir.
    * **Name** (`string`): Özel alanın adı.
    * **Value** (`string`): Özel alanın değeri.
    * **ImportStatus** (`boolean`): Özel alanın HR transfer için içe aktarım durumu. 
* **Managers** (`object[]`): Kullanıcının yöneticilerinin girildiği alandır. Var olan değerler eğer update işleminde gönderilmezse bu değerler kullanıcıdan silinir, girilen farklı değerler varsa onlarda kullanıcıya eklenir.
    * **Key** (`string`): Yöneticinin key değeri.
    * **ID** (`string`): Yönetici kullanıcının ID değeri. 

### api/Property/**GetPropertyTypes** `[GET]`
---
Sistemdeki tüm özellik tiplerini getirir.

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
      "Name": "DigitalSignatureCertificateIdentifier",
      "Caption": "Digital Signature Certificate Identifier",
      "Description": "Digital Signature Certificate Identifier",
      "Type": 0,
      "DefaultValue": ""
    },
    {
      "Name": "ExternalUsername",
      "Caption": "External Username",
      "Description": "LDAP or custom Authentication username",
      "Type": 0,
      "DefaultValue": ""
    },
    {
      "Name": "HasDigitalSignatureCertificate",
      "Caption": "Has Digital Signature Certificate",
      "Description": "Has Digital Signature Certificate",
      "Type": 2,
      "DefaultValue": "False"
    }
  ]
}
```

### api/Property/**GetPropertyTypeDetail** `[POST]`
---
Name değerine göre sistemdeki bir özellik tipini getirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Property/GetPropertyTypeDetail?name=ExternalUsername

#### Request Query Parameters
- **name** (`string`): Özellik tipi name değeri.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": {
    "Name": "ExternalUsername",
    "Caption": "External Username",
    "Description": "LDAP or custom Authentication username",
    "Type": 0,
    "DefaultValue": ""
  }
}
```

### api/Property/**AddNewPropertyType** `[POST]`
---
Sisteme girilen bilgilerle yeni bir özellik tipi ekler.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "Name": "ExternalUsername",
  "Caption": "External Username",
  "Description": "Harici kullanıcı adı",
  "Type": 0,
  "DefaultValue": "admin"
}
```

#### Request Body Parameters
* **Name** (`string`): Özellik tipi adı.
* **Caption** (`string`): Özellik tipi başlığı.
* **Description** (`string`): Özellik tipi açıklaması.
* **Type** (`integer`): Özellik tipi değer tipi.
    * **0** Metin
    * **1** Sayı
    * **2** Evet/Hayır
    * **3** Tarih
    * **4** Liste
    * **5** Virgüllü Sayı
    * **6** Dosya
    * **7** Resim
    * **8** Tablodan
    * **9** Şifre
* **DefaultValue** (`string`): Özellik tipi varsayılan değeri.

### api/Property/**UpdatePropertyType** `[POST]`
---
Var olan bir özellik tipinin bilgilerini günceller.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "Name": "ExternalUsername",
  "Caption": "External Username",
  "Description": "Harici kullanıcı adı",
  "Type": 0,
  "DefaultValue": "admin"
}
```

#### Request Body Parameters
* **Name** (`string`): Özellik tipi adı.
* **Caption** (`string`): Özellik tipi başlığı.
* **Description** (`string`): Özellik tipi açıklaması.
* **Type** (`integer`): Özellik tipi değer tipi.
    * **0** Metin
    * **1** Sayı
    * **2** Evet/Hayır
    * **3** Tarih
    * **4** Liste
    * **5** Virgüllü Sayı
    * **6** Dosya
    * **7** Resim
    * **8** Tablodan
    * **9** Şifre
* **DefaultValue** (`string`): Özellik tipi varsayılan değeri.

### api/Property/**DeletePropertyType** `[POST]`
---
Sistemdeki bir özellik tipini siler.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Property/DeletePropertyType?name=ExternalUsername

#### Request Query Parameters
- **name** (`string`): Özellik tipi adı.

### api/Property/**AddPropertyToUser** `[POST]`
---
Sistemdeki bir özellik tipini kullanıcı yapısıyla ilişkilendirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "Name": "ExternalUsername",
  "Order": 0,
  "Required": true
}
```

#### Request Body Parameters
* **Name** (`string`): Kullanıcı yapısıyla ilişkilendirilmek istenen özellik tipinin adı.
* **Order** (`integer`): Kullanıcı ekranında özellik tipinin sırası.
* **Required** (`boolean`): Özellik tipinin zorunluluk durumu.

### api/Property/**RemovePropertyFromUser** `[POST]`
---
Sistemdeki bir özellik tipini kullanıcı yapısından kaldırır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Property/RemovePropertyFromUser?name=ExternalUsername

#### Request Query Parameters
- **name** (`string`): Özellik tipi adı.

### api/Property/**AddPropertyToPosition** `[POST]`
---
Sistemdeki bir özellik tipini pozisyon yapısıyla ilişkilendirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "Name": "ExternalUsername",
  "Order": 0,
  "Required": true
}
```

#### Request Body Parameters
* **Name** (`string`): Pozisyon yapısıyla ilişkilendirilmek istenen özellik tipinin adı.
* **Order** (`integer`): Pozisyon ekranında özellik tipinin sırası.
* **Required** (`boolean`): Özellik tipinin zorunluluk durumu.

### api/Property/**RemovePropertyFromPosition** `[POST]`
---
Sistemdeki bir özellik tipini pozisyon yapısından kaldırır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Property/RemovePropertyFromPosition?name=ExternalUsername

#### Request Query Parameters
- **name** (`string`): Özellik tipi adı.

### api/Property/**AddPropertyToProfession** `[POST]`
---
Sistemdeki bir özellik tipini ünvan yapısıyla ilişkilendirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "Name": "ExternalUsername",
  "Order": 0,
  "Required": true
}
```

#### Request Body Parameters
* **Name** (`string`): Ünvan yapısıyla ilişkilendirilmek istenen özellik tipinin adı.
* **Order** (`integer`): Ünvan ekranında özellik tipinin sırası.
* **Required** (`boolean`): Özellik tipinin zorunluluk durumu.

### api/Property/**RemovePropertyFromProfession** `[POST]`
---
Sistemdeki bir özellik tipini ünvan yapısından kaldırır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Property/RemovePropertyFromProfession?name=ExternalUsername

#### Request Query Parameters
- **name** (`string`): Özellik tipi adı.

### api/Property/**AddPropertyToDepartment** `[POST]`
---
Sistemdeki bir özellik tipini departman yapısıyla ilişkilendirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "Name": "ExternalUsername",
  "Order": 0,
  "Required": true
}
```

#### Request Body Parameters
* **Name** (`string`): Departman yapısıyla ilişkilendirilmek istenen özellik tipinin adı.
* **Order** (`integer`): Departman ekranında özellik tipinin sırası.
* **Required** (`boolean`): Özellik tipinin zorunluluk durumu.

### api/Property/**RemovePropertyFromDepartment** `[POST]`
---
Sistemdeki bir özellik tipini departman yapısından kaldırır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Property/RemovePropertyFromDepartment?name=ExternalUsername

#### Request Query Parameters
- **name** (`string`): Özellik tipi adı.

### api/Property/**AddPropertyToGroup** `[POST]`
---
Sistemdeki bir özellik tipini grup yapısıyla ilişkilendirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "Name": "ExternalUsername",
  "Order": 0,
  "Required": true
}
```

#### Request Body Parameters
* **Name** (`string`): Grup yapısıyla ilişkilendirilmek istenen özellik tipinin adı.
* **Order** (`integer`): Grup ekranında özellik tipinin sırası.
* **Required** (`boolean`): Özellik tipinin zorunluluk durumu.

### api/Property/**RemovePropertyFromGroup** `[POST]`
---
Sistemdeki bir özellik tipini grup yapısından kaldırır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Property/RemovePropertyFromGroup?name=ExternalUsername

#### Request Query Parameters
- **name** (`string`): Özellik tipi adı.

### api/Role/**GetRoles** `[GET]`
---
Sistemdeki tüm rolleri getirir.

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
      "Name": "Admin",
      "Description": "Admin"
    },
    {
      "Name": "Default",
      "Description": "Default"
    },
    {
      "Name": "Standard",
      "Description": "Standart"
    }
  ]
}
```

### api/Role/**GetUserRoles** `[GET]`
---
Sistemdeki tüm kullanıcı rollerini getirir.

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
      "ID": "adogru",
      "Description": "Ali Doğru"
    },
    {
      "ID": "hkar",
      "Description": "Huseyin Kar"
    },
    {
      "ID": "kseckin",
      "Description": "Kerim Seçkin"
    }
  ]
}
```

### api/Role/**GetDepartmentRoles** `[GET]`
---
Sistemdeki tüm departman rollerini getirir.

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
      "ID": "G2",
      "Description": "Finans ve Mali işler"
    },
    {
      "ID": "G1",
      "Description": "Üretim"
    }
  ]
}
```

### api/Role/**GetPositionRoles** `[GET]`
---
Sistemdeki tüm pozisyon rollerini getirir.

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
      "ID": "PG1008",
      "Description": "Yazılım Uzmanı"
    },
    {
      "ID": "PG1007",
      "Description": "Yazılım Teknik Lideri"
    }
  ]
}
```

### api/Role/**GetGroupRoles** `[GET]`
---
Sistemdeki tüm grup rollerini getirir.

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
      "ID": "everyone",
      "Description": "Everyone"
    },
    {
      "ID": "BM",
      "Description": "Board Members"
    }
  ]
}
```

### api/Role/**GetProfessionRoles** `[GET]`
---
Sistemdeki tüm ünvan rollerini getirir.

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
      "ID": "T4",
      "Description": "Uzman"
    }
    {
      "ID": "T5",
      "Description": "Yönetici"
    }
  ]
}
```

### api/Role/**AddRoleToUser** `[POST]`
---
Girilen bilgilere göre bir kullanıcıyı bir yetki ile ilişkilendirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "App": "eba",
  "Name": "adogru",
  "IncludeName": "web.Delegation",
  "IncludeType": 1
}
```

#### Request Body Parameters
* **App** (`string`): Yetkinin uygulanacağı uygulama adı, genelde "eba" olarak verilir.
* **Name** (`string`): Yetkinin uygulanacağı kullanıcı ID değeri.
* **IncludeName** (`string`): Yetkinin adı.
* **IncludeType** (`integer`): Yetkinin tipi.
  * **1**: Yetki
  * **2**: Yetki Grubu

### api/Role/**RemoveRoleFromUser** `[POST]`
---
Girilen bilgilere göre bir kullanıcıdaki yetkiyi kaldırır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "App": "eba",
  "Name": "adogru",
  "IncludeName": "web.Delegation",
  "IncludeType": 1
}
```

#### Request Body Parameters
* **App** (`string`): Yetkinin kaldırılacağı uygulama adı, genelde "eba" olarak verilir.
* **Name** (`string`): Yetkinin kaldırılacağı kullanıcı ID değeri.
* **IncludeName** (`string`): Yetkinin adı.
* **IncludeType** (`integer`): Yetkinin tipi.
  * **1**: Yetki
  * **2**: Yetki Grubu

### api/Role/**AddRoleToDepartment** `[POST]`
---
Girilen bilgilere göre bir departmanı bir yetki ile ilişkilendirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "App": "eba",
  "Name": "DEP001",
  "IncludeName": "webLoginAsUser",
  "IncludeType": 1
}
```

#### Request Body Parameters
* **App** (`string`): Yetkinin uygulanacağı uygulama adı, genelde "eba" olarak verilir.
* **Name** (`string`): Yetkinin uygulanacağı departman ID değeri.
* **IncludeName** (`string`): Yetkinin adı.
* **IncludeType** (`integer`): Yetkinin tipi.
  * **1**: Yetki
  * **2**: Yetki Grubu

### api/Role/**RemoveRoleFromDepartment** `[POST]`
---
Girilen bilgilere göre bir kullanıcıdaki yetkiyi kaldırır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "App": "eba",
  "Name": "DEP001",
  "IncludeName": "webLoginAsUser",
  "IncludeType": 1
}
```

#### Request Body Parameters
* **App** (`string`): Yetkinin kaldırılacağı uygulama adı, genelde "eba" olarak verilir.
* **Name** (`string`): Yetkinin kaldırılacağı departman ID değeri.
* **IncludeName** (`string`): Yetkinin adı.
* **IncludeType** (`integer`): Yetkinin tipi.
  * **1**: Yetki
  * **2**: Yetki Grubu

### api/Role/**AddRoleToProfession** `[POST]`
---
Girilen bilgilere göre bir ünvanı bir yetki ile ilişkilendirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "App": "eba",
  "Name": "T1",
  "IncludeName": "managerFlowManager",
  "IncludeType": 1
}
```

#### Request Body Parameters
* **App** (`string`): Yetkinin uygulanacağı uygulama adı, genelde "eba" olarak verilir.
* **Name** (`string`): Yetkinin uygulanacağı ünvan ID değeri.
* **IncludeName** (`string`): Yetkinin adı.
* **IncludeType** (`integer`): Yetkinin tipi.
  * **1**: Yetki
  * **2**: Yetki Grubu

### api/Role/**RemoveRoleFromProfession** `[POST]`
---
Girilen bilgilere göre bir ünvandaki yetkiyi kaldırır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "App": "eba",
  "Name": "T1",
  "IncludeName": "managerFlowManager",
  "IncludeType": 1
}
```

#### Request Body Parameters
* **App** (`string`): Yetkinin kaldırılacağı uygulama adı, genelde "eba" olarak verilir.
* **Name** (`string`): Yetkinin kaldırılacağı ünvan ID değeri.
* **IncludeName** (`string`): Yetkinin adı.
* **IncludeType** (`integer`): Yetkinin tipi.
  * **1**: Yetki
  * **2**: Yetki Grubu

### api/Role/**AddRoleToPosition** `[POST]`
---
Girilen bilgilere göre bir pozisyonu bir yetki ile ilişkilendirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "App": "eba",
  "Name": "PG1008",
  "IncludeName": "designerAdmin",
  "IncludeType": 2
}
```

#### Request Body Parameters
* **App** (`string`): Yetkinin uygulanacağı uygulama adı, genelde "eba" olarak verilir.
* **Name** (`string`): Yetkinin uygulanacağı pozisyon ID değeri.
* **IncludeName** (`string`): Yetkinin adı.
* **IncludeType** (`integer`): Yetkinin tipi.
  * **1**: Yetki
  * **2**: Yetki Grubu

### api/Role/**RemoveRoleFromPosition** `[POST]`
---
Girilen bilgilere göre bir pozisyondaki yetkiyi kaldırır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "App": "eba",
  "Name": "PG1008",
  "IncludeName": "designerAdmin",
  "IncludeType": 2
}
```

#### Request Body Parameters
* **App** (`string`): Yetkinin kaldırılacağı uygulama adı, genelde "eba" olarak verilir.
* **Name** (`string`): Yetkinin kaldırılacağı pozisyon ID değeri.
* **IncludeName** (`string`): Yetkinin adı.
* **IncludeType** (`integer`): Yetkinin tipi.
  * **1**: Yetki
  * **2**: Yetki Grubu

### api/Role/**AddRoleToGroup** `[POST]`
---
Girilen bilgilere göre bir grubu bir yetki ile ilişkilendirir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "App": "eba",
  "Name": "everyone",
  "IncludeName": "Default",
  "IncludeType": 2
}
```

#### Request Body Parameters
* **App** (`string`): Yetkinin uygulanacağı uygulama adı, genelde "eba" olarak verilir.
* **Name** (`string`): Yetkinin uygulanacağı grup ID değeri.
* **IncludeName** (`string`): Yetkinin adı.
* **IncludeType** (`integer`): Yetkinin tipi.
  * **1**: Yetki
  * **2**: Yetki Grubu

### api/Role/**RemoveRoleFromPosition** `[POST]`
---
Girilen bilgilere göre bir gruptaki yetkiyi kaldırır.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
```json
{
  "App": "eba",
  "Name": "everyone",
  "IncludeName": "Default",
  "IncludeType": 2
}
```

#### Request Body Parameters
* **App** (`string`): Yetkinin kaldırılacağı uygulama adı, genelde "eba" olarak verilir.
* **Name** (`string`): Yetkinin kaldırılacağı grup ID değeri.
* **IncludeName** (`string`): Yetkinin adı.
* **IncludeType** (`integer`): Yetkinin tipi.
  * **1**: Yetki
  * **2**: Yetki Grubu

### api/Property/**GetUserRoleContents** `[POST]`
---
Bir kullanıcının hangi genel role dahil olduğunu belirtir.

#### Headers
**Content-Type**: `application/json`\
**Token**: `token`

#### Request Example
http://localhost/eBAHRAPI/api/Role/GetUserRoleContents?userId=hkar

#### Request Query Parameters
- **userId** (`string`): Kullanıcı ID değeri.

#### Response Example
```json
{
  "Success": true,
  "Code": 200,
  "Result": [
     {
      "ID": "hkar",
      "Name": "Admin",
      "Description": "Huseyin Kar"
    }
  ]
}
```

























