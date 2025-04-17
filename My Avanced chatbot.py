import colorama
import pydot
from colorama import Fore, Back, Style 
def print_mobile_details():
  print(Fore.WHITE + "\nChoose a Which you want to get mobile:")
  print(Fore.BLACK + "\n1. iQOO ")
  print(Fore.GREEN + "\n2. HMD Skyline")
  print(Fore.BLUE + "\n3. Google Pixel")
  print(Fore.GREEN + "\n4. OnePlus")
  print(Fore.BLUE + "\n5. Vivo")
  print(Fore.GREEN + "\n6. Redmi")
  print(Fore.BLUE + "\n7. Samsung:")
  print(Fore.BLACK + "\n8. Apple iPhone")
  print(Fore.RED + "\n9. Realme")
  print(Fore.BLUE + "\n10. Oppo Reno")
  print(Fore.RED + "\n11. Exit:")

def mobile_chatbot():
  print(Style.BRIGHT + Fore.BLUE + "Welcome to Mobile chatBot")
  name = input("\nEnter Your Name: ")

  while True:
    user_input_address = input("\n Enter Your Address: ") 
    if not user_input_address: 
      print("Enter the Valid Address.")
    else:
      address = user_input_address  
      break

  Email = input("Enter your Email: ")
  Mobile = input("\nEnter which mobile phone you want to Buy: ")

  print(Style.BRIGHT + Fore.RED + f"\nHello {name}")

  while True:
    print_mobile_details()

    user_input = input("Enter the Mobile Number choice: ")


    if user_input == "1":
      print(Fore.BLACK + "\n. iQOO.")
      print(Fore.GREEN + "\nMobile Brand Available in: 1.iQOO_13  \n2.iQOO_12 \n3. iQOO_Z9S \n4. iQOO_Neo9 Pro. \n5. iQOO_Z9 Lite.")
      user_input = input("Enter the choice the Mobile Brand: ")
      print(Fore.BLUE + "\nMobile Price: 1.₹51,999, \n2. ₹49,999, \n3. ₹26,999, \n4. ₹24,999, \n5. ₹21,999.")
      print(Fore.GREEN + "\nFacilities: 1. Extended Warranty \n2. Screen Protection \n3. Device Insurance \n4. Premium Support \n5. IQOO Care+ \n6. Accidental Damage Protection.")
      print(Fore.BLACK + "\nStorage: 1. 256GB \n2. 256GB \n3. 512GB \n4. 128GB \n5. 128GB.")
      print(Fore.RED + "\nRam: 1. 12GB \n2. 8GB \n3. 16GB \n4. 4GB \n5. 8GB.")
      print(Fore.BLUE + "\nQuantity: 1. Single Unit \n2. Bulk Order \n3.Bulk Order(5, 10, 20) \n4. Single Unit \n5. Bulk Order.")
      print(Fore.BLACK + "\nProcessor: AI Engine, Neural Engine \n2. Spectra ISP \n3. Quad-Core Processor.")
      print(Fore.BLUE + "\nEMI Details: EMI From ₹2,230 No Cost EMI available: 1 1.Amazon Pay ICICI Credit Card \n2. American Express Credit Card \n3. Axis bank Credit Card \n4. HDFC Bank        Credit Card \n5. ICICI Bank Credit Bank.")
      user_input = input("Enter the choice for Bank: ")
      print(f"{Fore.BLUE}\nYour bank has been successfully Added")
    
    elif user_input == "2":
      print(Fore.GREEN + "\n. HMD Skyline:")
      print(Fore.BLACK + "\nMobile Brand Available in:  1.HMD Skyline \n2. HMD Fusion \n3. HMD Crest Max \n4. HMD 110 Keypad.")
      user_input = input("Enter the choice the Mobile Brand: ")
      print(Fore.BLUE + "\nMobile Feature : 1. Connectivity \n2. Battery \n3. Software-Android 13 \n4. Security \n5. FM Radio.")
      print(Fore.GREEN + "\nMobile Price: 1 ₹40,000 \n2. ₹17,999 \n3. ₹14,999 \n4. ₹1,499.")
      print(Fore.BLUE + "\nQuantity: 1. Bulk Order(5, 10, 20) \n2. Single Unit. |\n3. bilk Order.")
      print(Fore.BLACK + "\nProcessor: 1. Quad-core processor with clock Speed of 1.4GHz.")
      print(Fore.BLUE + "\nFacilities: 1. After- sales service \n2. Repair Services \n3. Accessories. \n3.Guarantee: 1-year.")
      print(Fore.GREEN + "\nStorage: 1. 256GB \n2.128GB. \n3. 64GB \n4. 32GB. ")
      print(Fore.BLACK + "\nRam: 1.12GB \n2. 6GB \n3. 4GB \n4. 32MB.")
      print(Fore.RED + "\nCamera: Dual-camera setup with 13MP Primary Sensor.")
      print(Fore.BLUE + "\nEMI Details: EMI From ₹2,230 No Cost EMI available: 1 1.Amazon Pay ICICI Credit Card \n2. American Express Credit Card \n3. Axis bank Credit Card \n4. HDFC Bank Credit Card \n5. ICICI Bank Credit Bank.")
      user_input = input("Enter the choice for Bank: ")
      print(f"{Fore.BLUE}\nYour bank has been successfully Added.")

    elif user_input == "3":
      print(Fore.BLUE + "\n. Google Pixel:")
      print(Fore.BLACK + "\n.Mobile Brand Available: 1 Google Pixel9 Pro \n2. Sorry,We Currently have Google Pixel9 Pro model 1 of this mobile.")
      print(Fore.RED + "\nMobile Feature : 1. Display-6.7-inch OLED Display, HDR10+ support \n2.Performance-Google Tensor G2 chip, 12GB RAM \n3 Software- Android 13, Google Assistant \n4. Battery- 5124mAh battery.")
      print(Fore.RED + "\nMobile Price: 1 ₹39,000")
      print(Fore.RED + "\nWarranty: 1.1-year limited warranty \n2. Extended warranty.")
      print(Fore.GREEN + "\nStorage: 128GB.")
      print(Fore.RED + "\nRam: 12GB RAM.")
      print(Fore.BLUE + "\nOperating_system: Android 11.")
      print(Fore.GREEN + "\nSensors: 1.Fingerprint sensor \n2. Face unlock sensor \n3. Proximity sensor \n4. Accelerometer.")

    elif user_input == "4":
      print(Fore.BLUE + "\n. OnePlus:")
      print(Fore.BLACK + "\nMobile Brand Available: 1.OnePlue_12R \n2. OnePlus Nord 4 5G \n3. OnePlus Nord CE4 Lite 5G.")
      user_input = input("Enter the choice the Mobile Brand: ")
      print(Fore.BLACK + "\nMobile Feature : 1. Improved Display \n2. Enhanced Camera \n3. Faster Charging \n4. Longer Battery Life.")
      print(Fore.GREEN + "\nMobile Price: 12GB RAM + 256GB storage: ₹31,999 \n2. 8GB RAM + 128GB storage: ₹29,100. \n3.8GB RAM + 128GB storage:17,999.")
      print(Fore.BLUE + "\nSnapdragon: 8Genration 2 SoC.")
      print(Fore.RED + "\nSoftware: OnePlus 12R runs Android 14-based ColorOS 14.0 out-of-the-box.")
      print(Fore.BLUE + "\nRating: IP64 Rating.")
      print(Fore.BLUE + "\nProcessor Available: Octa-core CPU.")
      print(Fore.GREEN + "\nFacilities: 1. After- sales service \n2. Repair Services \n3. Accessories.")
      print(Fore.BLUE + "\nMobile EMI Details: 1. EMI from ₹ 7,025. NO cost EMI avilable EMI Option: 1. Kotak Mahindra Bank Credit Card \n2. SBI Credit Card \n3. HDFC Bank Credit Card \n4. Federal bank Credit Card.")
      user_input = input("Enter the choice for Bank: ")

    elif user_input == "5":
      print(Fore.BLUE + "\n. Vivo")
      print(Fore.RED + "\nMobile Brand: 1. Vivo_x200 \n2. Vivo_x200 Pro \n3. Vivo_x200 Pro Mini \n4. Vivo Y3oo5G \n5. Vivo X Fold3 Pro 5g \n6.Vivo V40e 5G AI Smartphone \n7. Vivo T3x 5G.")
      user_input = input("Enter the choice the Mobile Brand: ")
      print("\nMobile Feature : 1.Display and Design \n2.Camera Capabilities.")
      print("\nMobile EMI Details: 1. EMI from ₹ 2,230. No cost EMI avilable EMI options: 1.Amazon Pay ICICI Credit Card \n2. American Express Credit Card \n3. Axis bank Credit Card \n4. HDFC Bank Credit Card \n5. ICICI Bank Credit Bank.")
      user_input = input("Enter the choice for Bank: ")
      print("\nMobile Price: 1. ₹29,999 \n2.₹33,999 \n3. ₹21,000 \n4. ₹21,799 \n5. ₹68,999 \n6. ₹28,180. \n7. ₹13,939.") 
      print("\nFacilities: 1. Fast Charging_90W \n2. water and Dust Resistance: IP68 and IP69 Rating \n3. Camera: Triple rear camera setup.")
      print("\nStorage: 1.256GB \n2. 512GB \n3. 256GB Storage \n4. 128GB \n5. 512GB \n6. 68GB \n7. 12GB.")
      print("\nRAM: 1.12GB \n2. 16GB \n3. 12GB \n4. 8GB \n5. 16GB \n6. 6GB \n7. 4GB.")
      print("\nSnapdragon: 8Genration 2 processor for Every Mobile.")
      print("\nSensor Feature: 1. In-Display Fingerprint Sensor \n2. Face Recognition \n3. Proximity Sensor.")

    elif user_input == "6":
      print(Fore.RED + "\n Redmi:")
      print(Fore.BLUE + "\nMobile Brand: 1. Redmi_A4 \n2. Redmi 13C 5G \n3. Redmi Note 135G \n4. Redmi A3X \n5. Redmi New 3.")
      user_input = input("Enter the choice the Mobile Brand: ")
      print("\nMobile Feature: 1.Large Display \n2. Powerful Processor \n3. High-Capacity Battery \n4. Dual Camera Setup \n5. Face Unlock \n6. Dual SIM Support \n7. Affordable Price.")
      print("\nMobile Price: 1. ₹12,999 \n2. ₹9,099 \n3. ₹15,891 \n4. ₹7,424 \n5. ₹6,999.")
      print("\nMobile Storage: 1. 64GB \n2. 128GB \n3. 256GB \n4. 64GB \n5. 32GB.")
      print("\nMobile Ram: 1. 4GB \n2. 4GB \n3. 8GB \n4. 3GB \n5. 2GB.")
      print("\nGPS and GLONASS: Supports microSD cards up to 512GB.")
      print("\nFacilities: 1. Wi-Fi and Bluetooth \n2. 1 Witch free Gift  for every mobile.")
      print("\nSnapdragon: 1.4th Generation \n2. 8th Generation \n3. 8th Generation \n4. 4th Generation \n5. 8th Generation.")
      print("\nSoftware Update: Available in Software Update for every Monile.")
      print("\nMobile EMI Details: 1. EMI from ₹ 7,025. NO cost EMI avilable EMI Option: 1. Kotak Mahindra Bank Credit Card \n2. SBI Credit Card \n3. HDFC Bank Credit Card \n4. Federal bank Credit Card.")
      user_input = input("Enter the choice for Bank: ")
      print("\nNotification LED: The Phone has a notification LED, Which provis the usual alerts notification.")

    elif user_input == "7":
      print(Fore.GREEN + "\n Samsung:")
      print(Fore.RED + "\nMobile Brand: 1.Samsung Galaxy M15 5G \n2. Samsung Galaxy M14 4GB \n3. Samsung Galaxy F05 \n4. Samsung Galaxy S23 FE 5G \n5. Samsung Galaxy M55s 5G. \n6. Samsung Galaxy A35 5G.")
      user_input = input("Enter the choice the Mobile Brand: ")
      print("\nEMI Details: 1. EMI from ₹ 2,230. No cost EMI avilable EMI options: 1.Amazon Pay ICICI Credit Card \n2. American Express Credit Card \n3. Axis bank Credit Card \n4. HDFC Bank Credit Card \n5. ICICI Bank Credit Bank.")
      user_input = input("Enter the choice for Bank: ")
      print("\nMobile Price: 1. ₹11,999 \n2. ₹8,325 \n3. ₹7,388 \n4. ₹31,999 \n5. ₹20,999 \n6. ₹29,999.")
      print("\nOther Details: 1. FREE delivery, Payment: Secure Transaction, 1 Year Warranty, 7 Days Service Centre Replacemnt, Top Brand.")
      print("\nStorage: 1.128GB. \n2.64GB \n3. 64GB \n4. 128GB \n5. 128GB \n6. 128GB.")
      print("\nRam: 1. 6GB \n2. 4GB \n3. 4GB \n4. 8GB \n5. 8GB \n6. 8GB.")
      print("\nQuantity:1. Bulk Order(5, 10, 20) \n2. Single unit  \n3. Single unit  \n4. Bulk Order(5, 10, 20) \n5. Single unit \n6. Bulk Order.")
      print("\nProduct_details Top Highlights: 1. CPU model: A-Series \n2. CPU Speed: 2GHz \n3. Operating System: Android 14.")
      print("\nMobile About the Brand: 1. 89% positive rating from 100K+ Customers \n2. 100k+ recent orders from this brand \n3. 11+ years on Amazon.")

    elif user_input == "8":
      print(Fore.GREEN + "\n Apple iPhone:")
      print(Fore.BLUE + "\nMobile Brand: 1. Apple iPhone15 Pro \n2. iPhone 16 Pro \n3. Apple iPhone 13 \n4. Apple iPhone 15 Plus \n5. Apple iPhone 14.")
      user_input = input("Enter the choice the Mobile Brand: ")
      print("\nMobile EMI Details: 1. EMI from ₹ 7,025. NO cost EMI avilable EMI Option: 1. Kotak Mahindra Bank Credit Card \n2. SBI Credit Card \n3. HDFC Bank Credit Card \n4. Federal bank Credit Card.")
      user_input = input("Enter the choice for Bank: ")
      print("\nMobile Price: 1. ₹59,999 \n2. ₹49,999 \n3. ₹39,000 \n4. ₹40,000 \n5. ₹43,999.")
      print("\nMobile Quantity: 1. single Unit \n2. Bulk Order \n3. Bulk order \n4. Bulk Order \n5. Single unit.")
      print("\nMobile Details: 1. Brand: Apple, Operating System: iOS, Memory Storage Capacity: 100GB, Screen Size: 6.1 inches.")
      print("RAM: 1.12GB \n2. 6GB \n3. 12GB \n4. 16GB \n5. 12GB.")
      print("Storage: 1. 256GB \n2. 128GB \n3. 128GB \n4. 128GB \n5. 128GB.")
      print("\nWarranty Policy: Apple One (1) Year Limited Warranty.")

    elif user_input == "9":
      print(Fore.GREEN + "\n Realme:")
      print(Fore.RED + "\n 1. Realme GT7 Pro \n2. realme NARZO 70 Turbo 5G \n3. realme 12x 5G \n4. realme P1 Pro 5G \n5. realme C67 5G \n6. realme 13 Pro 5G.")
      user_input = input("Enter the choice the Mobile Brand: ")
      print("\nMobile EMI Details: 1. EMI from ₹ 2,909. No cost EMI avilable EMI Option: 1. Bajaj Finserv EMI Card \n2. Amazon Pay ICICI Credit Card \n3. Axis Bank Credit Card \n4. ICICI Bank Credit card.")
      user_input = input("Enter the choice for Bank: ")
      print("\nMobile Price: 1. ₹24,999 \n2. ₹16,998 \n3. ₹13,158 \n4. ₹17,705 \n5. ₹11,999 \n6. ₹23,330.")
      print("\nShop Highlight: 1. 7 days Centre Replacement \n2. 1 Year Warranty \n3. Top Brand \n4. Free Delivery.")
      print("\nMobile RAM: 1. 12GB \n2. 6GB \n3. 8GB \n4. 8GB \n5. 6GB \n6. 8GB.")
      print("\nmobile Storage: 1. 256 \n2. 128GB \n3. 128GB \n4. 128GB \n5. 128GB \n6. 128GB.")
      print("\nSnapdragon: India's First Snapdragon 8 Elite Processor.")
      print("\nProduct Details: 1. Brand: realme, Operating System: Android 15, Model Name: realme GT 7 Pro, network Serivice Provider: Unlocked for All Carriers.")
      print("\nColour: Mar Orange, Galaxy Gray.")

    elif user_input == "10":
      print(Fore.RED + "\n Oppo Reno12 Pro:")
      print(Fore.BLUE + "\nMobile Brand: 1. Oppo Reno12 Pro \n2. OPPO F27 5G \n3. OPPO A3 Pro 5G \n4. OPPO A3 5G \n5. OPPO F27 Pro+ 5G.")
      user_input = input("Enter the choice the Mobile Brand: ")
      print("\nMobile EMI Details: 1. EMI from ₹ 2,909. No cost EMI avilable EMI Option: 1. Bajaj Finserv EMI Card \n2. Amazon Pay ICICI Credit Card \n3. Axis Bank Credit Card \n4. ICICI Bank Credit card.")
      user_input = input("Enter the choice for Bank: ")
      print("\nMobile Feature: Power Processor: Qualcomm Snapdragon 8Gen 2 Chipset \n2. Advanced camera System \n3. fast Charging \n4. 5G Connectivity.")
      print("\nMobile Price: 1.₹22,500 \n2. ₹19,812 \n3. ₹17,999 \n4. ₹15,999 \n5. ₹21,000.")
      print("\nMobile RAM: 1.12GB \n2. 8GB \n3. 8GB \n4. 6GB \n5. 8GB.")
      print("\nMobile Storage: 256GB \n2. 256GB \n3. 128GB \n4. 128GB \n5. 128GB.")
      print("\nMobile Offers: 70%, 60%.")
      print("\nOther Details: 1. Brand: Oppo, CPU Model: Snapdragon, CPU Speed: 3.4 GHz, 500mAh Battery.")
      print("\nAbout the Brand: 1. 90% Positive rating from 100k+ customers \n2. 50k+ recent orders from this brand \n3. 10+ years on Amzon.")

    elif user_input == "11":
      print("Thank you for using mobile chatbot.")
      break

    else:
        print(Fore.BLACK + Fore.GREEN + "Please choose a number between 1 and 11.")

    further_question = input("\nDo you have any other queries? (Yes/No): ").strip().lower()
    
    if further_question == "no":
            print(Style.BRIGHT + Fore.GREEN + "\nThank you for Using Mobile chatbot.")

    elif further_question != "Yes":
         print(Back.MAGENTA + Fore.BLACK + "Please Enter 'Yes' Or 'No'.")
    break

if __name__=="__main__":
    mobile_chatbot()

