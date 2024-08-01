---
sidebar_label: Sık Sorulan Sorular ve Çalışma Mantığı
sidebar_position: 4
custom_edit_url: ""
---
# Sık Sorulan Sorular ve Çalışma Mantığı
<h1 style={{fontSize: '30px', fontWeight: 'bold', margin:'40px 0'}} align="center">Sık Sorulan Sorular</h1>

<h1 style={{fontSize: '20px', fontWeight: 'bold'}}>Soru 1: Güncel imza altyapısına geçen firmalar var mıdır? Yapılan geçişlerde herhangi bir sorun meydana geldi mi?</h1>
<p style={{fontSize: '16px'}}>Güncel E-İmza alt yapımızı kullanan müşterilerimiz mevcuttur. Şuan kullanımlarında bir problem yaşanmamaktadır.</p>

<h1 style={{fontSize: '20px', fontWeight: 'bold'}}>Soru 2: Güncel imza altyapısında sorun yaşamamak adına önlem almamız ya da bilmemiz gereken detaylar var mıdır?</h1>

Yeni E-İmza alt yapımızın çalışması için mutlaka Java  ve .NET Core 3.1’in sunucuda ve kullanıcı bilgisayarlarında kurulu olması gerekmektedir.

Kullanılan sucularin imza atma işlemi sırasında internet çıkış kısıtlarindan kaynakli erişim problemleri yaşanmaktadir. Server internete çıkabilmelidir. Burada problem imza işleminin tamamlanması aşamasında KamuSM apisinin farkli adreslere giderek sertifika iptal listesi kontrolü, sertifika doğrulama, imza kontrolü gibi işlemleri yapmasıdır. Bu adreslere server gidiş ve dönüş tam erişim yetkisi verilmeli. Whitecard olarak eklenmelidir.

Bu adreslerin listesini KamuSM'de bilmemektedir ve değişiklik gösterdiği icin tam listeyi bize verememektedir. Müşterilerden kontroller sirasinda elimizde aşağıdaki gibi bir liste oluşmuştur. Yeni adreslerde eklenebilmektedir. Güncel liste şu şekildedir;
<table >
    <tr>
        <th>IP</th>
        <th>Adres</th>
    </tr>
    <tr>
        <td>193.140.71.25</td>
        <td><a href="https://zd.kamusm.gov.tr" style={{color: 'blue'}}>zd.kamusm.gov.tr</a></td>
    </tr>
    <tr>
        <td>193.140.71.24</td>
        <td><a href="https://ocsp.kamusm.gov.tr" style={{color: 'blue'}}>ocsp.kamusm.gov.tr</a></td>
    </tr>
    <tr>
        <td>193.140.71.24</td>
        <td><a href="https://ocsp3.kamusm.gov.tr" style={{color: 'blue'}}>ocsp3.kamusm.gov.tr</a></td>
    </tr>
    <tr>
        <td>193.140.71.23</td>
        <td><a href="https://ocsp4.kamusm.gov.tr" style={{color: 'blue'}}>ocsp4.kamusm.gov.tr</a></td>
    </tr>
    <tr>
        <td>193.140.71.52</td>
        <td><a href="https://ocsp5.kamusm.gov.tr" style={{color: 'blue'}}>ocsp5.kamusm.gov.tr</a></td>
    </tr>
    <tr>
        <td>212.174.244.151</td>
        <td><a href="https://ocsp.turktrust.com.tr" style={{color: 'blue'}}>ocsp.turktrust.com.tr</a></td>
    </tr>
    <tr>
        <td>212.174.244.99</td>
        <td><a href="https://crl.turktrust.com.tr" style={{color: 'blue'}}>crl.turktrust.com.tr</a></td>
    </tr>
    <tr>
        <td>212.174.244.152</td>
        <td><a href="https://ts.turktrust.com.tr" style={{color: 'blue'}}>ts.turktrust.com.tr</a></td>
    </tr>
</table>
<p style={{fontSize: '17px', textDecoration: 'underline'}}>Dijital İmza hakkında yardımcı uzantılar: </p>

http://www.turktrust.com.tr/sil/TURKTRUST_Nitelikli_SIL_h4.crl <br/>
http://kamusm.bilgem.tubitak.gov.tr/

<p style={{fontSize: '17px', textDecoration: 'underline'}}>Bunların dışında, kullanılan imza kartına göre aşağıdaki linklere de izin verilmelidir. </p>

