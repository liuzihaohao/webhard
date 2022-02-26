from gettext import ngettext
from django.contrib import admin
from sympy import re
from .models import messgaelist
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.translation import ngettext
# Register your models here.
class messgaelistAdmin(admin.ModelAdmin):
	list_display = ['id','file','allpeople','text','time']
	list_display_links = ['id']
	list_filter = ['time']
	search_fields = ['text','file','id']
	date_hierarchy = 'time'
	actions=["se_del"]
	def get_queryset(self,request):
		qs=super(messgaelistAdmin,self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(allpeople=request.user)
	@admin.action(description='安全删除所选的 文件列表')
	def se_del(self,request, queryset):
		aa=queryset.delete()[0]
		self.message_user(request,ngettext(
			"%d 个文件成功删除",
			"%d 个文件成功删除",
			aa,
		)%aa,messages.SUCCESS)

admin.site.register(messgaelist,messgaelistAdmin)

admin.site.site_title="云盘"
admin.site.site_header="云盘"

from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType

class LogEntryAdmin(admin.ModelAdmin):
	list_display = ['action_time','user','content_type','object_id','object_repr','action_flag','change_message']
admin.site.register(LogEntry,LogEntryAdmin)

class SessionAdmin(admin.ModelAdmin):
	list_display = ['session_key','session_data','expire_date']
admin.site.register(Session,SessionAdmin)

class ContentTypeAdmin(admin.ModelAdmin):
	list_display = ['app_label','model']
admin.site.register(ContentType,ContentTypeAdmin)