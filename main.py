import qrcode
import customtkinter as ctk
from PIL import Image

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
        self.label.grid(row=0, column=3, padx=20, pady=25, sticky="n", columnspan=3)

#Creating segmented button used as main navigator
class Segmented_Button_Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=50)
        self.seg_button = ctk.CTkSegmentedButton(self, corner_radius=50, values=["Entry", "Customize"], border_width=5, height=50, command=self.seg_btn_callback)
        self.seg_button.grid(row=1, column=3, sticky="n")
        self.seg_button.set("Entry")

    def seg_btn_callback(self, value):
        print(f"{value}")

#Seg_Button is on QR-Code
class Entry_Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=50)

        self.entry = ctk.CTkEntry(self, placeholder_text="Paste URL here")
        self.entry.grid(row=2, column=2, padx= 20, pady=20, sticky="n", columnspan=3)
    def get_input_url(self):
        print("get_input_url is being called!!")
        return self.entry.get()


class Btn_GenQR_Frame(ctk.CTkFrame):
    def __init__(self, master, event_generate):
        super().__init__(master, corner_radius=50)

        self.generate_btn = ctk.CTkButton(self, text="Generate QR", command=event_generate)
        self.generate_btn.grid(row=2, column=2, padx=20, pady=20, sticky="n")
        def event_generate():
            super().pass_qr()
            
            
            
# _________ Slider for ForeGround Color QR ____________
class Slider_Group_Frame(ctk.CTkFrame):
    def __init__(self, master, red_slider_event, green_slider_event, blue_slider_event):
        super().__init__(master, corner_radius=50)
        
        self.label = ctk.CTkLabel(self, text="Foreground Color", font=ctk.CTkFont(size=20, weight="bold"), corner_radius = 50)
        self.label.grid(row=0,column=3, padx=20, pady=20, sticky="n")
        
        self.red_slider = ctk.CTkSlider(self, from_=0, to=255, command=red_slider_event, progress_color=("red", "red"), button_color="white", button_hover_color=("red", "red"))
        self.red_slider.grid(row=1, column=3, padx=20, pady=20, sticky="n", columnspan=2)
        def red_slider_event(value_red):
            super().red_slider_event(value_red)
            
        self.green_slider = ctk.CTkSlider(self, from_=0, to=255, command=green_slider_event, progress_color=("green", "green"), button_color="white", button_hover_color=("green", "green"))
        self.green_slider.grid(row=2, column=3, padx=20, pady=20, sticky="n", columnspan=2)
        def green_slider_event(value_green):
            super().green_slider_event(value_green)
            
        self.blue_slider = ctk.CTkSlider(self, from_=0, to=255, command=blue_slider_event, progress_color=("blue", "blue"), button_color="white", button_hover_color=("blue", "blue"))
        self.blue_slider.grid(row=3, column=3, padx=20, pady=20, sticky="n", columnspan=2)
        def blue_slider_event(value_blue):
            super().blue_slider_event(value_blue)



# ______ APP ________
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR-Code Generator")
        self.geometry("1000x600")
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        
        # Creating the Label frame off of parent class
        self.label_frame = Label_Frame(self)
        self.label_frame.grid(row=0, column=3, padx=20, pady=30, sticky="n", columnspan=1)

        #Creating seg_btn
        self.seg_btn = Segmented_Button_Frame(self)
        self.seg_btn.grid(row=1, column=3, padx=20, pady=20, sticky="n")

        self.entry = Entry_Frame(self)
        self.entry.grid(row=2, column=2, padx=20, pady=20, sticky="n")

        self.genQR = Btn_GenQR_Frame(self, self.pass_qr)
        self.genQR.grid(row=3, column=2, padx=20, pady=20, sticky="n")
        
        
        ######## slider group Foreground #######
        self.slider_group = Slider_Group_Frame(self, self.red_slider_event, self.green_slider_event, self.blue_slider_event)
        self.slider_group.grid(row=2, column=4, padx=20, pady=20, sticky="n", columnspan=2, rowspan=4)
        
        
    def red_slider_event(self, r_value):
        print(f"r:{r_value} in app")
        
    def green_slider_event(self, g_value):
        print(f"g:{g_value} in app")
        
    def blue_slider_event(self, b_value):
        print(f"b:{b_value} in app")
            
    
    
    
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
    print(f"basic_qr function gets value:{url}")
    qr.add_data(url)
    qr.make(fit=True)

    output_qr = qr.make_image(fill_color="black", back_color="white")
    output_qr.save("output.jpg")
    print(f"QR Code successfully saved!")







    #qr.add_data('Some data')
    #qr.make(fit=True)


    #img = qr.make_image(fill_color="black", back_color="white")


if __name__ == "__main__":
    main()