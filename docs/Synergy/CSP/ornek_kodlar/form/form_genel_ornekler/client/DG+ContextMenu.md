# Context menü ile DataGrid boolen column verisini değiştirme (Client)

```
async ContextMenu_OnItemClick(args: Controls.EventArgs.IContextMenuItemClickEventArgs) {    
	let stat = {	    
		'ButtonTestOk': true,	    
		'ButtonTestReject': false	    
	};    
	let currentKey = args.baseArgs.data.key;  
	let rowIndex = args.targetArgs.rowIndex;  
	this.dtgTest.rows[rowIndex].cells.find(cell => cell.name == 'Statu').value = stat[currentKey];
}
```
