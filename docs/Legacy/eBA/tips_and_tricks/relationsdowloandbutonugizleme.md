# Relations Dowloand Butonu Gizleme

İlişkili dökümanlar nesnesinde isteğe bağlı indirme butonunun gizlenmesi için örnek kod bloğu

```
	public void IliskiliDokumanlar1_OnBeforeRelation(object sender,eBAAddRelationFileEventArgs e)
		{
Etiket3.Text= @"<style>#fileView_ctl01_IliskiliDokumanlar1 > div > table > tbody > tr.tableHeader > td:nth-child(4) { display: none !important; } #fileView_ctl01_IliskiliDokumanlar1 > div > table > tbody > tr > td:nth-child(4) { display: none !important; }</style>";           
        
                }  
```