E-İmzaTR: http://ocsp.E-İmzatr.com <br/>
E-Tugra : http://ocsp.e-tugra.com/status/ocsp <br/>
e-Güven: http://ocsp2.e-guven.com/ocsp.xuda & http://sil.e-guven.com/ElektronikBilgiGuvenligiASGKNESIS6/LatestCRL.crl

<p style={{fontSize: '17px', textDecoration: 'underline'}}>WhiteCard verilmesi gereken Adresler :</p>
<p>*.kamusm.gov.tr <br/>
*.turktrust.com.tr <br/>
*.E-İmzatr.com <br/>
*.e-guven.com <br/>
*.e-tugra.com <br/></p>

<h1 style={{fontSize: '20px', fontWeight: 'bold'}}>Soru 3: Güncel imza altyapısına geçiş yapmamız durumunda stabil ve sorunsuz bir şekilde çalışacak mıdır?</h1>

Güncel imza altyapısı stabil çalışmaktadir. Geliştirme aşamasında işi asıl yapan <b>TÜBİTAK KamuSM</b>'den destek alınıp birlikte geliştirme yapılmıştır. İmzalama altyapısı sağlayan firmalar ürünlerini KamuSM altyapısını kullanarak geliştirdiler. Ürünümüzü geliştirirken ayni altyapıyı kullandığımız ve destek alma aşamasında KamuSM ile birlikte algoritmayı geliştirdiğimiz için diger imza uygulamalarıyla güvenlik, gizlilik ve kullanım olarak benzer yapıları geliştirdik. <b> Tek fark bu ürünün, Bimser’in kendi ürünü olmasıyla beraber tüm Bimser ürünlerine implemente edilebilmesidir.</b>

Dönem dönem sertifika konularında, imza atım aşamasında KamuSM isteklerinde erişim sağlanması gereken adresler olabilir. Bu tarz durumlarda sertifika konuları için yenileme ya da sertifika deposunda düzeltme sağlama işlemleri gerekli olabilmekedir. Erişim sorunları olduğu taktirde de network üzerinden gerekli çalışmaların yapılması gerekebilmektedir. Bu tarz konuların dışında imzalama altyapımız stabil ve sorunsuz olarak çalışmaktadır.

Yani sonuç olarak, ayni altyapi kullanıldiğı için imza sonuçlari ve doğrulama işlemleri KamuSM ve imzager uygulamasıyla aynıdır. Kullanılacak süreçlerde yapılacak tüm imzalama ayarlamaları yapıldıktan sonrasında sorunsuz şekilde imza işlemi gerçekleştirilebilir.

<h1 style={{fontSize: '20px', fontWeight: 'bold'}}>Soru 4: İmza sertifikalarımızın ve bilgilerimizin güvenliğini sağlayabilmekte misiniz?</h1>

Diğer imzalama altyapısı sağlayan firmalar gibi <b>TÜBİTAK KamuSM</b> üzerinden gerekli altyapı ve algoritmalar ile ürünümüzü geliştirdik. Güvenlik, gizlilik ve sertifika doğruluğu konularında diğer imzalama altyapısı sağlayan firmalar gibi aynı güvenceleri sunmaktayız.

<h1 style={{fontSize: '20px', fontWeight: 'bold'}}>Soru 5: İmza yazılımının -DSClient- üstünde hala geliştirme yapılmakta ve güncelleme almakta mıdır?</h1>

Şu an, 1 seneye yakın zamandır, 20 den fazla müşteri bu yapiya geçerek canlı olarak kullandigi için köklü değişiklikler tamamlanmıştır ve stabil bir 1.4.5 versiyonumuz vardir. Her yerde bu sürüm kullanılmaktadir. 

Ekstrem bi durumda güncel versiyon alınarak bir msi oluşturulmakta ve direkt çalıştırılarak kısa sürede güncelleme işlemi tamamlanabilmektedir. DSClient uygulaması farklı ihtiyaç ve tespit edilen sorunlar sebebiyle güncelleme alabilir.


<h1 style={{fontSize: '30px', fontWeight: 'bold', margin:'40px 0'}} align="center">Bimser Dijital İmza Çalışma Mantığı</h1>

