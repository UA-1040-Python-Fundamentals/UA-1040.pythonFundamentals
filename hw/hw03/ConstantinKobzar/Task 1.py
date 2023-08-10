def main():
    # The given line containing the Python philosophy
    python_philosophy = """
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    """

    # Find the number of occurrences of the words "better", "never", and "is" in the given line
    occurrences_better = python_philosophy.count("better")
    occurrences_never = python_philosophy.count("never")
    occurrences_is = python_philosophy.count("is")

    print(f"Occurrences of 'better': {occurrences_better}")
    print(f"Occurrences of 'never': {occurrences_never}")
    print(f"Occurrences of 'is': {occurrences_is}")

    # Display all text in uppercase
    python_philosophy_uppercase = python_philosophy.upper()
    print("\nText in uppercase:")
    print(python_philosophy_uppercase)

    # Replace all occurrences of the symbol "i" with "&"
    python_philosophy_replaced = python_philosophy.replace("i", "&")
    print("\nText with 'i' replaced by '&':")
    print(python_philosophy_replaced)

if __name__ == "__main__":
    main()