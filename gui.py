#gui
import ttkbootstrap as tb
import tensorflow as tf
import machine as mc
import numpy as np
from PIL import ImageTk, Image



dr='Stars.csv'
train_feature, test_feature, train_label, test_label, unique_label, unique_clss, unique_color, mean, scale = mc.data_process(dr)




def back(page2): #when back button
    for widget in page2.winfo_children(): #destroy all widget, reset page 2
        widget.destroy()
    page1.tkraise()

def button(): #when bush the button
    btn2 = tb.Button(page2, text="Back", command=lambda: back(page2))
    try: #try for error
        model_error = 1;
        model = tf.keras.models.load_model('star classification')
        model_error = 0;
        temp_val = float(temp.get()) #take in input
        lum_val = float(lum.get())
        rad_val = float(rad.get())
        mag_val = float(mag.get())
        clss_val = str(clss.get())
        color_val = str(color.get())
        test_feature1 = [temp_val, lum_val, rad_val, mag_val, color_val, clss_val] #put all input in an array
        input = mc.input_process(unique_clss, unique_color, mean, scale, test_feature1) #process input
        error = 0
    except:
        error=1

    if (error==0): #if no error
        predictions = model.predict(input) #predict using nerual network

        #interpret prediction
        predicted_label = np.argmax(predictions, axis=1) #highest possibility
        for i in predicted_label:
            resultant = unique_label[i]

        prdt = str(predictions[-1, predicted_label])
        np.set_printoptions(precision=2)

        #create canvas
        canvas = tb.Canvas(page2, width=600, height=350)
        canvas.pack(fill="both", expand=True)
        btn = tb.Button(canvas, text="Back", command=lambda: back(page2))

        #design using result
        if (resultant == 'Brown Dwarf'):
            canvas.create_image(0, 0, image=browndwarf, anchor="nw")

            canvas.create_text(300, 20, text=[resultant, prdt], font=("Helvetica", 20), fill="white")
            canvas.create_text( 300,150, text="Charasteristics of the star type: \n"
                                          "- Temperature: 2000 to 3500 K \n"
                                        "- Color: magenta, black, orange or red\n"
                                          "- Mass: 13 to 80 times that of Jupiter\n"
                                          "- Radius: from 0.64 to 1.13 times radius of the Jupiter\n"
                                          "- Luminosity: 1/100000 luminosity of the sun\n"
                                          "- Not big enough to sustain nuclear fusion of ordinary hydrogen into helium in their cores\n"
                                        "- As brown dwarfs do not undergo stable hydrogen fusion, they cool down over time, \n "
                                        "progressively passing through later spectral types as they age.\n"
                                        "- Example: 54 Piscium(0.79 radius of Jupiter), HN Pegasi(1.01 radius of Jupiter",font=("Helvetica",12), fill="white")
            btn_window=canvas.create_window(10,10,anchor="nw", window=btn)


        elif (resultant == 'Hypergiant'):
            canvas.create_image(0, 0, image=hypergiant, anchor="nw")

            canvas.create_text(300, 20, text=[resultant, prdt], font=("Helvetica bold", 20), fill="white")
            canvas.create_text(300,150,text="Charasteristics of the star type: \n "
                                        "- Temperature: 3,500 K to 35,000 K \n"
                                        "- Color: Blue, yellow, orange, red\n"
                                        "- Mass: more than 120 to 130 times mass of the sun \n"
                                        "- Radius: more than 1500 times radius of the sun\n"
                                        "- Luminosity: Between 1 million and 5 million times luminosity of the sun\n"
                                        "- A very rare type of star that has an extremely high luminosity, mass, size\n"
                                        " and mass loss because of its extreme stellar winds.\n"
                                        "- Example: WOH G64(1,540 times wider than the Sun), \n"
                                        "VY Canis Majoris(1,420 times wider than the Sun)", font=("Helvetica",13), fill="black")
            btn_window = canvas.create_window(10, 10, anchor="nw", window=btn)


        elif (resultant == 'Main Sequence'):
            canvas.create_image(0, 0, image=mainsequence, anchor="nw")


            canvas.create_text(300, 20, text=[resultant, prdt], font=("Helvetica bold", 20), fill="white")
            canvas.create_text(300,150,text="Charasteristics of the star type: \n"
                                        "- Temperature: 3000 to 30000 K, the sun is 5772 K \n"
                                        "- Color: Blue-white, yellow (sun), orange and red \n"
                                        "- Mass: 0.1 to 200 times mass of the sun \n"
                                        "- Radius: 0.1 to 12 times radius of the sun\n"
                                        "- Luminosity: 0.003 to 800000 times luminosity of the sun\n"
                                        "- Main sequence stars make up around 90% of the universe's stellar population\n"
                                        "- Example: the Sun", font=("Helvetica",13), fill="white")
            btn_window = canvas.create_window(10, 10, anchor="nw", window=btn)


        elif (resultant == 'Red Dwarf'):
            canvas.create_image(0, 0, image=reddwarf, anchor="nw")


            canvas.create_text(300, 20, text=[resultant, prdt], font=("Helvetica bold", 20), fill="white")
            canvas.create_text(300,150, text="Characteristics of the star type: \n"
                                        "- Temperature: 2000 to 3500 K \n"
                                        "- Color: Bright orange, red, black \n"
                                        "- Mass: 0.08 to 0.6 times mass of the sun \n"
                                        "- Radius: 0.09 to 1.26 times radius of the sun\n"
                                        "- Luminosity: 0.0001 to 0.1 times luminosity of the sun\n"
                                        "- A red dwarf is the smallest and coolest kind of star on the main sequence.\n"
                                        "- Red dwarfs are the most common type of star in the Milky Way\n"
                                        "- Red dwarfs cannot be easily observed \n as a result of their low luminosity\n"
                                        "- Examples: DH Tauri(largest known \n red dwarf of 1.26 times the radius of the sun", font=("Helvetica",13), fill="white")
            btn_window = canvas.create_window(10, 10, anchor="nw", window=btn)


        elif (resultant == 'Supergiant'):
            canvas.create_image(0, 0, image=supergiant, anchor="nw")


            canvas.create_text(300, 20, text=[resultant, prdt], font=("Helvetica bold", 20), fill="white")
            canvas.create_text( 300,150,text="Charasteristics of the star type: \n"
                                        "- Temperature: 3400 to 20000 K \n"
                                        "- Color: Red, blue \n"
                                        "- Mass: 8 to 12 times mass of the sun \n"
                                        "- Radius: 30 to 1000 times radius of the sun\n"
                                        "- Luminosity:  10,000 and 1 million times luminosity of the sun\n"
                                        "- Supergiants are among the most massive and most luminous stars\n"
                                        "- Examples: Rigel(the brightest star in the constellation Orion)", font=("Helvetica",13), fill="black")
            btn_window = canvas.create_window(10, 10, anchor="nw", window=btn)

        elif (resultant == 'White Dwarf'):
            canvas.create_image(0, 0, image=whitedwarf, anchor="nw")


            canvas.create_text(300, 20, text=[resultant, prdt], font=("Helvetica bold", 20), fill="white")
            canvas.create_text( 200,200,text="Charasteristics of the star type: \n"
                                          "- Temperature: 8,000 to 40,000 K \n"
                                          "- Color: Whitish-blue, yellow-orange \n"
                                          "- Mass: 0.17 to 1.33 times mass of the sun \n"
                                          "- Radius: 0.6 to 1.4 times radius of the sun\n"
                                          "- Luminosity: 0.04 times luminosity of the sun\n"
                                          "- A white dwarf is what stars like the Sun \n"
                                             "become after they have exhausted \n "
                                        "their nuclear fuel. \n "
                                        "- Near the end of its nuclear burning stage, "
                                             "\nthis type of star expels most of \n"
                                        "its outer material, creating a planetary nebula.\n"
                                        "- Example: Sirius B(closest white dwarf to Earth \nwith 8.6 light-year distance)", font=("Helvetica",13), fill="white")
            btn_window = canvas.create_window(10, 10, anchor="nw", window=btn)

    elif(error==1): #if error
        if(model_error==1):
            info = tb.Label(page2, text="Error! No trained model. Make sure buidmodel.exe is run first.")
        if(model_error==0):
            info = tb.Label(page2, text="Error! Please recheck your data.")
        info.pack(pady=10)
        btn2.pack(pady=10)



    page2.tkraise()

