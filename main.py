file_obj=open('three_digit_numbers.txt', 'r')
numbers = [int(line.strip()) for line in file_obj]
missing_numbers = set(range(300, 501)) - set(numbers)
sorted_numbers = sorted(numbers)
output_file=open ('sorted_numbers.txt', 'w')
for num in sorted_numbers:
    output_file.write(str(num) + '\n')
output_file.close()
file_obj.close()