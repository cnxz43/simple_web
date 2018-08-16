# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
import urllib.request as url_req
import json


# log
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def select_post(request):
    ctx = {}
    # https://api.douban.com/v2/book/1220562 douban图书api
    api = 'https://api.douban.com/v2/book/'

    if request.POST:
        # 判断submit
        free_search = request.POST.get('search1', '')
        list_search = request.POST.get('search2', '')


        # submit1 通过输入内容，进行搜索
        if free_search:
            url = api + request.POST['q'] #+ request.POST['s2'] + request.POST['s3']
            try:
                # 正常获取api信息
                content = url_req.urlopen(url)
                data = json.loads(content.read())
                ctx['rlt'] = data['title']
            except:
                # 获取api信息失败
                if request.POST['q'] == "110":
                    ctx['rlt'] = "try success"
                else:
                    ctx['rlt'] = "book not found"
            logger.info("search mode 1, context: %s result: %s", str(request.POST['q']),ctx['rlt'])

        # submit2 通过列表选择搜索
        elif list_search:
            url = api + request.POST['s1'] #+ request.POST['s2'] + request.POST['s3']
            try:
                content = url_req.urlopen(url)
                data = json.loads(content.read())
                ctx['rlt'] = data['title']
            except:
                ctx['rlt'] = "book not found 2"
            logger.info("search mode 2, context: %s result: %s", str(request.POST['s1']), ctx['rlt'])

        else:
            ctx['rlt'] = "please input book id"
            logger.info("no search, context: %s result: %s", str(request.POST['q']), ctx['rlt'])

    return render(request, "indexselect.html", ctx)


from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def terminal_svr(request):

    # # 这里利用了django自身的登陆验证系统
    # if not request.user.is_authenticated():
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))
    #
    # # doSomething to terminal svr
    a = {}
    a["result"] = "post_success"
    # # return HttpResponse(json.dumps(a), content_type='application/json')
    return render(request, "ajax.html", a)


@csrf_exempt
def ajax_try(request):
    return render(request, "ajax2.html")
