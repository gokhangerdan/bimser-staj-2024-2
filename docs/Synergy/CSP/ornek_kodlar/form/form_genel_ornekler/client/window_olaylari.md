# Client'da Window Olaylarını Kullanmak (TypeScript)

## Constructor Yapısı

Örneğin constructor metodunda window resize olayını dinlemek için bir event listener ekliyoruz.

```
export default class ExampleClass extends Form.SYNERGY {
    constructor() {
        // Constructor içinde window resize olayını dinlemek için event listener ekliyoruz
        window.addEventListener("resize", this.handleResize.bind(this));
    }

    // Resize olayını işleyecek metodu tanımlıyoruz
    handleResize = () => {
        const windowWidth = window.innerWidth;
        console.log(Window genişliği: ${windowWidth}px);
    }
}
```

Constructor: Bu metod, sınıfın yeni bir örneği oluşturulduğunda çağrılır. Burada window.addEventListener kullanarak window resize olayını dinliyoruz ve bu olayı handleResize metodu ile ilişkilendiriyoruz.

handleResize Metodu: Bu metod, window yeniden boyutlandırıldığında çağrılır ve mevcut window genişliğini console.log ile yazdırır.

## Özet

Bu örnek, window olaylarını dinleyerek belirli işlemleri gerçekleştirmek için nasıl kullanabileceğinizi göstermektedir. Daha karmaşık senaryolar için bu temeli genişletebilirsiniz.

