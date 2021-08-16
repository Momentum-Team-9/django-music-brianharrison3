from django.shortcuts import render
from .models import Album



# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": Album})

# def show_contact(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     form = NoteForm()
#     return render(
#         request,
#         "contacts/show_contact.html",
#         {"contact": contact, "pk": pk, "form": form},
#     )

