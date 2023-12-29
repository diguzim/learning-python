# run pip install camelcase in order to use this lib

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

# run pip freeze > requirements.txt in order to create a requirements.txt file with all the libs installed in the current environment

# run pip install -r requirements.txt in order to install all the libs in the requirements.txt file