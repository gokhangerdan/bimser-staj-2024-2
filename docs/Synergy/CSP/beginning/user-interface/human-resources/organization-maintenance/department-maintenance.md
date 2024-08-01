---
sidebar_label: Departman Bakımı
sidebar_position: 3
custom_edit_url: ""
---

# Departman Bakımı

Organizasyonda var olan bir departman kapatılabilir, başka bir departmanla birleştirilip yeni bir id ve tanım alabilir. Böyle bir durumda mevcut departmanın durumu pasife düşer. Pasif departman yerine yenisini tanımlamak için, Organizasyon Bakımı başlığı altındaki Departman Bakımı alanı kullanılır.

Departman Bakımı alanına tıklandığında, daha önceden tanımlanmış olan kayıtlar varsa onlar listelenecektir.

Bu kayıt listesinde arama yapılabilir, kolonları arasında sıralama yapılabilir veya yeni bir kayıt eklenebilir.

![Departman Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload97683ed5-3e10-4e85-a58e-3fb423046a58)

Yeni bir tanım eklemek için, kayıt listesinin sol üst köşesinde yer alan “Yeni” butonuna basılır. Yeni butonuna basıldığında yan panelde, **“No”** ve **“Yeni No”** alanlarının doldurulması beklenen boş bir sayfa açılacaktır.

| **Özellik** 	| **Açıklama** 	|
|---	|---	|
| No 	| Bu alandan, pasife düşen departmanın kaydı seçilmelidir 	|
| Yeni No 	| Bu alandan, pasif departmanın yerine geçecek departman kaydı seçilmelidir 	|

No ve Yeni No alanlarından departman kayıtları seçilerek sayfanın üzerindeki kaydet butonuna basıldığında, tanım işlemi tamamlanmış olur.

No alanından pasif departmanın seçimi;

![Departman Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7f2f2de-3b71-4aff-8c0f-ebed7a63f014)

Yeni No alanından aktif departmanın seçimi;

![Departman Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e1fa144-b446-41f9-b175-db8a499fa763)

Seçimlerin kaydedilme işlemi;

<div style={{textAlign: 'center'}}>

![Departman Bakımı](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2159249-9775-4ee4-830f-3d8fcde0da66)

</div>

No ve Yeni No alanlarından seçimler yapılıp Kaydet butonuna basıldığında, kayıt listesine yeni tanımlanan kayıt da eklenecektir. Bu işlem sonrasında sistem, pasife düşen kaydın geçtiği adımlarda işlemi yeni departman üzerinden yürütecektir.

## En İyi Uygulama

:::tip DOĞRU KULLANIM

- Yeni No alanından, pasife düşen departmanın yerine geçmesi istenen aktif bir departman seçimi yapılmalıdır. İş akışlarında, pasif departmanın kullanıldığı adımlarda  işlemler artık Yeni No alanından seçilen departman ile yürütülecektir

:::

:::danger YANLIŞ KULLANIM

- Bu işlem, iş akışlarında daha önceden kullanılmış bir departman kaydının pasife düşmesi durumunda hata alınmaması ve işlemlerin durmaması için kullanılır. Departman kaydı pasife düşmemişse bu bakım tanımı yapılmaz

:::