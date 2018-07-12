import os


# fetching a list of all our raw text
raw_files = os.listdir('raw')

for rf in raw_files:
    with open(f'raw/{rf}', 'r', encoding='utf-8') as f:
        title = f.readline().rstrip()  # grabbing the first line as our title
        content = ""
        for line in f.readlines()[1:]:  # everything but the first line
            content += f"<p>{''.join(line.rstrip())}</p>"
        # creating a basic HTML structure with our text input
        page = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    {content}
</body>
</html>"""
        # and finally writing the content to a HTML file
        with open(f'pages/{rf[:-4]}.html', 'w') as f:
            f.write(page)
