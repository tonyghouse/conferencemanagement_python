""" CONFERENCE/EVENT MANAGEMENT APPPLICATON
     using python with OOPS concepts(SOLID) and json,pandas,numpy library module
"""

import json
import pandas as pd
path = 'C:\\Users\\your\\Desktop\\database\\'

class dbmanager:

    def loadfromdb(self):
        existing_df = pd.read_json(path_or_buf=path + 'userdata.json', orient='index')
        return existing_df
    def savetodb(self,existing_df):
        existing_df.to_json(path_or_buf=path + 'userdata.json', orient='index', indent=5, index=True)

class eventhandler:
    events_dict={}

    def __init__(self):
        with open(path + 'events.json') as json_file:
            self.events_dict= json.load(json_file)

    def eventsdictloader(self):
        return self.events_dict

    def events_display(self):
        for event_num, event_info in self.events_dict.items():
            print("\n#", event_num, end =" ")
            for event_keys, event_values in event_info.items():
                print(event_values, end =" ")

    def choosen_events_display(self,iddarg):
        id=iddarg
        df=dbmanager().loadfromdb()
        print("CHOOSEN EVENTS:" + str(df.loc[id]['choosen_events']))
        choosen_events_list = df.loc[id]['choosen_events'].split()
        for itr in choosen_events_list:
            print("#"+itr+(self.events_dict[itr]["event-name"]))
        return choosen_events_list


class advertise:
    def show_advertise(self):
        print("[ADVERTISEMENT PAGE]")
        eventhandler().events_display()
        mainpage().show_mainpage()


class usermenu:
    def show_usermenu(self):
        print("\n[ USER MENU PAGE ]")
        print("Select the USER MENU PAGE Option:\n 1.New registration Page \n 2.Edit Registration Page \n 3.Fee Calculation \n 4.Payment \n 5.Refund request\n 0.Mainpage")
        usermenu_option = int(input("Enter Usermenu  Page Option:"))
        usermenu_options = {0:mainpage().show_mainpage, 1:newregister().show_newregister, 2: loginedit().show_loginedit, 3: feecalculation().show_feecalculation,
                             4: show_payment().show_payment, 5: refundreq().show_refundreq}
        try:
            usermenu_options[usermenu_option]()
        except Exception:
            print("??? Wrong Option ???\n")
            mainpage().show_mainpage()

class newregister:
    userform=["Name","Roll Number","Gender","Date of Birth","College Name or Profession","Qualification","Phone Number","Email id"]
    userdetails_dict={}
    def show_newregister(self):
        print("[NEW REGISTRATION PAGE]")
        id = input("Create your ID:")
        for i in self.userform:
            self.userdetails_dict[i] = input(i + ":")
        print("\n(Enter Event Numbers seperated with space)")
        self.userdetails_dict["choosen_events"] = input("\nChoose Events::: ")
        print(self.userdetails_dict)
        newdf = pd.DataFrame(self.userdetails_dict, index=[id])
        df =dbmanager().loadfromdb()
        df = df.append(newdf)
        dbmanager().savetodb(df)
        print("New Registration Successful !")
        mainpage().show_mainpage()

class loginedit:
    def show_loginedit(self):
        print("[LOGIN & EDIT REGISTER PAGE]")
        print("LOGIN & EDIT Option MENU: 1.Event Change Option, 2.Clear & Start Again, 3.Withdraw From Event , 0.Back to Main page")
        loginedit_option = int(input("Enter Option to edit:"))

        loginedit_menu_options = {0: mainpage().show_mainpage, 1: eventchange().show_eventchange, 2: clearstart().show_clearstart,
                             3: withdrawevents().show_withdrawevents}
        try:
            loginedit_menu_options[loginedit_option]()
        except Exception:
            print("??? Wrong Option ???\n")
            mainpage().show_mainpage()

class dbdatachanger:
    id=""
    option=""
    newdata=""
    def dbdatachanger(self,idarg,optionarg,newdatarg):
        self.id=idarg
        self.option=optionarg
        self.newdata=newdatarg
        df=dbmanager().loadfromdb()
        df.loc[self.id][self.option] =self.newdata
        dbmanager().savetodb(df)
        mainpage().show_mainpage()

