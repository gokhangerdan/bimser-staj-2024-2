# Synergy CSP Alt Akış Başlatma

Alt akış başlatma örnek koduna aşağıda ulaşabilirsiniz.
Not:
- TEST adlı projeden, TEST2 adlı projenin Flow1'i alt akış olarak başlatılmıştır.
- Başlayan alt akışta kullanıcının önüne gelecek olan formdaki TextBox nesnesine, ana akıştan bir değer atanmıştır.
- Başlayan alt akışta bir atama nesnesi ile, alt akış başladıktan sonra pozisyon nesnesinde sürecin hangi kullanıcıya gideceği değişkenden seçilmiştir. Bu değişkene atanacak değer de aşağıdaki kodlarda alt akışa gönderilmiştir. 
```
using System;
using Bimser.Synergy.Entities.Workflow.EventArguments;
using Bimser.CSP.Runtime.Common.Extensions;
using Bimser.Synergy.ServiceAPI; 
using Bimser.Synergy.ServiceAPI.Models.Authentication; 
using Newtonsoft.Json; 
using Bimser.Synergy.Entities.Shared.Business.Objects;
using System.Threading.Tasks;
using Bimser.Synergy.ServiceAPI.Models.Workflow;
using Bimser.Synergy.Entities.Workflow.Runtime.Models.Controller;
namespace TEST.Flows
{
	public partial class Flow1
	{
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
		public async Task<WorkflowInstance> CreateProcess(string projectName, string flowName, long processId = 0)
		{

			return await ServiceApi.WorkflowManager.Create(projectName, flowName, processId);
		}
		public  Task<FlowSaveAndContinueResponse> StartProcess()
		{
			var process =  CreateProcess("TEST2", "Flow1", 0).Result;

			// Alt akışa ait dokümana erişmek için kullanılır
			var form = process.Documents["Document1"].FormInstance;
			form.Controls["TextBox1"].Value = "alt akış";
			form.Save();
			// Alt akışın gönder eventiyle başlatılmasını sağlar
			process.StartingEvent = process.Events[4];
			// Alt akışı başlattığımız ana akışın processId’si gönderilir
			// MainProcessId alt akışta tanımladığımız public değişkenin adıdır
			//process.Variables["MainProcessId"] = _workflowData.General.ProcessId;
			// Alt akışta onayına gitmesini istediğimiz kullanıcının userId’si gönderilir
			// VarUserId alt akışta tanımladığımız public değişkenin adıdır
			process.Variables["VarUserId"] = "2";//akis ndale kullanicisinin uzerine dusecek

			return  process.SaveAndContinue();
		}


		public void FlowStart1_OnAfterExecution(object sender,OnAfterExecutionArguments args)
		{
			StartProcess();
		}
	}
}
```