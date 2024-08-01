---
title: "Form Bilgileri Bölümü"
sidebar_position: 1
---

# Form Bilgileri Bölümü
Öncelikle formun uygulama sırasında görünecek başlık ismi değiştirilir. Bunun için form üzerinde çift tıklandığında ekranın sağ tarafında açılan Özellik Görüntüleyici Panelinden **Caption** alanı “Masraf Beyan Formu” olarak güncellenir.
![masraf beyan form caption](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20beyan%20form%20caption-a52ddb42-4583-4ed3-9763-ce1f721389c3.png)

Form farklı bölümlerden (Form Bilgileri, Talep Eden Bilgileri, Masraf Detay Bilgileri gibi) oluşacağı için, karmaşık görünmemesi açısından, bölüm bilgileri Label nesnesi kullanılarak belirtilebilir. Böylece hangi nesne hangi bölüme ait ise ilgili bölüm başlığı altında bulunmuş olur.
![form bilgileri label](https://docsbimser.blob.core.windows.net/imagecontainer/form%20bilgileri%20label-7f7acef7-4bbe-44c4-9eea-0aa59fd390ec.png)

Form bilgileri bölümünde, **Belge Numarası** ve **Belge Tarihi** alanları bulunacaktır. Forma ait bu iki bilginin de form yaratıldığında sistem tarafından otomatik dolması için DocumentMetadata nesnesi kullanılır.

**Belge Numarası** alanı için, DocumentMetadata nesnesi forma eklenir ve özelliklerindeki **Select Metadata Type** alanından **Id** seçeneği seçilir.
![belge id](https://docsbimser.blob.core.windows.net/imagecontainer/belge%20id-4141e540-fc86-4f26-8168-e5aa2551a259.png)
Belge Numarası alanına istenilen formatta bir değer atanabilmesi için **Form** üzerindeki boş bir alana çift tıklanır ve sağ tarafta açılan form özelliklerinden **Identity Format** özelliğinin yanındaki üç noktaya tıklanır.
 
Daha önceden oluşturulmuş mevcut bir formatı seçmek için **Choose a templates here** bölümünden seçim yapılabilir veya yeni bir format oluşturmak için **Define new one and use** özelliği seçilebilir. 

Masraf Beyan Formunun Belge numarası alanı için **MB-{%year%}-{{cccc}}** şeklinde bir format belirlenebilir. Bu formattaki year alanı güncel yılı, cccc ise 4 haneli bir sayacı tanımlar. 

Doküman ilk oluşturulduğunda sayaç değerine “1” olarak verilen **Counter Start Value** alanında belirlenen değer atanır. Doküman her oluşturulduğunda sayaç, yine “1” olarak tanımlanmış **Counter Increment Value** değerinde artacaktır.
![masraf beyan format](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20beyan%20format-b81e93cf-4885-4f00-8cde-a4c8d3381b63.png)

**Belge Tarihi** alanı için, DocumentMetadata nesnesi forma eklenir ve özelliklerindeki Select Metadata Type alanından dokümanın oluşturulma tarihi veren **CreateDate** seçeneği otomatik olarak seçili gelir.
![belge tarihi](https://docsbimser.blob.core.windows.net/imagecontainer/belge%20tarihi-aba7b485-c889-4c6c-8fe3-ceba9b109520.png)
:::info BİLGİ
Bir Formda en fazla 2 DocumentMetadata nesnesi olabilmektedir. Bu nesneden 2 kez eklendiğinde, Metadata Type seçeneklerinde biri Id diğeri createDate olmak üzere sadece iki alan bulunduğu için son eklenen nesnedeki bu özellik otomatik seçili hale gelir ve nesnelerden biri kaldırılmadan bu özelliklerde değişime izin verilmez.
:::
