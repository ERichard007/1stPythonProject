import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def deposit():
    while True:
        amount = input("Deposit some money? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter some amount of money.")
        else:
            print("Please enter a number")

    return amount

def Get_Number_Of_Lines():
    while True:
        lines = input("Enter number of lines (1-" + str(MAX_LINES) + ")?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Please enter a number of lines between 1 and",MAX_LINES)

    return lines

def get_bet(Balance,Lines):
    while True:
        bet = input("How mouch would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET and bet*Lines <= Balance:
                break
            else:
                print(f"This would be a ${bet*Lines} total bet")
                print(f"Amount must be in between {MIN_BET} and {MAX_BET}. Also less then your balance of ${Balance}")
        else:
            print("Please enter a number")

    return bet

def get_slotmachine_spin(rows,cols,symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    
    for col in range(cols):
        Row = []
        for row in range(rows):
            value = random.choice(all_symbols)
            Row.append(value)
        columns.append(Row)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        print('|',end='')
        for x,column in enumerate(columns):
            if x!=len(columns)-1:
                print(column[row],end='|')
            else:
                print(f'{column[row]}|')

def Three_In_A_Row(columns):
    LettersWon = []
    RowWon = -1
    for col in columns:
        for pos,num in enumerate(col):
            if num == columns[1][pos] == columns[2][pos]:
                LettersWon.append(num)
                RowWon = pos
        break
    return LettersWon, RowWon+1

def main():
    Play = input('Would you like to play a little game?\n\n\n(y/n): ')

    if Play == 'y':
        print('\n\n\n')
        MoneyDeposited = deposit()
        StartedWith = MoneyDeposited

        while Play =='y':
            Lines = Get_Number_Of_Lines()
            Bet = get_bet(MoneyDeposited,Lines)
            Total = Bet*Lines

            print(f'You are betting ${Bet} on {Lines} lines. Your Total bet is ${Total}')

            columns = get_slotmachine_spin(ROWS,COLS,symbol_count)
            print_slot_machine(columns)

            LettersWon,RowWon = Three_In_A_Row(columns)

            if len(LettersWon)>0 and 0<=RowWon<=Lines:
                TotalWon = 0
                for letter in LettersWon:
                    TotalWon += (10-symbol_count[letter])*Bet

                MoneyDeposited += TotalWon

                print(f"YOU WON!\nTotal Win: ${TotalWon}\nNew Deposit Of: ${MoneyDeposited}")
                
                Play = input("\n\n\nTry again?(y/n): ")
                if Play =='y':
                    DepositMore = input(f"\n\n\nWould you like to deposit more money? Current Balance: ${MoneyDeposited}\n(y/n): ")
                    if DepositMore == 'y':
                        MoneyDeposited = MoneyDeposited + deposit()
                        StartedWith += MoneyDeposited
                    print('\n\n\n')
            else:
                MoneyDeposited -= Total
                Play = input(f"Sorry no matches...\nNew Deposit Of: ${MoneyDeposited}\n\n\nTry again?(y/n): ")
                if Play =='y':
                    DepositMore = input(f"\n\n\nWould you like to deposit more money? Current Balance: ${MoneyDeposited}\n(y/n): ")
                    if DepositMore == 'y':
                        MoneyDeposited = MoneyDeposited + deposit()
                        StartedWith += MoneyDeposited
                    print('\n\n\n')
        else:
            print(f'\n\n\n\n\nYou put in ${StartedWith} and ended up with ${MoneyDeposited}\n\nTotal Won/Lost: ${MoneyDeposited-StartedWith}')
    else:
        print('\n\n\nOk then...        Bye')

main()