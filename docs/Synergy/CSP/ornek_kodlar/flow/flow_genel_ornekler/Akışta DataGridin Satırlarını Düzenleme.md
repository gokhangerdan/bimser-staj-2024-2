# Akışta DataGrid'in Satırlarını Düzenleme

```csharp
    using Bimser.Synergy.ServiceAPI.Models.Form;
    using Newtonsoft.Json;

    GridData gridData = GridData.FromControl(Document1.Controls["DataGrid1"]);
    gridData.Rows.ForEach(row => {
        row.Cells[2].Value = true;
    });

    FormData formData = new FormData();
    formData.ControlValues.Add("DataGrid1", JsonConvert.SerializeObject(gridData));
    Document1.FormInstance.MergeData(formData.ControlValues);
    Document1.SaveDocument();
```
