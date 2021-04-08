from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from login.models import User
from tag.models import Tag
from .models import Board
from .forms import BoardForm
from django.http import Http404



from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView



# Create your views here.


class BoardtDetail(DetailView):
    template_name = 'board_detail.html'
    queryset = Board.objects.all()
    context_object_name = 'board'

    def board_detail(request, pk):
        try:
            board = Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404('게시글을 찾을 수 없습니다')

        return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/login/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(email=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})
    
        

       
           

        # return super().form_valid(form)


class BoardList(ListView):
    model = Board
    template_name = 'board_list.html'
    context_object_name = 'boards'

    def board_list(request):
        all_boards = Board.objects.all().order_by('-id')
        page = int(request.GET.get('p', 1))
        paginator = Paginator(all_boards, 3)

        boards = paginator.get_page(page)
        return render(request, 'board_list.html', {'boards': boards})
