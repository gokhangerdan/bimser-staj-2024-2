# eBA uygulamasının Logo'larının değiştirilmesi

Login ekranındaki eba logosu, eba uygulamasının kurulu olduğu dizinde "eba.net/Desktop/Images/Design/HeaderText" klasöründe yer alır. 
Buraya 'Login_Logo.png' ve 'ebalogo' ismiyle png uzantılı logo dosyası konulmalıdır. 


En uygun görünüm için varsayılan boyutlar esas alınmalıdır.

"Login_Logo.png" görseli Width: 143 Height: 124

"Ebalogo.png" görseli  Width: 198 Height: 74

![](https://docsbimser.blob.core.windows.net/imagecontainer/1-9dcf5944-94eb-4395-9ed0-1d499cca68dd.png)

ebA uygulamasına Giriş yaptıktan sonra, sol üstteki logoyu değiştirmek için eBA'da DM altında "system/customstyle" şeklinde yoksa yeni klasör oluşturulup, 'customstyle.css' dosyası ile logo bu klasörde barındırılmalıdır. Customstyle.css dosya içeriği sol üstteki logo için aşağıdaki şekilde olmalıdır.

.startupHeader {

    background-color: rgba(0, 0, 0, 0.6);
    height: 44px;
    min-width: 1000px;
    background-image: url(LogoAdi.png) !important;
    background-position: 10px center;
    background-repeat: no-repeat;
    background-size: 85px;
}

.top-menu-logo {
    
    background-color: rgba(0, 0, 0, 0.6);
    height: 44px;
    min-width: 1000px;
    background-image: url(LogoAdi.png) !important;
    background-position: 10px center;
    background-repeat: no-repeat;
    background-size: 85px;
}

eBA uygulamasının varsayılan logo'su ile değiştirilmek istenen logo üst üste binerse aşağıdaki ekleme yapılabilir.

.top-menu-logo {

    display: none;
}

![](https://docsbimser.blob.core.windows.net/imagecontainer/2-0fc6d87d-6afc-48ac-a405-41e6e90fae53.png)

