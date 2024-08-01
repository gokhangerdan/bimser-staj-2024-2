# Ana akışın formundaki detaylar nesnesindeki verileri Alt akışın ana formundaki detaylar nesnesine aktarma

Bir alt süreç başlatıldığında alt sürecin bir formunda bulunan detaylar nesnesine ana akıştaki formda bulunan detaylardaki veriler aktarılmak isteniyorsa bu işlem alttaki kod uyarlanarak sağlanabilir.

```Proje referanslarına 
%SystemPath%\Common\eBAPI.dll
%SystemPath%\Common\eBAIntegrationAPI.dll


using eBAPI.Connection;
using eBAPI.Workflow;


eBAConnection con = CreateServerConnection();
con.Open();
eBAForm frm = new eBAForm(Document1.ProfileId); //Alt akışın formunun id'si
eBAForm anafrm = new eBAForm(vrbAnaFormId.Value); //Ana akışın formunun id'si
FormDetails dtl = frm.Details["YeniTedarikciTanimlamaTablosu"]; // Alt akışın formdaki detayların adı
FormDetails dtlAna = anafrm.Details["YeniTedarikciTanimlamaTablosu"]; // Ana akışın formdaki detayların adı

try
{
    foreach foreach(FormDetailsRow fdr in dtlAna.Rows) //Ana akışın formundaki detaylar
    {
        WorkflowManager mng = con.WorkflowManager;
        eBAForm dtlForm = fdr.Form; // Ana akışın formundaki detayların satırlarında gezinirken üzerinde bulunduğumuz satıra ait modal form.
        WorkflowDocument doc = mng.CreateDocument("ParametreFormlari", "Form1");// ilk parametre proje ismi, ikinci parametre ise detaylara bağlı olan modal form ismi
        eBAForm modalForm = new eBAForm(doc.DocumentId);
        modalForm.Fields["supplier_Unvan"].AsString = dtlForm.Fields["Unvan"].AsString;
        modalForm.Fields["supplier_vkn"].AsString = dtlForm.Fields["VKN"].AsString;
        modalForm.Update();
        dtl.Rows.Add(doc.DocumentId);
    } //Alt akışın detaylarının içindeki detaylar nesnesi içinde bu kodu uyarlayarak yazmanız gerekecek


}
catch (Exception e)
{
    throw new Exception(e.ToString());
}
finally
{
    frm.Update();
    con.Close();
}```

