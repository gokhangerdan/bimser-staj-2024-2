# RelatedDocuments Silme İşlemini İptal Etme

```
void RelatedDocuments1_OnBeforeFileRemove(object sender, RelatedDocumentsRemoveEventArgs e) 

        { 

            // true olarak set edildiginde, silme islemi iptal edilecektir. 

            e.Cancel = CheckBox1.Value; 

            if(e.Cancel) 

            { 

                ShowMessage("RelatedDocuments1 - RelatedDocuments1_OnBeforeFileRemove", $"Dosya silme islemi iptal edildi ! #### File Creator Id : {e.File.CreatorId} ####", Bimser.CSP.FormControls.RuleManager.AlertType.Info); 

            }           

        } 
```

