from django.shortcuts import render
from .models import Usuario

#request serve para acessar os arquivos da pagina
# render serve para renderizar/criar uma pagina, ela precisa dos dados, entao chame request e depois uma pagina html responsavel por exibir esses dados
def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('Nome')
    novo_usuario.idade = request.POST.get('Idade')
    novo_usuario.save()
    # Exibir todos os usuarios ja cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)
