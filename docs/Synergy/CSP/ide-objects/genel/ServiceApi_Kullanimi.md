# ServiceAPI Kullanım Dokümantasyonu
Bu dokümantasyon, Synergy projelerinde kullanılan ServiceAPI sınıfının kullanımını ve yapılandırmasını açıklamaktadır. ServiceAPI, REST API üzerinden sisteme erişim sağlayan bir arayüzdür.

## ServiceAPI Nedir?
ServiceAPI, Bimser.Synergy.ServiceAPI namespacesi altında yer alan bir sınıftır. Bu sınıf, Synergy projelerinde formlarla ve akışlarla etkileşim kurmak için kullanılır. ServiceAPI üzerinden veriler alınabilir, güncellenebilir, yeni formlar oluşturulabilir, akışlar başlatılabilir ve dosya işlemleri gibi doküman yönetimi işlemleri gerçekleştirilebilir.

# TokenAuthentication ile Formda ServiceAPI Oluşturma
TokenAuthentication kullanarak ServiceAPI oluşturmak için aşağıdaki adımları izleyebilirsiniz:

1.  İlgili using direktiflerini ekleyin:
    ```csharp
    using Bimser.Synergy.ServiceAPI.Models.Authentication;
    using Bimser.Synergy.ServiceAPI;
    ```
2.  Formda ServiceAPI'nin instance'ını oluşturacak bir metot tanımlayın:
    ```csharp
    private void CreateServiceApiInstance()
    {
        string webInterfaceUrl = "https://danismanlik.bimser.net/web/api";
        var tokenAuthenticationParameters = new LoginWithTokenAuthenticationParameters
        {
            EncryptedData = Session.EncryptedData,
            Language = Session.Language,
            Token = Session.Token,
        };
        ServiceAPI serviceApi = new ServiceAPI(tokenAuthenticationParameters, webInterfaceUrl);
    }
    ```
3.  **webInterfaceUrl** değişkenine ServiceAPI'nin erişeceği REST API'nin URL'ini atayın.
4.  **tokenAuthenticationParameters** değişkenine kullanıcı oturum bilgilerini (şifrelenmiş veri, dil, token) atayın.
5.  **ServiceAPI** sınıfından yeni bir instance oluşturun, parametre olarak **tokenAuthenticationParameters** ve **webInterfaceUrl** değerlerini verin.

# TokenAuthentication ile Akışta ServiceAPI Oluşturma
TokenAuthentication kullanarak ServiceAPI oluşturmak için aşağıdaki adımları izleyebilirsiniz:

1.  İlgili using direktiflerini ekleyin:
    ```csharp
    using Bimser.Synergy.ServiceAPI.Models.Authentication;
    using Bimser.Synergy.ServiceAPI;
    ```
2.  Formda ServiceAPI'nin instance'ını oluşturacak bir metot tanımlayın:
    ```csharp
    private void CreateServiceApiInstance()
    {
        string webInterfaceUrl = "https://danismanlik.bimser.net/web/api";
        var tokenAuthenticationParameters = new LoginWithTokenAuthenticationParameters
        {
            EncryptedData = _workflowData.Context.EncryptedData,
            Language = _workflowData.Context.Language,
            Token = _workflowData.Context.Token,
        };
        ServiceAPI serviceApi = new ServiceAPI(tokenAuthenticationParameters, webInterfaceUrl);
    }
    ```
3.  **webInterfaceUrl** değişkenine ServiceAPI'nin erişeceği REST API'nin URL'ini atayın.
4.  **_workflowData.Context** içerisindeki oturum bilgilerini (EncryptedData, Language, Token) **tokenAuthenticationParameters** değişkenine atayın.
5.  **ServiceAPI** sınıfından yeni bir instance oluşturun, parametre olarak **tokenAuthenticationParameters** ve **webInterfaceUrl** değerlerini verin.

## Basic Authentication ile ServiceAPI Oluşturma
Basic Authentication kullanarak ServiceAPI oluşturmak için aşağıdaki adımları izleyebilirsiniz:
1.  İlgili using direktiflerini ekleyin:
    ```csharp
    using Bimser.Synergy.ServiceAPI.Models.Authentication;
    using Bimser.Synergy.ServiceAPI;
    ```
2.  Formda veya akışta ServiceAPI'nin instance'ını oluşturacak bir metot tanımlayın:
    ```csharp
    private void CreateServiceApiInstance()
    {
        string webInterfaceUrl = "https://danismanlik.bimser.net";
        var basicAuthenticationParameters = new LoginWithBasicAuthenticationParameters
        {
            DomainAddress = webInterfaceUrl,
            Language = "tr-TR",
            Username = "Oturum Açacak Kullanıcı Adı",
            Password = "Oturum Açacak Kullanıcının Parolası",
            RememberMe = false
        };
        ServiceAPI serviceApi = new ServiceAPI(basicAuthenticationParameters, webInterfaceUrl);
    }

    ```
3.  **webInterfaceUrl** değişkenine ServiceAPI'nin erişeceği REST API'nin URL'ini atayın.
4.  **basicAuthenticationParameters** değişkenine kullanıcı oturum bilgilerini (alan adı, dil, kullanıcı adı, parola, hatırla) atayın.
5.  **ServiceAPI** sınıfından yeni bir instance oluşturun, parametre olarak **basicAuthenticationParameters** ve **webInterfaceUrl** değerlerini verin.