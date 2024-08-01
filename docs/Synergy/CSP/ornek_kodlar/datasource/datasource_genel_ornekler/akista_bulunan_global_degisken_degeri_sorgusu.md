# Akışta Bulunan Global Değişken Değeri Sorgusu

```
DECLARE @VARIABLEKEY AS NVARCHAR(75)
DECLARE @VARIABLENAME AS NVARCHAR(75)
DECLARE @PROCESSID AS INT
DECLARE @JSONDATA AS NVARCHAR(MAX)
DECLARE @PERSISTENCEID AS INT
SET @VARIABLENAME = {{VariableName}} -- Örn: 'varTaskStatus'
SET @PROCESSID = {{ProcessId}} -- Örn: 45253

SELECT
@JSONDATA = Data,
@PERSISTENCEID = PersistenceId
FROM E_TESTPROJECT_Workflow -- E_[PROJEADI]_Workflow
WHERE
JSON_VALUE(Data,'$.General.ProcessId') = @PROCESSID

SELECT @VARIABLEKEY = flowObjects.[Key]
FROM OPENJSON(@JSONDATA, '$.Steps.Metadata') 
WITH ([Key] UNIQUEIDENTIFIER '$.Key', [Name] NVARCHAR(50) '$.Name') flowObjects
WHERE flowObjects.Name = @VARIABLENAME;

SELECT JSON_VALUE(j2.value,'$.Value')
FROM OPENJSON((SELECT Data From E_TESTPROJECT_Workflow WHERE PersistenceId = @PERSISTENCEID), '$.Steps.Variables') AS j1  -- E_[PROJEADI]_Workflow
CROSS APPLY OPENJSON(j1.value) AS j2
WHERE j1.[key] = LOWER(@VARIABLEKEY)
AND j2.[key] = 'ValueOptions'
```

Akış tarafında, **form üzerinde bir nesneye bağlı olmayan** değişkenlerin değerini görebilmek için kullanılan sorgudur. Değişken adı, süreç numarası ve proje adı bilgileri değiştirilerek kullanılabilir.

