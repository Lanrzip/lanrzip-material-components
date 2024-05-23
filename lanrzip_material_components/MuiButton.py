# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MuiButton(Component):
    """A MuiButton component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; default '按钮'):
    组件型，按钮内嵌元素.

- id (string; optional):
    组件唯一id.

- nClicks (number; default 0):
    按钮累计点击次数，用于监听按钮点击行为  默认值：`0`.

- variant (a value equal to: 'text', 'outlined', 'contained', 'string'; default 'contained'):
    组件样式."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'lanrzip_material_components'
    _type = 'MuiButton'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, variant=Component.UNDEFINED, nClicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'nClicks', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'nClicks', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MuiButton, self).__init__(children=children, **args)
