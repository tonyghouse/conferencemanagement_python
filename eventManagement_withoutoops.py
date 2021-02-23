""" CONFERENCE/EVENT MANAGEMENT APPPLICATON
     using python without OOPS and json,pandas,numpy library module
"""
#importing modules
import json
import pandas as pd
import numpy as np

path = 'C:\\Users\\userpcname\\Desktop\\database\\'

sessiondart = 0
sessionlogin=""
sessionpassword=""

""" definations of various functions """
event_list_dict={                                                   #list of all events in the conference
    1: "Robotics",
    2: "Aero Modelling",
    3: "Computer Vision",
    4: "IoT",
    5: "Image Processing",
    6: "Surveillance Robot",
    7: "Arduino",
    8: "AC Circuits",
    9: "DC Circuits",
    10: "Filters",
    11: "Power Electronics",
    12: "Oscillators",
    13: "Transformers",
    14: "Operational Amplifiers",
    15: "Advanced Wireless Communications",
    16: "Channel Tracking of Multi-Antenna System",
    17: "Fingerprint Identification and its Advanced Applications",
    18: "Autonomous Cars",
    19: "Radio Frequency Identification",
    20: "Cellular and Mobile Communication",
    21: "5G Wireless Technology",
    22: "Smart Antenna",
    23: "Augmented Reality"

}
event_price_dict={                                           #price for each event given by event number
    1: 100, 2: 150, 3: 100, 4: 200, 5: 250, 6: 300, 7: 100, 8: 300, 9: 225, 10: 175, 11: 150, 12: 175, 13: 200,
              14: 100, 15: 500, 16: 500, 17: 450, 18: 700, 19: 500, 20: 450, 21: 600, 22: 500, 23: 750
}
def display_events():
    for deitr in event_list_dict:
        if (deitr%8==0):
            print("\n")
        print(str(deitr)+":"+event_list_dict[deitr], end=" ")

def choosen_events_display(cedarg):
    global sessiondart
    cedstring=sheet.cell(row=cedarg,column=12).value
    cedlist=[int(itr) for itr in cedstring.split() if itr.isdigit()]
    print("Displaying Choosen Events by User:")
    for ceditr in cedlist:
        print("#"+str(ceditr)+":"+event_list_dict[ceditr]+"  |"+"Fee-"+str(event_price_dict[ceditr])+"|")
    return cedlist

def amountcalculator(amdartarg):
    totalamount=0
    choosen_events_list = choosen_events_display(amdartarg)
    for celitr in choosen_events_list:
        totalamount += int(event_price_dict[celitr])
    sheet.cell(row=amdartarg, column=13).value = totalamount
    wb.save(path + 'candidatedata.xlsx')
    return totalamount

def dartcatch(dcarg):
    global sessiondart
    sessiondart = dcarg
def authenticate():
    lidauth = input("Enter your login ID:")
    dartauth = 1
    global sessionlogin
    while (dartauth <= (sheet.max_row)):
        if (lidauth == (sheet.cell(row=dartauth, column=2).value)):
            break
        dartauth += 1
    if (dartauth > (sheet.max_row)):
        print("<<<NO Login ID Found! Try Again>>>")
        authenticate()

    if (dartauth < (sheet.max_row + 1)):
        sessionlogin=lidauth
        return dartcatch(dartauth)  # catch the variable into another variable

def passwordverify(pwdarg):
    password_arg=pwdarg
    global sessiondart
    global sessionlogin
    global sessionpassword
    if(password_arg==(sheet.cell(row=sessiondart,column=3).value)):
        sessionpassword=password_arg
        print("<<<Password MATCHED! Login successful! >>>")
        return "Verified!"
    else:
        print("<<<Password Doesn't MATCH try Again>>>")
        login_edit_register()



