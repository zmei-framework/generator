
@post and @get
###################

@post
===========

By default page do not allow post method. @post annotation make POST
method possible.

Then you can handle post method in page body code::

    [boo]
    @post {
        print('Post method happened!')
    }

It is also possible just mark page as "allow post", an have code that will run on
both get and post::

    [boo] {
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = NameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()

        data['form'] = form
    }

    @post


@get
=======

If you need to run a piece of code only on GET method::


    [boo]
    @get {
        print('Get method happened!')
    }
    @post {
        print('Post method happened!')
    }
