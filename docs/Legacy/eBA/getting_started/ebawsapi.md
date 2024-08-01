# EBA WEB SERVİCE START-CONTINUE

## 1. Bilgilendirme

Harici uygulamaya webservis linki  web reference olarak eklenmesi gerekmektedir

--> http://localhost/eba.net/ws/ebawsapi.asmx

**İşlem yapacak kullanıcıda  aşağıdaki yetki olması gerekmektedir.

-- sysHiddenImpersonation 
-- sysImpersonation 

** Request id için 

select * from FLOWREQUESTS Where PROCESSID='1465'

Sorgudan Dönen ID değerin son değerini almak gerekmektedir.

## 2. Akış Tarafı

Akış tarafına 2 tane değişken ekliyoruz. bunlardan 1 tanesi formid alacak (Harici uygulamada form create edilecek) 2.ci ise sürecin hariciden başladığını belirtecek değeri tutan değişken olacaktır.

akışta karşılaştırma nesnesine göre yönlendirme yapılacaktır. görseli paylaşıyorum.


![](https://docsbimser.blob.core.windows.net/imagecontainer/akisresim-2163121a-ec7f-474b-820b-ffc433dd3592.png)

## 3. WebService C# Code

```
namespace external_EBA_Project
{
    internal class Program
    {    
        static void Main(string[] args)
        {
          EbaProjeService projeService = new EbaProjeService();

            projeService.EbaStartProcess("Ext_EbaProject");

          //  projeService.EbaContinueProject(1465, 3, 5, "Harici Süreç devam edildi");
        }    
    }

    public class EbaProjeService
    {
        eBAWSAPI ebaservice = new eBAWSAPI();
        public string ebauser { get; set; } = "admin";
        public string ebapass { get; set; } = "0";
        public string ebatargetuser { get; set; } = "admin";
        public string ebalanguage { get; set; } = "Turkish";

        public void EbaStartProcess(string projename) //Ext_EbaProject
        {
            // Form oluşturuyoruz...
            CreateFormParameters createForm = new CreateFormParameters();

            createForm.Form = "Form";
            createForm.Process = projename;

            var resultform = ebaservice.CreateForm(ebauser, ebapass, ebatargetuser, ebalanguage, createForm);


            // Akış tarafına parametre gönderiyoruz.
            WorkflowStartParameters startParameters = new WorkflowStartParameters();
            List<WorkflowParameter> parameters = new List<WorkflowParameter>();
            parameters.Add(new WorkflowParameter()
            {
                Name = "vStatus",
                Value = "1"
            });
            parameters.Add(new WorkflowParameter()
            {
                Name = "vdocid",
                Value = resultform.DocumentId.ToString()
            });

            startParameters.Process = projename;
            startParameters.ProcessParameters = parameters.ToArray();

            //startprocess ile süreci tetikliyoruz.
            var result = ebaservice.StartProcess(ebauser, ebapass, ebatargetuser, ebalanguage, startParameters);

        }

        public void EbaContinueProject(int surecid,int requestid, int eventid,string reason)
        {
            WorkflowContinueParameters wfContinueParameters = new WorkflowContinueParameters();

            wfContinueParameters.ProcessId = surecid;  
            wfContinueParameters.RequestId = requestid;
            wfContinueParameters.ReturnValue = eventid; // Pozisyonun event id normalde 5 - 6 dır
            wfContinueParameters.Reason = reason;

            ebaservice.ContinueProcess(ebauser, ebapass, ebatargetuser, ebalanguage, wfContinueParameters);
        }


    }
        

}
```

