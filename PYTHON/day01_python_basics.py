# 1. Reverse a string and a list without using [::-1]
def reverse_string(text: str) -> str:
    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text
    return reversed_text

my_word = "SIDDHARTH"
result = reverse_string(my_word)
print("Original:", my_word)
print("Reversed:", result)

# 2. Reverse a list
def reverse_list(items: list) -> list:
    left, right = 0, len(items) - 1
    arr = items.copy()
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

my_list = [10, 20, 30, 40]
print("Reversed list:", reverse_list(my_list))

# EASY WAYS TO REVERSE LIST
nums = [10, 20, 30, 40]
nums.reverse()
print(nums)  # [40, 30, 20, 10]

#3. element_frequency
def element_frequency(items: list) -> dict:
    return {item: items.count(item) for item in set(items)}

skills = ["python", "sql", "python", "ml", "sql", "python"]
print("Frequency:", element_frequency(skills))

nums1 = [1, 1, 1, 2, 4, 6, 7]  #[cite: 10]
nums2 = [1, 2, 3, 6, 7, 8, 9, 10]  #[cite: 10]

n = len(nums1)  #[cite: 10]
m = len(nums2)  #[cite: 10]

i = 0  #[cite: 10]
j = 0  #[cite: 10]

merged = []

while i < n and j < m:  #[cite: 10]
    if nums1[i] <= nums2[j]:  #[cite: 10]
        merged.append(nums1[i])
        i += 1
    else:
        merged.append(nums2[j])
        j += 1

# 4 Append any remaining elements from nums1 or nums2
while i < n:
    merged.append(nums1[i])
    i += 1

while j < m:
    merged.append(nums2[j])
    j += 1

print("Merged (with duplicates):", merged)

# Without duplicates (matching the video title's focus)
merged_no_duplicates = []
for val in merged:
    if not merged_no_duplicates or merged_no_duplicates[-1] != val:
        merged_no_duplicates.append(val)

print("Merged (without duplicates):", merged_no_duplicates)

# 4. Two-Sum in O(n) time using a dictionary
def two_sum(nums: list, target: int) -> list:
    seen = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
    return []

nums = [2, 7, 11, 15]
target = 9
print("Two Sum indices:", two_sum(nums, target))

