# DataGrid Toolbar Action Button Parametre Değerini Okumak ve Değiştirmek

![DataGrid Toolbar Action Button Parametre Değerini Okumak ve Değiştirmek](https://docsbimser.blob.core.windows.net/imagecontainer/DataGrid%20Kodla%20Toolbar%20Action%20Button%20Parametre%20De%C4%9Ferini%20Okumak%20ve%20De%C4%9Fi%C5%9Ftirmek-97847c17-f157-4167-a98c-80d0034a7211.png)

### Değeri Değiştirmek İçin;

```csharp
DataGrid1.ToolbarActionButtons.Find(x => x.Name == "TESTBUTTON").Args.Parameters.Find(y => y.Name == "txtValue").Value = true;
```

### Değeri Okumak İçin;

```csharp
string val = DataGrid1.ToolbarActionButtons.Find(x => x.Name == "TESTBUTTON")?.Args.Parameters.Find(y => y.Name == "txtValue")?.Value.ToString();
```
