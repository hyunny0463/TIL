def my_url(itemPerPage=10, **api):
    if itemPerPage not in range(1, 11):
        return '1~10까지의 값을 넣어주세요.'
    if api.get('key') == None or api.get('targetId') == None:
        return '필수 요청변수가 누락되었습니다.'
        
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    url += f'itemPerPage={itemPerPage}&'
    for key, value in api.items():
        url += f'{key}={value}&'
    return url