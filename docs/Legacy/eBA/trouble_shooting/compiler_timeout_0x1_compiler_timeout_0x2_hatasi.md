# Compiler timeout 0x1 - Compiler timeout 0x2 hatası çözüm önerileri

1) Windows temp dizini altındaki dosyalar silinerek kontrol edilebilirsiniz.
	C:\Windows\Temp  veya problem devam ederse ilgili user temp klasörü  C:\Users\kullanıcınız\AppData\Local\Temp
	NOT: Eğer servisler bir user ile çalışıyorsa user temp kısmını kontrol edip siliniz.
2) Proje üzerinde detay tablo varsa, maximum row count değeri yüksek ise düşürülüp deneyebilirsiniz.
3) Dbde tablolar locklanmış olabilir. Bu kısmı kontrol edebilirsiniz.


