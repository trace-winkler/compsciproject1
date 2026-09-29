# Computer Science Project One Introduction

For this project I wanted to dive into making an interface for users to be able to give an input and get an output. I decided to build an easy program that outputs an NFL skill positions players statistics when their name or team is inputted. Overall it was a simple project, both writing the code and collecting the data only took a couple of days, no more than a week.

You can see the interface below. It isn't pretty and it's very bare bones but it gets the job done. Overall I'm proud of how this project turned out. 

<img width="987" height="597" alt="image" src="https://github.com/user-attachments/assets/d20fc1c3-7627-429c-b0ea-fe1e310b40ac" />

## Functions

For this project, I wanted to make sure that the functions were clearly defined so that I didn't get confused during the coding process.

All data that you see used in this program is is from the 2025-26 NFL regular season, and I collected it myself which was a lot of fun. 

#### Function 1 -- load_data(filename)
This function is simply used to open the workbook. After doing this, it will read every row after the header, and return a list of dictionaries. Each dictionary contains one player, their position, name, team, games played, total receptions, total targets, receiving yards, receiving touchdowns, total carries, rushing yards, and rushing touchdowns. A large amount of wide receivers and tight ends have no rushing stats. 

If the function doesn't find either a player or team, it returns an error that allows the user another opportunity to input a player or team name. 

#### Function 2 -- print_receiving_block(player)
This function was my favorite to code, as it allowed me to finally compile all of the statistical data that I collected. Long story short, this function simply prints the statistics of the player requested. 

#### Function 3 -- rec_rus_stats_wr1
This first function is used to determine both the total and average receiving and rushing (if applicable) statistics for the Wide Receiver 1 on all NFL teams. 

#### Function 4 -- rec_rus_stats_rb1
This first function is used to determine both the total and average receiving and rushing statistics for the Running Back 1 on all NFL teams.

#### Function 5 -- rec_rus_stats_te1
This first function is used to determine both the total and average receiving and rushing (if applicable) statistics for the Tight End 1 on all NFL teams.
