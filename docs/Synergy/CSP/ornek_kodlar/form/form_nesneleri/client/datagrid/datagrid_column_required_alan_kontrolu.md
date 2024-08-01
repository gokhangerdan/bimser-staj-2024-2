# Datagrid Column Required Alan Kontrolü

Datagrid Column Required Alan Kontrolünü Client(ts) tarafında Datagrid OnRowInserting eventinde yapabilirsiniz. Örnek kullanım aşağıdaki gibidir.

	async DataGrid2_OnRowInserting(args: Controls.EventArgs.IRowInsertingEventArgs) {
	        var a = args;
	        if(args.row["NewColumn2"] == null){
	            this.showToaster("Boş Geçilemez!","Bu alanın doldurulması zorunludur.","Validation");
	            args.cancel = true;
	        }
	}