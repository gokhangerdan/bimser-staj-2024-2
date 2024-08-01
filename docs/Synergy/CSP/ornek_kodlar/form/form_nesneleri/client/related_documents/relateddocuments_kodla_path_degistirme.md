# Related Documents Kodla Path Değiştirme

```
using System;
using System.Linq;
using Bimser.CSP.FormControls.Controls;
using Bimser.CSP.FormControls.Events;
using Bimser.CSP.Runtime.Common.Extensions;
using Bimser.Synergy.Entities.DocumentManagement.Business.DTOs.Requests;
using Bimser.Synergy.Entities.DocumentManagement.Business.DTOs.Responses;
using Bimser.Synergy.Entities.Shared.Business.Objects;
using Bimser.Synergy.ServiceAPI;
using Bimser.Synergy.ServiceAPI.Models.Authentication;
using Newtonsoft.Json;

namespace test.Forms
{
    
    public partial class Form2
    {
        internal static ServiceAPI GetServiceApiInstance(UserSession session, string webInterfaceUrl = null)
        {
            var credentials = GetTokenCredential(session);
            return new ServiceAPI(credentials, webInterfaceUrl ?? WebInterfaceUrl);
        }

        internal static LoginWithTokenAuthenticationParameters GetTokenCredential(UserSession session)
        {
            return new LoginWithTokenAuthenticationParameters()
            {
                DomainAddress = WebInterfaceUrl,
                Token = session.Token,
                EncryptedData = session.EncryptedData,
                Language = session.Language
            };
        }
        internal static HttpClientOptions _httpClientOptions;
        internal static string WebInterfaceUrl
        {
            get
            {
                if (_httpClientOptions == null)
                {
                    string envVar = Environment.GetEnvironmentVariable("HTTP_CLIENT_OPTIONS");
                    _httpClientOptions = JsonConvert.DeserializeObject<HttpClientOptions>(envVar);
                }

                return _httpClientOptions.WebInterfaceUrl;
            }
        }

        private string GetFolderSecretKey(ServiceAPI serviceapi, string path)
        {
            string root = path.Replace(@"\", "/");
            Bimser.Framework.Web.Models.WrapResponse<GetDMObjectsResponse> dmRootFolder = serviceapi.DocumentManagement.GetDMObjectsFromPath(new GetDMObjectsFromPathRequest(root)).Result;
            if (dmRootFolder.Success && dmRootFolder.Result.Items.Count > 0)
            {
              GetDMObjectResponse dmObject = dmRootFolder.Result.Items.First();
              return dmObject.SecretKey;
            }
            return null;
        }
   
		void RadioList1_OnValueChanged(object sender, PropertyChangedEventArgs<object> e)
		{
            var serviceapi = GetServiceApiInstance(Session);

            if (Convert.ToInt16(RadioList1.Value)==1)
            {
                RelatedDocuments1.Path="AnaDizin/AnaKlasor/Klasor1";
                RelatedDocuments1.TargetSecretKey= GetFolderSecretKey(serviceapi, RelatedDocuments1.Path);   
            }
            else if(Convert.ToInt16(RadioList1.Value)==2)
            {
                RelatedDocuments1.Path="AnaDizin/AnaKlasor/Klasor2";
                RelatedDocuments1.TargetSecretKey= GetFolderSecretKey(serviceapi, RelatedDocuments1.Path);
            }

		}
 }
}


```