root =tb.Window(themename="superhero")
root.title("Star classification")
root.geometry('600x350')

page1=tb.Frame(root)
page2=tb.Frame(root)


#create 2 pages
page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")

#load image
browndwarf = ImageTk.PhotoImage(Image.open("browndwarf.jpg"))
hypergiant = ImageTk.PhotoImage(Image.open("hypergiant.jpg"))
mainsequence = ImageTk.PhotoImage(Image.open("mainsequence.jpg"))
reddwarf = ImageTk.PhotoImage(Image.open("reddwarf.jpg"))
supergiant = ImageTk.PhotoImage(Image.open("supergiant.jpg"))
whitedwarf = ImageTk.PhotoImage(Image.open("whitedwarf.jpg"))

# page1
# temperature
lab_temp = tb.Label(page1, text='Temperature (K)')
lab_temp.grid(row=1,column=0)
temp = tb.Entry(page1, bootstyle="danger")
temp.grid(row=2, column=0, pady=5)
# luminosity
lab_lum = tb.Label(page1, text='Luminosity (L/Lo)')
lab_lum.grid(row=3,column=0)
lum = tb.Entry(page1, bootstyle="warning")
lum.grid(row=4,column=0, pady=5)
# radius
lab_rad = tb.Label(page1, text='Radius (R/Ro)')
lab_rad.grid(row=5,column=0)
rad = tb.Entry(page1, bootstyle="dark")
rad.grid(row=6,column=0, pady=5)


# Magnitude
lab_mag = tb.Label(page1, text='Absolute magnitude (Mv)')
lab_mag.grid(row=1,column=1,padx=50)
mag = tb.Entry(page1, bootstyle="info")
mag.grid(row=2,column=1)

# Star category
lab_clss = tb.Label(page1, text='Spectral class')
lab_clss.grid(row=3,column=1)
clss = tb.Entry(page1, bootstyle="secondary")
clss.grid(row=4,column=1)

# Star color
lab_color = tb.Label(page1, text='Star color')
lab_color.grid(row=5,column=1)
color = tb.Entry(page1, bootstyle="light")
color.grid(row=6,column=1)

#button

btn1 = tb.Button(page1, text='Check', command = button)
btn1.grid(row=7,column=0,pady=20)



page1.tkraise()
root.mainloop()