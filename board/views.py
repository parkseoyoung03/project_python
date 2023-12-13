from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Board index page.")


# 다음과 같이 수정
from .models import Board
from django.views import generic
from django.urls import reverse_lazy

#
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):
    all_boards = Board.objects.all().order_by("name") # 모든 데이터 조회, 내림차순(-표시) 조회
    paginator = Paginator(all_boards, 10)
    page = int(request.GET.get('page', 1))
    board_list = paginator.get_page(page)

    return render(request, 'board/board_paginated.html', {'title':'회원 리스트', 'board_list':board_list})

# board/list
# 메인 리스트

# def index2(request):
#     board_list = Board.objects.order_by('no') ## 조건
#     context = {'board_list': board_list}
#     return render(request, 'board/board_list.html', context)


# # 페이징 page
# class PaginatedBoardList(generic.ListView):
   
#    model = Board
#    template_name = 'board/board_paginated_list.html'
#    context_object_name = 'board_pagelist'
#    paginate_by = 10



# board/detail
# 눌렀을 때 결과값만 보여주는 것
# def detail(request, board_id):
#     board = Board.objects.get(id=board_id)
#     context = {'board': board}
#     return render(request, 'board/board_detail.html', context)

# board/create
# 등록
class create(generic.CreateView):
    model = Board
    fields = ['name', 'no', 'email', 'tel', 'birth']
    success_url = reverse_lazy('board:list')
    template_name_suffix = '_create'

# 수정
class UpdateBoard(generic.UpdateView):
    model = Board
    fields = ['name', 'no', 'email', 'tel', 'birth']
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse_lazy('board:list')
    

# 삭제delete
class DeleteBoard(generic.DeleteView):
    model = Board
    success_url = reverse_lazy('board:list')
    template_name = 'board/board_confirm_delete.html'

# 조회 check
# 수정, 삭제, 리스트 버튼이 있는 상세화면

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board': board}
    return render(request, 'board/board_check.html', context)


# 페이징 page
class PaginatedBoardList(generic.ListView):
   model = Board
   template_name = 'board/board_paginated_list.html'
   context_object_name = 'board_pagelist'
   paginate_by = 10

