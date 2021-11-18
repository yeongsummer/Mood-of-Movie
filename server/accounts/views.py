from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def signup(request):
    pass


def login(request):
    pass


def logout(request):
    pass


def delete(request):
    pass


def update(request, user_pk):
    pass


def password(request, user_pk):
    pass


def profile(request, user_name):
    pass