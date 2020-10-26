import tkinter as tk
from PIL import ImageTk

self = tk.Tk()

#-----white background-----#
blank = ImageTk.PhotoImage(file="images/blankPage.png")
blankPage = tk.Label(self, image=blank)
blankPage.image = blank
blankPage.place(x=0, y=0)

#-----background image(pink border)-----#
background = ImageTk.PhotoImage(file="images/resistorBBG.png")
bbpBG = tk.Label(self, image=background)
bbpBG.image = background
bbpBG.place(x=-2, y=-2)

#-----resistor template-----#
resistor = ImageTk.PhotoImage(file="images/resistorImage.png")
resistorImage = tk.Label(self, image=resistor)
resistorImage.image = resistor
resistorImage.config(borderwidth=0)
resistorImage.place(x=380, y=100)

#-----ohm symbol-----#
ohm = ImageTk.PhotoImage(file="images/ohm.png")
ohmSymbol = tk.Label(self, image=ohm)
ohmSymbol.image = ohm
ohmSymbol.config(borderwidth=0)
ohmSymbol.place(x=550, y=254)

#-----plus over minus symbol-----#
plusMinus = ImageTk.PhotoImage(file="images/symbol.png")
plusMinusSymbol = tk.Label(self, image=plusMinus)
plusMinusSymbol.image = plusMinus
plusMinusSymbol.config(borderwidth=0)
plusMinusSymbol.place(x=595, y=254)

#-----labels (first digit to tolerance)-----#
firstLabel = tk.Label(self, text="1st Digit", font=("Calibri", 13, "bold"), fg="#fb0668",
                      background="#ffffff")
firstLabel.place(x=40, y=73)

secondLabel = tk.Label(self, text="2nd Digit", font=("Calibri", 13, "bold"), fg="#fb0668",
                       background="#ffffff")
secondLabel.place(x=120, y=73)

multiplierLabel = tk.Label(self, text="Multiplier", font=("Calibri", 13, "bold"), fg="#fb0668",
                           background="#ffffff")
multiplierLabel.place(x=200, y=73)

toleranceLabel = tk.Label(self, text="Tolerance", font=("Calibri", 13, "bold"), fg="#fb0668",
                          background="#ffffff")
toleranceLabel.place(x=280, y=73)

#-----label for number zero (used when the first and second digit where zero)-----#
zeroLabel = tk.Label(self, text="", font=("Calibri", 30, "bold"), fg="#fb0668",
                     background="#ffffff")
zeroLabel.place(x=478, y=244)

#-----label for a point symbol-----#
pointLabel = tk.Label(self, text="", font=("Calibri", 27, "bold"), fg="#fb0668",
                      background="#ffffff")
pointLabel.place(x=498, y=244)

#-----default values of resistor when first run-----#
firstBandLabel = tk.Label(self, text="1", font=("Calibri", 30, "bold"), fg="#fb0668",
                          background="#ffffff")
firstBandLabel.place(x=473, y=240)

secondBandLabel = tk.Label(self, text="2", font=("Calibri", 30, "bold"), fg="#fb0668",
                           background="#ffffff")
secondBandLabel.place(x=495, y=240)

thirdBandLabel = tk.Label(self, text="k", font=("Calibri", 30, "bold"), fg="#fb0668",
                          background="#ffffff")
thirdBandLabel.place(x=518, y=240)

fourthBandLabel = tk.Label(self, text="5%", font=("Calibri", 30, "bold"), fg="#fb0668",
                           background="#ffffff")
fourthBandLabel.place(x=615, y=240)

#-----maximum and minimum labels (beneath the resistor value)-----#
minimumValueLabel = tk.Label(self, text="Minimum Value: 11,400 ohms", font=("Calibri", 20, "bold"), fg="#fb0668",
                             background="#ffffff")
minimumValueLabel.place(x=400, y=340)

maximumValueLabel = tk.Label(self, text="Maximum Value: 12,600 ohms", font=("Calibri", 20, "bold"), fg="#fb0668",
                             background="#ffffff")
maximumValueLabel.place(x=400, y=380)

