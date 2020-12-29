page project "/projects/" {
  _projects = python("Projects.objects.all()") ||
  foo = 123
}

model banner {
  name = str(100)

  admin {
    inline lala {
      type = stacked
      extra = 300
      fields = ["*", !"c"]
    }
    tab main {
      fields = ["*", !"c"]
    }
    tab other {
      fields = ["lala"]
    }
  }
}