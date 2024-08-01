# Memory Gates Checking Failed Because The Free Memor

![](https://docsbimser.blob.core.windows.net/imagecontainer/mmry-ffe43493-3ac8-434f-9ce4-55aa3e0ea304.png)

Memory gates checking failed because the free memory (537915392 bytes) is less than 5% of total memory. As a result, the service will not be available for incoming requests. To resolve this, either reduce the load on the machine or adjust the value of minFreeMemoryPercentageToActivateService on the serviceHostingEnvironment config element.

Bimserviewer'da alınan bu hatanın çözümü için:
BimserViewer  - Services klasöründeki web congifde aşağıdaki değeri ekliyoruz.

```
<system.serviceModel> 
    <serviceHostingEnvironment minFreeMemoryPercentageToActivateService="0" />
</system.serviceModel> 

```

