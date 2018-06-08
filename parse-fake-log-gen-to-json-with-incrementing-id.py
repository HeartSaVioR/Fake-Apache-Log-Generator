import sys
import apache_log_parser
import json
import time
from dateutil.parser import parse

auto_incr_id = 1
parser_format = '%a - - %t %D "%r" %s %b "%{Referer}i" "%{User-Agent}i"'
line_parser = apache_log_parser.make_parser(parser_format)
while True:
  line = sys.stdin.readline()
  if not line:
    break
  parsed_dict = line_parser(line)
  parsed_dict['id'] = auto_incr_id
  auto_incr_id += 1

  # works only python 2, but I don't care cause it's just a test module :)
  parsed_dict = {k.upper(): v for k, v in parsed_dict.iteritems() if not k.endswith('datetimeobj')}
  parsed_dict['TIME_RECEIVED_TIMESTAMP'] = int(time.mktime(parse(parsed_dict['TIME_RECEIVED_UTC_ISOFORMAT']).timetuple()))
  print json.dumps(parsed_dict)
