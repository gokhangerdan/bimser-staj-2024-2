# eBA Form Custom CSS Kullanımı

İlgili eBA formunun kod tarafı açılır ve OnLoad metodu override edilir ve aşağıdaki şekilde doldurululur.
```
protected override void OnLoad(EventArgs e)
{
base.OnLoad(e);// Eklenmesi zorunlu yoksa eba metodları çalışmaz!
Page.Header.Controls.Add(new System.Web.UI.LiteralControl("<link rel=\"stylesheet\" type=\"text/css\" href=\"http://localhost/eba.net/Desktop/style/FormCustomStyle.css\" />"));
}
```

![](https://docsbimser.blob.core.windows.net/imagecontainer/CSS-18bf4056-0d34-4820-9769-32456feaa822.png)

eBA’nın kurulu olduğu dizin içinde (genelde c:\eba.net\ te kurulu olur.) c:\eba.net\eba.net\ Desktop\style\ dizini altında FormCustomStyle.css isimli bir css kütüphanesi oluşturulur. İlgili dosya için IIS_IUSRS
kullanıcısına okuma yetkisi vermeniz gerekmektedir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/CSS1-1abb17b3-077a-44e0-95f6-7b21c9fa8623.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/CSS3-f2f3f301-5c54-466c-892a-dae400fd7973.png)

FormCustomStyle.css dosyası düzenleme modunda açılarak ilgili css kodları yazılır. Nesneler için hangi css kodlarının yazılacağını, tarayıcı (Chrome veya Mozilla) üzerinde ilgili form üzerindeki nesneye sağ tıklayarak açılan menu üzerinden incele seçeneğine tıklayarak tarayıcının geliştirici modülünü açın. Nesnenin css
özelliklerini inceleyerek kendi css kodlarınızı FormCustomStyle.css dosyasına yazılır ve kaydedilir. eBA formu tekrar açıldığı zaman oluşturduğunuz tasarımlar forma uygulanmış olacaktır. Css üzerinde yaptığınız bir
değişiklikten form etkilenmiyorsa ilgili tasarım kodunun sonuna !important özelliğini tanımlayabilirsiniz. Aşağıda FormCustomStyle.css dosyası için kod örneği bulunmaktadır.

