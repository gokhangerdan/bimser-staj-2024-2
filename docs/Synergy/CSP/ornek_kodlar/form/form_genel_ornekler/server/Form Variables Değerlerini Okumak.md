# Form Variables Değerlerini Okumak

```csharp
    string val = string.Empty;
    if(this.Variables.ContainsKey("TESTPARAM"))
        val = this.Variables["TESTPARAM"].ToString();
```
