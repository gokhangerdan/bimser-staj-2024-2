# Kodla Item Ekleme

Aşağıdaki kodlar kullanılarak ComboBox nesnesine item eklenebilir.

	ListItem listItem = new ListItem()
	{
		Value = 1,Text = new MultiLanguageText(new Dictionary<string, string> { { "tr-TR", "text_1 tr" }, { "en-US", "text_1 en"} })
	};
	ComboBox1.Items.Add(listItem);