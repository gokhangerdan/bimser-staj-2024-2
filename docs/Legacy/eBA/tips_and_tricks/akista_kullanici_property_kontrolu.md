# Akışta Kullanıcı Property Kontrolü

Proje üzerine sağ tıklayıp proje özelliklerini açın.


![](https://docsbimser.blob.core.windows.net/imagecontainer/p1-8d1c5cb4-6835-4330-8601-f1c0118bf154.png)

Referans Dosyalar sekmesine aşağıdaki referansları ekleyin ve akışın kod kısmında eBADBHelper’ı kullanıma ekleyin.

%SystemPath%\Common\eBADBHelper.dll
%SystemPath%\Common\eBAOrganization.dll
%SystemPath%\Common\eBASerialization.dll


using eBADBHelper;

![](https://docsbimser.blob.core.windows.net/imagecontainer/p2-b0e150b6-df17-4729-99f9-ab2d81e96ab1.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/p3-8e5dbfdc-b104-4141-866e-ffde7cc98cd3.png)

Akışa bir tane değişken ve bir tanede fonksiyon nesnesi ekleyin.

![](https://docsbimser.blob.core.windows.net/imagecontainer/p4-2f293e60-6f6e-4674-b835-1b29c405878e.png)

Fonksiyonun execute metoduna aşağıdaki kodu yazın

```
public void Fonksiyon1_Execute()
{
    eBAOrganization.Organization org = new eBAOrganization.Organization();
    Sube.Value = org.GetOsParameter(eBAOrganization.OrganizationObjectType.User,KarsilastirilacakPozisyon.User,"SUBEKODU"); 
}

```

Akışa eklediğiniz karşılaştırma nesnesi ile değişkeninizi karşılaştırarak akışınız yönlendirin.

![](https://docsbimser.blob.core.windows.net/imagecontainer/p5-37c2e96f-183a-417c-ac87-9879b47be665.png)

