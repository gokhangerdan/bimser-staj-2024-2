# Datagrid Column Sum

DataGrid'in client(ts) tarafında OnSummaryChanged eventinde aşağıdaki iletilen kod ile numberbox'a column toplamını yazdırabilirsiniz.


	async dgDeneme_OnSummaryChanged(args: Controls.EventArgs.ISummaryChangedEventArgs) {
	        this.NumberBox1.value = args.value;      
	}