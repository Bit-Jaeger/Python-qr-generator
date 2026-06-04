import qrcode
import sys
import customtkinter as ctk


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)



def main():
    print(f"Welcome to the QR-Code Generator!")
    print(f"Do you want to customize size and color from your qr code? [Y/N]")
    prompt_custom_yn()





    # prompt user if code should be customized - color,border, ...
    def prompt_custom_yn():

        doCustom = input()
        if doCustom.lower() == "n":
            basic_qr()
        
        elif doCustom.lower() == "y":
            custom_qr()
        
        else:
            sys.exit("Please provide a valid answer: [Y/N]")

        # decide what function to call, when user decided

        

    def basic_qr():
        print(f"This will be the basic qr-code")
        return 0


    def custom_qr():
        print(f"Custom QR-Code will be generated.")
        return 0




    print(f"Do you want to customize size and color from your qr code? [Y/N]")
    prompt_custom_yn()









    #qr.add_data('Some data')
    #qr.make(fit=True)




    #img = qr.make_image(fill_color="black", back_color="white")



if __name__ == "__main__":
    main()