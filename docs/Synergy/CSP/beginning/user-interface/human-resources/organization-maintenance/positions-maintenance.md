---
sidebar_label: Pozisyon Bakımı
sidebar_position: 2
custom_edit_url: ""
---

# Pozisyon Bakımı

İş akışları hem kullanıcı bazlı hem pozisyon bazlı yürütülebilmektedir. Süreç adımlarında pozisyon kullanıldığında işlemler, ilgili pozisyona sahip olan kişi tarafından yürütülür. Aynı kullanıcı gibi pozisyon da pasife düştüğünde, süreç adımlarında pasif bir pozisyona rastlanırsa sistem “pasif pozisyon” uyarısı verecektir. Bu uyarının alınmaması ve işlemlerin pasif pozisyon yerine, aktif bir pozisyonun üzerinden devam edebilmesi için Pozisyon Bakımı alanı kullanılır.

Organizasyon Bakımı başlığı altındaki Pozisyon Bakımı alanına tıklandığında, daha önceden tanımlanmış olan kayıtlar varsa onlar listelenecektir.

Bu kayıt listesinde arama yapılabilir, kolonları arasında sıralama yapılabilir veya yeni bir kayıt eklenebilir.

![Pozisyon Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbaaf9fde-2687-4be5-ada1-6ab33f907930)

Yeni bir tanım eklemek için, kayıt listesinin sol üst köşesinde yer alan “Yeni” butonuna basılır. Yeni butonuna basıldığında yan panelde, **“No”** ve **“Yeni No”** alanlarının doldurulması beklenen boş bir sayfa açılacaktır.

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| No 	| Bu alandan, pasife düşen pozisyon kaydı seçilmelidir 	|
| Yeni No 	| Bu alandan, pasif pozisyonun yerine geçecek pozisyonun kaydı seçilmelidir 	|

No ve Yeni No alanlarından pozisyon kayıtları seçilerek sayfanın üzerindeki kaydet butonuna basıldığında, tanım işlemi tamamlanmış olur.

No alanından pasif pozisyonun seçimi;

![Pozisyon Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5f45470-1569-4a05-828a-335db5fb4bef)

Yeni No alanından aktif pozisyonun seçimi;

![Pozisyon Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6bd3257d-2fa6-49cd-8f55-5f20835aa2bb)

Seçimlerin kaydedilme işlemi;

<div style={{textAlign: 'center'}}>

![Pozisyon Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade5b9427d-bc72-435c-8698-7a45440748f8)

</div>

No ve Yeni No alanlarından seçimler yapılıp Kaydet butonuna basıldığında, kayıt listesine yeni tanımlanan kayıt da eklenecektir. Bu işlem sonrasında sistem, pasife düşen kaydın geçtiği adımlarda işlemi yeni pozisyona otomatik yönlendirecektir.

## En İyi Uygulama

:::tip DOĞRU KULLANIM

- Yeni No alanından, pasife düşen pozisyonun yerine geçmesi istenen aktif bir pozisyon seçimi yapılmalıdır. İş akışlarında, pasif pozisyonun kullanıldığı adımlarda süreç istekleri bu işlemden sonra artık Yeni No alanından seçilen pozisyona düşürülecektir

:::

:::danger YANLIŞ KULLANIM

- Bu işlem, iş akışlarında daha önceden kullanılmış bir pozisyon kaydının pasife düşmesi durumunda hata alınmaması ve işlemlerin durmaması için kullanılır. Pozisyon kaydı pasife düşmemişse bu bakım tanımı yapılmaz

:::