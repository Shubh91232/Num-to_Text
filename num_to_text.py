# Define lists of words for numbers
ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
scales = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion']

def number_to_words(num):
    if num == 0:
        return 'zero'
    
    # Split the number into groups of three digits
    num_str = str(num)
    groups = []
    while num_str:
        groups.append(int(num_str[-3:]))
        num_str = num_str[:-3]
    
    words = []
    for i, group in enumerate(groups):
        if group != 0:
            group_words = []
            
            # Convert hundreds place
            hundreds = group // 100
            if hundreds > 0:
                group_words.append(ones[hundreds] + ' hundred')
            
            # Convert tens and ones places
            tens_ones = group % 100
            if tens_ones >= 10 and tens_ones <= 19:
                group_words.append(teens[tens_ones - 10])
            else:
                tens_digit = tens[tens_ones // 10]
                ones_digit = ones[tens_ones % 10]
                if tens_digit:
                    group_words.append(tens_digit)
                if ones_digit:
                    group_words.append(ones_digit)
            
            # Add scale word
            if i > 0:
                group_words.append(scales[i])
            
            words.extend(reversed(group_words))
    
    return ' '.join(reversed(words))

# Example usage
number = int(input("Enter Number : "))
text = number_to_words(number)
print(f"{number} in words: {text}")
