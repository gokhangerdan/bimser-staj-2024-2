# ServiceApi Kullanımı

## Gerekli Kütüphaneler

	using System;
	using System.Collections.Generic;
	using Bimser.CSP.FormControls.Common;
	using Bimser.CSP.FormControls.Events;
	using Bimser.Synergy.ServiceAPI;
	using Bimser.Synergy.ServiceAPI.Models.Authentication;
	using Bimser.CSP.DataSource.Api.Models;
	using Newtonsoft.Json;

## Kodlar

	protected LoginWithTokenAuthenticationParameters Credentials
	        {
	            get
	            {
	              return new LoginWithTokenAuthenticationParameters
	                {
	                    EncryptedData = Session.EncryptedData,
	                    Language = Session.Language,
	                    Token = Session.Token
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

Aşağıdaki kod ile, örnek olarak, ServiceApi ile bir form oluşturulabilir. 

	ServiceApi.FormManager.Create("projectName","formName",123);

	(Parametreler: proje adı, form adı, documentId)