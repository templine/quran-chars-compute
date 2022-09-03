from binascii import hexlify,unhexlify


def encodetext(utf8data):
    return hexlify(utf8data.encode())

def decodetext(encodedtext):
    return str(unhexlify(encodedtext).decode('utf-8'))

file = open('fullQuran.txt','r',encoding="utf-8").read()
rawbytes = encodetext(file)


def get_sowarnames():
    sora = encodetext('\nسُورَةُ ')
    sowar = rawbytes.split(sora)
    names = set()
    for i in sowar:
        raw = i.split(encodetext('\n'))
        name = raw[0]
        names.add(decodetext(name))
    return names


def sora_byname(name):
    try:
        results =rawbytes.split(encodetext(f'\nسُورَةُ {name}'))[1]
        results2 = results.split(encodetext('\nسُورَةُ '))[0]
        return str(decodetext(results2)).strip()
    except:
        return None

def countchars(utf8_text,chars_args=None):
    bytes_text = encodetext(utf8_text)
    default = ['ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'ل', 'م', 'ن','ه', 'و', 'ي']
    chars = None
    if chars_args:
        chars = chars_args
    else:
        chars = default
    result = []
    total = 0
    for char in chars:
        count = bytes_text.count(encodetext(char))
        result.append({char:count})
        total = total+count
    return {'result':result,'total':total}

def compute(args=None):
    all_sowar_names = get_sowarnames()
    calculs = []
    for sora_name in all_sowar_names:
        # print(sora_byname(sora_name))
        try:
            calcul = countchars(sora_byname(sora_name),args)
            calcul['name'] = sora_name
            calculs.append(calcul)
        except:
            pass
    return calculs

if __name__ == '__main__':
    datas = compute(['ا','ل','م'])
    newlist = sorted(datas, key=lambda d: d['total'],reverse=True) 
    with open('results.txt','w',encoding='utf-8') as f:
        for item in newlist:
            f.write(f'{str(item)}\n')
