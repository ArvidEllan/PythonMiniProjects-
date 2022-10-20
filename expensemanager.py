while True:
    try:
        input_read = int(input('how much did i earn last month'))
        input_count = int(input('how much will i spend on food'))
        input_count1 = int(input("where is your data"))
        break
    except ValueError:
        print("that is not a valid option brudda")
total_amount = int(input_read)
expense = int(input_count) + int(input_count1)
if expense > total_amount:
    print('not cutting according to budget? step mahn')
money_left = total_amount -expense
if money_left < 0.5 * total_amount:
    print('Bossman' + str(money_left) + ' ball out ')
input_count2 = input('how much have you saved right now')
savings = int(input_count2)
miscellaneous = money_left - savings
if savings > money_left:
    print('Howww???')
if miscellaneous > savings:
    print('still remaining' + str(miscellaneous))
    input_answer = input('would you want to save more' + 'please input Y or N')
    if input_answer.casefold() == 'Y':
        print('great idea!')
    elif input_answer.casefold() == 'N':
        print('i guess that means you have ' + str(miscellaneous) + 'for miscellaneous expenses')
input_answer1 = int(input('how much more '))
savings1 = savings + int(input(input_answer1))
miscellaneous_new = miscellaneous - savings1
if miscellaneous <= savings:
    print('use the remaining ' + str(miscellaneous_new) + 'you have earned it ')