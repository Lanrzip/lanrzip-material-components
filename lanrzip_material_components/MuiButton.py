# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MuiButton(Component):
    """A MuiButton component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    组件型，按钮内嵌元素.

- id (string; optional):
    组件唯一id.

- classes (dict; optional):
    覆盖或扩展应用于组件的样式.

- color (a value equal to: 'inherit', 'primary', 'secondary', 'success', 'error', 'info', 'warning', 'string'; default 'primary'):
    按钮颜色.

- component (optional):
    按钮组件.

- debounceWait (number; default 200):
    防抖等待时间.

- disableElevation (boolean; default False):
    是否禁用按钮阴影.

- disableFocusRipple (boolean; default False):
    是否禁用按钮聚焦时的涟漪效果.

- disableRipple (boolean; default False):
    是否禁用按钮涟漪效果.

- disabled (boolean; default False):
    是否禁用按钮.

- endIcon (a list of or a singular dash component, string or number; optional):
    按钮尾部图标.

- fullWidth (boolean; default False):
    是否自动扩展按钮宽度.

- href (string; optional):
    按钮链接.

- key (string; optional):
    组件key.

- nClicks (number; default 0):
    按钮累计点击次数，用于监听按钮点击行为  默认值：`0`.

- size (a value equal to: 'small', 'medium', 'large', 'string'; default 'medium'):
    按钮大小.

- startIcon (a list of or a singular dash component, string or number; optional):
    按钮头部图标.

- variant (a value equal to: 'outlined', 'contained', 'text', 'string'; default 'text'):
    组件样式."""
    _children_props = ['endIcon', 'startIcon']
    _base_nodes = ['endIcon', 'startIcon', 'children']
    _namespace = 'lanrzip_material_components'
    _type = 'MuiButton'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, component=Component.UNDEFINED, disabled=Component.UNDEFINED, disableElevation=Component.UNDEFINED, disableFocusRipple=Component.UNDEFINED, disableRipple=Component.UNDEFINED, endIcon=Component.UNDEFINED, fullWidth=Component.UNDEFINED, href=Component.UNDEFINED, size=Component.UNDEFINED, startIcon=Component.UNDEFINED, variant=Component.UNDEFINED, nClicks=Component.UNDEFINED, debounceWait=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'classes', 'color', 'component', 'debounceWait', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'disabled', 'endIcon', 'fullWidth', 'href', 'key', 'nClicks', 'size', 'startIcon', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'classes', 'color', 'component', 'debounceWait', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'disabled', 'endIcon', 'fullWidth', 'href', 'key', 'nClicks', 'size', 'startIcon', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MuiButton, self).__init__(children=children, **args)
