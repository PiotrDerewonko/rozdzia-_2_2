from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, DetailView
from .models import Book, Borrow, Author
from django.views import View
from .forms import BorrowForm
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pobierz wszystkie książki tego autora
        author = self.get_object()
        books = Book.objects.filter(author=author)
        context['books'] = books
        return context


class BookDetailView(View):

    def get(self, request, *args, **kwargs):
        my_param = kwargs.get('my_param')
        book = Book.objects.get(id=my_param)
        cond_1 = {'user__borrow__book_id': my_param}
        cond_2 = {'user__borrow__is_returned': False}
        is_borrow = Borrow.objects.filter(**cond_1, **cond_2)
        if is_borrow.exists():
            is_borrow = True
        else:
            is_borrow = False
        user = request.user.id
        form = BorrowForm(initial={'book': my_param, 'user': user})
        return render(request=request, template_name='book_detail.html', context={
            'form': form, 'book': book, 'is_borrow': is_borrow
        })

    def post(self, request, *args, **kwargs):
        form = BorrowForm(request.POST)
        my_param = kwargs.get('my_param')
        book = Book.objects.get(id=my_param)

        form.save()
        return render(request, 'book_detail.html', {'book': book, 'form': form})


@method_decorator(login_required, name='dispatch')
class UserBorrowList(ListView):
    model = Borrow
    template_name = 'user_borrow_list.html'
    paginate_by = 5

    def post(self, request, *args, **kwargs):
        borrow_id = request.POST.get('borrow_id')
        user_id = self.kwargs.get('user_id')
        Borrow.objects.filter(pk=borrow_id).update(is_returned=True, return_date=now())
        return redirect('books:user_borow_list', user_id=user_id)

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Borrow.objects.filter(user_id=user_id, is_returned=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
