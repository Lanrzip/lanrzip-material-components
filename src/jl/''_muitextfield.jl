# AUTO GENERATED FILE - DO NOT EDIT

export ''_muitextfield

"""
    ''_muitextfield(;kwargs...)

A MuiTextField component.

Keyword arguments:
- `id` (String; optional): 输入元素的ID
- `FormHelperTextProps` (Dict; optional): 应用于FormHelperText元素的属性
- `InputLabelProps` (Dict; optional): 应用于InputLabel元素的属性
- `InputProps` (Dict; optional): 应用于输入组件的属性
- `SelectProps` (Dict; optional): 应用于选择框元素的属性
- `autoComplete` (String; optional): 自动填充的类型
- `autoFocus` (Bool; optional): 是否自动聚焦
- `classes` (Dict; optional): 覆盖或扩展应用于组件的样式
- `color` (a value equal to: 'primary', 'secondary', 'error', 'info', 'success', 'warning', 'string'; optional): 组件的颜色
- `defaultValue` (Bool | Real | String | Dict | Array; optional): 默认值
- `disabled` (Bool; optional): 是否禁用组件
- `error` (Bool; optional): 是否显示错误状态
- `fullWidth` (Bool; optional): 是否占满父容器的宽度
- `helperText` (a list of or a singular dash component, string or number; optional): 帮助文本内容
- `inputProps` (Dict; optional): 应用于输入元素的属性
- `inputRef` (optional): 传递给输入元素的ref. inputRef has the following type: lists containing elements 'current'.
Those elements have the following types:
  - `current` (Bool | Real | String | Dict | Array; optional)
- `label` (a list of or a singular dash component, string or number; optional): 标签内容
- `margin` (a value equal to: 'dense', 'none', 'normal'; optional): 垂直间距调整
- `maxRows` (Real | String; optional): 多行时显示的最大行数
- `minRows` (Real | String; optional): 多行时显示的最小行数
- `multiline` (Bool; optional): 是否渲染为多行文本区域
- `name` (String; optional): 输入元素的名称
- `placeholder` (String; optional): 输入前的提示文本
- `required` (Bool; optional): 是否为必填项
- `rows` (Real | String; optional): 多行时显示的行数
- `select` (Bool; optional): 是否渲染为选择框
- `size` (a value equal to: 'medium', 'small', 'string'; optional): 组件的尺寸
- `sx` (Array of Dict | Bools | Dict; optional): 允许定义系统覆盖以及其他CSS样式的系统属性
- `type` (String; optional): 输入元素的类型
- `value` (Bool | Real | String | Dict | Array; optional): 输入元素的值
- `variant` (a value equal to: 'filled', 'outlined', 'standard'; optional): 组件的样式
"""
function ''_muitextfield(; kwargs...)
        available_props = Symbol[:id, :FormHelperTextProps, :InputLabelProps, :InputProps, :SelectProps, :autoComplete, :autoFocus, :classes, :color, :defaultValue, :disabled, :error, :fullWidth, :helperText, :inputProps, :inputRef, :label, :margin, :maxRows, :minRows, :multiline, :name, :placeholder, :required, :rows, :select, :size, :sx, :type, :value, :variant]
        wild_props = Symbol[]
        return Component("''_muitextfield", "MuiTextField", "lanrzip_material_components", available_props, wild_props; kwargs...)
end

