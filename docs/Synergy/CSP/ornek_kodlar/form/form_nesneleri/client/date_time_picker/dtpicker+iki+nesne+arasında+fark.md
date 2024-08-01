
# İki DateTimePicker arasında gün hesabı yapmak (Client)

```
const date1 = new Date(this.DateTimePicker1.value);
const date2 = new Date(this.DateTimePicker2.value);
const diffInTime = Math.abs(date2.getTime() - date1.getTime());
const diffInDays = Math.ceil(diffInTime / (1000 * 60 * 60 * 24));
console.log(diffInDays);
```
