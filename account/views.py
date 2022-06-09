from calendar import month
from django.shortcuts import render, redirect
from django.views.generic import TemplateView # テンプレートタグ
from .forms import AccountForm, AddAccountForm # ユーザーアカウントフォーム
from timeline.models import Event # イベントフォーム

# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#ログイン
def Login(request):
    # POST
    
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)


        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return render(request, 'account/login.html', context={"error_message": "アカウントが有効ではありません"})
        # ユーザー認証失敗
        else:
            return render(request, 'account/login.html', context={"error_message": "ログインIDまたはパスワードが間違っています"})
    # GET
    else:
        return render(request, 'account/login.html', )


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))



class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"account/register.html",context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # モデル保存
            add_account.save()

            Event.objects.create(
                user_id = add_account,
                name = "新規登録",
                detail = "最初のイベント",
            )

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

            # フォーム入力のユーザーID・パスワード取得
            ID = request.POST.get('username')
            Pass = request.POST.get('password')

            # Djangoの認証機能
            user = authenticate(username=ID, password=Pass)


            # ユーザー認証
            if user:
                #ユーザーアクティベート判定
                if user.is_active:
                    # ログイン
                    login(request,user)
                    # ホームページ遷移
                    return redirect('home')
            # GET
            else:
                return redirect('Login')

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)
            return render(request,"account/register.html",context=self.params)
