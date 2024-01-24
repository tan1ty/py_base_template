def longest_match(sequence, subsequence):
    longest_run = 0
    count = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
    i = 0

    while i < sequence_length:
        # Check if the next part of the sequence matches the subsequence
        if (i + subsequence_length <= sequence_length and 
            sequence[i:i+subsequence_length] == subsequence):
            count += 1
            i += subsequence_length  # Jump ahead by the length of the subsequence
        else:
            longest_run = max(longest_run, count)
            count = 0
            i += 1  # Move just one position ahead if no match

    # Update longest run for the last counted run (if the loop ended with a run)
    longest_run = max(longest_run, count)

    print(longest_run)


longest_match('AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG', 'AAGG')

def longest_matched(sequence, subsequence):
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0        
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1          
            else:
                break                

        longest_run = max(longest_run, count)
    print(longest_run)

longest_matched('AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG', 'AAGG')