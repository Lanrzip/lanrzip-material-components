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
- `nClicks` (Real; optional): 按钮累计点击次数，用于监听按钮点击行为
默认值：`0`
- `variant` (a value equal to: 'text', 'outlined', 'contained', 'string'; optional): 组件样式
"""
function ''_muibutton(; kwargs...)
        available_props = Symbol[:children, :id, :nClicks, :variant]
        wild_props = Symbol[]
        return Component("''_muibutton", "MuiButton", "lanrzip_material_components", available_props, wild_props; kwargs...)
end

''_muibutton(children::Any; kwargs...) = ''_muibutton(;kwargs..., children = children)
''_muibutton(children_maker::Function; kwargs...) = ''_muibutton(children_maker(); kwargs...)

