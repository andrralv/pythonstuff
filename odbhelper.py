def buildConnectionString(args):
	"""Build a connection string from dictionary parameters. Returns a string."""
	return ";".join(["%s=%s" % (k, v) for k, v in args.items()])

if __name__ == "__main__":
	myParams = {"server":"pilgrim", \
				"database":"master", \
				"uid":"sa", \
				"pwd":"secret" \
				}
	print buildConnectionString(myParams)
	
raw_input("\nPress the enter key to exit.")	


