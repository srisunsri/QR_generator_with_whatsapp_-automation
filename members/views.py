from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import qrcode
import pywhatkit
import important
import image
@ensure_csrf_cookie
#creTE

def members(request):
    return render(request,'index.html')

# Create your views here.
def product(request):
    qr = qrcode.QRCode(
        version=15,
        box_size=10,
        border=5
    )
    data=request.GET["na"]
    ph=request.GET["ph"]
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", black_color="white")
    img.save("text.png")

    pywhatkit.sendwhats_image(ph, "text.png", "Hai, This is the QR code that you are looking for.Have a nice day,Thankyou", 20)



