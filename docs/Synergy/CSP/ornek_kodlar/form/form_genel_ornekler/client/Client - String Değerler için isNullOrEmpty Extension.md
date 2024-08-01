# Client - String Değerler için isNullOrEmpty Extension

:::note

TypeScript'de form sınıfının dışına **_(export default class Form1 extends Form.Designer { })_** tanımlanması gerekmekte. Daha sonra **string** değişkenlerde **variable.isNullOrEmpty()** şeklinde kullanılabilir.

:::

```js
declare global {
    interface String {
            isNullOrEmpty(this: any): boolean;
    }
}

String.prototype.isNullOrEmpty = function (this: any): boolean {
    return isNullOrEmpty(this);
};

function isNullOrEmpty(value : any) : boolean {
    return value === undefined || value === null || value === "";
}
```
