# TreeView

TreeView nesnesi statik ve dinamik şekilde kullanımları bulunan bir nesnedir.

Dinamik tipte kullanım için bir rest bağlantısına ihtiyacınız vardır.

Sonrasında nesne özelliklerinden ilgili alanları doldurmalıdır. (Value Expression, Display Expression, Hierarchy Type, Children Key...)

Statik tipte kullanım için ise, Items kısmından itemlar eklemelidir. Her item'ın özellikleri içinde Children Items bulunur. Buradan da o item'ın alt itemları eklenir. Böylece kırılımlı bir hiyerarşik liste yapısı elde edilmiş olur.

TreeView'de listenin elemanları form üzerinde direkt görüntülenir. İstenilirse itemlara tıklanarak alt itemlar görüntülenir.

```
ID	PARENTID	VALUE
1	Null	         Text
2	Null	         Text2
3	1	         Text3

```

Treeview olarak yukarıdaki tabloyu düşünürsek;

```
Text
    Text3
Text2

```

şeklinde kırılım olması demektir.


*Ana kırılımların parentidleri null olmalıdır.

*ID ve ParentID verileri int tipinde olmak zorundadır.

Aşağıda Treeview kullanımı için örnek proje görselleri bulunmaktadır.



![](https://docsbimser.blob.core.windows.net/imagecontainer/treeview-sql-71c4fe05-aa90-4b3b-9054-590f6373e590.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/treeview-1-a41f6659-9927-457f-aeb6-51bbb702e54f.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/treeview2-3fef0c15-748b-4006-a0c4-bb897211f70a.png)

Server tarafında da TreeView nesnesine itemler eklenebilirsiniz:

```
TreeView treeView = new TreeView();

            //ilk item
            TreeViewItem item1 = new TreeViewItem();
            item1.Key = "Item1";
            item1.Text = "Item1Text";

            //ilk item in child i
            TreeViewItem item1child1 = new TreeViewItem();
            item1child1.Key = "Item1Child1";
            item1child1.Text = "Item1Child1Text";

            item1.Children.Add(item1child1);

            //ikinci item
            TreeViewItem item2 = new TreeViewItem();
            item2.Key = "Item2";
            item2.Text = "Item2Text";

            //ikinci item in child i
            TreeViewItem item2child1 = new TreeViewItem();
            item2child1.Key = "Item2Child1";
            item2child1.Text = "Item2Child1Text";

            item2.Children.Add(item2child1);


            treeView.TreeItems.Add(item1);
            treeView.TreeItems.Add(item2);

```

