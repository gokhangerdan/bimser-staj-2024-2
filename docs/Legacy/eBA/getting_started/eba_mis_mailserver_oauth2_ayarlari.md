# eBA MIS & MailServer OAuth2 Ayarları 

1. Common dizinindeki “OAuthConfig.json” dosyasına ilgili provider’dan alınan bilgiler doldurulur.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c151eef-d37b-4a20-a6bd-b51cb628a988)

2. Common dizinindeki OAuthLogin.exe uygulaması başlatılır. Microsoft için çalıştırılıyor ise; çalıştırıp 
token aldıktan sonra schedule task’lar için system user’ı ile de login olunup ayrıca token alınmalıdır.æ

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload501fe19c-3f82-47e1-bc94-1eb84a24098a)

2.1. System user’ı ile başlatabilmek için;
• PsExec tool’u https://learn.microsoft.com/en-us/sysinternals/downloads/psexec veya 
https://download.sysinternals.com/files/PSTools.zip adresinden indirilir ve 
“C:\Windows\System32\” altına kopyalanır.
• Command prompt (cmd.exe) admin yetkisi ile açılıp ”psexec -i -s 
......\Common\OAuthLogin.exe” komutu girilir ve OAuthLogin uygulaması başlatılır. (Noktalar 
ile belirtilen kısım ebanın kurulu olduğu yeri temsil ediyor)


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb450317-2064-4d59-bb0b-78043d04c93a)

3. Yön tuşları ile gezinip kullanılan provider seçilir ve doğrulama adımları gerçekleştirilir.
3.1. Google: Bir hesap seçimi ve doğrulama ekranı açılacaktır. Doğrulama adımları tamamlanıp token 
alım işlemi gerçekleştirilir. “Received verification code....” mesajı görüldükten sonra sayfa 
kapatılabilir. İstenirse “C:\ProgramData\Bimser” yolu ile token dosyası kontrol edilebilir.




![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5d8ee9b8-fba9-4b46-b0cc-3658c8912095)

3.2. Microsoft: Bir login url’si ve cihaz kodu içeren bir mesaj belirecektir. İlgili url’ye gidip verilen cihaz 
kodu girildikten sonra doğrulama adımları tamamlanıp token işlemi gerçekleştirilir. “You have 
signed in....” mesajı görüldükten sonra sayfa kapatılabilir. İstenirse “C:\ProgramData\Bimser” 
yolu ile token dosyası kontrol edilebilir.




![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload839361ee-315a-47bc-bea2-d500a90fc230)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60895ef8-7bf7-41ed-b3a9-b6417e68fcc5)

4. Token alımı başarıyla tamamlandıktan sonra OAuthLogin.exe uygulaması kapatılabilir.
5. Mail gönderimini sağlamak için;
5.1. eBA Configuration Manager’da Mail Settings sekmesindeki gerekli alanlar doldurulduktan sonra 
UseOAuth seçeneği aktif edilir. İlgili provider’ın gerektirdiği alanlar doldurulur ve uygulama
kaydedilir



![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7b828b8-f2d5-4e8a-a488-5ad48ab34e13)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload107595c1-f098-48b3-8160-1eac56a9cd61)

5.2. Advanced sekmesinden MailServer/Profiles/EBA anahtarı açılıp ilgili provider’a ait OAuth bilgileri 
kontrol edilir ve gerekli olan parametreler eklenir.
5.2.1. Google: ClientId, ClientSecret ve Scopes bilgileri aşağıdaki şekilde dolu olmalıdır.



![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4809231-6ed8-438c-86af-c9618ebac625)

5.2.2. Microsoft: ClientId, TenantId, Scopes, Instance ve RedirectUri bilgileri aşağıdaki şekilde 
dolu olmalıdır.




![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload585558e7-2b5c-4740-b538-ae88f9ce2e1c)

5.3. Uygulama kaydedilir. MailServer.exe veya Schedule Tasks üzerinden mail gönderimi test 
edilebilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload018a4056-d221-41db-9645-91b6aefa3981)

6. Mail okuma süreci için;
6.1. eBA Configuration Manager üzerindeki Mail Integration sekmesinden profil ekleme ekranı açılır 
ve gerekli alanlar doldurulduktan sonra UseOAuth seçeneği aktif edilir. İlgili provider’ın 
gerektirdiği alanlar doldurulur ve uygulama kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd00f88e-80f5-4c71-8f4b-01d91103fa29)

6.2. Advanced sekmesinden MailServer/Inboxes anahtarı açılıp ilgili profil üzerindeki OAuth bilgileri 
kontrol edilir ve gerekli olan parametreler eklenir.
6.2.1. 5.2.1 adımı aşağıdaki şekilde uygulanır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73b4e3c2-ee78-4bb5-b14f-8fe3db262332)

6.2.2. 5.2.2 adımı aşağıdaki şekilde uygulanır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada6af0d77-3fb7-48ef-b657-8c6f3cbee295)

6.3. Uygulama kaydedilir. Schedule Tasks üzerinden mail okuma süreci test edilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfef786e1-57e8-49a7-a45e-1077b2b41ba0)