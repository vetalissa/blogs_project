from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """
    Пользователь может создавать, редактировать или удалять свои собственные посты.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT':
            return False
        if request.method != 'GET':
            if request.method == 'DELETE':
                post = view.queryset.filter(id=view.kwargs['pk'])
                if post.exists():
                    return post.first().author == request.user
                else:
                    return False

            return obj['author'] == request.user.username

        return True

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return self.has_object_permission(request, view, request.data)
