# Redisin Linux Ortama Kurulması

### LINUX ORTAMININ İNTERNETE BAĞLANDIĞINDAN-ÇIKTIĞINDAN EMİN OLUN! LINUX ORTAMININ EBA SUNUCUSUNUN ORTAMIYLA İLETİŞİME GEÇEBİLDİĞİNDEN, PİNG ATABİLDİĞİNDEN EMİN OLUN!

SSH'ı linux ortama kurmak için sırayla:

sudo apt update
sudo apt install openssh-server

Redis kurulumu için terminal açılır:

1- sudo apt-get install redis
2- sudo service redis status
3- sudo nano /etc/redis/redis.conf 

(Bu komut terminali bir nevi text editöre çevirecektir bind, save, password dahil ayarları yapın sonra ctrl+o ve peşine enter'a basarak kaydedin, ctrl+x ile text editörden çıkın)

4- sudo ufw status verbose 
Devrede değilse -> sudo ufw enabled (port bağlantıları otomatik bloklanmaya başlayabilir, ssh dahil, alttaki kural tanımlamalarından sonra da devreye alabilirsiniz)
Kurulu değilse -> sudo apt-get install ufw
5- sudo ufw allow {redisport}/tcp ---- Örn: sudo ufw allow 6379/tcp
6- sudo ufw allow 22/tcp (ssh portuna izin veriyoruz)
not: Daha detaylı kural tanımlamalarını internette bulabilirsiniz (örn. Spesifik IP'den gelen isteklere izin vermek gibi)
7- sudo service redis restart
8- sudo service redis-server restart
9- sudo service redis-server status

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd04ef94d-514a-45f9-a447-6a8c558e67e2)

### Redis flush için komut rehberi

Linux sistemde: 
redis-cli -h {redis bind ip} -p {redis port} -a {redis şifre} flushall
Örn: redis-cli -h 10.10.10.10 -p 6379 -a Bimser123 flushall

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16b2293a-eb6b-4774-8ffd-0fe25cf48552)

Windows sistemden admin cmd açıp linuxtaki redise: 
1- ssh linuxtakiusername@linuxIP
2- Şifreyi girin, şifreyi size göstermez ama terminale yazar
3- redis-cli -h {redis bind ip} -p {redis port} -a {redis şifre} flushall 
Örn: redis-cli -h 10.10.10.10 -p 6379 -a Bimser123 flushall
4- exit

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload141a89f0-5fec-4ef9-83af-77c6a9530540)

### Veya linux ortamında bash dosyası oluşturabilirsiniz

Terminale açın:

1- which bash (oluşturulacak dosyanın nereye gideceğini gösterir)
2- nano Flushall_Redis.sh (bu terminalde text editör açar. Üstteki flush bilgisini yazıp, ctrl+o ile kaydedip ctrl+x ile çıkın)
3- chmod +x Flushall_Redis.sh (bu yazdığınız texti çalıştırılabilir bash scripte dönüştürür)
4- ./Flushall_Redis.sh (Oluşturulan dosyayı çalıştırır)
(İsterseniz spesifik bir dosya yoluna da bash dosyası oluşturabilirsiniz. İnternette bulabilirsiniz.)

Windows ortamında da admin olarak cmd açıp:

1- ssh linuxusername@linuxIP
2- Şifreyi girin, şifreyi size göstermez ama terminale yazar
3- ./Flushall_Redis.sh (komut dosyasını çalıştırır)
4- exit (ssh'tan çıkar)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0204412-d620-441f-962d-3e96ae6e41fb)