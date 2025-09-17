"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.P"""


n = int(input())

if n < 2 or n > 10:
    print("Enter between 2 and 10 participants")
else:
    arr = list(map(int, input().split()))
    
    # Check if all scores are within the valid range
    if all(-100 <= score <= 100 for score in arr):
        unique_scores = list(set(arr))
        unique_scores.sort(reverse=True)
        if len(unique_scores) >= 2:
            print(unique_scores[1])  # Runner-up score
        else:
            print("No runner-up score available")
    else:
        print("Scores must be between -100 and 100")
            
