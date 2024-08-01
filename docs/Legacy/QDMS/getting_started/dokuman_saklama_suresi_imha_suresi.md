# Doküman Saklama Süresi - İmha Süresi

Saklama Süresi: Klasör bazında sadece bilgi olarak gösterilir. Sürece herhangi bir etkisi bulunmamaktadır. Bu bilgiye işlenen süre tamamlandığında doküman iptal olmaz/silinmez. Entegre Yönetim Sistemi > Doküman İşlemleri > Klasör Tanımlama menüsünden ilgili klasörün içinde Klasör Ayarları kulakçığında bulunan Saklama Süresi(Ay) alanından beslenmektedir. 
Rapor olarak buradaki bilgiyi görmek için Raporlar > Doküman Özet Listesinin şablonu olan MasterSablon_TR şablonu SAT > BSAT > Konfg. Ayarları > Rapor Formatları Düzenleme menüsünden indirip, tag olarak ***SAKLAMASURESI*** tag'ini kolon olarak ekleyip kaydettikten sonra aynı dosya adı ile tekrardan Rapor Formatı Düzenleme menüsünden geri yükleyebilirsiniz. 
Doküman hazırlanırken klasörde hangi ay bilgisi varsa sistem raporda dokümanın ilgili tag'ine karşılık olarak o ay bilgisi basacaktır.

İmha Süresi/Sorumlusu: Doküman bazında, dokümanı iptal etmek veya silmek için bilgi amaçlı tutulan bir alandır.Sürece herhangi bir etkisi bulunmamaktadır. Bu bilgiye işlenen süre tamamlandığında doküman iptal olmaz/silinmez.
 Bu alanlar, SAT > BSAT > Konfg. Ayarları > Dil Ayarları menüsünde Doküman Modülü için Adı kolonundaki lblIMHASURESI ve lblIMHASORUMLUSU alanlarından beslenmektedir. İlgili parametrik alan adları tanımlı olduğunda;
Doküman hazırlama aşamasında Doküman Bilgileri kulakçığında bu iki alana tanımladığınız adlar, alt tarafta gözükecektir. Sistem imha süresini, dokümanı hazırladığınız klasörün klasör ayarlarında bulunan Saklama Süresi(Ay) alanından çekmektedir. Hazırlama aşamasında değiştirilebilir. 
Ayrıca dokümana girilen bu bilgi, Doküman Özet Listesinde gösterilebilir. MasterSablon_TR şablonunda tag olarak ***IMHASURESI*** tag'ini kullanabilirsiniz.