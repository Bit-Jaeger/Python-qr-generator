import qrcode
import customtkinter as ctk


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

#Label should be displayed at all times
class Label_Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=50)

        self.label = ctk.CTkLabel(self, text="Jaeger's QR-Code Generator", font=ctk.CTkFont(size=20, weight="bold"), corner_radius = 50)
        self.label.grid(row=0, column=0, padx=20, pady=25, sticky="ew", columnspan=2)


#Creating segmented button used as main navigator
class Segmented_Button_Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
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


class Btn_GenQR_Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=50)

        self.generate_btn = ctk.CTkButton(self, text="Generate QR")
        self.generate_btn.grid(row=2, column=1, padx=20, pady=20, sticky="n")

    def generate_qr():
        print(f"Generating the QR-Code => Logic has to go here")










#Class creating the FRAMES
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





        self.entry_frame = Entry_Frame(self)
        self.entry_frame.grid(row=2, column=1, padx=20, pady=20, sticky="n")

        self.genQR_frame = Btn_GenQR_Frame(self)
        self.genQR_frame.grid(row=3, column=1, padx=20, pady=20, sticky="n")





        






def main():
    print(f"Welcome to the QR-Code Generator!")

    app = App()
    app.mainloop()






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