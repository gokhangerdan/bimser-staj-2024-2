# DataGrid'e Eklenecek Tekerrür Değeri Engellemek

DataGrid'in OnRowInserting olayında eklenmeye çalışılan TEXTVAL değerini, DataGrid içinde bulunan diğer TEXTVAL değerleriyle karşılaştırıyor ve aynı değerin bulunması halinde yeni satırın eklenmesini engelliyoruz.

```
async DataGrid1_OnRowInserting(args: Controls.EventArgs.IRowInsertingEventArgs) 
    {
        if (args.rows.find(i => i["TEXTVAL"] == args.row["TEXTVAL"])) {
            this.showMessage("Uyarı !", "Bu değere(" + args.row["TEXTVAL"] + ") sahip veri, tabloda var olduğu için eklenemez.", "Blocked");
            args.cancel = true;
        }
    }
```