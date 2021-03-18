# -*- coding=UTF-8 -*-

name = input('请输入你的姓名:')
tel = input('请输入你的手机号:')
age = input('请输入你的年龄:')

if name == 'closer':
  print('='*20)
  print('你的姓名很有个性:%s'%name)
  print('你的手机号%s'%tel)
  print('你的年龄%s'%age)
  print('='*20)
else:
  print('='*20)
  print('你的名字很普通:%s'%name)
  print('你的手机号%s'%tel)
  print('你的年龄%s'%age)
  print('='*20)
      
if name == 'closer':
  print('='*20)
  print('你的名字也叫:%s'%name)
  print('='*20)
elif name == 'yourName':
  print('='*20)
  print('你仿佛在逗我笑%s'%name)
  print('='*20)
else:
  print('='*20)
  print('随便你叫啥')
  print('='*20)