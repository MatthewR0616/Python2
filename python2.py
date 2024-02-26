def product(a, b):
     return a + b

def weekday_name(day_of_week):
    
    DAYS = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    if day_of_week < 1 or day_of_week > 7:
        return None

    return DAYS[day_of_week - 1]

def last_element(lst):
      return (lst[-1])

def number_compare(a, b):
   if a > b:
       return "First is greater"
   elif b > a:  
       return  "Second is greater"
   else:
       return "Both are equal"
   

        
def reverse_string(phrase):
    return phrase[::-1]


def single_letter_count(word, letter):
       return word.count(letter)

def multiple_letter_count(phrase):
    counter = {}

    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1

    return counter

def list_manipulation(lst, command, location, value=None):
    if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)

    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst

def is_palindrome(phrase):
    
    normalized = phrase.lower().replace(' ', '')
    return normalized == normalized[::-1]

def frequency(lst, search_term):

    return lst.count(search_term)

def flip_case(phrase, to_swap):
    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out






    


   


    
   


