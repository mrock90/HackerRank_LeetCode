Task
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i ** 2 .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

0
1
4
Input Format

The first and only line contains the integer, .

Constraints

1 <= n <= 20

Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16

if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i**2)