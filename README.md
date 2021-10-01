# python-challenge

 ## PyBank - In this challenge, my Python script needs to analyze the financial records of a company. I give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, this company has rather lax standards for accounting so the records are simple.)  * My task was to create a Python script that analyzes the records to calculate each of the following: 
1.) The total number of months included in the dataset 
2.) The net total amount of "Profit/Losses" over the entire period 
3.) Calculated the changes in "Profit/Losses" over the entire period, then find the average of those changes
4.) The greatest increase in profits (date and amount) over the entire period
5.) The greatest decrease in profits (date and amount) over the entire period

As an example, my analysis looks similar to the one below:    
Financial Analysis   ----------------------------   Total Months: 86   Total: $38382578   Average  Change: $-2315.12   Greatest Increase in Profits: Feb-2012 ($1926159)   Greatest Decrease in Profits: Sep-2013 ($-2196167)   

* In addition, my final script prints both the analysis to the terminal and exports a text file with the results. 

  
## PyPoll - In this challenge, my Python script is mean to help a small, rural town modernize its vote counting process.  I am given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. My task was to create a Python script that analyzes the votes and calculates each of the following:  
1.) The total number of votes cast 
2.) A complete list of candidates who received votes 
3.) The percentage of votes each candidate won 
4.) The total number of votes each candidate won 
5.) The winner of the election based on popular vote.  

As an example, my analysis looks similar to the one below:  
Election Results   -------------------------   Total Votes: 3521001   -------------------------   Khan: 63.000% (2218231)   Correy: 20.000% (704200)   Li: 14.000% (492940)   O'Tooley: 3.000% (105630)   -------------------------   Winner: Khan   -------------------------   

* In addition, my final script prints both the analysis to the terminal and exports a text file with the results.
