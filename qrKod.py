import qrcode


data = "Merhaba, Qr Kod Oluşturmaya Hoşgeldin!"   #oluşturmak istediğiniz QR kodunun içeriğini belirliyorsunuz.


qr = qrcode.QRCode(             #    Şimdi, qrcode.QRCode sınıfını kullanarak bir QR kodu nesnesi oluşturuyorsunuz.     
    version=5,                  #  version parametresi QR kodunun versiyonunu, box_size parametresi kutu boyutunu ve border 
    box_size=15,                # parametresi de sınıra olan uzaklığı belirler. 
    border=3,
)
qr.add_data(data)    #yöntemi ile QR kodunun içine veriyi ekliyorsunuz.
qr.make(fit=True)    #make yöntemini kullanarak QR kodunu oluşturuyorsunuz. 
#fit=True parametresi, veriyi sığdırmak için otomatik boyutlandırmayı sağlar.
 
 
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

#QR kodunu oluşturduktan sonra, make_image yöntemi ile bir görüntü oluşturuyorsunuz.
# fill_color ve back_color parametreleri ile sırasıyla QR kodunun dolgu rengi ve arka plan rengini belirleyebilirsiniz


