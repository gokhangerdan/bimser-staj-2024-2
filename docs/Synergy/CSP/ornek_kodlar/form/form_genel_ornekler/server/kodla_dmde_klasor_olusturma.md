# Kodla DM'de Klasör Oluşturma

Aşağıdaki kod ile DM'de klasör oluşturulabilir.

	private void CreateFolder(string folderName, string folderDesc, string parentFolderPath){
	             ServiceApi.DocumentManagement.CreateFolderAsync(
	                new Dictionary<string, string>{{ "tr-TR", folderName}}, //olusturmak istediginiz klasorun adi
	                new Dictionary<string, string>{{ "tr-TR", folderDesc }}, //olusturmak istediginiz klasorun description'i
	                GetDMObject(parentFolderPath).SecretKey); //klasorun olusturulacagi dizin verilir.
	        }