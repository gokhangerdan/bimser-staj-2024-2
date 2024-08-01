# DateTimePicker nesnesinden seçilen tarihe göre tarih ayarlama (Client)

    async  DateTimePicker1_OnValueChanged(args: Controls.EventArgs.IPropertyChangedEventArgs<Date>) {
    	var tarih = new  Date(this.DateTimePicker1.value);
    	tarih.setDate(tarih.getDate() + 365);
    	this.DateTimePicker2.value = tarih.toDateString();
    }

