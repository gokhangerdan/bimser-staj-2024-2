# Datagrid Satır Kontrolü

Datagrid Satır Kontrolünü Client(ts) tarafında Form OnBeforeSave eventinde yapabilirsiniz. Örnek kullanım aşağıdaki gibidir.

	if (this.datagrid1.row.length == 0)
	{
	        this.showToaster("UYARI!","Datagrid boş","Warning");
	        args.cancel = true;
	}