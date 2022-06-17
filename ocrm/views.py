from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Contact, Interaction, OwnedProduct, ContactForm, OwnedProductForm, Product, ProductForm

def index(request):
    return render(request, "ocrm/index.html")

class ContactView(generic.DetailView):
    model = Contact
    template_name = 'ocrm/contact_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['interactions'] = Interaction.objects.filter(contact=self.kwargs['pk'])
        context['owned_products'] = OwnedProduct.objects.filter(contact=self.kwargs['pk'])
        return context


class ContactListView(generic.ListView):
    template_name = 'ocrm/contact_list.html'
    context_object_name = 'contacts_list'

    def get_queryset(self):
        return Contact.objects.filter(type='Contact').order_by('id')

class LeadListView(generic.ListView):
    template_name = 'ocrm/lead_list.html'
    context_object_name = 'lead_list'

    def get_queryset(self):
        return Contact.objects.filter(type='Lead').order_by('id')


class LeadView(generic.DetailView):
    model = Contact
    template_name = 'ocrm/lead_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['interactions'] = Interaction.objects.filter(contact=self.kwargs['pk'])
        return context


def create_contact(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('ocrm:contacts'))
        else:
            form = ContactForm(initial={'type':'Contact'})
        return render(request, 'ocrm/create_contact.html', {'form': form})

def create_lead(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('ocrm:leads'))
        else:
            form = ContactForm(initial={'type':'Lead'})
        return render(request, 'ocrm/create_lead.html', {'form': form})

def convert_lead_to_contact(request, lead_id):
    contact = get_object_or_404(Contact, pk=lead_id)
    contact.type = 'Contact'
    contact.save()
    return HttpResponseRedirect(reverse('ocrm:contact_detail', args=[lead_id]))


def create_owned_product(request, contact_id):
        if request.method == 'POST':
            form = OwnedProductForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('ocrm:contact_detail', args=[contact_id]))
        else:
            form = OwnedProductForm(initial={'contact':contact_id})
        return render(request, 'ocrm/create_owned_product.html', {'form': form, 'contact_id':contact_id})


class ProductListView(generic.ListView):
    template_name = 'ocrm/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.order_by('id')


def edit_product(request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('ocrm:products'))
        else:
            form = ProductForm(instance=product)
        return render(request, 'ocrm/edit_product.html', {'form': form, 'product_id': product_id})



# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'ocrm/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'ocrm/results.html'
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'ocrm/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('ocrm:results', args=(question.id,)))