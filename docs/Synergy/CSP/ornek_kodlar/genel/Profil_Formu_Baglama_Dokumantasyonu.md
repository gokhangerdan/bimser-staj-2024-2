
# Profil Formu Bağlama Dokümantasyonu

Synergy ortamına bir dosyayu yüklerken profil formu bağlamak için aşağıdaki adımları izleyebilirsiniz:

## Gereksinimler

1. **Proje ID Bilgisi**: Veri tabanındaki `PROJECTS` tablosundan `NAME` kolonuna göre filtreleme yaparak projenin ID değerini alın.
2. **Form ID Bilgisi**: `PROJECTFORMS` tablosundan `PROJECTID` ve `NAME` kolonlarını filtreleyerek formun ID değerini alın. `PROJECTFORMS` tablosundaki `NAME` kolonu form ismine karşılık gelmektedir.

## Adımlar

### 1. Proje ID Değerini Almak
```sql
SELECT ID
FROM PROJECTS
WHERE NAME = 'Proje Adı'
```

### 2. Form ID Değerini Almak
```sql
SELECT ID
FROM PROJECTFORMS
WHERE PROJECTID = 'ProjeID'
  AND NAME = 'Form Adı'
```

### 3. CreateFileDocumentItem Nesnesinden Liste Oluşturmak
- Proje adı, form adı, document ID, form ID ve proje ID bilgileriyle `CreateFileDocumentItem` nesneleri oluşturulur.

```csharp
List<CreateFileDocumentItem> profileFormList = new List<CreateFileDocumentItem>();
profileFormList.Add(new CreateFileDocumentItem{
    ProjectName = "SOS_ProfileFormExampleProject",
    FormName = "ExampleProfileForm",
    DocumentId = 4794,
    FormId = "d0b8a7a2-de28-4a95-b6e0-3927ca9512fd",
    ProjectId = "4b5c6b72-b570-4b2c-8eaf-f5d82301f105"
});
```

### 4. CreateFileRequest Nesnesi Oluşturmak ve Dosya Bağlamak
- `CreateFileRequest` nesnesi oluşturularak profil formu dosyaya bağlanır.

```csharp
CreateFileRequest createFileRequest = new CreateFileRequest(
    folderSecretKeyResult.Data,
    fileContentInfo,
    createFileModel.Name,
    createFileModel.Description,
    profileFormList,
    null
);
WrapResponse<GetDMObjectResponse> createFileResponse = _synergyHelper.ServiceApi.DocumentManagement.CreateFile(createFileRequest).Result;
```

Bu adımlar takip edilerek Synergy ortamında bir dosyaya profil formu bağlanabilir.

## Örnek Kod

```csharp
List<CreateFileDocumentItem> profileFormList = new List<CreateFileDocumentItem>();
profileFormList.Add(new CreateFileDocumentItem{
    ProjectName = "SOS_ProfileFormExampleProject",
    FormName = "ExampleProfileForm",
    DocumentId = 4794,
    FormId = "d0b8a7a2-de28-4a95-b6e0-3927ca9512fd",
    ProjectId = "4b5c6b72-b570-4b2c-8eaf-f5d82301f105"
});

CreateFileRequest createFileRequest = new CreateFileRequest(
    folderSecretKeyResult.Data,
    fileContentInfo,
    createFileModel.Name,
    createFileModel.Description,
    profileFormList,
    null
);

WrapResponse<GetDMObjectResponse> createFileResponse = _synergyHelper.ServiceApi.DocumentManagement.CreateFile(createFileRequest).Result;
```
