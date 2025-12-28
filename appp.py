import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load Model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🚲 Bike Price Prediction App")
st.markdown("Enter the details to predict the bike selling price")

brand_dict = {'Activa': 0, 'Aprilia': 1, 'BMW': 2, 'Bajaj': 3, 'Benelli': 4, 'Harley': 5, 'Hero': 6, 'Honda': 7, 'Hyosung': 8, 'Jawa': 9, 'KTM': 10, 'Kawasaki': 11, 'Mahindra': 12, 'Royal': 13, 'Suzuki': 14, 'TVS': 15, 'UM': 16, 'Vespa': 17, 'Yamaha': 18, 'Yo': 19}
model_dict = {'Activa 3g': 0, 'Activa 4g': 1, 'Aprilia SR 125': 2, 'BMW G310GS': 3, 'Bajaj  ct 100': 4, 'Bajaj Avenger 150': 5, 'Bajaj Avenger 150 street': 6, 'Bajaj Avenger 220': 7, 'Bajaj Avenger 220 dtsi': 8, 'Bajaj Avenger Cruise 220': 9, 'Bajaj Avenger Street 150 [2018]': 10, 'Bajaj Avenger Street 160': 11, 'Bajaj Avenger Street 220': 12, 'Bajaj Avenger [2015]': 13, 'Bajaj Boxer': 14, 'Bajaj CT 100': 15, 'Bajaj CT 110': 16, 'Bajaj Discover 100': 17, 'Bajaj Discover 100 M': 18, 'Bajaj Discover 100 T': 19, 'Bajaj Discover 110': 20, 'Bajaj Discover 125': 21, 'Bajaj Discover 125 M': 22, 'Bajaj Discover 125 ST': 23, 'Bajaj Discover 135': 24, 'Bajaj Discover 150': 25, 'Bajaj Discover 150F': 26, 'Bajaj Discover 150S': 27, 'Bajaj Dominar 400': 28, 'Bajaj Dominar 400 [2018]': 29, 'Bajaj Kristal': 30, 'Bajaj Platina 100': 31, 'Bajaj Pulsar  NS 200': 32, 'Bajaj Pulsar 125': 33, 'Bajaj Pulsar 135 LS': 34, 'Bajaj Pulsar 150': 35, 'Bajaj Pulsar 150 [2001-2011]': 36, 'Bajaj Pulsar 180': 37, 'Bajaj Pulsar 180F': 38, 'Bajaj Pulsar 220 DTS-i': 39, 'Bajaj Pulsar 220 F': 40, 'Bajaj Pulsar 220 Fi': 41, 'Bajaj Pulsar 220F': 42, 'Bajaj Pulsar 220S': 43, 'Bajaj Pulsar AS150': 44, 'Bajaj Pulsar AS200': 45, 'Bajaj Pulsar NS 200': 46, 'Bajaj Pulsar NS160': 47, 'Bajaj Pulsar NS200': 48, 'Bajaj Pulsar RS 200': 49, 'Bajaj Pulsar RS200': 50, 'Bajaj Super': 51, 'Bajaj V12': 52, 'Bajaj V15': 53, 'Bajaj Xcd': 54, 'Benelli TNT 25': 55, 'Harley-Davidson Street 750': 56, 'Harley-Davidson Street Bob': 57, 'Hero  CBZ Xtreme': 58, 'Hero  Ignitor Disc': 59, 'Hero Achiever 150': 60, 'Hero CBZ': 61, 'Hero CD Dawn': 62, 'Hero CD Deluxe': 63, 'Hero Duet': 64, 'Hero Extreme': 65, 'Hero Glamour': 66, 'Hero Glamour 125': 67, 'Hero Glamour FI': 68, 'Hero HF Deluxe': 69, 'Hero HF Deluxe i3s': 70, 'Hero Honda Achiever': 71, 'Hero Honda CBZ': 72, 'Hero Honda CBZ extreme': 73, 'Hero Honda CD Deluxe': 74, 'Hero Honda CD100': 75, 'Hero Honda CD100SS': 76, 'Hero Honda Glamour': 77, 'Hero Honda Hunk': 78, 'Hero Honda Karizma': 79, 'Hero Honda Karizma ZMR [2010]': 80, 'Hero Honda Passion': 81, 'Hero Honda Passion PRO [2012]': 82, 'Hero Honda Passion Plus': 83, 'Hero Honda Passion Pro': 84, 'Hero Honda Pleasure': 85, 'Hero Honda Splendor': 86, 'Hero Honda Splendor NXG': 87, 'Hero Honda Splendor PRO': 88, 'Hero Honda Splendor Plus': 89, 'Hero Honda Street Smart': 90, 'Hero Honda Super Splendor [2005]': 91, 'Hero Hunk': 92, 'Hero Ignitor': 93, 'Hero Karizma 2014': 94, 'Hero Karizma ZMR': 95, 'Hero Karizma [2003-2014]': 96, 'Hero Maestro': 97, 'Hero Maestro Edge': 98, 'Hero Passion PRO TR': 99, 'Hero Passion PRO i3s': 100, 'Hero Passion Pro': 101, 'Hero Passion Pro 110': 102, 'Hero Passion X Pro [2016-2017]': 103, 'Hero Passion X pro': 104, 'Hero Passion XPro': 105, 'Hero Pleasure': 106, 'Hero Pleasure [2005-2015]': 107, 'Hero Splender Plus': 108, 'Hero Splender iSmart': 109, 'Hero Splendor NXG': 110, 'Hero Splendor PRO': 111, 'Hero Splendor Plus': 112, 'Hero Splendor Plus i3s': 113, 'Hero Splendor iSmart': 114, 'Hero Super Splendor': 115, 'Hero Xpulse 200': 116, 'Hero Xpulse 200T': 117, 'Hero Xtreme 200R': 118, 'Hero Xtreme 2014': 119, 'Hero Xtreme Sports': 120, 'Hero Xtreme [2013-2014]': 121, 'Honda Activa 125': 122, 'Honda Activa 125 [2016-2017]': 123, 'Honda Activa 3G': 124, 'Honda Activa 4G': 125, 'Honda Activa 5G': 126, 'Honda Activa [2000-2015]': 127, 'Honda Activa i': 128, 'Honda Activa i [2016-2017]': 129, 'Honda Aviator': 130, 'Honda CB Hornet 160R': 131, 'Honda CB Shine': 132, 'Honda CB Shine SP': 133, 'Honda CB Trigger': 134, 'Honda CB Twister': 135, 'Honda CB Unicorn': 136, 'Honda CB Unicorn 150': 137, 'Honda CB Unicorn 160': 138, 'Honda CB Unicorn Dazzler': 139, 'Honda CB twister': 140, 'Honda CBF Stunner': 141, 'Honda CBR 150': 142, 'Honda CBR-250R': 143, 'Honda CBR150 R': 144, 'Honda Dio': 145, 'Honda Dream Neo': 146, 'Honda Dream Yuga': 147, 'Honda Dream Yuga ': 148, 'Honda Grazia': 149, 'Honda Karizma': 150, 'Honda Livo': 151, 'Honda Navi': 152, 'Honda Navi [2016-2017]': 153, 'Honda Shine': 154, 'Honda X-Blade': 155, 'Hyosung GT250R': 156, 'Jawa 42': 157, 'Jawa Standard': 158, 'KTM 125 Duke': 159, 'KTM 200 Duke': 160, 'KTM 250 Duke': 161, 'KTM 390 Duke': 162, 'KTM 390 Duke ': 163, 'KTM 390 Duke ABS [2013-2016]': 164, 'KTM RC 200': 165, 'KTM RC 390': 166, 'KTM RC200': 167, 'KTM RC390': 168, 'Kawasaki Ninja 250R': 169, 'Kawasaki Ninja 300': 170, 'Kawasaki Ninja 650 [2018-2019]': 171, 'Mahindra Flyte': 172, 'Mahindra Gusto': 173, 'Mahindra Mojo XT300': 174, 'Mahindra Rodeo': 175, 'Royal Enfield Bullet 350': 176, 'Royal Enfield Bullet 350 [2007-2011]': 177, 'Royal Enfield Bullet 500': 178, 'Royal Enfield Classic 350': 179, 'Royal Enfield Classic 500': 180, 'Royal Enfield Classic Chrome': 181, 'Royal Enfield Classic Desert Storm': 182, 'Royal Enfield Classic Gunmetal Grey': 183, 'Royal Enfield Classic Signals': 184, 'Royal Enfield Classic Squadron Blue': 185, 'Royal Enfield Classic Stealth Black': 186, 'Royal Enfield Continental GT 650': 187, 'Royal Enfield Continental GT [2013 - 2018]': 188, 'Royal Enfield Electra 4 S': 189, 'Royal Enfield Electra 5 S': 190, 'Royal Enfield Electra Twinspark': 191, 'Royal Enfield Himalayan': 192, 'Royal Enfield Interceptor 650': 193, 'Royal Enfield Machismo': 194, 'Royal Enfield Thunder 350': 195, 'Royal Enfield Thunder 500': 196, 'Royal Enfield Thunderbird 350': 197, 'Royal Enfield Thunderbird 350X': 198, 'Royal Enfield Thunderbird 500': 199, 'Royal Enfield Thunderbird 500X': 200, 'Suzuki Access 125': 201, 'Suzuki Access 125 [2007-2016]': 202, 'Suzuki GS150R': 203, 'Suzuki GSX S750': 204, 'Suzuki Gixxer SF': 205, 'Suzuki Gixxer SF Fi': 206, 'Suzuki Gixxer [2014-2018]': 207, 'Suzuki Intruder 150': 208, 'Suzuki Intruder 150 Fi': 209, "Suzuki Let''s": 210, 'Suzuki SlingShot': 211, 'Suzuki Swish [2012-2015]': 212, 'TVS Apache RR310': 213, 'TVS Apache RTR 160': 214, 'TVS Apache RTR 160 4V': 215, 'TVS Apache RTR 180': 216, 'TVS Apache RTR 200 4V': 217, 'TVS Apache [2006]': 218, 'TVS Centra': 219, 'TVS Excel': 220, 'TVS Flame': 221, 'TVS Jupiter': 222, 'TVS Jupyter': 223, 'TVS Max DLX': 224, 'TVS Radeon': 225, 'TVS Scooty Pep DLX': 226, 'TVS Scooty Pep Plus': 227, 'TVS Scooty Streak': 228, 'TVS Scooty Zest 110': 229, 'TVS Spectra': 230, 'TVS Sport': 231, 'TVS Sport ': 232, 'TVS Star City': 233, 'TVS Star City Plus': 234, 'TVS Streak': 235, 'TVS Victor': 236, 'TVS Victor GLX': 237, 'TVS Wego': 238, 'TVS XL 100': 239, 'TVS XL 100 Heavy Duty': 240, 'UM Renegade Commando': 241, 'UM Renegade Mojave': 242, 'Vespa LX 125': 243, 'Vespa SXL 149': 244, 'Vespa VX 125': 245, 'Yamaha Alpha': 246, 'Yamaha Cygnus Ray ZR': 247, 'Yamaha FZ  v 2.0': 248, 'Yamaha FZ 16': 249, 'Yamaha FZ S ': 250, 'Yamaha FZ S V 2.0': 251, 'Yamaha FZ S [2012-2016]': 252, 'Yamaha FZ V 2.0': 253, 'Yamaha FZ16': 254, 'Yamaha FZ25': 255, 'Yamaha Fascino 110': 256, 'Yamaha Fazer ': 257, 'Yamaha Fazer 25': 258, 'Yamaha Fazer Dlx': 259, 'Yamaha Fazer FI V 2.0 [2016-2018]': 260, 'Yamaha Fazer [2009-2016]': 261, 'Yamaha Gladiator': 262, 'Yamaha RX135': 263, 'Yamaha RXG': 264, 'Yamaha Ray Z': 265, 'Yamaha Rx': 266, 'Yamaha SZ RR V 2.0': 267, 'Yamaha SZ X': 268, 'Yamaha SZ [2013-2014]': 269, 'Yamaha SZ-S': 270, 'Yamaha Saluto': 271, 'Yamaha Saluto RX': 272, 'Yamaha YBR 125': 273, 'Yamaha YZF R15 S': 274, 'Yamaha YZF R15 V3': 275, 'Yamaha YZF R15 [2011-2018]': 276, 'Yamaha YZF R3': 277, 'Yo Style': 278}
seller_type_dict = {'Individual' : 0, 'Dealer' : 1}
owner_dict= {'1st owner': 0 ,'2nd owner' : 1 , '3rd owner' : 2, '4th owner':3}

