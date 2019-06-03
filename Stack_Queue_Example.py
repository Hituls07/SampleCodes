class Solution:

    def __init__(self):
        self.stack = []
        self.queue = []

    # Stack methods
    def pushCharacter(self, char):  # Adds input at the end of the stack
        self.stack.append(char)

    def popCharacter(self):     # Removes the last(most recent) element from the stack
        if len(self.stack) < 1:  # if there is no element left then
            return None
        return self.stack.pop()

    # Queue methods
    def enqueueCharacter(self, char):  # Adds input at the end of the queue
        self.queue.append(char)

    def dequeueCharacter(self):  # Removes the first element from the queue
        if len(self.queue) < 1:   # if there is no element left then
            return None
        return self.queue.pop(0)


obj = Solution()
s = input()  # read the input string

for i in s:
    obj.pushCharacter(i)
    obj.enqueueCharacter(i)


isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for j in range(len(s) // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

if isPalindrome:
    print('This word {} is a palindrome'.format(s))
else:
    print('This word {} is not a palindrome'.format(s))

