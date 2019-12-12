import re
import pathlib
test_file = pathlib.Path('Test.de').read_text()
test_str_re = re.sub('[\[\]]', '', test_file)
test_match_list = []
for match in re.finditer('\{(.*?)\}', test_str_re):
    test_match_text = '{'+"{group}".format(
        group=match.group(1), begin=match.start(),
        end=match.end())+'}'
    test_match_list.append(re.sub('[\{\}]', '', test_match_text))
for i in range(len(test_match_list)):
    print(i, test_match_list[i])


