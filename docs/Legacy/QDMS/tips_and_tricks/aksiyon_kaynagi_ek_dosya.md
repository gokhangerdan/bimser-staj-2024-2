# Aksiyon Kaynağına Göre Ek Dosya Zorunluğu

5.26 versiyonu ile birlikte istemiş olduğunuz aksiyon onay aşamalarında ana aksiyon özelinde veya aksiyon kaynağınıza göre ek dosya zorunluluğunu belirleyebileceğiniz alan uygulamamıza eklenmiştir. Bu özelliğin kullanılabilir olması için öncelikle ilgili alanı aktif hale getirmeniz ve SAT > AKSİYON > Aksiyon parametrelerinden 63 numaralı "(Ek dosyanın zorunlu olduğu statüler(1=Açma, 2=Gerçekleştirme, 3=Geciktirme, 4=Açılış Onayı, 5=Kapanış Onayı)" parametresinin değerini boş olarak kullanmanız gerekmektedir. İlgili parametre değerini boşalttıktan sonra SAT > BSAT > KONFİGÜRASYON AYARLARI > Dil Ayarları menüsüne geliniz Aksiyon modülünü seçtikten sonra başlıklar kısmındayken adı kısmına ekte(DilAyarları) ilettiğim gibi lblEkZorunluAsamalar yazınız ve değiştir butonu ile giriş sağlayınız. Değeri alanına ana aksiyon ve aksiyon kaynağı ekranında bu alanın görünücek ismini yazınız bizler Ek Dosya Zorunlu Statüler olarak tercih ettik ama bu tercih sizlere kalmıştır. Bu eklemeyi yaptıktan sonra ekte ilettiğim şekilde ana aksiyon ve aksiyon kaynağı menülerinde hangi onay aşamalarında ek dosyanın zorunlu olabileceğini seçebildiğiniz alan uygulamanıza eklenecektir. Sizler tercihinize göre ister ana aksiyonda hangi onay aşamasında ek dosyanın zorunlu olduğuna karar verebilir veya yine aynı ek dosya zorunluluğunu aksiyon kaynağı özelinde yapabilirsiniz. Sizlerin yapmış olduğu seçime göre ilgili onay aşamalarında ek dosya eklenmesi zorunlu olacak eğer kullanıcı işlem sırasında ek dosya eklemez ise sistem tarafından ek dosya eklemesi gerektiğine dair uyarı mesajı alır bilginize. Bu özelliği kullanabilmek için QMDS versiyonunuzun 5.26 veya daha yüksek bir versiyon olması gerekmektedir.




![](https://docsbimser.blob.core.windows.net/imagecontainer/1-f3a5122a-8360-4c71-9f88-b4ac50b270e1.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/2-43a425ca-026d-4c98-ab29-d2e90dbb59d6.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/3-7445cc27-c736-49fe-9254-2260869ffc9c.png)

