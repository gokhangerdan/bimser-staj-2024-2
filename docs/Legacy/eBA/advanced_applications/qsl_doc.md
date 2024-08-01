# Query String Login Web Service

![](https://docsbimser.blob.core.windows.net/imagecontainer/QSL-54194f1c-627c-4ada-827b-bb88a3fdcea9.png)

## Web Referans Ekleme

“http://localhost/eba.net/ws/querystringlogin.asmx” adresindeki web servisini referans olarak projenize ekleyiniz. Tabi buradaki localhost kısmına eba sunucusuna erişmenizi sağlayacak bir ip yada makine adı vermeniz gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/qslws-3b9d19ac-4002-47f0-842a-f0da0388205f.png)

## Parametresiz Giriş

```public void GetQSLMethod()   //parametresiz eba giriş linki oluşturuyor.
        {
            string serverName = "localhost";

            #region
            //istenirse bağlanılacak sunucunun adı değiştirilebilir
            qslins.Url = "http://" + serverName + "/eba.net/ws/querystringlogin.asmx";
            qslins.UseDefaultCredentials = true;
            #endregion

            textBox1.Text = qslins.GetQueryStringLogin(username, password, logonuser);

        }```

```// Kullanıcının userid değerini döndürür.
 public void GetExternalUserIdMethod()
        {
            textBox1.Text = "External User Id:" + "\t " + qslins.GetExternalUserId(username, password, logonuser);
        }

        public void GetInternalUserIdMethod()
        {
            textBox1.Text = "Internal User Id:" + "\t " + qslins.GetInternalUserId(username, password, logonuser);
        }
```

## Parametre ile yapılan işlemler

Web servisi kullanılarak, belli bir dokümanı açmak, belli bir ekrana konumlanmak gibi daha özel işlemler de yapılabilir. Bunun için
“QueryStringLoginParameters” sınıfını kullanarak web servisine belirli parametreleri göndermek gerekmektedir. Aşağıdaki örnekte bu parametrelerin ne şekilde kullanılabileceği gösterilmiştir.
 
using eBAQueryStringLoginWebService;


string serverName = "";

string userName = "";

string position = "";

string password = "";

string logonUser = "";//hangi kullanıcı adına giriş yapılacak

//Parametre bilgileri

bool showLeftMenu = true;   //soldaki menü gözüksün mü

bool showTopBar = true;     //üst kısımdaki menü gözüksün mü?

string activePosition = ""; //birden fazla pozisyon varsa

string action = "";         //yapılacak işlem

string processFilter = "";  //process adına göre filtre


 
Action Parametresine göre çeşitli işlemler yapılabilir. Bu parametre için verilecek değere göre yapılacak işlemler aşağıda açıklanmıştır.
 
5.1 [StartupPage]
Ana ekranı gösteren bir url döndürür.
 
5.2 [Approvals]
Kullanıcının onayında bekleyen akışları gösterir.
 
5.3 [Notifications]
Kullanıcı için yapılan bilgilendirmeler gösterilir.
 
5.4 [Sents]
Kullanıcının gönderdiği belgeler.
 
5.5 [Drafts]
Kullanıcının taslaklarında bekleyen belgeler.
 
5.6 [History]
Yapılmış olan işlemlerin tarhiçesini gösterir.
 
5.7 [Process] [processId][canEdit?]
İstenilen bir akışın gösterilmesi için Action parametresi akış numarasını (LIVEFLOWS tablosundaki ID alanı) ve akışta değişiklik yapılıp yapılamayacağını bilgisi (true\false olarak) verilir.Daha sonra url aşağıdaki gibi alınabilir.


```  public void GetQSLWithParameterMethod()  //parametreli eba giriş linki oluşturuyor. 
        {
            bool linkokey = true;
            string canedit = "false";
            string ineditmode = "false";

            int surecid = 0, requestid = 0;

            string path = "";

            string menuitemkey = "";


            if (!string.IsNullOrEmpty(processno.Text))
            {
                surecid = Convert.ToInt32(processno.Text);
            }
            if (!string.IsNullOrEmpty(requestno.Text))
            {
                requestid = Convert.ToInt32(requestno.Text);
            }

            if (this.canedit.Checked)
            {
                canedit = "true";
            }
            if (this.ineditmode.Checked)
            {
                ineditmode = "true";
            }

            if (!string.IsNullOrEmpty(docpath.Text))
            {
                path = docpath.Text;
            }

            if (!string.IsNullOrEmpty(itemkey.Text))
            {
                menuitemkey = itemkey.Text;
            }


            QueryStringLoginParameters qslparametre = new QueryStringLoginParameters();

            qslparametre.ClickCount = 10; // linke 10 kez tıklanma sınırı ekler   
            qslparametre.LeftMenuVisible = true;  // sol taraftaki menüyü kapatıyor
            qslparametre.TopBarVisible = true; // üst taraftaki barı kapatıyor.


            // qslparametre.ActivePosition = "PG0001"; //AD00002 // birden fazla pozisyon mevcutsa

            // qslparametre.ProcessFilter = "TESTPROCESS"; //process adına göre filtre

            // qslparametre.Parameters = ""; // gerekli alanlar için parametre verilir. 


            // ACTION ile yapılabilecekler.
            #region

            /*
            Action Parametresine göre çeşitli işlemler yapılabilir. Bu parametre için verilecek değere göre yapılacak işlemler aşağıda açıklanmıştır.

            [Applications][itemKey] -- Menü üzerindeki bir butona basılmış gibi işlem yaptırmak istersek aşağıdaki yöntemi kullanabiliriz.
            * Bunun için kullanmak istediğimiz süreci menu yöneticisinden “Item Key” atanması gerekiyor.
            * 
            ...
             qslparametre.Action = "[Applications][" + MenuItemKey + "]";
            ...

            [StartupPage]   --  Ana ekranı gösteren bir url döndürür.
            
            [Approvals]     --  Kullanıcının onayında bekleyen akışları gösterir.         

            [Notifications] --  Kullanıcı için yapılan bilgilendirmeler gösterilir.
            
            [Sents]         --  Kullanıcının gönderdiği belgeler.

            [Drafts]        --  Kullanıcının taslaklarında bekleyen belgeler.

            [History]       -- Yapılmış olan işlemlerin tarhiçesini gösterir.
            
            [Process][processId][canEdit ?] --  İstenilen bir akışın gösterilmesi için Action parametresi processid(LIVEFLOWS ID) ve akışta değişiklik yapılıp yapılamayacağını bilgisi(true\false olarak) verilir.
            ...
                    qslparametre.Action = "[Process][1678][false]";  
            ...

            [ProcessRequest][processId][requestId] -- Bu yöntemle akışı akış üzerindeki bir kişinin yetkileri ile açabiliriz. processID akış numarasını requestId FLOWREQUESTS tablosundaki ID alanının belirtmektedir.
            ...
                   qslparametre.Action = "[ProcessRequest][1678][3]";       
            ...

            [DocumentFromPath][Path][canEdit?][inEditMode?]  -- İstenilen bir eBA formunu direkt olarak açmaya yarar. eBA Fromları için yol(path) bilgisi workflow/projeAdi/formAdi/formID.wfd formatında belirtilir.            
                Diğer iki alan ise true\false değerleri alırlar. ilk alan editlenebilir mi?, diğeriyse belgenin değiştirme modunda (“Deşiklik Yap” butonuna basılmış gibi) açılıp açılmayacağını gösterir.
            ...
            qslparametre.Action = "[DocumentFromPath][workflow/deneme/Form/145.wfd][true][true]";       
            ...

            [DocumentExplorer] -- Doküman gezginini açar. / path verilmesi gerekir.

            [Delegations] -- Vekalet vermek için kullanılan ekranı açar.

            [UserSettings.ChangePassword] -- Şifre değişitirme ekranını açar.

            [Help] -- Yardım dokümanlarının olduğu kısmı açar.

            [DocumentProperties]  -- Dokümanın veya dizinin özelliklerini açar. Kullanıcının yetkisi dahilinde doküman veya dizin güvenlik yetki ayarları ve içerik ayarlarının düzenlendiği sekmelerde gelir.

             ...
            qslparametre.Action = "[DocumentProperties]";
            qslparametre.Parameters = "system/images/explorer/objects/folder.gif"; 
             ...

            */
            #endregion


            if (QSL_Param.Checked)
            {
                if (Application.Checked)
                {

                    if (!string.IsNullOrEmpty(menuitemkey))
                    {
                        qslparametre.Action = "[Applications][" + menuitemkey + "]";
                    }
                    else
                    {
                        MessageBox.Show("Bu işlem için Menü item key gerekmektedir.");
                    }
                }
                else if (StartupPage.Checked)
                {
                    qslparametre.Action = "[StartupPage]";

                }
                else if (Approvals.Checked)
                {
                    qslparametre.Action = "[Approvals]";
                }
                else if (Notifications.Checked)
                {
                    qslparametre.Action = "[Notifications]";
                }
                else if (Sents.Checked)
                {
                    qslparametre.Action = "[Sents]";
                }
                else if (Drafts.Checked)
                {
                    qslparametre.Action = "[Drafts]";
                }
                else if (Help.Checked)
                {
                    qslparametre.Action = "[Help]";
                }
                else if (Delegations.Checked)
                {
                    qslparametre.Action = "[Delegations]";
                }
                else if (History.Checked)
                {
                    // Menuitemkey vererek ilgili sürecin geçmişi draftı vs. açılabilir.

                    if (ekle.Checked)
                    {
                        qslparametre.Action = "[History][" + menuitemkey + "]";
                    }
                    else
                    {
                        qslparametre.Action = "[History]";
                    }
                }
                else if (changepassword.Checked)
                {
                    //  Şifre değişme kısmı gelmiyor.
                    qslparametre.Action = "[UserSettings.ChangePassword]";
                }
                else if (ProcessRequest.Checked)
                {
                    // yetkisi olmayanlar için süreçi gösterme linki oluşturur.
                    if (!string.IsNullOrEmpty(processno.Text) && !string.IsNullOrEmpty(requestno.Text))
                    {
                        qslparametre.Action = "[ProcessRequest]" + "[" + surecid + "]" + "[" + requestid + "]";
                    }
                    else
                    {
                        linkokey = false;
                        MessageBox.Show("Süreç İd ve request Id dolu olmalıdır.");
                    }

                }
                else if (Process.Checked)
                {
                    qslparametre.Action = "[Process]" + "[" + surecid + "]" + "[" + canedit + "]";
                }
                else if (DocProperty.Checked)
                {
                    if (!string.IsNullOrEmpty(docpath.Text))
                    {
                        qslparametre.Action = "[DocumentProperties]";
                        qslparametre.Parameters = path;
                        // qslparametre.Parameters = "system/document templates/samplepdf.pdf";
                    }
                    else
                    {
                        MessageBox.Show("Path Girilmelidir.!");
                        linkokey = false;
                    }
                }
                else if (DocExplorer.Checked)
                {
                    if (!string.IsNullOrEmpty(docpath.Text))
                    {
                        qslparametre.Action = "[DocumentExplorer]" + "[" + path + "]";
                    }
                    else
                    {
                        MessageBox.Show("Path Girilmelidir.!");
                        linkokey = false;
                    }

                }
                else if (DocFromPath.Checked)
                {
                    if (!string.IsNullOrEmpty(docpath.Text))
                    {
                        qslparametre.Action = "[DocumentFromPath]" + "[" + path + "]" + "[" + canedit + "]" + "[" + ineditmode + "]";
                        //[workflow/BytePdf/Form/1343.wfd]
                    }
                    else
                    {
                        MessageBox.Show("Path Girilmelidir.!");
                        linkokey = false;
                    }

                }
                else
                {
                    MessageBox.Show("Action Şeçilmedilir.");
                }

                if (linkokey)
                {
                    LinkArea.Text = qslins.GetQueryStringLoginWithParameters(username, password, logonuser, qslparametre);
                }
                else
                {
                    MessageBox.Show("Gerekli alanları doldurunuz!");
                }

            }

        }```

