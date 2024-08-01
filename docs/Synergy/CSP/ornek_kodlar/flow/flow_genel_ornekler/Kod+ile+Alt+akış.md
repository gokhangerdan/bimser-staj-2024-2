# Kod ile Alt Akışa İnme (Server)

 **using Bimser.Synergy.ServiceAPI.Models.Form;**

  
    public void Function1_Execute(object sender, OnExecuteEventArguments args) 
    {
    	var subflow = ServiceAPI.WorkflowManager.Create(_workflowData.General.ProjectName, "Flow2").Result;
    	subflow.Variables["vMainProcessId"] = _workflowData.General.ProcessId; //Parametre
    	subflow.Variables["vMainFormId"] = this.Document1.DocumentId;//Parametre
    	subflow.StartingEvent = subflow.Events[4];//Akış Başlangıç Kol Numarası
    	var res = subflow.SaveAndContinue().Result;
    }

