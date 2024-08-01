# ServiceApi Kullanımı

## Gerekli Kütüphaneler

	using System;
	using Bimser.Synergy.ServiceAPI;
	using Bimser.Synergy.ServiceAPI.Models.Authentication;
	using Bimser.Synergy.Entities.Shared.Business.Objects;
	using Newtonsoft.Json;

## Kodlar

	protected LoginWithTokenAuthenticationParameters Credentials
	        {
	            get
	            {
	              return new LoginWithTokenAuthenticationParameters
	                {
	                    EncryptedData = _workflowData.Context.EncryptedData,
	                    Language = _workflowData.Context.Language,
	                    Token = _workflowData.Context.Token
	                };
	            }
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

	        private ServiceAPI _serviceApi;
	        protected ServiceAPI ServiceApi
	        { 
	            get
	            {
	                if(_serviceApi == null)
	                {
	                    _serviceApi = new ServiceAPI(Credentials,WebInterfaceUrl);
	                }
	                
	                return _serviceApi;
	            }
	        }

## Örnek Kullanım

Aşağıdaki kod ile, örnek olarak, ServiceApi ile bir process oluşturulabilir.

	ServiceApi.WorkflowManager.Create("projectName","flowName");