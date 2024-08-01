# DENETİM SORUSU TANIMLAMA

Denetim modülünde 2 farklı türde denetim gerçekleştirilebilir. Sorular ve cevapların bulunduğu bir denetim gerçekleştirilebilir veya soru bulunmayan yalnızca bulguların girileceği bir denetim gerçekleştirilebilir. Soru sorulacak ve cevap verilecek olan denetimler için ik olarak sisteme denetim sorularının tanımlanması gerekmektedir.

Denetimde sorulacak olan soruların sisteme tanımlanması için ilk olarak Sistem Altyapı Tanımları > Denetim Faaliyetleri > Soru Havuzu sayfası açılır. Açılan sayfada "Yeni" butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Soru%20Havuzu-5aac18e3-2131-4fd1-8b66-1574d0db4c5b.png)

Soru kısmında bulunan TR alanına soru metni türkçe olarak girilir. Eğer bu soru farklı diller için de kullanılacak ve sorulacak ise ilgili sorunun diğer diller için karşılıklarının da doldurulması gerekmektedir. Beklenen cevap alanına ise ilgili soru sorulduğunda denetçiden beklenen bir cevabınız bulunuyor ise bu cevap yazılmalıdır, eğer beklenen bir cevap bulunmayacak ve seçenekli bir soru tarzı kullanılacak ise boş geçilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Puan%20Seçimi-f8e22193-57ae-4507-8bf4-8903b3f075f6.png)

Soru eklemesi yapılırken Durum kısmının aktif olduğu kontrol edilmelidir. Eğer puanlı soru tanımlanacak ise puan sisteminin nasıl olacağı belirlenir. 

Soru --> Soruya verilecek olan cevaba göre puanlama yapılmasını sağlar.

Seçenek --> Seçenekli bir soru ise ilgili soru için seçilecek olan seçeneğe verilen puana göre puanlama yapılmasını sağlar.

Kontrol Noktası --> Soru için kontrol noktası / noktaları bulunuyor ise kontrol noktalarına göre puanlama yapılmasını sağlar.

Bu sorudan alınabilecek olan minimum puan ve maksimum puan da belirlenmektedir. Eğer seçenekli veya kontrol noktalı soru tanımlanacak ise sorudan alınabilecek maksimum puanın seçenekten veya kontrol noktalarından alınabilecek olan maksimum puana eşit olması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Soru%20Havuzu%202-4f7ea073-1af1-44c9-88c2-0a43c3a4e617.png)

Eğer bir soru seçenekli olacak ise ilgili seçeneklerin soruya eklenmesi gerekmektedir.  Eğer ilgili soru için seçenek seçimi zorunlu tutulacak ise "Seçenek Zorunlu" alanının işaretlenmesi gerekmektedir.

Bir seçenek eklenirken ilgili seçeneğin seçilmesi halinde sistem tarafından zorunlu tutulmasını istediğiniz veya istenmeyen durumlar bulunuyor ise bu durumların sağ kısımdan seçilmesi gerekmektedir. 

Varsayılan --> İlgili seçeneğin denetim gerçekleştirme sırasında varsayılan olarak seçili gelmesini sağlar.

Kontrol Noktası Zorunlu --> İlgili seçeneğin seçilmesi durumunda kontrol noktası seçiminin zorunlu tutulmasını sağlar.

DÖF Zorunlu --> İlgili seçeneğin seçilmesi halinde sorudan DÖF açılmasının zorunlu tutulmasını sağlar.

Aksiyon Zorunlu --> İlgili seçeneğin seçilmesi halinde sorudan Aksiyon açılmasının zorunlu tutulmasını sağlar.

DÖF Açılamasın --> Seçeneğin seçilmesi durumunda ilgili sorudan DÖF açılmak istenir ise ilgili DÖF'ün açılamamasını sağlar.

Aksiyon Açılamasın --> Seçeneğin seçilmesi durumunda ilgili sorudan Aksiyon açılmak istenir ise ilgili Aksiyonun açılamamasını sağlar.

Cevap Zorunlu --> İlgili seçeneğin seçilmesi durumunda denetçinin bu soru için cevap girmesinin zorunlu tutulmasını sağlar.

Eğer bir soru için birden fazla seçeneğin aynı anda seçilebilir olması gerekiyor ise Birden fazla seçilebilir kutucuğu işaretlenmelidir.

Bu örnek için Evet seçeneği seçildiğinde DÖF açılamasın ve Aksiyon açılamasın koşulları eklenmiştir. 
Kısmen seçeneği için Aksiyon açılsın koşulu eklenmiştir. 
Hayır seçeneği için ise Kontrol Noktası Zorunlu ve DÖF açılsın koşulları eklenmiştir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Soru%20Havuzu%203-9ef83a4f-3c02-407a-9bf2-4c94ac599df1.png)

Kontrol noktaları tanımlanırken bir seçeneğin seçimine istinaden veya kontrol edilmesi istenen alanlar için tanımlanabilir. Kontrol noktaları için de seçeneklerde olduğu gibi yalnızca bir tanesi seçilebilir veya birden fazla seçilebilir. Birden fazla seçilebilir işaretlendiği durumda ise hesaplama yönteminin seçilmesi gerekmektedir. 

Toplama -->  Seçilen kontrol noktalarından alınan puanların toplanmasını sağlar.

Ortalama Alma --> Seçilen kontrol noktalarından alınan puanların toplanarak toplam kontrol noktası sayısına bölünerek ortalamasının alınmasını sağlar.

En Yüksek Değer --> Seçilen kontrol noktalarından alınacak en yüksek puanın alınmasını sağlar.

En Düşük Değer --> Seçilen kontrol noktalarından alınacak en düşük puanın alınmasını sağlar.

Seçilmeyenlerin Toplamı --> Seçilmeyen kontrol noktalarının alınan puanların toplanarak alınmasını sağlar.

Soru tanımlanması sırasında gerekli alanlar doldurularak "Kaydet" butonuna tıklanır ve sorunun kaydedilerek soru havuzu içerisinde bulunması sağlanır.

