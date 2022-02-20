from unittest import TestCase
from datetime import datetime
from datetime import date
from decimal import Decimal
class discount:
    def calculate_discount(self,day: date, total: Decimal)->Decimal:
        # initializing date ranges
        date_strt, date_end = datetime(2022, 11, 26), datetime(2022, 12, 24)
        ele = datetime.strptime(day, '%d %m %Y')
        holiday_list = [datetime(2022, 12, 8), datetime(2022, 12, 25), datetime(2022, 12, 26)]
        print("Date : ", ele)
        day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = datetime.strptime(day, '%d %m %Y').weekday()
        day = day_name[day]
        print("Day : ", day)
        print("Total amount : ", total)
        discountdate = False
        # checking for discount date
        if ele >= date_strt and ele <= date_end and ele not in holiday_list and day != 'Sunday':
            discountdate = True
        if discountdate:
            try:
                if (total > 0 and day !='Saturday'):
                    if total < 100:
                        disc = total * 0.05
                    elif total < 500:
                        disc = total * 0.1

                    else:
                        disc = 0.2 * total
                    print("Discount : ", round(disc, 2))
                    print("Net Pay  : ", round(total - disc, 2))
                elif (total > 0 and day =='Saturday'):
                    if total < 100:
                        disc = total * 0.15
                    elif total < 500:
                        disc = total * 0.2

                    else:
                        disc = 0.3 * total
                    print("Saturday Extra Discount : ", round(disc, 2))
                    print("Net Pay  : ", round(total - disc, 2))


                else:
                    print("invalid amount")
                    raise ValueError("invalid amount")
            except:
                print("invalid amount")
                raise ValueError("invalid amount")
        else:
            print("Discount not applicable")
            raise ValueError("Discount not applicable")

class TestGuru(TestCase):
    #Enter date format DD MM YYYY
    #Equivalance partition for Date1 - V
    def testcase1(self):
        dis=discount()
        dis.calculate_discount("09 12 2022",200.25888)

    # Equivalance partition for Date2- IV
    def testcase2(self):
        dis=discount()
        dis.calculate_discount("11 10 2021",500)
    # Equivalance partition for Date3- IV
    def testcase3(self):
        dis=discount()
        dis.calculate_discount("08 12 2023",10)
    # Equivalance partition for amount 1- V
    def testcase4(self):
        dis=discount()
        dis.calculate_discount("23 12 2022",80)

    # Equivalance partition for amount 2- IV
    def testcase5(self):
        dis=discount()
        dis.calculate_discount("01 12 2022",0)
    # Equivalance partition for amount 3- IV
    def testcase6(self):
        dis=discount()
        dis.calculate_discount("02 12 2022",-100.25)
    #Boundary value analysis for date 1 -IV
    def testcase7(self):
        dis=discount()
        dis.calculate_discount("25 11 2022",300)
    #Boundary value analysis for date 2-V
    def testcase8(self):
        dis=discount()
        dis.calculate_discount("26 11 2022",500)

    #Boundary value analysis for date 3-V
    def testcase9(self):
        dis=discount()
        dis.calculate_discount("27 11 2022",658)
    #Boundary value analysis for date 4-V
    def testcase10(self):
        dis=discount()
        dis.calculate_discount("23 12 2022",658)

    # Boundary value analysis for date 5-V
    def testcase11(self):
        dis = discount()
        dis.calculate_discount("24 12 2022", 65.58)

    # Boundary value analysis for date 6-IV
    def testcase12(self):
        dis = discount()
        dis.calculate_discount("25 12 2022", 0)

    # Boundary value analysis for amount 1-IV
    def testcase13(self):
        dis = discount()
        dis.calculate_discount("02 12 2022", 0)

    # Boundary value analysis for amount 2-V
    def testcase14(self):
        dis = discount()
        dis.calculate_discount("01 12 2022", 1)

    # Boundary value analysis for amount 3-V
    def testcase15(self):
        dis = discount()
        dis.calculate_discount("01 12 2022", 2)

    # Boundary value analysis for amount 4-V
    def testcase16(self):
        dis = discount()
        dis.calculate_discount("01 12 2022", 98)

    # Boundary value analysis for amount 5-V
    def testcase17(self):
        dis = discount()
        dis.calculate_discount("01 12 2022", 99)

    # Boundary value analysis for amount 6-V
    def testcase18(self):
        dis = discount()
        dis.calculate_discount("01 12 2022", 100)

    # Boundary value analysis for amount 7-V
    def testcase19(self):
        dis = discount()
        dis.calculate_discount("01 12 22", 101)

    # Boundary value analysis for amount 8-V
    def testcase20(self):
        dis = discount()
        dis.calculate_discount("01 12 22", 498)

    # Boundary value analysis for amount 9-V
    def testcase21(self):
        dis = discount()
        dis.calculate_discount("01 12 2022", 499)

    # Boundary value analysis for amount 10-V
    def testcase22(self):
        dis = discount()
        dis.calculate_discount("01 12 2022", 500)

    # Boundary value analysis for amount 11-V
    def testcase23(self):
        dis = discount()
        dis.calculate_discount("01 12 2022", 501)

    #Test cases for saturday discount-V/addtional discount
    def testcase24(self):
        dis=discount()
        dis.calculate_discount("10 12 2022",500)

    def testcasenew(self):
        dis = discount()
        dis.calculate_discount("10 12 2022", "500")
    #Test case for Sunday-IV
    def testcase25(self):
        dis=discount()
        dis.calculate_discount("11 12 2022",500)

    #Test case for holiday-IV
    def testcase26(self):
        dis=discount()
        dis.calculate_discount("08 12 2022",10)

    #Test case for not date type-IV
    def testcase27(self):
        dis=discount()
        dis.calculate_discount("date",10)

    #Test case for not amount type-IV
    def testcase28(self):
        dis=discount()
        dis.calculate_discount("13 12 2022","55")
#Test case for not amount type-IV
    def testcase29(self):
        dis=discount()
        dis.calculate_discount("07 12 2022",5555555555)