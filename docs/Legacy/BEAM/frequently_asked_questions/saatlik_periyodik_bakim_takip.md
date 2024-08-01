# Saatlik Periyodik Bakımları Uygulamada Nasıl Takip Edebilirim?

Saatlik periyodik bakımları da diğer zamana bağlı periyodik bakımlar gibi uygulamada takip etmek için;
1.	Saat tanımlı bir periyodik bakım zaman birimi tanımlanmalıdır.

2.	Tanımlanan bu periyot biriminin çarpan değeri 1 (bir) den küçük olmalıdır. Örneğin; 1/24=0,041 olabilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/saatlik_per_bak_takip_pic1-3deb9bc3-cca6-4fc8-9afa-6a32be2af033.png)

3.	İlgili varlık için periyodik bakım tanımı yaplır ve tanımda periyot birimi olarak birinci adımda tanımlanan saat birimi seçilir.
Yukarıdaki üç adımda anlatılan şekilde tanımlama yapıldığı zaman kurgunun düzgün çalışması için;
1.	İş emrilerinin zamanında oluşması için sunucu üzerinde çalışan periyodik bakım iş emri oluşturma servisinin kontrol süresi muhakkak periyodik bakım tanımındaki bakım periyodundan kısa olmalıdır. Örneğin; bakım periyodumuz 2 saat ise servisin kontrol süresi 30 dakika olmalıdır. 
2.	Periyodik bakımlardan iş emri oluştuğu zaman, oluşan iş emri zamanında kapatılmalıdır yoksa yeni iş emri oluşmayacaktır.


