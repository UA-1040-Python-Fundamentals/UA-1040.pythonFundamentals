#No yelling!

def filter_words(st):
    return ' '.join(st.split()).lower().capitalize()
    # Your code here.

print(filter_words('Hello        ssss'))
