---
title: 6. Form Data API
sidebar_position: 6
---

# 6. Form Data API 


Form Data API, eBA Formlarının verilerine, veritabanı bağlantısı ve sorgularına ihtiyaç duymadan, erişim ve güncelleme sağlar. Bu bölümde, FormDataAPI kullanarak, eBAForm nesnesi üzerinden, formların alanlarına, tablo ve listelerine erişim için kullanılan, özellik ve metotlar örnekler ile açıklanmaktadır. 


### 6.1. eBAForm 


eBAForm nesnesi, form üzerindeki bütün nesneleri içerisinde bulundurur. Bu nesneler üzerinde değişiklik yapılabilmesine imkan sağlar. 



### 6.1.1. Özellikler 


•	Form 

Tanım: Açılan form nesnesinin adı bilgisidir. 
Tipi: System.String 
Deklarasyon: public string Form{ get; } 

•	Id 

Tanım: Açılan form nesnesinin id bilgisidir. 
Tipi: System.Integer 
Deklarasyon: public int Id { get; } 

•	CreatorUserID 

Tanım: Formu oluşturan kullanıcının id bilgisidir. 
Tipi: System.String 
Deklarasyon: public string CreatorUserID { get; set; } 

•	Creator 

Tanım: Formu onaylayacak kişinin onaylama türü bilgisidir. 
Tipi: eBAFormData.ApproverType 
Deklarasyon: public eBAFormData.ApproverType Creator { get; set; } 



•	CreateDate 

Tanım: Açılan formun oluşturulma tarihi bilgisidir. 
Tipi: System.DateTime 
Deklarasyon: public DateTime CreateDate { get; set; } 

•	DocumentId 

Tanım: Akış dizaynında belirlenen formata göre oluşturulan form id bilgisidir. 
Tipi: System.String 
Deklarasyon: public string DocumentId { get; set; } 

•	DocumentPath 

Tanım: Açılan formun ait olduğu dokümanın konum yolu bilgisidir. 
Tipi: System.String 
Deklarasyon: public string DocumentPath { get; } 

•	DocumentVersion 

Tanım: Açılan formun ait olduğu dokümanın versiyon bilgisidir. 
Tipi: System.Integer 
Deklarasyon: public int DocumentVersion { get; set; } 

•	Deleted 

Tanım: Açılan formun silinmiş bir form olup olmadığı bilgisidir. 
Tipi: System.Boolean 
Deklarasyon: public bool Deleted { get; set; } 

•	OwnerDocumentId 

Tanım: Akış dizaynı sırasında atanan üst dokümanın id bilgisidir. 
Tipi: System.Integer 
Deklarasyon: public int OwnerDocumentId { get; set; } 

•	OwnerProcessId 

Tanım: Akış dizaynı sırasında atanan üst dokümanın ait olduğu sürecin id bilgisidir. 
Tipi: System.Integer 
Deklarasyon: public int OwnerProcessId { get; set; } 

•	Process 

Tanım: Açılan formun ait olduğu sürecin adı bilgisidir. 
Tipi: System.String 
Deklarasyon: public string Process { get; } 

•	UserId 

Tanım: Formu oluşturan kullanıcının id bilgisidir. 
Tipi: System.String 
Deklarasyon: public string UserId { get; set; } 

•	Status 

Tanım: Dokümanın şu anki durum bilgisidir. 
Tipi: System.Integer 
Deklarasyon: public int Status { get; set; } 

•	ReadOnly 

Tanım: Açılan formun salt okunur olup olmadığı bilgisidir. 
Tipi: System.Boolean 
Deklarasyon: public bool ReadOnly { get; set; } 

•	ProfileOwner 

Tanım: Açılan formun doküman yönetim sistemindeki yoludur. 
Tipi: System.String 
Deklarasyon: public string ProfileOwner { get; set; } 

•	Fields 

Tanım: Form üzerindeki nesnelerin listesidir. 
Tipi: eBAFormData.FormFieldCollection 
Deklarasyon: public eBAFormData.FormFieldCollection Fields { get; } 

Örnek: Fieldlara nasıl erişilir? 
eBAFormData.eBAForm form = new eBAFormData.eBAForm(71); 

string firstName = form.Fields[“txtFirstName”].AsString; string lastName = form.Fields[“txtLastName”].AsString; 
DateTime birthday = form.Fields[“txtBirthDay”].AsDateTime; //RadioButton 
int male = form.Fields[“rbMale”].AsInteger; //RadioButton seçili ise 1, değil ise 0 dönecek 

//CheckBox 
int english = form.Fields[“cbEnglish”].AsInteger; 

Örnek: Fieldlar üzerinde nasıl değişiklik yapılır? 
eBAFormData.eBAForm form = new eBAFormData.eBAForm(71); 

form.Fields[“txtFirstName”].AsString = “George Michael”; form.Fields[“cbEnglish”].AsInteger = 1; 

//Değişiklilerin geçerli olması için update metodunu çağırıyoruz. 
form.Update(); 

•	CheckLists 

Tanım: Form üzerindeki checklist tipindeki nesnelerin listesidir. 
Tipi: eBAFormData.CheckListCollection 
Deklarasyon: public eBAFormData.CheckListCollection CheckLists { get; } 

•	Columns 

