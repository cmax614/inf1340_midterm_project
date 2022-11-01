# inf1340_midterm

#Description
This program takes a csv file containing information of a company's monthly stock prices, and can perfrom the following tasks:
  1. Show descriptive Statistics of the stock
  2. Retrieve stock price on a specific date
  3. Visualize the monthly stock prices with a plot

#Execution instruction
When you run the program, it will asks for an input for the company file name (e.g. MCD for Mcdonald's)
Next, a Menu would pop up with the following options:
  Menu: 
  P = show descriptive statistics
  V = Visualize firm volatility
  D = show price on given date
  Q = Quit application
The program would prompt you to enter one of the letters to perform the corresponding task
Once the task is performed, the program would show menu again, and is ready to perform another task
When the user enter Q, you will quit the application and exit the program

#Example
The following example shows the user chooses to input the csv file of Mcdonald's stock
The user first chooses to retrieve the price on the date 2022-04-01
Then the user exit the program.

  Enter company file name(e.g. MCD)MCD
  Menu: 
  P = show descriptive statistics
  V = Visualize monthly stock prices
  D = Fetch price on given date
  Q = Quit application
  What do you want to do?(P,V,D,Q)D
  Which date?(e.g. 2022-06-01)2022-04-01
  The stock price on 2022-04-01 is $246.437775
  Menu: 
  P = show descriptive statistics
  V = Visualize monthly stock prices
  D = Fetch price on given date
  Q = Quit application
  What do you want to do?(P,V,D,Q)Q