class eventchange:
    id=""
    option='choosen_events'
    newdata=""
    def show_eventchange(self):
        print("[EVENT CHANGE PAGE]")
        self.id = input("Enter your ID (to login):")
        self.newdata= str(input("Enter events to change(with spaces):::"))
        dbdatachanger().dbdatachanger(self.id,self.option,self.newdata)
class clearstart:
    id=""
    option=':'
    newdata=" "
    def show_clearstart(self):
        print("[CLEAR & START PAGE]")
        self.id = input("Enter your ID (to login):")
        dbdatachanger().dbdatachanger(self.id,self.option,self.newdata)


class withdrawevents:
    id=""
    option='choosen_events'
    newdata="WITHDRAWN"
    def show_withdrawevents(self):
        print("[WITHDRAW FREOM EVENTS PAGE]")
        self.id = input("Enter your ID (to login):")
        dbdatachanger().dbdatachanger(self.id,self.option,self.newdata)

class feecalculation:
    id=""
    totalfee=0

    def show_feecalculation(self):
        self.id = input("Enter your ID (to login):")
        df = dbmanager().loadfromdb()
        choosen_events_list = eventhandler().choosen_events_display(self.id)
        events_dict = eventhandler().eventsdictloader()

        for itr in choosen_events_list:
            self.totalfee+=(events_dict[itr]["event-price"])
        print("\nTOTAL FEE NEED TO BE PAID:::"+str(self.totalfee))
        df.loc[self.id]['total_fee'] =self.totalfee
        dbmanager().savetodb(df)
        mainpage().show_mainpage()

class payment:
    id=""
    totalfee=""
    paystring=""
    def payment(self,idarg,totalfeearg,paystringarg):
        self.id = idarg
        self.totalfee = totalfeearg
        self.paystring = paystringarg
        df=dbmanager().loadfromdb()
        if (self.paystring != ""):
            df.loc[self.id]['paid_for'] = df.loc[self.id]['choosen_events']
            df.loc[self.id]['paid_by'] = self.paystring
            df.loc[self.id]['paid_amount'] = self.totalfee
            dbmanager().savetodb(df)
        else:
            print("Payment system has a problem! Try again!")
            usermenu().show_usermenu();

class upipayment(payment):
    pass

class netbankingpayment(payment):
    pass

class creditcardpayment(payment):
    pass

class debitcardpayment(payment):
    pass
class cashpayment(payment):
    pass

class show_payment:
    id=""
    totalfee=""
    payway=0
    paystring=""
    def show_payment(self):
        print("[PAYMENT PAGE]")
        self.id = input("Enter your ID (to login):")
        df = dbmanager().loadfromdb()
        self.totalfee = str(df.loc[self.id]['total_fee'])
        if ((self.totalfee) !='None'):
            print("Amount to be PAID:::" + self.totalfee)
            print("PAYMENT OPTIONS: 1.UPI, 2.Net banking, 3.Credit Card, 4.Debit card 5.Cash 0.Back to Candidate Reg//loginpage")
            self.payway = int(input("Choose a Payment method:"))
            payoption_dict = {1: show_upi().show_upi, 2: show_netbanking().show_netbanking,
                              3: show_creditcard().show_creditcard, 4: show_debitcard().show_debitcard,
                              5: show_cash().show_cash, 0 : mainpage().show_mainpage}
            self.paystring = payoption_dict[self.payway](self.totalfee)
        else:
            print("First Go &  Calculate FEE!")
            usermenu().show_usermenu()
        print(self.paystring)
        paymentoption_dict = {1: upipayment().payment, 2: netbankingpayment().payment,
                          3: creditcardpayment().payment, 4: debitcardpayment().payment,
                          5: cashpayment().payment, 0: mainpage().show_mainpage }
        paymentoption_dict[self.payway](self.id,self.totalfee,self.paystring)

