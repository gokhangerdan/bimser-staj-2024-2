# Asset'de Bulunan Dosyaların Bağlantısına Ulaşmak

```const logoAddress = this.fetch.BaseUrl.replace(/\/api$/, "/asset/").concat("bimser-logo.png");```

Burada API'ler için olan bağlantı değiştirilerek asset klasörüne çevrilmiştir. Ardından ulaşılmak istenilen dosyanın/görselin ismi uzantısıyla beraber birleştirilerek bir bağlantı adresi oluşturulmuştur.

