# DataGrid Mükerrer Kayıt Kontrolü (Client)

```
async Form1_OnBeforeSave(args: Controls.EventArgs.IBeforeSaveEventArgs) {     
	let test = this.dtgTest.rows.filter(row => row.cells.find(cell => cell.name == 'Statu' && cell.value != false));
	let EmptyYorumCount = test.filter(row => row.cells.find(cell => cell.name == 'Yorum' && cell.text == ''));  
	if (EmptyYorumCount.length > 0) {   
		let messages = {	    
			'tr-TR': "Yorum Yazmadan Testleri Tamamlayamazsın",	    
			'en-US': "Yorum Yazmadan Testleri Tamamlayamazsın"	    
		}	    	    		
		this.showToaster(captions[this.currentLanguage.culture], messages[this.currentLanguage.culture], "Warning");   
		args.cancel = true;
	}
}
```