# Input Features
Brand = st.selectbox("Brand", list(brand_dict.keys()))

Model = st.selectbox("Model", list(model_dict.keys()))

Owner = st.selectbox("Owner Type", ['1st owner', '2nd owner', '3rd owner', '4th owner'])

seller_type = st.selectbox("Seller Type", ["Individual", "Dealer"])

manufacture_year = st.slider("Manufacture Year", 2005, 2025, 2018)
Bike_Age = 2025 - manufacture_year  # Convert year → age for model

KM_Driven = st.number_input("Kilometers Driven", 0, 200000, 30000)

Ex_Showroom_Price = st.number_input("Ex-Showroom Price (₹)", 1000, 500000, 60000)


Bike_Age=np.log1p(Bike_Age)
Ex_Showroom_Price=np.log1p(Ex_Showroom_Price)
KM_Driven=np.log1p(KM_Driven)
KM_Driven = np.log1p(KM_Driven)





# Encoding
brand_val = brand_dict[Brand]
model_val = model_dict[Model]
seller_type_val = seller_type_dict[seller_type]
owner_val = owner_dict[Owner]

# Prediction button
if st.button("Predict Price"):
    input_data = np.array([[brand_val,model_val,seller_type_val,owner_val, KM_Driven, Ex_Showroom_Price,Bike_Age ]])
    prediction = model.predict(input_data)[0]
    
    st.success(f"Predicted Bike Price: ₹ {round(prediction, 2)}")
    st.balloons()
