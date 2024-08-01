# Yüksek Boyutlu Excel Dokümanlarının Viewer'da Görüntülenmesi

## GİRİŞ

Viewer uygulamasındaki Html5Viewer, çok fazla veri içeren excel dosyalarında, verinin html'e dönüştürülüp aynı sheet üzerinde gösterilmeye çalışılması yüzünden timeout'a uğruyor ve belgeyi açamıyor durumdaydı. Bu sebeple "RowsCountPerPage" parametresi oluşturulmuş ve ilgili parametre ile bu excel dosyalarının belli bir sayıda veri ile sınırlı sheet'lere bölünerek açılabilmesi sağlanmıştır. Aynı zamanda şunu da unutmamak gerekir ki, bu dosyaların açılması süreci farklı etkenlere de bağlı olduğu için yapılan geliştirme ilgili dosyaların sınırsız boyutlarda açılabilmesini sağlamaz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/html5viewerexcel-3a6101fe-157d-4312-9538-1d0e8968552b.png)


## Parametrenin Eklenmesi

eBA DM'de (system/settings/dm) bulunan Viewers.config dosyasında excel uzantılarında Html5Viewer veya Html5ViewerExcel seçilip "RowsCountPerPage" parametresi eklenmelidir. Bu tür dosyalarda her sheet üzerinde kaç satır gösterileceği bu parametre ile belirlenebilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/viewers_config-055881c2-f0b8-42de-b162-f33fee747e58.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/viewers_config_ext-d6c5b7bf-6b7d-4251-8ca2-1f6408d56c7d.png)

Aynı zamanda bu parametre ile sheet'lere bölünen veriler için ön yüklü olarak kaç sheet'in html'e dönüştürüleceği "PreloadPagesCount" parametresi ile belirlenebilir. Bu parametrede verilen sayı kadar sheet html'e dönüştürülür ve bundan sonraki sheet'ler üzerine tıkladıkça anlık olarak dönüştürülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/viewers_config_pre-48493408-a811-40c4-ac48-4aac6771b1a7.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/viewer_temp-f4028ec7-0a19-4605-acf2-b341a932abcf.png)

