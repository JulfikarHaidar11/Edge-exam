def find_unique_twice(lst):
    counts = {}
    
    # Count occurrences of each number
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Collect numbers that appear exactly twice
    result = []
    for num, count in counts.items():
        if count == 2:
            result.append(num)

    return result

# Example usage
example_list = [1, 2, 3, 2, 4, 1, 5, 6, 6]
print(find_unique_twice(example_list))  
