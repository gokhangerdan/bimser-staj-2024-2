# Datagrid'de SetCellValue eventi ile hücreye değer atama

```   //Datagrid nesnesine SetCellValue eventi ile hangi column da işlem yapıldı ve değer dolu mu kontrolü yapıldı.
   //Datagrid nesnesinde COLUMN_2 deki hücreye değer ataması yapıldı.
 
     async Datagrid1_SetCellValue(args: Controls.EventArgs.ISetCellValueChangeEventArgs) {
       
        if (args.columnName == 'COLUMN_1' && args.value != null ) {
                 args.newData["COLUMN_2"] = "COLUMN_1 kolonunda ki veri değiştirildi.";
       }```

