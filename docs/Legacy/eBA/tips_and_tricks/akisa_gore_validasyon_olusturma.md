# Akışa Göre Validasyon Oluşturma

(Ad isimli metin kutusunun akışa göre zorunluluğunun değişmesi.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/p1-b00618fa-7820-469c-ae49-7fce818d6db3.png)

Kontrol isimli bir metin kutusu oluşturun ve visible seçeneğini false yapın. (İsmi değişebilir)
Form üzerine sağ tıklayarak View Validation Code seçeneğine tıklayın.



![](https://docsbimser.blob.core.windows.net/imagecontainer/p2-fae63de1-ee77-4700-b391-3360bddc0a86.png)

Açılan kod penceresini aşağıdaki gibi doldurun.

if(String.IsNullOrEmpty(Kontrol) && String.IsNullOrEmpty(Ad)){
                summary.AddMessage("Ad alanı boş bırakılamaz!");
}



![](https://docsbimser.blob.core.windows.net/imagecontainer/p3-917da312-421d-4965-96ae-0ebb974e60b8.png)

Akış tarafında revize istenen adıma bir fonksiyon ekleyin.

![](https://docsbimser.blob.core.windows.net/imagecontainer/p4-5305113e-64a0-4561-9039-4c3adddb964d.png)

Fonsiyonun içeriğini aşağıdaki gibi doldurun.

public void FlowScript1_Execute()
{
eBAForm frm = new eBAForm(Document1.ProfileId); 
frm.Fields["Text1"].AsString = "Revize";
frm.Update();	 
}



![](https://docsbimser.blob.core.windows.net/imagecontainer/p5-dd836a7c-afd4-4dcd-8937-187511f56429.png)

Bu şekilde akışta revize istenen bir işlemden sonra bazı alanların zorunluluğunu kaldırabilirsiniz.

