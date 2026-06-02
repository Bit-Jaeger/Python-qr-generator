import qrcode


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


print(f"Do you want to customize size and color from your qr code? [Y/N]")
def prompt_custom_yn()



# prompt user if code should be customized - color,border, ...
def prompt_custom_yn(){

    doCustom = input()
    if(doCustom.lower() == "n"){
        basic_qr()
    }
    elif(doCustom.lower() == "y"){
        custom_qr()
    }
    else{
        print(f"Please provide a valid answer: [Y/N]")
    }
}






def basic_qr(){
    print(f"This will be the basic qr-code")
}

def custom_qr(){
    print(f"Custom QR-Code will be generated.")
}

#qr.add_data('Some data')
#qr.make(fit=True)




#img = qr.make_image(fill_color="black", back_color="white")