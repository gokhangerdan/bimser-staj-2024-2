# DataGrid Çift Tıklama ile Row Değeri Değiştirme (Client)

```
async DataGrid1_OnRowDoubleClick(args: Controls.EventArgs.IRowDoubleClickEventArgs) {
    this.DataGrid1.rows.find(row => row.cells.find(cell => cell.name == 'Code' && cell.value == args.row.Code)).cells.find(cell => cell.name == 'Statu').value = 1 - args.row.Statu;
}
```
