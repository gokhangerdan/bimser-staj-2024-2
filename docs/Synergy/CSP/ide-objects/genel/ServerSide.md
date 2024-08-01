# Server-Side(Sunucu Tarafı) Kodlama
Server-Side kodlama, web uygulamalarının sunucu tarafında çalışan kodların geliştirilmesi sürecini ifade eder. Bu tür kodlama, sunucu tarafında veritabanıyla etkileşim, iş mantığının yürütülmesi, kullanıcı isteklerinin işlenmesi ve dinamik içerik oluşturma gibi görevleri içerir..

Server-Side kodlama, bir sunucu tarafı programlama dili kullanılarak gerçekleştirilir ve sunucu tarafında çalışan bir web sunucusunda çalıştırılır. Sunucu tarafında çalışan kod, genellikle HTTP taleplerini işler, veritabanı sorgularını gerçekleştirir, verileri işler ve HTML, JSON veya diğer formatlarda yanıtlar üretir.

## Form'lar için Server-Side Kodlama
-   ![](https://docsbimser.blob.core.windows.net/imagecontainer/client-870fab56-b75d-45c0-abff-6fd9108f6e65.png)
1.  Server-Side kodlama yapılacak Form kırılımı açılır.
2.  Server kırılımı açılır.
3.  Yapılacak geliştirme türüne göre .cs veya .Controller.cs seçilir.
*  ![](https://docsbimser.blob.core.windows.net/imagecontainer/1-ca2af821-6397-478f-98d8-ade9c162732d.png)

    *   ## FormAdı.cs
        *   Form için geliştirilen tasarım nesnelerinin ve eventlerinin yönetimlerinin sağlanabileceği dosya formatıdır.
        - Örnek TextBox nesnesinine değer atamanması
        ```cSharp
           public void SetFullName()
           {
                string firstName = Session.User.FirstName;
                string lastName = Session.User.LastName;
                string fullName = firstName + " " + lastName; 
                TextBox1.Text = fullName;
           }       
        ```
        - Örnek bir TextBox nesnesinin değerinin değiştiğinde gerçekleştirilen eventin çalıştırılması
            1.  İlgili nesnenin özellikleri açılır.
            2.  Olaylar tabındaki Server bölümünde OnValueChanged eventi bulunur.
            3.  Bu event için bir olay oluşturulur.

                ![](https://docsbimser.blob.core.windows.net/imagecontainer/1-aafcd9fc-70e9-49d5-b7b0-dbb6226cb0ed.png)
            4. ```cSharp
                    void TextBox1_OnValueChanged(object sender, PropertyChangedEventArgs<string> e)
                    {
                        string newValue = e.NewValue;
                        string oldValue = e.OldValue;
                        if(newValue == oldValue)
                        {
                            ShowMessage("Bildilendirme !","TextBox1 içerisinde, önceki ve yeni değerler aynıdır.",AlertType.Info);
                        }
                        else
                        {
                            ShowMessage("Bildilendirme !", "TextBox1 içerisinde, önceki ve yeni değerler farklıdır.", AlertType.Info);
                        }
                    }
                ```