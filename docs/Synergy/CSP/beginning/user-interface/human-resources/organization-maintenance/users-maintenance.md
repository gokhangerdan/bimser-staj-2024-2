---
sidebar_label: Kullanıcı Bakımı
sidebar_position: 1
custom_edit_url: ""
---

# Kullanıcı Bakımı

İşten çıkma, mevcut kullanıcı id sinin değişmesi gibi durumlarda, kullanıcının sistemdeki kaydının durumu pasife düşer. Mevcut id, sistemde yürütülmekte olan süreçlerde tanımlanmış olabilir. Kayıt pasife düştüğü anda, devam etmekte olan süreçler bu pasif kayda geldiğinde sistem “kullanıcı pasif” uyarısı verecek ve süreç tıkanacaktır. Bu sorunun önüne geçmek için Kullanıcı Bakımı alanından, pasif kullanıcı id si yerine, aktif bir kullanıcı id si tanımlanması gerekmektedir. Tanımlanan aktif kullanıcı artık pasif kullanıcı yerine geçecek demektir.

Organizasyon Bakımı başlığı altındaki Kullanıcı Bakımı alanına tıklandığında, daha önceden tanımlanmış olan kayıtlar varsa onlar listelenecektir.

Bu kayıt listesinde arama yapılabilir, kolonları arasında sıralama yapılabilir veya yeni bir kayıt eklenebilir.

![Kullanıcı Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73a8b7a5-ef1e-4c14-bb40-d3f24401ff2e)

Yeni bir tanım eklemek için, kayıt listesinin sol üst köşesinde yer alan **“Yeni”** butonuna basılır. Yeni butonuna basıldığında yan panelde, **“No”** ve **“Yeni No”** alanlarının doldurulması beklenen boş bir sayfa açılacaktır.

![Kullanıcı Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64d138a3-6876-4bc0-bb7a-c033f8a94ba7)

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| No 	| Bu alandan, pasife düşen kullanıcı kaydı seçilmelidir 	|
| Yeni No 	| Bu alandan, pasif kişinin yerine geçecek kullanıcının kaydı seçilmelidir 	|

No ve Yeni No alanlarından kullanıcı kayıtları seçilerek sayfanın üzerindeki kaydet butonuna basıldığında, tanım işlemi tamamlanmış olur.

No alanından pasif kullanıcının seçimi;

![Kullanıcı Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9768939-fb77-42ef-b43d-6fe958535dc9)

Yeni No alanından aktif kullanıcının seçimi;

![Kullanıcı Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0cf7af18-63b5-44b6-897c-f419b24271a6)

Seçimlerin kaydedilme işlemi;

<div style={{textAlign: 'center'}}>

![Kullanıcı Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9f2abf5-f823-406d-b2ab-499ec109a504)

</div>

No ve Yeni No alanlarından seçimler yapılıp Kaydet butonuna basıldığında, kayıt listesine yeni tanımlanan kayıt da eklenecektir. Bu işlem sonrasında sistem, pasife düşen kaydın geçtiği adımlarda işlemi yeni kullanıcıya otomatik yönlendirecektir.

## En İyi Uygulama

:::tip DOĞRU KULLANIM

- Yeni No alanından, pasife düşen kullanıcının yerine geçmesi istenen aktif bir kullanıcının seçimi yapılmalıdır. İş akışlarında, pasif kullanıcının kullanıldığı adımlarda süreç istekleri bu işlemden sonra artık Yeni No alanından seçilen kişiye düşürülecektir

:::

:::danger YANLIŞ KULLANIM

- Bu işlem, iş akışlarında daha önceden kullanılmış bir kullanıcı kaydının pasife düşmesi durumunda hata alınmaması ve işlemlerin durmaması için kullanılır. Kullanıcı kaydı pasife düşmemişse bu bakım tanımı yapılmaz

:::