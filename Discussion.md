## Solutions Considered
To extract logs efficiently from large file as such, I thought of follwing appraches from which I went with the last one.

### **1. Using String Splitting**
One basic approach could have been splitting each line using spaces **line.split(" ")** and checking if the first element matches the given date. But splitting every line into a list is way too much memory space used and time consuming. Also regular expressions are clearer when dealing with structured logs.

### **2. Using Regular Expressions**
Instead of splitting strings, I decided to use **regular expressions** to match logs starting with the given date. I went with this since it directly checks if the line starts with the date instead of unnecessary splitting, and works well even if the log format slightly changes.


### Extra Stuff I Added:
**1. UTF-8 Encoding** - I explicitly set `encoding='utf-8'` to avoid weird encoding issues across different platforms. Logs could have special characters, so this takes care of it.

**2. Exception Handling** - Instead of assuming everything will go perfectly, I wrapped file operations in a `try-except` block to catch errors.

**3. Output Directory Handling** - Automatically creates an `output/` folder if it doesn’t exist, so the user doesn’t have to worry about manually making it.


**Update** : I just opened test_log file and found the log format is like **2024-11-02T07:19:55.0000 - ERROR - User successfully logged in** instead of given in Readme.md. So all i had to change in my code was `pat = re.compile(f"^{date} ")` to `pat = re.compile(f"^{date}T")`

## **Steps to run**

Place extract_logs.py in the same directory as the log file. Run the script with a date:

`python extract_logs.py 2024-12-01`


Extracted logs will be in output/output_YYYY-MM-DD.txt.


