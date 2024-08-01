---
sidebar_label: Görünüm Yöneticisi Paneli
sidebar_position: 10
custom_edit_url: ""
---

# Görünüm Yöneticisi Paneli

Proje formlarının birden fazla görünümü tasarlanabilir. Akışın farklı adımlarında, farklı kişilere veya farklı durumlara bağlı olarak formun farklı görünümleri gösterilmek istenebilir.

Projeler ilk oluşturulduklarında formlar varsayılan (default) görünüme sahiptir. Form üzerine Araç Kutusu panelinden sürüklenip bırakılan nesnelerle varsayılan görünümün tasarımı gerçekleştirilir. Herhangi bir şarta ya da duruma göre, aynı formun farklı görünümleri oluşturulmak istenirse bu işlem, Görünüm Yöneticisi panelinden gerçekleştirilir.

Aynı formun farklı görünümünü oluşturma işlemi;

- Herhangi bir duruma ya da formu görüntüleyecek kişiye bağlı olarak, varsayılan görünümde olmayan farklı bir nesne form üzerinde gösterilmek istendiğinde,
> *(Örn; Varsayılan görünümde “Tutar” alanı mevcut değildir. Akışta Muhasebe grubunun gördüğü formda “Tutar” isimli bir alana ihtiyaç vardır. Bu durumda Muhasebe grubu için yeni bir form görünümü oluşturularak “Tutar” alanı sadece bu görünüme eklenir. Böylece, varsayılan görünümü görüntüleyen kişiler “Tutar” alanını göremezken, Muhasebe grubundaki kişiler form üzerindeki “Tutar” alanını görebilir olurlar.)*

- Herhangi bir duruma ya da formu görüntüleyecek kişiye bağlı olarak, varsayılan form üzerindeki nesnelerin yerleri değiştirilmek istendiğinde,
durumlarında tercih edilebilir.

:::caution UYARI

Mevcut görünümde form üzerinde bulunan bir nesne, duruma göre gizlenmek istenirse, bu nesnenin gizlendiği yeni bir görünüm oluşturmak yerine, ilgili şart sağlandığında o nesneyi gizleyen bir kural, **[Kural Yöneticisi](./rule-manager.md)** panelinden tanımlanmalıdır.

:::

Görünüm alanından “Görünüm Yöneticisi” paneli aktif edildiğinde, henüz başka bir görünüm oluşturulmamışsa bu alanda default(varsayılan) görünümün kaydı mevcuttur.

![Görünüm Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5b3d6818-e177-4f6c-86a7-fc73d8d5329d)

Default görünüm kaydının yanında beliren detay kısmına tıklandığında, **“Düzen”** ve **“Çoğalt”** seçenekleri belirir.

**Düzen** alanına tıklandığında, görünümün adı ve açıklamasının düzenlenebildiği bir pencere açılır.

**Çoğalt** alanına tıklandığında ise, ilgili görünümün bir kopyası yeni görünüm olarak oluşturulur. Mevcut görünümde bulunan tüm form nesneleri, çoğaltılan kopya görünümde de mevcuttur. Bu seçenek; iki görünüm arasında çok fazla fark olmadığı durumlarda, yeni görünümü sıfırdan oluşturup ana görünümdeki nesneleri tek tek yeni görünüme eklemektense, ana görünümün aynısından kopya oluşturup ufak değişikliği kopya görünüm üzerinde gerçekleştirmek için kullanılır.

Default görünümde form üzerinde TextBox ve MaskInput nesneleri bulunsun;

![Görünüm Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0bfe15ea-dc84-461a-bb6c-2b602bc71915)

Formun, “Kontrolcü” isimli yeni bir görünümünü oluşturalım. Bu görünümün, default görünümden tek farkı mevcut form nesnelerine ek olarak formda bir adet ComboBox nesnesinin olması olsun. Default görünüm kaydının detaylarından “Çoğalt” butonuna tıklanarak “default_copy_1” isimli, default görünüm ile aynı form alanlarına sahip yeni bir görünüm oluşturulur.