def main_page():
    print("-----EVENT\tMANAGEMENT\tAPPLICATION-----")
    print("Select the MAIN PAGE Option:\n 1.Advertisement Page \n 2.Candidate Registration & Login Page \n 3.Issue Entry Pass Page \n 4.Abort&Exit\n")
    mainpage_option = int(input("Enter Main Page Option:"))
    def switcher_mainpage_option(mainpage_option_arg):
        useroption_dict = {1:advertise, 2: candidate_reglogin_menu, 3: entrypass, 4: abortexit}
        return useroption_dict[mainpage_option_arg]()

    switcher_mainpage_option(mainpage_option)



def advertise():
    print("---Events Posters---")
    print("||||||||Indraprastha Institute of Information Technology, Delhi||||||||")
    print("TECH FEST CONFERENCE/EVENT")
    print("[EVENTS LIST & FEE DETAILS]")
    print("*Workshops: 1-Robotics (rs.100), 2-Aero Modelling (rs.150), 3-Computer Vision (rs.100), 4-IoT (rs.200), 5-Image Processing (rs.250), 6-Surveillance Robot (rs.300)")
    print("*Tutorials: 7-Arduino (rs.100), 8-AC Circuits (rs.300), 9-DC Circuits (rs.225), 10-Filters (rs.175) , 11-Power Electronics (rs.150),\n\t\t\t12-Oscillators (rs.175), 13-Transformers (rs.200), 14-Operational Amplifiers (rs.100)")
    print("*Paper Presentation: 15-Advanced Wireless Communications (rs.500), 16-Channel Tracking of Multi-Antenna System (rs.500), 17-Fingerprint Identificationand its Advanced Applications (rs.450),\n\t\t\t18-Autonomous Cars (rs.700), 19-Radio Frequency Identification (rs.500), 20-Cellular and Mobile Communication (rs.450)")
    print("*Panel Discussion: 21-5G Wireless Technology (rs.600), 22-Smart Antenna (rs.500), 23-Augmented Reality (rs.750)")
    print("[DISPLAY DETAILS]")
    print("Venue:Indraprastha Institute of IT campus")
    print("Timings:02-oct-2020 9am to 6pm")
    main_page()


def new_register():                             #new reigistration Module
    global sessionlogin
    global sessionpassword
    global sessiondart
    print("[NEW REGISTRATION PAGE]")
                                                #cusrsor pointer (dart) to point to the next field in the MS-excel file
    dart = (sheet.max_row)+1
    sheet.cell(row=dart, column=1).value =dart
    loginid="2k20conf"+str(dart)
    sheet.cell(row=dart,column=2).value=loginid
    print("___LOGIN-ID:"+loginid)                #loginid is generated unique to every candidate
    print("Enter Your Details.....")
    password=input("Create your Password:")
    sheet.cell(row=dart,column=3).value=password
    name = input("Name:")
    sheet.cell(row=dart,column=4).value=name
    rollnum = input("Roll Number:")
    sheet.cell(row=dart,column=5).value=rollnum
    gender = input("Gender:")
    sheet.cell(row=dart,column=6).value=gender
    dob=input("Date of Birth:")
    sheet.cell(row=dart,column=7).value=dob
    clgname_profession = input("College Name or Profession:")
    sheet.cell(row=dart,column=8).value=clgname_profession
    qualification=input("Qualification:")
    sheet.cell(row=dart,column=9).value=qualification
    phone = input("Phone:")
    sheet.cell(row=dart,column=10).value=phone
    email = input("Email:")
    sheet.cell(row=dart,column=11).value=email
    print("\n(Enter Event Numbers seperated with space)")
    display_events()
    choosen_eventlist = input("\nChoose Events::: ")
    sheet.cell(row=dart,column=12).value=choosen_eventlist
    wb.save(path + 'candidatedata.xlsx')
    sessionlogin=loginid
    sessionpassword=password
    sessiondart=dart
    print("New Registration Successful !")
    candidate_reglogin_menu()

def event_change():
    global sessiondart
    print(sessiondart)
    display_events()
    updated_events=input("\nEnter Your Changed Events list::: ")
    sheet.cell(row=sessiondart, column=12).value=updated_events
    print("Your Choosen Events list is updated!")
    wb.save(path + 'candidatedata.xlsx')
    candidate_reglogin_menu()

