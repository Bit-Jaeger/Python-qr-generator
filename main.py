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


        ###### url-entry #####
        self.entry = ctk.CTkEntry(self, placeholder_text="Paste URL here")
        self.entry.grid(row=1, column=2, padx= 20, pady=20, sticky="n", columnspan=3)

    

        
        self.filename_entry = ctk.CTkEntry(self, placeholder_text=">filename<.jpg")
        self.filename_entry.grid(row=2, column=2, padx=20, pady=20, sticky="n")
        
    def get_entry_string(self):
        return self.filename_entry.get()

        ####### functions ########
        #------ url ------#
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
    def __init__(self, master):
        super().__init__(master, corner_radius=50)
        
        self.label = ctk.CTkLabel(self, text="Foreground:", font=ctk.CTkFont(size=20, weight="bold"), corner_radius = 50)
        self.label.grid(row=0,column=3, padx=20, pady=20, sticky="n")
        
                
        self.fg_canvas = ctk.CTkCanvas(self, height=20, width=20, bg="black")
        self.fg_canvas.grid(row=0, column=4, sticky="w")

        
        self.red_slider = ctk.CTkSlider(self, from_=0, to=255, command=self.on_slider_move, progress_color=("white", "red"), button_color="white")
        self.red_slider.grid(row=1, column=3, padx=20, pady=20, sticky="n", columnspan=2)
        self.red_slider.set(0)

            
        self.green_slider = ctk.CTkSlider(self, from_=0, to=255, command=self.on_slider_move, progress_color=("white", "green"), button_color="white")
        self.green_slider.grid(row=2, column=3, padx=20, pady=20, sticky="n", columnspan=2)
        self.green_slider.set(0)

            
        self.blue_slider = ctk.CTkSlider(self, from_=0, to=255, command=self.on_slider_move, progress_color=("white", "blue"), button_color="white")
        self.blue_slider.grid(row=3, column=3, padx=20, pady=20, sticky="n", columnspan=2)
        self.blue_slider.set(0)
        
        # Creating rgb variable in object, to have easy access to it
        self.rgb_value = (0, 0, 0)
            
            
    def on_slider_move(self, value):
        r = int(self.red_slider.get())
        g = int(self.green_slider.get())
        b = int(self.blue_slider.get())
        
        # Update Canvas preview color -> for fun in HEX
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        self.fg_canvas.config(bg=hex_color)
        
        rgb = (r, g, b)
        
        # Function to provide value in slider-object for App to have direct access to it!
        self.rgb_value = rgb
        



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
        self.slider_group = Slider_Group_Frame(self)
        self.slider_group.grid(row=2, column=4, padx=20, pady=20, sticky="n", columnspan=2, rowspan=5)
        
            
    
    ###### also passes other values!! #######
    def pass_qr(self):
        url = self.entry.get_input_url()
        rgb = self.slider_group.rgb_value
        filename = self.entry.get_entry_string()
        basic_qr(url, rgb, filename)






def main():

    app = App()
    app.mainloop()


def basic_qr(url, rgb, filename):
    print(f"basic_qr function gets value:{url}")
    qr.clear()
    qr.add_data(url)
    qr.make(fit=True)

    output_qr = qr.make_image(fill_color=rgb, back_color="white")
    
    # check if filename is empty
    if(filename==""):
        filename = "output"
    
    #### check if filename is empty string -> then output.jpg #####
    output_qr.save(f"{filename}.jpg")
    print(f"QR Code successfully saved!")




if __name__ == "__main__":
    main()