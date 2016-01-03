## opihelper
# returns a list of an objects methods doc strings
# 01/03/16

def info(object, spacing = 10, collapse = 1):
	"""Prints methods doc strings
	Takes module, class, list, dictionary or string."""
	methodList = [method for method in dir(object) if callable(getattr(object, method))]
	processFunct = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
	print "\n".join(["%s %s" % (method.ljust(spacing), processFunct(str(getattr(object, method).__doc__))) for method in methodList])

if __name__ == '__main__':
	print info.__doc__	