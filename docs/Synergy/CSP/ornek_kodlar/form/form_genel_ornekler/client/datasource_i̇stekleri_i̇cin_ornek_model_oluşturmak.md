# DataSource İstekleri İçin Örnek Model Oluşturmak

```interface FormInputTypesResponse {
        result: {
                ROWID: number;
                DESCRIPTION: string;
                REQUESTSTATUS: boolean;
                OFFERSTATUS: boolean;
                INSTALLMENTSTATUS: boolean;
        }[];
}


await this.fetch.post<FormInputTypesResponse>("DataSource/GetFormInputTypes", { SELECTEDID: inputValue }).then(i => {
        var requestDetailsStatus: boolean = i.data.result[0].REQUESTSTATUS;
        var offerDetailsStatus: boolean = i.data.result[0].OFFERSTATUS;
        var installmentDetailsStatus: boolean = i.data.result[0].INSTALLMENTSTATUS;
        this.Tab_RequestDetails.clientVisible = requestDetailsStatus;
        this.Tab_OfferDetails.clientVisible = offerDetailsStatus;
        this.Tab_InstallmentDetails.clientVisible = installmentDetailsStatus;
        if (requestDetailsStatus) this.Tab_RequestDetails.selected = true;
        else if (offerDetailsStatus) this.Tab_OfferDetails.selected = true;
        else if (installmentDetailsStatus) this.Tab_InstallmentDetails.selected = true;
});```

Burada proje üzerindeki bir DataSource'a istek gönderilir ve dönen sütun isimlerine göre bir model oluşturulur. İstek gönderilirken model this.fetch.post\<ModelName\> şeklinde belirtilir ve dönen veriler örnekteki gibi kullanılır.