#-----importing all color bands from first to fourth band-----#
firstBand0 = ImageTk.PhotoImage(file="images/firstBand0.png")
firstBand1 = ImageTk.PhotoImage(file="images/firstBand1.png")
firstBand2 = ImageTk.PhotoImage(file="images/firstBand2.png")
firstBand3 = ImageTk.PhotoImage(file="images/firstBand3.png")
firstBand4 = ImageTk.PhotoImage(file="images/firstBand4.png")
firstBand5 = ImageTk.PhotoImage(file="images/firstBand5.png")
firstBand6 = ImageTk.PhotoImage(file="images/firstBand6.png")
firstBand7 = ImageTk.PhotoImage(file="images/firstBand7.png")
firstBand8 = ImageTk.PhotoImage(file="images/firstBand8.png")
firstBand9 = ImageTk.PhotoImage(file="images/firstBand9.png")
secondBand0 = ImageTk.PhotoImage(file="images/secondBand0.png")
secondBand1 = ImageTk.PhotoImage(file="images/secondBand1.png")
secondBand2 = ImageTk.PhotoImage(file="images/secondBand2.png")
secondBand3 = ImageTk.PhotoImage(file="images/secondBand3.png")
secondBand4 = ImageTk.PhotoImage(file="images/secondBand4.png")
secondBand5 = ImageTk.PhotoImage(file="images/secondBand5.png")
secondBand6 = ImageTk.PhotoImage(file="images/secondBand6.png")
secondBand7 = ImageTk.PhotoImage(file="images/secondBand7.png")
secondBand8 = ImageTk.PhotoImage(file="images/secondBand8.png")
secondBand9 = ImageTk.PhotoImage(file="images/secondBand9.png")
thirdBand0 = ImageTk.PhotoImage(file="images/thirdBand0.png")
thirdBand1 = ImageTk.PhotoImage(file="images/thirdBand1.png")
thirdBand2 = ImageTk.PhotoImage(file="images/thirdBand2.png")
thirdBand3 = ImageTk.PhotoImage(file="images/thirdBand3.png")
thirdBand4 = ImageTk.PhotoImage(file="images/thirdBand4.png")
thirdBand5 = ImageTk.PhotoImage(file="images/thirdBand5.png")
thirdBand6 = ImageTk.PhotoImage(file="images/thirdBand6.png")
thirdBand7 = ImageTk.PhotoImage(file="images/thirdBand7.png")
thirdBand8 = ImageTk.PhotoImage(file="images/thirdBand8.png")
thirdBand9 = ImageTk.PhotoImage(file="images/thirdBand9.png")
thirdBandGold = ImageTk.PhotoImage(file="images/thirdBandGold.png")
thirdBandSilver = ImageTk.PhotoImage(file="images/thirdBandSilver.png")
fourthBand = ImageTk.PhotoImage(file="images/fourthBand.png")
fourthBand1 = ImageTk.PhotoImage(file="images/fourthBand1.png")
fourthBand2 = ImageTk.PhotoImage(file="images/fourthBand2.png")
fourthBandGold = ImageTk.PhotoImage(file="images/fourthBandGold.png")
fourthBandSilver = ImageTk.PhotoImage(file="images/fourthBandSilver.png")

#-----setting up the default value of the resistor as well as placing it into the resistor image-----#
firstBandColor = tk.Label(self, image=firstBand1, background="#ffffff")
firstBandColor.image = firstBand1
firstBandColor.config(borderwidth=0)
firstBandColor.place(x=485, y=118)
secondBandColor = tk.Label(self, image=secondBand2, background="#ffffff")
secondBandColor.image = secondBand2
secondBandColor.config(borderwidth=0)
secondBandColor.place(x=523, y=126)
thirdBandColor = tk.Label(self, image=thirdBand3, background="#ffffff")
thirdBandColor.image = thirdBand3
thirdBandColor.config(borderwidth=0)
thirdBandColor.place(x=566, y=129)
fourthBandColor = tk.Label(self, image=fourthBandGold, background="#ffffff")
fourthBandColor.image = fourthBandGold
fourthBandColor.config(borderwidth=0)
fourthBandColor.place(x=646, y=119)

#-----default values (used later)-----#
self.firstBandValue = 1             #brown
self.secondBandValue = 2            #red
self.multiplierValue = 1000         #orange
self.toleranceValue = 0.05          #gold
self.multiplierChecker = True       #multiplier in thousands
self.decimalChecker = False         #multiplier in decimals(last two bands)
self.millionChecker = False         #multiplier is in millions
self.gigaChecker = False            #multiplier is in gigamillion

#-----the image was used to cover up the values and replace with zero value-----#
cover = ImageTk.PhotoImage(file="images/magic.png")
coverImage = tk.Label(self, image=cover)
coverImage.image = cover
coverImage.config(borderwidth=0)

#-----these are the labels used when the first and second digit were zero-----#
#-----ex: first and second digit are zero; the display would be 00 not 0-----#
secondBandLabel2 = tk.Label(self, text="0", font=("Calibri", 30, "bold"), fg="#fb0668",
                            background="#ffffff")

fourthBandLabel2 = tk.Label(self, text="5%", font=("Calibri", 30, "bold"), fg="#fb0668",
                            background="#ffffff")

#-----symbols for the same reason as above-----#
ohm2 = ImageTk.PhotoImage(file="images/ohm.png")
ohmSymbol2 = tk.Label(self, image=ohm2)
ohmSymbol2.image = ohm2
ohmSymbol2.config(borderwidth=0)

plusMinus2 = ImageTk.PhotoImage(file="images/symbol.png")
plusMinusSymbol2 = tk.Label(self, image=plusMinus2)
plusMinusSymbol2.image = plusMinus2
plusMinusSymbol2.config(borderwidth=0)

