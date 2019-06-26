from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request,'index.html')

def mostrar_pombos(request):
    return render(request, 'pombos.html')

def mostrar_rolezinho(request):
    roles = ['bailão','Shopping União','Quermesse Da paróquia de São João','Calçadão de Osasco','SESC']
    bairro = 'Rochdale'
    return render(request,'rolezinho.html',{'roles':roles,'bairro':bairro}
    )