def clear_start():
    global sessiondart
    cleardart=4
    while(cleardart<=sheet.max_column):
        sheet.cell(row=sessiondart, column=cleardart).value="CLEARED"
        cleardart +=1
    wb.save(path + 'candidatedata.xlsx')
    print("Data is cleared....! & Start Again")
    candidate_reglogin_menu()


def withdraw_events():
    global sessiondart
    sheet.cell(row=sessiondart, column=12).value = "WITHDRAWN"
    wb.save(path + 'candidatedata.xlsx')
    print("withdrawn from events.....!")
    candidate_reglogin_menu()

def login_edit_register():                            # login and edit registration module
    print("[LOGIN & EDIT REGISTER PAGE]")
    authenticate()
    print("LoginID is : "+sessionlogin)
    user_password=input("Enter Your Password:")
    dartloginedit = passwordverify(user_password)
    print(dartloginedit)
    print("EDIT Option MENU: 1.Event Change Option, 2.Clear & Start Again, 3.Withdraw From Event , 0.Back to Main page")
    edit_option = int(input("Enter Option to edit:"))
    def switcher_editoption(edit_option_arg):
        editoption_dict = {1: event_change, 2: clear_start, 3: withdraw_events, 0:main_page}
        return editoption_dict[edit_option_arg]()

    switcher_editoption(edit_option)



def fee_calculation():
    global sessionlogin
    global sessiondart
    global sessionpassword
    totalamount=0
    authenticate()
    print("LoginID is : " + sessionlogin)
    user_pwd_fee = input("Enter Your Password:")
    dartloginedit = passwordverify(user_pwd_fee)
    print(dartloginedit)
    totalfee=amountcalculator(sessiondart)
    print("TOTAL AMOUNT:"+str(totalfee))
def upi(upiarg):
    print("(UPI PAYMENT PAGE)")
    upiusername=input("Enter UPI Username:")
    upipassword=input("Enter UPI Password:")
    print("Invoice: Amount-"+str(upiarg)+" Paid by "+upiusername)
    return "UPI"+" "+upiusername+" "+upipassword
def netbanking(nbarg):
    print("(NET BANKING PAGE)")
    nbusername = input("Enter Netbanking Username:")
    nbpassword = input("Enter Netbaking Password:")
    print("Invoice: Amount-"+str(nbarg) + " Paid by " + nbusername)
    return "NETBANKING"+" "+nbusername+" "+nbpassword

def creditcard(ccarg):
    print("(CREDIT CARD PAY PAGE)")
    ccnum = input("Enter Credit Card Number:")
    ccusername=input("Enter Credit Card username:")
    ccbankname = input("Enter Bank Name:")
    cccvv=input("Enter cvv:")
    ccdate = input("Enter Expiry Date:")
    print("Invoice: Amount-"+str(ccarg) + " Paid by " + ccusername)
    return "CREDITCARD"+" "+ccnum+" "+ccusername+" "+ccbankname+" "+cccvv+" "+ccdate

def debitcard(dcarg):
    print("(DEBIT CARD PAY PAGE)")
    dcnum = input("Enter Debit Card Number:")
    dcusername = input("Enter Debit Card username:")
    dcbankname = input("Enter Bank Name:")
    dccvv = input("Enter cvv:")
    dcdate = input("Enter Expiry Date:")
    dcotp=input("Enter OTP:")
    print("Invoice: Amount-"+str(dcarg) + " Paid by " + dcusername)
    return "DEBITCARD"+" "+dcnum+" "+dcusername+" "+dcbankname+" "+dccvv+" "+dcdate+" "+dcotp
def cash(casharg):
    print("(CASH PAY PAGE)")
    cashname=input("Enter your Legal name and Pay cash:")
    print("Invoice: Amount-"+str(casharg) + " Paid by " + cashname)
    return "CASH"
