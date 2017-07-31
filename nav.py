#-*- encoding:utf-8 -*-
'''
flask_nav来给页面增加导航条
'''
from flask_nav import Nav
from flask_nav.elements import *

nav = Nav()

nav.register_element('top',Navbar(u'四爷爱小屋',
                                  View(u'主页','home'),
                                  View(u'关于','about'),
                                  Subgroup(u'爱屋吉屋',
                                      View(u'爱记录','log'),
                                      Separator(),
                                      View(u'爱自拍','picture'),
                                  ),
))