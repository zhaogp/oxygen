import hashlib

from django.http import HttpResponse

from log import logger


def verify(request):
    """
    验证请求是否从微信服务器发出
    :param request:
    :return:
    """
    token = 'jcloud'
    timestamp, nonce = request.GET.get('timestamp'), request.GET.get('nonce')
    a_list = [token, timestamp, nonce]
    logger.info(a_list)
    if timestamp is None:
        logger.info('Can not get parameter timestamp')
        return HttpResponse('Timestamp is None', content_type='text/plain')

    a_list.sort()
    sorted_str = ''.join(i for i in a_list)
    local_signature = hashlib.sha1(sorted_str).hexdigest()
    logger.info('计算出来的 signature: %s', local_signature)
    remote_signature = request.GET.get('signature')
    logger.info('传过来的 signature: %s', remote_signature)
    if remote_signature == local_signature:
        echostr = request.GET.get('echostr')
        logger.info(echostr)
        return HttpResponse(echostr, content_type='text/plain')