#-----function for determining the minimum and maximum value-----#
#-----calculated using the referenced values (with self variables)-----#
def minimumMaximum():
    nominalValue = (int(str(self.firstBandValue) + str(self.secondBandValue))) * self.multiplierValue
    toleranceValue = nominalValue * self.toleranceValue
    # -----checking the multiplier value  for correct calculation and  unit at the end-----#
    if self.multiplierChecker:
        minimumValue = "{:,d}".format(int(nominalValue - toleranceValue))
        maximumValue = "{:,d}".format(int(nominalValue + toleranceValue))
        minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + " ohms")
        maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + " ohms")
    elif self.gigaChecker:
        minimumValue = (nominalValue - toleranceValue) / 1000000000
        maximumValue = (nominalValue + toleranceValue) / 1000000000
        minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + "G ohms")
        maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + "G ohms")
    elif self.millionChecker:
        minimumValue = (nominalValue - toleranceValue) / 1000000
        maximumValue = (nominalValue + toleranceValue) / 1000000
        minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + "M ohms")
        maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + "M ohms")
    elif self.decimalChecker:
        minimumValue = "{:.3f}".format(nominalValue - toleranceValue)
        maximumValue = "{:.3f}".format(nominalValue + toleranceValue)
        minimumValueLabel.configure(text="Minimum Value: " + minimumValue + " ohms")
        maximumValueLabel.configure(text="Maximum Value: " + maximumValue + " ohms")
    else:
        minimumValue = nominalValue - toleranceValue
        maximumValue = nominalValue + toleranceValue
        minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + " ohms")
        maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + " ohms")
    if self.firstBandValue == 9 and self.secondBandValue == 9 and self.multiplierValue == 10000000:
        maximumValue = (nominalValue + toleranceValue) / 1000000000
        maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + "G ohms")

"""
-----function for setting the band color and value after button click-----
value = value of resistor from 1 to 10
color = color of the resistor based on the button clicked (this is an image)
multi = multiplier value
percent = tolerance
"""

def firstDigit(value, color):
    firstBandColor.configure(image=color)
    firstBandLabel.configure(text=value)
    self.firstBandValue = value
    if self.firstBandValue == 0 and self.secondBandValue == 0:
        minimumValueLabel.configure(text="Minimum Value: 0 ohms")
        maximumValueLabel.configure(text="Maximum Value: 0 ohms")
        coverImage.place(x=465, y=244)
        secondBandLabel2.place(x=510, y=240)
        fourthBandLabel2.place(x=600, y=240)
        ohmSymbol2.place(x=540, y=254)
        plusMinusSymbol2.place(x=580, y=254)
    else:
        coverImage.place(x=1590, y=1254)
        secondBandLabel2.place(x=1515, y=1240)
        fourthBandLabel2.place(x=1625, y=1240)
        ohmSymbol2.place(x=1560, y=1254)
        plusMinusSymbol2.place(x=1605, y=1254)
    minimumMaximum()


def secondDigit(value, color):
    secondBandColor.configure(image=color)
    secondBandLabel.configure(text=value)
    self.secondBandValue = value
    if self.firstBandValue == 0 and self.secondBandValue == 0:
        minimumValueLabel.configure(text="Minimum Value: 0 ohms")
        maximumValueLabel.configure(text="Maximum Value: 0 ohms")
        coverImage.place(x=465, y=244)
        secondBandLabel2.place(x=510, y=240)
        fourthBandLabel2.place(x=600, y=240)
        ohmSymbol2.place(x=540, y=254)
        plusMinusSymbol2.place(x=580, y=254)
    else:
        coverImage.place(x=1590, y=1254)
        secondBandLabel2.place(x=1515, y=1240)
        fourthBandLabel2.place(x=1625, y=1240)
        ohmSymbol2.place(x=1560, y=1254)
        plusMinusSymbol2.place(x=1605, y=1254)
    minimumMaximum()
    if self.firstBandValue == 0 and self.multiplierValue != 0.1 and self.multiplierValue != 0.01 \
            and self.multiplierValue != 100 and self.multiplierValue != 100000 \
            and self.multiplierValue != 100000000:
        firstBandLabel.configure(text='')
    else:
        firstBandLabel.configure(text=self.firstBandValue)


