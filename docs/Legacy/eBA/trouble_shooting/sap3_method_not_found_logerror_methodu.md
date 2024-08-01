# SAP3 Method Not Found Hatası (LogError Methodu)

Hata mesajı:

Query execution failed
System.TypeInitializationException: The type initializer for 'SAP.Middleware.Connector.RfcConfigParameters' threw an exception. ----> System.MissingMethodException: Method not found: 'Void SAP.Middleware.Connector.RfcTrace.LogError(System.String, System.Object[], System.Exception)'.
   at SAP.Middleware.Connector.RfcConfigParameters..cctor()
   --- End of inner ExceptionDetail stack trace ---
   at SAP.Middleware.Connector.RfcConfigParameters..ctor()

   at eBASAPAPI3.eBASAPIntegration.b()

   at eBASAPAPI3.eBASAPIntegration.a()

   at eBASAPAPI3.eBASAPIntegration.Execute()

   at eBASystemIntegration.SAP3.eBASAPQuery.Execute(QueryParameter[] parameters, eBASystemQueryExecutionParameters ep)

   at k.a(String A_0, String A_1, List`1 A_2, QueryMode A_3, QueryExecutionParameters A_4)
   --- End of inner ExceptionDetail stack trace ---
   at k.a(String A_0, String A_1, List`1 A_2, QueryMode A_3, QueryExecutionParameters A_4)

   at d.a(String A_0, String A_1, List`1 A_2, QueryMode A_3, QueryExecutionParameters A_4)

   at SyncInvokeExecuteQuery(Object , Object[] , Object[] )

   at System.ServiceModel.Dispatcher.SyncMethodInvoker.Invoke(Object instance, Object[] inputs, Object[]& outputs)

   at System.ServiceModel.Dispatcher.DispatchOperationRuntime.InvokeBegin(MessageRpc& rpc)

   at System.ServiceModel.Dispatcher.ImmutableDispatchRuntime.ProcessMessage5(MessageRpc& rpc)

   at System.ServiceModel.Dispatcher.ImmutableDispatchRuntime.ProcessMessage11(MessageRpc& rpc)

   at System.ServiceModel.Dispatcher.MessageRpc.Process(Boolean isOperationContextSet)

Çözüm:

sapnco ve sapnco_utils dll'lerinin sürümü 3.0.2 iken bu hata alınmakta. 3.0.18 veya 3.0.25 sürümüne ihtiyacınız var.
https://bimsercozumyazilim-my.sharepoint.com/:u:/g/personal/eibrahimoglu_bimser_com/EaGu76GOIixLvp7UrIpArtcBx4AhwCcMCPJA7oaRwoHkBA?e=U2yG0X

