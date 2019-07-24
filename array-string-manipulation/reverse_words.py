# Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault. 
# The message has been mostly deciphered, but all the words are backward! 
# Your colleagues have handed off the last step to you.

# Write a function reverse_words() that takes a message as a 
# list of characters and reverses the order of the words in place.

# Decode the message by reversing the words
def reverse_words(message):

    def reverse_str(arr, left, right):
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    reverse_str(message, 0, len(message) - 1)

    start = 0
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            end = i - 1
            reverse_str(message, start, end)
            start = i + 1