def multiplier(value, color, multi):
    thirdBandColor.configure(image=color)
    if self.firstBandValue == 0 and self.secondBandValue == 0:
        minimumValueLabel.configure(text="Minimum Value: 0 ohms")
        maximumValueLabel.configure(text="Maximum Value: 0 ohms")
        coverImage.place(x=465, y=244)
        secondBandLabel2.place(x=510, y=240)
        fourthBandLabel2.place(x=600, y=240)
        ohmSymbol2.place(x=540, y=254)
        plusMinusSymbol2.place(x=580, y=254)
    else:
        if color == thirdBand0:
            self.multiplierValue = multi
            zeroLabel.place(x=1580, y=1254)
            ohmSymbol.place(x=550, y=254)
            plusMinusSymbol.place(x=590, y=254)
            pointLabel.place(x=408, y=244)
            pointLabel.configure(text='')
            firstBandLabel.place(x=493, y=240)
            secondBandLabel.place(x=515, y=240)
            thirdBandLabel.place(x=408, y=240)
            thirdBandLabel.configure(text='')
            fourthBandLabel.place(x=610, y=240)
            self.millionChecker = False
            self.decimalChecker = False
            self.multiplierChecker = False
            self.gigaChecker = False
            minimumMaximum()
        elif color == thirdBand1:
            self.multiplierValue = multi
            zeroLabel.place(x=1580, y=1254)
            ohmSymbol.place(x=550, y=254)
            plusMinusSymbol.place(x=595, y=254)
            pointLabel.place(x=498, y=244)
            pointLabel.configure(text='')
            firstBandLabel.place(x=473, y=240)
            secondBandLabel.place(x=495, y=240)
            thirdBandLabel.place(x=518, y=240)
            thirdBandLabel.configure(text=value)
            fourthBandLabel.place(x=615, y=240)
            self.millionChecker = False
            self.decimalChecker = False
            self.multiplierChecker = False
            self.gigaChecker = False
            minimumMaximum()
        elif color == thirdBand2:
            self.multiplierValue = multi
            zeroLabel.place(x=1580, y=1254)
            ohmSymbol.place(x=560, y=254)
            plusMinusSymbol.place(x=605, y=254)
            pointLabel.place(x=491, y=244)
            pointLabel.configure(text='.')
            firstBandLabel.place(x=471, y=240)
            secondBandLabel.place(x=505, y=240)
            thirdBandLabel.place(x=528, y=240)
            thirdBandLabel.configure(text=value)
            fourthBandLabel.place(x=625, y=240)
            self.millionChecker = False
            self.decimalChecker = False
            self.multiplierChecker = True
            self.gigaChecker = False
            nominalValue = (int(str(self.firstBandValue) + str(self.secondBandValue))) * self.multiplierValue
            toleranceValue = nominalValue * self.toleranceValue
            minimumValue = "{:,d}".format(int(nominalValue - toleranceValue))
            maximumValue = "{:,d}".format(int(nominalValue + toleranceValue))
            minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + " ohms")
            maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + " ohms")
        elif color == thirdBand3:
            self.multiplierValue = multi
            zeroLabel.place(x=1580, y=1254)
            ohmSymbol.place(x=550, y=254)
            plusMinusSymbol.place(x=595, y=254)
            pointLabel.place(x=481, y=244)
            pointLabel.configure(text='')
            firstBandLabel.place(x=473, y=240)
            secondBandLabel.place(x=495, y=240)
            thirdBandLabel.place(x=518, y=240)
            thirdBandLabel.configure(text=value)
            fourthBandLabel.place(x=615, y=240)
            self.millionChecker = False
            self.decimalChecker = False
            self.multiplierChecker = True
            self.gigaChecker = False
            nominalValue = (int(str(self.firstBandValue) + str(self.secondBandValue))) * self.multiplierValue
            toleranceValue = nominalValue * self.toleranceValue
            minimumValue = "{:,d}".format(int(nominalValue - toleranceValue))
            maximumValue = "{:,d}".format(int(nominalValue + toleranceValue))
            minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + " ohms")
            maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + " ohms")
        elif color == thirdBand4:
            self.multiplierValue = multi
            zeroLabel.place(x=1580, y=1254)
            ohmSymbol.place(x=563, y=254)
            plusMinusSymbol.place(x=605, y=254)
            pointLabel.place(x=491, y=244)
            pointLabel.configure(text='')
            firstBandLabel.place(x=473, y=240)
            secondBandLabel.place(x=495, y=240)
            thirdBandLabel.place(x=518, y=240)
            thirdBandLabel.configure(text=value)
            fourthBandLabel.place(x=625, y=240)
            self.millionChecker = False
            self.decimalChecker = False
            self.multiplierChecker = True
            self.gigaChecker = False
            nominalValue = (int(str(self.firstBandValue) + str(self.secondBandValue))) * self.multiplierValue
            toleranceValue = nominalValue * self.toleranceValue
            minimumValue = "{:,d}".format(int(nominalValue - toleranceValue))
            maximumValue = "{:,d}".format(int(nominalValue + toleranceValue))
            minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + " ohms")
            maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + " ohms")
        elif color == thirdBand5:
            self.multiplierValue = multi
            zeroLabel.place(x=1580, y=1254)
            ohmSymbol.place(x=568, y=254)
            plusMinusSymbol.place(x=610, y=254)
            pointLabel.place(x=483, y=244)
            pointLabel.configure(text='.')
            firstBandLabel.place(x=463, y=240)
            secondBandLabel.place(x=500, y=240)
            thirdBandLabel.place(x=523, y=240)
            thirdBandLabel.configure(text=value)
            fourthBandLabel.place(x=630, y=240)
            self.multiplierChecker = False
            self.decimalChecker = False
            self.millionChecker = True
            self.gigaChecker = False
            nominalValue = (int(str(self.firstBandValue) + str(self.secondBandValue))) * self.multiplierValue
            toleranceValue = nominalValue * self.toleranceValue
            minimumValue = (nominalValue - toleranceValue) / 1000000
            maximumValue = (nominalValue + toleranceValue) / 1000000
            minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + "M ohms")
            maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + "M ohms")
        elif color == thirdBand6:
            self.multiplierValue = multi
            zeroLabel.place(x=1580, y=1254)
            ohmSymbol.place(x=563, y=254)
            plusMinusSymbol.place(x=605, y=254)
            pointLabel.place(x=483, y=244)
            pointLabel.configure(text='')
            firstBandLabel.place(x=473, y=240)
            secondBandLabel.place(x=495, y=240)
            thirdBandLabel.place(x=518, y=240)
            thirdBandLabel.configure(text=value)
            fourthBandLabel.place(x=625, y=240)
            self.multiplierChecker = False
            self.decimalChecker = False
            self.millionChecker = True
            self.gigaChecker = False
            nominalValue = (int(str(self.firstBandValue) + str(self.secondBandValue))) * self.multiplierValue
            toleranceValue = nominalValue * self.toleranceValue
            minimumValue = (nominalValue - toleranceValue) / 1000000
            maximumValue = (nominalValue + toleranceValue) / 1000000
            minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + "M ohms")
            maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + "M ohms")
        elif color == thirdBand7:
            self.multiplierValue = multi
            zeroLabel.place(x=1580, y=1254)
            ohmSymbol.place(x=568, y=254)
            plusMinusSymbol.place(x=610, y=254)
            pointLabel.place(x=483, y=244)
            firstBandLabel.place(x=463, y=240)
            secondBandLabel.place(x=485, y=240)
            thirdBandLabel.place(x=508, y=240)
            thirdBandLabel.configure(text=value)
            fourthBandLabel.place(x=630, y=240)
            self.multiplierChecker = False
            self.decimalChecker = False
            self.millionChecker = True
            self.gigaChecker = False
            nominalValue = (int(str(self.firstBandValue) + str(self.secondBandValue))) * self.multiplierValue
            toleranceValue = nominalValue * self.toleranceValue
            minimumValue = (nominalValue - toleranceValue) / 1000000
            maximumValue = (nominalValue + toleranceValue) / 1000000
            minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + "M ohms")
            maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + "M ohms")
            if self.firstBandValue == 9 and self.secondBandValue == 9 and self.multiplierValue == 10000000:
                maximumValue = (nominalValue + toleranceValue) / 1000000000
                maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + "G ohms")
        elif color == thirdBand8:
            self.multiplierValue = multi
            zeroLabel.place(x=1580, y=1254)
            ohmSymbol.place(x=563, y=254)
            plusMinusSymbol.place(x=605, y=254)
            pointLabel.place(x=488, y=244)
            pointLabel.configure(text='.')
            firstBandLabel.place(x=468, y=240)
            secondBandLabel.place(x=500, y=240)
            thirdBandLabel.place(x=523, y=240)
            thirdBandLabel.configure(text=value)
            fourthBandLabel.place(x=625, y=240)
            self.multiplierChecker = False
            self.decimalChecker = False
            self.millionChecker = False
            self.gigaChecker = True
            nominalValue = (int(str(self.firstBandValue) + str(self.secondBandValue))) * self.multiplierValue
            toleranceValue = nominalValue * self.toleranceValue
            minimumValue = (nominalValue - toleranceValue) / 1000000000
            maximumValue = (nominalValue + toleranceValue) / 1000000000
            minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + "G ohms")
            maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + "G ohms")
        elif color == thirdBand9:
            self.multiplierValue = multi
            zeroLabel.place(x=1580, y=1254)
            ohmSymbol.place(x=563, y=254)
            plusMinusSymbol.place(x=605, y=254)
            pointLabel.place(x=488, y=244)
            pointLabel.configure(text='')
            firstBandLabel.place(x=478, y=240)
            secondBandLabel.place(x=500, y=240)
            thirdBandLabel.place(x=523, y=240)
            thirdBandLabel.configure(text=value)
            fourthBandLabel.place(x=625, y=240)
            self.gigaChecker = True
            self.multiplierChecker = False
            self.decimalChecker = False
            self.millionChecker = False
            nominalValue = (int(str(self.firstBandValue) + str(self.secondBandValue))) * self.multiplierValue
            toleranceValue = nominalValue * self.toleranceValue
            minimumValue = (nominalValue - toleranceValue) / 1000000000
            maximumValue = (nominalValue + toleranceValue) / 1000000000
            minimumValueLabel.configure(text="Minimum Value: " + str(minimumValue) + "G ohms")
            maximumValueLabel.configure(text="Maximum Value: " + str(maximumValue) + "G ohms")
        elif color == thirdBandGold:
            firstBandLabel.configure(text=self.firstBandValue)
            self.multiplierValue = multi
            ohmSymbol.place(x=553, y=254)
            plusMinusSymbol.place(x=595, y=254)
            zeroLabel.place(x=1713, y=1244)
            pointLabel.place(x=510, y=244)
            pointLabel.configure(text='.')
            firstBandLabel.place(x=485, y=240)
            secondBandLabel.place(x=523, y=240)
            thirdBandLabel.place(x=713, y=240)
            thirdBandLabel.configure(text='')
            fourthBandLabel.place(x=615, y=240)
            self.multiplierChecker = False
            self.decimalChecker = True
            self.millionChecker = False
            self.gigaChecker = False
            nominalValue = (int(str(self.firstBandValue) + str(self.secondBandValue))) * self.multiplierValue
            toleranceValue = nominalValue * self.toleranceValue
            minimumValue = "{:.3f}".format(nominalValue - toleranceValue)
            maximumValue = "{:.3f}".format(nominalValue + toleranceValue)
            minimumValueLabel.configure(text="Minimum Value: " + minimumValue + " ohms")
            maximumValueLabel.configure(text="Maximum Value: " + maximumValue + " ohms")
        else:
            self.multiplierValue = multi
            ohmSymbol.place(x=563, y=254)
            plusMinusSymbol.place(x=605, y=254)
            zeroLabel.place(x=475, y=240)
            zeroLabel.configure(text='0')
            pointLabel.place(x=498, y=244)
            pointLabel.configure(text='.')
            firstBandLabel.place(x=510, y=240)
            secondBandLabel.place(x=533, y=240)
            thirdBandLabel.place(x=713, y=240)
            thirdBandLabel.configure(text='')
            fourthBandLabel.place(x=625, y=240)
            self.multiplierChecker = False
            self.decimalChecker = True
            self.millionChecker = False
            self.gigaChecker = False
            nominalValue = (int(str(self.firstBandValue) + str(self.secondBandValue))) * self.multiplierValue
            toleranceValue = nominalValue * self.toleranceValue
            minimumValue = "{:.3f}".format(nominalValue - toleranceValue)
            maximumValue = "{:.3f}".format(nominalValue + toleranceValue)
            minimumValueLabel.configure(text="Minimum Value: " + minimumValue + " ohms")
            maximumValueLabel.configure(text="Maximum Value: " + maximumValue + " ohms")
        if self.firstBandValue == 0 and self.multiplierValue != 0.1 and self.multiplierValue != 0.01 \
                and self.multiplierValue != 100 and self.multiplierValue != 100000 \
                and self.multiplierValue != 100000000:
            firstBandLabel.configure(text='')
        else:
            firstBandLabel.configure(text=self.firstBandValue)


