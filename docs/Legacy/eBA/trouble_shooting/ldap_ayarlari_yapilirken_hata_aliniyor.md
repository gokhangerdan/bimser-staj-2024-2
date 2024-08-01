# LDAP Ayarları Yapılırken Hata Alınıyor

eBA Configuration üzerinden LDAP ayarları yapılırken hata alıyorsanız ve bu hatayı Config Editörde değişiklikleri kaydederken alıyorsanız ve hata mesajı aşağıdaki gibiyse çözümü mevcut.

XmlException

The ' ' character, hexadecimal value 0x09, cannot be included in a name.

   at System.Xml.XmlDocument.CheckName(String name)

   at System.Xml.XmlElement..ctor(XmlName name, Boolean empty, XmlDocument doc)

   at System.Xml.XmlDocument.CreateElement(String prefix, String localName, String namespaceURI)

   at System.Xml.XmlDocument.CreateElement(String name)

   at eBASystemAPI.Config.Node.a(XmlNode A_0, Node A_1, List`1 A_2)

   at eBASystemAPI.Config.Node.ConvertToXml(Node exportNode)

   at eBASystemAPI.Config.Node.GetXmlText()

Çözüm:

Veritabanında Configuration tablosuna Default LDAP alanının "key" kısmı boşluklu şekilde 
"Security.    FIRMAADI      true     false" benzeri yapıda yazılmış, eski haline "Security.Default" keyine çevirdikten sonra servis restart edildi, problem çözüldü.

