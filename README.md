AMAZON POLLY HESAP AYARLARI
Amazon hesabı oluşturduktan sonra aşağıdaki gibi Bir kullanıcı tanımlamalı ve gerekli izinler verilmelidir. Alınan anahtarlar ile daha sonra amazona bağlanarak gönderdiğimiz metinleri sese çevirip okuyacaktır. 

Aşağıdaki izinlerin verildiğinden emin olun. Verilmemiş ise köşedeki Add inline policy tuşuna basarak ekleyiniz.
•	AdministratorAccess
•	AmazonPollyReadOnlyAccess
•	AmazonPollyFullAccess

Daha sonra Access key ve secret access key anahtarlarınız alarak amazondaki bölümü tamamlıyoruz.
Şimdi amazon Polly kullanmak için boto3 kütüphanesini ekleyelim
pip install boto3

Projede kullandığımız formu oluşturmak için tkinter ses dosyalarını açmak için Pygame kütüphanesinde ekleyelim.
pip install pygame 
pip install tkinter
Yukardaki işlemler bittikten sonra anahtarları gerekli alanlara ekliyoruz
polly_client = boto3.Session(
               aws_access_key_id=”access_key”, 
               aws_secret_access_key='secret_access_key',
               region_name=’us-east-1’).client('polly')
response = polly_client.synthesize_speech(
                   VoiceId='Joanna',
                   OutputFormat='mp3',
                   Engine = 'neural', 
                   TextType = "ssml", 
                   Text = "<speak><prosody rate='90%'>TEXT</prosody></speak>")
 
Okunacak metni ses çevirdikten sonra belirtiğimiz dosya yolundaki klasöre ses dosyasını kaydediyoruz daha sonra bu ses dosyasını pygame ile oynatıyoruz
    new=str(random.randint(45, 500))+".mp3"
    with open('folder/'+new, 'wb') as file: 
       file.write(response['AudioStream'].read())
    mixer.init()
    mixer.music.load('folder/'+new) 
    mixer.music.play()
Metin textbox içine girildikten sonra seslendir tuşuna tıklandıktan kısa bir süre sonra metni okumaya başlayacaktır. Sesleri oluşturduğumuz dosya olan folder a kaydedip oradan oynatmaktadır.
