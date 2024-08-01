# Log Yazdırma

Aşağıdaki kodlar kullanılarak konsola log yazdırılabilir.

## Gerekli Kütüphaneler

	using Bimser.CSP.Runtime.Common.Extensions;

## Kod

	LogExtension.Log("log",args.Context);
	LogExtension.Warning("warning",args.Context);
	LogExtension.Error("error",args.Context);

![](https://docsbimser.blob.core.windows.net/imagecontainer/ornekLog(Flow)-4bcc56cc-2795-4cd2-a97d-0e1044f96de1.png)

## NOT

Flow nesnelerinin fonksiyonlarının içerisinde log yazdırırken args.Context kullanılabilir. 

Ancak args'ye erişimin olmadığı durumlarda, örneğin kendi oluşturduğunuz bir fonksiyonda, bunun yerine _workflowData.Context kullanılabilir.