def tolerance(value, color, percent):
    self.toleranceValue = value
    fourthBandColor.configure(image=color)
    fourthBandLabel.configure(text=str(percent) + '%')
    fourthBandLabel2.configure(text=str(percent) + '%')
    minimumMaximum()

#all the buttons
first0 = ImageTk.PhotoImage(file="images/digit0.png")
button = tk.Button(self, image=first0)
button.image = first0
first0Button = tk.Button(self, image=first0, command=lambda: firstDigit(0, firstBand0))
first0Button.place(x=38, y=100)

first1 = ImageTk.PhotoImage(file="images/digit1.png")
button = tk.Button(self, image=first1)
button.image = first1
first1Button = tk.Button(self, image=first1, command=lambda: firstDigit(1, firstBand1))
first1Button.place(x=38, y=133)

first2 = ImageTk.PhotoImage(file="images/digit2.png")
button = tk.Button(self, image=first2)
button.image = first2
first2Button = tk.Button(self, image=first2, command=lambda: firstDigit(2, firstBand2))
first2Button.place(x=38, y=166)

first3 = ImageTk.PhotoImage(file="images/digit3.png")
button = tk.Button(self, image=first3)
button.image = first3
first3Button = tk.Button(self, image=first3, command=lambda: firstDigit(3, firstBand3))
first3Button.place(x=38, y=199)

