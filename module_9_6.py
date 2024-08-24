def all_variants(text):
    t_len = len(text)
    for i in range(t_len):
        for t in range(t_len):
            # print(t,t+i+1)
            yield text[t:t + i +1]

a = all_variants("abc")
for i in a:
    print(i)