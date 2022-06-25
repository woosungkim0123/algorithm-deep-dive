import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r"[^a-zA-Z0-9-_.]", "", new_id)
    new_id = re.sub('(([.])\\2{1,})', ".", new_id)
    new_id = new_id.strip('.')
    if new_id == '':
        new_id += 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')

    if len(new_id) <= 2:
        idSize = len(new_id)
        addchar = new_id[idSize - 1]
        while len(new_id) < 3:
            new_id += addchar
    return new_id


solution("...!@BaT#*..y.abcdefghijklm")


# 다른사람풀이


def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + \
        "".join([st[-1] for i in range(3-len(st))])
    return st
