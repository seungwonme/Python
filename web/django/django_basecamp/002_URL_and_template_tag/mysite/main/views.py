from django.shortcuts import render
from django.http import HttpResponse

blog_list_db = [
    {
        "id": 1,
        "title": "장고는 너무 재미있어!!!",
        "content": "This is the content of blog 1",
        "author": "Author 1",
    },
    {
        "id": 2,
        "title": "파이썬도 너무 재미있어!!!!",
        "content": "This is the content of blog 2",
        "author": "Author 2",
    },
    {
        "id": 3,
        "title": "자바스크립트는 별로였어!!!",
        "content": "This is the content of blog 3",
        "author": "Author 3",
    },
]

user_list_db = [
    {
        "id": 1,
        "username": "seunan",
        "email": "seunan@gmail.com",
        "password": "1234",
    },
    {
        "id": 2,
        "username": "jihun",
        "email": "jihun@gmail.com",
        "password": "1234",
    },
    {
        "id": 3,
        "username": "junho",
        "email": "junho@gmail.com",
        "password": "1234",
    },
]

mock_data = [
    {
        "_id": "e57a00c9-87b0-4f17-C781-340a17eaebd2",
        "index": "1",
        "name": "엄태규",
        "email": "user-44yf3kg@blandit.net",
        "phone": "010-6668-3556",
        "country": "바베이도스",
        "address": "여의대방로 87-4",
        "job": "기계공학 기술자ㆍ연구원",
        "age": "40"
    },
    {
        "_id": "5b95d56f-3d33-43b9-B3bb-391f4b08875a",
        "index": "2",
        "name": "라재윤",
        "email": "user-yz9qcic@Molestie.co.kr",
        "phone": "010-8447-0746",
        "country": "지브롤터",
        "address": "노량진로 53-1",
        "job": "프로게이머",
        "age": "25"
    },
    {
        "_id": "51858a30-b8ff-433e-C61f-903aac588993",
        "index": "3",
        "name": "명태우",
        "email": "user-0nd4d80@cursus.io",
        "phone": "010-3961-7120",
        "country": "콜롬비아",
        "address": "잠실로 38-5",
        "job": "판사",
        "age": "60"
    },
    {
        "_id": "e7a7e0b1-cb0c-4e89-A15c-2d8c1a8e3db1",
        "index": "4",
        "name": "가원준",
        "email": "user-72pdi31@quia.org",
        "phone": "010-9592-8486",
        "country": "폴란드",
        "address": "홍익로 44-1",
        "job": "신약개발연구원",
        "age": "36"
    },
    {
        "_id": "c876871d-d2eb-4dbd-Ab35-ab055b944cb4",
        "index": "5",
        "name": "피\n종\n혁\n",
        "email": "user-5nels27@at.net",
        "phone": "010-9930-8128",
        "country": "바하마",
        "address": "공덕로 85-7",
        "job": "물리학연구원",
        "age": "30"
    },
    {
        "_id": "a65ca03c-c79d-4968-C69a-ba39d317973b",
        "index": "6",
        "name": "국채윤",
        "email": "user-pktjqt6@leo.co.kr",
        "phone": "010-9067-8857",
        "country": "칠레",
        "address": "여의대방로 16-2",
        "job": "자연계중등학교교사",
        "age": "34"
    },
]


def index(request):
    context = {
        "mock_data": mock_data,
    }
    return render(request, "main/index.html", context)


def blog_list(request):
    context = {
        "blog_list": blog_list_db,
    }
    return render(request, "main/blog_list.html", context)


# s = f'hello world' # 개행이 안되고
# ss = f'''hello world''' #개행이 됩니다.


def blog_details(request, pk):
    blog = blog_list_db[pk - 1]
    languages = ["python", "java", "javascript"]
    context = {
        "blog": blog,
        "languages": languages,
    }
    return render(request, "main/blog_details.html", context)


def accounts_details(request, username):
    # all(filter(user_list_db, lambda x: x['username'] == user))
    finduser = None
    for user in user_list_db:
        if user["username"] == username:
            finduser = user
            break
    if finduser is None:
        return HttpResponse("User not found")
    context = {
        "user": finduser,
    }
    return render(request, "main/accounts_details.html", context)
