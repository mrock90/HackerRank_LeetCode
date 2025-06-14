Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

2 <= n <= 10
-100 <= A[i] <= 100

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

if __name__ == '__main__':
    # Read the number of scores (n)
    # n indicates how many scores will be provided in the next line.
    n = int(input())

    # Read the scores and convert them to a list of integers
    # input().split() reads the line of space-separated numbers and splits it into a list of strings.
    # map(int, ...) converts each string in that list to an integer.
    # list(...) converts the map object into a concrete list for easier manipulation.
    arr = map(int, input().split())
    scores = list(arr)

    # Step 1: Remove duplicate scores
    # Convert the list to a set to automatically remove all duplicate values.
    # Sets only store unique elements.
    # Example: [2, 3, 6, 6, 5] becomes {2, 3, 5, 6} (order is not guaranteed in a set).
    unique_scores = set(scores)

    # Step 2: Convert the set back to a list
    # This is necessary because sets are unordered, and we need a list
    # to sort the elements and access them by index.
    unique_scores_list = list(unique_scores)

    # Step 3: Sort the list of unique scores in ascending order
    # The .sort() method modifies the list in place.
    # Example: {2, 3, 5, 6} (after conversion to list) becomes [2, 3, 5, 6] after sorting.
    unique_scores_list.sort()

    # Step 4: Find the runner-up score
    # In a sorted list, the largest element is at the last index (-1).
    # The second largest (runner-up) is at the second-to-last index (-2).
    runner_up_score = unique_scores_list[-2]

    # Print the runner-up score
    # This adheres to the Output Format requirement.
    print(runner_up_score)