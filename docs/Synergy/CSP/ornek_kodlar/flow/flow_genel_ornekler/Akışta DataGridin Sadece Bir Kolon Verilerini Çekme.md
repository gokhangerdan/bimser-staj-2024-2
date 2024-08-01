# Akışta DataGrid'in Sadece Bir Kolon Verilerini Çekme

```csharp
    using System.Collections;
    using System.Collections.Generic;

    public void Function1_Execute(object sender, OnExecuteEventArguments args)
    {
        List<object> approvalStatusList = Document1.GetDataGridCellValues("DataGrid1", "approvalStatus");
        LogExtension.Log("approvalStatusList.Count ->" + approvalStatusList.Count, args.Context);
    }
```
