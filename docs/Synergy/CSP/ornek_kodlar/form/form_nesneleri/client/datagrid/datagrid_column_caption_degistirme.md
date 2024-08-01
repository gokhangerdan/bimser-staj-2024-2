# DataGrid Column Caption Değiştirme

```
async Button1_OnClick(args: Controls.EventArgs.IClickEventArgs) {
        this.DataGrid1.columns[0].caption["tr-TR"] = "test1";
        this.DataGrid1.columns[1].caption["tr-TR"] = "test2";
 
        this.DataGrid1.getColumns(); //bu satrin da eklenmesi gerekmekte
}

```

