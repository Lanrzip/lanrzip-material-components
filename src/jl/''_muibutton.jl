# AUTO GENERATED FILE - DO NOT EDIT

export ''_muibutton

"""
    ''_muibutton(;kwargs...)
    ''_muibutton(children::Any;kwargs...)
    ''_muibutton(children_maker::Function;kwargs...)


A MuiButton component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): 组件型，按钮内嵌元素
- `id` (String; optional): 组件唯一id
- `classes` (Dict; optional): 覆盖或扩展应用于组件的样式
- `color` (a value equal to: 'inherit', 'primary', 'secondary', 'success', 'error', 'info', 'warning', 'string'; optional): 按钮颜色
- `component` (optional): 按钮组件
- `debounceWait` (Real; optional): 防抖等待时间
- `disableElevation` (Bool; optional): 是否禁用按钮阴影
- `disableFocusRipple` (Bool; optional): 是否禁用按钮聚焦时的涟漪效果
- `disableRipple` (Bool; optional): 是否禁用按钮涟漪效果
- `disabled` (Bool; optional): 是否禁用按钮
- `endIcon` (a list of or a singular dash component, string or number; optional): 按钮尾部图标
- `fullWidth` (Bool; optional): 是否自动扩展按钮宽度
- `href` (String; optional): 按钮链接
- `key` (String; optional): 组件key
- `nClicks` (Real; optional): 按钮累计点击次数，用于监听按钮点击行为
默认值：`0`
- `size` (a value equal to: 'small', 'medium', 'large', 'string'; optional): 按钮大小
- `startIcon` (a list of or a singular dash component, string or number; optional): 按钮头部图标
- `variant` (a value equal to: 'outlined', 'contained', 'text', 'string'; optional): 组件样式
"""
function ''_muibutton(; kwargs...)
        available_props = Symbol[:children, :id, :classes, :color, :component, :debounceWait, :disableElevation, :disableFocusRipple, :disableRipple, :disabled, :endIcon, :fullWidth, :href, :key, :nClicks, :size, :startIcon, :variant]
        wild_props = Symbol[]
        return Component("''_muibutton", "MuiButton", "lanrzip_material_components", available_props, wild_props; kwargs...)
end

''_muibutton(children::Any; kwargs...) = ''_muibutton(;kwargs..., children = children)
''_muibutton(children_maker::Function; kwargs...) = ''_muibutton(children_maker(); kwargs...)

