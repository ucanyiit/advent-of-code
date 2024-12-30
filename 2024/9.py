with open("9.in") as f:
    lines = f.readlines()
    line = lines[0].strip()
    
    file_ids = []
    
    for i in range(len(line)):
        size = int(line[i])
        is_file = i % 2 == 0
        file_id = int(i / 2)
        
        for i in range(size):
            file_ids.append(file_id if is_file else -1)
            
    i = 0
    j = len(file_ids) - 1
    res = 0
    
    while i <= j:
        if file_ids[i] != -1:
            res += i * file_ids[i]
            i += 1
            continue
        if file_ids[j] == -1:
            j -= 1
            continue
        res += i * file_ids[j]
        i+=1
        j-=1
        
    print(res)

def print_chunks(chunks):
    s = ""
    for chunk in chunks:
        for i in range(chunk[0]):
            s += str(chunk[1]) if chunk[1] != -1 else "."
    print(s)
        
with open("9.in") as f:
    lines = f.readlines()
    line = lines[0].strip()
    
    file_ids = []
    chunks = []
    
    for i in range(len(line)):
        size = int(line[i])
        is_file = i % 2 == 0
        file_id = int(i / 2)
        chunks.append((size, file_id if is_file else -1))
    
    # print_chunks(chunks)
    start_map = {}
    
    for i in range(len(chunks)-1 , -1, -1):
        i_is_file = chunks[i][1] != -1
        if not i_is_file:
            continue
        
        file_size = chunks[i][0]
        j_start = 0 if file_size not in start_map else start_map[file_size]
        
        start_map[file_size] = 10000000
        very_end = [(chunks[i][0], -1)] + chunks[i+1:]

        for j in range(j_start, i):
            j_is_file = chunks[j][1] != -1
            if j_is_file or chunks[j][0] < chunks[i][0]:
                continue
            start = chunks[:j]
            end = chunks[j + 1:i] + very_end
            if chunks[j][0] == chunks[i][0]:
                chunks = start + [chunks[i]] + end
            else:
                new_size = chunks[j][0] - chunks[i][0]
                chunks = start + [chunks[i]] + [(new_size, -1)] + end
                for k in range(1, new_size + 1):
                    # print(" - ",k, j, min(
                    #     10000000 if k not in start_map else start_map[k],
                    #     j))
                    start_map[k] = min(
                        0 if k not in start_map else start_map[k],
                        j)
                    
            start_map[file_size] = j
            break

    res = 0
    ii = 0
    for chunk in chunks:
        for i in range(chunk[0]):
            if chunk[1] != -1:
                res += ii * chunk[1]
            ii += 1

    print(res)        