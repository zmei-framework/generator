Crud
##############

Syntax::

    [dashboard_tokens: $/dashboard/tokens]
    @crud {
        rest_framework.authtoken.Token(user=request.user)
    }


Full example with nested cruds::

    [base]
    @menu.left {
        index => "Home": page(index)
        docs => "Documentation": url('/docs/generator/index.html')
    }
    @menu.right {
        dashboard => Dashboard: page(dashboard)
    }

    [base->index: $/]

    [base->dashboard: $/dashboard]
    @menu.dashboard {
        index => "Home": page(dashboard)
        tokens => "Tokens": page(dashboard_tokens)
        projects => "Projects": page(projects)
        /*email => "Email settings": reverse('account_email')*/
    }


    [dashboard->dashboard_tokens: $/dashboard/tokens]
    @crud {
        #token<user=request.user>
        fields: name
        skip: update
        block: tab_content
    }

    [dashboard->projects: $/dashboard/projects]
    @crud {
        #project<user=request.user>
        fields: *, ^user, ^created
        block: tab_content
    }


    [projects->projects_detail: $/dashboard/projects/<pk>/]
    item: Project.objects.get(user=request.user, pk=url.pk) @or_404
    @merge
    @crud.history {
        #history_item<user=request.user, project=Project.objects.get(pk=url.pk)>
        fields: source
        block: tab_content
        link_extra: "pk=url.pk"
    }

    #token
    ----------
    name
    user: one(cratis_profile.User)

    @mixin(rest_framework.authtoken.models.Token)

    #project
    ----------
    created: create_time
    user: one(cratis_profile.User)
    =name

    #history_item
    ----------
    ="{me.project} -> {me.created:%d.%m.%Y}: #{me.id}"

    created: create_time
    user: one(cratis_profile.User)
    project: one(#project -> history)
    source: longtext

