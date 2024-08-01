# Mail Süreç Onay veya Bilgilendirme Linkini Mobilde Açmak

Döküman Yönetiminde "system/settings/workflow mail templates" altında bulunan ilgili dildeki mail template dosyasını aşağıdaki ile güncelleyerek mobil uygulamayı açmayı sağlayacak linki mail gönderiminde barındırtılabiliyor.

```<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<HTML>
<HEAD>
<meta http-equiv="Content-Type" content="text/html; charset=unicode">
<TITLE>eBA İşakışı Yönetim Sistemi 5.0</TITLE>
<style>
    BODY {
        margin:0px;
    }
    .fnt {
        font-size: 10pt;
        font-family: Tahoma;
    } 
    .redmes {
        color:red;
        font-weight:bold;
    }
</style>
</HEAD>
<BODY bgcolor="whitesmoke">
<div>
<table cellpadding="0" cellspacing="0" width="100%">
<tr><td>
<table class="fnt" cellpadding="3" cellspacing="3">
<tr><td colspan="2"><?=Name> <?=Surname></td></tr>
<tr><td class="redmes" colspan="2"><?=Text></td></tr>
<tr><td>
<?=ProcessProperties>
</td></tr>
<tr><td colspan="2"><a href="<?=Link>" target=_blank>Tarayıcıda görüntüle</a></td></tr>
<tr><td colspan="2"><a href="<?=Link>%isMobile=1" target=_blank>Mobilde görüntüle</a></td></tr>
</table>
</td></tr>
</table>
</div>
</BODY>
</HTML>```

