# Flow'un Hangi Adımında Olduğunu Tespit Etmek

Form tarafında, akışın hangi adımında olunduğu bilgisi, aşağıdaki kod ile öğrenilebilir.

## Gerekli Kütüphaneler

	using System;
	using System.Collections.Generic;
	using Bimser.CSP.FormControls.Common;
	using Bimser.CSP.FormControls.Events;
	using Newtonsoft.Json.Linq;
	using Bimser.Synergy.Entities.Workflow.Runtime.Models.Controller;
	using Bimser.CSP.Runtime.Common.Extensions;

## Kod

	if (ResponseParameters.TryGetValue("workflowInfo", out object workflowInfoObject))
	            {
	                var workflowInfo = ((JObject)workflowInfoObject).ToObject<WorkflowInfo>();

	                LogExtension.Log("Mevcut Adım: "+workflowInfo.CurrentStep.Name,Session);

	            }