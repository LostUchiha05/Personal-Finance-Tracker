import argparse
from financeTracker import add_income,add_expense,filter_data
parser=argparse.ArgumentParser()


parser.add_argument("commands",choices=["income","expense","filter"],help="Select the Mode you want")
parser.add_argument("-a","--amount",type=int,help="For Entering the Amount")
parser.add_argument("--Description","-d",help="For the Description for the Amounts Nature")
parser.add_argument("--Date",help="Only for Filtering")
args = parser.parse_args()

if(args.commands == "income"):
    add_income(args.amount,args.Description)
elif(args.commands == 'expense'):
    add_expense(args.amount,args.Description)
elif(args.commands == 'filter'):
    result = filter_data(args.Date)
    if result:
        print(result)
