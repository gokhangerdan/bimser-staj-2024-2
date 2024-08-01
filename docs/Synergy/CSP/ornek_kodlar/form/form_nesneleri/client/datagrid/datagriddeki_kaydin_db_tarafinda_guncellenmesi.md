# DataGrid Üzerinde İşlem Yapılan Kaydın DB Tarafında Güncellenmesi

```
export default class Form1 extends Form.Designer {
    async DataGrid1_OnRowUpdated(args: Controls.EventArgs.IRowUpdatedEventArgs) {
        this.fetch.post("DataSource/test", { 'DocumentId': args.newRow.DOCUMENTID }).then(result => { this.DataGrid1.reload(true); });
        console.log(args.newRow.DOCUMENTID);

    }
}


```

DATASOURCE/test tarafı:

UPDATE E_testbimsers_Form1 SET DateTimePicker1=GETDATE() WHERE DOCUMENTID={{DocumentId}}


