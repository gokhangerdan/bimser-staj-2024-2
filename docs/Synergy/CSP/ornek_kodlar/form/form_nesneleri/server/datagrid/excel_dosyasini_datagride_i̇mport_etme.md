# Excel Dosyasını DataGrid'e İmport Etme

Excel dosyasını DataGride import etmek için cs tarafında yazılan kod aşağıdaki şekilde olmalıdır,



```
using System;
using System.Collections.Generic;
using Bimser.CSP.FormControls.Common;
using Bimser.CSP.FormControls.Controls;
using Bimser.CSP.FormControls.Events;
using INTG_Excel_ServiceAPI.Entities;
using Bimser.CSP.Runtime.Common.Extensions;
// using Bimser.CSP.Workflow.EventArguments;
// using Bimser.CSP.Workflow.Runtime.Models.Controller;
using Bimser.Synergy.ServiceAPI;
using Bimser.Synergy.Entities.DocumentManagement.Business.DTOs.Responses;
using Bimser.Synergy.ServiceAPI.Models.Authentication;
using Bimser.Synergy.ServiceAPI.Models.Workflow;
using Bimser.Synergy.ServiceAPI.Models.Form;
using System.Threading.Tasks;
using System.Net;
using Aspose.Cells;
using System.Data;
using System.IO;

namespace INTG_Excel_ServiceAPI.Forms {
    public partial class Main_Form {
            void RelatedDocuments1_OnAfterFileAdd(object sender, RelatedDocumentsAddEventArgs e)
        {
            LogExtension.Log("On after file add working...",Session); 
            if (RelatedDocuments1.Files != null)
            {
                LogExtension.Log($"e.files is not null... {e.Files.Count}",Session);
                foreach (var file in RelatedDocuments1.Files)
                {  
                    ServiceAPI service = new ServiceAPI(new Bimser.Synergy.ServiceAPI.Models.Authentication.LoginWithTokenAuthenticationParameters()
                    {
                        EncryptedData = Session.EncryptedData,
                        Language = Session.Language,
                        Token = Session.Token
                    }, "https://...ADRES..../api/web");
                    GetDownloadUrlResponse response = service.DocumentManagement.GetDownloadUrl(file.SecretKey, file.Name).Result;
                    string url = "https://...ADRES..../api/web/"+response.DownloadUrl;
                    byte[] excelBytes;
                    using (var webClient = new WebClient()) 
                    { 
                        excelBytes = webClient.DownloadData(url);  
                    }
                    Workbook wb = new Workbook(new MemoryStream(excelBytes));
                    LogExtension.Log($"count :{wb.Worksheets.Count}",Session);
                    //Get the first worksheet.
                    Worksheet worksheet = wb.Worksheets[0];
                    LogExtension.Log($"worksheet :{worksheet}",Session);
                    
                    DataTable dt = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxDataRow, worksheet.Cells.MaxDataColumn + 1, new ExportTableOptions()  { ExportColumnName = true });
                    
                    if(dt != null && dt.Rows != null && dt.Rows.Count > 0)
                    {
                        LogExtension.Log("dt and dt.rows are not null...",Session);
                        foreach(DataRow row in dt.Rows){         
                            
                            DataGridRow rw = DataGrid1.NewRow();
                            ComboBox1.Text = row["Süreç Adı"].ToString();
                            rw["exc_ID"].Value =  Convert.ToInt32(row["ID"]); 
                            rw["str_Surec"].Text = row["Süreç"].ToString();
                            rw["str_SurecAdi"].Text = row["Süreç Adı"].ToString();
                            rw["str_Sorumlu"].Text = row["Sorumlu"].ToString();
                            rw["str_SorumluDepartman"].Text = row["Sorumlu Departman"].ToString();
                            DataGrid1.Rows.Add(rw);                            
                        }
                    }
                }
            }
        }
    }
}
```

Yukarı iletmiş olduğum kodda dikkat edilmesi gereken hususlar ise şunlardır.

1.Eklemiş olduğumuz RelatiedDocument nesnesinin  Server tarafındaki OnAfterFileAdd eventine bağlanmalı
2. İmport edeceğiniz Excel dosyasındaki sütun isimleri kodumuzda yazdığımız bilgiler ile eşleşmeli
3. Kullandığımız DataGrid nesnesindeki ekleyeceğimiz Column'lar kodumuzla aynı olmalı 


