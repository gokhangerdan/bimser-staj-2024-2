# Süreçler Nasıl Pasif Edilir?

## Versiyon Yönetimi Kullanılıyorken Süreç Pasif Etme İşlemi

Pasif edilmesi istenen süreç, diğer süreçlerin modellerinde ilişkilendirilmişse pasif edilemez, önce ilişkiler kaldırılmalıdır. Ayrıca pasif edilmek istenen sürece ait alt süreç varsa önce alt süreçlerin silinmesi veya bu alt süreçlere ait üst süreç bilgilerinin temizlenmesi/değiştirilmesi gerekmektedir. Pasif etmeyi engelleyen bu durumlara dair bilgilendirme uygulama arayüzünden işlemi gerçekleştirirken görüntülenebilir.

Pasif etme işleminde onay akışı izlenmektedir, bu sebeple sürecin onay matrisi dolu olmalıdır. Süreç onaycılara iptal onayına gider. Onaylandığı durumda süreç pasif edilir ve pasif süreçler listesinde yer alır.

Süreçlerde yetkilendirme kullan parametresi aktif ise sadece süreçte yetkili olan kullanıcı tarafından pasif edilme işlemi gerçekleştirilebilir

## Versiyon Yönetimi Kullanılmıyorken

Versiyon yönetimi kullanılıyorken geçerli olan onay akışı bu durumda geçerli olmayacaktır. Süreç direkt pasif edilebilir. 
Süreçlerde yetkilendirme kullan parametresi aktif ise sadece süreçte yetkili olan kullanıcı tarafından pasif edilme işlemi gerçekleştirilebilir. Pasif edilme işlemi başarıyla gerçekleştirilmiş süreçler Pasif Süreçler listesinde yer alır.