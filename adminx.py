# 设置主题
import xadmin
from Log.models import Error_msg
from xadmin import views


class GlobalSetting(object):  # 全局设置
    site_title = '项目后台数据监控'  # 设置页眉和 HTML 标题。
    site_footer = '聚凡科技公司版权所有，违法必究。'  # 设置页脚
    menu_style = 'accordion'  # 设置左侧侧边栏显示方式。


xadmin.site.register(views.CommAdminView, GlobalSetting)  # 将GlobalSetting中的设置注册到CommAdminView中



class Error_msgAdmin(object):  # 注册BombboxInfoAdmin。注意，它继承的是object

    list_display = ['path','creat_time','count','last_send_time','state','solve_time']
    list_filter = ['creat_time','last_send_time','state','solve_time']

xadmin.site.register(Error_msg, Error_msgAdmin)  # 将管理器注册
