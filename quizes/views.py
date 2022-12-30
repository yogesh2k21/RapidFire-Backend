from django.shortcuts import render,redirect
from room.models import Quiz,Room,Score

# Create your views here.
def quiz_dashboard(request):
    try:        
        quizes=Quiz.objects.filter(host=request.user).order_by('-datetime')
        print(quizes)
        return render(request,'dashboard.html',{"quizes":quizes})
    except Exception as e:
        print(e)
        return redirect('home')

def quiz_detail(request,id):
    try: 
        quiz=Quiz.objects.get(id=id,host=request.user)
        print(quiz.room)
        scores=Score.objects.filter(room=quiz.room).order_by('-point')
        print(scores)
        return render(request,'quiz_detail.html',{"scores":scores})
    except Exception as e:
        print(e)
        return redirect('home')