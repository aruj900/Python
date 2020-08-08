from html import escape

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return '{0}(<i>{1}</i>'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a,2))

def html_str(s):
    return html_escape(s).replace('\n','<br/>\n')

def html_list(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l
            )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(html_escape(k),htmlize(v))
            for k,v in d.items())
    return '<ul>\n' +'\n'.join(items) + '\n</ul>'


print(html_str("""this is a multi line string with special characters: 10 < 100"""))

print(html_int(255))

print(html_escape(1+5j))

from decimal import Decimal

def htmlize(arg):
    if isinstance(arg,int):
        return html_int(arg)
    elif isinstance(arg,float) or isinstance(arg,Decimal):
        return html_real(arg)
    elif isinstance(arg,str):
        return html_str(arg)
    elif isinstance(arg,list) or isinstance(arg,tuple):
        return html_list(arg)
    elif isinstance(arg,dict):
        return html_dict(arg)
    else:
        return html_escape(arg)

print(htmlize(100))

print(htmlize(["""python
               rocks!""",(10,20,30),100,{1:2}]))


def htmlize1(arg):
    registry ={
        object: html_escape,
        int: html_int,
        float: html_real,
        Decimal: html_real,
        str: html_str,
        list: html_list,
        tuple: html_list,
        set: html_set,
        dict: html_dict
    }
    
    fn = registry.get(type(arg), registry[object])
    
    return fn(arg)

def singleddispatch(fn):
    
    registry = {}
    
    registry[object] = fn
    registry[int] = lambda a: '{0}(<i>{1}</i>'.format(a, str(hex(a)))
    registry[str] = lambda s: escape(s).replace('\n','<br/>\n')
    
    def inner(arg):
        return registry.get(type(arg), registry[object])(arg)
        
    return inner

@singleddispatch
def htmlize(a):
    return escape(str(a))

print(htmlize('1 < 100'))
print(htmlize(100))


def singleddispatch(fn):
    
    registry = {}
    
    registry[object] = fn
    
    
    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner
    
    def dispatch(type_):
        registry.get(type_, registry[object])
    
    decorated.register = register
    decorated.dispatch = dispatch
    return decorated

@singleddispatch
def htmlize(a):
    return escape(str(a))

print(htmlize('1 < 100'))

@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i>'.format(a, str(hex(a)))

print(htmlize(100))

@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l
            )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(htmlize([1,2,3]))
    
print(htmlize.dispatch(int))

print(htmlize(100))

from numbers import Integral 

@singleddispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def html_integral_number(a):
    return '{0}(<i>{1}</i>'.format(a, str(hex(a)))


from functools import singledispatch

from numbers import Integral
from collections.abc import Sequence 

@singledispatch
def htmlize(a):
    return esscape(str(a))

print(htmlize.registry)

@htmlize.register(Integral)
def html_integral_number(a):
    return '{0}(<i>{1}</i>'.format(a, str(hex(a)))
 

print(htmlize.dispatch(int))

