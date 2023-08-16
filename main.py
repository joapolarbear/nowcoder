import bisect
from datetime import datetime
from prettytable import PrettyTable  
  



INFINIT = 1e6
DEBUG = False
def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def main():
    s = input().strip()
    date = datetime.fromisoformat(s)

    # # Creating a new table   
    # newTable = PrettyTable(["DAY AND DATE", "START TIME", "END TIME", "LOCATION"]) 
    # # Add rows  
    # newTable.add_row([date.strftime("%b. %-d, %Y"), "8:30 AM", "9:00 AM", "Online"])

    rst = f'DAY AND DATE: {date.strftime("%b. %-d, %Y")}\t\tLOCATION: Online'
    rst += f'\nSTART TIME: 8:30 AM\t\t\tEND TIME: 9:00 AM'
    print(rst)


while True:
    try:
        main()
    except EOFError:
        break