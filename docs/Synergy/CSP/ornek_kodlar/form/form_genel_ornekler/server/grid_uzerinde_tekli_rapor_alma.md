# Grid üzerinde Tekli Rapor Alma (Controller)

Controller tarafı için kullanılan kodlar

```
[HttpPost] 
  [ActionName("GetReport")] 
 [NoRequestHeaders] 
 [NoResponseHeaders] 
 public GetReportResponse GetReport([FromBody] GetReportRequest body){ 
 _EncryptedData = body.Session.EncryptedData;
 _Language = body.Session.Language;
 _Token = body.Session.Token; 
 ClientServices.DocumentManagementService dmInternalApiClient = null;
 ServiceApiHelper serviceApiHelper = null; 
 string tokenId = ""; 
  dmInternalApiClient = new ClientServices.DocumentManagementService(HttpClientConfiguration.InternalApiUrl);
 tokenId = body.Session.TokenId; 
  MemoryStream publishedStream = new MemoryStream(); 
 ExcelDocument document = new ExcelDocument();
 var form = ServiceApi.FormManager.Create("ProjectName", "FormName", body.DocumentId).Result; 
 document.Items.AddText("-", form.Controls["-"].Text.ToString()); 
 document.Items.AddText("-", form.Controls["-"].Text.ToString()); 
  DownloadDataRequest downloadDataRequest = new DownloadDataRequest 
 {Id = // Id -> Dosya Id  
 Parameters = Headers,
 CommitId = 0,
 ForDownload = true,
 IsBranch = false,
 Path = "",
 TokenId = tokenId, 
 Type = ObjectType.File, 
  VersionId = 0 
};
 Google.Protobuf.ByteString byteString = dmInternalApiClient.DownloadData(downloadDataRequest).Result.Result.Data;Stream stream = new MemoryStream(byteString.ToByteArray());
 document.Build(stream).Wait();
 document.Save(publishedStream, Bimser.Synergy.DocumentBuilder.Common.Enums.CellSaveFormat.Xlsx).Wait();
 publishedStream.Position = 0; 
 UploadFileRequest uploadFileRequest = new UploadFileRequest 
 { Data = Google.Protobuf.ByteString.FromStream(publishedStream),
 Parameters = Headers,
 MimeType = "application/xlsx",
 FolderId = //FOLDERID  -> Klasör Id 
 };
 uploadFileRequest.Name.Add("tr-TR", $"{form.Controls["-"].Text.ToString()}.xlsx");
 UploadFile uploadFileResponse = dmInternalApiClient.UploadFile(uploadFileRequest).Result.Result; 
 return new GetReportResponse{SecretKey=uploadFileResponse.SecretKey,FileName=uploadFileResponse.Name[body.Session.Language],Result=""}; 
} 
 
```

Gerekli olan methodlar

```
public class GetReportRequest{
 public long DocumentId{get;set;} 
 public UserSession Session{get;set;}
 public long ProcessId{get;set;}
 public long ReportType{get;set;}
  }
 public class GetReportResponse{ 
  public string SecretKey{get;set;} 
 public string FileName{get;set;} 
  public string Result{get;set;} 
 }

```

Client tarafında raporu indirmek için kullanılan kodlar (Client)

```
const getReportRes:any= await this.fetch.post("/FormName/GetReport", 
  {DocumentId: (Number)(args.targetArgs.row.data.DOCUMENTID),Session: this.session,ProcessId: args.targetArgs.row.data.ProcessID});                 let downloadUrl  = await this.fetch.post((window as any).serviceConfig.services.dm.baseURL +"/DocumentManagement/Objects/GetDownloadUrl", {secretKey: getReportRes.data.secretKey,fileName : getReportRes.data.fileName} );const link = document.createElement('a'); link.target = "_blank";
 link.href = (window as any).serviceConfig.services.dm.baseURL + "/" + (downloadUrl.data as any).downloadUrl; 
 link.setAttribute('download', getReportRes.data.fileName);
 document.body.appendChild(link); 
 link.click();
 console.log("indirme başlatılıyor"); 
 document.body.removeChild(link);
```

