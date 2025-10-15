import random
from bisect import bisect_right
import sys

# Increase recursion limit for potentially deep functions, though here it's mainly for safety.
sys.setrecursionlimit(2000)

# --- 1. Pre-calculate Pyramid Block Counts (P_H) ---
# Maximum N is 10^18. Max H corresponding to this N is ~632455.
MAX_H = 640000 
PYRAMID_SUMS = [0] * (MAX_H + 1)

# P_H = Sum of (2i - 1)^2 for i=1 to H
for i in range(1, MAX_H + 1):
    blocks_needed = (2 * i - 1) ** 2
    PYRAMID_SUMS[i] = PYRAMID_SUMS[i - 1] + blocks_needed

# Constants
TARGET_PH = PYRAMID_SUMS[632455] # P_632455 ~ 10^18
MAX_N_S1 = 10**9
H_MAX_S1 = bisect_right(PYRAMID_SUMS, MAX_N_S1, lo=1, hi=MAX_H) - 1 # H_MAX_S1 is 1000

# Emerald values (for remaining blocks calculation)
EMERALD_VALUES = {
    'CP': 1,
    'IR': 5,
    'GD': 20,
    'DM': 100
}

def solve(cp, ir, gd, dm):
    """
    Solves the problem for a single test case (cp, ir, gd, dm).
    Returns (H, R) -> (Max Height, Max Remaining Emeralds).
    """
    N = cp + ir + gd + dm
    
    # 1. Find Max Height (H)
    h_index = bisect_right(PYRAMID_SUMS, N, lo=1, hi=MAX_H) - 1
    
    H = h_index
    
    # Handle the H=0 case explicitly
    if H == 0:
        return 0, (cp * 1 + ir * 5 + gd * 20 + dm * 100)

    blocks_used = PYRAMID_SUMS[H]
    blocks_to_consume = blocks_used
    
    # 2. Consume blocks greedily (CP -> IR -> GD -> DM)
    
    # Copper (CP)
    used_cp = min(cp, blocks_to_consume)
    blocks_to_consume -= used_cp
    
    # Iron (IR)
    used_ir = 0
    if blocks_to_consume > 0:
        used_ir = min(ir, blocks_to_consume)
        blocks_to_consume -= used_ir
        
    # Gold (GD)
    used_gd = 0
    if blocks_to_consume > 0:
        used_gd = min(gd, blocks_to_consume)
        blocks_to_consume -= used_gd
        
    # Diamond (DM)
    used_dm = 0
    if blocks_to_consume > 0:
        used_dm = min(dm, blocks_to_consume)
        
    # 3. Calculate Remaining Emerald Value (R)
    
    left_cp = cp - used_cp
    left_ir = ir - used_ir
    left_gd = gd - used_gd
    left_dm = dm - used_dm
    
    R = (left_cp * EMERALD_VALUES['CP'] +
         left_ir * EMERALD_VALUES['IR'] +
         left_gd * EMERALD_VALUES['GD'] +
         left_dm * EMERALD_VALUES['DM'])
         
    return H, R


