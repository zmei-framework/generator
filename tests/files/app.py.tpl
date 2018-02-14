from cratis import *
from cratis_common.base import Common
from {name}.features import {class_name}

app = App()
app.load(
    Common(),
    {class_name}()
)
app.run(locals())
