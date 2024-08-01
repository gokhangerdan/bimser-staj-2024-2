---
sidebar_label: Kontrol Listesi ve Şema
sidebar_position: 5
custom_edit_url: ""
---

#  Kontrol Listesi ve Şema


### **Uygulamalar**

|      Program   			|   İndirme Linki			  									 |
|---------------------------|----------------------------------------------------------------|
|Java - **Versiyon 1.8**	| https://www.java.com/tr/download/manual.jsp 					 |
|Net Core **3.1** veya 7.0 	| https://dotnet.microsoft.com/en-us/download/dotnet/3.1		 |
|Net Core 3.1 veya **7.0** 	| https://dotnet.microsoft.com/en-us/download/dotnet/7.0		 |
|Akis Kart Yöneticisi 		| https://www.turktrust.com.tr/diger-yazilimlar.html 			 |
|Palma Uygulası				| https://www.turktrust.com.tr/kurulum-islemleri.html            |

---
### **Parametreler**

|      Program   			|   İndirme Linki			  									 |
|---------------------------|----------------------------------------------------------------|
|JAVA_HOME	| Java nın Kurulu Olduğu Path'in verilmesi gerekiyor.1 den fazla java versiyonu kurulu olduğu durumlar için **https://docs.bimser.net/** den detaylara ulaşabilirsiniz. |
|DSCLIENT_PROXY_HOST 	| DSClient Proxy üzerinden haberleşecekse **Host** Bilgisinin Girilmesi Gerekiyor.   |
|DSCLIENT_PROXY_PORT 	| DSClient Proxy üzerinden haberleşecekse **Port** Bilgisinin Girilmesi Gerekiyor. |
|DSCLIENT_PROXY_USER		|  DSClient Proxy üzerinden haberleşecekse **Username** Bilgisinin Girilmesi Gerekiyor. |
|DSCLIENT_PROXY_PASSWORD			| DSClient Proxy üzerinden haberleşecekse **Password** Bilgisinin Girilmesi Gerekiyor.   |
|DSCLIENT_XMS| JVM başlatıldığında ilk ram boyutunu ayarlar.|
|DSCLIENT_XMX| JVM başlatıldığında Maksimum ram boyutunu ayarlar.   |

---
##### **Xml Config Parametreleri**
| Parametre Dosyası |   Parametre |Açıklama			  									 |
|---------------------------|------------------|----------------------------------------------|
| certval-policy.xml| TrustedCertificateFinderFromECertStore | Açık olduğu durumda sertifikadeposu.svt' de setifika doğrulaması yapar |
| certval-policy.xml| TrustedCertificateFinderFromXml  | Value parametresindeki adresten sertifika doğrulaması yapar |
| certval-policy.xml| TrustedCertificateFinderFromFileSystem| Value parametresindeki dosya uzantısında bulunan sertifikalar arasından doğrulaması yapar |
| certval-policy.xml| CertStoreCRLSaver| sertifikadeposu.svt dosyasına, daha önceden doğrulanmış sertifikaları kaydeder. (Kamusm kullanılmasını önermiyor, kaldırmayı düşünüyorlar.) |
| certval-policy.xml| QualifiedCertificateChecker| Nitelikli sertifikaları denetlemek için kullanılır. (Kamusm kullanılmasını önermiyor, kaldırmayı düşünüyorlar.) |
| certval-policy.xml| OCSPResponseFinderFromAIA| Açık olması durumunda sertifika OCSP ile doğrulanır. Kapatılması durumunda Seritifika bilgileri içerisindeki AIA adresi kullanılır. Orası da kullanılmaz ise Sertifika SİL (CLR) ile doğrulanmaya çalışılır.) |
| certval-policy.xml| CRLDateChecker| Bu parametre sertifikaların CLR geçerlik tarihini kontrol eder. KESİNLİKLE KAPATILMAMASI gerekir. Kapatıldığı tahdirde geçersiz sertifikalar ile imza atılır ve sertifika geçerli gözükür.) |
| esya-signature-config.xml | http (TAG)| Tag içerisindeki alanlara Proxy bilgileri yazılırsa istekler proxy üzerinden gider. Fakat biz bunu çalıştıramadık, bunun yerine SistemDeğişkenlerindeli Proxy ayarları kullanılabilir. |
| esya-signature-config.xml | timestamp-server (TAG)| Zaman damgası bilgileri yazılır. |
| esya-signature-config.xml | validate-certificate-before-signing | Pades imzalar için imzalama öncesi sertifika kontrolü ayarıdır. true/false değeri alır. |
| esya-signature-config.xml | certificate-validation-policy-file| Sertifikalara hangi policy dosyasına göre işlem yapılacağını belirtir|
| esya-signature-config.xml | certificate-validation-policy-file for="MaliMuhurCertificate| Malimühür sertifikalara hangi policy dosyasına göre işlem yapılacağını belirtir|
| mobilesignature-config.xml | MobileSignature (TAG) | Mobil imzalar için kullanılacak adresleri ve bu adreslere giriş  yapılırken kullanılacak Id ve Şifreleri tutar. |
---
**Mobil İmzaların Akışı**
---
![title](https://docsbimser.blob.core.windows.net/imagecontainer/mobilimza-ef2175e3-8dfd-4bb8-a3af-84b37f4d43be.png)

**Elektronik İmza Akışı**
---
Aşağıdaki şekillerin için açıklama Dijital İmza Kullanımı başlığında yapılmıştır.

---
**1. Tip İmza**

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd354f3ef-da35-4dd5-b48b-eb32472cf430)

---
**2. Tip İmza**

![title](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d4d4c7f-6f5b-419d-ad82-de699dc6d33f)





