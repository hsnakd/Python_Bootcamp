"""

20. Create a python file named browser. Write a program that can display the name of selected browser
        1. declare a String variable named browser_name
        2. Assume that the valid browsers are: chrome, firefox, opera, safari, edge.
        3. if the browser name does not match with the valid browser names, out put should be: Invalid Browser Name

        Ex:
            String browser = "chrome";

        Output:
            Chrome Browser is selected

        Note: MUST use nested if

"""

browser_name = str(input("Enter Browser Name: ")).lower()

if browser_name == "chrome":
    selected_browser = "Chrome Browser"
elif browser_name == "firefox":
    selected_browser = "Firefox Browser"
elif browser_name == "opera":
    selected_browser = "Opera Browser"
elif browser_name == "safari":
    selected_browser = "Safari Browser"
elif browser_name == "edge":
    selected_browser = "Edge Browser"
else:
    selected_browser = "Invalid Browser Name"

print(selected_browser + " is selected")

