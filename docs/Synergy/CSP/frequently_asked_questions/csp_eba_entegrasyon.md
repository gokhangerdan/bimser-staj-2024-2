# EBA ENTEGRASYON 

Eba entegrasyonu için veri tabanında Configuration tablosunda aşağıdaki satırı eklenmesi gerekmektedir.
Keyname kısmı için, Web.eBAIntegration.Config 
Value kısmı için, 
{"enabled":true,"configs":[{"name":"https://*****/eba.net","version":"6.7","url":"https://******/eba.n
et","userName":"xxxx","password":"xxxxxxxx","externalUserType":"sapuser"},{"name":"https://*****/e
ba.net","version":"6.4","url":"https://********/eba.net","userName":"xxxx","password":"xxxxxxx"}]}
Olarak girilmelidir.
Burada password alanları base64 tipinde olmalıdır.
Veri tabannıdaki işlemimiz bittikten sonra Config cache temizlenmelidir.
https://docs.bimser.net/docs/Synergy/CSP/frequently_asked_questions/invalidate_configurations_cache_temizleme/

Bu şekilde işlemlerinizi tamamlandığında aşağıdaki  görselde görülen 'Düğüm İşlem Türü' kısmına 'Eba Entegrasyon' kısmı gelecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eba_entegrasyon1-cb5b471b-b7ac-4394-b3fa-643ee2ab9161.png)

