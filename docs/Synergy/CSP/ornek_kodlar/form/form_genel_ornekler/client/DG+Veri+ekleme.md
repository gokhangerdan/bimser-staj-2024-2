# Kod ile DataGrid'e Veri Ekleme (Client)

```
Button1_OnClick(args: Controls.EventArgs.IClickEventArgs) {
    var row1 = this.DataGrid1.newRow();
    row1.cells[0].text = 'column1Text';
    row1.cells[0].value = 'column1Value';
    row1.cells[1].text = 'column2Text';
    row1.cells[1].value = 'column2Value';
    this.DataGrid1.rows.push(row1);
}
```
