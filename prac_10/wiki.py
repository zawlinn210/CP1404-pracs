"""
CP1404 - Practical 10
Wikipedia API & Python Library
"""
import wikipedia


def main():
    print("Enter a wiki page title")
    user_input = input(""">>>""")
    while user_input != "":
        try:
            page = wikipedia.page(user_input, auto_suggest=False)
            print(f"Title: {page.title}")
            print(f"URL: {page.url}")
            print(f"Summary: {page.summary}")
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        user_input = input(""">>>""")
    print("Done")


main()