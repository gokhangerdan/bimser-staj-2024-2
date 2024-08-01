# Form Üzerinde Limit Kontrolü

Kod kısmına gelmeden önce proje üzerine sağ tıklayarak proje özelliklerini açın ve aşağıdaki dll leri sisteme ekleyin.


```
%SystemPath%\Common\eBAPI.dll
%SystemPath%\Common\eBAIntegrationAPI.dll
```

![](https://docsbimser.blob.core.windows.net/imagecontainer/src1-be6c3c60-bd0a-49bd-87f0-0632193724a7.png)

Form üzerine sağ tıklayarak ‘View Server Code’ seçeneğine tıklayın. Forma aşağıdaki referansları ekleyin.


```
using eBAPI;
using eBAPI.Connection;
using eBAIntegrationAPI;
using System.Data;
using System.Collections.Generic;
```

Kod Tarafına aşağıdaki fonksiyonu ekleyin.


```
DataTable IntegrationQuery(string Baglanti,string Sorgu,Dictionary<string,string> Parametreler)
{
eBAConnection con = CreateServerConnection();
con.Open();
eBAIntegrationQuery qry= new eBAIntegrationQuery(Baglanti, Sorgu);
foreach(KeyValuePair<string,string> veri in Parametreler)
{
qry.Parameters.Add(veri.Key, veri.Value);
}
DataTable dt = qry.Execute(con);
return dt;
}
Formun OnLoadData metoduna çift tıklayarak ağaıdaki gibi doldurun. Bu şekilde kalan bakiyenizi Fiyat kontrol nesnesinme atamış bulunmaktayız. Sorgunuz parametre alacaksa new Dictionary<string,string> {} alanını . new Dictionary<string,string> { {"Param1", “Value1”}, {"Param2", “Value2”}, {"Param3", “Value3”}} şeklinde parametre adı ve değeri şeklinde doldurun.
public void OnLoadData()
{
DataTable dt = IntegrationQuery("BağlatıAdı","SorguAdı",new Dictionary<string,string> {});
if (dt != null && dt.Rows != null && dt.Rows.Count > 0 && dt.Rows[0].ItemArray.Length > 0)
{
FiyatKontrol.Text = dt.Rows[0].ItemArray[0].ToString();
}
}
```

Formun OnLoadData metoduna çift tıklayarak aşağıdaki gibi doldurun. 
Bu şekilde kalan bakiyenizi Fiyat kontrol nesnesinme atamış bulunmaktayız. 
Sorgunuz parametre alacaksa  
Dictionary<string,string> {} alanını . new Dictionary<string,string> { {"Param1", “Value1”}, {"Param2", “Value2”}, {"Param3", “Value3”}} şeklinde parametre adı ve değeri şeklinde doldurun.

```
public void OnLoadData()
{
DataTable dt = IntegrationQuery("BağlatıAdı","SorguAdı",new Dictionary<string,string> {});
if (dt != null && dt.Rows != null && dt.Rows.Count > 0 && dt.Rows[0].ItemArray.Length > 0)
{
FiyatKontrol.Text = dt.Rows[0].ItemArray[0].ToString();
}
}
```

![](https://docsbimser.blob.core.windows.net/imagecontainer/src2-10fd2905-3f04-462e-9d11-3bf7a9b88d5c.png)

Form üzerine sağ tıklayın ve açılan menüde ‘View Validation Code’ seçeneğini tıklayın. Açılan Kod ekranındaki OnValidateDocument metodunu aşağıdaki gibi doldurun. Bu şekikde limit kontrolü sağlanacaktır ve uyarı olarak kalan limit mesajı verilecektir.


```
public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary)
{
// TahminiFiyat nesnenin ismidir. TahminiFiyat.Text şeklinde kullanmayınız.
if(Convert.ToDouble(TahminiFiyat) > Convert.ToDouble(FiyatKontrol))
{
summary.AddMessage("Bu ayki kalan limit "+FiyatKontrol.ToString()+” TL dir. ”);
}
}
```

