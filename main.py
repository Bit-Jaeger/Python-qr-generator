import qrcode
import customtkinter as ctk

# ------ GENERATING LOGIC -------
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


# ------ UI LOGIC -------

# ______ Contents ________
#Label should be displayed at all times
class Label_Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=50)

        self.label = ctk.CTkLabel(self, text="Jaeger's QR-Code Generator", font=ctk.CTkFont(size=20, weight="bold"), corner_radius = 50)
        self.label.grid(row=0, column=0, padx=20, pady=25, sticky="ew", columnspan=2)

#Creating segmented button used as main navigator
class Segmented_Button_Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=50)
        self.seg_button = ctk.CTkSegmentedButton(self, corner_radius=50, values=["Entry", "Customize"], border_width=5, height=50, command=self.seg_btn_callback)
        self.seg_button.grid(row=1, column=1, sticky="n")
        self.seg_button.set("Entry")

    def seg_btn_callback(self, value):
        print(f"{value}")

#Seg_Button is on QR-Code
class Entry_Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=50)

        self.entry = ctk.CTkEntry(self, placeholder_text="Paste URL here")
        self.entry.grid(row=2, column=0, padx= 20, pady=20, sticky="n", columnspan=3)
    def get_input_url(self):
        print("get_input_url is being called!!")
        return self.entry.get()


class Btn_GenQR_Frame(ctk.CTkFrame):
    def __init__(self, master, event_generate):
        super().__init__(master, corner_radius=50)

        self.generate_btn = ctk.CTkButton(self, text="Generate QR", command=event_generate)
        self.generate_btn.grid(row=2, column=1, padx=20, pady=20, sticky="n")
        def event_generate():
            super().pass_qr()



# ______ Frames ________
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR-Code Generator")
        self.geometry("800x800")
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        
        # Creating the Label frame off of parent class
        self.label_frame = Label_Frame(self)
        self.label_frame.grid(row=0, column=1, padx=20, pady=30, sticky="n", columnspan=1)

        #Creating seg_btn
        self.seg_btn = Segmented_Button_Frame(self)
        self.seg_btn.grid(row=1, column=1, padx=20, pady=20, sticky="n")

        self.entry = Entry_Frame(self)
        self.entry.grid(row=2, column=1, padx=20, pady=20, sticky="n")

        self.genQR = Btn_GenQR_Frame(self, self.pass_qr)
        self.genQR.grid(row=3, column=1, padx=20, pady=20, sticky="n")
        
        
    def pass_qr(self):
        url = self.entry.get_input_url()
        basic_qr(url)





        






def main():

    app = App()
 
    app.mainloop()

   
        
    #current_input = app.entry.get_input_url()
    #basic_qr(current_input)
    
    
    


def basic_qr(url):
    print(f"This will be the basic qr-code")
    print(f"basic_qr functino gets value:{url}")








    #qr.add_data('Some data')
    #qr.make(fit=True)


    #img = qr.make_image(fill_color="black", back_color="white")


if __name__ == "__main__":
    main()