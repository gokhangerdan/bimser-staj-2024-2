# Kodla DataSource Çalıştırma

Aşağıdaki kodlar kullanılarak, Flow tarafında kod ile DataSource çalıştırılıp dönen sonuç okunabilir.

## Gerekli Kütüphaneler

	using Bimser.Synergy.Entities.Workflow.EventArguments;
	using System;
	using Bimser.CSP.Runtime.Common.Extensions;
	using Bimser.Synergy.ServiceAPI; 
	using Bimser.Synergy.ServiceAPI.Models.Authentication; 
	using Bimser.Synergy.ServiceAPI.Models.Form; 
	using Newtonsoft.Json; 
	using Bimser.Synergy.Entities.Shared.Business.Objects;
	using System.Threading.Tasks;
	using System.Collections.Generic;
	using Bimser.CSP.FormControls.Common;

## Kod

	 // Sorgudan dönecek sonuç bu sınıfa yazılır.
		   public class UserData
	        {
	            public string UserName{get;set;}

	        }

		   public void Position1_OnAfterExecution(object sender,OnAfterExecutionArguments args)
	        {
		// Sorguya gönderilecek parametreler bu kısımda verilir.
	            var parameters = new
	            {
	                ID= ".."//parametre değeri
	            };
	            var result = ServiceApi.DataSourceManager.ExecuteQuery<UserData>("PROJE_ADI", "DATASOURCE_ADI",parameters).Result;
	            if (result.Count>0)
	            {
	                foreach (var resultItem in result)
	                {
	                    LogExtension.Log(resultItem.UserName,args.Context);
	                }

	            }
	            else{
	                LogExtension.Log("noresult",args.Context);
	            }
	        }