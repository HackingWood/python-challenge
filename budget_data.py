import os
import csv
import statistics
#store each month being counted
month_counter = set()
#value for total profit or loss
gross_profit = 0
#value for greatest profit
greatest_profit = 0

#value for greatest loss
greatest_loss = 0

list_of_profits = []
prev_cur = 0

csvpath = os.path.join("budget_data.csv")
with open(csvpath, encoding='UTF-8') as csv_file:
    budget_reader = csv.reader(csv_file, delimiter =",")
    #skips the header rows
    next(budget_reader)
    

    for row in budget_reader:
        #define columns 
        date_string = row[0]
        currency = int(row[1])

        changes_per_month = []


        gross_profit = gross_profit + int(currency)
      
        month_counter.add(date_string)
        list_of_profits.append(currency)


        #find the greatest profit and save the date/value
        if currency - prev_cur > greatest_profit:
            greatest_profit = currency - prev_cur
            
            our_best_day = date_string
        #find the geatest loss and save the date/value    
        if prev_cur - currency > greatest_loss:
            greatest_loss = prev_cur - currency
            the_great_depression = date_string


        #iterate through the list of profits starting from the second value
        for i in range(1, len(list_of_profits)):
            #add the difference between each month to the changes per month list
            changes_per_month.append(list_of_profits[i] - list_of_profits[i-1])

        prev_cur = currency

    num_unique_months = len(month_counter)
    average_profits = round(statistics.mean(changes_per_month),2)

    #print(num_unique_months)
    #print(gross_profit)
    #print(greatest_profit)
    #print(our_best_day)
    #print(greatest_loss)
    #print(the_great_depression)
    #print(average_profits)

#make text file with analysis
with open ('Financial_Analysis.txt','w') as file:
    #i have no idea why but i get an error if i try to hit enter and split up the lines for easy viewing after every "\n"
    #error reads:
    #SyntaxError: unterminated string literal
    #And points at the start of the f-string
    #this outputs a text file fine as is though

    file.writelines(f'Financial Analysis \nTotal Months: {num_unique_months} \nTotal: ${gross_profit} \nAverage Change: ${average_profits} \nGreatest Increase in Profits: {our_best_day} (${greatest_profit}) \nGreatest Decrease in Profits: {the_great_depression} ({greatest_loss})')
