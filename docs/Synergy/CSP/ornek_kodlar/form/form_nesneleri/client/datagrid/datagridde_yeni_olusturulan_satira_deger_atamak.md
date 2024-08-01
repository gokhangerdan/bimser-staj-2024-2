# DataGrid'de Yeni Satır Oluşturulma Anında TypeScript ile Değer Atama

Bu dokümantasyon, DataGrid bileşeni üzerinde yeni bir satır oluşturulduğunda TypeScript kullanılarak değer atama işlemi için bir rehberdir.

## Başlarken

DataGrid içerisinde yeni bir satır oluştururken, `OnInitNewRow` event'ini kullanarak TypeScript tarafında belirli değerler atayabiliriz. Bu işlem özellikle yeni satıra varsayılan değerler vermek için faydalıdır.

### OnInitNewRow Event'i

`OnInitNewRow` event'i, DataGrid nesnesinde yeni bir satır oluşturulduğunda tetiklenir. Bu event'e bir fonksiyon atayarak, yeni satıra değer ataması yapabiliriz.

#### Örnek Event Kullanımı:
```typescript
async DataGrid1_OnInitNewRow(args: Controls.EventArgs.IInitNewRowEventArgs) {
    // Bu fonksiyon içerisinde yeni oluşturulan satıra değer ataması yapılabilir.
}
```

### Yeni Satıra Değer Atama

Yeni oluşturulan satır için değer atama işlemi `args.data` nesnesi üzerinden yapılır. Bu nesne üzerindeki ilgili kolon adı kullanılarak değer ataması gerçekleştirilebilir.

#### Tarih Ataması

`INSERTEDDATE` kolonuna şu anın tarihini atama örneği:
```typescript
args.data["INSERTEDDATE"] = new Date(); // Şu anın tarih ve saat bilgisini atanır.
```

Bu kod parçası, `INSERTEDDATE` adında bir kolona yeni Date objesi yaratarak, o anın tarih ve saat bilgisini atar.

### Örnek Kullanım

```typescript
async DataGrid1_OnInitNewRow(args: Controls.EventArgs.IInitNewRowEventArgs) {
    // Yeni satır için "INSERTEDDATE" kolonuna şu anın tarihini atayalım.
    args.data["INSERTEDDATE"] = new Date();
}
```

Bu örnekte, `OnInitNewRow` event'i ile tetiklenen fonksiyon içinde, yeni oluşturulan satırın `INSERTEDDATE` kolonuna JavaScript `Date` objesi ile o anın tarihi atanmıştır.

