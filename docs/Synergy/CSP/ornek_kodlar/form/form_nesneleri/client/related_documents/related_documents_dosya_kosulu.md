# RelatedDocuments Dosya Koşulu

RelatedDocuments Dosya Koşulunu Client(ts) tarafında Datagrid OnBeforeSave eventinde yapabilirsiniz. Örnek kullanım aşağıdaki gibidir.

	async Form1_OnBeforeSave(args: Controls.EventArgs.IBeforeSaveEventArgs) {
	        if(this.RelatedDocuments1.files.length == 0)
	        {
	        this.showMessage("Uyarı!","İzin Taahhütnamesinin yüklenmesi zorunludur!..","Warning");
	        args.cancel = true;   
	        }
	}