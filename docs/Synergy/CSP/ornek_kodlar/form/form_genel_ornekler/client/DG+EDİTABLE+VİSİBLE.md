# DATAGRİD AKIŞ KULLANICISINA GÖRE COLUMN EDITABLE - VİSİBLE (Client)

```
async DataGrid1_OnEditingStart(args: Controls.EventArgs.IEditingStartEventArgs) {

	if (this.responseParameters.workflowInfo.currentStep.name != 'Position1') {
	
		this.DataGrid1.columns.find(col => col.name == 'test1').visible = false; // görünürlük kapanır
	
	}
	
	else if (this.responseParameters.workflowInfo.currentStep.name != 'Position2') {
	
		this.DataGrid1.columns.find(col => col.name == 'test2').editingEnabled = false; // Editleme açılır
	
	} 
}
```

**YOL 2**

```
async DataGrid1_OnEditingStart(args: Controls.EventArgs.IEditingStartEventArgs) {
	this.DataGrid1.columns[3].editingEnabled=false; // Editleme kapalır
}
```
