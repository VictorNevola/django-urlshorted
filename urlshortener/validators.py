import validators

def URLValidator(url):
  urlIsValid = url != '' and True
  urlIsValid = validators.url(url)

  return urlIsValid and urlIsValid or False