Dijital imza uygulaması Tübitak'ın sunduğu ve İmza firmaları KamuSM Ma3api altyapısını kullanarak geliştirildi. Bu bağlamda KamuSM apinin açık uçlarına istek atan ve sonuçları alıp EBA.NET'e ileten bir web-api uygulamasıdır. 

Burada müşteri imza verisini koruyabilmek ve sertifika gizliliğini sağlayabilmek için algoritmayı şu şekilde geliştirdik; Öncelikle müşteri imza dongle ını kendi local bilgisayarına takıyor. EBA üzerinde imzalama isteğinde bulunmak için tarayıcıdan EBA.NET i açıyor. EBA.NET müşteri server da kurulu. Biz imza uygulamasını hem müşteri server ına hemde local makineye kuruyoruz. İlk aşamada imzala butonu tetiklendiğinde müşteri serverında initialize işlemi tetiklenerek imzalanacak verinin bir hash bilgisi alınıyor ve bu bilgi müşteri bilgisayarına iletiliyor. 2. Aşama olan sign işlemini müşteri bilgisayarında imza dongle ının kurulu olduğu yerde yani local makinede gerçekleştiriyoruz. Böylece müşteri sertifika bilgisini local makine dışında bir yere taşımıyoruz ve trafiğe sızıp bilgilerin alınmasına izin vermiyoruz. Daha sonra imza işlemi localde gerçekleştikten sonra belgesinin imzalı hash bilgisini alarak 3. aşama finalize aşamasında tekrar servera dönüp imzalı veriyi değiştiriyoruz. Belgenin hash bilgisinin gelip dönmesinin sebebi de belgenin tamamını gönderip performans kaybının önüne geçmektir. 

Bu algoritmayı geliştirme aşamasında Tubitak KamuSM'den destek alınmıştır ve güvenlik için yönlendirmeleri göz önüne alınarak uygulanmıştır. İmza geliştiren firmaların aynı algoritmayı kulladıkları KamuSM tarafından iletilmiştir.
 
Burada müşteri localinde eğer müşterinin kendi kök sertifikaları varsa eklemesi için kurulu olduğu adreste şu kısma ekleme yapabilir. Onun dışında diğer genel sertifikaları 'sertifikadeposu.svt' nin içerisindeki adreslerden otomatik çekmektedir ve belirli aralıklarla güncellemektedir.

<p align="center">
    <img src="https://docsbimser.blob.core.windows.net/imagecontainer/ds_sss_1-06eeaf4a-0984-463e-bbb3-9d4fed7cebe2.png" alt="Bimser Çözüm" style={{border: '3px solid #dee0df', borderRadius:'15px', boxShadow:'3px 5px #dee0df'}}/>
    <img src="https://docsbimser.blob.core.windows.net/imagecontainer/ds_sss_2-71c5a0b3-c871-4240-9f79-7ff7456f5402.png" alt="Bimser Çözüm" style={{border: '3px solid #dee0df', borderRadius:'15px', boxShadow:'3px 5px #dee0df'}}/>
</p>

Mobil imza işleminde ise dijital imzadaki gibi imza bilgisini tutan dongle'a ihtiyaç yoktur. Tarayıcıdan belgeyi açtığımızda mobil imza at işleminden sonra kamusm; turkcell, vodafone veya avea mobil imza sunucularından mobil hattının sertifika bilgisini alır. Initialize aşamasında Bimser'in mobile-gateway suncusuna sertifika ile imza isteği atılır. Sonrasında doğrulama amaçlı telefona istek gelir. Fingerprint adında bir doğrulama kodu gelecektir. Doğrulama işlemi yapıldıktan sonra 'FinalizeSigning' metodu imzalı belgeyi ugulamaya gönderir. 

<p style={{fontWeight:'bold'}}>Mobil imza içinde aynı elektronik imza uygulamamızın kurulu olması gerekmektedir.</p>

İmza uygulamasının anlık logları kurulu olduğu server ve müşteri localinin kurulum dizinine yazılmaktadır. EBA.NET kendi içerisinde de hata loglarını tutmaktadır. 
 
Uygulamanın çalışması için EBA.NET dışında, .NET Core 3.1, Java 8 ve imza uygulamasının (DS-Client) kurulu olması gerekmektedir. DS-Client kurulum dosyasının üzerinden kurulum yapıldığında imza uygulaması Windows servisi olarak kurulur ve çalışır. Uygulama kaldırılmak istendiğinde ise kurulum klasörleri ve Windows servis kendiliğinden silinir. 



