# İlişkili DataGrid'e Satır Eklemek

Aşağıdaki kodlar kullanılarak Flow tarafında, formdaki bir  ilişkili DataGrid'e satır eklenebilir.

İlişkili DataGrid'in her satırı aslında bir form olduğu için, satır eklemeden önce; 
- İlgili formu oluşturmak, içerisindeki verileri doldurmak ve kaydedip documentId değerini almak gerekir.
- Sonrasında DataGrid'e eklenecek satır hazırlanır.
- Daha sonra DataGrid'in olduğu forma erişmek gerekir. Buradan DataGrid'e erişilir. Satır eklenir. Veri birşleştirilir. Form kaydedilir.

## Gerekli Kütüphaneler

	using Bimser.Synergy.Entities.Workflow.EventArguments;
	using System;
	using Bimser.Synergy.ServiceAPI;
	using Bimser.Synergy.ServiceAPI.Models.Authentication;
	using Bimser.Synergy.Entities.Shared.Business.Objects;
	using Newtonsoft.Json;
	using Bimser.CSP.Runtime.Common.Extensions;
	using System.Collections.Generic;
	using System.Threading.Tasks;
	using Bimser.Synergy.ServiceAPI.Models.Form;

## Kodlar

	//modal formu doldurma
			FormInstance modalForm = GetFormInstance("projeAdi","modalformAdi",0).Result;
	            modalForm.Controls["TextBox1"].Value = "text";
	            modalForm.Controls["TextBox1"].Text = "text";
	            var docid = modalForm.Save().Result.DocumentId;

	            // DataGrid'e yeni satır ekleme
	            GridDataRow newRow = new GridDataRow
	            {
	                Cells = new List<GridDataRowCell>
	                {
	                    new GridDataRowCell(docid,"RELATIONDOCUMENTID"), 
	                    new GridDataRowCell(modalForm.Controls["TextBox1"].Text,"TextBox1")
	                }
	            };

	            //DataGrid'in oldugu forma erismek
	            FormInstance form = GetFormInstance("projeAdi","formAdi",Document1.DocumentId).Result;
	            Control control =form.Controls["DataGrid1"]; //Form üzerindeki DataGrid verisine ulaşılır
	            GridData DataGrid1Data = GridData.FromControl(control); //İşlemler için formdata'dan griddata'ya cast edilir.
	            DataGrid1Data.Rows.Add(newRow); // satırın eklenmesi
	            // DataGrid içindeki veriyi eski DataGrid ile birleştirme
	            FormData data = new FormData();
	            data.ControlValues.Add("DataGrid1", JsonConvert.SerializeObject(DataGrid1Data));
	            form.MergeData(data.ControlValues);
	            form.Save();