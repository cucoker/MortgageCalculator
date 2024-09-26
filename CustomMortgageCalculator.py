from loanterms import Loanterms
from monthlyamort import monthlyAmort
from datetime import datetime

#from dateutil.relativedelta import relativedelta
#Adding Comment for source control
#Adding another comment for source control
# Adding Comment from developer 2

class MortageCalculator:
    def __init__(self, loanterms, startdate):
        self.loanterms = loanterms
        self.amortschedule = []
        self.startdate = startdate
        self.mortgagepayment = 0
        
        #amort = monthlyAmort(1,100, 200, 300000)
        #self.amortschedule.append(amort)
        

        self.boil = 0
    
    def calculatemonthlypaymet(self):
        interestrate = self.loanterms.APR/100/12
        months = self.loanterms.Term * 12
        self.mortgagePayment = self.loanterms.saleprice * (interestrate * (1 + interestrate)
                                ** months) / ((1 + interestrate) ** months - 1)
        gint = 0
        return round(self.mortgagePayment,2)

    def calculateamortization(self):     
        
        interest = 0
        principle = 0
        money_owed = self.loanterms.saleprice
        monthlyapr = (self.loanterms.APR/100/12)
        payment = self.calculatemonthlypaymet()
        
        for x in range(self.loanterms.Term*12):
            interest = money_owed * monthlyapr
            money_owed = money_owed + interest
            if (money_owed < payment):
                break
            
            money_owed = money_owed - payment 
            principle = payment - interest   
            amort = monthlyAmort(x, interest, principle,money_owed)
            self.amortschedule.append(amort)

        return self.amortschedule   

def add_months(current_date, months_to_add):
    new_date = datetime(current_date.year + (current_date.month + months_to_add - 1) // 12,
                        (current_date.month + months_to_add - 1) % 12 + 1,
                        current_date.day, current_date.hour, current_date.minute, current_date.second)
    return new_date

def main():
    loanterms = Loanterms(2.7, 30, 400000)
    amortdate1 = datetime(2021,1,1)
    mortgagecalculator = MortageCalculator(loanterms, amortdate1)
    amort = mortgagecalculator.calculateamortization()
    #mortgagepayment = mortgagecalculator.calculatemonthlypaymet()
    #print(mortgagepayment)
    amortdate = mortgagecalculator.startdate
    
    for x in amort:
        print(f'{x.monthint}, {amortdate:%B %Y}, {x.interest:.0f}, {x.principle:.0f}, {x.balance:.0f}')
        amortdate = add_months(amortdate,1)     

main()      
