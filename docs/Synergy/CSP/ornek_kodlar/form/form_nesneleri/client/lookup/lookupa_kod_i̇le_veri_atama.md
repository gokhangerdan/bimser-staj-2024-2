# Lookup'a Kod İle Veri Atama

Datasource kullanılmadan kod ile Lookup nesnesine veri atılması için aşağıda örnek kod bulunmaktadır.

```
 void Button1_OnClick(object sender, MouseEventArgs e)
        {
            Lookup1.DataSource.ValueMember ="DGID";
            Lookup1.DataSource.DisplayMember = new List<string>(){"DGID"};
            Lookup1.DataSource.DisplayFormat ="{{DGID}}";  //GÖRÜNECEK KOLON İSTERSEN A DA YAPABİLİRSİN FARKETMEZ
              var dataGridRow =Lookup1.NewRow();
                dataGridRow.Cells[0].Value = 1;
                dataGridRow.Cells[0].Text = "1";
                dataGridRow.Cells[1].Text = "tset";
                dataGridRow.Cells[1].Value = "tset";
                Lookup1.Rows.Add(dataGridRow);
        }


```

![](https://docsbimser.blob.core.windows.net/imagecontainer/img1-dcc3019f-164e-4373-afcc-802100bafa72.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/img2-d577cf76-7837-47cd-b966-20bb16161602.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/img3-a31f6a31-99c1-4fe5-9fee-7d3513e82bee.png)

