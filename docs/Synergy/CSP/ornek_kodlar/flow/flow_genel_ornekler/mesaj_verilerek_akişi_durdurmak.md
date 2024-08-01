# Mesaj verilerek akışı durdurmak

Mesaj verilerek akışı durdurmak için aşağıdaki api methodlarını akış kodunda kullanabilirsiniz.

```public void StopWithError(string title, string message, Context context)
public void StopWithError(Dictionary<string, string> title, Dictionary<string, string> message, Context context)
 
public void StopWithInfo(string title, string message, Context context)
public void StopWithInfo(Dictionary<string, string> title, Dictionary<string, string> message, Context context)
 
public void StopWithWarning(string title, string message, Context context)
public void StopWithWarning(Dictionary<string, string> title, Dictionary<string, string> message, Context context)```

