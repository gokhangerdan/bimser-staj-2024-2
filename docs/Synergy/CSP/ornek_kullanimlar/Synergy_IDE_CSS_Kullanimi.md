
# Synergy IDE Ortamında Harici CSS Dosyalarının Kullanımı

Bu dokümantasyon, Synergy IDE ortamında harici CSS dosyalarının form dosyalarında veya farklı bir CSS dosyasında nasıl kullanılacağını açıklamaktadır. Örnek olarak, `/asset/Styles/Loading.css` isimli bir dosyanın nasıl kullanılacağı gösterilecektir.

## 1. Başka Bir CSS Dosyasında Harici CSS Dosyasını Kullanma

Bir CSS dosyasını başka bir CSS dosyasında kullanmak için, `@import` kuralını kullanabilirsiniz. Örneğin, `/asset/Styles/Loading.css` dosyasını aynı klasör yapısında bulunan `BaseStyle.css` dosyasında kullanmak için:

```css
/* BaseStyle.css dosyasının en üstüne ekleyin */
@import url("./Loading.css");
```

Bu şekilde, `Loading.css` dosyasındaki tüm stiller `BaseStyle.css` dosyasına dahil edilecektir.

## 2. Form Dosyasında Harici CSS Dosyasını Kullanma

Bir formun CSS dosyasında başka bir CSS dosyasını kullanmak için de `@import` kuralını kullanabilirsiniz. Örneğin, `BaseStyle.css` dosyasını formun CSS dosyasına eklemek için:

```css
/* Form'un CSS dosyasının en üstüne ekleyin */
@import url("/asset/Styles/BaseStyle.css");
```

Bu şekilde, `BaseStyle.css` dosyasındaki tüm stiller formun CSS dosyasına dahil edilecektir.

### Örnek Senaryo

1. `/asset/Styles/Loading.css` dosyasının içeriği:

    ```css
    /* Loading.css */
    .loading-spinner {
        width: 50px;
        height: 50px;
        border: 5px solid #f3f3f3;
        border-radius: 50%;
        border-top: 5px solid #3498db;
        animation: spin 2s linear infinite;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    ```

2. `/asset/Styles/BaseStyle.css` dosyasının içeriği:

    ```css
    /* BaseStyle.css */
    @import url("./Loading.css");

    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
    }
    ```

3. Formun CSS dosyasının içeriği:

    ```css
    /* Form'un CSS dosyası */
    @import url("/asset/Styles/BaseStyle.css");

    .form-container {
        width: 100%;
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    ```

Bu örneklerde, `Loading.css` dosyasındaki stiller `BaseStyle.css` dosyasına dahil edilmiştir. Aynı şekilde, `BaseStyle.css` dosyasındaki stiller formun CSS dosyasına dahil edilmiştir. Bu sayede, tüm stiller hiyerarşik olarak birbirine dahil edilerek kullanılabilir.

## Sonuç

Synergy IDE ortamında, harici CSS dosyalarını başka bir CSS dosyasında veya formun CSS dosyasında kullanmak için `@import` kuralını kullanabilirsiniz. Bu yöntem, stil yönetimini daha modüler ve düzenli hale getirir.
