# DateTimeBox Tarih Alanların Kaybolması

DateTimeBox nesnesinin form üzerinde alanlarının kaybolması,nesnenin içerisinde yazan değerlerin silenmesi ve nesnenin anlık readonly olma problemi için aşşağıdaki iletilen çözüm yöntemi uygulanabilir:

DateTimeBox nesnesi tarih alanları form üzerinden kaybolursa , ilgili alanın bozulması için eBA'nın
BimserCozum\eBA\Languages klasörü içerisindeki dil xml'i dışarıdan müdahaleyle bozulmaya uğramıştır.

Sisteme hangi dil ile giriş sağladığınızda problem yaşıyorsanız eBA'nın bulunduğunuz versionun default dil xml'ini içeriye aktarılıp problemin çözümünü sağlayabilirsiniz.