first4 = ImageTk.PhotoImage(file="images/digit4.png")
button = tk.Button(self, image=first4)
button.image = first4
first4Button = tk.Button(self, image=first4, command=lambda: firstDigit(4, firstBand4))
first4Button.place(x=38, y=232)

first5 = ImageTk.PhotoImage(file="images/digit5.png")
button = tk.Button(self, image=first5)
button.image = first5
first5Button = tk.Button(self, image=first5, command=lambda: firstDigit(5, firstBand5))
first5Button.place(x=38, y=265)

first6 = ImageTk.PhotoImage(file="images/digit6.png")
button = tk.Button(self, image=first6)
button.image = first6
first6Button = tk.Button(self, image=first6, command=lambda: firstDigit(6, firstBand6))
first6Button.place(x=38, y=298)

first7 = ImageTk.PhotoImage(file="images/digit7.png")
button = tk.Button(self, image=first7)
button.image = first7
first7Button = tk.Button(self, image=first7, command=lambda: firstDigit(7, firstBand7))
first7Button.place(x=38, y=331)

first8 = ImageTk.PhotoImage(file="images/digit8.png")
button = tk.Button(self, image=first8)
button.image = first8
first8Button = tk.Button(self, image=first8, command=lambda: firstDigit(8, firstBand8))
first8Button.place(x=38, y=364)

