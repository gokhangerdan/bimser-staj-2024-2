# DataGrid Satır Silme

```
async DataGrid2_OnRowRemoved(args: Controls.EventArgs.IRowRemovedEventArgs) 
   {
   let idToRemove: number = args.row.NewColumn1; // Silmek istediğiniz öğenin ID'si
   let row: any = { key: idToRemove, type: "remove" };
   this.DataGrid1.rowChangeAction(row);
   await this.applyChanges();
   }
```

