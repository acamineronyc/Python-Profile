import re

# PRINT LOG FILE WITH NAMES

filename = 'logs.log'
save_file = 'save.log'
with open(filename) as file_object:
    with open(save_file, 'a') as output:
        for line in file_object:
            r = re.search(r'(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}) - - \[(.*)\] \"(\w{3,6}.* \w{0,4}/\d\.\d)\" (\d+) (\d+) "(\S+)" ["](.*)["] ["](\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})', line)
            http_x_real_ip = r.groups()[0]
            print(http_x_real_ip)
            time_local = r.groups()[1]
            print(time_local)
            request = r.groups()[2]
            print(request)
            status = r.groups()[3]
            print(status)
            body_bytes_sent = r.groups()[4]
            print(body_bytes_sent)
            http_referer = r.groups()[5]
            print(http_referer)
            http_user_agent = r.groups()[6]
            print(http_user_agent)
            http_x_forwarded_for = r.groups()[7]
            print(http_x_forwarded_for)

            output.write(r.groups()[0])
