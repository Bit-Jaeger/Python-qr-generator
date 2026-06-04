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
    prompt_custom_yn()

    #generate the UI 
    app = ctk.CTk()
    app.geometry("500x400")

    #config for Button
    button = ctk.CTkButton(app, text="Generate QR-Code", command=button_test)
    button.grid(row=0, column=0, padx=20, pady=20)



    app.mainloop()





def button_test():
    print(f"Button was pressed")

# prompt user if code should be customized
def prompt_custom_yn():

    print(f"Do you want to customize size and color from your qr code? [Y/N]")
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






    #qr.add_data('Some data')
    #qr.make(fit=True)




    #img = qr.make_image(fill_color="black", back_color="white")



if __name__ == "__main__":
    main()