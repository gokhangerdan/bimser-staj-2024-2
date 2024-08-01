# DataGrid İçindeki Bir Elemanı Silme  (Client)

Bir datagrid içindeki bir elemanı silme işleminin nasıl gerçekleştirileceğini deleteItem fonksiyonunun nasıl kullanıldığını ve context menüdeki onItemClick olayı ile nasıl ilişkilendirildiğini gösteriliyor.

### Kullanım Şekli

Aşağıdaki kod, deleteItem fonksiyonunu kullanarak bir data grid içindeki elemanı silmek için context menüdeki onItemClick olayını nasıl kullanacağınızı gösterir.

```
async ctxMenu_OnItemClick(args: Controls.EventArgs.IContextMenuItemClickEventArgs) { 
        if (args.baseArgs.data.key === "Delete") {
            this.deleteItem(args, "Delete_ItemInMenu", this.DataGrid);
        }
}
```

