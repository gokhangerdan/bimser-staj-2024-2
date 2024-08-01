# Öneri - Kiosk Entegrasyonu

1)	Öncelikle kullanıcıların kiosk girişi sağlamanız için QDMS kiosk adresi aşağıdaki gibidir. QDMS kiosk adresi  ; 
http://qdmsadresi/QDMS/QDMSNET/BSAT/LogonCardReader.aspx?cs=   şeklinde olmalıdır. 

2)	Sonrasında kullanıcıların kiosk kart numaraları QDMS sistemine tanımlı olmalıdır. Sisteme tanımlamak için excel şablonda kolon olarak “Kart Numarası” ve “QDMS Sicil No” bilgilerini iletmeniz gerekmektedir.(BSS kaydı üzerinden iletilebilir)

3)	Son olarak Sistem alt yapı parametrelerinden 112 numaralı ‘Kart okuyucu ile kullanıcı girişinde kart numarasının kaç karakteri kullanılacak ?’ parametre değişikliği ihtiyaca göre değiştirilir. Örnek olarak Kart numarasının ilk 7 hanesinin okunacağını iletirse Parametre değeri olarak 7 yazılır ve ilk 7 hanesinin doğru olduğu kabul edilir. Kiosk Kart numarasının tüm karakterleri okunacaksa en büyük Kart numarasından büyük bir değer yazılabilir. Örnek olarak Max kart numara karakter sayısı 15 ise parametre değeri olarak 15 ten büyük bir değer yazılmalıdır.
4)	Ayarlar tamamlandıktan sonra kullanıcılar kiosk üzerinde kartlarını okutarak sisteme erişim sağlayabilirsiniz.  


![](https://docsbimser.blob.core.windows.net/imagecontainer/Kiosk.png-9b1593e8-8629-4186-adf9-aa2896fbde0e.png)

