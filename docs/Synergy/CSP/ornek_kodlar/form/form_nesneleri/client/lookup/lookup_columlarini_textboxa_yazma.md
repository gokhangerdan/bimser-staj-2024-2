# Lookup Columnlarını Textbox'a Yazma

Lookup Columnlarını Textbox'a Yazma işlemini Client(ts) tarafında Lookup OnBeforeSave eventinde yapabilirsiniz. 
Örnek olarak Lookup Display Expressionda NAME,MUSTERINO,VERGINO,VERGIDAIRESI bulunmaktadır. Display Format  ise {{ NAME }}|{{ MUSTERINO }}|{{ VERGINO }}|{{ VERGIDAIRESI }} şeklinde revizse edilmiştir. 
Örnek kullanım aşağıdaki gibidir.

		async lkpMusteri_OnValueChanged(args: Controls.EventArgs.IPropertyChangedEventArgs<any[]>) {
	       await this.applyChanges();
	        var str = this.lkpMusteri.text;
	        if(str.indexOf("|")!=-1)
	        {
	            var res=str.split("|");
	            this.lkpMusteri.text = res[0].trim();//Müşteri
	            this.txtMusteriKodu.text = res[1].trim();//Müşteri No
	            this.txtVergiNo.text = res[2].trim();//Vergi No 
	            this.txtVergiDairesi.text = res[3].trim();//Vergi Dairesi 
		    }
	    }