# İlişkili Dökümanlar Nesnesine Formdan Ek Ekleme

İlişkili dökümanlar nesnesiyle ,döküman yönetimi üzerinden seçilen dökümana. Form üzerindeki attachment nesnesine eklediğimiz dosyaları ek olarak eklemek için aşşağıdaki kod bloğunu detaylı olarak inceleyip ,
sisteminize göre revize edebilirsiniz


```%SystemPath%\Common\eBAPI.dll
using System;
using System.Collections;
using System.Text;
using System.Data;
using eBAControls;
using eBAControls.eBABaseForm;
using eBAFormData;
using eBAPI;
using eBAPI.Connection;
using eBAPI.DocumentManagement;
using System.IO;


namespace RelationsEkekleme
{

	public partial class Form
	{
		
		public void RelatedDocuments1_OnAfterRelation(object sender, eBARelationFileEventArgs e)
		{
		Text1.Text=e.Filename;       //İlişkili dökümanlar nesnesinin path bilgisine ulaşılır 
		}
		
		public void Ekekle_OnClick(Object sender, EventArgs e)
		{
			    eBAConnection con = CreateServerConnection();  
          try
          {
            con.Open();
            string fileNameRel=Text1.Text;//İlişkili dökümanlar nesnesinin pathi aktarılır
            DMFile form = con.FileSystem.GetFile(Filename);
            foreach (var item in form.GetAttachments("default")) //formdaki attachmentin içerisinde geziyoruz
              {
                 byte[] arr =con.FileSystem.DownloadFileAttachmentContentToByteArray(form.Path,"default",item.ContentName);  
                 DMFile relFilename = con.FileSystem.GetFile(fileNameRel);
                 con.FileSystem.UploadFileAttachmentContentFromByteArray(relFilename.Path,"default",item.ContentName,arr);    //Attachmetnin içerisinde bulduğumuz dosyaları,ilişkili dökümanların eklerine ekliyoruz
              }
          }
          finally
          {
            con.Close();
          }
		}


	}
}
```



