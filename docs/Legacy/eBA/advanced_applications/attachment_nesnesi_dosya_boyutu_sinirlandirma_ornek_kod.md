# Attachment Nesnesi -Dosya Boyutu Sınırlandırma Örnek Kod


Dosyalar nesnesi dosya boyutu kontrol
```

using eBAPI.Connection;

using eBAPI.DocumentManagement;

//eklenmeli

 

//nesnenin onafterattach eventinde formdaki örn. txtDosyaBoyutu isimli metin kutusuna MB cinsinden değer yazılır.

public void Dosyalar1_OnAfterAttach(object sender, eBAAttachmentFileEventArgs e)

                               {

                                 txtDosyaBoyutu.Text = (dosyaBoyutu()/(1024 * 1024)).ToString();      

                               }

                              

//ilgili method

                               public long dosyaBoyutu()

        {

              eBAConnection eBACon = CreateServerConnection();

              eBACon.Open();

             

              try

              {     

               

                  FileSystem fs = eBACon.FileSystem;  

                  DMFile fileExcel = fs.GetFile("workflow/Proje1/Form/" + id.ToString()  + ".wfd");

                 

                  DMCategoryContentCollection SourceAttachments = fileExcel.GetAttachments("default");                  

               

                  DMFileContent fl = SourceAttachments[0];

                 

                  return fl.Size;

              }                                

            finally

            {

                eBACon.Close();

            }

        }

 

//formun validasyon kod tarafında

if(txtDosyaBoyutu > 10)

                     summary.AddMessage("Dosya Boyutu 10MB den Büyük Olamaz.");
```

