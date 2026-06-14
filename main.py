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
        return self.entry.get()

class Btn_GenQR_Frame(ctk.CTkFrame):
    #### solution for calling pass_qr to hand over all values when clicking the button: ####
    #### app hands over the function(pass_qr) and the button inherits this function, calls it when button is pressed, and app collects all data it needs ####
    def __init__(self, master, pass_qr):
        super().__init__(master, corner_radius=50)

        self.generate_btn = ctk.CTkButton(self, text="Generate QR", command=pass_qr)
        self.generate_btn.grid(row=2, column=2, padx=20, pady=20, sticky="n")
            
            
            
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
        

# _________ Slider for ForeGround Color QR ____________
class Slider_Group_Frame_bg(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=50)
        
        self.label = ctk.CTkLabel(self, text="Background:", font=ctk.CTkFont(size=20, weight="bold"), corner_radius = 50)
        self.label.grid(row=0,column=3, padx=20, pady=20, sticky="n")
        
                
        self.fg_canvas = ctk.CTkCanvas(self, height=20, width=20, bg="white")
        self.fg_canvas.grid(row=0, column=4, sticky="w")

        
        self.red_slider = ctk.CTkSlider(self, from_=0, to=255, command=self.on_slider_move_bg, progress_color=("white", "red"), button_color="white")
        self.red_slider.grid(row=1, column=3, padx=20, pady=20, sticky="n", columnspan=2)
        self.red_slider.set(255)

            
        self.green_slider = ctk.CTkSlider(self, from_=0, to=255, command=self.on_slider_move_bg, progress_color=("white", "green"), button_color="white")
        self.green_slider.grid(row=2, column=3, padx=20, pady=20, sticky="n", columnspan=2)
        self.green_slider.set(255)

            
        self.blue_slider = ctk.CTkSlider(self, from_=0, to=255, command=self.on_slider_move_bg, progress_color=("white", "blue"), button_color="white")
        self.blue_slider.grid(row=3, column=3, padx=20, pady=20, sticky="n", columnspan=2)
        self.blue_slider.set(255)
        
        # Creating rgb variable in object, to have easy access to it
        self.rgb_value_bg = (255, 255, 255)
            
            
    def on_slider_move_bg(self, value):
        r = int(self.red_slider.get())
        g = int(self.green_slider.get())
        b = int(self.blue_slider.get())
        
        # Update Canvas preview color -> for fun in HEX
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        self.fg_canvas.config(bg=hex_color)
        
        rgb_bg = (r, g, b)
        
        # Function to provide value in slider-object for App to have direct access to it!
        self.rgb_value_bg = rgb_bg
        



class Feedback_Label_Frame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master, corner_radius=50)
        self.Feedback = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=12, weight="bold"), corner_radius = 50)
        self.grid(row=3, column=3, padx=20, pady=20, sticky="n")
        
        def success():
            self.Feedback.configure(text="QR has been generated :)")




# ______ APP ________
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR-Code Generator")
        self.geometry("1000x800")
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        
        # Creating the Label frame off of parent class
        self.label_frame = Label_Frame(self)
        self.label_frame.grid(row=0, column=3, padx=20, pady=30, sticky="n", columnspan=1)


        self.entry = Entry_Frame(self)
        self.entry.grid(row=2, column=2, padx=20, pady=20, sticky="n")


        self.genQR = Btn_GenQR_Frame(self, self.pass_qr)
        self.genQR.grid(row=3, column=2, padx=20, pady=20, sticky="n")
        
        self.feedback = Feedback_Label_Frame(self)
        self.feedback.grid(row=2, column=3, padx=20, pady=20, sticky="n")
        
        
        ######## slider group Foreground #######
        self.slider_group = Slider_Group_Frame(self)
        self.slider_group.grid(row=2, column=4, padx=20, pady=20, sticky="n", columnspan=2, rowspan=5)
        
        ######## slider group Background #######
        self.slider_group2 = Slider_Group_Frame_bg(self)
        self.slider_group2.grid(row=4, column=4, padx=20, pady=20, sticky="n", columnspan=2, rowspan=5)
            
    
    ###### also passes other values!! #######
    def pass_qr(self):
    # COLLECT ALL VALUES
        url = self.entry.get_input_url()
        rgb = self.slider_group.rgb_value
        rgb_bg = self.slider_group2.rgb_value_bg
        filename = self.entry.get_entry_string()
        
        
    # HAND THEM OVER TO CREATION FUNCTION
        basic_qr(url, rgb, filename, rgb_bg)



        






def main():

    app = App()
    app.mainloop()


def basic_qr(url, rgb, filename, rgb_bg):
    print(f"basic_qr function gets value:{url}")
    qr.clear()
    qr.add_data(url)
    qr.make(fit=True)

    output_qr = qr.make_image(fill_color=rgb, back_color=rgb_bg)
    
    # check if filename is empty
    if(filename==""):
        filename = "output"
    
    #### check if filename is empty string -> then output.jpg #####
    output_qr.save(f"{filename}.jpg")
    ######### Give Feedback to the User inside of a label in the middle of the UI ###########
    print(f"QR Code successfully saved!")
    return True


if __name__ == "__main__":
    main()