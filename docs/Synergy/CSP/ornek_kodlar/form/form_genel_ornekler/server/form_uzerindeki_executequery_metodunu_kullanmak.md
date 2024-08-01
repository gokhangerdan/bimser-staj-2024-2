# Form Üzerindeki Execute Query'yi Kullanmak

ServiceAPI'den daha hızlı olan Form üzerindeki ExecuteQuery methodunun kullanımını ve dönen sonucun anlaşılır hale getirilmesi.

Kullanacağımız ilgili datasource içindeki Kolonlar sekmesi altında gelen kolonların tiplerine göre Class oluşturmalıyız. Bu bize gelen veriyi kullanım kolaylığı sağlacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/datasourceColumns-d96a6f06-823b-42f6-ae9a-7185d563238f.png)

### Kullanım Örneği

```
var res = ExecuteQuery<Class>(DataSourceName, new[] { new { ParameterKey = ParameterValue } });
```

### Örnek Class

```
public class Class
{
    public int ID { get; set; }
    public string USERNAME { get; set; }
    public string FIRSTNAME { get; set; }
}
```

### Yardımcı Metot

```
public List<T> ExecuteQuery<T>(string queryName, object[] queryArguments) where T : class, new()
{
    var queryResult = (List<Dictionary<string, object>>)((DataSourceResponse)ExecuteQuery(queryName, queryArguments).Result.QueryResult).Result;
    List<T> typedList = new List<T>();
    foreach (var dictionary in queryResult)
    {
        T typed = new T();
        foreach (var kvp in dictionary)
        {
            if (kvp.Value is not DBNull)
            {
                typed.GetType().GetProperty(kvp.Key).SetValue(typed, kvp.Value);
            }
        }
        typedList.Add(typed);
    }
    return typedList;
}
```

