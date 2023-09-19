# DESCRIPTION:
# Write a function taking in a string like WOW this is REALLY
# amazing and returning Wow this is really amazing. String should be capitalized
# and properly spaced. Using re and string is not allowed.
#
# Examples:
#
# filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
# filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
# filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary!

def filter_words(st):
    text = st.strip()
    text = text[0].upper() + text[1:].lower()
    text = " ".join(text.split())
    return text


a= filter_words("   This    WIll    not    pass   ")
print(a)

# a = "   This    WIll    not    pass   "
# a.strip()
# print(a.strip())