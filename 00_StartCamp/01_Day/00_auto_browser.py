import webbrowser

idols = ['bts', 'ioi', 'IU', 'winner', 'red velvet']

for idol in idols:
    print(idol)
    webbrowser.open('https://search.naver.com/search.naver?query=' + idol)