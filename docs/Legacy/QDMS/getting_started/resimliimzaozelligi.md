# Resimli İmza Özelliği

Merhaba,
Doküman parametrelerinden 311,312,313 no'lu parametre değerlerini kullanarak resim imza özelliğini aktif edebilirsiniz.

İlk olarak 312 no'lu(Imza dosyaları yüklenebilsin mi?) parametre değeri evet yapılır.
Parametre değeri evet yapıldığında ana ekranda sağ üstte kullanıcı ismi yazan yere tıklandığında 'Kullanıcı imza yükleme' adında bir alan çıkacaktır. Buraya kullanıcı, kendi imzasını yüklemesi gerekmektedir.

Yüklenen imza doküman parametrelerinden 311(Dijital imza resim boyutları) formatında olmalıdır. Bu parametre değerine en-boy değeri girilmeli ve kullanıcı, resim olarak imzasını formata göre tanımlamalı.(Parametre kullanım örnek: 75,100)



Tanımlamalar yapıldıktan sonra, doküman üzerinde aşağıda iletilen taglerin kullanılması durumunda, ilgili taglerin yerine sistem, otomatik olarak kullanıcı imza resmini replace edecektir.
Ayrıca doküman parametrelerinden 313 no'lu parametre ile de, sadece belirli taglerin kullanılması sağlanabilir. Bu parametre değeri boş olduğunda sistem, tagleri yine replace edecektir. Doldurulduğunda, sadece doldurulan tagler replace edilir.

<HAZIRLAYAN_SIGN>

<ON_KONT_EDEN_SIGN>

<KONTROL_EDEN_SIGN>

<SON_ONAY_SIGN>

<REVIZE_EDEN_SIGN>

<1_ONAY_SIGN>

<2_ONAY_SIGN>

<3_ONAY_SIGN>

İyi çalışmalar.


![](https://docsbimser.blob.core.windows.net/imagecontainer/311.png-fdefbb76-8a28-4a95-b35b-fe181de0063b.png)