def generate_single_case(constraint_type, index):
    """Generates a single (CP, IR, GD, DM) tuple based on constraints and index (for edge case injection)."""
    
    # 1. Edge cases and boundary conditions (mixed into files 1, 5, etc. using index modulo)
    
    # Edge Case 1: H=0
    if index % 25 == 0:
        return (0, 0, 0, 0)
    
    # Edge Case 2: H=1, exact fit
    if index % 25 == 1 and constraint_type == 'S1': 
        return (1, 0, 0, 0)
    
    # Edge Case 3: Max H, exact fit, CP only (tests speed/large number handling)
    if index % 25 == 2:
        H_max = H_MAX_S1 if constraint_type == 'S1' else 632455
        blocks_needed = PYRAMID_SUMS[H_max]
        
        # Ensure blocks_needed doesn't exceed S1 constraint if applicable
        blocks_needed = min(blocks_needed, MAX_N_S1) if constraint_type == 'S1' else blocks_needed

        return (blocks_needed, 0, 0, 0)
    
    # Edge Case 4: Near Miss Case: N is one short of P_H
    if index % 25 == 3:
        H_target = random.choice([5, 100, H_MAX_S1]) if constraint_type == 'S1' else random.choice([10000, 100000, 632455])
        blocks_needed = PYRAMID_SUMS[H_target]
        N = blocks_needed - 1
        
        N = min(N, MAX_N_S1) if constraint_type == 'S1' else N

        # Force high R by supplying only expensive blocks
        cp, ir, gd = 1, 1, 1
        dm = N - 3
        
        if dm < 0: # Fails if N is too small (e.g. N=1), fall back to random
            pass 
        else:
            return (cp, ir, gd, dm)

    # Edge Case 5: High R case (stressing greedy choice): Use only DM/GD, leave massive CP/IR remainder
    if index % 25 == 4:
        H_target = random.choice([5, 10]) if constraint_type == 'S1' else random.choice([10000, 100000])
        blocks_needed = PYRAMID_SUMS[H_target]
        
        # Supply blocks using only DM, leave high CP remainder
        dm_used = blocks_needed
        
        if constraint_type == 'S1':
             # Maximize remainder up to S1 limit
            cp_rem = MAX_N_S1 - dm_used if MAX_N_S1 > dm_used else 1
            if cp_rem < 0: cp_rem = 1
            ir_rem, gd_rem = 1, 1
        else:
            # Maximize remainder up to 10^18
            cp_rem = 10**16 
            ir_rem = 10**16 
            gd_rem = 10**16 
            
        return (cp_rem, ir_rem, gd_rem, dm_used)

    # 6. Standard Random Case
    if constraint_type == 'S1':
        # N up to 10^9
        N = random.randint(1, MAX_N_S1)
    else: # S2
        # N from 10^12 up to TARGET_PH
        N = random.randint(10**12, TARGET_PH) 

    # Distribute N blocks randomly
    cp = random.randint(0, N)
    ir = random.randint(0, N - cp)
    gd = random.randint(0, N - cp - ir)
    dm = N - cp - ir - gd

    # Ensure at least one block of cheapest types if N > 0 to stress greedy choice
    if N > 0 and cp == 0 and ir == 0:
        cp = 1 
        N += 1
        
    # Re-calculate N for a small chance of going over the current N in the shuffle
    
    # Randomly shuffle resource order to ensure input diversity
    resources = [cp, ir, gd, dm]
    random.shuffle(resources)
    return tuple(resources)


def write_files_structured():
    """Generates 10 pairs of files, 4 for S1 and 6 for S2, using zero-padded filenames."""
    
    print("\n--- Generating 10 pairs of structured test files ---")

    # --- Subtask 1 Files (1 to 4) ---
    for file_num in range(1, 5):
        # T <= 1000
        T = random.randint(900, 1000) 
        input_content = [str(T)]
        output_content = []
        
        # Zero-pad the file number
        file_name_padded = f'{file_num:02d}'
        
        for i in range(T):
            cp, ir, gd, dm = generate_single_case('S1', i)
            input_content.append(f"{cp} {ir} {gd} {dm}")
            H, R = solve(cp, ir, gd, dm)
            output_content.append(f"{H} {R}")

        # Use padded file names (e.g., input01.txt)
        with open(f'input{file_name_padded}.txt', 'w') as f:
            f.write('\n'.join(input_content) + '\n')
        with open(f'output{file_name_padded}.txt', 'w') as f:
            f.write('\n'.join(output_content) + '\n')
        print(f"Generated input{file_name_padded}.txt and output{file_name_padded}.txt (T={T}, N<={MAX_N_S1})")

    # --- Subtask 2 Files (5 to 10) ---
    for file_num in range(5, 11):
        # T <= 10^5
        T = random.randint(90000, 100000) 
        input_content = [str(T)]
        output_content = []
        
        # Zero-pad the file number
        file_name_padded = f'{file_num:02d}'
        
        for i in range(T):
            cp, ir, gd, dm = generate_single_case('S2', i)
            input_content.append(f"{cp} {ir} {gd} {dm}")
            H, R = solve(cp, ir, gd, dm)
            output_content.append(f"{H} {R}")

        # Use padded file names (e.g., input05.txt)
        with open(f'input{file_name_padded}.txt', 'w') as f:
            f.write('\n'.join(input_content) + '\n')
        with open(f'output{file_name_padded}.txt', 'w') as f:
            f.write('\n'.join(output_content) + '\n')
        print(f"Generated input{file_name_padded}.txt and output{file_name_padded}.txt (T={T}, N<={TARGET_PH})")
    
    print("\nScript finished. 10 pairs of zero-padded test files are ready.")


if __name__ == '__main__':
    write_files_structured()