# Election Analysis



### Overview of Election Audit

A Colorado Elections Board employee called Tom has requested for an audit on a Colorado congressional precinct to report on the election results. The reporting and audit is usually done in Excel. However, Tom would like to know if the tabulation can be automated with a Python script. This audit will explore whether the reporting process can be automated and applied accross other elections in the future. When the script is executed, the output/results can either be viewed in the terminal or viewed in a text file.

----

### Election-Audit Results:


After running the election analysis audit, the results below are as follows (or refer to screenshot image below):

*  A total of 369,11 votes were cast in this congressional election. To calculate the total number of votes casted, a *for* loop was used to iterate through each             row of the CSV file containing the election data and then incremented and stored in the *total_votes* variable. The *total_votes* variable is initialised to 0 before the *for* loop begins.
*  Votes by county:
    * Jeffersson County accounted for 10.5% votes (38,855)
    * Denver County accounted for 82.8% votes (306,055)
    * Arapahoe County accounted for 6.7% votes (24,801)
* Denver County had the largest number of votes accounting for 82% of total votes.

* Number of votes each candidate received:  
    * Charles Casper Stockham received 23.0% of the vote (85,213)
    * Diana DeGette received 73.8% of the vote (272,892)
    * Raymon Anthony Doane received 3.1% of the vote (11,606)
* Candidate Diana DeGette won the election. She received the highest number of votes **272,892** and accounted for 73.8% of the votes.


![screenshot terminal output](https://github.com/YanLuong/Election_Analysis/blob/main/Resources/Terminal%20Output%20Of%20Results.png)

### Methods used to calculate the candidate and county vote.

A *for* loop was used to calculate both the candidate and county votes to read in each row of the data set. Two conditional *if* loops were nested within the *for* loop, one used to calculate the candidate votes and then the other for county votes. They both followed the similar conditional checks. The *if* statement, would first check if the candidate name exists in the candidate_options list [], if it does not then the candidate's name would be added(appended) to the candidate_options list.
Once the candidate is in the list or already exists in the list, it will begin counting the candidate votes by +1 everytime it appears when the for loop iterates through each row in the csv data set. The same format was applied for county votes.

![counting candidate votes](https://github.com/YanLuong/Election_Analysis/blob/main/Resources/Counting%20votes%20-%20candidate%20screenshot.png)





----

### Election-Audit Summary: 

This election audit showed that the script can be used successfully during the tabulation process of the election. This script also has potential to be used across other elections. With some modifications, it can be applied to other districts. Depending on where the csv data file is stored, the file_to_load path would need to be updated to reflect the new directory file path so that the correct file is located. If the csv data file is renamed, that would also have to be reflected in the file_to_load section of the script. Another thing to consider is where the text file will be saved? If the file directory is changed then we would need to consider updating the file_to_save part of the script to a new directly as well.
