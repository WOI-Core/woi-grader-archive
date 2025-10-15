
import random
import os

def generate_test_case(test_case_num,t_min, t_max, d_min, d_max, output_dir):
    file_name = os.path.join(output_dir, f"input{test_case_num:02d}.txt")
    t_value = random.randint(t_min, t_max)
    with open(file_name, 'w') as f:
        f.write(str(t_value) + '\n')
        for _ in range(t_value):
            d = random.randint(d_min, d_max)
            f.write(str(d) + '\n')
    print(f"Generated {file_name} with t={t_value}, d range=[{d_min}, {d_max}]")

output_directory = "/Users/nonbangkok/Documents/VS_code/ComProg/Author/Nonbangkok/Developing/Faith/testcases/input"
os.makedirs(output_directory, exist_ok=True)

# Test Case 1: Subtask 1 (t=1, d around 0)
generate_test_case(1,6, 6, 0, 9, output_directory)

# Test Case 2: Subtask 1 (t small, d small positive)
generate_test_case(2,10, 10, -10, 10, output_directory)

# Test Case 3: Subtask 2 (t small, d with negative values)
generate_test_case(3,50, 60, -10**3, 10**3, output_directory)

# Test Case 4: Subtask 2 (t larger, d up to 10^4, including negative)
generate_test_case(4,90, 100, -10**4, 10**4, output_directory)

# Test Case 5: Subtask 3 (t mid, d up to 10^9, including negative)
generate_test_case(5,300, 500, -10**9, 10**9, output_directory)

# Test Case 6: Subtask 3 (t mid-high, d up to 10^9, including edges)
generate_test_case(6,800, 1000, -10**9, 10**9, output_directory)

# Test Case 7: Subtask 4 (t high, d up to 2*10^10, including negative)
generate_test_case(7,1000, 2000, -2 * 10**10, 2 * 10**10, output_directory)

# Test Case 8: Subtask 4 (t max, d across full range)
generate_test_case(8,2000, 4000, -2 * 10**10, 2 * 10**10, output_directory)

# Test Case 9: Subtask 4 (t max, d across full range)
generate_test_case(9,5000, 7000, -10**10, 2 * 10**10, output_directory)

# Test Case 10: Subtask 4 (t max, d across full range)
generate_test_case(10,9000, 10000, -2 * 10**10, 10**10, output_directory)

print("All 10 test cases generated successfully.")
