# The maximum number of form, query string, or posted file items has already been read from the request. To change the maximum allowed request collection count from its current value of 2000

![](https://docsbimser.blob.core.windows.net/imagecontainer/hata-962eea51-b5b6-4229-a32a-af9bb7d66537.png)


eBA uygulamasının kurulu olduğu dizine gidiniz.eba.net/Web.config dosyasında  aşağıdaki keyin value değerini yükseltip 10000 yaptığınızda problem düzelecektir.Defaul değeri 2000 olarak set edilmiştir. 



```<add key="aspnet:MaxHttpCollectionKeys" value="10000" />```

