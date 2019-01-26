from django.shortcuts import render
from collections import Counter

# Create your views here.
def home(request):
    return render(request,'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']
    words = full_text.split()
    counts = list(sorted(Counter(words).items(), key= lambda x:x[1], reverse=True))
    return render(request, 'wordcount/count.html',{'fulltext': full_text, 'words': words, 'result': counts})

# ### 값을 넘겨줄때 결과 값을 넘겨 줘야함,
# full_text = """아무도 가르쳐 주지 않아 이 길이 옳은지 다른 길로 가야 할지 난 저길 저 끝에 다 다르면 멈추겠지 끝이라며 가로막힌 미로 앞에 서 있어 내 길을 물어도 대답 없는 메아리 어제와 똑같은 이 길에 머물지 몰라 저 거미줄 끝에 꼭 매달린 것처럼 세상 어딘가 저 길 가장 구석에 갈 길을 잃은 나를 찾아야만 해 저 해를 삼킨 어둠이 오기 전에 긴 벽에 갇힌 나의 길을 찾아야만 하겠지 가르쳐줘 내 가려진 두려움 이 길이 끝나면 다른 길이 있는지 두 발에 뒤엉킨 이 매듭 끝을 풀기엔 내 무뎌진 손이 더 아프게 조여와 세상 어딘가 저 길 가장 구석에 갈 길을 잃은 나를 찾아야만 해 저 해를 삼킨 어둠이 오기 전에 긴 벽에 갇힌 나의 길을 찾아야만 하겠지 아무도 가르쳐 주지 않아 이 길이 옳은지 다른 길로 가야 할지 난 저길 저 끝에 다 다르면 멈추겠지 끝이라며 가로막힌 미로 앞에 서 있어 내 길을 물어도 대답 없는 메아리 어제와 똑같은 이 길에 머물지 몰라 저 거미줄 끝에 꼭 매달린 것처럼 세상 어딘가 저 길 가장 구석에 갈 길을 잃은 나를 찾아야만 해 저 해를 삼킨 어둠이 오기 전에 긴 벽에 갇힌 나의 길을 찾아야만 하겠지 가르쳐줘 내 가려진 두려움 이 길이 끝나면 다른 길이 있는지 두 발에 뒤엉킨 이 매듭 끝을 풀기엔 내 무뎌진 손이 더 아프게 조여와 세상 어딘가 저 길 가장 구석에 갈 길을 잃은 나를 찾아야만 해 저 해를 삼킨 어둠이 오기 전에 긴 벽에 갇힌 나의 길을 찾아야만 하겠지"""
#
# words = full_text.split()
# for k,v in Counter(words).items():
#     print(k,v)
