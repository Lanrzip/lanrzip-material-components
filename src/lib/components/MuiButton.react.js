import * as React from 'react';
import Button from '@mui/material/Button';
import PropTypes from 'prop-types';

const MuiButton = (props) => {
    let {id, children, variant, nClicks, setProps} = props;

    const onClick = (run) => {
        setProps({nClicks: nClicks + 1});
    };


    const renderElement = (
        <Button
            id={id}
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
     * 组件型，按钮内嵌元素
      */
    children: PropTypes.node,

    /**
     * 组件样式
      */
    variant: PropTypes.oneOf(['text', 'outlined', 'contained', 'string']),

    /**
     * 按钮累计点击次数，用于监听按钮点击行为
     * 默认值：`0`
     */
    nClicks: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

MuiButton.defaultProps = {
    variant: 'contained',
    children: '按钮',
    nClicks: 0
};

export default MuiButton;