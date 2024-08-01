# Beam akışı için EbaHr hazırlanması

## 1.Eba System Manager

İlk olarak Eba System Manager da Integration Manager- Connection – New Connection – Connector for Microsoft SQL Server Database i seçip Next diyoruz.


![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem1-6fa2b188-badd-4f03-beaf-386ecf124bfd.png)

Connection ismi ve açıklaması girip Next diyoruz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem2-b0caad01-9d78-4f37-9e05-624143b8f461.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem3-0b597132-a060-433a-bd8a-a5cbfce4d8aa.png)

Server adını giriyoruz .
Use informaion to log on to the server ı eğer veritabanının windows autotantication özelliği açıksa seçebiliriz yada User a spesific user name ve password u veritabanımıza ilk girişte kullandığımız kullanıcı adı ve şifresini yazarak ta seçebiliriz.
Son olarak ilgili veritabanını seçip Finish diyoruz. Karşımıza gelen ekranda Save and Compile diyoruz.
Save and Compile dedikten sonra new query oluşturuyoruz. Query nin HROrganization ve SQL kodunu giriyoruz. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASytem4-8bdd97d5-9879-4c4d-b74a-9ae42c5691b5.png)

HR entergrasyonunda kullanılan sorgu aksi bir durum yoksa genel olarak şudur:
 
Select KULKOD USERID,KULAD FIRSTNAME,'.'LASTNAME,'BOYS' DEPARTMENT,'' EMPLOYEMENTSTART,
'' POSITION,'' POSITIONNAME,EMAILADR EMAIL ,'' MANAGERUSERID,'BOYS' PROFESSION,'BOYS' DEPARTMENTNAME, 1 STATUS,
 'BOYS' PROFESSIONNAME from BC_USERS WHERE ISTATUS=1 AND KULKOD NOT IN (SELECT ID FROM [EBA].dbo.OSUSERS WHERE IMPORTSTATUS = 0)
 
Veya 
Select KULKOD USERID,KULAD FIRSTNAME,'.'LASTNAME,'BOYS'DEPARTMENT,''EMPLOYEMENTSTART,
'' POSITION,''POSITIONNAME,EMAILADR ASEMAIL ,''MANAGERUSERID,'BOYS'PROFESSION,'BOYS'DEPARTMENTNAME, 1 STATUS,
  'BOYS'PROFESSIONNAME  fromBC_USERS WHEREISTATUS=1)
 
HATA VERİRSE:
Select KULKOD USERID, KULAD FIRSTNAME, '.' LASTNAME, 'BOYS' DEPARTMENT,'' EMPLOYEMENTSTART,
'' POSITION,'' POSITIONNAME,EMAILADR AS EMAIL ,'' MANAGERUSERID, 'BOYS' PROFESSION, 'BOYS' DEPARTMENTNAME, 1 STATUS,
  'BOYS' PROFESSIONNAME  from BC_USERS WHERE ISTATUS=1  AND EMAILADR IS NOT NULL AND EMAILADR!='' AND  KULKOD COLLATE Turkish_CI_AS NOT IN ( SELECT ID FROM [EBA].dbo.OSUSERS WHERE IMPORTSTATUS = 0)
 
Ok deyip karşımıza çıkan ekrana Save and Compile diyoruz.


![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem5-ecbb7ced-631b-4177-a37d-50512abaff33.png)

Ekranda karşımıza çıkan Boys kullanıcımızın Eba’da kayıtlı olmadığını görüyoruz.Next diyoruz ve daha sonrasında Finish diyoruz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASytem6-fc603fd4-30f3-48a3-832c-1b198bdf386c.png)

Finish dediğimizde Succesfull Compiled! Uyarısını görüyoruz.
İkinci olarak HROrganizationRelations Query si için de yeni bir new query oluşturuyoruz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem7-24727dba-fb81-4cc6-b890-da6b9b82f063.png)

Bu durumda kullandığımız sorgu :
SELECT    'BOYS' AS DEPARTMENT,'BOYS' AS DEPARTMENTNAME, 'BOYS' AS MANAGERUSERID , 'BOYS' AS MANAGERDEPARTMENT
Ok diyoruz. Save and Compile diyoruz.


![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem8-1a940e76-6606-4c86-920d-4c1514b8a347.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem9-ae645f41-41dd-4e2a-a22c-828f94c4a47e.png)

Finish ve Save and Compile deyip bu kısmı bitiriyoruz.

## 2.Eba Configuration Manager

Bu kısımda ilgili ayarları yapıyoruz. Eba Configuration Manager den hangi uygulama ile ilgili HR yapıldı ise onu seçiyoruz.


![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem10-e4bcbdfe-630e-47e8-b1d9-12f721d9d862.png)

Ok dediğimizde karşımıza gelen ekranda Advanced bölümüne geçiyoruz.
Advanced bölümünde HR ve Transfer kısmına geliyoruz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem11-e85387fb-d154-4988-a1cd-6ffdbd7ad45c.png)

İntegration Connection kısmına en başta yeni connection a verdiğimiz ismi yazıyoruz. BOYS olarak bağlantı adı vermiştik. Source kısmına integration yazıyoruz, diğer kısımları ise false yapıyoruz ve File – Save deyip kaydediyoruz.
Daha sonra arayüz kısmına geçiyoruz.
Eba system Manager de Profession (Ünvan) tanımlıyoruz. Transfer durumunu aktif olarak seçiyoruz

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem12-3a0db0a0-d0ce-469d-808d-ee9d611c84c3.png)

Eba Configuration Manager de – Schedule Task  a geliyoruz.


![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem13-4a317081-8ca3-46c4-9cc8-1fc0856f96bb.png)

New butonundan yeni bir job ekliyoruz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBASystem14-751c7e08-072d-476b-8545-c70922d4cf17.png)

 Job Name yapmış olduğumuz entegrasyon adı , 
Assembly Path : eba klasörünün içinde ki common un altında ebaHRTransfer.exe yoludur.
Class Name = eBAHRTransfer.HRTransferJob
Test etmek için de : Eba – common – ebaHRTansfer.exe 

