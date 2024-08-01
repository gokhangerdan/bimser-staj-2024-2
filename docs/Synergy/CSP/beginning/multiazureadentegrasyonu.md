# MULTI AZURE AD ENTEGRASYONU

Basic Azure AD entegrasyonunda yapılması gerekenler;

İlk olarak Database tarafında  CONFIGURATIONS tablosunda ‘Security.Section-sys.AdditionalLoginMethods’ KEYNAME alanına karşılık gelecek VALUE kolonunun düzenlenmesi gerekmektedir.

```
[

{

"name": "Azure AD",

"url": "https://<HOSTNAME>/oauth/azuread",

"icon": "",

"enabled": true,

"providerKeys": {

"TokenIssuer": "[https://login.microsoftonline.com/<TENANTID>/v2.0](https://login.microsoftonline.com/%3cTENANTID%3e/v2.0)",

"TokenAudience": "<CLIENTID>",

"OpenIdConfigurationEndPoint": "[https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration](https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration)"

}

}

]
```

**HOSTNAME** -> Ortamın dns adresi

**TENANTID** -> Müşterinin azure hesabının tenantid’ si. Müşteriden talep edilmelidir.

**CLIENTID** -> Azure AD entegrasyonu yaparken istediğimiz application registry'nin clientid'si. Bu bilgi hali hazırda var olan müşteriler tarafından bize verilmiş ve oauth servisinin konfigurasyonunda kullanılmaktadır.

Multi Azure  AD entegrasyonunda da yine aynı şekilde Database tarafında  CONFIGURATIONS tablosunda ‘Security.Section-sys.AdditionalLoginMethods’ KEYNAME alanına karşılık gelecek VALUE kolonunun düzenlenmesi gerekmektedir.

Örnek;
```
[

{

"name": "Azure AD1",

"url": "https://<HOSTNAME>/oauth/azuread1",

"icon": "https://synergy.net/logo1/ logo1.svg",

"enabled": true,

"providerKeys": {

"TokenIssuer": "[https://login.microsoftonline.com/<TENANTID>/v2.0](https://login.microsoftonline.com/%3cTENANTID%3e/v2.0)",

"TokenAudience": "<CLIENTID>",

"OpenIdConfigurationEndPoint": "[https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration](https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration)"

}

},

{

"name": "Azure AD2",

"url": "https://<HOSTNAME>/oauth/azuread2",

"icon": " https://synergy.net/logo2/ logo2.svg ",

"enabled": true,

"providerKeys": {

"TokenIssuer": "[https://login.microsoftonline.com/<TENANTID>/v2.0](https://login.microsoftonline.com/%3cTENANTID%3e/v2.0)",

"TokenAudience": "<CLIENTID>",

"OpenIdConfigurationEndPoint": "[https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration](https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration)"

}

},

{

"name": "Azure AD3",

"url": "https://<HOSTNAME>/oauth/azuread3",

"icon": " https://synergy.net/logo3/ logo3.svg ",

"enabled": true,

"providerKeys": {

"TokenIssuer": "[https://login.microsoftonline.com/<TENANTID>/v2.0](https://login.microsoftonline.com/%3cTENANTID%3e/v2.0)",

"TokenAudience": "<CLIENTID>",

"OpenIdConfigurationEndPoint": "[https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration](https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration)"

}

}

]  
<![if !supportLineBreakNewLine]>  
<![endif]>
```

"**name**" parametresi hangi domaine ismine karşılık geleceğini belirtmektedir.

"**url**" parametresinde sunucu tarafında oluşturulan servislerin configmap içinde belirtilen **AZURE_URL** parametesinin değeridir.  Yukarıdaki örnekte görüleceği üzere her bir domain için azuread1, azuread2 ve azuread3 olarak isimlendirilmiştir.

"**icon**":  parametresi her bir domain için login sayfasında yansıtılacak logoları temsil eder.

"TokenIssuer" ve  "TokenAudience" parametrelerinde herbir domaine ait TENANT_ID ve CLIENT_ID değerleri belirtilmektedir.

Database tarafında yapılan değişiklik sonrası core service restart edilmelidir.

Sunucu tarafında ise;

İlk olarak kaç adet domain varsa o kadar oauth servis create edilmelidir.

Aşağıdaki script ile ilgili alanlara gerekli bilgiler eklenerek sunucu tarafında helm ile servis create edilir.
```
helm upgrade --install oauthservice-0 --atomic --namespace=synergy --set deploymentName=oauthservice-0 --set environments.azureEnabled=false --set environments.googleEnabled=false --set environments.linkedInEnabled=false --set environments.ldapEnabled=true --set environments.oauth20Enabled=false --set environments.ldapUrl=””  --set environments.ldapPort=3003 --set environments.azurePort=3000 --set environments.googlePort=3001 --set environments.linkedInPort=3002 --set environments.oauth20Port=3004 --set environments.ldapBindDN=" " --set environments.ldapBindCredentials= environments.ldapSearchBase= --set environments.ldapSearchFilter=\(sAMAccountName\=\{\{username\}\}\) --set global.image.repository=synergystable.azurecr.io synergystable.azurecr.io/oauthservice
```
Her bir servisin  configmap kısmında aşağıdaki komut ile düzenlemeler sağlanır.

Kubectl edit cm -n synergy oauthservice-0-cm

AZURE_CLIENTID, AZURE_CLIENTSECRET, AZURE_URL parametrelerindeki bilgiler girilerek servis tarafında düzenlemeler sağlanır.

Son olarak oluşturulan oauth servisler restart edilerek entegrasyon tamamlanmış olur.	
