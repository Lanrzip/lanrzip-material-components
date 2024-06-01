# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MuiTextField(Component):
    """A MuiTextField component.


Keyword arguments:

- id (string; optional):
    输入元素的ID.

- FormHelperTextProps (dict; optional):
    应用于FormHelperText元素的属性.

- InputLabelProps (dict; optional):
    应用于InputLabel元素的属性.

- InputProps (dict; optional):
    应用于输入组件的属性.

- SelectProps (dict; optional):
    应用于选择框元素的属性.

- autoComplete (string; optional):
    自动填充的类型.

- autoFocus (boolean; default False):
    是否自动聚焦.

- classes (dict; optional):
    覆盖或扩展应用于组件的样式.

- color (a value equal to: 'primary', 'secondary', 'error', 'info', 'success', 'warning', 'string'; default 'primary'):
    组件的颜色.

- defaultValue (boolean | number | string | dict | list; optional):
    默认值.

- disabled (boolean; default False):
    是否禁用组件.

- error (boolean; default False):
    是否显示错误状态.

- fullWidth (boolean; default False):
    是否占满父容器的宽度.

- helperText (a list of or a singular dash component, string or number; optional):
    帮助文本内容.

- inputProps (dict; optional):
    应用于输入元素的属性.

- inputRef (dict; optional):
    传递给输入元素的ref.

    `inputRef` is a dict with keys:

    - current (boolean | number | string | dict | list; optional)

- label (a list of or a singular dash component, string or number; optional):
    标签内容.

- margin (a value equal to: 'dense', 'none', 'normal'; default 'none'):
    垂直间距调整.

- maxRows (number | string; optional):
    多行时显示的最大行数.

- minRows (number | string; optional):
    多行时显示的最小行数.

- multiline (boolean; default False):
    是否渲染为多行文本区域.

- name (string; optional):
    输入元素的名称.

- placeholder (string; optional):
    输入前的提示文本.

- required (boolean; default False):
    是否为必填项.

- rows (number | string; optional):
    多行时显示的行数.

- select (boolean; default False):
    是否渲染为选择框.

- size (a value equal to: 'medium', 'small', 'string'; default 'medium'):
    组件的尺寸.

- sx (list of dicts | boolean | dict; optional):
    允许定义系统覆盖以及其他CSS样式的系统属性.

- type (string; optional):
    输入元素的类型.

- value (boolean | number | string | dict | list; optional):
    输入元素的值.

- variant (a value equal to: 'filled', 'outlined', 'standard'; default 'outlined'):
    组件的样式."""
    _children_props = ['helperText', 'label']
    _base_nodes = ['helperText', 'label', 'children']
    _namespace = 'lanrzip_material_components'
    _type = 'MuiTextField'
    @_explicitize_args
    def __init__(self, autoComplete=Component.UNDEFINED, autoFocus=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, error=Component.UNDEFINED, FormHelperTextProps=Component.UNDEFINED, fullWidth=Component.UNDEFINED, helperText=Component.UNDEFINED, id=Component.UNDEFINED, InputLabelProps=Component.UNDEFINED, inputProps=Component.UNDEFINED, InputProps=Component.UNDEFINED, inputRef=Component.UNDEFINED, label=Component.UNDEFINED, margin=Component.UNDEFINED, maxRows=Component.UNDEFINED, minRows=Component.UNDEFINED, multiline=Component.UNDEFINED, name=Component.UNDEFINED, onChange=Component.UNDEFINED, placeholder=Component.UNDEFINED, required=Component.UNDEFINED, rows=Component.UNDEFINED, select=Component.UNDEFINED, SelectProps=Component.UNDEFINED, size=Component.UNDEFINED, sx=Component.UNDEFINED, type=Component.UNDEFINED, value=Component.UNDEFINED, variant=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'FormHelperTextProps', 'InputLabelProps', 'InputProps', 'SelectProps', 'autoComplete', 'autoFocus', 'classes', 'color', 'defaultValue', 'disabled', 'error', 'fullWidth', 'helperText', 'inputProps', 'inputRef', 'label', 'margin', 'maxRows', 'minRows', 'multiline', 'name', 'placeholder', 'required', 'rows', 'select', 'size', 'sx', 'type', 'value', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'FormHelperTextProps', 'InputLabelProps', 'InputProps', 'SelectProps', 'autoComplete', 'autoFocus', 'classes', 'color', 'defaultValue', 'disabled', 'error', 'fullWidth', 'helperText', 'inputProps', 'inputRef', 'label', 'margin', 'maxRows', 'minRows', 'multiline', 'name', 'placeholder', 'required', 'rows', 'select', 'size', 'sx', 'type', 'value', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MuiTextField, self).__init__(**args)
