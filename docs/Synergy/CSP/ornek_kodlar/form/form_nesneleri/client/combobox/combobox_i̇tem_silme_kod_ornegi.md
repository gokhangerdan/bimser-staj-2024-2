# Combobox İtem Silme Kod Örneği

Form cs tarafında bir Combobox nesnesinde item silmek isterseniz aşağıdaki kod örneğini projenize uyarlayabilirsiniz.

```
void Form1_OnLoad(object sender, LoadEventArgs e) 

        { 

            if (ComboBox1.Text != "18" || ComboBox1.Text != "8") 

            { 

                ComboBox1.Items.RemoveAll(ListItem => ListItem.Text["tr-TR"].EndsWith("8")); 

            } 

        } 
```

ComboBox nesnesinden, belirli koşullara uyan itemlar silinebilir. Belirli bir değeri içeren itemlar silinebilir.  

ComboBox1.Items.RemoveAll(ListItem => ListItem.Text["tr-TR"].Contains("test"));  

Belirli bir değer ile başlayan itemlar silinebilir.  

ComboBox1.Items.RemoveAll(ListItem => ListItem.Text["tr-TR"].StartsWith("te")); 

