# Form üzerindeki switch nesnesinin değerine göre akış kolunun visible özelliğinin ayarlanması

```
var result = ServiceAPI.FormManager.Create("ProjectName", "FormName", Convert.ToInt64(Document1.FormInstance.Controls["ID"].Value.ToString())).Result; 
  if (result.Controls["SwitchName"].Value.ToString().ToLower() == "true") { 
  NoLongerRiskAssessors.Events.FirstOrDefault(x => x.Id == 21).Visible = false; 
 } 
 else { 
 NoLongerRiskAssessors.Events.FirstOrDefault(x => x.Id == 25).Visible = false; } 
 
```

