# Koşullu CSS

```
 async Form1_OnLoad(args: Controls.EventArgs.ILoadEventArgs) {
        this.TextBox1.value == "test1" ? this.TextBox1.customClassName="özelSınıfınız": null;

    }
```

##  //textBox değeri test1 olduğunda, ilgili nesnenin customClassName özelliğine css tarafına eklemiş olduğunuz css tanımlamasını ekler ve formdaki görünümünü değiştirmiş olur.

