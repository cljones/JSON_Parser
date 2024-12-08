# JSON_Parser

During my time as an intern and contract software engineer, I often had to go through tedious routines just to make sure the JSON file is read properly when I test a website before I give word that the website is good to go live. Some of the key values would contain invalid values like “N/A” when they are supposed to contain an integer or a double value, and sometimes the integer or double values are saved as string values. These problems made my web development routine aggravating and time consuming. Rather than constantly going back and forth between my favorite text editor and IDE I would rather just have something to just automatically parse the correct key values in the JSON file to make the web development routine go more smoothly. This application that I wrote accomplishes that goal.

The Process
1. The JSON parser takes one key at a time, so, for the first step enter the key value you want to “clean up”.
2. Next just click on the Parse button.
3. Choose the JSON file you want to work with.
4. After the JSON file is chosen the parser will automatically change the key values into the correct data types and eliminate all unnecessary “N/A”s and show you the new edition of your JSON file via chosen text editor.
