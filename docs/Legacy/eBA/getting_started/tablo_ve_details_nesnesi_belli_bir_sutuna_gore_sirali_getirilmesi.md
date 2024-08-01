# Tablo ve Details Nesnesi Belli Bir Sütuna Göre Sıralı Getirilmesi 

şağıdaki kod örneği ile Details1 nesnesindeki Text1 alanına göre sıralı olarak yüklenmesi sağlanıyor. 

	public void Duzenle() 

	{ 

	         DataView dv = Details1.Data.DefaultView;                                 

	             dv.Sort = "Text1 DESC"; 

	             Details1.Data = dv.ToTable(); 

	}