def payment():
    global sessionlogin
    global sessiondart
    global sessionpassword
    authenticate()
    print("LoginID is : " + sessionlogin)
    user_pwd_pay = input("Enter Your Password:")
    dartloginpay = passwordverify(user_pwd_pay)
    print(dartloginpay)
    amountcalculator(sessiondart)
    totalpay=(sheet.cell(row=sessiondart, column=13).value)
    print("Amount to be PAID:::"+str(totalpay))
    print("PAYMENT OPTIONS: 1.UPI, 2.Net banking, 3.Credit Card, 4.Debit card 5.Cash 0.Back to Candidate Reg//loginpage")
    pay_way=int(input("Choose a Payment method:"))
    def switcher_payoption(pay_way_arg):
        payoption_dict = {1: upi, 2: netbanking, 3: creditcard, 4: debitcard, 5: cash, 0:candidate_reglogin_menu}
        return payoption_dict[pay_way_arg](totalpay)

    pay_string=switcher_payoption(pay_way)
    if(pay_string!=""):
        sheet.cell(row=sessiondart, column=14).value = sheet.cell(row=sessiondart, column=12).value
        sheet.cell(row=sessiondart, column=15).value = pay_string
        sheet.cell(row=sessiondart, column=16).value = totalpay
    else:
        print("Payment system has a problem! Try again!")
        candidate_reglogin_menu()

    wb.save(path + 'candidatedata.xlsx')
    print("Payment Completed......!")
    main_page()


def refund():
    global sessionlogin
    global sessiondart
    global sessionpassword
    authenticate()
    print("LoginID is : " + sessionlogin)
    user_pwd_refund = input("Enter Your Password:")
    dartrefund = passwordverify(user_pwd_refund)
    print(dartrefund)
    if(str(sheet.cell(row=sessiondart, column=13).value)==str(sheet.cell(row=sessiondart, column=16).value)):
        print("Refund of Amount:: "+str((sheet.cell(row=sessiondart, column=16).value))+" By"+sessionlogin)
        print("Request will be handled by Admin and refund will be provided!")
        sheet.cell(row=sessiondart, column=17).value="REFUNDED"
        sheet.cell(row=sessiondart, column=16).value = "CANCELLED"

    else:
        print("Total amount/fees is NOT payed!")
        candidate_reglogin_menu()

    wb.save(path + 'candidatedata.xlsx')
    print("refund intitiated......!")


def candidate_reglogin_menu(): # candidate conference/event registration & login module
    print("Select the Option:\n 1.New_Registration \n 2.Login & Edit_Registration \n 3.Fee Calculation \n 4.Payment \n 5.Refund \n 0.Back to Main page")
    user_option = int(input("Enter Option:"))

    # to switch user options
    def switcher_useroption(user_option_arg):
        useroption_dict = {1: new_register, 2: login_edit_register, 3: fee_calculation, 4: payment, 5: refund, 0:main_page}
        return useroption_dict[user_option_arg]()

    switcher_useroption(user_option)


###candidate_reglogin_menu()


def entrypass():
    global sessionlogin
    global sessiondart
    global sessionpassword
    authenticate()
    print("LoginID is : " + sessionlogin)
    user_pwd_entrypass = input("Enter Your Password:")
    dartentrypass = passwordverify(user_pwd_entrypass)
    print(dartentrypass)

    print("Entry Pass")
    print("+-----------------------------------------------------------------+")
    print("ID:"+str(sessionlogin))
    print("Name: "+str(sheet.cell(row=sessiondart, column=4).value))
    print("RollNumber: " + str(sheet.cell(row=sessiondart, column=5).value))
    print("College/Profession: " + str(sheet.cell(row=sessiondart, column=8).value))
    print("Qualification: " + str(sheet.cell(row=sessiondart, column=9).value))
    print("Phone: " + str(sheet.cell(row=sessiondart, column=10).value))
    print("Email: " + str(sheet.cell(row=sessiondart, column=11).value))
    print("Amount Paid: " + str(sheet.cell(row=sessiondart, column=16).value))
    print("+-----------------------------------------------------------------+")

    print("\nEntry pass issued!")
    main_page()

def abortexit():
    print("////////////// EXITED //////////////")
    main_page()


# main block of code for event/conference management software
main_page()




