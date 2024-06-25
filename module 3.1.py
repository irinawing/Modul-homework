calls = 0

def count_calls():
    global calls
    calls+=1
    return calls

def string_info(str_,len_=0, str_upper='', str_lower=''):
    count_calls()
    len_=len(str_)
    str_upper = str_.upper()
    str_lower = str_.lower()
    return len_, str_upper, str_lower

def is_contains(str_, list_to_search):
     count_calls()
     is_in_list = False
     str_ = str_.lower()
     for i in list_to_search:
        if str_ == i.lower():
            is_in_list = True
     return is_in_list

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)