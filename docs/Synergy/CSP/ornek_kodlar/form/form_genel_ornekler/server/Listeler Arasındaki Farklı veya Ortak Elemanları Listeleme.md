# Listeler Arasındaki Farklı veya Ortak Elemanları Listeleme

```csharp
    using System.Linq;

    list2.Except(list1).ToList() //list2'de list1'e göre farklı olanlar elemanlar
    list1.Intersect(list2).ToList()  //list1'de list2'de ki ortak elemanlar
```
