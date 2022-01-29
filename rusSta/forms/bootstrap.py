# 给每一行添加的标签，样式
class BootStrapForm(object):
    def __init__(self, *args, **kwargs):  # 给每个字段都加上form-control属性
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)
