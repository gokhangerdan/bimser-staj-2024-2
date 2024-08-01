# DateRangePicker Nesnesinde tarih kontrolü

DateRangePicker nesnesinde seçilen tarih aralığını DateTimePicker nesnesinde kontrol etme.

```
async DateTimePicker1_OnValueChanged(args: Controls.EventArgs.IPropertyChangedEventArgs<Date>) { 
        let selectedDate = new Date(this.DateTimePicker1.value);
   let firstvalue = new Date(this.DateRangePicker1.value[0]);
  let secondvalue = new Date(this.DateRangePicker1.value[1]);
    if (!(selectedDate >= firstvalue && selectedDate <= secondvalue)) {
            this.showToaster("Hata", "Seçilen tarih, belirtilen aralığın dışında.", "Warning");
            this.DateTimePicker1.value = null;
        }
}
```

