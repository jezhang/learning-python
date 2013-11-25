
import datetime

print 'module functions loaded.'

def get_bj_time():    
    return datetime.datetime.utcnow() + datetime.timedelta(hours=+8)

def sid():
    now=get_bj_time()
    return now.strftime('%Y%m%d%H%M%S')+str(now)

def current_datetime_str():
	return datetime.datetime.now().strftime('%Y%m%d%H%M%S')




