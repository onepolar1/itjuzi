#!/usr/bin/env python
# -*- coding: utf-8 -*-
from proxy import proxy

proxy = proxy()
PROXIES = proxy.get()
print "== 加载代理列表完成 =="