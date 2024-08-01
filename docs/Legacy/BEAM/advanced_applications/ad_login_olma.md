# Active Directory ile Uygulamaya Giriş Yapılabilmesi İçin Gerekenler

Active Directory ile login olabilmek için öncelikle arayüzde LDAP ayarlarının tanımlı olması gerekmektedir. Bunun için aşağıdaki yol izlenmelidir:
Ana Menü -> Sistem -> Active Directory Tanımları
Doldurulması gereken alanlar ise: “Alan Adı” ve “Ldap Adı” alanlarının dolu olması gerekmektedir.
Bu ayarlar yapıldıktan sonra kullanıcı ayarlarına geçilir.
Bunun için aşağıdaki yol izlenmelidir:
Ana Menü -> Sistem -> Kullanıcılar -> İlgili kullanıcı -> Değiştir -> Eğer kullanıcının kodu active directory de farklı ise “Active Directory Kullanıcı” alanının dolu olması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/AD1-1d389f5d-7b9c-46de-a3c7-a23daaedf774.png)

Genel bilgiler kısmında ise ilgili kullanıcı sisteme girerken AD ile girecekse, Şifre Kontrol Türü “Active Directory”; her ikisini de kullanacaksa “Hepsi” seçilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/AD2-e31a0f90-2a1a-4c4f-a481-781284c10c5a.png)

Yapılması gereken ayarların tümü bu şekildedir.