first9 = ImageTk.PhotoImage(file="images/digit9.png")
button = tk.Button(self, image=first9)
button.image = first9
first9Button = tk.Button(self, image=first9, command=lambda: firstDigit(9, firstBand9))
first9Button.place(x=38, y=397)

second0 = ImageTk.PhotoImage(file="images/digit0.png")
button = tk.Button(self, image=second0)
button.image = second0
second0Button = tk.Button(self, image=second0, command=lambda: secondDigit(0, secondBand0))
second0Button.place(x=120, y=100)

second1 = ImageTk.PhotoImage(file="images/digit1.png")
button = tk.Button(self, image=second1)
button.image = second1
second1Button = tk.Button(self, image=second1, command=lambda: secondDigit(1, secondBand1))
second1Button.place(x=120, y=133)

second2 = ImageTk.PhotoImage(file="images/digit2.png")
button = tk.Button(self, image=second2)
button.image = second2
second2Button = tk.Button(self, image=second2, command=lambda: secondDigit(2, secondBand2))
second2Button.place(x=120, y=166)

second3 = ImageTk.PhotoImage(file="images/digit3.png")
button = tk.Button(self, image=second3)
button.image = second3
second3Button = tk.Button(self, image=second3, command=lambda: secondDigit(3, secondBand3))
second3Button.place(x=120, y=199)

second4 = ImageTk.PhotoImage(file="images/digit4.png")
button = tk.Button(self, image=second4)
button.image = second4
second4Button = tk.Button(self, image=second4, command=lambda: secondDigit(4, secondBand4))
second4Button.place(x=120, y=232)

second5 = ImageTk.PhotoImage(file="images/digit5.png")
button = tk.Button(self, image=second5)
button.image = second5
second5Button = tk.Button(self, image=second5, command=lambda: secondDigit(5, secondBand5))
second5Button.place(x=120, y=265)

second6 = ImageTk.PhotoImage(file="images/digit6.png")
button = tk.Button(self, image=second6)
button.image = second6
second6Button = tk.Button(self, image=second6, command=lambda: secondDigit(6, secondBand6))
second6Button.place(x=120, y=298)

second7 = ImageTk.PhotoImage(file="images/digit7.png")
button = tk.Button(self, image=second7)
button.image = second7
second7Button = tk.Button(self, image=second7, command=lambda: secondDigit(7, secondBand7))
second7Button.place(x=120, y=331)

second8 = ImageTk.PhotoImage(file="images/digit8.png")
button = tk.Button(self, image=second8)
button.image = second8
second8Button = tk.Button(self, image=second8, command=lambda: secondDigit(8, secondBand8))
second8Button.place(x=120, y=364)

second9 = ImageTk.PhotoImage(file="images/digit9.png")
button = tk.Button(self, image=second9)
button.image = second9
second9Button = tk.Button(self, image=second9, command=lambda: secondDigit(9, secondBand9))
second9Button.place(x=120, y=397)

multiplier0 = ImageTk.PhotoImage(file="images/multiplier0.png")
button = tk.Button(self, image=multiplier0)
button.image = multiplier0
multiplier0Button = tk.Button(self, image=multiplier0, command=lambda: multiplier('', thirdBand0, 1))
multiplier0Button.place(x=200, y=100)

multiplier1 = ImageTk.PhotoImage(file="images/multiplier1.png")
button = tk.Button(self, image=multiplier1)
button.image = multiplier1
multiplier1Button = tk.Button(self, image=multiplier1, command=lambda: multiplier('0', thirdBand1, 10))
multiplier1Button.place(x=200, y=127)

multiplier2 = ImageTk.PhotoImage(file="images/multiplier2.png")
button = tk.Button(self, image=multiplier2)
button.image = multiplier2
multiplier2Button = tk.Button(self, image=multiplier2, command=lambda: multiplier('k', thirdBand2, 100))
multiplier2Button.place(x=200, y=154)

