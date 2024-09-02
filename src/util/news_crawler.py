import requests
import urllib.parse

from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_links(url):
    # Get the soup of the page
    soup = get_soup(url)
    # Get all the links in the page
    links = soup.find_all('a')
    return links


def get_html(url):
    # Get the HTML of the page
    response = requests.get(url)
    return response.text


def get_soup(url):
    # Get the soup of the page
    html = get_html(url)
    return bs4.BeautifulSoup(html, 'html.parser')


def get_uplus_news_links():
    # Get the links of the news articles
    return get_links('https://www.uplus.co.kr/news/main')


def get_url_robot_txt(url):
    # Get the robots.txt of the page
    return requests.get(url + '/robots.txt').text


# 네이버 뉴스 크롤러 예제
def crawler_naver_test():
    # 검색할 키워드
    search_keyword = "LG U+"
    # 검색어를 URL 인코딩
    encoded_keyword = urllib.parse.quote(search_keyword)

    # 네이버 뉴스 검색 URL
    url = f"https://search.naver.com/search.naver?where=news&query={search_keyword}&sm=tab_opt&sort=0&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0"

    # 웹 페이지 요청
    response = requests.get(url)

    # 응답이 성공적이면 (상태 코드 200)
    if response.status_code == 200:
        # HTML 파싱
        soup = bs4(response.text, 'html.parser')

        # 뉴스 기사 링크 추출
        # 네이버 뉴스 검색 결과의 기사 링크는 'a' 태그의 'href' 속성에 포함되어 있음
        # 주의: 페이지 구조가 변경될 수 있으므로 실제 HTML 구조에 맞게 수정 필요
        articles = soup.find_all('a', href=True)

        for article in articles:
            href = article['href']
            # 뉴스 링크는 'https://news.naver.com/'으로 시작하는 경우가 많음
            # if "https://news.naver.com/" in href:
            print(href)
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")


# 구글 뉴스 크롤러 예제
def crawler_google_test():
    # 검색할 키워드
    search_keyword = "LG U+"

    # Selenium 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless 모드 (브라우저 UI를 표시하지 않음)

    # 웹 드라이버 설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # 구글 뉴스 검색 URL
    url = f"https://www.google.com/search?q={urllib.parse.quote(search_keyword)}&tbm=nws"

    # 페이지 열기
    driver.get(url)

    # 검색 결과의 링크 추출
    search_results = driver.find_elements('tag name', 'a')

    for result in search_results:
        href = result.get_attribute('href')
        if 'google.com' not in str(href):
            print(href)

    # 브라우저 닫기
    driver.quit()
