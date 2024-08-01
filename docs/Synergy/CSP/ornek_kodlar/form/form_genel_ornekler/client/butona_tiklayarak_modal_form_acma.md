# Butona Tıklayarak Modal Form Açma 


Aşağıda bulunan kod  bloğu eklemiş olduğumuz butonun Onclick Eventine yazdığımız kod sayesinde istemiş olduğumuz bir modal formu açmamızı sağlar. 

```
async BtnEdit_OnClick(args: Controls.EventArgs.IClickEventArgs) {
        this.openForm(
                {
                    documentId: this.DocID.value.toString(),
                    typeName: "OpenFormArgs",
                    view : this.viewName.value,
                    parameters: []
                }
            );
    }
```

Ek olarak bu kodumuzu eklenen parametre örneğini de aşağıdaki bölümde bulabilirsiniz.

```
                parameters: [{
                    name: "param",
                    type: "string",
                    value: this.TextBox1.text
                    }
                ]
```

