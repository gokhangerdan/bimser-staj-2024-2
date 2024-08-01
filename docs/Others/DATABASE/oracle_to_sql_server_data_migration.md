# ORACLE TO SQL SERVER DATA MIGRATION

Data taşınmaya başlanmadan önce taşınacak uygulamanın SQL Server versiyonu SQL sunucusunda kurulur. Tabloların oluşması sağlanır. Oluşan boş tablolara Oracle tarafındaki mevcut data aktarılacak. 

___

### SSMA ile Oracle’da SQL Server’a data migrate adımları:

1.	SQL SERVER MIGRATION ASSISTANT for ORACLE (SSMA) tool’u indirilip kurulur. 
2.	SSMA çalıştırılır.
3.	New Project ile yeni proje oluşturulur. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload334f9d5a-0086-4449-8c31-0fb1ba64b4a7)

4.	Yeni Projeye isim verilir. Proje dosyasının lokasyonu seçilir ve Taşınma yapılacak SQL Server versiyonu seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c35a1e8-0705-43ba-a42f-b6844a197aa9)

5.	Connect to Oracle butonu tıklanır ve Oracle DB’ye bağlanır. 
Örnek connection string:  Data Source =(DESCRIPTION=(ADDRESS=(HOST=xxx.xxx.xx.xx) (PROTOCOL=TCP)(PORT=1521)) (CONNECT_DATA=(SID=xxxx))); password=xxxxx; user id=xxxx; DBA Privilege=SYSDBA;


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e795496-adca-42a2-bb98-e6ddb0464a04)

6.	Oracle’a bağlandıktan sonra açılan pencerede taşınacak datanın olduğu şemalar seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90c3751b-39d0-4b05-a311-8d178ccde3ee)

7.	Connect to SQL Server butonu tıklanır. SQL Server bilgileri girilerek SQL server’a bağlanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a44234d-3eab-42b9-b174-353c336476db)

8.	Oracle Schemas tıklanıp açılan sağ tarafta kaynak ve hedef şema seçimi yapılır. Sql server tarafında .dbo gibi.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26781c7a-4980-43b8-8dd2-ff5cfc124eff)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload162d77a1-b1ad-4a05-a983-353e35b0d212)

9.	Migrate Data butonu ile taşıma işlemi başlatılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9af5bc5f-6cc1-437d-a71d-38ea22389801)