![Görünüm Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada707eefd-9a80-4cdb-8dfb-5eabadef1123)

Yeni görünüm seçili iken Araç Kutusu panelinden forma 1 adet ComboBox nesnesi eklenir.

![Görünüm Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5a22ce3-1f03-4ea2-8d12-1c9413e65e65)

Kopya ile oluşturulan “default_copy_1” isimli görünümün detaylarından “Düzen” seçeneğine tıklanarak, görünüme yeni Ad ve Açıklama metinleri girilir.

<div style={{textAlign: 'center'}}>

![Görünüm Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f207bb0-d9d0-4db3-b775-c444b3aeada1)

</div>

Böylece formun farklı 2 adet görünümü oluşturulmuş olur.

![Görünüm Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6e02b95-aa37-4e42-bce5-7f71a3aa78de)

Formun farklı görünümleri, mevcut görünüm kopyalanarak oluşturulabileceği gibi sıfırdan bir form görünümü olarak da oluşturulup tasarlanabilir. Bunun için Görünüm Yöneticisi panelinde bulunan **“Yeni Görünüm Oluştur” (+)** butonuna tıklanır. Yeni görünüm oluştur butonuna tıklandığında Görünüm Yöneticisi panelinde **“view1”** isimli yeni boş bir form görünümü açılacaktır.

![Görünüm Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0cd36251-4162-4081-8730-60dc997e6e8e)

Formun farklı görünümünde bulunan herhangi bir nesne yeni oluşturulan görünüme, nesne gezgini panelinden sürüklenip bırakılarak dahil edilebilir. Örneğin default form görünümünde aşağıdaki nesneler olsun.

![Görünüm Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b2879dd-5e8d-4f3f-9010-5ebdea1da7f9)

View1 görünümünde de default görünümdeki Password1 ve Etiket nesneleri gösterilmek istenirse, view1 görünümü seçili iken Nesne Gezgini paneline geçilir ve ilgili nesneler sürükle bırak yöntemi ile forma eklenebilir. Böylece başka görünümde var olan nesneler diğer görünümde de gösterilmiş olur.

![Görünüm Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a0c0910-a0d7-44cb-9496-8443cbe75fe6)

![Görünüm Yöneticisi Paneli](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37d8a0a4-9f9b-40e6-83bd-227cc82866a4)

Görünümde aktif edilen nesne ilgili görünümden kaldırılmak istenirse, Nesne Gezgini panelindeki nesne detayından, **“Görünümden Sil”** seçeneği ile kaldırılabilir. Bu seçenek seçilirse ilgili nesne sadece o görünümden kaldırılacaktır. Nesne, aktif olduğu diğer görünümlerde görünmeye devam eder.

Eğer nesne gezgininden bir nesnenin detayına girilip **“Sil”** seçeneğine tıklanırsa nesne direkt olarak formdan kaldırılır. Dolayısıyla formun sahip olduğu tüm görünümlerden bu nesne silinmiş olur.

Formun farklı görünümleri;

- Formu açan kişiye göre görünüm değiştirilmek istendiğinde,
- Akışın farklı adımlarında kişi ya da gruplara farklı form görünümleri gösterilmek istendiğinde,
- Kural Yöneticisi panelinde belirlenen herhangi bir şarta göre form görünümü değiştirilmek istendiğinde,
- Bilgilendirme maillerinde ya da formun pdf görünümünde özel alanların olduğu form görünümü gösterilmek istendiğinde gibi durumlar için kullanılır.

Akış nesnelerinde doküman seçim özelliği bulunan nesnelerde (Doküman nesnesi, Pozisyon nesnesi, Pozisyon Grubu nesnesi, Bilgilendirme nesnesi gibi) formun hangi görünümü nesnede gösterilmek isteniyorsa onun da seçimi yapılabilmektedir.