import pypandoc

def main():
    output = pypandoc.convert_file('test.md', 'pdf', outputfile='test.pdf')

if __name__ == "__main__":
    main()
