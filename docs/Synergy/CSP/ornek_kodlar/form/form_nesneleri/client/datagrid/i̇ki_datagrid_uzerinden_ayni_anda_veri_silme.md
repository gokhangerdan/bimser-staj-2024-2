# 2 DataGrid Üzerinden Aynı Anda Veri Silme

İhtiyaçlar doğrultusunda bir Form içerisindeki iki DataGrid'den aynı anda veri silme işlemi için yazdığımız kod ile bir DataGrid'den silinen veri diğer DataGrid'den de silinmiş olacaktır.

```
async DataGrid2_OnRowRemoved(args: Controls.EventArgs.IRowRemovedEventArgs) 
    {
    let idToRemove: number = args.row.NewColumn1; // Silmek istediğiniz öğenin ID'si
    let row: any = { key: idToRemove, type: "remove" };
    this.DataGrid1.rowChangeAction(row);
    await this.applyChanges();
    }

```

