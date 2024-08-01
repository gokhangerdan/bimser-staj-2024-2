# DataGrid DateTime Column Kontrolü

## DateTime tipli column üzerinden seçim yaparken, belirtilen koşula bağlı uyarı oluşturmak.

```

 async DataGrid2_SetCellValue(args: Controls.EventArgs.ISetCellValueChangeEventArgs) {
              
                if (new Date() < new Date(args.value)) {
                        this.showMessage("Uyarı", `${new Date(args.value)} tarihinden sonra seçim yapılamaz.`, "Warning")
                }
        }

```

