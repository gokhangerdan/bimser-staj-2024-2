# BEAM GİRİŞ EKRANI RENK ÖZELLEŞTİRMESİ

Beam uygulaması üzerinden, giriş ekranındaki geçişli kırmızı ve daha koyu kırmızı renk yerine, istenilen başka iki rengi geçişli şekilde ayarlayabilirsiniz.


Bu işlem için uygulamadaki Sistem > Sistem Parametreleri menüsünü açın. "Anahtar Değer" alanında "WebUISettings.Style.LoginGradient.Color" filtrelemesi yaptığınızda, karşınıza iki adet sistem parametresi çıkacak. Bu satırların "Değer" alanlarında HTML renk kodları göreceksiniz.


"WebUISettings.Style.LoginGradient.Color1" parametresinin karşısındaki renk kodu, giriş ekranındaki orta kısımın rengini temsil eder.


"WebUISettings.Style.LoginGradient.Color2" parametresinin karşısındaki renk kodu ise, giriş ekranındaki kenar kısımların rengini temsil eder.


Bu iki renk kodu değerini istediğiniz renklerin HTML renk kodları ile değiştirip üst taraftaki "Uygula" butonuna tıkladığınızda uygulama ayarları kaydedilecektir. Giriş ekranına döndüğünüzde, giriş panelindeki standart geçişli kırmızı arka plan rengi yerine, parametrelerde ayarladığınız iki rengi "ikinci renk - birinci renk - ikinci renk" şeklinde geçişli halde göreceksiniz.


