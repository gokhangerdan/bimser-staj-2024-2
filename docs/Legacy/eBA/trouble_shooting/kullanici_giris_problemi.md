# Kullanıcı Giriş Problemi

### Sorun

X sicil numaralı kullanıcı sisteme giriş yapamıyor ve login as olarak giriş yapmak istendiğinde listede gözükmüyor. Servis restart ettik düzelmedi.

### Çözüm

Kullanıcıya atanmış durumda olan Ünvan koduna bağlı bir Ünvan olmadığından system managerda ünvan kısmı boş gözüküyordu, değiştirmeyi denediğimizde "...derived or constant field" şeklinde sql hatası veriyordu. Kullanıcının ünvanını değiştirmeden pasife almaya çalıştığımızda Ünvan alanı zorunlu uyarısı yapıyordu. Ünvan koduna sahip bir ünvan oluşturup servis restart ettik, kullanıcı login as listesinde gözüktü.