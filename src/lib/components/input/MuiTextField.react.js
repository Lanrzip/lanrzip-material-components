import * as React from 'react';
import PropTypes from 'prop-types';
import TextField from '@mui/material/TextField';


const MuiTextField = (props) => {
    let {
        autoComplete,
        autoFocus,
        classes,
        color,
        defaultValue,
        disabled,
        error,
        FormHelperTextProps,
        fullWidth,
        helperText,
        id,
        InputLabelProps,
        inputProps,
        InputProps,
        inputRef,
        label,
        margin,
        maxRows,
        minRows,
        multiline,
        name,
        onChange,
        placeholder,
        required,
        rows,
        select,
        SelectProps,
        size,
        sx,
        type,
        value,
        variant,
        setProps
    } = props;

    const handleChange = (event) => {
        setProps({ value: event.target.value });
        if (onChange) {
            onChange(event);
        }
    };

    const renderElement = (
        <TextField
            autoComplete={autoComplete}
            autoFocus={autoFocus}
            classes={classes}
            color={color}
            defaultValue={defaultValue}
            disabled={disabled}
            error={error}
            FormHelperTextProps={FormHelperTextProps}
            fullWidth={fullWidth}
            helperText={helperText}
            id={id}
            InputLabelProps={InputLabelProps}
            inputProps={inputProps}
            InputProps={InputProps}
            inputRef={inputRef}
            label={label}
            margin={margin}
            maxRows={maxRows}
            minRows={minRows}
            multiline={multiline}
            name={name}
            onChange={handleChange}
            placeholder={placeholder}
            required={required}
            rows={rows}
            select={select}
            SelectProps={SelectProps}
            size={size}
            sx={sx}
            type={type}
            value={value}
            variant={variant}
        />
    );

    return renderElement;
}


MuiTextField.propTypes = {
    /**
     * 自动填充的类型
     */
    autoComplete: PropTypes.string,
    
    /**
     * 是否自动聚焦
     */
    autoFocus: PropTypes.bool,
    
    /**
     * 覆盖或扩展应用于组件的样式
     */
    classes: PropTypes.object,
    
    /**
     * 组件的颜色
     */
    color: PropTypes.oneOf(['primary', 'secondary', 'error', 'info', 'success', 'warning', 'string']),
    
    /**
     * 默认值
     */
    defaultValue: PropTypes.any,
    
    /**
     * 是否禁用组件
     */
    disabled: PropTypes.bool,
    
    /**
     * 是否显示错误状态
     */
    error: PropTypes.bool,
    
    /**
     * 应用于FormHelperText元素的属性
     */
    FormHelperTextProps: PropTypes.object,
    
    /**
     * 是否占满父容器的宽度
     */
    fullWidth: PropTypes.bool,
    
    /**
     * 帮助文本内容
     */
    helperText: PropTypes.node,
    
    /**
     * 输入元素的ID
     */
    id: PropTypes.string,
    
    /**
     * 应用于InputLabel元素的属性
     */
    InputLabelProps: PropTypes.object,
    
    /**
     * 应用于输入元素的属性
     */
    inputProps: PropTypes.object,
    
    /**
     * 应用于输入组件的属性
     */
    InputProps: PropTypes.object,
    
    /**
     * 传递给输入元素的ref
     */
    inputRef: PropTypes.oneOfType([
        PropTypes.func,
        PropTypes.shape({ current: PropTypes.any })
    ]),
    
    /**
     * 标签内容
     */
    label: PropTypes.node,
    
    /**
     * 垂直间距调整
     */
    margin: PropTypes.oneOf(['dense', 'none', 'normal']),
    
    /**
     * 多行时显示的最大行数
     */
    maxRows: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
    
    /**
     * 多行时显示的最小行数
     */
    minRows: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
    
    /**
     * 是否渲染为多行文本区域
     */
    multiline: PropTypes.bool,
    
    /**
     * 输入元素的名称
     */
    name: PropTypes.string,
    
    /**
     * 值改变时的回调函数
     */
    onChange: PropTypes.func,
    
    /**
     * 输入前的提示文本
     */
    placeholder: PropTypes.string,
    
    /**
     * 是否为必填项
     */
    required: PropTypes.bool,
    
    /**
     * 多行时显示的行数
     */
    rows: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
    
    /**
     * 是否渲染为选择框
     */
    select: PropTypes.bool,
    
    /**
     * 应用于选择框元素的属性
     */
    SelectProps: PropTypes.object,
    
    /**
     * 组件的尺寸
     */
    size: PropTypes.oneOf(['medium', 'small', 'string']),
    
    /**
     * 允许定义系统覆盖以及其他CSS样式的系统属性
     */
    sx: PropTypes.oneOfType([
        PropTypes.arrayOf(PropTypes.oneOfType([PropTypes.func, PropTypes.object, PropTypes.bool])),
        PropTypes.func,
        PropTypes.object
    ]),
    
    /**
     * 输入元素的类型
     */
    type: PropTypes.string,
    
    /**
     * 输入元素的值
     */
    value: PropTypes.any,
    
    /**
     * 组件的样式
     */
    variant: PropTypes.oneOf(['filled', 'outlined', 'standard']),
    
    /**
     * Dash分配的回调函数，用于报告属性更改，以便在回调中使用
     */
    setProps: PropTypes.func
};


MuiTextField.defaultProps = {
    autoFocus: false,
    color: 'primary',
    disabled: false,
    error: false,
    fullWidth: false,
    margin: 'none',
    multiline: false,
    required: false,
    select: false,
    size: 'medium',
    variant: 'outlined'
};

export default MuiTextField;