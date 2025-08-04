# Communication Contract
## How to REQUEST data
Request data from the software by writing into weighted-scores-calculator.txt. Data must be written with the following parameters in this exact order:
1. Item Identifier
2. Category, category weight, score of item

No spaces between commas allowed. More than one category can be requested at a time as an optional parameter. All parameters must be separated by a new line.

Example request call:
Your program:
```
with open('weighted-scores-calculator.txt', 'w', newline='') as f:
    f.write('Poodle\nbreed,2,1\nsize,1,2')
```

weighted-scores-calculator.txt:
```
Poodle
breed,2,1
size,1,2
```

In this example, the item identifier is "Poodle." The second parameter is the category "breed," category weight "2," and item score "1." PLease note that there are no spaces between the commas. An extra category is requested in a separate line. This follows the format of parameter 2 with the category "size," followed by category weight "1," and item score "2."

## How to RECEIVE data
Receive data from the microservice by reading weighted-scores-calculator.txt after it has been updated.

After writing your REQUEST to the weighted-scores-calculator.txt, the software will calculate the requested data and write into the same text file, weighted-scores-calculator.txt. The response will either be a 2d array of the requested data with a total weighted score, or an error message.

Example receive call:
Your program:
```
with open('weighted-scores-calculator.txt', 'r', newline='') as f:
    data = f.read()
    print(data)
```

Console:
```
[['Item ID', 'breed (2)', 'size (1)', 'Total Weighted Score'], ['Poodle', '1', '2', 4]]
```

If your REQUEST call was formatted incorrectly, you'll receive one of the following errors:
- **Error: Parameters missing. See Documentation for details.**: One or more parameters are missing. Please refer to this document for details on correct formatting.
- **Error: Priority category is missing data.**: Parameter 2 or any additional category parameters are missing either a category name, category weight, or item score. Please refer to this document for details on correct parameter details.
- **Error: Priority category weight or score is not a number.**: The entered category weight or item score is not numeric. Please refer to this document for details on correct parameter details.

## UML Sequence Diagram
![UML Image](/Images/uml.png)
