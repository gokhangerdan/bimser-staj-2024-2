# DataGrid'e Kodla Satır Ekleme (Server/CS)

Aşağıdaki kodlar kullanılarak DataGrid'e satır eklenebilir.


	DataGridRow dataGridRow = DataGrid1.NewRow();

	dataGridRow["dtgid"].Value = 1;
	dataGridRow["dtgid"].Text = "1";
	dataGridRow["dtgtext"].Value = "test1";
	dataGridRow["dtgtext"].Text = "test1";

	DataGrid1.Rows.Add(dataGridRow);