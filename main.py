import qrcode
import sys
import customtkinter as ctk


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

class Label_Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text="Jaeger's QR-Code Generator", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=25, sticky="ew", columnspan=2)

class Entry_Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.entry = ctk.CTkEntry(self, placeholder_text="Paste URL here")
        self.entry.grid(row=1, column=0, padx= 20, pady=20, sticky="ew", columnspan=1)


class Options_Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        check_var = ctk.StringVar(value="off")
        self.checkbox = ctk.CTkCheckBox(self, text="Customize your QR?", command=allow_custom_qr, variable=check_var, onvalue="on", offvalue="off")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR-Code Generator")
        self.geometry("700x400")
        self.grid_columnconfigure((0, 1), weight=1)
        
        # Creating the Label frame off of parent class
        self.label_frame = Label_Frame(self)
        self.label_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", columnspan=2)

        self.entry_frame = Entry_Frame(self)
        self.entry_frame.grid(row=1, column=0, padx=20, pady= 20, sticky="nsew")

        self.customqr_frame = Options_Frame(self)
        self.customqr_frame.grid(row=1, column= 1, padx=20, pady=20, sticky="nw")





def main():
    print(f"Welcome to the QR-Code Generator!")


    app = App()
    app.mainloop()
    prompt_custom_yn()



def allow_custom_qr():
    #TODO: allow checkboxes/inputs for customizable qr-code (color, ...)
    return 0

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