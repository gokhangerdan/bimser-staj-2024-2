# DataGrid Elemanlarını Toplu Silme

DataGrid'in client(ts) tarafında OnToolbarButtonClick eventinde aşağıda bulunan kod ile elemanların hepsini toplu şekilde  silebilirsiniz. Değişken olarak gridin ismini ve primary key'in verilmesi gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/tumunusil-6d5a8389-df5f-4790-8ec0-cad81cd67727.png)

```
deleteItemInRow = async (gridName: string, docId: any) => {
                //@ts-ignore
                const grid = this[gridName];
                let documentId: number;

                if (grid.rows.length > 0) {
                        const filteredRows: Array<any> = grid.selectedRowsData.filter((item: any) => {
                                return documentId = docId;
                        });
                        filteredRows.forEach((item) => {
                                this.applyChanges().then(() => {
                                        let row: any = {
                                                key: documentId,
                                                type: "remove",
                                                data: {}
                                        }
                                        grid.rowChangeAction(row);
                                });
                        });
                        grid.selectedRowKeys = [];
                        grid.selectedRowsData = [];
                        grid.reload(true);
                }
        }
```

Daha sonrasında bu fonksiyonu OnToolbarButtonClick eventinde çağırıyoruz.

```
const grid = this["DataGrid1"];
if (grid.rows.length > 0) {
                grid.selectedRowsData.forEach((item) => {
                                                this.deleteItemInRow("DataGrid1", item.DOCUMENTID); 
                                       
                });
 }
```

