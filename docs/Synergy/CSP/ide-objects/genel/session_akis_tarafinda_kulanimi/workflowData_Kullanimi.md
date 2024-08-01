# WorkflowData Kullanımı
### WorkflowData.Context Nedir ?
-   Form tarafında kullanılan Sessionların, Flow tarafındaki karşılığına denk gelir.
-   Synergy ortamının flow tarafında kullanılan Session'ın örnek çıktısı ise şu şekildedir;  
```json
{
  "Instance": "****",
  "Token": "****",
  "Language": "tr-TR",
  "EncryptedData": "****",
  "UserId": 13,
  "Username": "oselcuk",
  "TokenId": "****",
  "AuthenticationType": 1,
  "InternalUserId": 13,
  "InternalUsername": "oselcuk",
  "Positions": [],
  "DelegationId": null,
  "Severity": 5,
  "FootPrint": "****",
  "TraceId": "*****",
  "Baggage": {},
  "Host": null
}
```
## Flow Tarafında Kullanımı
- Örnek bir kullanıcın id ve username değerlerini getiren örnek kod bloğu şu şekilderdir;

```csharp
    string userId = _workflowData.Context.UserId.ToString();
    string userName = _workflowData.Context.Username;
```