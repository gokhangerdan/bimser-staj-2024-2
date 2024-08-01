# DataGrid OnEditingStart sadece belirli bir sütunu düzenlenebilir yapmak (Client)

Datagrid'in OnEditingStart olayı sırasında, sadece belirli bir sütunun düzenlenebilir olmasını ve diğer sütunların düzenlenemez olmasını sağlamak.

```
async dataGrid_OnEditingStart(args: Controls.EventArgs.IEditingStartEventArgs) {
    // Yalnızca 'PROCESSSTEP' isimli sütunu düzenlenebilir yap, diğerlerini düzenlenemez yap.
    this.dataGrid.columns.map(column => {
        column.editingEnabled = column.name === "PROCESSSTEP";
    });
}
```

