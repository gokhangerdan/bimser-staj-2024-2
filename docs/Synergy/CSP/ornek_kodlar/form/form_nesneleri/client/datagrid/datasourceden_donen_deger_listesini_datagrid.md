# DataSource'den Dönen Değer Listesini DataGrid'e Yazdırma

Eklemiş olduğumuz bir Datasource'dan dönen bilgileri Buton aracılığı ile DataGride'e aktardığımız kod bilgisi aşağıdadır. 


```
 async Button1_OnClick(args: Controls.EventArgs.IClickEventArgs) {
    var veri: any = await this.fetch.post("DataSource/test", {});
    let satirlar:any = [];
    veri.data.result.forEach(((soru: any) => {
      let satir = this.DataGrid1.newRow();
      satir.cells[0].text = String(soru.ID);
      satir.cells[0].value = soru.ID;
      satir.cells[1].text = soru.USERNAME;
      satir.cells[2].text = soru.FIRSTNAME;

	  satir.data = soru;

      satirlar.push(satir);
    }))
    this.DataGrid1.rows = satirlar;
  }

```

