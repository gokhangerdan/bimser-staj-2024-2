# eBA DateTime Nesnesi  Örnekleri

## DateTime Gün Farklı Alma

Textbox tipi tarih olarak seçinlen alanlara text şeklinde ulaşamazsınız. 
Tarih olarak seçilen textbox nesne tipi eBADatetimeBox olarak değişmektedir.
İki tarihin çıkarılması TimeSpan nesnesi olarak sonuç döner.
Bunun için C# timespan nesnesini incelemeniz gerekmektedir.
Örnek olarak timeSpan nesnesinin TotalDays değişkenini çağırdığınızda double olarak iki tarih arasındaki gün farkını döner.



```
//EbaDateTimeNesnelerinini Text1 ve Text2 olduğu varsayılmıştır.
if (Text1.IsValid && Text2.IsValid)
{  
    ToplamSure.Text = (Text2.Value - Text1.Value).TotalDays.ToString();
}
```

İki tarih arasında gün farkının alınması detaylı örneği


```
   DateTime dtBaslangic =  DateTime.Parse(txt_GirisTarih.Text);

            DateTime dtBitis =  DateTime.Parse(txt_CikisTarih.Text);

            TimeSpan zaman = new TimeSpan(); 

            zaman = dtBitis - dtBaslangic;                 

            int gunFark =   Convert.ToInt32(zaman.TotalDays) ;
```

## DateTime Yıl Hesaplama

```
DateTime myDate =  DateTime.ParseExact(Text1.Text, "d.M.yyyy HH:mm:ss", CultureInfo.InvariantCulture);       //d.M.yyyy HH:mm:ss   çevirdiğimiz stringin formatı      
TimeSpan ts = Text2.Value - myDate;              
ShowMessageBox((ts.TotalDays / 365.25).ToString());
```

## DateTime  İki Tarih Arasındaki Farkı Saniye/Milisaniye Dönüştürme

Bu örneği baz alarak TimeSpan ile Günü,Saate,Saati dakikaya veyahutta tersine bir yapı olarak kullanılabilir.

```
//Metin6-Metin8 eBADatetimeBox

 TimeSpan ts = Metin6.Value.Subtract(Metin8.Value);  // TimeSpan nesnesi içinden ulaşabiliyoruz bundan dolayı  iki metnin farkını alıp ts değerine alıyoruz.
              Metin7.Text =ts.TotalMilliseconds.ToString(); //daha sonra tsyi milisaniye cinsine çevirip texte yazdırıyoruz.
```

## eBADateTime Seçilen Tarihin Gününü Bulma 

```
public void OnModalReturn(object sender, eBAModalEventArgs e)

{

if(sender == Metin6)

{

        int gun = Convert.ToInt32(Metin6.Value.DayOfWeek);

         

        switch (gun)

                    {

                        case 1:

                            Metin12.Text = "Pazartesi";

                            break;

                        case 2:

                            Metin12.Text ="Salı";

                            break;

                        case 3:

                            Metin12.Text ="Çarşamba";

                            break;

                        case 4:

                            Metin12.Text ="Perşembe";

                            break;

                        case 5:

                            Metin12.Text ="Cuma";

                            break;

                        case 6:

                            Metin12.Text ="Cumartesi";

                            break;

                        case 7:

                            Metin12.Text = "Pazar";

                            break;

                    }

             }

}

```

