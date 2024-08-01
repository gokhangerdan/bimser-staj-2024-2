---
sidebar_label: Kavramlar
sidebar_position: 1
custom_edit_url: ""
---

# Kavramlar

## Proje Nedir?

Proje, belirli bir ihtiyaç doğrultusunda tasarlanan, ihtiyacın karşılanması için kullanıma sunulan, özelleştirilmiş işlem paketidir. Sistem içerisinde geliştirilen her proje, farklı iş gereksinimlerini yürütmek için, farklı dizayn ve kurgularla oluşturulan süreçleri ifade eder.

Projeler genel olarak, kullanıcı ön yüzünü oluşturan, veri girişi yapılabilen ve girilen verilerin görüntülenebildiği form yapılarından ve arka tarafta projenin işlem adımlarının yürütüldüğü iş akışı yapılarından oluşur.

Projeler, form, akış, form ve akış kısımlarına yazılan kodlar, referans dosyaları, klasörler ve farklı tiplerde (TypeScript File, TypeScript JSX File, C# Class, C# Controller, Css, Html) dosyalar barındırabilen yapılardır.

Geliştirilen proje yayınlanarak, içerisindeki form tasarımları, akış senaryoları, kod kontrolleri doğrultusunda kullanıma sunulmuş olur. Kullanıma sunulan projelerin oluşturduğu veriler, kullanılan veritabanı yapılarına kaydedilerek, sistem içerisindeki her bir iş sürecinin kontrolü, takibi ve yönetimi sağlanmış olur.

## Çözüm Nedir?

Çözüm, bir ya da daha fazla farklı projeyi barındırabilen yapıdır. Farklı projeler tek bir çözüm altında toplanabilir. Genel olarak aynı tip ve benzer işlevli projeleri, tek bir yapı altında gruplamak için kullanılır.

Çözüm derlendiğinde, çözümün altında bulunan tüm projeler derlenmiş olur.

## Form Nedir?

Form, projenin, web arayüzde kullanıcıların görebileceği ve etkileşime geçebilecekleri kısmıdır. Kullanıcılar, web arayüzde, form ekranlarındaki alanları doldurabilir, daha önceden doldurulan alanları görebilir, forma girilen verilerle ve formda seçilen değerlerle iş süreçlerini ilerletebilir ve yönetebilirler.

Formlar, her biri kendine has özelliklere sahip ve farklı kullanım amaçlarına yönelik geliştirilmiş form nesneleri ile tasarlanır. Form nesneleri, sürükle / bırak yöntemi ile formlara eklenir.

Aynı form için, farklı form görselleri dizayn edilebilir. Kullanıcı, pozisyon, ünvan, departman, yetki, mevcut akış adımı bilgisi, herhangi bir alanın değeri veya belirlenen başka bir durum baz alınarak, kullanıcıların görebileceği form görünümleri farklılaştırılabilir. Form görünümleri ve davranışları şarta bağlı olarak değiştirilip yönetilebilir.

Form yapısında, form nesneleri ile görsel düzenlemeler yapılan dizayn ekranı ile birlikte, formların ve form üzerindeki nesnelerin davranış, görünüm ve işlevlerinin yönetileceği, C#, Css ve TypeScript kodların yazılabileceği kod editör ekranları da bulunmaktadır.

## Akış Nedir?

Akış, projenin ilerleyeceği işlem adımlarının tasarlandığı kısımdır. İş akışı süreçleri, farklı işlem adımlarından oluşan, her işlem adımında farklı aksiyonların alınabileceği, onay mekanizmalarının kurulabileceği, belirli bir yaşam döngüsü içeren yapılardan oluşur. Bu süreç senaryoları, projenin akış kısmında tasarlanır ve yönetilir.

Form ekranlarının farklı kullanıcı ya da kullanıcıların aksiyonuna sunulması, kullanıcıların form üzerinde kendisine belirlenen aksiyonu alarak süreci bir sonraki adıma ilerletmesi ya da geri göndermesi, hatırlatma mekanizmaları kurulabilmesi, form tarafındaki bir veri ya da başka bir kaynaktan sağlanan veri ile akış senaryolarının değiştirilip akışın farklı adımlara yönlendirilmesi, bilgilendirme mesajları ve mail gönderimlerinin yapılabilmesi gibi birçok işlem, akış kısmında tasarlanır ve yönetilir.

Akış ekranında oluşturulabilecek tüm senaryolar, sürükle / bırak yöntemi kullanılarak akışa eklenebilen akış nesneleriyle dizayn edilir. Akış nesnelerinin her birinin kendine has özellikleri, kullanımları ve farklı kullanım amaçları mevcuttur. İhtiyaç duyulan süreç senaryosuna göre ilgili akış nesneleri kullanılarak akışlar tasarlanır.

Akışlarda geçen kullanıcılara ne zaman aksiyon isteği düştüğü, kullanıcıların bu aksiyonu ne zaman aldığı, hangi aksiyonu aldığı, akışın şuan hangi adımda olduğu vb. birçok kayıtlı veri kullanılarak performans raporları elde edilebilir. Süreçlerin izlenebilen ve takip edilebilen yol haritaları oluşturulmuş olur.

Akış yapısında, akış nesneleriyle işlem adımları oluşturulan dizayn ekranı ile birlikte, akış işleyişi sırasında yapılması gereken kodsal işlemlerin yönetilebileceği, C# kodlarının yazılabileceği kod editör ekranı da bulunmaktadır.

## Nesne Nedir?

Nesneler, belirli bir işlevi yerine getirmek için tasarlanmış, kullanım amacına yönelik özelleştirilmiş görsel geliştirme arayüzü elemanlarıdır.

Projenin, form dizayn ekranında form nesneleri, akış dizayn ekranında akış nesneleri kullanılmaktadır. Her bir nesnenin kendine has özellikleri ve olayları mevcuttur.

Geliştirilecek proje ihtiyacına göre gerekli olan nesneler, form ve akış tarafına sürükle / bırak yöntemi ile eklenerek konfigure edilir. Nesnelerin kendi özellik ekranlarındaki ayarları yapılarak ya da kod tarafında nesnelere erişim sağlanarak, nesneler yönetilebilir ve proje isterlerine göre çalışmaları sağlanabilir.

Geliştirme arayüzünde kullanılabilecek tüm nesneler ve özellikleri hakkında detaylı bilgi için **[Geliştirme Ortamı Nesneleri](../ide-objects/index.mdx)** başlığı altındaki dokümanları inceleyebilirsiniz.