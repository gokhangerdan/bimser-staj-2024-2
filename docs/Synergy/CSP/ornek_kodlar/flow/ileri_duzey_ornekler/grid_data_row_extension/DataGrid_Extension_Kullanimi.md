
# Flow Tarafında DataGrid'ler İçin Yardımcı Extension Kullanımı

Bu dokümantasyon, Flow tarafında DataGrid elemanlarının çağırımı için sürdürülebilir bir yapı oluşturmak amacıyla kullanılan yardımcı extension metodunun nasıl oluşturulacağını ve kullanılacağını açıklamaktadır.

## Problem Tanımı

Flow tarafında DataGrid'in elemanlarının hücrelerine erişim genellikle index değerleri ile gerçekleştirilir. Ancak, bu yöntem DataGrid'de yapılacak değişikliklerden dolayı sürdürülebilir bir yapıdan uzaklaşır. Bu nedenle, hücrelere isimleriyle erişim sağlayarak daha sürdürülebilir bir yöntem oluşturabiliriz.

## Çözüm: Extension Method Kullanımı

DataGrid hücrelerine isimleriyle erişim sağlamak için bir extension method oluşturacağız. Bu sayede, hücrelere erişimi daha okunabilir ve sürdürülebilir hale getirebiliriz.

### Adımlar

1. **Extensions Klasörünün Oluşturulması:**

   Ana klasör yapısında `Extensions` isimli bir klasör oluşturun.

2. **GridDataRowExtension.cs Dosyasının Oluşturulması:**

   `Extensions` klasörü içerisinde `GridDataRowExtension.cs` isimli bir dosya oluşturun ve aşağıdaki sınıfı ekleyin:

    ```csharp
    using Bimser.Synergy.ServiceAPI.Models.Form;
    using System.Linq;
    using System;
    using Newtonsoft.Json;

    namespace ExampleProject1.Extensions
    {
        public static class GridDataRowExtension
        {
            public static GridDataRowCell GetCellByName(this GridDataRow gridDataRow, string name)
            {
                var cell = gridDataRow.Cells.FirstOrDefault(x => x.Name == name);
                if (cell is null)
                    throw new Exception($"GridDataRowExtension.Error, A cell named {name} could not be found!");
                return cell;
            }
        }
    }
    ```

3. **Flow Tarafında Extension'a Erişim:**

   Flow tarafında bu extension'a erişebilmek için, gerekli using ifadesini ekleyin:

    ```csharp
    using ExampleProject1.Extensions;
    ```

4. **Extension Method'un Kullanımı:**

   Bu extension method ile DataGrid hücrelerine isimleriyle erişim sağlayabilirsiniz. Örneğin:

    ```csharp
    var approverList = GridData.FromControl(Document1.Controls["dgApprovers"]);
    var currentApprover = approverList.Rows.First(x => x.GetCellByName("APPROVESTATUS").Value.ToString() == "Onaylanmadı");
    ```

### Karşılaştırma

**Extension Method Kullanarak Çağrım:**

```csharp
var approverList = GridData.FromControl(Document1.Controls["dgApprovers"]);
var currentApprover = approverList.Rows.First(x => x.GetCellByName("APPROVESTATUS").Value.ToString() == "Onaylanmadı");
```

**Extension Method Kullanmadan Çağrım:**

```csharp
var approverList = GridData.FromControl(Document1.Controls["dgApprovers"]);
var currentApprover = approverList.Rows.First(x => x.Cells[3].Value.ToString() == "Onaylanmadı !");
```

## Sonuç

DataGrid hücrelerine index ile erişim yerine, hücrelerin isimleriyle erişim sağlayarak daha sürdürülebilir ve okunabilir bir yapı oluşturabilirsiniz. Bu işlemi sıkça kullanmanız durumunda, extension method kullanarak kodunuzu daha modüler ve yönetilebilir hale getirebilirsiniz.
