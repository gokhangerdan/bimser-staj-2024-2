# Lookup Kodla Satır Ekleme

Server(cs) tarafında lookup'a kodla satır ekleme ile ilgili  örnek kullanım aşağıdaki gibidir.

	DataGridRow dataGridRow =  Lookup1.NewRow();
	dataGridRow.Cells[0].Value = 1;
	dataGridRow.Cells[1].Value = "test";
	Lookup1.Rows.Add(dataGridRow);