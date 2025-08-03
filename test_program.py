import time

while True:
    priority1 = input("What's your number one priority in looking for a doggo?")
    weight1 = '3'
    priority2 = input("What's your second priority in looking for a doggo?")
    weight2 = '2'
    priority3 = input("What's your third priority in looking for a doggo?")
    weight3 = '1'

    print(".........................................")
    print("Awesome! Let's look for a match.")
    print("Looking for furry friend...")
    time.sleep(5)
    print("Match found!")
    print(".........................................")
    print("Here's Lauren, a medium-sized poodle. She's rather shy, but once she warms up to you, she likes to sit by your side and cuddle.")
    prompt_starter = "How would you rate Lauren on "
    score1 = input(prompt_starter + priority1 + '?')
    score2 = input(prompt_starter + priority2 + '?')
    score3 = input(prompt_starter + priority3 + '?')

    with open('weighted-scores-calculator.txt', 'w', newline='') as f:
        f.write('Laruen\n' + priority1 + ',' + weight1 + ',' + score1 + '\n' + priority2 + ',' + weight2 + ',' + score2 + '\n' + priority3 + ',' + weight3 + ',' + score3)
        # f.write('Laruen\n' + priority2 + ',' + weight2 + ',' + score2 + '\n' + priority3 + ',' + weight3 + ',' + score3 + '\n' + priority1 + ',' + weight1 + ',' + score1)  #scores out of order

    time.sleep(5)

    with open('weighted-scores-calculator.txt', 'r', newline='') as f:
        print(f.read())

    time.sleep(20)
