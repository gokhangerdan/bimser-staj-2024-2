# StartWorkflowWithDocument

Postman üzerinden StartWorkflowWithDocument  ile iletmiş olduğumuz endpointe istek atarak, akış tetiklettirebilmekteyiz. Sizler için örnek olarak cspdestek ortamımızda, HBA_01 projesini Flow1 akışı ile başlatmaktayız. 

StartWorkflowWithDocument işlemleri:
1) https://................ DNS ADRESİ .................... /apis/projects/............. PROJE ADI ..................../workflows/............. FLOW ADI ..................../StartWorkflowWithDocument
2) Authorization bölümüne bearer tokenı girilmelidir. (3)
3) Headers alanına Bimser-Encrypted-Data ve Bimser-Language ve Bimser-FootPrint  keyleri eklenerek value değerleri yazılır. (2)
4) Aşağıda iletmiş olduğum Body kısmını girmelisiniz. (4)

{
  "documentName": "Document1",  
  "documentData": {
    "secretKey": "string",
    "controlValues": {                                          //Projedeki nesnelerin valueleri set edilir. Bizim projemizde TextBox1 ve TextBox2 nesnesi bulunmaktadır.
      "TextBox1": "D613B166",
      "TextBox2": "LBA0960137"
    }
  },
  "eventId": 4                                                    // Proje akışında akış başlangıcı nesnesinin gönder eventinin Identity'si 4tür.  Bu yüzden eventId'ye 4 yazılmıştır.
}

Not: bearer tokenını ve headers alanına girilecek key value değerlerini csp sayfasına giriş yaptıktan sonra f12'den alabilirsiniz. Network --> GetUserDetail 'dan alabilirsiniz.

5) Bu işlemleri bitirdikten sonra isteği gönderebilirsiniz.  Result kısmından istek kontrol edilmelidir. (1) CSP üzerinden de akışın ilerlediğini, ve pozisyon nesnesine geldiğini görmekteyiz.(5)

![](https://docsbimser.blob.core.windows.net/imagecontainer/s1-668f54bc-a650-4aea-a176-48462e165f0a.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/s2-71ad3a38-ee90-42d9-9cce-15c7c91b0980.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/s3-fd47a882-b219-40a9-bdd2-e7f3ed4472cf.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/s4-8b4ad897-8161-4bfc-a35d-fbee115fc945.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/s5-94cbffba-9b78-4667-9adc-3551cd746bdd.png)