multiplier3 = ImageTk.PhotoImage(file="images/multiplier3.png")
button = tk.Button(self, image=multiplier3)
button.image = multiplier3
multiplier3Button = tk.Button(self, image=multiplier3, command=lambda: multiplier('k', thirdBand3, 1000))
multiplier3Button.place(x=200, y=181)

multiplier4 = ImageTk.PhotoImage(file="images/multiplier4.png")
button = tk.Button(self, image=multiplier4)
button.image = multiplier4
multiplier4Button = tk.Button(self, image=multiplier4, command=lambda: multiplier('0k', thirdBand4, 10000))
multiplier4Button.place(x=200, y=208)

multiplier5 = ImageTk.PhotoImage(file="images/multiplier5.png")
button = tk.Button(self, image=multiplier5)
button.image = multiplier5
multiplier5Button = tk.Button(self, image=multiplier5, command=lambda: multiplier('M', thirdBand5, 100000))
multiplier5Button.place(x=200, y=235)

multiplier6 = ImageTk.PhotoImage(file="images/multiplier6.png")
button = tk.Button(self, image=multiplier6)
button.image = multiplier6
multiplier6Button = tk.Button(self, image=multiplier6, command=lambda: multiplier('M', thirdBand6, 1000000))
multiplier6Button.place(x=200, y=262)

multiplier7 = ImageTk.PhotoImage(file="images/multiplier7.png")
button = tk.Button(self, image=multiplier7)
button.image = multiplier7
multiplier7Button = tk.Button(self, image=multiplier7, command=lambda: multiplier('0M', thirdBand7, 10000000))
multiplier7Button.place(x=200, y=289)

multiplier8 = ImageTk.PhotoImage(file="images/multiplier8.png")
button = tk.Button(self, image=multiplier8)
button.image = multiplier8
multiplier8Button = tk.Button(self, image=multiplier8, command=lambda: multiplier('G', thirdBand8, 100000000))
multiplier8Button.place(x=200, y=316)

multiplier9 = ImageTk.PhotoImage(file="images/multiplier9.png")
button = tk.Button(self, image=multiplier9)
button.image = multiplier9
multiplier9Button = tk.Button(self, image=multiplier9, command=lambda: multiplier('G', thirdBand9, 1000000000))
multiplier9Button.place(x=200, y=343)

multiplierGold = ImageTk.PhotoImage(file="images/multiplierGold.png")
button = tk.Button(self, image=multiplierGold)
button.image = multiplierGold
multiplierGoldButton = tk.Button(self, image=multiplierGold, command=lambda: multiplier(0.1, thirdBandGold, 0.1))
multiplierGoldButton.place(x=200, y=376)

multiplierSilver = ImageTk.PhotoImage(file="images/multiplierSilver.png")
button = tk.Button(self, image=multiplierSilver)
button.image = multiplierSilver
multiplierSilverButton = tk.Button(self, image=multiplierSilver,
                                   command=lambda: multiplier(0.01, thirdBandSilver, 0.01))
multiplierSilverButton.place(x=200, y=404)

toleranceBrown = ImageTk.PhotoImage(file="images/toleranceBrown.png")
button = tk.Button(self, image=toleranceBrown)
button.image = toleranceBrown
toleranceBrownButton = tk.Button(self, image=toleranceBrown, command=lambda: tolerance(0.01, fourthBand1, 1))
toleranceBrownButton.place(x=280, y=133)

toleranceRed = ImageTk.PhotoImage(file="images/toleranceRed.png")
button = tk.Button(self, image=toleranceRed)
button.image = toleranceRed
toleranceRedButton = tk.Button(self, image=toleranceRed, command=lambda: tolerance(0.02, fourthBand2, 2))
toleranceRedButton.place(x=280, y=166)

toleranceGold = ImageTk.PhotoImage(file="images/toleranceGold.png")
button = tk.Button(self, image=toleranceGold)
button.image = toleranceGold
toleranceGoldButton = tk.Button(self, image=toleranceGold, command=lambda: tolerance(0.05, fourthBandGold, 5))
toleranceGoldButton.place(x=280, y=331)

toleranceSilver = ImageTk.PhotoImage(file="images/toleranceSilver.png")
button = tk.Button(self, image=toleranceSilver)
button.image = toleranceSilver
toleranceSilverButton = tk.Button(self, image=toleranceSilver, command=lambda: tolerance(0.1, fourthBandSilver, 10))
toleranceSilverButton.place(x=280, y=364)

toleranceNone = ImageTk.PhotoImage(file="images/toleranceNone.png")
button = tk.Button(self, image=toleranceNone)
button.image = toleranceNone
toleranceNoneButton = tk.Button(self, image=toleranceNone, command=lambda: tolerance(0.2, fourthBand, 20))
toleranceNoneButton.place(x=280, y=397)

self.title("Resistor Color Coding")
self.geometry("800x454")
self.resizable(False,False)
self.mainloop()