```
/*Metin Kutusu(Textbox) nesnesi stili*/
.css-textbox{
border:2px solid #456879; border-radius:10px; height: 22px;
padding-left:5px !important;
-moz-transition: all .51s !important;
-o-transition: all .51s !important;
-webkit-transition: all .51s !important; transition: all .51s !important;
outline: none !important;
}

.css-textbox:hover{
border-radius:3px !important; outline: none !important;
}

.css-textbox:focus {
border-radius:3px !important; outline: none !important;
border:1px solid red;
box-shadow: 0 0 10px #0089ff;
}

/*Tek Seçimlik Liste(Grid yapılı) (eBACombobox) nesnesi stili*/

.css-combobox,.css-combobox:focus,.css-combobox:hover{ border-top-right-radius :0px !important;
border-bottom-right-radius :0px !important;
}

.ComboBoxDelButton{ border: 1px solid #aaa; box-sizing: border-box; margin-left: -1px;
border-bottom-right-radius: 10px; border-top-right-radius: 10px;
-moz-transition: all .51s !important;
-o-transition: all .51s !important;
-webkit-transition: all .51s !important; transition: all .51s !important;
outline: none !important;
}

.ComboBoxDelButton:hover{ border: 1px solid #aaa; box-sizing: border-box; margin-left: -1px;
border-bottom-right-radius: 3px; border-top-right-radius: 3px;
}

/*Buton (Button) nesnesi stili*/
.css-button {
-moz-box-shadow:inset 0px 1px 0px 0px #54a3f7 !important;
-webkit-box-shadow:inset 0px 1px 0px 0px #54a3f7 !important; box-shadow:inset 0px 1px 0px 0px #54a3f7 !important;
background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #007dc1), color-stop(1, #0061a7)) !important; background:-moz-linear-gradient(top, #007dc1 5%, #0061a7 100%) !important;
background:-webkit-linear-gradient(top, #007dc1 5%, #0061a7 100%) !important;
background:-o-linear-gradient(top, #007dc1 5%, #0061a7 100%) !important;
background:-ms-linear-gradient(top, #007dc1 5%, #0061a7 100%) !important; background:linear-gradient(to bottom, #007dc1 5%, #0061a7 100%) !important;
filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#007dc1', endColorstr='#0061a7',GradientType=0) !important; background-color:#007dc1 !important;
-moz-border-radius:3px !important;
-webkit-border-radius:3px !important; border-radius:3px !important; border:1px solid #124d77 !important; display:inline-block !important; cursor:pointer !important;
color:#ffffff !important;
font-family:Arial !important; font-size:13px !important; padding:2px 12px !important;
text-decoration:none !important;
text-shadow:0px 1px 0px #154682 !important; width:auto !important;
height:auto !important;
-moz-transition: all .51s !important;
-o-transition: all .51s !important;
-webkit-transition: all .51s !important; transition: all .51s !important;
outline: none !important; border-radius:10px !important;
}
.css-button:hover {
background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #0061a7), color-stop(1, #007dc1)) !important; background:-moz-linear-gradient(top, #0061a7 5%, #007dc1 100%) !important;
background:-webkit-linear-gradient(top, #0061a7 5%, #007dc1 100%) !important;
background:-o-linear-gradient(top, #0061a7 5%, #007dc1 100%) !important;
background:-ms-linear-gradient(top, #0061a7 5%, #007dc1 100%) !important; background:linear-gradient(to bottom, #0061a7 5%, #007dc1 100%) !important;
filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#0061a7', endColorstr='#007dc1',GradientType=0) !important; background-color:#0061a7 !important;
border-radius:3px !important;
}
.css-button:active {
position:relative !important; top:1px !important;

}

.shadow-z-1 {
-webkit-box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12), 0 1px 2px 0 rgba(0, 0, 0, 0.24);
-moz-box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12), 0 1px 2px 0 rgba(0, 0, 0, 0.24);
box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12), 0 1px 2px 0 rgba(0, 0, 0, 0.24);
}
/* Detaylar Tablo (Details Grid) nesnesi stili*/ td > table {
width: 100%;
max-width: 100%; margin-bottom: 2rem;
background-color: transparent; border: 1px solid #687a9a; border-collapse: collapse; border-radius: 4px;
border-style: hidden;
box-shadow: 0 0 0 1px #326490;
}
td > table > thead > tr, td > table > tbody > tr, td > table > tfoot > tr {

-webkit-transition: all 0.3s ease;
-o-transition: all 0.3s ease; transition: all 0.3s ease;
}
td > table > thead > tr > th, td > table > tbody > tr > th, td > table > tfoot > tr > th, td > table > thead > tr > td, td > table > tbody > tr > td, td > table > tfoot > tr > td { text-align: left;
padding: 5px 3px; vertical-align: top; border-top: 0;
-webkit-transition: all 0.3s ease;
-o-transition: all 0.3s ease; transition: all 0.3s ease;
}
td > table > thead > tr > th { font-weight: 400;
color: #757575; vertical-align: bottom;
border-bottom: 1px solid rgba(0, 0, 0, 0.12);
}
td > table > caption + thead > tr:first-child > th, td > table > colgroup + thead > tr:first-child > th, td > table > thead:first-child > tr:first-child > th, td > table > caption + thead > tr:first-child > td, td > table > colgroup + thead > tr:first-child > td, td > table > thead:first-child > tr:first-child > td { border-top: 0;
}

td > table > tbody > tr:first-child {
background-color: rgba(35, 50, 90, 0.25) !important;
}

td > table > tbody > tr:last-child > td { padding: 2px !important;
}

td > table > tbody > tr > td > .css-textbox{ width:95% !important;
}

td > table > tbody > tr:last-child > td > .css-textbox{ width:25px !important;
text-align: center;
}

td > table > tbody > tr:first-child > td > span { text-align: center !important;
padding: 4px 0px !important; font-size: 12px !important; font-weight: bold !important; width: 100% !important;
color:#2d2d2d !important;
}

td > table > tbody > tr > td:first-child {
background-color: rgba(35, 50, 90, 0.25) !important; text-align: center;
font-size: 12px; font-weight: bold; padding: 8px;
}

td > table > tbody + tbody {
border-top: 1px solid rgba(0, 0, 0, 0.12);
}
td > table td > table {

background-color: #fff;
}
td > table .no-border { border: 0;
}

/* Detaylar ve Tablo (Details and Table) nesnesi stili*/
.eBATableContainer{
padding-left: 1px; padding-top: 1px; padding-bottom: 1px;
background-color: transparent; border: none;
margin-bottom: -30px;
}

.eBATable{
width: 100%;
max-width: 100%; margin-bottom: 2rem;
background-color: transparent; border: 1px solid #687a9a; border-collapse: collapse; border-radius: 4px;
border-style: hidden;
box-shadow: 0 0 0 1px #326490;
}

.eBATable .tableHeader{
background-color:transparent !important;
}

.eBATable > thead > tr,
.eBATable > tbody > tr,
.eBATable > tfoot > tr {
-webkit-transition: all 0.3s ease;
-o-transition: all 0.3s ease; transition: all 0.3s ease;
}

.eBATable > thead > tr > th,
.eBATable > tbody > tr > th,
.eBATable > tfoot > tr > th,
.eBATable > thead > tr > td,
.eBATable > tbody > tr > td,
.eBATable > tfoot > tr > td { text-align: left;
padding: 5px 3px; vertical-align: top; border-top: 0;
-webkit-transition: all 0.3s ease;
-o-transition: all 0.3s ease; transition: all 0.3s ease;
}

.eBATable .tableHeader td {
border-right: 1px solid rgb(104, 122, 154); text-align: center;
background-color: rgba(35, 50, 90, 0.25) !important; text-align: center;
font-size: 12px; font-weight: bold; width: 100%;
padding: 7px 10px !important; color:#2d2d2d !important;
}

.eBATable .tableAlternativeStyle1, .eBATable .tableAlternativeStyle2{ background-color: transparent;
border-width: 1px; border-color: rgb(104, 122, 154);

}

.eBATable .tableAlternativeStyle1 td, .eBATable .tableAlternativeStyle2 td{ border-width: 1px;
border-color: rgb(104, 122, 154);
border: 1px solid rgb(104, 122, 154);
}


.eBATable > tbody > .tableAlternativeStyle2{

}

.eBATable .tableAlternativeStyle1 td ,.eBATable .tableAlternativeStyle2 td { padding: 3px 7px;
vertical-align: middle;
}

.eBATable .tableAlternativeStyle1 td img,.eBATable .tableAlternativeStyle2 td img { margin: 5px 7px;
}

.eBATable .tableAlternativeStyle1 td input,.eBATable .tableAlternativeStyle2 td input { margin: 5px 10px;
}
```