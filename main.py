import pypandoc

def main():
    # https://stackoverflow.com/questions/40988240/pandoc-latex-pdf-headed-and-footer
    # https://stackoverflow.com/questions/16965490/pandoc-markdown-page-break
    args = [
        '-H',
        'header.tex',
        '-V',
        'geometry:margin=2.5cm'
    ]

    output = pypandoc.convert_file(
        'test.md',
        'pdf',
        outputfile='test.pdf',
        extra_args=args
    )

if __name__ == "__main__":
    main()
