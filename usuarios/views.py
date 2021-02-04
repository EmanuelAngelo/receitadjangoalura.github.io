from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from receitas.models import Receita

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('o campo nome nao pode  ficar em branco')
            return redirect ('cadastro')
        if not email.strip():
            print('o campo email nao pode  ficar em branco')
            return redirect ('cadastro')
        if senha != senha2:
            print ('as senhas nao sao iguais')
            return redirect ('cadastro')
        if User.objects.filter(email=email).exists():
            print ('usuario ja existe')
            return redirect ('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('usuario cadastro')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            print('os campos email e senha nao podem ficar em branco')
            return redirect ('login')
        if User.objects.filter(email=email).exists(): #camparando se email existe no banco de dados
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect ('dashboard')
    return render(request,'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated: #saber se usuario esta logado
        id = request.user.id
        receitas = Receita.objects.order.by ('-date_receita').filter(pessoa=id)
        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def cria_receita(request):
    if request.method == 'POST': #trazendo os dados do cria receita
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id) #tras o id do usuario na requisição e atribui a variavel user
        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, #inviando dados para banco de dados
        ingredientes=ingredientes, modo_preparo=modo_preparo, tempo_preparo=tempo_preparo,
        rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)
        receita.save() #salvando dados no banco de dados
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')