Tanım: Form üzerindeki nesnelerin veri tabanındaki kolonlarının listesidir. 
Tipi: eBAFormData.ColumnCollection 
Deklarasyon: public eBAFormData.ColumnCollection Columns { get; } 

•	Details 

Tanım: Form üzerindeki detaylar tipindeki nesnelerin listesidir. 
Tipi: eBAFormData.FormDetailsCollection 
Deklarasyon: public eBAFormData.FormDetailsCollection Details { get; } 

Örnek:  
Detaylar nesnesindeki bir forma nasıl erişilir, üzerinde nasıl değişiklik yapılır? 
eBAFormData.eBAForm form = new eBAFormData.eBAForm(71); 
foreach(var row in dtlExperiences.Rows) 
{ 
       eBAForm modalForm = row.Form; 
       string companyName = modalForm.Fields["txtCompanyName"].AsString;        modalForm.Fields["txtCompanyName"].AsString = companyName + "_";  	  modalForm.Update(); 
} 

Örnek:  
Detaylar nesnesinden bir satır nasıl silinir? 
```
if(dtlExperiences.Rows.Count>1) 
{ 
        dtlExperiences.Rows[dtlExperiences.Rows.Count-1].Form.Deleted = true;         dtlExperiences.Rows[dtlExperiences.Rows.Count-1].Form.Update();         dtlExperiences.Rows[dtlExperiences.Rows.Count-1].Delete();         form.Update(); 
} 
```
Örnek:  
Detaylar nesnesine yeni bir satır nasıl eklenir? 
WorkflowDocument doc = workflowManager.CreateDocument("Project1", 
"Form2"); 
if(doc != null) 
{ 
     eBAForm modalForm = new eBAForm(doc.DocumentId);        modalForm.Fields["txtCompanyName"].AsString = "Bimser";      modalForm.Fields["txtStartDate"].AsDateTime = DateTime.Now.AddYears(-1);      modalForm.Fields["txtLeaveDate"].AsDateTime = DateTime.Now;      modalForm.Update(); 
     dtlExperiences.Rows.Add(doc.DocumentId);     
} 
Form.Update(); 

•	DetailsGrid 

Tanım: Form üzerindeki detay tablo tipindeki nesnelerin listesidir. 
Tipi: eBAFormData.FormDatailsGridCollection 
Deklarasyon: public eBAFormData.FormDatailsGridCollection DetailsGrid { get; } 

Örnek:  
Detay tablo nesnesinde bulunan verilere nasıl erişilir ve üzerinde nasıl değişiklik yapılır? 
eBAFormData.eBAForm form = new eBAFormData.eBAForm(71); 

FormDetailsGrid dtlEducation = frm.DetailsGrids["dtlEducation"]; foreach(var row in dtlEducation.Rows) 
{ 
string level = row["listLevel"].AsString; string schoolName = row["txtSchoolName"].AsString; 
double grade = row["txtGrade"].IsNull ? 0 : (double)row["txtGrade"].Value; row["txtGrade"].Value = grade + 1; 
} 
form.Update(); 

Örnek:  
Detay tabloya nasıl yeni bir satır eklenir ya da var olan bir satır silinir? 
eBAFormData.eBAForm form = new eBAFormData.eBAForm(71); 

FormDetailsGrid dtlEducation = frm.DetailsGrids["dtlEducation"]; if(dtlEducation.Rows.Count == 0){         dtlEducation.Rows.Add(); 
} else { 
        dtlEducation.Rows[dtlEducation.Rows.Count-1].Delete(); 
} 
form.Update(); 

•	Lists 

Tanım: Form üzerindeki liste tipindeki nesnelerin listesidir. 
Tipi: eBAFormData.FormListCollection 
Deklarasyon: public eBAFormData.FormListCollection Lists { get; } 

Liste nesnelerine erişim ve liste nesnesindeki verileri değiştirme: foreach (var item in frm.Lists["listHobbies"].Rows) 
{ 
       string h += item.Text + " " + item.Value + "-";         item.Text = item.Text + "x"; 
} 

•	Tables 

Tanım: Form üzerindeki tablo tipindeki nesnelerin listesidir. 
Tipi: eBAFormData.FormTableCollection 
Deklarasyon: public eBAFormData.FormTableCollection Tables { get; }  


### 6.1.2. Metotlar 

•	eBAForm(int) 

Tanım: Belirtilen idye sahip eBA formunu getirir. 
Parametreler : 
id: Getirilmek istenilen formun id’sini belirtir. 
Dönüş tipi: eBAForm 

eBAFormData.eBAForm form = new eBAFormData.eBAForm(71); 

•	eBAForm(int, string, string) 

Tanım: Belirtilen parametrelere sahip formu getirir. 
Parametreler: 
id: Getirilmek istenilen formun id bilgisini belirtir. 
process: Getirilmek istenilen formun hangi sürece ait olduğu bilgisini belirtir. 
form: Getirilmek istenilen formun hangi tipte olduğu bilgisini belirtir. 
Dönüş tipi: eBAForm 
eBAFormData.eBAForm form = new eBAFormData.eBAForm(71, “Project1”, 
“Form1”); 

•	Update() 

Tanım: Form üzerinde yapılan değişikliklerin geçerli olabilmesi için kullanılır. 

eBAFormData.eBAForm form = new eBAFormData.eBAForm(71); 
//Form üzerinde işlemler 
form.Update();