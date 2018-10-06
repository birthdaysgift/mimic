from django.urls import path

from .views import EditView, PageView, SendFriendRequestView, \
    AcceptFriendRequestView, DenyFriendRequestView, RemoveFriendView, \
    ResetFriendRequestView, FriendsListView

app_name = "pages"

urlpatterns = [
    path("<str:username>/", PageView.as_view(), name="page"),
    path("<str:username>/edit/", EditView.as_view(), name="edit"),
    path("<str:username>/send_friend_request/", SendFriendRequestView.as_view(),
         name="send_friend_request"),
    path("<str:username>/reset_friend_request/",
         ResetFriendRequestView.as_view(), name="reset_friend_request"),
    path("<str:username>/accept_friend_request/",
         AcceptFriendRequestView.as_view(), name="accept_friend_request"),
    path("<str:username>/deny_friend_request/", DenyFriendRequestView.as_view(),
         name="deny_friend_request"),
    path("<str:username>/remove_friend/", RemoveFriendView.as_view(),
         name="remove_friend"),
    path("<str:username>/friends/", FriendsListView.as_view(),
         name="friends")
]
