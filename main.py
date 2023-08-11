import pypandoc

def main():
    output = pypandoc.convert_file('test.md', 'pdf', outputfile='test.pdf')
    # print(type(output))

    # f = open("test.pdf", "x")
    # f.write

if __name__ == "__main__":
    main()
