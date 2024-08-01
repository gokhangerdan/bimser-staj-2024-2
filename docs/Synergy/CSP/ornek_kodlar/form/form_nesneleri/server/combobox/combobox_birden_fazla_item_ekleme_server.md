# Kodla Item Ekleme (Birden Fazla)

Aşağıdaki kodlar kullanılarak ComboBox nesnesine bir liste şeklinde itemlar eklenebilir.

	ListItemCollection listItems = new ListItemCollection()
	{
		new ListItem { Value = 1, Text = new MultiLanguageText(new Dictionary<string, string> { { "tr-TR", "text_1 tr" }, { "en-US", "text_1 en"} }) },
		new ListItem { Value = 2, Text = new MultiLanguageText(new Dictionary<string, string> { { "tr-TR", "text_2 tr" }, { "en-US", "text_2 en"} }) },
		new ListItem { Value = 3, Text = new MultiLanguageText(new Dictionary<string, string> { { "tr-TR", "text_3 tr" }, { "en-US", "text_3 en"} }) },
		new ListItem { Value = 4, Text = new MultiLanguageText(new Dictionary<string, string> { { "tr-TR", "text_4 tr" }, { "en-US", "text_4 en"} }) }
	};
	ComboBox1.Items.AddRange(listItems);