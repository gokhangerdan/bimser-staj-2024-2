# Kod İle Formun Kaydedilmesini İptal Etme

Client (ts) tarafında formun kaydedilmesini kodla iptal etmek için, formun OnBeforeSave eventinde aşağıdaki kodlar kullanılabilir.

	args.cancel = true;

## Not:

Yukarıdaki kodda, formun kaydedilmesi iptal edilmek istendiğinden, işlem OnBeforeSave 'de yapılmıştır. Herhangi bir nesnenin eventinde args.cancel işlemi yapılabilir.