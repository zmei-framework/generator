
@auth
###################

With @auth you can restrict access to page as "for logged in users only"::

    [members: /member_area/]
    boo:= 321

    @auth

Also, you can check privileges by passing a python expression as an argument::

    [project_admin: /project/<pk>/admin/]
    project: Project.objects.get(pk=url.pk) @or_404
    is_admin: project.owner.pk == request.user.pk

    @auth{ data.is_admin }

