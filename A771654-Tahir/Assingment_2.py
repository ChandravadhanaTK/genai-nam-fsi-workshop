
from collections import Counter

# Create a program that efficiently finds the most frequent element in an array or list,
#  optimizing both time and space complexity.

def most_frequent_element(arr):
    if not arr:
        return None  # Handle empty list

    # Use Counter to count occurrences of each element
    counter = Counter(arr)

    # Find the most common element and its count
    most_common_element, frequency = counter.most_common(1)[0]

    return most_common_element

# Example usage:
def main():

    my_list = [1, 2, 3, 1, 2, 2, 4, 5, 4, 2, 2, 2, 3,1,1,1,1,1,1,1,1]
    result = most_frequent_element(my_list)
    print(f"The most frequent element is: {result}")

if __name__ == "__main__":
    main()

