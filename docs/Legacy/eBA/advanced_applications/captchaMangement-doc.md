# eBA Captcha Detaylı Kullanım Dokümanı
Bu doküman eBA platformu içerisinde captcha özelliğinin nasıl yapılandırılarak kullanabileceğini anlatmaktadır. 

## Kullanım 
eBA içerisinde captcha yapılandırma ve kullanımı **eBA Configuration Editor** üzerindeki **Advanced** sekmesindeki **Security** kırılımından gerçekleştirilir.

Genel olarak captcha 3 parametre üzerinden yönetilir, bunlar;
- EnableCaptcha
- CaptchaCount
- CaptchaCase

![](https://docsbimser.blob.core.windows.net/imagecontainer/captcha-configuration-2a57cdca-a1bc-4e83-9215-7106786f0cca.png)


Captchayı sistem üzerinde aktif edebilmek için bu ekranda **EnableCaptcha** parametresini **true** olarak ayarlamak ve **CaptchaCount** parametresine değer vermek gereklidir. **EnableCaptcha** parametresi sistem genelinde captchanın aktif olup/olmayacağını belirten parametredir. **CaptchaCount** parametresi de captcha sistem genelinde aktif ise kaç başarısız giriş denemesinden sonra ekranda captcha'nın görüneceğini belirtir.

**CaptchaCase** Parametresi ise görüntülenen captcha içerisinde ki harflerin sadece büyük, sadece küçük yada büyük/küçük karışık bir şekilde geleceğini belirten parametredir. Bu parametre 2 farklı değer alabilir bunlar;
- upper
- lower

Parametre "upper" olarak belirtildiğinde captcha içerisinde görüntülenen karakterler aşağıdaki gibi sadece büyük olarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/upper-40600f77-2a12-43c7-95a7-96bcea33bae0.png)

Parametre "lower" olarak belirtildiğinde captcha içerisinde görüntülenen karakterler aşağıdaki gibi sadece küçük olarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/lower-0d83206b-0503-4a31-b84d-77210d9510b9.png)

Eğer bu parametre hiç eklenmezse yada boş geçilirse captcha içerisinde görüntülenen karakterler aşağıdaki gibi büyük/küçük karışık olarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/mixed-094642dd-b7e0-41df-b525-0558edca850e.png)

eBA Configuration Editor parametreleri ile ilgili daha detaylı bilgilere [buradan](https://docs.bimser.net/docs/Legacy/eBA/advanced_applications/config_key_list 'Config Key List') ulaşabilirsiniz.