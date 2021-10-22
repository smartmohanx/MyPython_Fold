from bs4 import BeautifulSoup

html_str = '''
<html>
    <body>
        <h1>welcome to python class buddy</h1>
        <h1>i am mohan buddy</h1>
        <h1>forever relationship</h1>
    </body>
</html>
'''
bs = BeautifulSoup(html_str,'html.parser')
result = bs.find_all("h1")
for i in result:
    print(i.text)