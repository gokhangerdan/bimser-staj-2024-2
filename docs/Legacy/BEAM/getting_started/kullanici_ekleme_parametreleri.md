# SİSTEM YÖNETİMİNDE KULLANICI EKLERKEN HANGİ SEKMELERDE NASIL İŞLEVLER GERÇEKLEŞTİRİLİYOR?

![](https://docsbimser.blob.core.windows.net/imagecontainer/SİSTEM%20YÖNETİMİ.1-97123ad2-6b64-4207-95cb-e5080f30c60b.png)

İlk aşamada Sistem yönetimi>Kullanıcılar sekmesine girilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/sistem%20yönetimi.2-c7a5af6e-967a-42fc-9bc8-4511551e1d14.png)

Artı butonu ile sisteme yeni bir kullanıcı eklenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/sistem%20yönetimi.3-48d3ef74-52f0-4b1e-af75-9c9abf5509a4.png)

Bir kullanıcı eklerken genel bilgiler sayfasında zorunlu doldurulması gereken alanlar kalın siyah punto ve * ile ifade edilmiştir. Kullanıcı kodu ve kullanıcı tanımı yazılmalıdır. Sadece talep açan bir kullanıcı ise kullanıcı rol tipi sekmesinden "talep kullanıcısı" seçilmektedir. Kullanıcı eğer normal kullanıcı rol tipinde ise istersem bakım sorumlusu istersem admin yetkisi verilebilmektedir. 

Ait olduğu kullanıcı grubu belirtilmelidir. Örnek veriyorum talep kullanıcısı ise kullanıcı grubu "Talep kullanıcıları" grubu seçilmelidir. Bakım yapan kullanıcılar için ise "Emir kullanıcıları" grubu seçilmelidir.

Birden fazla şirketi olan müşteriler "yetkili olduğu şirketler" sekmesinden kullanıcının ait olduğu şirketi belirtmelidir.  Şifre saklama türü seçildikten sonra kaydet butonu ile sisteme bir kullanıcı eklenebilir. 

Ek olarak kullanıcıya mobil kullanabilme yetkisi verilecek ise en aşağıda yer alan"mobil lisansı etkinleştir" seçeneği işaretlenmelidir veya kullanıcıya yönetici yetkisi verilecek ise "yönetici mi" ifadesi işaretlenmelidir. 

Aşağıda sistem yönetiminde bir kullanıcı eklerken yer alan sekmeler hakkında bilgilere değinilmektedir.

### Yetkili Olduğu İşletmeler

Yetkili olduğu işletmeler filtresi sekmesinden kullanıcıya “işletme yetkisi” verildiğinde sadece o işletmenin varlıklarını ve kısımlarını görür. Filtrelerde yalnız ait olduğu işletmenin sarfyeri ve kısmını görür.

### Yetkili Olduğu Malzeme Hareket Türleri

Malzeme hareket türü verdiğimizde malzeme talebi ve transferi sayfasında verdiğimiz hareket türü yetkisini görür ve yapabilir. Sadecekullanıcı gruplarından ((BCG1.112) - Malzeme Talebi ve Transferini Onaylayabilir)  Parametresini pasifleştirmemiz gerekmektedir. Pasifleştirdiğimizde grup bazlı malzeme talebi etme ve grup bazlı malzeme talebi onaylama yetkisini verebiliriz

### Yetkili Olduğu Varlık Kodu

Kullanıcıya yetkili olduğu varlık kodu verilirse: verilen varlık kodundaki varlıkları görebiliyor. Kullanamaz yetkisi verilirse (yalnız görebilir işaretli ise) iş emri içerisinde o varlığı göremez, iş emrinde o varlığı kullanamaz, sadece o varlığı varlıklar sayfasında inceler

### Yetkili Olduğu İş Emri Türü

Kullanıcıya yetkili olduğu iş emri türü yetkisi verdim. Arızi türü görebilir kullanabilir, montajı kullanamaz. Montaja açılan iş emirlerini iş emri sayfasında gördü ama montaja iş emri açamadı, arızi hariç hiçbirine iş emri açamadı.

### Yetkili Olduğu Ambar Kodu

Yetkili olduğu ambar kodu yetkisini verdim, malzeme hareketleri sayfasından istediğim hareketi yaparsa yapsın yetkili olduğu ambar seçilir. Ambarı değiştiremez.

### Varsayılan Filtreler

Varsayılan filtreler sekmesi görebildiğin varlıkları kısıtlamamazı sağlar. Talep açarken hangi varlıkları görmeliyim, hangi bakım arıza kodlu olan işemirlerini sayfamda görmeliyim. Sayfamı nasıl görmek istiyorsam “varsayılan” sekmesinden şekillendiriyorum.
Seçim kutucuğundan ise neleri seçebilirim onları sisteme tanıtıyorum. Seçimlerimi kısıtlıyorum.


### Varlık Filtreleri

Varlık filtreleri sayfasından sarfyeri yetkisi verildiğinde kullanıcı varlıklar sayfasında sadece o sarfyerinde bulunan varlıkları görebiliyor. Varlık ekleyecekse sadece o sarfyerine varlık ekleyebiliyor. Sadece bu sarfyerindeki varlıklara talep/işemri açabiliyor. Sarfyeri değiştirme yetkisi olmuyor.

Varlık filtreleri malzemeler kutucuğunda kısım yetkisi verildiğinde kullanıcıya, o kısım harici malzeme hareketi başka bir kısımda yapılınca göremiyor

### İş Emri Yetkileri

İş emri yetkileri sekmesinde: iş talebi değiştirme yetkileri kutucuğunda mekanik yetkisi verildi bu sayede inşaat iş talebine giremiyor. "İnşaat" filtresini değiştirme yetkiniz yoktur diye uyarı alınıyor. Sadece opr iş tipindeki iş emrini değiştirebiliyor fakat kapatılamıyor.