class show_upi:
    def show_upi(self,totalfeearg):
        print("(UPI PAYMENT PAGE)")
        upiusername = input("Enter UPI Username:")
        upipassword = input("Enter UPI Password:")
        print("Invoice: Amount-" + str(totalfeearg) + " Paid by " + upiusername)
        return "UPI" + " " + upiusername + " " + upipassword

class show_netbanking:
    def show_netbanking(self,totalfeearg):
        print("(NET BANKING PAGE)")
        nbusername = input("Enter Netbanking Username:")
        nbpassword = input("Enter Netbaking Password:")
        print("Invoice: Amount-" + str(totalfeearg) + " Paid by " + nbusername)
        return "NETBANKING" + " " + nbusername + " " + nbpassword

class show_creditcard:
    def show_creditcard(self,totalfeearg):
        print("(CREDIT CARD PAY PAGE)")
        ccnum = input("Enter Credit Card Number:")
        ccusername = input("Enter Credit Card username:")
        ccbankname = input("Enter Bank Name:")
        cccvv = input("Enter cvv:")
        ccdate = input("Enter Expiry Date:")
        print("Invoice: Amount-" + str(totalfeearg) + " Paid by " + ccusername)
        return "CREDITCARD" + " " + ccnum + " " + ccusername + " " + ccbankname + " " + cccvv + " " + ccdate

class show_debitcard:
    def show_debitcard(self,totalfeearg):
        print("(DEBIT CARD PAY PAGE)")
        dcnum = input("Enter Debit Card Number:")
        dcusername = input("Enter Debit Card username:")
        dcbankname = input("Enter Bank Name:")
        dccvv = input("Enter cvv:")
        dcdate = input("Enter Expiry Date:")
        dcotp = input("Enter OTP:")
        print("Invoice: Amount-" + str(totalfeearg) + " Paid by " + dcusername)
        return "DEBITCARD" + " " + dcnum + " " + dcusername + " " + dcbankname + " " + dccvv + " " + dcdate + " " + dcotp

class show_cash:
    def show_cash(self,totalfeearg):
        print("(CASH PAY PAGE)")
        cashname = input("Enter your Legal name and Pay cash:")
        print("Invoice: Amount-" + str(totalfeearg) + " Paid by " + cashname)
        return "CASH"

class refundreq:
    id="";
    def show_refundreq(self):
        self.id = input("Enter your ID (to login):")
        df=dbmanager().loadfromdb()
        df.loc[self.id]['refund_req'] = "REFUND REQUESTED"
        dbmanager().savetodb(df)
        print("Refund initaited...........!")
class entrypass:
    uplmt = 0
    downlmt = 12
    def show_entrypass(self):
        id = input("Enter your ID (to login):")
        df=dbmanager().loadfromdb()
        print("||| Entry Pass |||")
        print("+-----------------------------------------------------------------+")
        print("|||YOUR ID:::" + str(id) + "|||")
        print(df.loc[id][self.uplmt:self.downlmt])
        print("+-----------------------------------------------------------------+")
        mainpage().show_mainpage()

class abortexit:
    def show_abortexit(self):
        print("\n////////////// EXITED //////////////\n")
        mainpage().show_mainpage()


class mainpage:

    def show_mainpage(self):
        print("\n\n-----EVENT\tMANAGEMENT\tAPPLICATION-----")
        print("Select the MAIN PAGE Option:\n 1.Advertisement Page \n 2.User menu(Candidate Registration & Login) Page \n 3.Issue Entry Pass Page \n 4.Abort&Exit\n 0.Mainpage")
        mainpage_option = int(input("Enter Main Page Option:"))
        main_menu_options = {0: mainpage().show_mainpage, 1: advertise().show_advertise, 2: usermenu().show_usermenu,
                            3: entrypass().show_entrypass, 4: abortexit().show_abortexit}
        try:
            main_menu_options[mainpage_option]()
        except Exception:
            print("??? Wrong Option ???\n")
            mainpage().show_mainpage()

if __name__ == "__main__":
    mainpage().show_mainpage()





