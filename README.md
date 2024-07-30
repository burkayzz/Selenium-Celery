Bu Repo Celery-Selenium-Rabbitmq Kullanımı amacıyla birden fazla proje içermektedir 


1. Sel Projesi
   Proje veritabanındaki keywordler üzerinden ekşisözlükte arama yapar. Keyworde karşılık gelen aramalar içerisinde ilk 3 sayfa içerisinde paylaşımları ve buna dair bilgileri toplar ve veritabanına kaydeder.
   İlk 4 arama için bu veriyi yeni sayar fakat daha fazlası için bu verilerin yeniliği kaybolur.

2. Trends Projesi
   X'e giriş yapar ve trend paylaşımları kaydeder. Her sabah kullanıcıya günün trendlerinin olduğu bir haber maili gönderir.

3. Forex Projesi
   Döviz kurlarını Alpha Vantage apileri üzerinden alan ve bu bilgileri her 15 dakikada bir türkiyedeki güncel borsa saatleri içerisinde güncel kurları bildiren bir sistemdir.

4. Set theme Projesi
   Saat 20.00'da windowsun temasını göz sağlığını korumak adına karanlık moda alır - Saat 09.00'da ise windowsun temasını aydınlık moda alır ve kullanıcı deneyimini zenginleştirir.
   ( Proje windows tabanlı olması sebebiyle docker üzerinde çalışmayan komut setlerine sahiptir yalnızca demodur ) 
