Marta Kivkule, 241RHM008

# EUROPEAN PARLIAMENT ELECTIONS 2019 - Data Visualizer
###  Description
This program fetches data from the European Parliament elections 2019 API and formats it into tables. The program runs in the command prompt, allowing users to visualize various statistics and information about the elections. To run this program, you need to have Python installed on your system. Additionally, you need to install the following packages: To start it user needs to instal the packages mentioned below and then start it with the run function(below). Then a menu will apear from which the user can choose which of the data it want to visaulize into a table.

There are 5 options to visualize:
    1. Statistics by polling stations
    2. Election candidates
    3. Party info
    4. Statistics of elected candidates
    5. Candidate demographics

For **"Statistics by polling stations"**, the table will show "Polling station location", "Votes" and "Votes in %".

For **"Election candidates"**, the table will show "Name", "Surname", "Party", "Birth year", "Education", "Work place", "Languages skills".

For **"Party info"**, the table will show "Party title", "Candidate Count".

For **"Statistics of elected candidates"**, the table will show "Name", "Surname", "Party", "Count", "Count (%)", "Plus Count", "Minus Count".

For **"Candidate demographics"**, it will visualize the data into 4 table. One of them is going to be - **Age statistics of candidates**, with rows called Age", "Count", "Count (%)", then the 2nd table with the title **Candidates' education statistics**, will show Education", "Count", "Count (%). The third table **Gender statistics** of candidates will show "Gender", "Count", "Count (%)" and the fourth table **Statistics of candidates residence** will show "Place of residence", "Count", "Count (%)".

## Install packages
py -m pip install pick

py -m pip install requests

py -m pip install rich

## Run (in CMD)
`py main.py`


## This program is essential for these reasons:

Transparency and Accessibility: It makes election data more accessible to the public, promoting transparency and trust in the electoral process.
Data Analysis: Researchers, analysts, and political enthusiasts can quickly analyze and interpret election data without manually parsing large datasets.

