# Form Tarafına Gelen Parametreleri Okumak

```csharp
string val = string.Empty;
if(this.ResponseParameters.ContainsKey("TESTPARAM"))
    val = this.ResponseParameters["TESTPARAM"].ToString();
```
