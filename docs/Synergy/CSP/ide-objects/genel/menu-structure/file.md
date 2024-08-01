---
sidebar_label: Dosya
sidebar_position: 1
custom_edit_url: ""
---

# Dosya

Dosya başlığı altından; yeni proje ya da çözüm oluşturulabilir, mevcut proje ya da çözüm açılabilir, projeye dosya eklenebilir, yapılan değişiklikler kaydedilebilir, proje ya da çözüm kapatılabilir veya son işlem yapılan projeler listesinden hızlıca bir projenin açılması sağlanabilir.

![Dosya](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad17264d-8d37-425a-bc57-607ac2692b0e)

- **Yeni Boş Proje** : Geliştirme ortamında yeni bir proje oluşturmak için bu işlem seçeneğine tıklanır.

:::info BİLGİ

Yeni proje oluşturma adımları ile ilgili detaylı bilgi için **[Yeni Proje Oluşturma](ide-operations/create-new-project.md)** dokümanını inceleyiniz.

:::

- **Yeni Boş Çözüm** : Geliştirme ortamında yeni bir çözüm oluşturmak için bu işlem seçeneğine tıklanır.

:::info BİLGİ

Yeni çözüm oluşturma adımları ile ilgili detaylı bilgi için **[Yeni Çözüm Oluşturma](ide-operations/create-new-solution.md)** dokümanını inceleyiniz.

:::

- **Çözüm Aç** : Geliştirme ortamında daha önceden oluşturulmuş bir çözümü, arayüzde açmak için kullanılır.

:::info BİLGİ

Sistemde mevcut bir çözümü açma adımları ile ilgili detaylı bilgi için **[Çözüm Açma İşlemi](ide-operations/open-solution.md)** dokümanını inceleyiniz.

:::

- **Proje Aç** : Geliştirme ortamında daha önceden oluşturulmuş bir projeyi, arayüzde açmak için kullanılır.

:::info BİLGİ

Sistemde mevcut bir projeyi açma adımları ile ilgili detaylı bilgi için **[Proje Açma İşlemi](ide-operations/open-project.md)** dokümanını inceleyiniz.

:::

- **Dosya Ekle** : Geliştirme arayüzünde bir proje açıkken, proje adına tıklandığında bu seçenek aktif hale gelir. Ya da proje adına sağ tıklandığında gelen “Yeni Öge” seçeneği ile de bu alana erişilebilir. Dosya Ekle seçeneği, seçilen projeye dosya eklemek için kullanılır. Sistemdeki bir projeye eklenebilecek dosya tipleri;

    - TypeScript File (A blank TypeScript source file)
    - TypeScript JSX File (A blank TypeScript JSX source)
    - C# Class (An empty class declaration)
    - C# Controller Class (An empty controller class)
    - Style Sheet (Css)
    - Html (Html) şeklindedir. Projeye eklenmek istenen dosya tipi seçilip, dosyaya bir isim verilerek tamam denildiğinde, projeye, seçilen dosya tipinde, kodlamaya hazır bir dosya eklenmiş olur.

- **Kaydet** : O an üzerinde çalışılan proje ekranı üzerinde yapılan değişiklikleri kaydetmeye yarayan seçenektir. Proje içerisindeki herhangi bir ekran üzerinde değişiklik yapıldığında bu buton aktif hale gelir. Üzerinde değişiklik yapılan ekran kaydedilmeden, geliştirme arayüzünden çıkış yapılmak istendiğinde ya da değişiklik yapılan proje ekranı kapatılmak istendiğinde, “Yapılan değişiklikler kaydedilmedi, kaydetmek ister misiniz?” şeklinde uyarı mesajları ile kaydedilmeyen güncellemelerin kaybolmasının önüne geçilmeye çalışılır. Kaydet işlemi, Ctrl + S kısayol kombinasyonu ile de gerçekleştirilebilir.

- **Tümünü Kaydet** : İlgili çözüm içerisinde yer alan tüm projeleri, proje içerisinde yer alan tüm ekran ve dosyaları kaydetmek için kullanılan seçenektir. Çözüm ve proje içerisinde yapılan tüm değişiklikleri ve yapının son halini tek bir tuş ile kaydetmeye yarar. Tümünü kaydet işlemi, Ctrl + Shift + S kısayol kombinasyonu ile de gerçekleştirilebilir.

- **Farklı Kaydet** : Üzerinde çalışılan projeyi farklı bir isimle kaydetmeye yarayan seçenektir. Bu seçenek genelde aynı veya benzer yapıda başka bir proje daha oluşturulması gereken durumlarda, projeyi baştan tasarlamak yerine, mevcut projeyi farklı bir isimle sisteme yaratıp, düzenlemeleri bu yeni proje üzerinden yapmak için kullanılır. Veya mevcut projede değişiklik yapılacağı zaman, varolan proje üzerinde değil, var olan projenin farklı isimle oluşturulmuş kopyasında denemelerin yapılarak nihai yapı direkt asıl projeye uygulanabilir. Farklı kaydet işlemi ile, var olan projeye yeni bir isim ve sistemde kaydedileceği yeni dizin belirtilerek, birbirinden kayıt yeri ve proje adı olarak ayrılmış ama aynı yapıya sahip yeni projeler elde edilebilir.

- **Çözümü Kapat** : Geliştirme arayüzünde açık olan çözümü ve çözümün altında bulunan tüm proje ve bileşenlerini kapatmaya yarayan seçenektir.

- **Projeyi Kapat** : Geliştirme arayüzü üzerinde açık olan projeyi kapatmak için kullanılan seçenektir.

- **Son Dosyalar** : Son dosyalar alanında, son zamanlarda işlem yapılan projelerin dizinleri listelenir. Kişinin güncel projeleri, düzenleme tarihine göre burada sıralanır. Bu proje dizinlerinden birine tıklandığında ilgili proje, geliştirme arayüzünde açılmış olur. Son dosyalar alanının faydası, yakın zamanda üzerinde çalışılan bir projenin, Dosya -> Proje Aç -> gelen projeler arasından ilgili projeyi bul ve aç, işlemlerine gerek kalmaksızın, direkt seçilen projeyi açmak için kısayol oluşturmasıdır.