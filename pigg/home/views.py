from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .models import Post
from .models import Days
from django.views.generic import ListView,DetailView
from django.core.mail import EmailMessage

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.
def main_feed(request):
    days=Days.objects.all()

    return render(
        request,
        'home/main_feed.html',
        {'days': days}
    )


def history(request):
    return render(
        request,
        'home/history.html'
    )

def story(request):
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'home/story.html', {'postlist': postlist})

def style(request):
    days=Days.objects.all()

    return render(
        request,
        'home/style.html',
        {'days' : days}
    )

def menu(request):
    return render(
        request,
        'home/menu.html'
    )

def restaurant(request):
    return render(
        request,
        'home/restaurant.html'
    )

def franchise_story(request):
    return render(
        request,
        'home/story.html'
    )

def franchise(request):
    return render(
        request,
        'home/franchise.html'
    )

def review(request):
    return render(
        request,
        'home/review.html'
    )

def index(request):
    return render(request, 'home/blog.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'home/blog.html', {'postlist': postlist})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(
        request,
        'home/posting.html',
        {'post':post,}
    )

class PostList(ListView):
    model = Post
    template_name = 'blog/index2.html'
    orderinf = '-pk'

class PostDetail(DetailView):
    model = Post


def send_email(request):
    if request.method == 'POST':
        # 폼 필드 데이터 가져오기
        title = request.POST.get('title')
        name = request.POST.get('name')
        number = request.POST.get('number')
        place = request.POST.get('place')
        content = request.POST.get('content')

        # 필수 필드 확인
        if not title or not name or not number or not place or not content:
            return HttpResponseBadRequest("모든 필드를 입력해 주세요.")

        # 이메일 내용 구성
        email_content = {
            'title': title,
            'name': name,
            'number': number,
            'place': place,
            'content': content
        }

        msg_html = render_to_string('email_format.html', email_content)

        # 이메일 보내기
        msg = EmailMessage(
            subject=title,
            body=msg_html,
            from_email="djangoemailtester001@gmail.com",
            to=["recipient@example.com"],  # 여기에 실제 받는 사람 이메일 주소를 넣어야 합니다.
        )
        msg.content_subtype = 'html'
        msg.send()

        # 성공 후 리다이렉트
        return redirect(reverse('index'))

    # GET 요청 시 처리
    return HttpResponseBadRequest("잘못된 요청입니다.")