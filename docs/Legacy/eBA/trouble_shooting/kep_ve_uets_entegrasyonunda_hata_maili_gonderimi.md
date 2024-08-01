# Kep Ve UETS Entegrasyonunda Hata Oluşması Durumunda Mail İle Bildirim Alınması

Kep hata mailini almak için önce Doküman yönetiminde //Root/system/settings/kep mail templates dizini oluşturulur. İçerisine “kep_receive_error_log_template.txt” ve “kep_send_error_log_template.txt”  olmak üzere iki tane dosya eklenir.

Mail Template için aşağıda örnek dosya içeriklerine ulaşabilirsiniz.


## kep_receive_error_log_template.txt

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title></title>
</head>
<body>
    <h4>{{provider_name}} Failed to Receive Kep Mail(s)</h4>
    <table cellpadding="7" cellspacing="0">
        <thead>
            <tr>
                <th style="text-align:left;">ProfileID</th>
                <th style="text-align:left;">StartProcess</th>
                <th style="text-align:left;">GetOnlyUnreadMails</th>
                <th style="text-align:left;">MailAddress</th>
                <th style="text-align:left;">ProviderName</th>
                <th style="text-align:left;">Date</th>
            </tr>
        </thead>
        <tbody>
            <repeat-item>
                <tr>
                    <td>{{profile_id}}</td>
                    <td>{{start_process}}</td>
                    <td>{{get_only_unread_mails}}</td>
                    <td>{{mail_address}}</td>
                    <td>{{provider_name}}</td>
                    <td>{{date}}</td>
                </tr>
            </repeat-item>
            {{repeat_output}}
        </tbody>
    </table>
</body>
</html>
```

## kep_send_error_log_template.txt

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title></title>
</head>
<body>
    <h4>{{provider_name}} Failed to Send Kep Mail(s)</h4>
    <table cellpadding="7" cellspacing="0">
        <thead>
            <tr>
                <th style="text-align:left;">EMLPath</th>
                <th style="text-align:left;">MailID</th>
                <th style="text-align:left;">Profile</th>
                <th style="text-align:left;">ProviderName</th>
                <th style="text-align:left;">MailAddress</th>
                <th style="text-align:left;">Date</th>
            </tr>
        </thead>
        <tbody>
            <repeat-item>
                <tr>
                    <td>{{eml_path}}</td>
                    <td>{{mail_id}}</td>
                    <td>{{profile}}</td>
                    <td>{{provider_name}}</td>
                    <td>{{mail_address}}</td>
                    <td>{{date}}</td>
                </tr>
            </repeat-item>
            {{repeat_output}}
        </tbody>
    </table>
</body>
</html>
```

![](https://docsbimser.blob.core.windows.net/imagecontainer/r-5cc2af36-276f-4ee2-ba39-1c557ccd3215.png)

## KEP Profili ile hata bildirimin yapılacağı mail adresinin eşleştirilmesi.

KEP profillerinin tanımlandığı ekran açılarak, ekran görüntülerinde gösterildiği gibi, entegrasyona hata oluşması durumunda mail bilgilendirmesinin yapılacağı mail adresi ilgili alana yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBA_KEP_GIRIS-484479bc-ed30-4bd1-9b48-43c8c4692ddc.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBA_KEP_DETAY-d94a17e8-c79d-42c0-bb71-1c516eef3c51.png)