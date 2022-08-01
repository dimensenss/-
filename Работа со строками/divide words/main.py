def foo(text):
    for item, i in enumerate(len(text),0):
        if i.isupper():
            text = text

    return text    
            
def main():
    print(foo('helloWorld'))
if __name__ == "__main__":
    main()