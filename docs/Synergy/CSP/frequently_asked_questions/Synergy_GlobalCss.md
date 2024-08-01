
# Synergy Global CSS Güncelleme

Bu belge, Synergy uygulamasının global CSS stilini güncellemek için kullanılabilir. Synergy'nin CONFIGURATIONS tablosundaki `Web.Css` KEYNAME'ine CSS kodları ekleyerek bu değişiklikleri yapabilirsiniz.

## CSS Değişikliği Yapma

1. Synergy CONFIGURATIONS tablosuna erişin.
2. `Web.Css` KEYNAME'i bulun.
3. Yeni CSS stilini `Web.Css` KEYNAME'inin VALUE'sına ekleyin.
4. Değişikliklerinizi kaydedin.

Bu işlem, Synergy uygulamasının tüm sayfalarında global CSS stilini etkileyecektir.

## Örnek CSS Kodu

Login sayfasında bulunan Google Play Store ve App Store logolarını gizlemek için aşağıdaki CSS kodunu kullanabilirsiniz:

```css
div[class*="storeLinks"] {
    display: none !important;
}
```

Bu kod, class adı "storeLinks" içeren tüm div elementlerini sayfada gizleyecektir.
