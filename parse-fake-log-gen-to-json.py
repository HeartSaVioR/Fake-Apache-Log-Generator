import sys
import apache_log_parser
import json

parser_format = '%a - - %t %D "%r" %s %b "%{Referer}i" "%{User-Agent}i"'
line_parser = apache_log_parser.make_parser(parser_format)
while True:
  line = sys.stdin.readline()
  if not line:
    break
  parsed_dict = line_parser(line)

  # works only python 2, but I don't care cause it's just a test module :)
  parsed_dict = {k: v for k, v in parsed_dict.iteritems() if not k.endswith('datetimeobj')}
  print json.dumps(parsed_dict)
