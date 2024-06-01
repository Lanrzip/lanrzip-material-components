import * as React from 'react';
import PropTypes from 'prop-types';
import Button from '@mui/material/Button';
import { useRequest } from 'ahooks';


const MuiButton = (props) => {
    let {
        id,
        key,
        children,
        classes,
        color,
        component,
        disabled,
        disableElevation,
        disableFocusRipple,
        disableRipple,
        endIcon,
        fullWidth,
        href,
        size,
        startIcon,
        // sx,
        variant,
        nClicks,
        debounceWait,
        setProps
    } = props;

    const { run: onClick} = useRequest(
        () => setProps({nClicks: nClicks + 1}),
        {
            debounceWait: debounceWait,
            debounceLeading: true,
            manual: true
        }
    )


    const renderElement = (
        <Button
            id={id}
            key={key}
            classes={classes}
            color={color}
            component={component}
            disabled={disabled}
            disableElevation={disableElevation}
            disableFocusRipple={disableFocusRipple}
            disableRipple={disableRipple}
            endIcon={endIcon}
            fullWidth={fullWidth}
            href={href}
            size={size}
            startIcon={startIcon}
            // sx={sx}
            variant={variant}
            onClick={onClick}
        >
            {children}
        </Button>
    );

  return renderElement;
}

MuiButton.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 组件key
     */
    key: PropTypes.string,

    /**
     * 组件型，按钮内嵌元素
      */
    children: PropTypes.node,

    /**
     * 覆盖或扩展应用于组件的样式
     */
    classes: PropTypes.object, 

    /**
     * 按钮颜色
     */
    color: PropTypes.oneOf(['inherit', 'primary', 'secondary', 'success', 'error', 'info', 'warning', 'string']),

    /**
     * 按钮组件
     */
    component: PropTypes.elementType,
    
    /**
         * 是否禁用按钮
         */
    disabled: PropTypes.bool,

    /**
     * 是否禁用按钮阴影
     */
    disableElevation: PropTypes.bool,

    /**
     * 是否禁用按钮聚焦时的涟漪效果
     */
    disableFocusRipple: PropTypes.bool,

    /**
     * 是否禁用按钮涟漪效果
     */
    disableRipple: PropTypes.bool,

    /**
     * 按钮尾部图标
     */
    endIcon: PropTypes.node,

    /**
     * 是否自动扩展按钮宽度
     */
    fullWidth: PropTypes.bool,

    /**
     * 按钮链接
     */
    href: PropTypes.string,

    /**
     * 按钮大小
     */
    size: PropTypes.oneOf(['small', 'medium', 'large', 'string']),

    /**
     * 按钮头部图标
     */
    startIcon: PropTypes.node,

    /**
     * 允许定义系统覆盖以及其他CSS样式的系统属性。
     */
    // sx: PropTypes.oneOf(
    //     [
    //         PropTypes.array([PropTypes.func, PropTypes.object, PropTypes.bool]),
    //         PropTypes.func,
    //         PropTypes.object,
    //     ]
    // ),

    /**
     * 组件样式
      */
    variant: PropTypes.oneOf(['outlined', 'contained', 'text', 'string']),

    /**
     * 按钮累计点击次数，用于监听按钮点击行为
     * 默认值：`0`
     */
    nClicks: PropTypes.number,

    /**
     * 防抖等待时间
     */
    debounceWait: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

MuiButton.defaultProps = {
    color: 'primary',
    disabled: false,
    disableElevation: false,
    disableFocusRipple: false,
    disableRipple: false,
    fullWidth: false,
    size: 'medium',
    variant: 'text',
    nClicks: 0,
    debounceWait: 200
};

export default MuiButton;